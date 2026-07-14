# NI DOCUMENT BUNDLE: rfmxwcdma-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwcdma-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes.html language=enus -->
## TOPIC 00001: Attributes

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPAdvancedCarrierCDACHPModAccOBWQEVMSEMSlotPhaseSlotPowerTriggerGroup membersNameDescriptionRFMXWCDMA_ATTR_BANDSpecifies the Universal Mobile Telecommunications System (UMTS) operation band. RFMXWCDMA_ATTR_CENTER_FREQUENCYFor a single-carrier measurement, this attribute specifies the center f

### Attributes

#### Groups

- ACP
- Advanced
- Carrier
- CDA
- CHP
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
| RFMXWCDMA_ATTR_BAND | Specifies the Universal Mobile Telecommunications System (UMTS) operation band. |
| RFMXWCDMA_ATTR_CENTER_FREQUENCY | For a single-carrier measurement, this attribute specifies the center frequency of the acquired RF signal. |
| RFMXWCDMA_ATTR_EXTERNAL_ATTENUATION | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
| RFMXWCDMA_ATTR_LINK_DIRECTION | Specifies the link direction of the units under test. |
| RFMXWCDMA_ATTR_REFERENCE_LEVEL | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| RFMXWCDMA_ATTR_REFERENCE_LEVEL_HEADROOM | Specifies the margin RFmx adds to the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| RFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUT | Specifies the time to wait before results are available in the RFmxWCDMA Attribute. |
| RFMXWCDMA_ATTR_SELECTED_PORTS | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |

#### Attachments

None

Parent topic:

niRFmxWCDMA.h

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga152b396daf67b26ba9af435208faaf74.html language=enus -->
## TOPIC 00002: RFMXWCDMA_ATTR_SELECTED_PORTS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga152b396daf67b26ba9af435208faaf74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga152b396daf67b26ba9af435208faaf74.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. SyntaxRFMXWCDMA_ATTR_SELECTED_PORTSNumeric ValueData TypeAccessApplies To5246973char[]Read/WriteN/ARemarks You do not need to use a selector string to configure o

### RFMXWCDMA_ATTR_SELECTED_PORTS

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr_GetAvailablePorts](/csh?context=rfmxinstr_rfmxinstrcref_function_get_available_ports) function to get the valid port names.

#### Syntax

RFMXWCDMA_ATTR_SELECTED_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246973 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

**Valid values**

| Name (value) | Description |
| --- | --- |
| PXIe-5830 | if0, if1 |
| PXIe-5831/5832 | if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel |
| Other devices | "" (empty string) |

**Default values**

| Name (value) | Description |
| --- | --- |
| PXIe-5830/5831/5832 | if1 |
| Other devices | "" (empty string) |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga192a2f8b7bb8cf43610b6c802dfb97e3.html language=enus -->
## TOPIC 00003: RFMXWCDMA_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga192a2f8b7bb8cf43610b6c802dfb97e3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga192a2f8b7bb8cf43610b6c802dfb97e3.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxRFMXWCDMA_ATTR_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To5242882float64Read/WriteN/ARemarks You do not ne

### RFMXWCDMA_ATTR_REFERENCE_LEVEL

Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

RFMXWCDMA_ATTR_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242882 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga36dc67f834e7bae8ff27f3b32d1b4d29.html language=enus -->
## TOPIC 00004: RFMXWCDMA_ATTR_LINK_DIRECTION

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga36dc67f834e7bae8ff27f3b32d1b4d29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga36dc67f834e7bae8ff27f3b32d1b4d29.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the link direction of the units under test. SyntaxRFMXWCDMA_ATTR_LINK_DIRECTIONNumeric ValueData TypeAccessApplies To5242893int32Read/WriteN/ARemarks The unit under test is either the base station or the user equipment.You do not need to use a selector string to configure or read this attr

### RFMXWCDMA_ATTR_LINK_DIRECTION

Specifies the link direction of the units under test.

#### Syntax

RFMXWCDMA_ATTR_LINK_DIRECTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242893 | int32 | Read/Write | N/A |

#### Remarks

The unit under test is either the base station or the user equipment.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Uplink**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_LINK_DIRECTION_DOWNLINK | 0 (0x0) | The link is from the base transceiver station to the user equipment. |
| RFMXWCDMA_VAL_LINK_DIRECTION_UPLINK | 1 (0x1) | The link is from the user equipment to the base transceiver station. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga5c17896916c08e5a7d8739cd68357001.html language=enus -->
## TOPIC 00005: RFMXWCDMA_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga5c17896916c08e5a7d8739cd68357001.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga5c17896916c08e5a7d8739cd68357001.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin RFmx adds to the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxRFMXWCDMA_ATTR_REFERENCE_LEVEL_HEADROOMNumeric ValueData TypeAccessApplies To5246972float64Read/WriteN/AR

### RFMXWCDMA_ATTR_REFERENCE_LEVEL_HEADROOM

Specifies the margin RFmx adds to the [RFMXWCDMA_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga192a2f8b7bb8cf43610b6c802dfb97e3.html) attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

RFMXWCDMA_ATTR_REFERENCE_LEVEL_HEADROOM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246972 | float64 | Read/Write | N/A |

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

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes_1gaa75db9abfa121e1a8a2ddcc72f855976.html language=enus -->
## TOPIC 00006: RFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes_1gaa75db9abfa121e1a8a2ddcc72f855976.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes_1gaa75db9abfa121e1a8a2ddcc72f855976.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxWCDMA Attribute. SyntaxRFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUTNumeric ValueData TypeAccessApplies To5292032float64Read/WriteN/ARemarks This value is expressed in seconds.Set this value to a time longer than expected for fetching the meas

### RFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUT

Specifies the time to wait before results are available in the RFmxWCDMA Attribute.

#### Syntax

RFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5292032 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in seconds.

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWCDMA Attribute waits until the measurement is complete.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes_1gabfed4607523c2852023190b88efd267c.html language=enus -->
## TOPIC 00007: RFMXWCDMA_ATTR_CENTER_FREQUENCY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes_1gabfed4607523c2852023190b88efd267c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes_1gabfed4607523c2852023190b88efd267c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For a single-carrier measurement, this attribute specifies the center frequency of the acquired RF signal. SyntaxRFMXWCDMA_ATTR_CENTER_FREQUENCYNumeric ValueData TypeAccessApplies To5242881float64Read/WriteN/ARemarks For multi-carrier measurements, this attribute specifies the reference frequency fo

### RFMXWCDMA_ATTR_CENTER_FREQUENCY

For a single-carrier measurement, this attribute specifies the center frequency of the acquired RF signal.

#### Syntax

RFMXWCDMA_ATTR_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242881 | float64 | Read/Write | N/A |

#### Remarks

For multi-carrier measurements, this attribute specifies the reference frequency for the values in the [RFMXWCDMA_ATTR_CARRIER_FREQUENCY](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1gacfc638beac56d7c91cb233c418af971f.html) attribute.

This value is expressed in Hz.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value this attribute is hardware dependent.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga5e37bcbe3f7b9fce1dd84745e6752a30.html language=enus -->
## TOPIC 00008: RFMXWCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga5e37bcbe3f7b9fce1dd84745e6752a30.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga5e37bcbe3f7b9fce1dd84745e6752a30.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. SyntaxRFMXWCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To5247008int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read

### RFMXWCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

RFMXWCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247008 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| RFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured.Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832/5842/5860 |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga64e47ab85f65bd35398dfcf8f6f7aace.html language=enus -->
## TOPIC 00009: RFMXWCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga64e47ab85f65bd35398dfcf8f6f7aace.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga64e47ab85f65bd35398dfcf8f6f7aace.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the ACP measurement. SyntaxRFMXWCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To5246996int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXWCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the ACP measurement.

#### Syntax

RFMXWCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246996 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga72fea005bca43753027a5ff569afe49c.html language=enus -->
## TOPIC 00010: RFMXWCDMA_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga72fea005bca43753027a5ff569afe49c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga72fea005bca43753027a5ff569afe49c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation function to configure the external attenuation table. SyntaxRFMXWCDMA_A

### RFMXWCDMA_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXWCDMA_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247032 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXWCDMA_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1gaf94e5e030c9242bc237f04f2f47b62d6.html language=enus -->
## TOPIC 00011: RFMXWCDMA_ATTR_ACP_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1gaf94e5e030c9242bc237f04f2f47b62d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1gaf94e5e030c9242bc237f04f2f47b62d6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ACP measurement. SyntaxRFMXWCDMA_ATTR_ACP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5246976int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Stri

### RFMXWCDMA_ATTR_ACP_MEASUREMENT_ENABLED

Specifies whether to enable the ACP measurement.

#### Syntax

RFMXWCDMA_ATTR_ACP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246976 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced.html language=enus -->
## TOPIC 00012: Advanced

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSETSpecifies the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. RFMXWCDMA_ATTR_ACP_IF_OU

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET | Specifies the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. |
| RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. |
| RFMXWCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET | Specifies the power offset to use to adjust the IF output power level for offset channels near the carrier channel. Adjusting the IF output power level improves the dynamic range. |
| RFMXWCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE | Specifies the number of bins to use for FFT computation when the RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD attribute is set to Sequential FFT. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga39331363f36500215956783536a1da6a.html language=enus -->
## TOPIC 00013: RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga39331363f36500215956783536a1da6a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga39331363f36500215956783536a1da6a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. SyntaxRFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTONumeric ValueData TypeAccessApplies To5247028int32Read/WriteN/ARemarks You do not need to use a

### RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement.

#### Syntax

RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247028 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

This attribute is used only if you set the [RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga80ab80f99769a630cc18af0a21176cc9.html) attribute to **Dynamic Range**. The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE | 0 (0x0) | The measurement sets the IF output power level offset using the values of the RFMXWCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET and RFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET attributes. |
| RFMXWCDMA_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE | 1 (0x1) | The measurement automatically computes an IF output power level offset for the offset channels. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga8567086103306f99581247ea14a38ca1.html language=enus -->
## TOPIC 00014: RFMXWCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga8567086103306f99581247ea14a38ca1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga8567086103306f99581247ea14a38ca1.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of bins to use for FFT computation when the RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD attribute is set to Sequential FFT. SyntaxRFMXWCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZENumeric ValueData TypeAccessApplies To5247033int32Read/WriteN/ARemarks You do not need to use a selector string to co

### RFMXWCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE

Specifies the number of bins to use for FFT computation when the [RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga80ab80f99769a630cc18af0a21176cc9.html) attribute is set to **Sequential FFT**.

#### Syntax

RFMXWCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247033 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 512.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga96825704aa3947636d7ea5d2278bd7d7.html language=enus -->
## TOPIC 00015: RFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga96825704aa3947636d7ea5d2278bd7d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga96825704aa3947636d7ea5d2278bd7d7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range. SyntaxRFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSETNumeric ValueData TypeAccessApplies To5247030float64Read

### RFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET

Specifies the power offset to use to adjust the IF output power level for offset channels that are far from the carrier channel. Adjusting the IF output power level improves the dynamic range.

#### Syntax

RFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247030 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in dB.

This attribute is used only if you set the [RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga80ab80f99769a630cc18af0a21176cc9.html) attribute to **Dynamic Range** and set the [RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga39331363f36500215956783536a1da6a.html) attribute to **False**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 20.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1gaee724ef718d32b85a45e99dbb18b7ce8.html language=enus -->
## TOPIC 00016: RFMXWCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1gaee724ef718d32b85a45e99dbb18b7ce8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1gaee724ef718d32b85a45e99dbb18b7ce8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power offset to use to adjust the IF output power level for offset channels near the carrier channel. Adjusting the IF output power level improves the dynamic range. SyntaxRFMXWCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSETNumeric ValueData TypeAccessApplies To5247029float64Read/WriteN/ARem

### RFMXWCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

Specifies the power offset to use to adjust the IF output power level for offset channels near the carrier channel. Adjusting the IF output power level improves the dynamic range.

#### Syntax

RFMXWCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247029 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in dB.

This attribute is used only if you set the [RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp_1ga80ab80f99769a630cc18af0a21176cc9.html) attribute to **Dynamic Range** and set the [RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__advanced_1ga39331363f36500215956783536a1da6a.html) attribute to **False**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging.html language=enus -->
## TOPIC 00017: Averaging

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED to True. RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLEDSpecifies whether to enable averaging for the ACP measurement. RFMXWCDMA_

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED to True. |
| RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED | Specifies whether to enable averaging for the ACP measurement. |
| RFMXWCDMA_ATTR_ACP_AVERAGING_TYPE | Specifies the averaging type for averaging the spectrum of multiple acquisitions. The averaged spectrum is used for ACP measurement. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging_1ga0bb51844d9fa1f68b39b21bf0e01c579.html language=enus -->
## TOPIC 00018: RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging_1ga0bb51844d9fa1f68b39b21bf0e01c579.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging_1ga0bb51844d9fa1f68b39b21bf0e01c579.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the ACP measurement. SyntaxRFMXWCDMA_ATTR_ACP_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To5246998int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the S

### RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED

Specifies whether to enable averaging for the ACP measurement.

#### Syntax

RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246998 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The ACP measurement uses the value of the RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT attribute as the number of acquisitions over which the ACP measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging_1ga337d12cd7b88e97d0c88e52671a69d33.html language=enus -->
## TOPIC 00019: RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging_1ga337d12cd7b88e97d0c88e52671a69d33.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging_1ga337d12cd7b88e97d0c88e52671a69d33.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED to True. SyntaxRFMXWCDMA_ATTR_ACP_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To5246997int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this att

### RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__averaging_1ga0bb51844d9fa1f68b39b21bf0e01c579.html) to **True**.

#### Syntax

RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246997 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__carrier.html language=enus -->
## TOPIC 00020: Carrier

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__carrier.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTHReturns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH | Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__carrier_1ga99d65c7d5899ddbfb7641f6a69b73034.html language=enus -->
## TOPIC 00021: RFMXWCDMA_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__carrier_1ga99d65c7d5899ddbfb7641f6a69b73034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__carrier_1ga99d65c7d5899ddbfb7641f6a69b73034.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To5246981float64Read-OnlyCarrierRemarks Use "carrier<n>" as the selector string to read this a

### RFMXWCDMA_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246981 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__fft.html language=enus -->
## TOPIC 00022: FFT

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__fft.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_FFT_OVERLAPReturns the number of samples to overlap between consecutive chunks while performing FFT. RFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODESpecifies how overlapping is applied when computing the FFT of the acquired samples. AttachmentsNone

### FFT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_FFT_OVERLAP | Returns the number of samples to overlap between consecutive chunks while performing FFT. |
| RFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODE | Specifies how overlapping is applied when computing the FFT of the acquired samples. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__fft_1gabec92c99c217667ac86d20b76c653e10.html language=enus -->
## TOPIC 00023: RFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__fft_1gabec92c99c217667ac86d20b76c653e10.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__fft_1gabec92c99c217667ac86d20b76c653e10.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how overlapping is applied when computing the FFT of the acquired samples. SyntaxRFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODENumeric ValueData TypeAccessApplies To5247034int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal ins

### RFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODE

Specifies how overlapping is applied when computing the FFT of the acquired samples.

#### Syntax

RFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247034 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_ACP_FFT_OVERLAP_MODE_DISABLED | 0 (0x0) | Indicates that overlapping is not applied to the acquired samples. |
| RFMXWCDMA_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC | 1 (0x1) | Indicates that the RFmx driver automatically chooses optimal values of the RFMXWCDMA_ATTR_ACP_FFT_OVERLAP attribute based on the measurement configuration. |

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset.html language=enus -->
## TOPIC 00024: Offset

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPower ReferenceGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_NUMBER_OF_OFFSETSSpecifies the number of offset channels. RFMXWCDMA_ATTR_ACP_OFFSET_FREQUENCYReturns the center frequency of the offset channel, relative to the center frequency of the carrier(s). This value is expressed in Hz. RFMX

### Offset

#### Groups

- Power Reference

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_NUMBER_OF_OFFSETS | Specifies the number of offset channels. |
| RFMXWCDMA_ATTR_ACP_OFFSET_FREQUENCY | Returns the center frequency of the offset channel, relative to the center frequency of the carrier(s). This value is expressed in Hz. |
| RFMXWCDMA_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH | Returns the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset_1ga252f6cbaa8eaff2585c5ebcbc30501a7.html language=enus -->
## TOPIC 00025: RFMXWCDMA_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset_1ga252f6cbaa8eaff2585c5ebcbc30501a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset_1ga252f6cbaa8eaff2585c5ebcbc30501a7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To5246990float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to read t

### RFMXWCDMA_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

Returns the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246990 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this attribute.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__rbw__filter_1gadd3da3644631a059f6328f83757a55b7.html language=enus -->
## TOPIC 00026: RFMXWCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__rbw__filter_1gadd3da3644631a059f6328f83757a55b7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__rbw__filter_1gadd3da3644631a059f6328f83757a55b7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxRFMXWCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To5247003int32Read/WriteN/ARemarks This attribute is valid only if you set the RFMXWCDMA_ATTR_ACP_RBW_FILTER_TYPE attribute to Gaussian or Flat.If you set the ACP

### RFMXWCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the RBW.

#### Syntax

RFMXWCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247003 | int32 | Read/Write | N/A |

#### Remarks

This attribute is valid only if you set the [RFMXWCDMA_ATTR_ACP_RBW_FILTER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__rbw__filter_1ga95e9d08f9f45bca24c2ee1383c709750.html) attribute to **Gaussian** or **Flat**.

If you set the ACP RBW Filter Type attribute to **FFT Based**, the measurement calculates the RBW regardless of the value of this attribute.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_ACP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXWCDMA_VAL_ACP_RBW_AUTO_TRUE | 1 (0x1) | The measurement calculates the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results_1ga9e4694952f484cdb0511a76bc81c87cb.html language=enus -->
## TOPIC 00027: RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results_1ga9e4694952f484cdb0511a76bc81c87cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results_1ga9e4694952f484cdb0511a76bc81c87cb.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER attribute. For a single-carrier measurement, total carrier power is the same as carrier absolute power. SyntaxRFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARR

### RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the [RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__carrier_1ga5a48dfbb77dcceb469fe7f2f8be62aca.html) attribute. For a single-carrier measurement, total carrier power is the same as carrier absolute power.

#### Syntax

RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247010 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__carrier.html language=enus -->
## TOPIC 00028: Carrier

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__carrier.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWERReturns the carrier power. RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWERReturns the carrier power relative to the RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER | Returns the carrier power. |
| RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER | Returns the carrier power relative to the RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__carrier_1ga5a48dfbb77dcceb469fe7f2f8be62aca.html language=enus -->
## TOPIC 00029: RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__carrier_1ga5a48dfbb77dcceb469fe7f2f8be62aca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__carrier_1ga5a48dfbb77dcceb469fe7f2f8be62aca.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power. SyntaxRFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To5247014float64Read-OnlyCarrierRemarks This value is expressed in dBm.The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 M

### RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

Returns the carrier power.

#### Syntax

RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247014 | float64 | Read-Only | Carrier |

#### Remarks

This value is expressed in dBm.

The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the [RFMXWCDMA_ATTR_CENTER_FREQUENCY](group____root__ni_r_fmx_w_c_d_m_a__attributes_1gabfed4607523c2852023190b88efd267c.html) and [RFMXWCDMA_ATTR_CARRIER_FREQUENCY](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1gacfc638beac56d7c91cb233c418af971f.html) attributes.

Use "carrier<k>" as the selector string to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__lower__offset.html language=enus -->
## TOPIC 00030: Lower Offset

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__lower__offset.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERReturns the lower offset channel power. RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWERReturns the lower offset channel power relative to the power of the carrier(s) that you specify in the RFMXWCDMA_A

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER | Returns the lower offset channel power. |
| RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER | Returns the lower offset channel power relative to the power of the carrier(s) that you specify in the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__lower__offset_1ga4d5f65e743cfe80788e9a05b824eafa8.html language=enus -->
## TOPIC 00031: RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__lower__offset_1ga4d5f65e743cfe80788e9a05b824eafa8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__lower__offset_1ga4d5f65e743cfe80788e9a05b824eafa8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset channel power. SyntaxRFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To5247020float64Read-OnlyOffsetRemarks This value is expressed in dBm.The lower offset channel power is the integrated power of the RRC-filtered signal at the lower

### RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

Returns the lower offset channel power.

#### Syntax

RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247020 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dBm.

The lower offset channel power is the integrated power of the RRC-filtered signal at the lower offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__upper__offset.html language=enus -->
## TOPIC 00032: Upper Offset

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__upper__offset.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWERReturns the upper offset channel power. RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWERReturns the upper offset channel power relative to the power of the carrier(s) that you specify in the RFMXWCDMA_A

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER | Returns the upper offset channel power. |
| RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER | Returns the upper offset channel power relative to the power of the carrier(s) that you specify in the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__upper__offset_1ga4973486b77f47d1c28eed52eb5a14745.html language=enus -->
## TOPIC 00033: RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__upper__offset_1ga4973486b77f47d1c28eed52eb5a14745.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results__upper__offset_1ga4973486b77f47d1c28eed52eb5a14745.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset channel power relative to the power of the carrier(s) that you specify in the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. SyntaxRFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWERNumeric ValueData TypeAccessApplies To5247027float64Read-OnlyOffsetRemarks T

### RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

Returns the upper offset channel power relative to the power of the carrier(s) that you specify in the [RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset__power__reference_1ga8c650634e5720b37039a2af0c4d66a8e.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247027 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dB.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__sweep__time_1ga52d5c2b1332338a0ef1614a3c2d616b9.html language=enus -->
## TOPIC 00034: RFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__sweep__time_1ga52d5c2b1332338a0ef1614a3c2d616b9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__sweep__time_1ga52d5c2b1332338a0ef1614a3c2d616b9.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXWCDMA_ATTR_ACP_SWEEP_TIME_AUTO attribute to False. SyntaxRFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To5247007float64Read/WriteN/ARemarks This value is expressed in seconds.You do not need to use a selector string to configu

### RFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXWCDMA_ATTR_ACP_SWEEP_TIME_AUTO](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__sweep__time_1gac8c15e0fe6a5809fb5df70694021a550.html) attribute to **False**.

#### Syntax

RFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5247007 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier.html language=enus -->
## TOPIC 00035: Carrier

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsChannelScramblingGroup membersNameDescriptionRFMXWCDMA_ATTR_CARRIER_FREQUENCYSpecifies the center frequency of the carrier, relative to the RF RFMXWCDMA_ATTR_CENTER_FREQUENCY. RFMXWCDMA_ATTR_NUMBER_OF_CARRIERSSpecifies the number of carriers. AttachmentsNone

### Carrier

#### Groups

- Channel
- Scrambling

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_CARRIER_FREQUENCY | Specifies the center frequency of the carrier, relative to the RF RFMXWCDMA_ATTR_CENTER_FREQUENCY. |
| RFMXWCDMA_ATTR_NUMBER_OF_CARRIERS | Specifies the number of carriers. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1ga02230e930e6a26c73d04eaef7f404035.html language=enus -->
## TOPIC 00036: RFMXWCDMA_ATTR_NUMBER_OF_CARRIERS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1ga02230e930e6a26c73d04eaef7f404035.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1ga02230e930e6a26c73d04eaef7f404035.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of carriers. SyntaxRFMXWCDMA_ATTR_NUMBER_OF_CARRIERSNumeric ValueData TypeAccessApplies To5242894int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for informa

### RFMXWCDMA_ATTR_NUMBER_OF_CARRIERS

Specifies the number of carriers.

#### Syntax

RFMXWCDMA_ATTR_NUMBER_OF_CARRIERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242894 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1gacfc638beac56d7c91cb233c418af971f.html language=enus -->
## TOPIC 00037: RFMXWCDMA_ATTR_CARRIER_FREQUENCY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1gacfc638beac56d7c91cb233c418af971f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1gacfc638beac56d7c91cb233c418af971f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the center frequency of the carrier, relative to the RF RFMXWCDMA_ATTR_CENTER_FREQUENCY. SyntaxRFMXWCDMA_ATTR_CARRIER_FREQUENCYNumeric ValueData TypeAccessApplies To5242895float64Read/WriteCarrierRemarks This value is expressed in Hz.Use "carrier<k>" as the selector string to configure or

### RFMXWCDMA_ATTR_CARRIER_FREQUENCY

Specifies the center frequency of the carrier, relative to the RF [RFMXWCDMA_ATTR_CENTER_FREQUENCY](group____root__ni_r_fmx_w_c_d_m_a__attributes_1gabfed4607523c2852023190b88efd267c.html).

#### Syntax

RFMXWCDMA_ATTR_CARRIER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242895 | float64 | Read/Write | Carrier |

#### Remarks

This value is expressed in Hz.

Use "carrier<k>" as the selector string to configure or read this attribute.

The default value is 0.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel.html language=enus -->
## TOPIC 00038: Channel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsUser DefinedGroup membersNameDescriptionRFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODESpecifies the channel configuration mode. RFMXWCDMA_ATTR_DOWNLINK_TEST_MODELSpecifies the symbol boundary synchronization method. RFMXWCDMA_ATTR_UPLINK_TEST_MODELSpecifies the uplink test model when the user sets

### Channel

#### Groups

- User Defined

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE | Specifies the channel configuration mode. |
| RFMXWCDMA_ATTR_DOWNLINK_TEST_MODEL | Specifies the symbol boundary synchronization method. |
| RFMXWCDMA_ATTR_UPLINK_TEST_MODEL | Specifies the uplink test model when the user sets the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Test Model. |

#### Attachments

None

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga1a0ff4a6266a3df664dd3dd15ff8ae4b.html language=enus -->
## TOPIC 00039: RFMXWCDMA_ATTR_DOWNLINK_TEST_MODEL

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga1a0ff4a6266a3df664dd3dd15ff8ae4b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga1a0ff4a6266a3df664dd3dd15ff8ae4b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the symbol boundary synchronization method. SyntaxRFMXWCDMA_ATTR_DOWNLINK_TEST_MODELNumeric ValueData TypeAccessApplies To5242906int32Read/WriteCarrierRemarks Use "carrier<n>" as the selector string to configure or read this attribute.NameValueDescriptionRFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_T

### RFMXWCDMA_ATTR_DOWNLINK_TEST_MODEL

Specifies the symbol boundary synchronization method.

#### Syntax

RFMXWCDMA_ATTR_DOWNLINK_TEST_MODEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242906 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the selector string to configure or read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_16DPCH | 0 (0x0) | Test Model 1 with 16 DPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_32DPCH | 1 (0x1) | Test Model 1 with 32 DPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_64DPCH | 2 (0x2) | Test Mode 1 with 64 DPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_16DPCH_SCCPCH | 3 (0x3) | Test Model 1 with 16 DPCH and S-CCPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_32DPCH_SCCPCH | 4 (0x4) | Test Model 1 with 32 DPCH and S-CCPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_64DPCH_SCCPCH | 5 (0x5) | Test Model 1 with 64 DPCH and S-CCPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_2 | 6 (0x6) | Test Model 2 is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_2_SCCPCH | 7 (0x7) | Test Model 2 with a S-CCPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_16DPCH | 8 (0x8) | Test Mode 3 with 16 DPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_32DPCH | 9 (0x9) | Test Mode 3 with 32 DPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_16DPCH_SCCPCH | 10 (0xa) | Test Model 3 with 16 DPCH/S-CCPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_32DPCH_SCCPCH | 11 (0xb) | Test Model 3 with 16 DPCH/S-CCPCH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_4 | 12 (0xc) | Test Model 4 is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_4_PCPICH | 13 (0xd) | Test Model 4 with P-CPICH is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_2HSPDSCH_16QAM | 14 (0xe) | Test Model 5 with 2 HS-PDSCH [16QAM] is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_4HSPDSCH_4DPCH_16QAM | 15 (0xf) | Test Model 5 with 4 HS-PDSCH / 4DPCH [16QAM] is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_4HSPDSCH_14DPCH_16QAM | 16 (0x10) | Test Model 5 with 4 HS-PDSCH / 14DPCH [16QAM] is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_8HSPDSCH_16QAM | 17 (0x11) | Test Model 5 with 8 HS-PDSCH [16QAM] is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_6_4HSPDSCH_64QAM | 18 (0x12) | Test Model 6 with 4 HS-PDSCH [64QAM] is used for synchronization. |
| RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_6_8HSPDSCH_64QAM | 19 (0x13) | Test Model 6 with 8 HS-PDSCH [64QAM] is used for synchronization. |

Parent topic:

Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html language=enus -->
## TOPIC 00040: RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel configuration mode. SyntaxRFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODENumeric ValueData TypeAccessApplies To5242896int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String t

### RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

Specifies the channel configuration mode.

#### Syntax

RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242896 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT | 0 (0x0) | The measurement detects the channels. |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED | 1 (0x1) | Configure the channels using the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute and the RFmxWCDMA_CfgUserDefinedChannelArray function. |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL | 2 (0x2) | Choose from the standard-defined channel configurations using the RFMXWCDMA_ATTR_UPLINK_TEST_MODEL attribute. |

Parent topic:

Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel__user__defined_1ga0fbd050cdb574a70cd47e0c92b4cd1a4.html language=enus -->
## TOPIC 00041: RFMXWCDMA_ATTR_MODULATION_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel__user__defined_1ga0fbd050cdb574a70cd47e0c92b4cd1a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel__user__defined_1ga0fbd050cdb574a70cd47e0c92b4cd1a4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation type for the channel. SyntaxRFMXWCDMA_ATTR_MODULATION_TYPENumeric ValueData TypeAccessApplies To5242903int32Read/WriteChannelRemarks Use "carrier<n>/channel<k>" as the selector string to configure or read this attribute.The default value is BPSK/QPSK.NameValueDescriptionRFMX

### RFMXWCDMA_ATTR_MODULATION_TYPE

Specifies the modulation type for the channel.

#### Syntax

RFMXWCDMA_ATTR_MODULATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242903 | int32 | Read/Write | Channel |

#### Remarks

Use "carrier<n>/channel<k>" as the selector string to configure or read this attribute.

The default value is **BPSK/QPSK**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODULATION_TYPE_BPSK_QPSK | 0 (0x0) | The modulation type is BPSK. |
| RFMXWCDMA_VAL_MODULATION_TYPE_4PAM_16QAM | 1 (0x1) | The modulation type is 4-PAM. |
| RFMXWCDMA_VAL_MODULATION_TYPE_64QAM | 2 (0x2) | The modulation type is 64-QAM. |

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink.html language=enus -->
## TOPIC 00042: Downlink

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_PRIMARY_CODESpecifies the primary scrambling code. RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_SECONDARY_CODESpecifies the secondary scrambling code. RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_TYPESpecifies the scrambling code type. Attachments

### Downlink

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_PRIMARY_CODE | Specifies the primary scrambling code. |
| RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_SECONDARY_CODE | Specifies the secondary scrambling code. |
| RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_TYPE | Specifies the scrambling code type. |

#### Attachments

None

Parent topic:

Scrambling

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink_1ga270e052fd2af3b7c5dcf3db1fc74b157.html language=enus -->
## TOPIC 00043: RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_PRIMARY_CODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink_1ga270e052fd2af3b7c5dcf3db1fc74b157.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink_1ga270e052fd2af3b7c5dcf3db1fc74b157.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the primary scrambling code. SyntaxRFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_PRIMARY_CODENumeric ValueData TypeAccessApplies To5242910int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Strin

### RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_PRIMARY_CODE

Specifies the primary scrambling code.

#### Syntax

RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_PRIMARY_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242910 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink_1gaf3ed33dbcfa1d7d74c720c81419e1426.html language=enus -->
## TOPIC 00044: RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_SECONDARY_CODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink_1gaf3ed33dbcfa1d7d74c720c81419e1426.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__downlink_1gaf3ed33dbcfa1d7d74c720c81419e1426.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the secondary scrambling code. SyntaxRFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_SECONDARY_CODENumeric ValueData TypeAccessApplies To5242911int32Read/WriteN/ARemarks Use "carrier<n>" as the selector string to configure or read this attribute.

### RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_SECONDARY_CODE

Specifies the secondary scrambling code.

#### Syntax

RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_SECONDARY_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242911 | int32 | Read/Write | N/A |

#### Remarks

Use "carrier<n>" as the selector string to configure or read this attribute.

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__uplink.html language=enus -->
## TOPIC 00045: Uplink

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__uplink.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__scrambling__uplink.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_UPLINK_SCRAMBLING_CODESpecifies the scrambling code for the uplink channel. RFMXWCDMA_ATTR_UPLINK_SCRAMBLING_TYPESpecifies the type of scrambling to use for the measurement. AttachmentsNone

### Uplink

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_UPLINK_SCRAMBLING_CODE | Specifies the scrambling code for the uplink channel. |
| RFMXWCDMA_ATTR_UPLINK_SCRAMBLING_TYPE | Specifies the type of scrambling to use for the measurement. |

#### Attachments

None

Parent topic:

Scrambling

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga116333ed0c89d5d7caf14985e68c41a7.html language=enus -->
## TOPIC 00046: RFMXWCDMA_ATTR_CDA_SPECTRUM_INVERTED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga116333ed0c89d5d7caf14985e68c41a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga116333ed0c89d5d7caf14985e68c41a7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxRFMXWCDMA_ATTR_CDA_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To5328901int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXWCDMA_ATTR_CDA_SPECTRUM_INVERTED

Specifies whether the spectrum of the signal is inverted.

#### Syntax

RFMXWCDMA_ATTR_CDA_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328901 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_CDA_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The spectrum is not inverted. |
| RFMXWCDMA_VAL_CDA_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The spectrum is inverted. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga65dba037bb7e82e5e0b0484755a292ce.html language=enus -->
## TOPIC 00047: RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga65dba037bb7e82e5e0b0484755a292ce.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga65dba037bb7e82e5e0b0484755a292ce.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXWCDMA_ATTR_CDA_SYNCHRONIZATION_MODE attribute. SyntaxRFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To5328899in

### RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [RFMXWCDMA_ATTR_CDA_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1gafac686ea3421e362d8ec807ca9704fe5.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328899 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0, (15 - [RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH](group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga93ca287a28d4dedbe6bcb9854344f0a1.html))]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga72c5c3ba9ebd66bf9c7dcb612b2d3650.html language=enus -->
## TOPIC 00048: RFMXWCDMA_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga72c5c3ba9ebd66bf9c7dcb612b2d3650.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga72c5c3ba9ebd66bf9c7dcb612b2d3650.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the CDA measurement. SyntaxRFMXWCDMA_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To5328902int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance

### RFMXWCDMA_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED

Specifies whether to remove the I/Q offset before the CDA measurement.

#### Syntax

RFMXWCDMA_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328902 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q offset is not removed before the CDA measurement. |
| RFMXWCDMA_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q offset is removed before the CDA measurement. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga93ca287a28d4dedbe6bcb9854344f0a1.html language=enus -->
## TOPIC 00049: RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga93ca287a28d4dedbe6bcb9854344f0a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga93ca287a28d4dedbe6bcb9854344f0a1.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the code domain measurement. This value is expressed in slots. SyntaxRFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To5328900int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default sign

### RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH

Specifies the duration of the code domain measurement. This value is expressed in slots.

#### Syntax

RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328900 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1. Valid values are [1, (15 - [RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET](group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1ga65dba037bb7e82e5e0b0484755a292ce.html))]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1gafe4a9f735945bf4f97ae63ed0cf7cf59.html language=enus -->
## TOPIC 00050: RFMXWCDMA_ATTR_CDA_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1gafe4a9f735945bf4f97ae63ed0cf7cf59.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda_1gafe4a9f735945bf4f97ae63ed0cf7cf59.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the CDA measurement. SyntaxRFMXWCDMA_ATTR_CDA_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5328896int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Stri

### RFMXWCDMA_ATTR_CDA_MEASUREMENT_ENABLED

Specifies whether to enable the CDA measurement.

#### Syntax

RFMXWCDMA_ATTR_CDA_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328896 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__measurement__channel_1ga9238d719475e4b9e2406477657766182.html language=enus -->
## TOPIC 00051: RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__measurement__channel_1ga9238d719475e4b9e2406477657766182.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__measurement__channel_1ga9238d719475e4b9e2406477657766182.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement. SyntaxRFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_FACTORNumeric ValueData TypeAccessApplies To5328905int32Read/WriteN/ARemarks You do not need to use a selector st

### RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR

Specifies the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

#### Syntax

RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328905 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 256. Valid values are 2, 4, 8, 16, 32, 64, 128, and 256.

Parent topic:

Measurement Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__measurement__channel_1gaaf2b9459e47cc88f70206d5107365e8c.html language=enus -->
## TOPIC 00052: RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_CODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__measurement__channel_1gaaf2b9459e47cc88f70206d5107365e8c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__measurement__channel_1gaaf2b9459e47cc88f70206d5107365e8c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spreading code of the measurement channel. This value is used to compute the symbol results of the CDA measurement. SyntaxRFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_CODENumeric ValueData TypeAccessApplies To5328906int32Read/WriteN/ARemarks You do not need to use a selector string

### RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_CODE

Specifies the spreading code of the measurement channel. This value is used to compute the symbol results of the CDA measurement.

#### Syntax

RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328906 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. Valid values are 0 to ([RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR](group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__measurement__channel_1ga9238d719475e4b9e2406477657766182.html) - 1).

Parent topic:

Measurement Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__results.html language=enus -->
## TOPIC 00053: Results

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__results.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_CDA_RESULTS_CHIP_RATE_ERRORReturns the chip rate error of the composite signal. This value is expressed in ppm. RFMXWCDMA_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWERReturns the average code power among the set of active in-phase channels in the code doma

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_CDA_RESULTS_CHIP_RATE_ERROR | Returns the chip rate error of the composite signal. This value is expressed in ppm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER | Returns the average code power among the set of active in-phase channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER | Returns the largest code power among the set of inactive in-phase channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER | Returns the average of all the active channel powers. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER | Returns the average code power among the set of inactive channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER | Returns the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| RFMXWCDMA_ATTR_CDA_RESULTS_PEAK_ACTIVE_POWER | Returns the largest code power among the set of active channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER | Returns the largest code power among the set of inactive channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVM | Returns the peak EVM for the measurement channel. This value is expressed as a percentage. |
| RFMXWCDMA_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER | Returns the average code power among the set of active quadrature-phase channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_Q_PEAK_INACTIVE_POWER | Returns the largest code power among the set of inactive quadrature-phase channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM | Returns the RMS EVM for the measurement channel. This value is expressed as a percentage. |
| RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR | Returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage. |
| RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_PHASE_ERROR | Returns the RMS phase error for the measurement channel. This value is expressed in degrees. |
| RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_ACTIVE_POWER | Returns the sum of all the active channel powers. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER | Returns the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__results_1gaea08b2e576eeed04456dab408cf5442d.html language=enus -->
## TOPIC 00054: RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__results_1gaea08b2e576eeed04456dab408cf5442d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__cda__results_1gaea08b2e576eeed04456dab408cf5442d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM for the measurement channel. This value is expressed as a percentage. SyntaxRFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_EVMNumeric ValueData TypeAccessApplies To5328919float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for the default signal and res

### RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM

Returns the RMS EVM for the measurement channel. This value is expressed as a percentage.

#### Syntax

RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5328919 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp_1ga742a39cc05938b72bf1506c645db35d5.html language=enus -->
## TOPIC 00055: RFMXWCDMA_ATTR_CHP_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp_1ga742a39cc05938b72bf1506c645db35d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp_1ga742a39cc05938b72bf1506c645db35d5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the CHP measurement. SyntaxRFMXWCDMA_ATTR_CHP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5255168int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Stri

### RFMXWCDMA_ATTR_CHP_MEASUREMENT_ENABLED

Specifies whether to enable the CHP measurement.

#### Syntax

RFMXWCDMA_ATTR_CHP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255168 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp_1gabf8f2f1e38263ee6432cd6182f0963a6.html language=enus -->
## TOPIC 00056: RFMXWCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp_1gabf8f2f1e38263ee6432cd6182f0963a6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp_1gabf8f2f1e38263ee6432cd6182f0963a6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the CHP measurement. SyntaxRFMXWCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To5255171int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of thread

### RFMXWCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the CHP measurement.

#### Syntax

RFMXWCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255171 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__averaging_1ga211d38366754fd37ec77437b69b86749.html language=enus -->
## TOPIC 00057: RFMXWCDMA_ATTR_CHP_AVERAGING_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__averaging_1ga211d38366754fd37ec77437b69b86749.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__averaging_1ga211d38366754fd37ec77437b69b86749.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging the spectrum of multiple acquisitions. SyntaxRFMXWCDMA_ATTR_CHP_AVERAGING_TYPENumeric ValueData TypeAccessApplies To5255177int32Read/WriteN/ARemarks The averaged spectrum is used for CHP measurement.You do not need to use a selector string to configure or r

### RFMXWCDMA_ATTR_CHP_AVERAGING_TYPE

Specifies the averaging type for averaging the spectrum of multiple acquisitions.

#### Syntax

RFMXWCDMA_ATTR_CHP_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255177 | int32 | Read/Write | N/A |

#### Remarks

The averaged spectrum is used for CHP measurement.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

the default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MAX | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MIN | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__averaging_1ga5ed8851a55506c5aa194b18a30324a48.html language=enus -->
## TOPIC 00058: RFMXWCDMA_ATTR_CHP_AVERAGING_COUNT

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__averaging_1ga5ed8851a55506c5aa194b18a30324a48.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__averaging_1ga5ed8851a55506c5aa194b18a30324a48.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_CHP_AVERAGING_ENABLED attribute to True. SyntaxRFMXWCDMA_ATTR_CHP_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To5255174int32Read/WriteN/ARemarks You do not need to use a selector string to configure or rea

### RFMXWCDMA_ATTR_CHP_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXWCDMA_ATTR_CHP_AVERAGING_ENABLED](group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__averaging_1gae88ae2facd6a501c873cfa3a771e64c4.html) attribute to **True**.

#### Syntax

RFMXWCDMA_ATTR_CHP_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255174 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__carrier.html language=enus -->
## TOPIC 00059: Carrier

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__carrier.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTHReturns the frequency range, over which the measurement integrates the power. This value is expressed in Hz. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH | Returns the frequency range, over which the measurement integrates the power. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__carrier_1ga305fa0146a1faef9225448be7145bb4e.html language=enus -->
## TOPIC 00060: RFMXWCDMA_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__carrier_1ga305fa0146a1faef9225448be7145bb4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__carrier_1ga305fa0146a1faef9225448be7145bb4e.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range, over which the measurement integrates the power. This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To5255170float64Read-OnlyCarrierRemarks Use "carrier<n>" as the selector string to read this attribut

### RFMXWCDMA_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

Returns the frequency range, over which the measurement integrates the power. This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255170 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter.html language=enus -->
## TOPIC 00061: RBW Filter

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the RBW. RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the RBW. |
| RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. |
| RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE | Specifies the shape of the digital RBW filter. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga2887f7a8ce860d49d8d1b7a51e6d401f.html language=enus -->
## TOPIC 00062: RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga2887f7a8ce860d49d8d1b7a51e6d401f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga2887f7a8ce860d49d8d1b7a51e6d401f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxRFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To5255180int32Read/WriteN/ARemarks This attribute is valid only if you set the RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE attribute to Gaussian or Flat.If you set the CHP

### RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the RBW.

#### Syntax

RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255180 | int32 | Read/Write | N/A |

#### Remarks

This attribute is valid only if you set the [RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga957a5a9003a1ac904d24b7414f9b61de.html) attribute to **Gaussian** or **Flat**.

If you set the CHP RBW Filter Type attribute to **FFT Based**, the measurement calculates the RBW regardless of what you set in this attribute.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_CHP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXWCDMA_VAL_CHP_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga7137a3daa2a0c1ee250612107fe12ba9.html language=enus -->
## TOPIC 00063: RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga7137a3daa2a0c1ee250612107fe12ba9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga7137a3daa2a0c1ee250612107fe12ba9.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. SyntaxRFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To5255181float64Read/WriteN/ARemarks This attribute is valid

### RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga2887f7a8ce860d49d8d1b7a51e6d401f.html) attribute to **False**.

#### Syntax

RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255181 | float64 | Read/Write | N/A |

#### Remarks

This attribute is valid only if you set the [RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga957a5a9003a1ac904d24b7414f9b61de.html) attribute to **Gaussian** or **Flat**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 50 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga957a5a9003a1ac904d24b7414f9b61de.html language=enus -->
## TOPIC 00064: RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga957a5a9003a1ac904d24b7414f9b61de.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__rbw__filter_1ga957a5a9003a1ac904d24b7414f9b61de.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To5255182int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String top

### RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255182 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **FFT Based**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is applied. |
| RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__results.html language=enus -->
## TOPIC 00065: Results

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__results.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCarrierGroup membersNameDescriptionRFMXWCDMA_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWERReturns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER attribute. For a single-carrier measurement, total carrier p

### Results

#### Groups

- Carrier

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWER | Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER attribute. For a single-carrier measurement, total carrier power is the same as carrier absolute power. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__sweep__time_1ga002e9003804e32ea07902e4c1ecc01a0.html language=enus -->
## TOPIC 00066: RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__sweep__time_1ga002e9003804e32ea07902e4c1ecc01a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__sweep__time_1ga002e9003804e32ea07902e4c1ecc01a0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO attribute to False. SyntaxRFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To5255186float64Read/WriteN/ARemarks This value is expressed in seconds.You do not need to use a selector string to configu

### RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO](group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__sweep__time_1ga9675aaaa74318249ee00a6858c964c12.html) attribute to **False**.

#### Syntax

RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255186 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__sweep__time_1ga9675aaaa74318249ee00a6858c964c12.html language=enus -->
## TOPIC 00067: RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__sweep__time_1ga9675aaaa74318249ee00a6858c964c12.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__chp__sweep__time_1ga9675aaaa74318249ee00a6858c964c12.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To5255185int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5255185 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |
| RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time value of one slot duration. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc.html language=enus -->
## TOPIC 00068: ModAcc

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDownlink Timing ChannelResultsGroup membersNameDescriptionRFMXWCDMA_ATTR_MODACC_ALL_TRACES_ENABLEDSpecifies whether to enable the traces after performing the modulation accuracy (ModAcc) measurement. RFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLEDSpecifies whether to remove I/Q gain im

### ModAcc

#### Groups

- Downlink Timing Channel
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_MODACC_ALL_TRACES_ENABLED | Specifies whether to enable the traces after performing the modulation accuracy (ModAcc) measurement. |
| RFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED | Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement. In case of multi-carrier measurements, this attribute is valid only when you set the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to LO per Carrier. |
| RFMXWCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove the I/Q offset before the ModAcc measurement. |
| RFMXWCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED | Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. In case of multi-carrier measurements, this attribute is valid only when you set the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to LO per Carrier. |
| RFMXWCDMA_ATTR_MODACC_MEASUREMENT_ENABLED | Specifies whether to enable the ModAcc measurement. |
| RFMXWCDMA_ATTR_MODACC_MEASUREMENT_LENGTH | Specifies the duration of the ModAcc measurement. |
| RFMXWCDMA_ATTR_MODACC_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. |
| RFMXWCDMA_ATTR_MODACC_RRC_FILTER_ENABLED | Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered. |
| RFMXWCDMA_ATTR_MODACC_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. |
| RFMXWCDMA_ATTR_MODACC_TRANSIENT_REMOVAL_ENABLED | Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga0e88da31a920ff4c6ae5132ebdd74b83.html language=enus -->
## TOPIC 00069: RFMXWCDMA_ATTR_MODACC_RRC_FILTER_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga0e88da31a920ff4c6ae5132ebdd74b83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga0e88da31a920ff4c6ae5132ebdd74b83.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered. SyntaxRFMXWCDMA_ATTR_MODACC_RRC_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To5312571int32Read/WriteN/ARemarks You do not need to use a selector string to config

### RFMXWCDMA_ATTR_MODACC_RRC_FILTER_ENABLED

Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RRC_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312571 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | Disables the RRC filter in the measurement. |
| RFMXWCDMA_VAL_MODACC_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | Enables the RRC filter in the measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga3fabd5c2bfcebd2b95722b3651f58d39.html language=enus -->
## TOPIC 00070: RFMXWCDMA_ATTR_MODACC_MEASUREMENT_LENGTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga3fabd5c2bfcebd2b95722b3651f58d39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga3fabd5c2bfcebd2b95722b3651f58d39.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the ModAcc measurement. SyntaxRFMXWCDMA_ATTR_MODACC_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To5312516int32Read/WriteN/ARemarks This value is expressed in slots.You do not need to use a selector string to configure or read this attribute for the default signal

### RFMXWCDMA_ATTR_MODACC_MEASUREMENT_LENGTH

Specifies the duration of the ModAcc measurement.

#### Syntax

RFMXWCDMA_ATTR_MODACC_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312516 | int32 | Read/Write | N/A |

#### Remarks

This value is expressed in slots.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1. Valid values are [1, (15 - [RFMXWCDMA_ATTR_MODACC_MEASUREMENT_OFFSET](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1gaaf29136812b2bc94b533e15f1940bd62.html))]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga43f2d41288bbc817fee56bc7edf8ba35.html language=enus -->
## TOPIC 00071: RFMXWCDMA_ATTR_MODACC_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga43f2d41288bbc817fee56bc7edf8ba35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga43f2d41288bbc817fee56bc7edf8ba35.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ModAcc measurement. SyntaxRFMXWCDMA_ATTR_MODACC_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5312512int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXWCDMA_ATTR_MODACC_MEASUREMENT_ENABLED

Specifies whether to enable the ModAcc measurement.

#### Syntax

RFMXWCDMA_ATTR_MODACC_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312512 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga6719ba2236e0743e22020c42e7a7a9bc.html language=enus -->
## TOPIC 00072: RFMXWCDMA_ATTR_MODACC_TRANSIENT_REMOVAL_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga6719ba2236e0743e22020c42e7a7a9bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga6719ba2236e0743e22020c42e7a7a9bc.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. SyntaxRFMXWCDMA_ATTR_MODACC_TRANSIENT_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To5312519int32Read/WriteN/AR

### RFMXWCDMA_ATTR_MODACC_TRANSIENT_REMOVAL_ENABLED

Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results.

#### Syntax

RFMXWCDMA_ATTR_MODACC_TRANSIENT_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312519 | int32 | Read/Write | N/A |

#### Remarks

Transients are expected to be present at the slot boundaries, where the mean power of the received signal can change.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_TRANSIENT_REMOVAL_ENABLED_FALSE | 0 (0x0) | The entire measurement interval is used to compute the RMS EVM, peak EVM, RMS magnitude error, and RMS phase error results. |
| RFMXWCDMA_VAL_MODACC_TRANSIENT_REMOVAL_ENABLED_TRUE | 1 (0x1) | The measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error, and RMS phase error results. The RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute must be set to Frame, Slot, or Marker. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga7a9b2318855f0dd5d1385f9361b01c85.html language=enus -->
## TOPIC 00073: RFMXWCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga7a9b2318855f0dd5d1385f9361b01c85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga7a9b2318855f0dd5d1385f9361b01c85.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. In case of multi-carrier measurements, this attribute is valid only when you set the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to LO per Carrier. SyntaxRFMXWCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL

### RFMXWCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. In case of multi-carrier measurements, this attribute is valid only when you set the [RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_w_c_d_m_a__attributes__advanced_1gae8eb12aa91b5befbd3c993ad6bfef8d0.html) attribute is set to **LO per Carrier**.

#### Syntax

RFMXWCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312573 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q quadrature error is not removed before the ModAcc measurement. |
| RFMXWCDMA_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q quadrature error is removed before the ModAcc measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1gaaf29136812b2bc94b533e15f1940bd62.html language=enus -->
## TOPIC 00074: RFMXWCDMA_ATTR_MODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1gaaf29136812b2bc94b533e15f1940bd62.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1gaaf29136812b2bc94b533e15f1940bd62.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. SyntaxRFMXWCDMA_ATTR_MODACC_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To531

### RFMXWCDMA_ATTR_MODACC_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga2cf66134d1373e4d337a7540d5390ae7.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_MODACC_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312515 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0, (15 - [RFMXWCDMA_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga3fabd5c2bfcebd2b95722b3651f58d39.html) )]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1gadc8a0b086cb7670cc08c1940ce3c7388.html language=enus -->
## TOPIC 00075: RFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1gadc8a0b086cb7670cc08c1940ce3c7388.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1gadc8a0b086cb7670cc08c1940ce3c7388.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement. In case of multi-carrier measurements, this attribute is valid only when you set the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to LO per Carrier. SyntaxRFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

### RFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement. In case of multi-carrier measurements, this attribute is valid only when you set the [RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_w_c_d_m_a__attributes__advanced_1gae8eb12aa91b5befbd3c993ad6bfef8d0.html) attribute is set to **LO per Carrier**.

#### Syntax

RFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312572 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_w_c_d_m_a__attributes__advanced_1gae8eb12aa91b5befbd3c993ad6bfef8d0.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q gain imbalance is not removed before the ModAcc measurement. |
| RFMXWCDMA_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q gain imbalance is removed before the ModAcc measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel.html language=enus -->
## TOPIC 00076: Downlink Timing Channel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_CODEThe channel code. RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTORThe spreading factor. AttachmentsNone

### Downlink Timing Channel

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_CODE | The channel code. |
| RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTOR | The spreading factor. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel_1ga593bb93998f8159957133f8e69ad2325.html language=enus -->
## TOPIC 00077: RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTOR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel_1ga593bb93998f8159957133f8e69ad2325.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel_1ga593bb93998f8159957133f8e69ad2325.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The spreading factor. SyntaxRFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTORNumeric ValueData TypeAccessApplies To5312521int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String

### RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTOR

The spreading factor.

#### Syntax

RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312521 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Downlink Timing Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel_1gaba594150eca21de382192cc6232bbe53.html language=enus -->
## TOPIC 00078: RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_CODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel_1gaba594150eca21de382192cc6232bbe53.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__downlink__timing__channel_1gaba594150eca21de382192cc6232bbe53.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The channel code. SyntaxRFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_CODENumeric ValueData TypeAccessApplies To5312522int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for inform

### RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_CODE

The channel code.

#### Syntax

RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312522 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Downlink Timing Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results.html language=enus -->
## TOPIC 00079: Results

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDetected ChannelGroup membersNameDescriptionRFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERRORReturns the chip rate error of the composite signal. RFMXWCDMA_ATTR_MODACC_RESULTS_DPCH_TIMING_OFFSETThe timing offset of the selected channel. RFMXWCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERRORReturns the freq

### Results

#### Groups

- Detected Channel

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR | Returns the chip rate error of the composite signal. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_DPCH_TIMING_OFFSET | The timing offset of the selected channel. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERROR | Returns the frequency offset of the composite signal. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE | Returns the I/Q gain imbalance of the composite signal of a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET | Returns the I/Q origin offset of the composite signal of a carrier. This value is expressed in dB. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR | Returns the I/Q quadrature error of the composite signal of a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_MULTI_CARRIER_IQ_ORIGIN_OFFSET | Returns the estimated I/Q origin offset of the multicarrier signal when the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to LO per Band. This value is expressed in dB. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE | Returns the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH | Returns the branch of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE attribute for a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_CODE | Returns the spreading code of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE attribute for a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_SPREADING_FACTOR | Returns the spreading factor of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE attribute for a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE | Returns the maximum code domain error value (CDE). |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH | Returns the branch corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE attribute. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_CODE | Returns the spreading code corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE attribute. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_EVM | Returns the peak EVM of the composite signal. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE | Returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_BRANCH | Returns the branch of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE attribute for a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_CODE | Returns the spreading code of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE attribute for a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_SPREADING_FACTOR | Returns the spreading factor of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE attribute for a carrier. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_PSCH_POWER | The primary SCH power for a BS UUT. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_RHO | Returns the figure of merit used to characterize the modulation accuracy of the composite code domain signal. It refers to the fraction of the total power that can be correlated to the correct active channels in the detected reference signal. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_EVM | Returns the RMS EVM of the composite signal. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR | Returns the RMS magnitude error of the composite signal. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_PHASE_ERROR | Returns the RMS phase error of the composite signal. |
| RFMXWCDMA_ATTR_MODACC_RESULTS_SSCH_POWER | The secondary SCH power for a BS UUT. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga017ec92eb75e76185527e7b6297fcb11.html language=enus -->
## TOPIC 00080: RFMXWCDMA_ATTR_MODACC_RESULTS_PSCH_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga017ec92eb75e76185527e7b6297fcb11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga017ec92eb75e76185527e7b6297fcb11.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The primary SCH power for a BS UUT. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PSCH_POWERNumeric ValueData TypeAccessApplies To5312543float64Read-OnlyN/ARemarks Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_PSCH_POWER

The primary SCH power for a BS UUT.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PSCH_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312543 | float64 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga134c9be6f753ab4e798b7340cfdff370.html language=enus -->
## TOPIC 00081: RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_EVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga134c9be6f753ab4e798b7340cfdff370.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga134c9be6f753ab4e798b7340cfdff370.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of the composite signal. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_RMS_EVMNumeric ValueData TypeAccessApplies To5312529float64Read-OnlyN/ARemarks This value is expressed as a percentage.Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_EVM

Returns the RMS EVM of the composite signal.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312529 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed as a percentage.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga2d5d1c171c79e3f6a8aa76c5829efa45.html language=enus -->
## TOPIC 00082: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga2d5d1c171c79e3f6a8aa76c5829efa45.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga2d5d1c171c79e3f6a8aa76c5829efa45.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDENumeric ValueData TypeAccessApplies To5312546float64Read-OnlyN/ARemarks The relative CDEs are computed by desprea

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE

Returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312546 | float64 | Read-Only | N/A |

#### Remarks

The relative CDEs are computed by despreading the descrambled error vector corresponding to each active channel with the appropriate active channel codes. The RCDE is defined as the ratio of the mean power of this despread error vector to the mean power of the corresponding reference waveform.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga35d068afc8356a1cf968dfa9150b074c.html language=enus -->
## TOPIC 00083: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_EVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga35d068afc8356a1cf968dfa9150b074c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga35d068afc8356a1cf968dfa9150b074c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak EVM of the composite signal. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_EVMNumeric ValueData TypeAccessApplies To5312530float64Read-OnlyN/ARemarks This value is expressed as a percentage.Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_EVM

Returns the peak EVM of the composite signal.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312530 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed as a percentage.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga542453af22448beef1a78c656b8f2ca6.html language=enus -->
## TOPIC 00084: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga542453af22448beef1a78c656b8f2ca6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga542453af22448beef1a78c656b8f2ca6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the branch corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE attribute. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCHNumeric ValueData TypeAccessApplies To5312554int32Read-OnlyN/ARemarks Use "carrier<n>" as the selector string to read this attribute.NameValueDesc

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH

Returns the branch corresponding to the value of the [RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga62ff582fa797b781b82fdbe705d1ea7d.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312554 | int32 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |
| RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |
| RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga6bae85358c762b3c035a1943ba18730f.html language=enus -->
## TOPIC 00085: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_SPREADING_FACTOR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga6bae85358c762b3c035a1943ba18730f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga6bae85358c762b3c035a1943ba18730f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE attribute for a carrier. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_SPREADING_FACTORNumeric ValueData TypeAccessApplies To5312541int32Read-OnlyN/ARemarks Use "carrier<

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_SPREADING_FACTOR

Returns the spreading factor of the channel corresponding to the value of the [RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gaae5077316bbc39496ec76c8e3af4f12c.html) attribute for a carrier.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312541 | int32 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga74b36ff79290a03811f0a7533536bbd6.html language=enus -->
## TOPIC 00086: RFMXWCDMA_ATTR_MODACC_RESULTS_DPCH_TIMING_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga74b36ff79290a03811f0a7533536bbd6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga74b36ff79290a03811f0a7533536bbd6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The timing offset of the selected channel. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_DPCH_TIMING_OFFSETNumeric ValueData TypeAccessApplies To5312545float64Read-OnlyN/ARemarks Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_DPCH_TIMING_OFFSET

The timing offset of the selected channel.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_DPCH_TIMING_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312545 | float64 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga7fb3a081daa7b42e8c58458386bb0985.html language=enus -->
## TOPIC 00087: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_SPREADING_FACTOR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga7fb3a081daa7b42e8c58458386bb0985.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga7fb3a081daa7b42e8c58458386bb0985.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE attribute for a carrier. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_SPREADING_FACTORNumeric ValueData TypeAccessApplies To5312547int32Read-OnlyN/ARemarks Use "carrier<n>" as the s

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_SPREADING_FACTOR

Returns the spreading factor of the channel corresponding to the value of the [RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga2d5d1c171c79e3f6a8aa76c5829efa45.html) attribute for a carrier.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312547 | int32 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga818b196613c8e90bd73a419f83c9132e.html language=enus -->
## TOPIC 00088: RFMXWCDMA_ATTR_MODACC_RESULTS_MULTI_CARRIER_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga818b196613c8e90bd73a419f83c9132e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga818b196613c8e90bd73a419f83c9132e.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated I/Q origin offset of the multicarrier signal when the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to LO per Band. This value is expressed in dB. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_MULTI_CARRIER_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To5312559float64Re

### RFMXWCDMA_ATTR_MODACC_RESULTS_MULTI_CARRIER_IQ_ORIGIN_OFFSET

Returns the estimated I/Q origin offset of the multicarrier signal when the [RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_w_c_d_m_a__attributes__advanced_1gae8eb12aa91b5befbd3c993ad6bfef8d0.html) attribute is set to **LO per Band**. This value is expressed in dB.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_MULTI_CARRIER_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312559 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

This result is useful when the LO is at the center of the multicarrier signal.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga869db2d480872fe632f05d332d35ab3c.html language=enus -->
## TOPIC 00089: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_CODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga869db2d480872fe632f05d332d35ab3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga869db2d480872fe632f05d332d35ab3c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading code of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE attribute for a carrier. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_CODENumeric ValueData TypeAccessApplies To5312548int32Read-OnlyN/ARemarks Use "carrier<n>" as the selector string

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_CODE

Returns the spreading code of the channel corresponding to the value of the [RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga2d5d1c171c79e3f6a8aa76c5829efa45.html) attribute for a carrier.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312548 | int32 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga9bf611f225eb7def725cc654d9113d18.html language=enus -->
## TOPIC 00090: RFMXWCDMA_ATTR_MODACC_RESULTS_SSCH_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga9bf611f225eb7def725cc654d9113d18.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga9bf611f225eb7def725cc654d9113d18.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The secondary SCH power for a BS UUT. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_SSCH_POWERNumeric ValueData TypeAccessApplies To5312544float64Read-OnlyN/ARemarks Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_SSCH_POWER

The secondary SCH power for a BS UUT.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_SSCH_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312544 | float64 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gaae5077316bbc39496ec76c8e3af4f12c.html language=enus -->
## TOPIC 00091: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gaae5077316bbc39496ec76c8e3af4f12c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gaae5077316bbc39496ec76c8e3af4f12c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDENumeric ValueData TypeAccessApplies To5312540float64Read-OnlyN/ARemarks The active CDEs are computed by despreading the descrambled er

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE

Returns the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312540 | float64 | Read-Only | N/A |

#### Remarks

The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gab5323f5d9e8a412d4f9099b2ee89a3e0.html language=enus -->
## TOPIC 00092: RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gab5323f5d9e8a412d4f9099b2ee89a3e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gab5323f5d9e8a412d4f9099b2ee89a3e0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS magnitude error of the composite signal. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To5312531float64Read-OnlyN/ARemarks This value is expressed as a percentage.Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR

Returns the RMS magnitude error of the composite signal.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312531 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed as a percentage.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gabb8d625cf1083e25c7fb0df6e3a28dac.html language=enus -->
## TOPIC 00093: RFMXWCDMA_ATTR_MODACC_RESULTS_RHO

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gabb8d625cf1083e25c7fb0df6e3a28dac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gabb8d625cf1083e25c7fb0df6e3a28dac.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the figure of merit used to characterize the modulation accuracy of the composite code domain signal. It refers to the fraction of the total power that can be correlated to the correct active channels in the detected reference signal. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_RHONumeric ValueData

### RFMXWCDMA_ATTR_MODACC_RESULTS_RHO

Returns the figure of merit used to characterize the modulation accuracy of the composite code domain signal. It refers to the fraction of the total power that can be correlated to the correct active channels in the detected reference signal.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_RHO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312533 | float64 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

You can calculate the value of Rho using the following equation:

*Rho* = *Power correctly correlated to active channels* / *Total power*

A Rho value of 1 indicates that all the transmitted power is correlated to the correct active channels and there is no power in the inactive (undesired) channels. Any energy correlated to the inactive channels degrades modulation quality and results in a value of Rho less than 1. Valid values are 0.0 to 1.0, inclusive.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gac1e32490e23f06da19c6208e9d5ce2f5.html language=enus -->
## TOPIC 00094: RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_BRANCH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gac1e32490e23f06da19c6208e9d5ce2f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gac1e32490e23f06da19c6208e9d5ce2f5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the branch of the channel corresponding to the value of the RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE attribute for a carrier. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_BRANCHNumeric ValueData TypeAccessApplies To5312556int32Read-OnlyN/ARemarks Use "carrier<n>" as the selector string to re

### RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_BRANCH

Returns the branch of the channel corresponding to the value of the [RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1ga2d5d1c171c79e3f6a8aa76c5829efa45.html) attribute for a carrier.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_BRANCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312556 | int32 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |
| RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |
| RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gace59c08cbcbc0ed57a4cb0e99c76881d.html language=enus -->
## TOPIC 00095: RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_PHASE_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gace59c08cbcbc0ed57a4cb0e99c76881d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gace59c08cbcbc0ed57a4cb0e99c76881d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS phase error of the composite signal. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_RMS_PHASE_ERRORNumeric ValueData TypeAccessApplies To5312532float64Read-OnlyN/ARemarks This value is expressed in degrees.Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_PHASE_ERROR

Returns the RMS phase error of the composite signal.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312532 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed in degrees.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gadbfb5af705551fcc21c527bd1a8ea886.html language=enus -->
## TOPIC 00096: RFMXWCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gadbfb5af705551fcc21c527bd1a8ea886.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gadbfb5af705551fcc21c527bd1a8ea886.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency offset of the composite signal. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To5312535float64Read-OnlyN/ARemarks This value is expressed in Hz.Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

Returns the frequency offset of the composite signal.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312535 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed in Hz.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gaf1e4c16e525e49f32c868b70568b0e87.html language=enus -->
## TOPIC 00097: RFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gaf1e4c16e525e49f32c868b70568b0e87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results_1gaf1e4c16e525e49f32c868b70568b0e87.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip rate error of the composite signal. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERRORNumeric ValueData TypeAccessApplies To5312536float64Read-OnlyN/ARemarks This value is expressed in ppm.Use "carrier<n>" as the selector string to read this attribute.

### RFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

Returns the chip rate error of the composite signal.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312536 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed in ppm.

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga51d35614e3cc7975fc2729451f2e1b9d.html language=enus -->
## TOPIC 00098: RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga51d35614e3cc7975fc2729451f2e1b9d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga51d35614e3cc7975fc2729451f2e1b9d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation type of the detected channel. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPENumeric ValueData TypeAccessApplies To5312552int32Read-OnlyChannelRemarks If the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute is set to User Defined or Test Model, the ModAcc Resul

### RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE

Returns the modulation type of the detected channel.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312552 | int32 | Read-Only | Channel |

#### Remarks

If the [RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html) attribute is set to **User Defined** or **Test Model**, the ModAcc Results Detected Mod Type attribute returns the modulation type of the configured channel of a carrier.

Use "carrier<n>/channel<k>" as the selector string to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_BPSK_QPSK | 0 (0x0) | The modulation type is BPSK. |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_4PAM_16QAM | 1 (0x1) | The modulation type is 4-PAM. |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_64QAM | 2 (0x2) | The modulation type is 64-QAM. |

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga8cc4c424ef551084925f6158a65af71a.html language=enus -->
## TOPIC 00099: RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_CODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga8cc4c424ef551084925f6158a65af71a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga8cc4c424ef551084925f6158a65af71a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading code of the detected channel. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_CODENumeric ValueData TypeAccessApplies To5312551int32Read-OnlyChannelRemarks If you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined or Test Model, the ModAcc Result

### RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_CODE

Returns the spreading code of the detected channel.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_CODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312551 | int32 | Read-Only | Channel |

#### Remarks

If you set the [RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html) attribute to **User Defined** or **Test Model**, the ModAcc Results Detected Spreading Code attribute returns the spreading code of the configured channel of a carrier.

Use "carrier<n>/channel<k>" as the selector string to read this result.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga9d4422c24b33e7690ba4ed6cd9d101c2.html language=enus -->
## TOPIC 00100: RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga9d4422c24b33e7690ba4ed6cd9d101c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1ga9d4422c24b33e7690ba4ed6cd9d101c2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the branch of the detected channel. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCHNumeric ValueData TypeAccessApplies To5312553int32Read-OnlyChannelRemarks If the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute is set to User Defined or Test Model, the ModAcc Results Detected Branch

### RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH

Returns the branch of the detected channel.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312553 | int32 | Read-Only | Channel |

#### Remarks

If the [RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html) attribute is set to **User Defined** or **Test Model**, the ModAcc Results Detected Branch attribute returns the branch of the configured channel of a carrier.

Use "carrier<n>/channel<k>" as the selector string to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1gaefea7d6bf1d2f9131c75184487e094a1.html language=enus -->
## TOPIC 00101: RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTOR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1gaefea7d6bf1d2f9131c75184487e094a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1gaefea7d6bf1d2f9131c75184487e094a1.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor of the detected channel. SyntaxRFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTORNumeric ValueData TypeAccessApplies To5312550int32Read-OnlyChannelRemarks If the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute is set to User Defined or Test Model, the ModAcc Res

### RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTOR

Returns the spreading factor of the detected channel.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312550 | int32 | Read-Only | Channel |

#### Remarks

If the [RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html) attribute is set to **User Defined** or **Test Model**, the ModAcc Results Detected Spreading Factor attribute returns the spreading factor of the configured channel of a carrier.

Use "carrier<n>/channel<k>" as the selector string to read this result.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1gaf7b27d425b8537a61441f42f9b6334c0.html language=enus -->
## TOPIC 00102: RFMXWCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1gaf7b27d425b8537a61441f42f9b6334c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc__results__detected__channel_1gaf7b27d425b8537a61441f42f9b6334c0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of detected channels when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Auto Detect. If you set the Channel Configuration Mode attribute to User Defined or Test Model, this attribute returns the number of configured channels. SyntaxRFMXWCDMA_ATTR_MODACC_RESULT

### RFMXWCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

Returns the number of detected channels when you set the [RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html) attribute to **Auto Detect**. If you set the Channel Configuration Mode attribute to **User Defined** or **Test Model**, this attribute returns the number of configured channels.

#### Syntax

RFMXWCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5312549 | int32 | Read-Only | N/A |

#### Remarks

Use "carrier<n>" as the selector string to read this attribute.

Parent topic:

Detected Channel

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw.html language=enus -->
## TOPIC 00103: OBW

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXWCDMA_ATTR_OBW_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. RFMXWCDMA_ATTR_OBW_AMPLITUDE_CORRECTION_TYPESpecifies whether the amplitude of the freque

### OBW

#### Groups

- Averaging
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_OBW_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. |
| RFMXWCDMA_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation function to configure the external attenuation table. |
| RFMXWCDMA_ATTR_OBW_MEASUREMENT_ENABLED | Specifies whether to enable the OBW measurement. |
| RFMXWCDMA_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the OBW measurement. |
| RFMXWCDMA_ATTR_OBW_SPAN | Returns the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1ga883916ef75370e85ff468b4e87eabbca.html language=enus -->
## TOPIC 00104: RFMXWCDMA_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1ga883916ef75370e85ff468b4e87eabbca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1ga883916ef75370e85ff468b4e87eabbca.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the OBW measurement. SyntaxRFMXWCDMA_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To5267459int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of thread

### RFMXWCDMA_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the OBW measurement.

#### Syntax

RFMXWCDMA_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267459 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaa8cb69e41f61eb71d7452f776e487f33.html language=enus -->
## TOPIC 00105: RFMXWCDMA_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaa8cb69e41f61eb71d7452f776e487f33.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaa8cb69e41f61eb71d7452f776e487f33.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation function to configure the external attenuation table. SyntaxRFMXWCDMA_A

### RFMXWCDMA_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXWCDMA_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267482 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXWCDMA_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaaa0e89b3089ab2ea7d1204a12bce5864.html language=enus -->
## TOPIC 00106: RFMXWCDMA_ATTR_OBW_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaaa0e89b3089ab2ea7d1204a12bce5864.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaaa0e89b3089ab2ea7d1204a12bce5864.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the OBW measurement. SyntaxRFMXWCDMA_ATTR_OBW_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5267456int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Stri

### RFMXWCDMA_ATTR_OBW_MEASUREMENT_ENABLED

Specifies whether to enable the OBW measurement.

#### Syntax

RFMXWCDMA_ATTR_OBW_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267456 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaf8edec221ef477aa5b4f36eb57b8abd3.html language=enus -->
## TOPIC 00107: RFMXWCDMA_ATTR_OBW_ALL_TRACES_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaf8edec221ef477aa5b4f36eb57b8abd3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw_1gaf8edec221ef477aa5b4f36eb57b8abd3.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. SyntaxRFMXWCDMA_ATTR_OBW_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To5267474int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for t

### RFMXWCDMA_ATTR_OBW_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement.

#### Syntax

RFMXWCDMA_ATTR_OBW_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267474 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__averaging.html language=enus -->
## TOPIC 00108: Averaging

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__averaging.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_OBW_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLED attribute to True. RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLEDSpecifies whether to enable averaging for the OBW measurement.

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_OBW_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLED attribute to True. |
| RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLED | Specifies whether to enable averaging for the OBW measurement. |
| RFMXWCDMA_ATTR_OBW_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__averaging_1ga46f96e9cb395bc10e34c90dff2f2ad2c.html language=enus -->
## TOPIC 00109: RFMXWCDMA_ATTR_OBW_AVERAGING_COUNT

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__averaging_1ga46f96e9cb395bc10e34c90dff2f2ad2c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__averaging_1ga46f96e9cb395bc10e34c90dff2f2ad2c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLED attribute to True. SyntaxRFMXWCDMA_ATTR_OBW_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To5267462int32Read/WriteN/ARemarks You do not need to use a selector string to configure or rea

### RFMXWCDMA_ATTR_OBW_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLED](group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__averaging_1ga10719ae0befd356f5a40fa55376cc8bf.html) attribute to **True**.

#### Syntax

RFMXWCDMA_ATTR_OBW_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267462 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter.html language=enus -->
## TOPIC 00110: RBW Filter

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the RBW. RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the RBW. |
| RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH attribute to False. |
| RFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPE | Specifies the shape of the digital RBW filter. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1ga22f80a95bf6d5bc0c3c60d29ed250d4b.html language=enus -->
## TOPIC 00111: RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1ga22f80a95bf6d5bc0c3c60d29ed250d4b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1ga22f80a95bf6d5bc0c3c60d29ed250d4b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH attribute to False. SyntaxRFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To5267469float64Read/WriteN/ARemarks This attribute is valid

### RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [RFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1gaee73880d1d2ba2b70d83193153bbf175.html) attribute to **False**.

#### Syntax

RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267469 | float64 | Read/Write | N/A |

#### Remarks

This attribute is valid only if you set the [RFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1ga2cfcb3865616503dcd7827960c0790c9.html) attribute to **Gaussian** or **Flat**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 30 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1ga2cfcb3865616503dcd7827960c0790c9.html language=enus -->
## TOPIC 00112: RFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1ga2cfcb3865616503dcd7827960c0790c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__rbw__filter_1ga2cfcb3865616503dcd7827960c0790c9.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To5267470int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String top

### RFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267470 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is applied. |
| RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__results.html language=enus -->
## TOPIC 00113: Results

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__results.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_OBW_RESULTS_ABSOLUTE_POWERReturns the total integrated power of the acquired signal. RFMXWCDMA_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTHReturns the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the ca

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_OBW_RESULTS_ABSOLUTE_POWER | Returns the total integrated power of the acquired signal. |
| RFMXWCDMA_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH | Returns the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers. |
| RFMXWCDMA_ATTR_OBW_RESULTS_START_FREQUENCY | Returns the start frequency of the RFMXWCDMA_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH. |
| RFMXWCDMA_ATTR_OBW_RESULTS_STOP_FREQUENCY | Returns the stop frequency of the RFMXWCDMA_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time.html language=enus -->
## TOPIC 00114: Sweep Time

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTOSpecifies whether the measurement computes the sweep time. RFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. AttachmentsNone

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO | Specifies whether the measurement computes the sweep time. |
| RFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time_1ga50d818c6ee1c3670eab74fceea428602.html language=enus -->
## TOPIC 00115: RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time_1ga50d818c6ee1c3670eab74fceea428602.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time_1ga50d818c6ee1c3670eab74fceea428602.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To5267471int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267471 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_OBW_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXWCDMA_VAL_OBW_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time value of one slot duration. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time_1gadfd83cab43878213b8cab2ce1c084d08.html language=enus -->
## TOPIC 00116: RFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time_1gadfd83cab43878213b8cab2ce1c084d08.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time_1gadfd83cab43878213b8cab2ce1c084d08.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO attribute to False. SyntaxRFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To5267472float64Read/WriteN/ARemarks This value is expressed in seconds.You do not need to use a selector string to configu

### RFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO](group____root__ni_r_fmx_w_c_d_m_a__attributes__obw__sweep__time_1ga50d818c6ee1c3670eab74fceea428602.html) attribute to **False**.

#### Syntax

RFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5267472 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm.html language=enus -->
## TOPIC 00117: QEVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingResultsGroup membersNameDescriptionRFMXWCDMA_ATTR_QEVM_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. RFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLEDSpecifies whether to remove the I/Q offset before the QEVM mea

### QEVM

#### Groups

- Averaging
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_QEVM_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. |
| RFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove the I/Q offset before the QEVM measurement. |
| RFMXWCDMA_ATTR_QEVM_MEASUREMENT_ENABLED | Specifies whether to enable the QPSK EVM measurement. |
| RFMXWCDMA_ATTR_QEVM_MEASUREMENT_LENGTH | Specifies the duration of the QEVM measurement. This value is expressed in chips. |
| RFMXWCDMA_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the QEVM measurement. |
| RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED | Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered. |
| RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga2354c6a9042582112cac9b784fa9ebd5.html language=enus -->
## TOPIC 00118: RFMXWCDMA_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga2354c6a9042582112cac9b784fa9ebd5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga2354c6a9042582112cac9b784fa9ebd5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the QEVM measurement. SyntaxRFMXWCDMA_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To5316621int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defau

### RFMXWCDMA_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the QEVM measurement.

#### Syntax

RFMXWCDMA_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316621 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga4d78159d2577b26f70b9fb11837c9ac7.html language=enus -->
## TOPIC 00119: RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga4d78159d2577b26f70b9fb11837c9ac7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga4d78159d2577b26f70b9fb11837c9ac7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered. SyntaxRFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To5316619int32Read/WriteN/ARemarks You do not need to use a selector string to configur

### RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED

Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316619 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | Disables the RRC filter in the measurement. |
| RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | Enables the RRC filter in the measurement. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga79afd260cca0fb183ea5c3518b1fd4f4.html language=enus -->
## TOPIC 00120: RFMXWCDMA_ATTR_QEVM_MEASUREMENT_LENGTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga79afd260cca0fb183ea5c3518b1fd4f4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga79afd260cca0fb183ea5c3518b1fd4f4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the QEVM measurement. This value is expressed in chips. SyntaxRFMXWCDMA_ATTR_QEVM_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To5316611int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal ins

### RFMXWCDMA_ATTR_QEVM_MEASUREMENT_LENGTH

Specifies the duration of the QEVM measurement. This value is expressed in chips.

#### Syntax

RFMXWCDMA_ATTR_QEVM_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316611 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 2560. NI recommends that you set this attribute to n * 512, where the value of n can range from 1 to 10.

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga7c92bbf2b54ec0470b184fd12aa44578.html language=enus -->
## TOPIC 00121: RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga7c92bbf2b54ec0470b184fd12aa44578.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga7c92bbf2b54ec0470b184fd12aa44578.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. SyntaxRFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To5316615int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selec

### RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED

Specifies whether the spectrum of the signal is inverted.

#### Syntax

RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316615 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The spectrum is not inverted. |
| RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The spectrum is inverted. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga7db61fce5db3610d818c53dd7d00e767.html language=enus -->
## TOPIC 00122: RFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga7db61fce5db3610d818c53dd7d00e767.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1ga7db61fce5db3610d818c53dd7d00e767.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the QEVM measurement. SyntaxRFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To5316616int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instan

### RFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

Specifies whether to remove the I/Q offset before the QEVM measurement.

#### Syntax

RFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316616 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE | 0 (0x0) | The I/Q offset is not removed before the QEVM measurement. |
| RFMXWCDMA_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_TRUE | 1 (0x1) | The I/Q offset is removed before the QEVM measurement. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1gaf5b8cc064df1ceccaa755283f1079168.html language=enus -->
## TOPIC 00123: RFMXWCDMA_ATTR_QEVM_ALL_TRACES_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1gaf5b8cc064df1ceccaa755283f1079168.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm_1gaf5b8cc064df1ceccaa755283f1079168.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. SyntaxRFMXWCDMA_ATTR_QEVM_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To5316620int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXWCDMA_ATTR_QEVM_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

#### Syntax

RFMXWCDMA_ATTR_QEVM_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316620 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga1218c238485fe5e13a5dfa9091f7e3dc.html language=enus -->
## TOPIC 00124: RFMXWCDMA_ATTR_QEVM_AVERAGING_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga1218c238485fe5e13a5dfa9091f7e3dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga1218c238485fe5e13a5dfa9091f7e3dc.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the QEVM measurement. SyntaxRFMXWCDMA_ATTR_QEVM_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To5316613int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXWCDMA_ATTR_QEVM_AVERAGING_ENABLED

Specifies whether to enable averaging for the QEVM measurement.

#### Syntax

RFMXWCDMA_ATTR_QEVM_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316613 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The QEVM measurement uses the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute as the number of acquisitions over which the QEVM measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results.html language=enus -->
## TOPIC 00125: Results

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERRORReturns the maximum chip rate error value for a QPSK signal. This value is expressed in ppm. This value is obtained over all averaging iterations. RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERRORReturns the m

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR | Returns the maximum chip rate error value for a QPSK signal. This value is expressed in ppm. This value is obtained over all averaging iterations. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR | Returns the maximum value of the frequency errors for a QPSK signal. This value is expressed in Hz. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET | Returns the maximum value of the I/Q origin offsets for a QPSK signal. This value is expressed in dB. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR | Returns the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM | Returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR | Returns the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM | Returns the maximum value of the RMS EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR | Returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR | Returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET | Returns the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR | Returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM | Returns the mean of peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the peak EVMs over all averaging acquisitions. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR | Returns the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage. |
| RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_RMS_EVM | Returns the mean of the RMS EVM values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. |

#### Attachments

None

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga3480701db3294f6a6331a6ef8cbb79e5.html language=enus -->
## TOPIC 00126: RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga3480701db3294f6a6331a6ef8cbb79e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga3480701db3294f6a6331a6ef8cbb79e5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the RMS EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. SyntaxRFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVMNumeric ValueData TypeAccessApplies To5316623float64Read-OnlyN/ARemarks The number of acquisiti

### RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM

Returns the maximum value of the RMS EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316623 | float64 | Read-Only | N/A |

#### Remarks

The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga38f2f5ec2b221e4ebdeabb6d74be5c7b.html language=enus -->
## TOPIC 00127: RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga38f2f5ec2b221e4ebdeabb6d74be5c7b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga38f2f5ec2b221e4ebdeabb6d74be5c7b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To5316630float64Read-OnlyN/ARemarks This value is obtained by the mean of frequency errors obtained over all averaging

### RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

Returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316630 | float64 | Read-Only | N/A |

#### Remarks

This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga3fe3d89f6a65824ac150b9492f1da5b8.html language=enus -->
## TOPIC 00128: RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga3fe3d89f6a65824ac150b9492f1da5b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga3fe3d89f6a65824ac150b9492f1da5b8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the frequency errors for a QPSK signal. This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To5316631float64Read-OnlyN/ARemarks This value is obtained over all averaging iterations. The number of acq

### RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR

Returns the maximum value of the frequency errors for a QPSK signal. This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316631 | float64 | Read-Only | N/A |

#### Remarks

This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga4f514494aa8cf5e0a8955ccebdcf6c35.html language=enus -->
## TOPIC 00129: RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_RMS_EVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga4f514494aa8cf5e0a8955ccebdcf6c35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga4f514494aa8cf5e0a8955ccebdcf6c35.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the RMS EVM values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. SyntaxRFMXWCDM

### RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_RMS_EVM

Returns the mean of the RMS EVM values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_RMS_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316622 | float64 | Read-Only | N/A |

#### Remarks

The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga9606a23419afee971a00d705c2fec249.html language=enus -->
## TOPIC 00130: RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga9606a23419afee971a00d705c2fec249.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga9606a23419afee971a00d705c2fec249.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. SyntaxRFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVMNumeric ValueData TypeAccessApplies To5316625float64Read-OnlyN/ARemarks The number of acquisi

### RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM

Returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316625 | float64 | Read-Only | N/A |

#### Remarks

The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga967e5ef1c7c04b4a2ca16301d25f498e.html language=enus -->
## TOPIC 00131: RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga967e5ef1c7c04b4a2ca16301d25f498e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1ga967e5ef1c7c04b4a2ca16301d25f498e.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB. SyntaxRFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To5316632float64Read-OnlyN/ARemarks This value is obtained by averaging the I/Q origin offsets over all averaging acquis

### RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

Returns the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316632 | float64 | Read-Only | N/A |

#### Remarks

This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gaa52e9b7b8701a6c1f385fcbeb9f92f87.html language=enus -->
## TOPIC 00132: RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gaa52e9b7b8701a6c1f385fcbeb9f92f87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gaa52e9b7b8701a6c1f385fcbeb9f92f87.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. SyntaxRFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To5316626float64Read-OnlyN/ARemarks This value is obtained by averaging the RMS magnitude errors over all ave

### RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

Returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316626 | float64 | Read-Only | N/A |

#### Remarks

This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gab308f365333a827cdb9808a7042a5b78.html language=enus -->
## TOPIC 00133: RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gab308f365333a827cdb9808a7042a5b78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gab308f365333a827cdb9808a7042a5b78.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. SyntaxRFMXW

### RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

Returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316634 | float64 | Read-Only | N/A |

#### Remarks

The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gac3178320f2140f8fdc5e2a47555026bf.html language=enus -->
## TOPIC 00134: RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gac3178320f2140f8fdc5e2a47555026bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__results_1gac3178320f2140f8fdc5e2a47555026bf.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. SyntaxRFMXWCDMA_ATTR_QEVM_RESULTS_

### RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

Returns the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT](group____root__ni_r_fmx_w_c_d_m_a__attributes__qevm__averaging_1ga6f2863cc6d9c3c363e694122eeb88c7a.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5316629 | float64 | Read-Only | N/A |

#### Remarks

The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem.html language=enus -->
## TOPIC 00135: SEM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingCarrierOffsetResultsSweep TimeGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. RFMXWCDMA_ATTR_SEM_AMPLITUDE_CORRECTION_TYPESpecifies whether the amplitude of the fre

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
| RFMXWCDMA_ATTR_SEM_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. |
| RFMXWCDMA_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation function to configure the external attenuation table. |
| RFMXWCDMA_ATTR_SEM_MEASUREMENT_ENABLED | Specifies whether to enable the SEM measurement. |
| RFMXWCDMA_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the SEM measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1ga4015e4cb7612fe609fbf0f2a51d7f109.html language=enus -->
## TOPIC 00136: RFMXWCDMA_ATTR_SEM_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1ga4015e4cb7612fe609fbf0f2a51d7f109.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1ga4015e4cb7612fe609fbf0f2a51d7f109.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SEM measurement. SyntaxRFMXWCDMA_ATTR_SEM_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5275648int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Stri

### RFMXWCDMA_ATTR_SEM_MEASUREMENT_ENABLED

Specifies whether to enable the SEM measurement.

#### Syntax

RFMXWCDMA_ATTR_SEM_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275648 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1ga9475d997149f05b91c81718828880a3b.html language=enus -->
## TOPIC 00137: RFMXWCDMA_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1ga9475d997149f05b91c81718828880a3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1ga9475d997149f05b91c81718828880a3b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the SEM measurement. SyntaxRFMXWCDMA_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To5275677int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of thread

### RFMXWCDMA_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the SEM measurement.

#### Syntax

RFMXWCDMA_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275677 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1gaaaf243111711ee48b07d184f87788603.html language=enus -->
## TOPIC 00138: RFMXWCDMA_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1gaaaf243111711ee48b07d184f87788603.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1gaaaf243111711ee48b07d184f87788603.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation function to configure the external attenuation table. SyntaxRFMXWCDMA_A

### RFMXWCDMA_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXWCDMA_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275724 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXWCDMA_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1gabec0e6cdaf24d1d4dd48e924ccdab5b0.html language=enus -->
## TOPIC 00139: RFMXWCDMA_ATTR_SEM_ALL_TRACES_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1gabec0e6cdaf24d1d4dd48e924ccdab5b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem_1gabec0e6cdaf24d1d4dd48e924ccdab5b0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. SyntaxRFMXWCDMA_ATTR_SEM_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To5275687int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for t

### RFMXWCDMA_ATTR_SEM_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.

#### Syntax

RFMXWCDMA_ATTR_SEM_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275687 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging.html language=enus -->
## TOPIC 00140: Averaging

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED attribute to True. RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLEDSpecifies whether to enable averaging for the SEM measurement.

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SEM_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED attribute to True. |
| RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED | Specifies whether to enable averaging for the SEM measurement. |
| RFMXWCDMA_ATTR_SEM_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging_1ga3581c60ca2f6387942bdc1ecb76c75ea.html language=enus -->
## TOPIC 00141: RFMXWCDMA_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging_1ga3581c60ca2f6387942bdc1ecb76c75ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging_1ga3581c60ca2f6387942bdc1ecb76c75ea.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. SyntaxRFMXWCDMA_ATTR_SEM_AVERAGING_TYPENumeric ValueData TypeAccessApplies To5275681int32Read/WriteN/ARemarks The averaged spectrum is used for the SEM measurement.You do not need to use a selector string to configure or read

### RFMXWCDMA_ATTR_SEM_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions.

#### Syntax

RFMXWCDMA_ATTR_SEM_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275681 | int32 | Read/Write | N/A |

#### Remarks

The averaged spectrum is used for the SEM measurement.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MAX | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MIN | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging_1ga6519717a99759c7508dc0e11fbf72e2d.html language=enus -->
## TOPIC 00142: RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging_1ga6519717a99759c7508dc0e11fbf72e2d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__averaging_1ga6519717a99759c7508dc0e11fbf72e2d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the SEM measurement. SyntaxRFMXWCDMA_ATTR_SEM_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To5275679int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the S

### RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED

Specifies whether to enable averaging for the SEM measurement.

#### Syntax

RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275679 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The SEM measurement uses the value of the RFMXWCDMA_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__carrier.html language=enus -->
## TOPIC 00143: Carrier

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__carrier.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHReturns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. AttachmentsNone

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH | Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset.html language=enus -->
## TOPIC 00144: Offset

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsRBW FilterGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_NUMBER_OF_OFFSETSReturns the number of offset segments. RFMXWCDMA_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRALReturns the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. RFMXWCDMA_ATTR_SEM_OFFSET_

### Offset

#### Groups

- RBW Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SEM_NUMBER_OF_OFFSETS | Returns the number of offset segments. |
| RFMXWCDMA_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL | Returns the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. |
| RFMXWCDMA_ATTR_SEM_OFFSET_START_FREQUENCY | Returns the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. |
| RFMXWCDMA_ATTR_SEM_OFFSET_STOP_FREQUENCY | Returns the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1ga15387b97d3dfe87914bc315bf1bf2e38.html language=enus -->
## TOPIC 00145: RFMXWCDMA_ATTR_SEM_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1ga15387b97d3dfe87914bc315bf1bf2e38.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1ga15387b97d3dfe87914bc315bf1bf2e38.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_SEM_OFFSET_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To5275669float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to read

### RFMXWCDMA_ATTR_SEM_OFFSET_STOP_FREQUENCY

Returns the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_SEM_OFFSET_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275669 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this attribute.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1ga6783b66371134cc05e10939fa6302008.html language=enus -->
## TOPIC 00146: RFMXWCDMA_ATTR_SEM_OFFSET_START_FREQUENCY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1ga6783b66371134cc05e10939fa6302008.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1ga6783b66371134cc05e10939fa6302008.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_SEM_OFFSET_START_FREQUENCYNumeric ValueData TypeAccessApplies To5275668float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to rea

### RFMXWCDMA_ATTR_SEM_OFFSET_START_FREQUENCY

Returns the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_SEM_OFFSET_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275668 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this attribute.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1gabb95652db00534a2578bb93620eb0cba.html language=enus -->
## TOPIC 00147: RFMXWCDMA_ATTR_SEM_NUMBER_OF_OFFSETS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1gabb95652db00534a2578bb93620eb0cba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset_1gabb95652db00534a2578bb93620eb0cba.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of offset segments. SyntaxRFMXWCDMA_ATTR_SEM_NUMBER_OF_OFFSETSNumeric ValueData TypeAccessApplies To5275659int32Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector String topic for informati

### RFMXWCDMA_ATTR_SEM_NUMBER_OF_OFFSETS

Returns the number of offset segments.

#### Syntax

RFMXWCDMA_ATTR_SEM_NUMBER_OF_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275659 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset__rbw__filter_1ga5126cddc4bfd2aca4f0a623adf7ed479.html language=enus -->
## TOPIC 00148: RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset__rbw__filter_1ga5126cddc4bfd2aca4f0a623adf7ed479.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset__rbw__filter_1ga5126cddc4bfd2aca4f0a623adf7ed479.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To5275671float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to read this attribu

### RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

Returns the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275671 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this attribute.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset__rbw__filter_1ga9368289989a21bc6d55ee02a42beb20f.html language=enus -->
## TOPIC 00149: RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset__rbw__filter_1ga9368289989a21bc6d55ee02a42beb20f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__offset__rbw__filter_1ga9368289989a21bc6d55ee02a42beb20f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the shape of the digital RBW filter. SyntaxRFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To5275672int32Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to read this attribute.NameValueDescriptionRFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED0 (

### RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_TYPE

Returns the shape of the digital RBW filter.

#### Syntax

RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275672 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |
| RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |
| RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |
| RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4 | 3 (0x3) | The RBW filter has a response of a 4-pole synchronously tuned filter. |
| RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5 | 4 (0x4) | The RBW filter has a response of a 5-pole synchronously tuned filter. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results.html language=enus -->
## TOPIC 00150: Results

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCarrierLower OffsetUpper OffsetGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUSIndicates the overall SEM measurement status, based on the value of the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS and the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT

### Results

#### Groups

- Carrier
- Lower Offset
- Upper Offset

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS | Indicates the overall SEM measurement status, based on the value of the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS and the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS attributes. |
| RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER | Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER attribute. For a single-carrier measurement, total carrier power is the same as carrier absolute power. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga080d8a77b3c74a29e1b913c5e33198e6.html language=enus -->
## TOPIC 00151: RFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga080d8a77b3c74a29e1b913c5e33198e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga080d8a77b3c74a29e1b913c5e33198e6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall SEM measurement status, based on the value of the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS and the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS attributes. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To5

### RFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

Indicates the overall SEM measurement status, based on the value of the [RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga367ce46d1493032356c7341de42300c6.html) and the [RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga2b33dc8506010494ffb8be0d72294986.html) attributes.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275689 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The measurement status of at least one offset segment has failed. |
| RFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_PASS | 1 (0x1) | The measurement status of all offset segments have passed. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html language=enus -->
## TOPIC 00152: RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER attribute. For a single-carrier measurement, total carrier power is the same as carrier absolute power. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS

### RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the [RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaf09c17a9a2b453ccac7420869f096198.html) attribute. For a single-carrier measurement, total carrier power is the same as carrier absolute power.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275688 | float64 | Read-Only | N/A |

#### Remarks

This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and named results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier.html language=enus -->
## TOPIC 00153: Carrier

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWERReturns the carrier power. RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWERReturns the peak power in the carrier channel. RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCYReturns the frequency at

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER | Returns the carrier power. |
| RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER | Returns the peak power in the carrier channel. |
| RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY | Returns the frequency at which the peak power is observed in the carrier channel. |
| RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER | Returns the carrier power relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa375f31e3d2aad6325f4753af5c087aa.html language=enus -->
## TOPIC 00154: RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa375f31e3d2aad6325f4753af5c087aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa375f31e3d2aad6325f4753af5c087aa.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To5275694float64Read-OnlyCarrierRemarks This value is expressed in dB.Use "carrier<k>" as the selector strin

### RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER

Returns the carrier power relative to the [RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html).

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275694 | float64 | Read-Only | Carrier |

#### Remarks

This value is expressed in dB.

Use "carrier<k>" as the selector string to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa49458a6965f6d3a6b091cf7dfd7d36f.html language=enus -->
## TOPIC 00155: RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa49458a6965f6d3a6b091cf7dfd7d36f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa49458a6965f6d3a6b091cf7dfd7d36f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power in the carrier channel. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To5275695float64Read-OnlyCarrierRemarks This value is expressed in dBm.Use "carrier<k>" as the selector string to read this result.

### RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER

Returns the peak power in the carrier channel.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275695 | float64 | Read-Only | Carrier |

#### Remarks

This value is expressed in dBm.

Use "carrier<k>" as the selector string to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa78eb68b004be1831e0127f95d13adbe.html language=enus -->
## TOPIC 00156: RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa78eb68b004be1831e0127f95d13adbe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaa78eb68b004be1831e0127f95d13adbe.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power is observed in the carrier channel. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To5275696float64Read-OnlyCarrierRemarks This value is expressed in Hz.Use "carrier<k>" as the selector string to read this resu

### RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY

Returns the frequency at which the peak power is observed in the carrier channel.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275696 | float64 | Read-Only | Carrier |

#### Remarks

This value is expressed in Hz.

Use "carrier<k>" as the selector string to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaf09c17a9a2b453ccac7420869f096198.html language=enus -->
## TOPIC 00157: RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaf09c17a9a2b453ccac7420869f096198.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__carrier_1gaf09c17a9a2b453ccac7420869f096198.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To5275693float64Read-OnlyCarrierRemarks This value is expressed in dBm.The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidt

### RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

Returns the carrier power.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275693 | float64 | Read-Only | Carrier |

#### Remarks

This value is expressed in dBm.

The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the value of the [RFMXWCDMA_ATTR_CENTER_FREQUENCY](group____root__ni_r_fmx_w_c_d_m_a__attributes_1gabfed4607523c2852023190b88efd267c.html) and the [RFMXWCDMA_ATTR_CARRIER_FREQUENCY](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier_1gacfc638beac56d7c91cb233c418af971f.html) attributes.

Use "carrier<k>" as the selector string to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset.html language=enus -->
## TOPIC 00158: Lower Offset

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERReturns the power measured in the lower, or negative, offset segment. RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWERReturns the peak power measured in the lower, or negative, offset se

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER | Returns the power measured in the lower, or negative, offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER | Returns the peak power measured in the lower, or negative, offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN | Returns the margin of the lower offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power at the frequency corresponding to the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY | Returns the frequency corresponding to the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power at the frequency corresponding to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute and relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS | Indicates the measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power is observed in the lower offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER | Returns the power measured in the lower, or negative, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER | Returns the peak power measured in the lower, or negative, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga10d6e223580aff6fe970b25a60f57793.html language=enus -->
## TOPIC 00159: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga10d6e223580aff6fe970b25a60f57793.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga10d6e223580aff6fe970b25a60f57793.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the lower, or negative, offset segment. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To5275702float64Read-OnlyOffsetRemarks This value is expressed in dBm.Use "offset<n>" as the selector string to read this re

### RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

Returns the peak power measured in the lower, or negative, offset segment.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275702 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dBm.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga367ce46d1493032356c7341de42300c6.html language=enus -->
## TOPIC 00160: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga367ce46d1493032356c7341de42300c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga367ce46d1493032356c7341de42300c6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To5275709int32Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to read this result.

### RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

Indicates the measurement status based on the [RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1gaec35a37b864977bf8434294634c5f5af.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275709 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the value of the SEM Results Lower Offset Margin attribute is positive. |
| RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the value of the SEM Results Lower Offset Margin attribute is zero or negative. |

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga67170e573fdede20eba112c9c7b0630e.html language=enus -->
## TOPIC 00161: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga67170e573fdede20eba112c9c7b0630e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga67170e573fdede20eba112c9c7b0630e.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at the frequency corresponding to the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To5275706float64Read-OnlyOffsetRemarks This value is expressed in dBm.Use "offset<n

### RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

Returns the power at the frequency corresponding to the [RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1gaec35a37b864977bf8434294634c5f5af.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275706 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dBm.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga8e071632e1718d1ddd6117793d498b77.html language=enus -->
## TOPIC 00162: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga8e071632e1718d1ddd6117793d498b77.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga8e071632e1718d1ddd6117793d498b77.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the lower, or negative, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To5275703float64Read-OnlyOffsetRemarks This value i

### RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power measured in the lower, or negative, offset segment relative to the [RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275703 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dB.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga9f5889bc0e7882f8914dd2371c9bf34c.html language=enus -->
## TOPIC 00163: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga9f5889bc0e7882f8914dd2371c9bf34c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1ga9f5889bc0e7882f8914dd2371c9bf34c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the lower, or negative, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To5275701float64Read-OnlyOffsetRemarks This value

### RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power measured in the lower, or negative, offset segment relative to the [RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275701 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dB.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1gaec35a37b864977bf8434294634c5f5af.html language=enus -->
## TOPIC 00164: RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1gaec35a37b864977bf8434294634c5f5af.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__lower__offset_1gaec35a37b864977bf8434294634c5f5af.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin of the lower offset segment. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGINNumeric ValueData TypeAccessApplies To5275705float64Read-OnlyOffsetRemarks This value is expressed in dB.In a single carrier SEM, the maximum value of the absolute spectrum trace with reference to the

### RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

Returns the margin of the lower offset segment.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275705 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dB.

In a single carrier SEM, the maximum value of the absolute spectrum trace with reference to the standard-defined absolute mask limit of the lower offset segment is measured. The maximum relative spectrum trace with reference to the standard-defined relative mask limit of the lower offset segment is also measured. The minimum of these two values is the margin.

In a multicarrier SEM, the maximum value of the absolute spectrum trace with reference to the standard-defined absolute mask limit of the lower offset segment is the margin.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset.html language=enus -->
## TOPIC 00165: Upper Offset

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWERReturns the power measured in the upper, or positive, offset segment. RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWERReturns the peak power measured in the upper, or positive, offset se

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER | Returns the power measured in the upper, or positive, offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER | Returns the peak power measured in the upper, or positive, offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN | Returns the margin of the upper offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power at the frequency corresponding to the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY | Returns the frequency corresponding to the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. This value is expressed in Hz. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power at the frequency corresponding to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute relative to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS | Indicates the measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power is observed in the upper offset segment. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER | Returns the power measured in the upper, or positive, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. |
| RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER | Returns the peak power measured in the upper, or positive, offset segment relative to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga2b33dc8506010494ffb8be0d72294986.html language=enus -->
## TOPIC 00166: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga2b33dc8506010494ffb8be0d72294986.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga2b33dc8506010494ffb8be0d72294986.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To5275722int32Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to read this result.

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

Indicates the measurement status based on the [RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gaefb66d5e2314a3fd0d8dca00079882bd.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275722 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The value of the SEM Results Upper Offset Margin attribute is positive. |
| RFMXWCDMA_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | The value of the SEM Results Upper Offset Margin attribute is zero or negative. |

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga2bd236a2d4d28768193dd20f8953cbff.html language=enus -->
## TOPIC 00167: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga2bd236a2d4d28768193dd20f8953cbff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga2bd236a2d4d28768193dd20f8953cbff.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at the frequency corresponding to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute relative to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_REL

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

Returns the power at the frequency corresponding to the value of the [RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gaefb66d5e2314a3fd0d8dca00079882bd.html) attribute relative to the value of the [RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html) attribute. This value is expressed in dB.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275720 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga3d08b04c4b6f35966093cdecb61fb36f.html language=enus -->
## TOPIC 00168: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga3d08b04c4b6f35966093cdecb61fb36f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga3d08b04c4b6f35966093cdecb61fb36f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper, or positive, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To5275714float64Read-OnlyOffsetRemarks This value

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power measured in the upper, or positive, offset segment relative to the [RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275714 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dB.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga6d8a8b2074a055faead816dc8226fd1a.html language=enus -->
## TOPIC 00169: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga6d8a8b2074a055faead816dc8226fd1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga6d8a8b2074a055faead816dc8226fd1a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper, or positive, offset segment. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To5275713float64Read-OnlyOffsetRemarks This value is expressed in dBm.Use "offset<n>" as the selector string to read this r

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER

Returns the power measured in the upper, or positive, offset segment.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275713 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dBm.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga7b7d4a53a86a35b9c9357b1e3484e3ed.html language=enus -->
## TOPIC 00170: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga7b7d4a53a86a35b9c9357b1e3484e3ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga7b7d4a53a86a35b9c9357b1e3484e3ed.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper, or positive, offset segment. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWERNumeric ValueData TypeAccessApplies To5275715float64Read-OnlyOffsetRemarks This value is expressed in dBm.Use "offset<n>" as the selector string to read this re

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

Returns the peak power measured in the upper, or positive, offset segment.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275715 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dBm.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga82e08fdec18eb9831fd34a19d1b7f94d.html language=enus -->
## TOPIC 00171: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga82e08fdec18eb9831fd34a19d1b7f94d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1ga82e08fdec18eb9831fd34a19d1b7f94d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency corresponding to the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. This value is expressed in Hz. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCYNumeric ValueData TypeAccessApplies To5275721float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

Returns the frequency corresponding to the [RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gaefb66d5e2314a3fd0d8dca00079882bd.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275721 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gac4ab8b80a68922eacbf496a4b4b95c40.html language=enus -->
## TOPIC 00172: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gac4ab8b80a68922eacbf496a4b4b95c40.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gac4ab8b80a68922eacbf496a4b4b95c40.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at the frequency corresponding to the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To5275719float64Read-OnlyOffsetRemarks This value is expressed in dBm.Use "offset<n

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

Returns the power at the frequency corresponding to the [RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gaefb66d5e2314a3fd0d8dca00079882bd.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275719 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dBm.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gac66e2a223297a4647e80ac3c367a26ac.html language=enus -->
## TOPIC 00173: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gac66e2a223297a4647e80ac3c367a26ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gac66e2a223297a4647e80ac3c367a26ac.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper, or positive, offset segment relative to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To5275716float64Read-OnlyOffsetRemarks

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power measured in the upper, or positive, offset segment relative to the value of the [RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results_1ga356ce017d68488da1bbcbcbce63e6350.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275716 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in dB.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gadf9f913a4d3a9c2d901c356be48a15a2.html language=enus -->
## TOPIC 00174: RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gadf9f913a4d3a9c2d901c356be48a15a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__results__upper__offset_1gadf9f913a4d3a9c2d901c356be48a15a2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power is observed in the upper offset segment. SyntaxRFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To5275717float64Read-OnlyOffsetRemarks This value is expressed in Hz.Use "offset<n>" as the selector string to read t

### RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

Returns the frequency at which the peak power is observed in the upper offset segment.

#### Syntax

RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275717 | float64 | Read-Only | Offset |

#### Remarks

This value is expressed in Hz.

Use "offset<n>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__sweep__time_1ga0aa82e1fe0c35d6b45244b0d3d5c27b6.html language=enus -->
## TOPIC 00175: RFMXWCDMA_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__sweep__time_1ga0aa82e1fe0c35d6b45244b0d3d5c27b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__sweep__time_1ga0aa82e1fe0c35d6b45244b0d3d5c27b6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXWCDMA_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. SyntaxRFMXWCDMA_ATTR_SEM_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To5275686float64Read/WriteN/ARemarks This value is expressed in seconds.You do not need to use a selector string to configu

### RFMXWCDMA_ATTR_SEM_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXWCDMA_ATTR_SEM_SWEEP_TIME_AUTO](group____root__ni_r_fmx_w_c_d_m_a__attributes__sem__sweep__time_1ga204e7ceb0c698b45ee65b27c4c535f10.html) attribute to **False**.

#### Syntax

RFMXWCDMA_ATTR_SEM_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5275686 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase.html language=enus -->
## TOPIC 00176: SlotPhase

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsResultsGroup membersNameDescriptionRFMXWCDMA_ATTR_SLOTPHASE_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_ENABLEDSpecifies whether to enable the SlotPhase measurement. RFMXWCD

### SlotPhase

#### Groups

- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SLOTPHASE_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. |
| RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_ENABLED | Specifies whether to enable the SlotPhase measurement. |
| RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_LENGTH | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. |
| RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE attribute. |
| RFMXWCDMA_ATTR_SLOTPHASE_RRC_FILTER_ENABLED | Specifies whether to enable the RRC filter. Use this attribute to disable the filter if the received signal is already RRC-filtered. |
| RFMXWCDMA_ATTR_SLOTPHASE_SPECTRUM_INVERTED | Specifies whether the signal spectrum is inverted. |
| RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame or the slot boundary. |
| RFMXWCDMA_ATTR_SLOTPHASE_TRANSIENT_REMOVAL_ENABLED | Specifies whether the SlotPhase measurement excludes 25 microseconds from the start and end of each slot while computing the linear-fit chip phase error, which is used to compute phase discontinuities at the slot boundaries. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga1defa50a74890847e69664254de01dab.html language=enus -->
## TOPIC 00177: RFMXWCDMA_ATTR_SLOTPHASE_SPECTRUM_INVERTED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga1defa50a74890847e69664254de01dab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga1defa50a74890847e69664254de01dab.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal spectrum is inverted. SyntaxRFMXWCDMA_ATTR_SLOTPHASE_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To5324807int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXWCDMA_ATTR_SLOTPHASE_SPECTRUM_INVERTED

Specifies whether the signal spectrum is inverted.

#### Syntax

RFMXWCDMA_ATTR_SLOTPHASE_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5324807 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The spectrum is not inverted. |
| RFMXWCDMA_VAL_SLOTPHASE_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The spectrum is inverted. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga2e1f58e52466ee9e62c84c02be8943be.html language=enus -->
## TOPIC 00178: RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga2e1f58e52466ee9e62c84c02be8943be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga2e1f58e52466ee9e62c84c02be8943be.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPhase measurement. SyntaxRFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5324800int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the S

### RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

Specifies whether to enable the SlotPhase measurement.

#### Syntax

RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5324800 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga4b983a28156b62489a6b1f1f2a8a7dd7.html language=enus -->
## TOPIC 00179: RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga4b983a28156b62489a6b1f1f2a8a7dd7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1ga4b983a28156b62489a6b1f1f2a8a7dd7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE attribute. SyntaxRFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies

### RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1gafe52334cb7fbde54bbb413aa6d07e8e4.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5324803 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. The valid values are any value greater than or equal to 0.

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1gafe52334cb7fbde54bbb413aa6d07e8e4.html language=enus -->
## TOPIC 00180: RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1gafe52334cb7fbde54bbb413aa6d07e8e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase_1gafe52334cb7fbde54bbb413aa6d07e8e4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxRFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To5324802int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default s

### RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5324802 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length attribute starting at SlotPhase Meas Offset slots from the slot boundary. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results.html language=enus -->
## TOPIC 00181: Results

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1Returns the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_CO

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1 | Returns the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. |
| RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT2 | Returns the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. |
| RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_MINIMUM_DISTANCE | Returns the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. |
| RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY | Returns the maximum of all the measured phase discontinuity values at the slot boundaries. |

#### Attachments

None

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga44afc21ba4468c15b8192e268040acec.html language=enus -->
## TOPIC 00182: RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga44afc21ba4468c15b8192e268040acec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga44afc21ba4468c15b8192e268040acec.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. SyntaxRFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1Numeric ValueData TypeAccessApplies To5324815int32Read-OnlyN/ARemarks You do not

### RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1

Returns the number of times the phase discontinuity values exceed the *Limit 1* value for the acquired signal. *Limit 1* is fixed at 36 degrees.

#### Syntax

RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5324815 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga522aa0fac0aa1d90880e5fa07e883c46.html language=enus -->
## TOPIC 00183: RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_MINIMUM_DISTANCE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga522aa0fac0aa1d90880e5fa07e883c46.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga522aa0fac0aa1d90880e5fa07e883c46.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. SyntaxRFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_MINIMUM_DISTANCENumeric ValueData TypeAccessApplies To5324817int32Read-OnlyN/A

### RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_MINIMUM_DISTANCE

Returns the minimum distance between two phase discontinuity measurements exceeding the *Limit 1* value. *Limit 1* is fixed at 36 degrees. This value is expressed in slots.

#### Syntax

RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_MINIMUM_DISTANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5324817 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

If there are no phase discontinuity values greater than *Limit 1*, or if there is only one phase discontinuity value greater than *Limit 1*, this result is not valid. In such a case, -1 is reported as the result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga58598c93756157489cbffb308ff448f2.html language=enus -->
## TOPIC 00184: RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga58598c93756157489cbffb308ff448f2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotphase__results_1ga58598c93756157489cbffb308ff448f2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of all the measured phase discontinuity values at the slot boundaries. SyntaxRFMXWCDMA_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITYNumeric ValueData TypeAccessApplies To5324814float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for defaul

### RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY

Returns the maximum of all the measured phase discontinuity values at the slot boundaries.

#### Syntax

RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5324814 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

This value is expressed in degrees.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower.html language=enus -->
## TOPIC 00185: SlotPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLEDSpecifies whether to enable the SlotPower measurement. RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTHSpecifies the duration of the SlotPower measurement. This value is expressed in slots. RFMXWCDMA_ATTR_SLOTPOWER_MEASUREM

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLED | Specifies whether to enable the SlotPower measurement. |
| RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH | Specifies the duration of the SlotPower measurement. This value is expressed in slots. |
| RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE attribute. |
| RFMXWCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED | Specifies whether to enable the RRC filter. |
| RFMXWCDMA_ATTR_SLOTPOWER_SPECTRUM_INVERTED | Specifies whether the spectrum of the signal is inverted. |
| RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE | Specifies whether the measurement is performed from the frame or slot boundary. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga0ba5039521a6f5987b745c9d920dd72b.html language=enus -->
## TOPIC 00186: RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga0ba5039521a6f5987b745c9d920dd72b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga0ba5039521a6f5987b745c9d920dd72b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE attribute. SyntaxRFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies

### RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1gaaba40955fb86fc725786938e54334ea5.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5332994 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. The valid values are any value greater than or equal to 0.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga37b9ce43c78d3bda84fa224e3f48b7a5.html language=enus -->
## TOPIC 00187: RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga37b9ce43c78d3bda84fa224e3f48b7a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga37b9ce43c78d3bda84fa224e3f48b7a5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPower measurement. SyntaxRFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To5332992int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the S

### RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

Specifies whether to enable the SlotPower measurement.

#### Syntax

RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5332992 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga58e561d79c5dcbd7e002f6a1171016e8.html language=enus -->
## TOPIC 00188: RFMXWCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga58e561d79c5dcbd7e002f6a1171016e8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1ga58e561d79c5dcbd7e002f6a1171016e8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the RRC filter. SyntaxRFMXWCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To5332997int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Stri

### RFMXWCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED

Specifies whether to enable the RRC filter.

#### Syntax

RFMXWCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5332997 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SLOTPOWER_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | Disables the RRC filter in the measurement. |
| RFMXWCDMA_VAL_SLOTPOWER_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | Enables the RRC filter in the measurement. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1gaaba40955fb86fc725786938e54334ea5.html language=enus -->
## TOPIC 00189: RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1gaaba40955fb86fc725786938e54334ea5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1gaaba40955fb86fc725786938e54334ea5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. SyntaxRFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To5332999int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signa

### RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

Specifies whether the measurement is performed from the frame or slot boundary.

#### Syntax

RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5332999 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary. |
| RFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPower Measurement Length attribute starting at SlotPower Measurement Offset slots from the slot boundary. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1gab25c984461ffbf64a47c08b67b87673f.html language=enus -->
## TOPIC 00190: RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1gab25c984461ffbf64a47c08b67b87673f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__slotpower_1gab25c984461ffbf64a47c08b67b87673f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the SlotPower measurement. This value is expressed in slots. SyntaxRFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To5332995int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

Specifies the duration of the SlotPower measurement. This value is expressed in slots.

#### Syntax

RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5332995 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 15. The valid values are any value greater than or equal to 1.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger.html language=enus -->
## TOPIC 00191: Trigger

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXWCDMA_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. RFMXWCDMA_ATTR_TRIGGER_TYPESpecifies the trigger type. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. |
| RFMXWCDMA_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__digital__edge_1ga58db34dd8a10fd501cc8b2ef88b261b2.html language=enus -->
## TOPIC 00192: RFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__digital__edge_1ga58db34dd8a10fd501cc8b2ef88b261b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__digital__edge_1ga58db34dd8a10fd501cc8b2ef88b261b2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital edge trigger. SyntaxRFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To5242885char[]Read/WriteN/ARemarks This attribute is used only when you set the RFMXWCDMA_ATTR_TRIGGER_TYPE attribute to Digital Edge.You do not need to us

### RFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

Specifies the source terminal for the digital edge trigger.

#### Syntax

RFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242885 | char[] | Read/Write | N/A |

#### Remarks

This attribute is used only when you set the [RFMXWCDMA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger_1ga6f9fbf39fde9877c523d54a2cfecda02.html) attribute to **Digital Edge**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge.html language=enus -->
## TOPIC 00193: IQ Power Edge

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVELSpecifies the power level at which the device triggers. RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPESpecifies the reference for the RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. RFMXWCDMA_ATTR_IQ_POWER_EDGE_TR

### IQ Power Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL | Specifies the power level at which the device triggers. |
| RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE | Specifies the reference for the RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. |
| RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. |
| RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXWCDMA_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1ga037c5c08dbbe7340487e809728a9677a.html language=enus -->
## TOPIC 00194: RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1ga037c5c08dbbe7340487e809728a9677a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1ga037c5c08dbbe7340487e809728a9677a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXWCDMA_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To5242887char[]Read/WriteN/ARemarks You do not n

### RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the [RFMXWCDMA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger_1ga6f9fbf39fde9877c523d54a2cfecda02.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242887 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1ga220bdc795cf4d25b0a36a667c74679e7.html language=enus -->
## TOPIC 00195: RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1ga220bdc795cf4d25b0a36a667c74679e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1ga220bdc795cf4d25b0a36a667c74679e7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level at which the device triggers. SyntaxRFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVELNumeric ValueData TypeAccessApplies To5242888float64Read/WriteN/ARemarks This value is expressed in dB when the RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute is set to Relative and in

### RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

Specifies the power level at which the device triggers.

#### Syntax

RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242888 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in dB when the [RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae8d22338ea489edc3b347f0d2c43dc19.html) attribute is set to **Relative** and in dBm when the IQ Power Edge Level Type attribute is set to **Absolute**.

The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the [RFMXWCDMA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger_1ga6f9fbf39fde9877c523d54a2cfecda02.html) attribute to **IQ Power Edge**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae44d85db053c5b2327f444f032286a11.html language=enus -->
## TOPIC 00196: RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae44d85db053c5b2327f444f032286a11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae44d85db053c5b2327f444f032286a11.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. SyntaxRFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPENumeric ValueData TypeAccessApplies To5242889int32Read/WriteN/ARemarks The device asserts the trigger when the signal power exceeds the specified le

### RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling.

#### Syntax

RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242889 | int32 | Read/Write | N/A |

#### Remarks

The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the [RFMXWCDMA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger_1ga6f9fbf39fde9877c523d54a2cfecda02.html) attribute to **IQ Power Edge**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae8d22338ea489edc3b347f0d2c43dc19.html language=enus -->
## TOPIC 00197: RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae8d22338ea489edc3b347f0d2c43dc19.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae8d22338ea489edc3b347f0d2c43dc19.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. SyntaxRFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPENumeric ValueData TypeAccessApplies To5246975int32Read/WriteN/ARemarks The IQ Power Edge Level Type attribute is used only when you set the RFMXWCDMA_ATTR_TRIGGE

### RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

Specifies the reference for the [RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1ga220bdc795cf4d25b0a36a667c74679e7.html) attribute.

#### Syntax

RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5246975 | int32 | Read/Write | N/A |

#### Remarks

The IQ Power Edge Level Type attribute is used only when you set the [RFMXWCDMA_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger_1ga6f9fbf39fde9877c523d54a2cfecda02.html) attribute to **IQ Power Edge**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The IQ Power Edge Level attribute is relative to the value of the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute. |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00198: Minimum Quiet Time

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODESpecifies whether the measurement computes

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. |
| RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time_1ga54060941212ee713fe53c13d57038127.html language=enus -->
## TOPIC 00199: RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time_1ga54060941212ee713fe53c13d57038127.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time_1ga54060941212ee713fe53c13d57038127.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxRFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODENumeric ValueData TypeAccessApplies To5242891int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defau

### RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242891 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Manual**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time_1ga889be1e08c8872702f052253e7648957.html language=enus -->
## TOPIC 00200: RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time_1ga889be1e08c8872702f052253e7648957.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__minimum__quiet__time_1ga889be1e08c8872702f052253e7648957.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. SyntaxRFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONNumeric ValueData TypeAccessApplies To5242892float64Read/WriteN/ARemarks This value is expressed in seconds.If you set th

### RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger.

#### Syntax

RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5242892 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in seconds.

If you set the [RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE](group____root__ni_r_fmx_w_c_d_m_a__attributes__trigger__iq__power__edge_1gae44d85db053c5b2327f444f032286a11.html) attribute to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions.html language=enus -->
## TOPIC 00201: Functions

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedBuild StringConfigurationFetchSelect MeasurementSet and Get AttributesUtilityGroup membersNameDescriptionRFmxWCDMA_CloseCloses the session to the device. RFmxWCDMA_GetErrorRetrieves and then clears the error information for the session or the current execution thread. You must provide

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
| RFmxWCDMA_Close | Closes the session to the device. |
| RFmxWCDMA_GetError | Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxWCDMA_GetErrorString | Converts a status code returned by an RFmxWCDMA function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxWCDMA_Initialize | Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. |
| RFmxWCDMA_Initiate | Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the RFmxWCDMA Attribute. |

#### Attachments

None

Parent topic:

niRFmxWCDMA.h

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions_1ga788e3374525bfd8899668468043c6569.html language=enus -->
## TOPIC 00202: RFmxWCDMA_GetErrorString

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions_1ga788e3374525bfd8899668468043c6569.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions_1ga788e3374525bfd8899668468043c6569.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxWCDMA function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxWCDMA_GetErrorString(niRFmxInstrHandle

### RFmxWCDMA_GetErrorString

Converts a status code returned by an RFmxWCDMA function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxWCDMA function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions_1ga8bd17a09cfd73e2d24f075d7b3703051.html language=enus -->
## TOPIC 00203: RFmxWCDMA_Initiate

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions_1ga8bd17a09cfd73e2d24f075d7b3703051.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions_1ga8bd17a09cfd73e2d24f075d7b3703051.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in

### RFmxWCDMA_Initiate

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the RFmxWCDMA Attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])

#### Remarks

To get the status of measurements, use the [RFmxWCDMA_WaitForMeasurementComplete](group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga928d88e79a0ac23f6f521da1b4872b11.html) function or the [RFmxWCDMA_CheckMeasurementStatus](group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga8668dd75d5b6b2f554b79069010c82fa.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance.Example:"result::r1""r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html language=enus -->
## TOPIC 00204: RFmxWCDMA_GetError

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxWCDMA_GetError(niRFmxInstrH

### RFmxWCDMA_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxWCDMA_GetErrorString](group____root__ni_r_fmx_w_c_d_m_a__functions_1ga788e3374525bfd8899668468043c6569.html) function if the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function does not return an error message.

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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced.html language=enus -->
## TOPIC 00205: Advanced

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAnalyze2Group membersNameDescriptionRFmxWCDMA_AbortMeasurementsStops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxWCDMA_Initiate function or measurement read functions. Calling this fu

### Advanced

#### Groups

- Analyze2

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxWCDMA_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error. |
| RFmxWCDMA_ClearAllNamedResults | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxWCDMA_ClearNamedResult | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxWCDMA_CloneSignalConfiguration | Creates a new instance of a signal by copying all the attribute values from an existing signal instance. |
| RFmxWCDMA_CreateSignalConfiguration | Creates a new instance of a signal. |
| RFmxWCDMA_DeleteSignalConfiguration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxWCDMA_GetAllNamedResultNames | Returns the named result names of the signal that you specify in the Selector String parameter. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga0234aaa35a2fd13e5a82b7a3f1af25c4.html language=enus -->
## TOPIC 00206: RFmxWCDMA_GetAllNamedResultNames

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga0234aaa35a2fd13e5a82b7a3f1af25c4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga0234aaa35a2fd13e5a82b7a3f1af25c4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxWCDMA_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defa

### RFmxWCDMA_GetAllNamedResultNames

Returns the named result names of the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga0dd0307a949d76740f5d72525d5369f8.html language=enus -->
## TOPIC 00207: RFmxWCDMA_CreateSignalConfiguration

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga0dd0307a949d76740f5d72525d5369f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga0dd0307a949d76740f5d72525d5369f8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxWCDMA_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obt

### RFmxWCDMA_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxWCDMA_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga365eb81bff516e7fe4e48610fe56eb8b.html language=enus -->
## TOPIC 00208: RFmxWCDMA_DeleteSignalConfiguration

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga365eb81bff516e7fe4e48610fe56eb8b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga365eb81bff516e7fe4e48610fe56eb8b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. Syntaxint32 __stdcall RFmxWCDMA_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx

### RFmxWCDMA_DeleteSignalConfiguration

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga49940a9d954be5acbca85ff0ee239cab.html language=enus -->
## TOPIC 00209: RFmxWCDMA_ClearAllNamedResults

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga49940a9d954be5acbca85ff0ee239cab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga49940a9d954be5acbca85ff0ee239cab.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxWCDMA_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxWCDMA_ClearAllNamedResults

Clears all results for the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga84b95164119c5fc28ebd5acd605dd3b1.html language=enus -->
## TOPIC 00210: RFmxWCDMA_ClearNamedResult

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga84b95164119c5fc28ebd5acd605dd3b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1ga84b95164119c5fc28ebd5acd605dd3b1.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. Syntaxint32 __stdcall RFmxWCDMA_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the R

### RFmxWCDMA_ClearNamedResult

Clears a result instance specified by the result name in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1gabce9f797af1206b5c9bb2294830c0729.html language=enus -->
## TOPIC 00211: RFmxWCDMA_CloneSignalConfiguration

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1gabce9f797af1206b5c9bb2294830c0729.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1gabce9f797af1206b5c9bb2294830c0729.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the attribute values from an existing signal instance. Syntaxint32 __stdcall RFmxWCDMA_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]n

### RFmxWCDMA_CloneSignalConfiguration

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Syntax

int32 __stdcall RFmxWCDMA_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| oldSignalName | [in] | char[] | This parameter specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::OldSigName""OldSigName" |
| newSignalName | [in] | char[] | This parameter specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::NewSigName""NewSigName" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1gaf637380de3f94399e441d05fdd292d20.html language=enus -->
## TOPIC 00212: RFmxWCDMA_AbortMeasurements

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1gaf637380de3f94399e441d05fdd292d20.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__advanced_1gaf637380de3f94399e441d05fdd292d20.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxWCDMA_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it i

### RFmxWCDMA_AbortMeasurements

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxWCDMA_Initiate](group____root__ni_r_fmx_w_c_d_m_a__functions_1ga8bd17a09cfd73e2d24f075d7b3703051.html) function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxWCDMA_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__build__string.html language=enus -->
## TOPIC 00213: Build String

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__build__string.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_BuildCarrierStringCreates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch functions, properties, and results. RFmxWCDMA_BuildChannelStringCreates the channel string to use as the selector string with

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_BuildCarrierString | Creates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch functions, properties, and results. |
| RFmxWCDMA_BuildChannelString | Creates the channel string to use as the selector string with the channel configuration and results. |
| RFmxWCDMA_BuildOffsetString | Creates the offset string to use as the selector string with the SEM and ACP offset configuration or fetch attributes and functions. |
| RFmxWCDMA_BuildSignalString | Creates selector string for use with configuration or fetch attributes and functions. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__build__string_1ga7fb0eae3262179642267b2d9708354e4.html language=enus -->
## TOPIC 00214: RFmxWCDMA_BuildChannelString

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__build__string_1ga7fb0eae3262179642267b2d9708354e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__build__string_1ga7fb0eae3262179642267b2d9708354e4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the channel string to use as the selector string with the channel configuration and results. Syntaxint32 __stdcall RFmxWCDMA_BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorSt

### RFmxWCDMA_BuildChannelString

Creates the channel string to use as the selector string with the channel configuration and results.

#### Syntax

int32 __stdcall RFmxWCDMA_BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| channelNumber | [in] | int32 | This parameter specifies the channel number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string that can be passed to the Selector String parameter of Fetch functions. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__build__string_1gaaaaab6ea40532ae4ceee47efdd660ee0.html language=enus -->
## TOPIC 00215: RFmxWCDMA_BuildSignalString

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__build__string_1gaaaaab6ea40532ae4ceee47efdd660ee0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__build__string_1gaaaaab6ea40532ae4ceee47efdd660ee0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxWCDMA_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])ParametersNameDirectionTypeDescriptionsignalName[in]char[]This parameter spe

### RFmxWCDMA_BuildSignalString

Creates selector string for use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxWCDMA_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Example:"signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string).Example:"result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter returns the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration.html language=enus -->
## TOPIC 00216: Configuration

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPArraysCDACHPFrequencyModAccOBWQEVMSEMSlotPhaseSlotPowerTriggerGroup membersNameDescriptionRFmxWCDMA_AutoLevelExamines the input signal to calculate the peak power level and sets it as the value of the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approxima

### Configuration

#### Groups

- ACP
- Arrays
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
| RFmxWCDMA_AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. |
| RFmxWCDMA_CfgBand | Configures the Universal Mobile Telecommunications System (UMTS) operating band. |
| RFmxWCDMA_CfgCarrierFrequency | Configures the center frequency of the carrier, relative to the RF center frequency. |
| RFmxWCDMA_CfgChannelConfigurationMode | Configures the channel configuration mode. |
| RFmxWCDMA_CfgContiguousCarriers | Configures the contiguous carriers based on the number of carriers and the carrier at the center frequency. |
| RFmxWCDMA_CfgExternalAttenuation | Configures the external attenuation. |
| RFmxWCDMA_CfgFrequencyReference | Configures the Reference Clock and the frequency reference source. |
| RFmxWCDMA_CfgMechanicalAttenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxWCDMA_CfgNumberOfCarriers | Configures the number of carriers for ACP, CHP, OBW, SEM, and ModAcc measurements. |
| RFmxWCDMA_CfgNumberOfChannels | Configures the number of user-defined channels for the measurement. This function is used when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. Call this function before you call the RFmxWCDMA_CfgUserDefinedChannelArray function or the RFmxWCDMA_CfgUserDefinedChannel function. |
| RFmxWCDMA_CfgRF | Configures the RF attributes of the signal specified by the selector string. |
| RFmxWCDMA_CfgRFAttenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxWCDMA_CfgReferenceLevel | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| RFmxWCDMA_CfgUplinkScrambling | Configures the uplink scrambling type and the scrambling code. |
| RFmxWCDMA_CfgUplinkTestModel | Configures the uplink test model. |
| RFmxWCDMA_CfgUserDefinedChannel | Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this function, you must configure the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute with the appropriate number of channels. |
| RFmxWCDMA_SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxWCDMA Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga23b0241be571778f4a6651b9ee68fd46.html language=enus -->
## TOPIC 00217: RFmxWCDMA_CfgUplinkTestModel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga23b0241be571778f4a6651b9ee68fd46.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga23b0241be571778f4a6651b9ee68fd46.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the uplink test model. Syntaxint32 __stdcall RFmxWCDMA_CfgUplinkTestModel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkTestModel)RemarksUse "carrier<n>" as the selector string to configure this function.ParametersNameDirectionTypeDescriptioninstrumentHandle[in]ni

### RFmxWCDMA_CfgUplinkTestModel

Configures the uplink test model.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgUplinkTestModel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkTestModel)

#### Remarks

Use "carrier<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| uplinkTestModel | [in] | int32 | This parameter specifies the uplink test model when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Test Model.Each test model is a set of channel configurations defined by the standard.Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<n>, where n is the oldest release number with a given set of channel configurations. The default value is R6 C.2.1.NameValueDescriptionRFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_10 (0x0)The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_21 (0x1)The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_32 (0x2)The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_43 (0x3)The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_54 (0x4)The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST15 (0x5)The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST26 (0x6)The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST37 (0x7)The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST48 (0x8)The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST59 (0x9)The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST610 (0xa)The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST111 (0xb)The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST212 (0xc)The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST313 (0xd)The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST414 (0xe)The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST115 (0xf)The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST216 (0x10)The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST317 (0x11)The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST418 (0x12)The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST519 (0x13)The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST120 (0x14)The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST221 (0x15)The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST322 (0x16)The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST423 (0x17)The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST524 (0x18)The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_4_SUBTEST125 (0x19)The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_1 | 0 (0x0) | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_2 | 1 (0x1) | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_3 | 2 (0x2) | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_4 | 3 (0x3) | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_5 | 4 (0x4) | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST1 | 5 (0x5) | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST2 | 6 (0x6) | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST3 | 7 (0x7) | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST4 | 8 (0x8) | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST5 | 9 (0x9) | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST6 | 10 (0xa) | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST1 | 11 (0xb) | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST2 | 12 (0xc) | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST3 | 13 (0xd) | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST4 | 14 (0xe) | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST1 | 15 (0xf) | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST2 | 16 (0x10) | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST3 | 17 (0x11) | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST4 | 18 (0x12) | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST5 | 19 (0x13) | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST1 | 20 (0x14) | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST2 | 21 (0x15) | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST3 | 22 (0x16) | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST4 | 23 (0x17) | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST5 | 24 (0x18) | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_4_SUBTEST1 | 25 (0x19) | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3983b23c83c4d08c84835df51a306dc0.html language=enus -->
## TOPIC 00218: RFmxWCDMA_CfgBand

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3983b23c83c4d08c84835df51a306dc0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3983b23c83c4d08c84835df51a306dc0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Universal Mobile Telecommunications System (UMTS) operating band. Syntaxint32 __stdcall RFmxWCDMA_CfgBand(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 band)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx

### RFmxWCDMA_CfgBand

Configures the Universal Mobile Telecommunications System (UMTS) operating band.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgBand(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 band)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| band | [in] | int32 | This parameter specifies the UMTS operation band. The default value is 1.Name (Value)Description1 (1)The terminal operates in UMTS Band I.2 (2)The terminal operates in UMTS Band II.3 (3)The terminal operates in UMTS Band III.4 (4)The terminal operates in UMTS Band IV.5 (5)The terminal operates in UMTS Band V.6 (6)The terminal operates in UMTS Band function.7 (7)The terminal operates in UMTS Band VII.8 (8)The terminal operates in UMTS Band VIII.9 (9)The terminal operates in UMTS Band IX.10 (10)The terminal operates in UMTS Band X.11 (11)The terminal operates in UMTS Band XI.12 (12)The terminal operates in UMTS Band XII.13 (13)The terminal operates in UMTS Band XIII.14 (14)The terminal operates in UMTS Band XIV.19 (19)The terminal operates in UMTS Band XIX.20 (20)The terminal operates in UMTS Band XX.21 (21)The terminal operates in UMTS Band XXI.22 (22)The terminal operates in UMTS Band XXII.25 (25)The terminal operates in UMTS Band XXV.26 (26)The terminal operates in UMTS Band XXVI. |
| Name (Value) | Description |  |  |
| 1 (1) | The terminal operates in UMTS Band I. |  |  |
| 2 (2) | The terminal operates in UMTS Band II. |  |  |
| 3 (3) | The terminal operates in UMTS Band III. |  |  |
| 4 (4) | The terminal operates in UMTS Band IV. |  |  |
| 5 (5) | The terminal operates in UMTS Band V. |  |  |
| 6 (6) | The terminal operates in UMTS Band function. |  |  |
| 7 (7) | The terminal operates in UMTS Band VII. |  |  |
| 8 (8) | The terminal operates in UMTS Band VIII. |  |  |
| 9 (9) | The terminal operates in UMTS Band IX. |  |  |
| 10 (10) | The terminal operates in UMTS Band X. |  |  |
| 11 (11) | The terminal operates in UMTS Band XI. |  |  |
| 12 (12) | The terminal operates in UMTS Band XII. |  |  |
| 13 (13) | The terminal operates in UMTS Band XIII. |  |  |
| 14 (14) | The terminal operates in UMTS Band XIV. |  |  |
| 19 (19) | The terminal operates in UMTS Band XIX. |  |  |
| 20 (20) | The terminal operates in UMTS Band XX. |  |  |
| 21 (21) | The terminal operates in UMTS Band XXI. |  |  |
| 22 (22) | The terminal operates in UMTS Band XXII. |  |  |
| 25 (25) | The terminal operates in UMTS Band XXV. |  |  |
| 26 (26) | The terminal operates in UMTS Band XXVI. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3e51a8b32e74df82ff615cc71840d53f.html language=enus -->
## TOPIC 00219: RFmxWCDMA_CfgUplinkScrambling

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3e51a8b32e74df82ff615cc71840d53f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3e51a8b32e74df82ff615cc71840d53f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the uplink scrambling type and the scrambling code. Syntaxint32 __stdcall RFmxWCDMA_CfgUplinkScrambling(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkScramblingCode, int32 uplinkScramblingType)RemarksUse "carrier<n>" as the selector string to configure this functi

### RFmxWCDMA_CfgUplinkScrambling

Configures the uplink scrambling type and the scrambling code.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgUplinkScrambling(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkScramblingCode, int32 uplinkScramblingType)

#### Remarks

Use "carrier<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| uplinkScramblingCode | [in] | int32 | This parameter specifies the scrambling code for the uplink channel. The default value is 0.Valid values are 0 to 16,777,215. |
| uplinkScramblingType | [in] | int32 | This parameter specifies the type of scrambling to use for the measurement. The default value is Long.NameValueDescriptionRFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_LONG0 (0x0)A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used.RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_SHORT1 (0x1)A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_LONG | 0 (0x0) | A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |  |
| RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_SHORT | 1 (0x1) | A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3fde4988b28085f48f559be724a4c7cd.html language=enus -->
## TOPIC 00220: RFmxWCDMA_CfgCarrierFrequency

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3fde4988b28085f48f559be724a4c7cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga3fde4988b28085f48f559be724a4c7cd.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency of the carrier, relative to the RF center frequency. Syntaxint32 __stdcall RFmxWCDMA_CfgCarrierFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 carrierFrequency)RemarksUse "carrier<n>" as the selector string to configure this function.Param

### RFmxWCDMA_CfgCarrierFrequency

Configures the center frequency of the carrier, relative to the RF center frequency.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgCarrierFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 carrierFrequency)

#### Remarks

Use "carrier<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| carrierFrequency | [in] | float64 | This parameter specifies the center frequency of the carrier, relative to the RF center frequency. This value is expressed in Hz. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga506ec2133504bca21cb54e63964bb8d4.html language=enus -->
## TOPIC 00221: RFmxWCDMA_CfgNumberOfCarriers

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga506ec2133504bca21cb54e63964bb8d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga506ec2133504bca21cb54e63964bb8d4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of carriers for ACP, CHP, OBW, SEM, and ModAcc measurements. Syntaxint32 __stdcall RFmxWCDMA_CfgNumberOfCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis par

### RFmxWCDMA_CfgNumberOfCarriers

Configures the number of carriers for ACP, CHP, OBW, SEM, and ModAcc measurements.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgNumberOfCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| numberOfCarriers | [in] | int32 | This parameter specifies the number of carriers. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga530fc7e102f35dda2209c5977940d9dd.html language=enus -->
## TOPIC 00222: RFmxWCDMA_CfgUserDefinedChannel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga530fc7e102f35dda2209c5977940d9dd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga530fc7e102f35dda2209c5977940d9dd.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this function, you must configure the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute with the appropriate number of channels. Syntaxint32 __stdcall RFmxWCDMA_CfgUserDefinedChannel(n

### RFmxWCDMA_CfgUserDefinedChannel

Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this function, you must configure the [RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel__user__defined_1ga6a1f436d357acc220f477811837ce821.html) attribute with the appropriate number of channels.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spreadingFactor, int32 spreadingCode, int32 modulationType, int32 branch)

#### Remarks

Use "carrier<k>/channel<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, carrier number, and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0/channel0".Example:"carrier0/channel0""signal::sig1/carrier0/channel0"You can use the RFmxWCDMA_BuildChannelString function to build the selector string. |
| spreadingFactor | [in] | int32 | This parameter specifies the spreading factor of the channel. The default value is 256. Valid values are 2, 4, 8, 16, 32, 64, 128, and 256. |
| spreadingCode | [in] | int32 | This parameter specifies the spreading code of the channel.The default value is 0. Valid values are 0 to (Spreading factor - 1). |
| modulationType | [in] | int32 | This parameter specifies the modulation type of the channel. The default value is BPSK/QPSK.NameValueDescriptionRFMXWCDMA_VAL_MODULATION_TYPE_BPSK_QPSK0 (0x0)The modulation type is BPSK.RFMXWCDMA_VAL_MODULATION_TYPE_4PAM_16QAM1 (0x1)The modulation type is 4-PAM.RFMXWCDMA_VAL_MODULATION_TYPE_64QAM2 (0x2)The modulation type is 64-QAM. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_MODULATION_TYPE_BPSK_QPSK | 0 (0x0) | The modulation type is BPSK. |  |
| RFMXWCDMA_VAL_MODULATION_TYPE_4PAM_16QAM | 1 (0x1) | The modulation type is 4-PAM. |  |
| RFMXWCDMA_VAL_MODULATION_TYPE_64QAM | 2 (0x2) | The modulation type is 64-QAM. |  |
| branch | [in] | int32 | This parameter specifies the branch on which the data is modulated. The default value is I.NameValueDescriptionRFMXWCDMA_VAL_BRANCH_I0 (0x0)The signal is modulated in the in-phase branch.RFMXWCDMA_VAL_BRANCH_Q1 (0x1)The signal is modulated in the quadrature-phase branch.RFMXWCDMA_VAL_BRANCH_I_AND_Q2 (0x2)The signal is complex modulated. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_BRANCH_I | 0 (0x0) | The signal is modulated in the in-phase branch. |  |
| RFMXWCDMA_VAL_BRANCH_Q | 1 (0x1) | The signal is modulated in the quadrature-phase branch. |  |
| RFMXWCDMA_VAL_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga568ccd39174e6d85735f42b1c767a9f6.html language=enus -->
## TOPIC 00223: RFmxWCDMA_SendSoftwareEdgeTrigger

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga568ccd39174e6d85735f42b1c767a9f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga568ccd39174e6d85735f42b1c767a9f6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxWCDMA Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. Syntaxint32 __stdcall RFmxWCDMA_SendSoftwareEdgeTrigger(n

### RFmxWCDMA_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use the RFmxWCDMA Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger.

#### Syntax

int32 __stdcall RFmxWCDMA_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [RFmxWCDMA_Initiate](group____root__ni_r_fmx_w_c_d_m_a__functions_1ga8bd17a09cfd73e2d24f075d7b3703051.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga58dc406c40983946de81ecb3bd925024.html language=enus -->
## TOPIC 00224: RFmxWCDMA_CfgFrequencyReference

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga58dc406c40983946de81ecb3bd925024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga58dc406c40983946de81ecb3bd925024.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxWCDMA_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Instru

### RFmxWCDMA_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXWCDMA_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXWCDMA_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXWCDMA_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXWCDMA_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXWCDMA_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXWCDMA_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXWCDMA_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXWCDMA_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXWCDMA_VAL_CLK_IN_STR or RFMXWCDMA_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga6aae463a12b9e3c65d706f91ca024771.html language=enus -->
## TOPIC 00225: RFmxWCDMA_AutoLevel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga6aae463a12b9e3c65d706f91ca024771.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga6aae463a12b9e3c65d706f91ca024771.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. Syntaxint32 __stdcall RFmxWCDMA_AutoLevel(niRFmxInstrHandle instrumentHandle, char

### RFmxWCDMA_AutoLevel

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXWCDMA_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_w_c_d_m_a__attributes_1ga192a2f8b7bb8cf43610b6c802dfb97e3.html) attribute. Use this function to help calculate an approximate setting for the reference level.

#### Syntax

int32 __stdcall RFmxWCDMA_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64 *referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [RFMXWCDMA_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](group____root__ni_r_fmx_w_c_d_m_a__attributes__advanced_1ga2a6ed949818a8373624aa0142b917c66.html) attribute.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxWCDMA Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| measurementInterval | [in] | float64 | This parameter specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms.Auto Level function does not use any trigger for acquisition. It ignores the user-configured trigger attributes. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | [out] | float64 * | This parameter returns the reference level that represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga75405a1c8257122925b8de6bb34f4574.html language=enus -->
## TOPIC 00226: RFmxWCDMA_CfgChannelConfigurationMode

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga75405a1c8257122925b8de6bb34f4574.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga75405a1c8257122925b8de6bb34f4574.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the channel configuration mode. Syntaxint32 __stdcall RFmxWCDMA_CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFm

### RFmxWCDMA_CfgChannelConfigurationMode

Configures the channel configuration mode.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| channelConfigurationMode | [in] | int32 | This parameter specifies the channel configuration mode. The default value is Auto Detect.NameValueDescriptionRFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT0 (0x0)The measurement detects the channels.RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED1 (0x1)Configure the channels using the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute and the RFmxWCDMA_CfgUserDefinedChannelArray function.RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL2 (0x2)Choose from the standard-defined channel configurations using the RFMXWCDMA_ATTR_UPLINK_TEST_MODEL attribute. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT | 0 (0x0) | The measurement detects the channels. |  |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED | 1 (0x1) | Configure the channels using the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute and the RFmxWCDMA_CfgUserDefinedChannelArray function. |  |
| RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL | 2 (0x2) | Choose from the standard-defined channel configurations using the RFMXWCDMA_ATTR_UPLINK_TEST_MODEL attribute. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaa0158e3f82b3867474530c1b169d1c32.html language=enus -->
## TOPIC 00227: RFmxWCDMA_CfgReferenceLevel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaa0158e3f82b3867474530c1b169d1c32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaa0158e3f82b3867474530c1b169d1c32.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level, which represents the maximum expected power of an RF input signal. Syntaxint32 __stdcall RFmxWCDMA_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstr

### RFmxWCDMA_CfgReferenceLevel

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gabc158bbf519ebdc57369d8adfc8182a2.html language=enus -->
## TOPIC 00228: RFmxWCDMA_CfgMechanicalAttenuation

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gabc158bbf519ebdc57369d8adfc8182a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gabc158bbf519ebdc57369d8adfc8182a2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxWCDMA_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wrap

### RFmxWCDMA_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXWCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXWCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXWCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXWCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXWCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gad42f83693d28a5c9278fa224edd4bee9.html language=enus -->
## TOPIC 00229: RFmxWCDMA_CfgContiguousCarriers

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gad42f83693d28a5c9278fa224edd4bee9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gad42f83693d28a5c9278fa224edd4bee9.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the contiguous carriers based on the number of carriers and the carrier at the center frequency. Syntaxint32 __stdcall RFmxWCDMA_CfgContiguousCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers, int32 carrierAtCenterFrequency)ParametersNameDirectionT

### RFmxWCDMA_CfgContiguousCarriers

Configures the contiguous carriers based on the number of carriers and the carrier at the center frequency.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgContiguousCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers, int32 carrierAtCenterFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| numberOfCarriers | [in] | int32 | This parameter specifies the number of carriers. The default value is 1. |
| carrierAtCenterFrequency | [in] | int32 | This parameter specifies the index of the carrier that is at the center frequency.Set this parameter to -1 to specify a center frequency at the center of all carriers.For example, if you set the value of the Number of Carriers parameter to 2, and set the value of the Carrier at Center Frequency parameter to 1, the center frequency is at carrier1.If you set the value of the Number of Carriers parameter to 2, and set the value of the Carrier at Center Frequency parameter to -1, the center frequency is at the center of carrier0 and carrier1.If you set the value of the Number of Carriers parameter to 3, and set the value of the Carrier at Center Frequency parameter to either -1 or 1, the center frequency is at carrier1, which is the center of all carriers.The default value is -1. Recommended values are -1 to (Number of Carriers - 1). If you set this parameter to a value greater than (Number of Carriers - 1), the value of this parameter is coerced to (Number of Carriers - 1). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaec8239dd9471f5c8940491d0e393f2fa.html language=enus -->
## TOPIC 00230: RFmxWCDMA_CfgNumberOfChannels

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaec8239dd9471f5c8940491d0e393f2fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaec8239dd9471f5c8940491d0e393f2fa.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of user-defined channels for the measurement. This function is used when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. Call this function before you call the RFmxWCDMA_CfgUserDefinedChannelArray function or the RFmxWCDMA_CfgUserDefinedChannel

### RFmxWCDMA_CfgNumberOfChannels

Configures the number of user-defined channels for the measurement. This function is used when you set the [RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html) attribute to **User Defined**. Call this function before you call the [RFmxWCDMA_CfgUserDefinedChannelArray](group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga3c08e651cbadbcfa29bea61408b3a8cc.html) function or the [RFmxWCDMA_CfgUserDefinedChannel](group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga530fc7e102f35dda2209c5977940d9dd.html) function.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels)

#### Remarks

Use "carrier<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| numberOfChannels | [in] | int32 | This parameter specifies the number of user-defined channels. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaf4cf918834c6548f185c92fe2a530b9a.html language=enus -->
## TOPIC 00231: RFmxWCDMA_CfgExternalAttenuation

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaf4cf918834c6548f185c92fe2a530b9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1gaf4cf918834c6548f185c92fe2a530b9a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the external attenuation. Syntaxint32 __stdcall RFmxWCDMA_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refn

### RFmxWCDMA_CfgExternalAttenuation

Configures the external attenuation.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp.html language=enus -->
## TOPIC 00232: ACP

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_ACPCfgAveragingConfigures averaging for the ACP measurement. RFmxWCDMA_ACPCfgMeasurementMethodConfigures the method for performing the ACP measurement. RFmxWCDMA_ACPCfgNoiseCompensationEnabledConfigures the compensation of the channel power for the inh

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_ACPCfgAveraging | Configures averaging for the ACP measurement. |
| RFmxWCDMA_ACPCfgMeasurementMethod | Configures the method for performing the ACP measurement. |
| RFmxWCDMA_ACPCfgNoiseCompensationEnabled | Configures the compensation of the channel power for the inherent noise floor of the signal analyzer. |
| RFmxWCDMA_ACPCfgNumberOfOffsets | Configures the number of offsets for the ACP measurement. |
| RFmxWCDMA_ACPCfgOffsetPowerReference | Configures the power reference to use for measuring the relative power of the offset channel. |
| RFmxWCDMA_ACPCfgRBWFilter | Configures the RBW filter. |
| RFmxWCDMA_ACPCfgSweepTime | Configures the sweep time interval. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga139189d98e349c0c0734e3fc5d384c98.html language=enus -->
## TOPIC 00233: RFmxWCDMA_ACPCfgMeasurementMethod

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga139189d98e349c0c0734e3fc5d384c98.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga139189d98e349c0c0734e3fc5d384c98.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the ACP measurement. Syntaxint32 __stdcall RFmxWCDMA_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxWCDMA_ACPCfgMeasurementMethod

Configures the method for performing the ACP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method for performing the ACP measurement. The default value is Normal.NameValueDescriptionRFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_NORMAL0 (0x0)The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range.RFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE1 (0x1)The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range.Supported Devices: PXIe-5665/5668R\| RFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT \| 2 (0x2) \| The ACP measurement acquires I/Q samples for a duration specified by the RFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. The size of each chunk is defined by the RFMXWCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following attributes have limited support when you set the ACP Measurement Method attribute to Sequential FFT.\| Property \| Supported Value \|\|-----------------------------------------—\|------------------—\|\| RFMXWCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH \| True \|\| RFMXWCDMA_ATTR_ACP_RBW_FILTER_TYPE \| FFT Based \|\| RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT \| False \|\| RFMXWCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED \| >=1 \|\| RFMXWCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS \| >=1 \|\| RFMXWCDMA_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE \| RF Center Frequency \|Note For multi-span FFT, the averaging count should be 1.\| |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |  |
| RFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE | 1 (0x1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range.Supported Devices: PXIe-5665/5668R |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga2bff1951e649db07f4099be79a8f7c2c.html language=enus -->
## TOPIC 00234: RFmxWCDMA_ACPCfgSweepTime

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga2bff1951e649db07f4099be79a8f7c2c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga2bff1951e649db07f4099be79a8f7c2c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval. Syntaxint32 __stdcall RFmxWCDMA_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx s

### RFmxWCDMA_ACPCfgSweepTime

Configures the sweep time interval.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.NameValueDescriptionRFMXWCDMA_VAL_ACP_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL attributeRFMXWCDMA_VAL_ACP_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement uses a sweep time value of one slot duration. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL attribute |  |
| RFMXWCDMA_VAL_ACP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time value of one slot duration. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga4f65676ac6f380787932bd42979cf017.html language=enus -->
## TOPIC 00235: RFmxWCDMA_ACPCfgAveraging

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga4f65676ac6f380787932bd42979cf017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga4f65676ac6f380787932bd42979cf017.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ACP measurement. Syntaxint32 __stdcall RFmxWCDMA_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis p

### RFmxWCDMA_ACPCfgAveraging

Configures averaging for the ACP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging of the spectrum for the measurement. The default value is False.NameValueDescriptionRFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_TRUE1 (0x1)The ACP measurement uses the value of the RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT attribute as the number of acquisitions over which the ACP measurement is averaged. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The ACP measurement uses the value of the RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT attribute as the number of acquisitions over which the ACP measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXWCDMA_VAL_ACP_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_MAX3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_MIN4 (0x4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_MAX | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_MIN | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga73ca0c1b13003a336fb10bf6fbc0c218.html language=enus -->
## TOPIC 00236: RFmxWCDMA_ACPCfgNumberOfOffsets

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga73ca0c1b13003a336fb10bf6fbc0c218.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1ga73ca0c1b13003a336fb10bf6fbc0c218.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offsets for the ACP measurement. Syntaxint32 __stdcall RFmxWCDMA_ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFm

### RFmxWCDMA_ACPCfgNumberOfOffsets

Configures the number of offsets for the ACP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| numberOfOffsets | [in] | int32 | This parameter specifies the number of offset channels. The default value is 2. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gaa9fa8977a261cd1bcc3aa8fbd2a7ac80.html language=enus -->
## TOPIC 00237: RFmxWCDMA_ACPCfgOffsetPowerReference

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gaa9fa8977a261cd1bcc3aa8fbd2a7ac80.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gaa9fa8977a261cd1bcc3aa8fbd2a7ac80.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power reference to use for measuring the relative power of the offset channel. Syntaxint32 __stdcall RFmxWCDMA_ACPCfgOffsetPowerReference(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetPowerReferenceCarrier, int32 offsetPowerReferenceSpecific)ParametersNameDire

### RFmxWCDMA_ACPCfgOffsetPowerReference

Configures the power reference to use for measuring the relative power of the offset channel.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPCfgOffsetPowerReference(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetPowerReferenceCarrier, int32 offsetPowerReferenceSpecific)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| offsetPowerReferenceCarrier | [in] | int32 | This parameter specifies the carrier to use as the power reference to measure offset channel relative power. The default value is Composite.NameValueDescriptionRFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST0 (0x0)The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference.RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST1 (0x1)The measurement uses the highest measured active carrier power as the power reference.RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE2 (0x2)The measurement uses total measured active carrier power as the power reference.RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC3 (0x3)The measurement uses the power measured in the carrier with index specified by the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC attribute as the power reference. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST | 0 (0x0) | The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. |  |
| RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST | 1 (0x1) | The measurement uses the highest measured active carrier power as the power reference. |  |
| RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE | 2 (0x2) | The measurement uses total measured active carrier power as the power reference. |  |
| RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC | 3 (0x3) | The measurement uses the power measured in the carrier with index specified by the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC attribute as the power reference. |  |
| offsetPowerReferenceSpecific | [in] | int32 | This parameter specifies the index of the carrier to be used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the Offset Power Reference Carrier parameter to Specific. The default value is 0. Valid values are 0 to (Value of the RFMXWCDMA_ATTR_NUMBER_OF_CARRIERS attribute - 1). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gabda6b5f4e81bca5fceff66a4239bcd44.html language=enus -->
## TOPIC 00238: RFmxWCDMA_ACPCfgRBWFilter

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gabda6b5f4e81bca5fceff66a4239bcd44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gabda6b5f4e81bca5fceff66a4239bcd44.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxWCDMA_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxWCDMA_ACPCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat.If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter.NameValueDescriptionRFMXWCDMA_VAL_ACP_RBW_AUTO_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute.RFMXWCDMA_VAL_ACP_RBW_AUTO_TRUE1 (0x1)The measurement calculates the RBW. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXWCDMA_VAL_ACP_RBW_AUTO_TRUE | 1 (0x1) | The measurement calculates the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False.This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 38.4 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is used.RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)An RBW filter with a Gaussian response is applied.RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_FLAT2 (0x2)An RBW filter with a flat response is applied. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is used. |  |
| RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gaf2c3a6c6c7af456c1143ffc19cfd2f4a.html language=enus -->
## TOPIC 00239: RFmxWCDMA_ACPCfgNoiseCompensationEnabled

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gaf2c3a6c6c7af456c1143ffc19cfd2f4a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__acp_1gaf2c3a6c6c7af456c1143ffc19cfd2f4a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the compensation of the channel power for the inherent noise floor of the signal analyzer. Syntaxint32 __stdcall RFmxWCDMA_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)ParametersNameDirectionTypeDescriptioninstrum

### RFmxWCDMA_ACPCfgNoiseCompensationEnabled

Configures the compensation of the channel power for the inherent noise floor of the signal analyzer.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | [in] | int32 | This parameter specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False.NameValueDescriptionRFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE0 (0x0)Disables compensation of the channel powers for the noise floor of the signal analyzer.RFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE1 (0x1)Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured.Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832/5842/5860 |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |  |
| RFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured.Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832/5842/5860 |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays.html language=enus -->
## TOPIC 00240: Arrays

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_CfgCarrierFrequencyArrayConfigures an array of the center frequencies of the carriers, relative to the RF center frequency. RFmxWCDMA_CfgNumberOfChannelsArrayConfigures the number of user-defined channels for all the carriers in the measurement. This f

### Arrays

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_CfgCarrierFrequencyArray | Configures an array of the center frequencies of the carriers, relative to the RF center frequency. |
| RFmxWCDMA_CfgNumberOfChannelsArray | Configures the number of user-defined channels for all the carriers in the measurement. This function is used when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. Call this function before you call the RFmxWCDMA_CfgUserDefinedChannel function or the RFmxWCDMA_CfgUserDefinedChannel function. |
| RFmxWCDMA_CfgUplinkScramblingArray | Configures the scrambling code and the scrambling code type for all the carriers. |
| RFmxWCDMA_CfgUplinkTestModelArray | Configures the uplink test model for all the carriers. |
| RFmxWCDMA_CfgUserDefinedChannelArray | Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this function, you must configure the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute with the appropriate number of user-defined channels. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga2ba2115b39006c0f65c85e5f306f8c02.html language=enus -->
## TOPIC 00241: RFmxWCDMA_CfgCarrierFrequencyArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga2ba2115b39006c0f65c85e5f306f8c02.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga2ba2115b39006c0f65c85e5f306f8c02.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the center frequencies of the carriers, relative to the RF center frequency. Syntaxint32 __stdcall RFmxWCDMA_CfgCarrierFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 carrierFrequency[], int32 numberOfElements)ParametersNameDirectionTypeDescri

### RFmxWCDMA_CfgCarrierFrequencyArray

Configures an array of the center frequencies of the carriers, relative to the RF center frequency.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgCarrierFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 carrierFrequency[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| carrierFrequency | [in] | float64[] | This parameter specifies an array of the center frequencies of the carriers, relative to the RF center frequency.This value is expressed in Hz. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Arrays

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga3c08e651cbadbcfa29bea61408b3a8cc.html language=enus -->
## TOPIC 00242: RFmxWCDMA_CfgUserDefinedChannelArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga3c08e651cbadbcfa29bea61408b3a8cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga3c08e651cbadbcfa29bea61408b3a8cc.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this function, you must configure the RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS attribute with the appropriate number of user-defined channels. Syntaxint32 __stdcall RFmxWCD

### RFmxWCDMA_CfgUserDefinedChannelArray

Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this function, you must configure the [RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel__user__defined_1ga6a1f436d357acc220f477811837ce821.html) attribute with the appropriate number of user-defined channels.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spreadingFactor[], int32 spreadingCode[], int32 modulationType[], int32 branch[], int32 numberOfElements)

#### Remarks

Use "carrier<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| spreadingFactor | [in] | int32[] | This parameter specifies an array of spreading factor of the channels. The default value is 256. Valid values are 2, 4, 8,16, 32, 64, 128, and 256. |
| spreadingCode | [in] | int32[] | This parameter specifies an array of spreading code of the channels.The default value is 0. Valid values are 0 to (Spreading factor - 1). |
| modulationType | [in] | int32[] | This parameter specifies an array of modulation types of the channels. The default value is BPSK/QPSK.NameValueDescriptionRFMXWCDMA_VAL_MODULATION_TYPE_BPSK_QPSK0 (0x0)The modulation type is BPSK.RFMXWCDMA_VAL_MODULATION_TYPE_4PAM_16QAM1 (0x1)The modulation type is 4-PAM.RFMXWCDMA_VAL_MODULATION_TYPE_64QAM2 (0x2)The modulation type is 64-QAM. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_MODULATION_TYPE_BPSK_QPSK | 0 (0x0) | The modulation type is BPSK. |  |
| RFMXWCDMA_VAL_MODULATION_TYPE_4PAM_16QAM | 1 (0x1) | The modulation type is 4-PAM. |  |
| RFMXWCDMA_VAL_MODULATION_TYPE_64QAM | 2 (0x2) | The modulation type is 64-QAM. |  |
| branch | [in] | int32[] | This parameter specifies an array of branches on which the data is modulated in the channel. The default value is I.NameValueDescriptionRFMXWCDMA_VAL_BRANCH_I0 (0x0)The signal is modulated in the in-phase branch.RFMXWCDMA_VAL_BRANCH_Q1 (0x1)The signal is modulated in the quadrature-phase branch.RFMXWCDMA_VAL_BRANCH_I_AND_Q2 (0x2)The signal is complex modulated. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_BRANCH_I | 0 (0x0) | The signal is modulated in the in-phase branch. |  |
| RFMXWCDMA_VAL_BRANCH_Q | 1 (0x1) | The signal is modulated in the quadrature-phase branch. |  |
| RFMXWCDMA_VAL_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |  |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Arrays

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga604286368bef90d90207ea8cc7816a45.html language=enus -->
## TOPIC 00243: RFmxWCDMA_CfgUplinkTestModelArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga604286368bef90d90207ea8cc7816a45.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga604286368bef90d90207ea8cc7816a45.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the uplink test model for all the carriers. Syntaxint32 __stdcall RFmxWCDMA_CfgUplinkTestModelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkTestModel[], int32 numberOfElements)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis pa

### RFmxWCDMA_CfgUplinkTestModelArray

Configures the uplink test model for all the carriers.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgUplinkTestModelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkTestModel[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| uplinkTestModel | [in] | int32[] | This parameter specifies the array of uplink test models when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Test Model.Each test model is a set of channel configurations defined by the standard.Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<n>, where n is the oldest release number with a given set of channel configurations. The default value is R6 C.2.1.NameValueDescriptionRFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_10 (0x0)The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_21 (0x1)The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_32 (0x2)The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_43 (0x3)The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_54 (0x4)The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST15 (0x5)The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST26 (0x6)The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST37 (0x7)The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST48 (0x8)The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST59 (0x9)The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST610 (0xa)The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST111 (0xb)The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST212 (0xc)The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST313 (0xd)The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST414 (0xe)The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST115 (0xf)The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST216 (0x10)The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST317 (0x11)The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST418 (0x12)The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST519 (0x13)The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST120 (0x14)The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST221 (0x15)The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST322 (0x16)The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST423 (0x17)The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST524 (0x18)The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8.RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_4_SUBTEST125 (0x19)The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_1 | 0 (0x0) | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_2 | 1 (0x1) | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_3 | 2 (0x2) | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_4 | 3 (0x3) | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_5 | 4 (0x4) | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST1 | 5 (0x5) | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST2 | 6 (0x6) | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST3 | 7 (0x7) | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST4 | 8 (0x8) | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST5 | 9 (0x9) | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST6 | 10 (0xa) | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST1 | 11 (0xb) | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST2 | 12 (0xc) | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST3 | 13 (0xd) | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST4 | 14 (0xe) | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST1 | 15 (0xf) | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST2 | 16 (0x10) | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST3 | 17 (0x11) | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST4 | 18 (0x12) | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST5 | 19 (0x13) | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST1 | 20 (0x14) | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST2 | 21 (0x15) | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST3 | 22 (0x16) | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST4 | 23 (0x17) | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST5 | 24 (0x18) | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |  |
| RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_4_SUBTEST1 | 25 (0x19) | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |  |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Arrays

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga6ef4fcc9ec8e2b87a7b12308836bbb42.html language=enus -->
## TOPIC 00244: RFmxWCDMA_CfgUplinkScramblingArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga6ef4fcc9ec8e2b87a7b12308836bbb42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga6ef4fcc9ec8e2b87a7b12308836bbb42.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the scrambling code and the scrambling code type for all the carriers. Syntaxint32 __stdcall RFmxWCDMA_CfgUplinkScramblingArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkScramblingType[], int32 uplinkScramblingCode[], int32 numberOfElements)ParametersNameDirec

### RFmxWCDMA_CfgUplinkScramblingArray

Configures the scrambling code and the scrambling code type for all the carriers.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgUplinkScramblingArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 uplinkScramblingType[], int32 uplinkScramblingCode[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| uplinkScramblingType | [in] | int32[] | This parameter specifies the array of types of scrambling to use for the measurement. The default value is Long.NameValueDescriptionRFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_LONG0 (0x0)A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used.RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_SHORT1 (0x1)A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_LONG | 0 (0x0) | A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |  |
| RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_SHORT | 1 (0x1) | A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |  |
| uplinkScramblingCode | [in] | int32[] | This parameter specifies the array of scrambling codes for the uplink channel. The default value is 0.Valid values are 0 to 16,777,215. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Arrays

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga71158727e9d65900c360b24b9bdb558d.html language=enus -->
## TOPIC 00245: RFmxWCDMA_CfgNumberOfChannelsArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga71158727e9d65900c360b24b9bdb558d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__arrays_1ga71158727e9d65900c360b24b9bdb558d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of user-defined channels for all the carriers in the measurement. This function is used when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined. Call this function before you call the RFmxWCDMA_CfgUserDefinedChannel function or the RFmxWCDMA_CfgUser

### RFmxWCDMA_CfgNumberOfChannelsArray

Configures the number of user-defined channels for all the carriers in the measurement. This function is used when you set the [RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__carrier__channel_1ga68cc05f694ee78d4a90fc8a94ffb3da8.html) attribute to **User Defined**. Call this function before you call the [RFmxWCDMA_CfgUserDefinedChannel](group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga530fc7e102f35dda2209c5977940d9dd.html) function or the [RFmxWCDMA_CfgUserDefinedChannel](group____root__ni_r_fmx_w_c_d_m_a__functions__configuration_1ga530fc7e102f35dda2209c5977940d9dd.html) function.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgNumberOfChannelsArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| numberOfChannels | [in] | int32[] | This parameter specifies the array of number of channels. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Arrays

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda.html language=enus -->
## TOPIC 00246: CDA

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_CDACfgMeasurementChannelConfigures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. RFmxWCDMA_CDACfgPowerUnitConfigures the power unit for all code domain power results, except Total Power (dBm). RFmxWCDM

### CDA

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_CDACfgMeasurementChannel | Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. |
| RFmxWCDMA_CDACfgPowerUnit | Configures the power unit for all code domain power results, except Total Power (dBm). |
| RFmxWCDMA_CDACfgSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gab128df28fb4fbb47b4a29a5b990599e2.html language=enus -->
## TOPIC 00247: RFmxWCDMA_CDACfgMeasurementChannel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gab128df28fb4fbb47b4a29a5b990599e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gab128df28fb4fbb47b4a29a5b990599e2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. Syntaxint32 __stdcall RFmxWCDMA_CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spreadingFactor, int32 spreadingCode, int32 modulationType, int32 bran

### RFmxWCDMA_CDACfgMeasurementChannel

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

#### Syntax

int32 __stdcall RFmxWCDMA_CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spreadingFactor, int32 spreadingCode, int32 modulationType, int32 branch)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| spreadingFactor | [in] | int32 | This parameter specifies the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement.The default value is 256. Valid values are 2, 4, 8, 16, 32, 64, 128, and 256. |
| spreadingCode | [in] | int32 | This parameter specifies the spreading code of the measurement channel. This value is used to compute the symbol results of the CDA measurement.The default value is 0. Valid values are 0 to (Spreading Factor - 1). |
| modulationType | [in] | int32 | This parameter specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement.The default value is BPSK/QPSK.NameValueDescriptionRFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE_BPSK_QPSK0 (0x0)The modulation type is BPSK.RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE_4PAM_16QAM1 (0x1)The modulation type is 4-PAM. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE_BPSK_QPSK | 0 (0x0) | The modulation type is BPSK. |  |
| RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE_4PAM_16QAM | 1 (0x1) | The modulation type is 4-PAM. |  |
| branch | [in] | int32 | This parameter specifies the branch of the measurement channel. This value is used to compute the symbol results of the CDA measurement.The default value is I.NameValueDescriptionRFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_I0 (0x0)The signal is modulated on the in-phase branch.RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_Q1 (0x1)The signal is modulated on the quadrature-phase branch. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |  |
| RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gadcf5a87fda2d9e48981599b63ec3cd6b.html language=enus -->
## TOPIC 00248: RFmxWCDMA_CDACfgSynchronizationModeAndInterval

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gadcf5a87fda2d9e48981599b63ec3cd6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gadcf5a87fda2d9e48981599b63ec3cd6b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. Syntaxint32 __stdcall RFmxWCDMA_CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)ParametersNameD

### RFmxWCDMA_CDACfgSynchronizationModeAndInterval

Configures the synchronization mode, measurement offset, and measurement length.

#### Syntax

int32 __stdcall RFmxWCDMA_CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame, slot, or symbol boundary.The default value is Slot.NameValueDescriptionRFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_FRAME0 (0x0)The frame boundary is detected and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the frame boundary.RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_SLOT1 (0x1)The slot boundary is detected and the measurement is performed over the number of slots expressed by CDA Meas Length attribute, starting at CDA Meas Offset slots from the slot boundary.RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY2 (0x2)The symbol boundary is detected and the measurement is performed over the number of slots expressed by the CDA Meas Length attribute, starting at CDA Meas Offset slots from the symbol boundary. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH attribute, starting at RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET slots from the frame boundary. |  |
| RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by CDA Meas Length attribute, starting at CDA Meas Offset slots from the slot boundary. |  |
| RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY | 2 (0x2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the CDA Meas Length attribute, starting at CDA Meas Offset slots from the symbol boundary. |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter.The default value is 0. The Valid values are [0, (15 - Measurement Length)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the code domain measurement. This value is expressed in slots.The default value is 1. Valid values are [1, (15 - Measurement Offset)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gae046e7de2290a9d9ea1aa084b5bee9a0.html language=enus -->
## TOPIC 00249: RFmxWCDMA_CDACfgPowerUnit

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gae046e7de2290a9d9ea1aa084b5bee9a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__cda_1gae046e7de2290a9d9ea1aa084b5bee9a0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power unit for all code domain power results, except Total Power (dBm). Syntaxint32 __stdcall RFmxWCDMA_CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter

### RFmxWCDMA_CDACfgPowerUnit

Configures the power unit for all code domain power results, except Total Power (dBm).

#### Syntax

int32 __stdcall RFmxWCDMA_CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| powerUnit | [in] | int32 | This parameter specifies the measurement unit of all power results, except, RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER.The default value is dB.NameValueDescriptionRFMXWCDMA_VAL_CDA_POWER_UNIT_DB0 (0x0)Specifies the power relative to the total power.RFMXWCDMA_VAL_CDA_POWER_UNIT_DBM1 (0x1)Specifies the absolute power measured. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CDA_POWER_UNIT_DB | 0 (0x0) | Specifies the power relative to the total power. |  |
| RFMXWCDMA_VAL_CDA_POWER_UNIT_DBM | 1 (0x1) | Specifies the absolute power measured. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1ga8aeb914eae994973c53443d313bebfc4.html language=enus -->
## TOPIC 00250: RFmxWCDMA_CHPCfgAveraging

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1ga8aeb914eae994973c53443d313bebfc4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1ga8aeb914eae994973c53443d313bebfc4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the CHP measurement. Syntaxint32 __stdcall RFmxWCDMA_CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis p

### RFmxWCDMA_CHPCfgAveraging

Configures averaging for the CHP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging of the spectrum for the measurement. The default value is False.NameValueDescriptionRFMXWCDMA_VAL_CHP_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXWCDMA_VAL_CHP_AVERAGING_ENABLED_TRUE1 (0x1)The CHP measurement uses the value of the RFMXWCDMA_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CHP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXWCDMA_VAL_CHP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The CHP measurement uses the value of the RFMXWCDMA_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXWCDMA_VAL_CHP_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MAX3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MIN4 (0x4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MAX | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MIN | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP
