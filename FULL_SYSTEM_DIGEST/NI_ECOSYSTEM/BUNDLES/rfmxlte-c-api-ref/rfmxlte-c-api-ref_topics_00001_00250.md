# NI DOCUMENT BUNDLE: rfmxlte-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxlte-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes_1ga3d199b316b8cf6c720d1152dfb02df42.html language=enus -->
## TOPIC 00001: RFMXLTE_ATTR_UPLINK_DOWNLINK_CONFIGURATION

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes_1ga3d199b316b8cf6c720d1152dfb02df42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes_1ga3d199b316b8cf6c720d1152dfb02df42.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. SyntaxRFMXLTE_ATTR_UPLINK_DOWNLINK_CONFIGURATIONNumeric ValueData TypeAccessApplies To3145742int32Read/WriteN/ARemarks Y

### RFMXLTE_ATTR_UPLINK_DOWNLINK_CONFIGURATION

Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the *3GPP TS 36.211* specification to configure the LTE frame.

#### Syntax

RFMXLTE_ATTR_UPLINK_DOWNLINK_CONFIGURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145742 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **0**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_0 | 0 (0x0) | The configuration of the LTE frame structure in the TDD duplex mode is 0. |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_1 | 1 (0x1) | The configuration of the LTE frame structure in the TDD duplex mode is 1. |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_2 | 2 (0x2) | The configuration of the LTE frame structure in the TDD duplex mode is 2. |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_3 | 3 (0x3) | The configuration of the LTE frame structure in the TDD duplex mode is 3. |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_4 | 4 (0x4) | The configuration of the LTE frame structure in the TDD duplex mode is 4. |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_5 | 5 (0x5) | The configuration of the LTE frame structure in the TDD duplex mode is 5. |
| RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_6 | 6 (0x6) | The configuration of the LTE frame structure in the TDD duplex mode is 6. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes_1ga5b20f89818854cd6f9568e67fe625531.html language=enus -->
## TOPIC 00002: RFMXLTE_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes_1ga5b20f89818854cd6f9568e67fe625531.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes_1ga5b20f89818854cd6f9568e67fe625531.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the index of the component carrier having its center at the user-configured center frequency. RFmx LTE uses this attribute along with RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE attribute to calculate the value of the RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY. SyntaxRFMXLTE_ATTR_COMPONENT_C

### RFMXLTE_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY

Specifies the index of the component carrier having its center at the user-configured center frequency. RFmx LTE uses this attribute along with [RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE](group____root__ni_r_fmx_l_t_e__attributes_1ga2ab5d2314897d440bc235bfc03eef890.html) attribute to calculate the value of the [RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY](group____root__ni_r_fmx_l_t_e__attributes__component__carrier_1ga6d45a9d11d8a65534c1df0faf6f1f010.html).

#### Syntax

RFMXLTE_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145748 | int32 | Read/Write | Subblock |

#### Remarks

Refer to the [Carrier Frequency Offset Definition and Reference Frequency](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/carrier-frequency-offset-definition-and-refer.html) topic for more information about component carrier frequency.

Use "subblock<n>" as the selector string to configure or read this attribute.

Valid values are -1, 0, 1 ... n - 1, inclusive, where n is the number of component carriers in the subblock.

The default value is -1. If the value is -1, the component carrier frequency values are calculated such that the center of aggregated carriers (subblock) lies at the Center Frequency. This attribute is ignored if you set the CC Spacing Type attribute to **User**.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes_1ga6c6f5b92ad1ebbc9506e72acc1b4c5f7.html language=enus -->
## TOPIC 00003: RFMXLTE_ATTR_SELECTED_PORTS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes_1ga6c6f5b92ad1ebbc9506e72acc1b4c5f7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes_1ga6c6f5b92ad1ebbc9506e72acc1b4c5f7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. SyntaxRFMXLTE_ATTR_SELECTED_PORTSNumeric ValueData TypeAccessApplies To3149821char[]Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXLTE_ATTR_SELECTED_PORTS

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr_GetAvailablePorts](/csh?context=rfmxinstr_rfmxinstrcref_function_get_available_ports) function to get the valid port names.

#### Syntax

RFMXLTE_ATTR_SELECTED_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149821 | char[] | Read/Write | N/A |

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

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes_1gab346ce526a57059115f151e4bb5d17d8.html language=enus -->
## TOPIC 00004: RFMXLTE_ATTR_DUPLEX_SCHEME

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes_1gab346ce526a57059115f151e4bb5d17d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes_1gab346ce526a57059115f151e4bb5d17d8.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duplexing technique of the signal being measured. SyntaxRFMXLTE_ATTR_DUPLEX_SCHEMENumeric ValueData TypeAccessApplies To3145741int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector S

### RFMXLTE_ATTR_DUPLEX_SCHEME

Specifies the duplexing technique of the signal being measured.

#### Syntax

RFMXLTE_ATTR_DUPLEX_SCHEME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145741 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **FDD**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_DUPLEX_SCHEME_FDD | 0 (0x0) | Specifies that the duplexing technique is frequency-division duplexing. |
| RFMXLTE_VAL_DUPLEX_SCHEME_TDD | 1 (0x1) | Specifies that the duplexing technique is time-division duplexing. |
| RFMXLTE_VAL_DUPLEX_SCHEME_LAA | 2 (0x2) | Specifies that the duplexing technique is license assisted access. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp_1ga9013e8de3ed500773ab6b4aac04bafd7.html language=enus -->
## TOPIC 00005: RFMXLTE_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp_1ga9013e8de3ed500773ab6b4aac04bafd7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp_1ga9013e8de3ed500773ab6b4aac04bafd7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRFMXL

### RFMXLTE_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXLTE_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149888 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXLTE_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__component__carrier_1ga66222a988c3bdc4934408c449c9f153d.html language=enus -->
## TOPIC 00006: RFMXLTE_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__component__carrier_1ga66222a988c3bdc4934408c449c9f153d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__component__carrier_1ga66222a988c3bdc4934408c449c9f153d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of the component carrier (CC). This value is expressed in Hz. SyntaxRFMXLTE_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To3149829float64Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector str

### RFMXLTE_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

Specifies the integration bandwidth of the component carrier (CC). This value is expressed in Hz.

#### Syntax

RFMXLTE_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149829 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

The default value is 9 MHz.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__fft.html language=enus -->
## TOPIC 00007: FFT

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__fft.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_ACP_FFT_OVERLAPSpecifies the samples to overlap between the consecutive chunks as a percentage of the RFMXLTE_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute value when you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT and the RFMXL

### FFT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACP_FFT_OVERLAP | Specifies the samples to overlap between the consecutive chunks as a percentage of the RFMXLTE_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute value when you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT and the RFMXLTE_ATTR_ACP_FFT_OVERLAP_MODE attribute to User Defined. |
| RFMXLTE_ATTR_ACP_FFT_OVERLAP_MODE | Specifies the overlap mode when you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__noise__calibration.html language=enus -->
## TOPIC 00008: Noise Calibration

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__noise__calibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__noise__calibration.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingGroup membersNameDescriptionRFMXLTE_ATTR_ACP_NOISE_CALIBRATION_MODESpecifies whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more informatio

### Noise Calibration

#### Groups

- Averaging

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_MODE | Specifies whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__noise__calibration__averaging_1ga268d4a264077ea0d28bcf613de1dbe54.html language=enus -->
## TOPIC 00009: RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__noise__calibration__averaging_1ga268d4a264077ea0d28bcf613de1dbe54.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__noise__calibration__averaging_1ga268d4a264077ea0d28bcf613de1dbe54.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxRFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTONumeric ValueData TypeAccessApplies To3149898int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this at

### RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149898 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE | 0 (0x0) | RFmx uses the averages that you set for RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. |
| RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE | 1 (0x1) | RFmx uses the following averaging counts: When you set the RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD attribute to Normal or Sequential FFT, RFmx uses a noise calibration averaging count of 32. When you set the ACP Meas Method attribute to Dynamic Range and sweep time is less than 5 ms, RFmx uses a noise calibration averaging count of 15. When you set the ACP Meas Method attribute to Dynamic Range and sweep time is greater than or equal to 5 ms, RFmx uses a noise calibration averaging count of 5. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga612e5b264835e4f87763f058dbd10d7b.html language=enus -->
## TOPIC 00010: RFMXLTE_ATTR_ACP_NUMBER_OF_STANDALONE_NB_IOT_OFFSETS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga612e5b264835e4f87763f058dbd10d7b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga612e5b264835e4f87763f058dbd10d7b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH to 200.0 k, RFMXLTE_ATTR_LINK_DIRECTION to Downlink and the RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED attribute to True. SyntaxRFMXLTE_ATTR_ACP_

### RFMXLTE_ATTR_ACP_NUMBER_OF_STANDALONE_NB_IOT_OFFSETS

Specifies the number of Standalone NB-IoT adjacent channel offsets to be configured when you set the [RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH](group____root__ni_r_fmx_l_t_e__attributes__component__carrier_1ga670f71a39fab2b7edb0fe4096f2892d1.html) to **200.0 k**, [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) to **Downlink** and the [RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED](group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html) attribute to **True**.

#### Syntax

RFMXLTE_ATTR_ACP_NUMBER_OF_STANDALONE_NB_IOT_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149904 | int32 | Read/Write | Subblock |

#### Remarks

The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center.

Use "subblock<n>" as the selector string to configure or read this attribute.

The default value is 2, when you set the CC Bandwidth attribute to is **200.0 k** and the Link Direction to is **Downlink**. The default value is 0, otherwise.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga6b76d36117877e4b3a95585e98369122.html language=enus -->
## TOPIC 00011: RFMXLTE_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga6b76d36117877e4b3a95585e98369122.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga6b76d36117877e4b3a95585e98369122.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of an offset carrier. This value is expressed in Hz. SyntaxRFMXLTE_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To3149838float64Read-OnlyOffsetRemarks Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result

### RFMXLTE_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

Specifies the integration bandwidth of an offset carrier. This value is expressed in Hz.

#### Syntax

RFMXLTE_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149838 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

The default value is 9 MHz.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html language=enus -->
## TOPIC 00012: RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the number of offsets is computed by measurement or configured by you. SyntaxRFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLEDNumeric ValueData TypeAccessApplies To3149892int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute fo

### RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED

Specifies whether the number of offsets is computed by measurement or configured by you.

#### Syntax

RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149892 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

When the carrier bandwidth is 200 kHz or the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) is **Downlink**, the default value is **False**. The default value is **True**, otherwise.

Note

In case of downlink, this attribute is valid only for number of E-UTRA offsets. For the number of UTRA offsets, only 3GPP specification defined values are supported.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED_FALSE | 0 (0x0) | Measurement will set the number of offsets. |
| RFMXLTE_VAL_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED_TRUE | 1 (0x1) | Measurement will use the user configured value for number of offsets. |

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7bcd3ba434e62f23350a98b989579dfb.html language=enus -->
## TOPIC 00013: RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7bcd3ba434e62f23350a98b989579dfb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7bcd3ba434e62f23350a98b989579dfb.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the evolved universal terrestrial radio access (E-UTRA) offset channel definition. SyntaxRFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITIONNumeric ValueData TypeAccessApplies To3149891int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defau

### RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION

Specifies the evolved universal terrestrial radio access (E-UTRA) offset channel definition.

#### Syntax

RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149891 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Note

In case of non-contiguous, the inner offset channel definition will be configured internally as per the 3GPP specification. Offset power reference for the outer UTRA offsets are set according to ACP EUTRA Offset Definition attribute.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACP_EUTRA_OFFSET_DEFINITION_AUTO | 0 (0x0) | Measurement will set the E-UTRA definition and offset power reference based on the link direction. For downlink, the definition is Closest and for uplink, it is Composite. |
| RFMXLTE_VAL_ACP_EUTRA_OFFSET_DEFINITION_CLOSEST | 1 (0x1) | Integration bandwidth is derived from the closest LTE carrier. Offset power reference is set to Closest internally. |
| RFMXLTE_VAL_ACP_EUTRA_OFFSET_DEFINITION_COMPOSITE | 2 (0x2) | Integration bandwidth is derived from the aggregated sub-block bandwidth. Offset power reference is set as Composite Sub-Block. |

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1gac61e7f48330e1fb9582faa7ca283153c.html language=enus -->
## TOPIC 00014: RFMXLTE_ATTR_ACP_NUMBER_OF_GSM_OFFSETS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1gac61e7f48330e1fb9582faa7ca283153c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1gac61e7f48330e1fb9582faa7ca283153c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of GSM adjacent channel offsets to be configured when you set the RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH to 200.0 k and the RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED attribute to True. SyntaxRFMXLTE_ATTR_ACP_NUMBER_OF_GSM_OFFSETSNumeric ValueData TypeAccessApplie

### RFMXLTE_ATTR_ACP_NUMBER_OF_GSM_OFFSETS

Specifies the number of GSM adjacent channel offsets to be configured when you set the [RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH](group____root__ni_r_fmx_l_t_e__attributes__component__carrier_1ga670f71a39fab2b7edb0fe4096f2892d1.html) to **200.0 k** and the [RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED](group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html) attribute to **True**.

#### Syntax

RFMXLTE_ATTR_ACP_NUMBER_OF_GSM_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149890 | int32 | Read/Write | Subblock |

#### Remarks

The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center.

Use "subblock<n>" as the selector string to configure or read this attribute.

The default value is 1, when you set the CC Bandwidth attribute to is **200.0 k** and Link Direction to **Uplink**. The default value is 0, otherwise.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1gae5d0691725565b81a4c0eb5e082f68e4.html language=enus -->
## TOPIC 00015: RFMXLTE_ATTR_ACP_NUMBER_OF_UTRA_OFFSETS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1gae5d0691725565b81a4c0eb5e082f68e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1gae5d0691725565b81a4c0eb5e082f68e4.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED attribute to True. SyntaxRFMXLTE_ATTR_ACP_NUMBER_OF_UTRA_OFFSETSNumeric ValueData TypeAccessApplie

### RFMXLTE_ATTR_ACP_NUMBER_OF_UTRA_OFFSETS

Specifies the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the [RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED](group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html) attribute to **True**.

#### Syntax

RFMXLTE_ATTR_ACP_NUMBER_OF_UTRA_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149882 | int32 | Read/Write | Subblock |

#### Remarks

Use "subblock<n>" as the selector string to configure or read this attribute.

The default value is 1, when you set the [RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH](group____root__ni_r_fmx_l_t_e__attributes__component__carrier_1ga670f71a39fab2b7edb0fe4096f2892d1.html) to **200.0 k** and [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) to **Uplink**.

The default value is 0, when you set the [RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH](group____root__ni_r_fmx_l_t_e__attributes__component__carrier_1ga670f71a39fab2b7edb0fe4096f2892d1.html) to **200.0 k** and [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) to **Downlink**. The default value is 0, when you set the [RFMXLTE_ATTR_BAND](group____root__ni_r_fmx_l_t_e__attributes_1gaa1a4c1e2ea00d7168567fa96e2d94aab.html) attribute to 46 or [RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION](group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7bcd3ba434e62f23350a98b989579dfb.html) attribute to **LAA**.

Note

In case of downlink, only 3GPP specification defined values are supported. In case of non-contiguous carrier aggregation, the configured value will be used only for the outer offsets and the offset channels in the gap region are defined as per the 3GPP specification. Offset power reference for the outer UTRA offsets are set according to the value of [RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION](group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7bcd3ba434e62f23350a98b989579dfb.html) attribute.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__rbw__filter_1ga40fe1f18dad4a94ec7e76b231357c07c.html language=enus -->
## TOPIC 00016: RFMXLTE_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__rbw__filter_1ga40fe1f18dad4a94ec7e76b231357c07c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__rbw__filter_1ga40fe1f18dad4a94ec7e76b231357c07c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxRFMXLTE_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To3149851int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXLTE_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the RBW.

#### Syntax

RFMXLTE_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149851 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXLTE_ATTR_ACP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__rbw__filter_1gac5a3b203464c8466794d305475950adf.html language=enus -->
## TOPIC 00017: RFMXLTE_ATTR_ACP_RBW_FILTER_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__rbw__filter_1gac5a3b203464c8466794d305475950adf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__rbw__filter_1gac5a3b203464c8466794d305475950adf.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the RBW filter. SyntaxRFMXLTE_ATTR_ACP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To3149853int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for inf

### RFMXLTE_ATTR_ACP_RBW_FILTER_TYPE

Specifies the shape of the RBW filter.

#### Syntax

RFMXLTE_ATTR_ACP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149853 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **FFT Based**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |
| RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results.html language=enus -->
## TOPIC 00018: Results

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsComponent CarrierLower OffsetUpper OffsetGroup membersNameDescriptionRFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_CENTER_FREQUENCYReturns the absolute center frequency of the subblock, which is the center of the subblock integration bandwidth. This value is expressed in Hz. Integration bandwidth is the s

### Results

#### Groups

- Component Carrier
- Lower Offset
- Upper Offset

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_CENTER_FREQUENCY | Returns the absolute center frequency of the subblock, which is the center of the subblock integration bandwidth. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |
| RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH | Returns the integration bandwidth used in calculating the power of the subblock. This value is expressed in Hz. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |
| RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_POWER | Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. |
| RFMXLTE_ATTR_ACP_RESULTS_TOTAL_AGGREGATED_POWER | Returns the sum of powers of all the frequency bins over the integration bandwidths of all subblocks. The sum includes the power in inter-carrier gaps within a subblock but it does not include the power in subblock gaps. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results_1ga5fcbf34a6a6434a006c311cf89d5d41a.html language=enus -->
## TOPIC 00019: RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results_1ga5fcbf34a6a6434a006c311cf89d5d41a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results_1ga5fcbf34a6a6434a006c311cf89d5d41a.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. SyntaxRFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_POWERNumeric ValueData TypeAccessApplies To3149880float64Read-OnlySubblockRemarks When you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, the attribute

### RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_POWER

Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149880 | float64 | Read-Only | Subblock |

#### Remarks

When you set the [RFMXLTE_ATTR_ACP_POWER_UNITS](group____root__ni_r_fmx_l_t_e__attributes__acp_1gac872ab071b277ea5fcf501710ea8a66e.html) attribute to **dBm**, the attribute returns the total subblock power in dBm of all the active carriers measured over the subblock. When you set the ACP Pwr Units attribute to **dBm/Hz**, the attribute returns the power spectral density in dBm/Hz based on the power in all the active carriers measured over the subblock.

Use "subblock<n>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results_1ga719c79ff493d8939bbce074d96ba2cca.html language=enus -->
## TOPIC 00020: RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results_1ga719c79ff493d8939bbce074d96ba2cca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results_1ga719c79ff493d8939bbce074d96ba2cca.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth used in calculating the power of the subblock. This value is expressed in Hz. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. SyntaxRFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_INTEGRATION

### RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH

Returns the integration bandwidth used in calculating the power of the subblock. This value is expressed in Hz. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149879 | float64 | Read-Only | Subblock |

#### Remarks

Use "subblock<n>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results_1gaa6b0d9ec62ef9eab7143be6f8a2fc5c2.html language=enus -->
## TOPIC 00021: RFMXLTE_ATTR_ACP_RESULTS_TOTAL_AGGREGATED_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results_1gaa6b0d9ec62ef9eab7143be6f8a2fc5c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results_1gaa6b0d9ec62ef9eab7143be6f8a2fc5c2.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers of all the frequency bins over the integration bandwidths of all subblocks. The sum includes the power in inter-carrier gaps within a subblock but it does not include the power in subblock gaps. SyntaxRFMXLTE_ATTR_ACP_RESULTS_TOTAL_AGGREGATED_POWERNumeric ValueData TypeAcce

### RFMXLTE_ATTR_ACP_RESULTS_TOTAL_AGGREGATED_POWER

Returns the sum of powers of all the frequency bins over the integration bandwidths of all subblocks. The sum includes the power in inter-carrier gaps within a subblock but it does not include the power in subblock gaps.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_TOTAL_AGGREGATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149858 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXLTE_ATTR_ACP_POWER_UNITS](group____root__ni_r_fmx_l_t_e__attributes__acp_1gac872ab071b277ea5fcf501710ea8a66e.html) attribute to **dBm**, the attribute returns the total integrated power in dBm of all the active carriers measured. When you set the ACP Pwr Units attribute to **dBm/Hz**, the attribute returns the power spectral density in dBm/Hz based on the power in all the active carriers measured.

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results_1gaa88cba94e4595fe14bc86f171cf1ea1b.html language=enus -->
## TOPIC 00022: RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_CENTER_FREQUENCY

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results_1gaa88cba94e4595fe14bc86f171cf1ea1b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results_1gaa88cba94e4595fe14bc86f171cf1ea1b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute center frequency of the subblock, which is the center of the subblock integration bandwidth. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. SyntaxRFMXLTE_

### RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_CENTER_FREQUENCY

Returns the absolute center frequency of the subblock, which is the center of the subblock integration bandwidth. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149881 | float64 | Read-Only | Subblock |

#### Remarks

Use "subblock<n>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier.html language=enus -->
## TOPIC 00023: Component Carrier

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWERReturns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the

### Component Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER | Returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER | Returns the component carrier power relative to its subblock power. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier_1ga00a589a6b180c0bfe39bbf3b144af07b.html language=enus -->
## TOPIC 00024: RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier_1ga00a589a6b180c0bfe39bbf3b144af07b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier_1ga00a589a6b180c0bfe39bbf3b144af07b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. SyntaxRFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_P

### RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

Returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the [RFMXLTE_ATTR_ACP_POWER_UNITS](group____root__ni_r_fmx_l_t_e__attributes__acp_1gac872ab071b277ea5fcf501710ea8a66e.html) attribute to **dBm**, and in dBm/Hz when you set the ACP Pwr Units attribute to **dBm/Hz**.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149862 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier_1ga042a953be5c805c9bef68192a93a082d.html language=enus -->
## TOPIC 00025: RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier_1ga042a953be5c805c9bef68192a93a082d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__component__carrier_1ga042a953be5c805c9bef68192a93a082d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the component carrier power relative to its subblock power. This value is expressed in dB. SyntaxRFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWERNumeric ValueData TypeAccessApplies To3149863float64Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector s

### RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

Returns the component carrier power relative to its subblock power. This value is expressed in dB.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149863 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset.html language=enus -->
## TOPIC 00026: Lower Offset

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWERReturns the lower (negative) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER | Returns the lower (negative) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER | Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset_1gacaa910a06ea75539de9c2eae4b771eed.html language=enus -->
## TOPIC 00027: RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset_1gacaa910a06ea75539de9c2eae4b771eed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset_1gacaa910a06ea75539de9c2eae4b771eed.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower (negative) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set

### RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

Returns the lower (negative) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the [RFMXLTE_ATTR_ACP_POWER_UNITS](group____root__ni_r_fmx_l_t_e__attributes__acp_1gac872ab071b277ea5fcf501710ea8a66e.html) attribute to **dBm**, and in dBm/Hz when you set the ACP Pwr Units attribute to **dBm/Hz**.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149868 | float64 | Read-Only | Offset |

#### Remarks

Refer to the *3GPP 36.521* specification for more information about the applicability of an offset channel. Refer to the [LTE Uplink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-adjacent-channel-power.html) and [LTE Downlink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-adjacent-channel-power.html) topics for more information.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset_1gaf2e157fd9ef452dd0b806be2e045f68e.html language=enus -->
## TOPIC 00028: RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset_1gaf2e157fd9ef452dd0b806be2e045f68e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__lower__offset_1gaf2e157fd9ef452dd0b806be2e045f68e.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. SyntaxRFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWERNum

### RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149869 | float64 | Read-Only | Offset |

#### Remarks

Refer to the *3GPP TS 36.521* specification for more information about the applicability of the offset channel. Refer to the [LTE Uplink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-adjacent-channel-power.html) and [LTE Downlink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-adjacent-channel-power.html) topics for more information.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset.html language=enus -->
## TOPIC 00029: Upper Offset

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWERReturns the upper (positive) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER | Returns the upper (positive) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the ACP Pwr Units attribute to dBm/Hz. |
| RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER | Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned.. Refer to the 3GPP TS 36.521 specification for more information about the applicability of the offset channel. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset_1gac6f11af38606f5f0525df10bd125f08c.html language=enus -->
## TOPIC 00030: RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset_1gac6f11af38606f5f0525df10bd125f08c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset_1gac6f11af38606f5f0525df10bd125f08c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned.. Refer to the 3GPP TS 36.521 specification for more infor

### RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned.. Refer to the *3GPP TS 36.521* specification for more information about the applicability of the offset channel.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149875 | float64 | Read-Only | Offset |

#### Remarks

Refer to the [LTE Uplink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-adjacent-channel-power.html) and [LTE Downlink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-adjacent-channel-power.html) topics for more information about ACP offsets.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset_1gadec4a15d2bc181aa6d5d1f8d74c6e66b.html language=enus -->
## TOPIC 00031: RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset_1gadec4a15d2bc181aa6d5d1f8d74c6e66b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__results__upper__offset_1gadec4a15d2bc181aa6d5d1f8d74c6e66b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper (positive) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, and in dBm/Hz when you set

### RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

Returns the upper (positive) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the [RFMXLTE_ATTR_ACP_POWER_UNITS](group____root__ni_r_fmx_l_t_e__attributes__acp_1gac872ab071b277ea5fcf501710ea8a66e.html) attribute to **dBm**, and in dBm/Hz when you set the ACP Pwr Units attribute to **dBm/Hz**.

#### Syntax

RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149874 | float64 | Read-Only | Offset |

#### Remarks

Refer to the *3GPP TS 36.521* specification for more information about the applicability of offset channel. Refer to the [LTE Uplink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-adjacent-channel-power.html) and [LTE Downlink Adjacent Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-adjacent-channel-power.html) topics for more information about ACP offsets.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time.html language=enus -->
## TOPIC 00032: Sweep Time

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_ACP_SWEEP_TIME_AUTOSpecifies whether the measurement computes the sweep time. RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. Atta

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO | Specifies whether the measurement computes the sweep time. |
| RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time_1ga2e8af3f7bbe79991d5e4da6c6b395a01.html language=enus -->
## TOPIC 00033: RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time_1ga2e8af3f7bbe79991d5e4da6c6b395a01.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time_1ga2e8af3f7bbe79991d5e4da6c6b395a01.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To3149855float64Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO](group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time_1gabc48bc89544f0596d3a12a42d03f08e3.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149855 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 ms.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time_1gabc48bc89544f0596d3a12a42d03f08e3.html language=enus -->
## TOPIC 00034: RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time_1gabc48bc89544f0596d3a12a42d03f08e3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__acp__sweep__time_1gabc48bc89544f0596d3a12a42d03f08e3.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXLTE_ATTR_ACP_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To3149854int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3149854 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL attribute. |
| RFMXLTE_VAL_ACP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time of 1 ms. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__advanced.html language=enus -->
## TOPIC 00035: Advanced

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__advanced.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLEDSpecifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. RFMXLTE_ATTR_AUTO_LEVE

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED | Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. |
| RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL | Specifies the initial reference level that the RFmxLTE_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| RFMXLTE_ATTR_CENTER_FREQUENCY_FOR_LIMITS | Specifies the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this attribute, the measurement internally uses the RFMXLTE_ATTR_CENTER_FREQUENCY for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz. |
| RFMXLTE_ATTR_LIMITED_CONFIGURATION_CHANGE | Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. |
| RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE | Specifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga5d643b5746c2f72fdd88fc489c5d66e8.html language=enus -->
## TOPIC 00036: RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga5d643b5746c2f72fdd88fc489c5d66e8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga5d643b5746c2f72fdd88fc489c5d66e8.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. SyntaxRFMXLTE_ATT

### RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE

Specifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated.

#### Syntax

RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3198978 | int32 | Read/Write | N/A |

#### Remarks

The measurement ignores this attribute when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Downlink**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **LO per Component Carrier**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_COMPONENT_CARRIER | 0 (0x0) | IQ impairments and In-band emission are calculated per component carrier. |
| RFMXLTE_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_SUBBLOCK | 1 (0x1) | Additional subblock based results such as Subblock IQ Offset and Subblock In band emission are calculated apart from per carrier results. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga6c4609e705b495ae91a02d0a1ffb47cb.html language=enus -->
## TOPIC 00037: RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga6c4609e705b495ae91a02d0a1ffb47cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga6c4609e705b495ae91a02d0a1ffb47cb.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial reference level that the RFmxLTE_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. SyntaxRFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To3198976float64Read/WriteN/ARemarks You do not need

### RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

Specifies the initial reference level that the [RFmxLTE_AutoLevel](group____root__ni_r_fmx_l_t_e__functions__configuration_1ga22b81cb37f2c7293a0dd4ff709a0cb50.html) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

#### Syntax

RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3198976 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 30.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga78551068c4f220df04d408ec335a3a9c.html language=enus -->
## TOPIC 00038: RFMXLTE_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga78551068c4f220df04d408ec335a3a9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga78551068c4f220df04d408ec335a3a9c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. SyntaxRFMXLTE_ATTR_LIMITED_CONFIGURATION_CHANGENumeric ValueData TypeAccessApplies To3198979int32Read/WriteN/ARemarks If your test system performs the same measurement at different selected ports, m

### RFMXLTE_ATTR_LIMITED_CONFIGURATION_CHANGE

Specifies the set of attributes that are considered by RFmx in the locked signal configuration state.

#### Syntax

RFMXLTE_ATTR_LIMITED_CONFIGURATION_CHANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3198979 | int32 | Read/Write | N/A |

#### Remarks

If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this attribute can help achieve faster measurements. When you set this attribute to a value other than **Disabled**, RFmx will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](https://www.ni.com/docs/en-US/bundle/rfmx-wcdma-prop/page/rfmxwcdmaprop/limitations.html) topic.

You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration.

NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to pre-compute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFmxInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED | 0 (0x0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE | 1 (0x1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY | 2 (0x2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the RFMXLTE_ATTR_CENTER_FREQUENCY and RFMXLTE_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL | 3 (0x3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXLTE_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL | 4 (0x4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type attribute to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL | 5 (0x5) | Signal configuration, other than Selected Ports, Center frequency, Reference level, External attenuation, and RFmxInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type attribute to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga809beb9a87b1ec01e1c2c30de86875f8.html language=enus -->
## TOPIC 00039: RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga809beb9a87b1ec01e1c2c30de86875f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga809beb9a87b1ec01e1c2c30de86875f8.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. SyntaxRFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLEDNumeric ValueData TypeAccessApplies To3198977int32Read

### RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

#### Syntax

RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3198977 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Refer to the [Acquisition Bandwidth Optimization Enabled](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/acquisition-bandwidth-optimization.html) topic for more information.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE | 0 (0x0) | RFmx does not optimize acquisition bandwidth and will be based on the Nyquist criterion. The value of the acquisition center frequency is the same as the value of the RFMXLTE_ATTR_CENTER_FREQUENCY that you configure. |
| RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE | 1 (0x1) | RFmx positions the acquisition center frequency to acquire the least bandwidth based on the configuration and span needed for the measurement. This helps in reducing the amount of data to process for the measurement, thus improving the speed. However this might cause the LO to be positioned at a non-dc subcarrier position, hence the measurement sensitive to it should have this attribute disabled. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga9ef4dae397265d6bf2f153f2748e7134.html language=enus -->
## TOPIC 00040: RFMXLTE_ATTR_CENTER_FREQUENCY_FOR_LIMITS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga9ef4dae397265d6bf2f153f2748e7134.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga9ef4dae397265d6bf2f153f2748e7134.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this attribute, the measurement internally uses the RFMXLTE_ATTR_CENTER_FREQUENCY for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed

### RFMXLTE_ATTR_CENTER_FREQUENCY_FOR_LIMITS

Specifies the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this attribute, the measurement internally uses the [RFMXLTE_ATTR_CENTER_FREQUENCY](group____root__ni_r_fmx_l_t_e__attributes_1gac4330bfa5013eaea66d56201e0a279c9.html) for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz.

#### Syntax

RFMXLTE_ATTR_CENTER_FREQUENCY_FOR_LIMITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3198980 | float64 | Read/Write | Subblock |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp.html language=enus -->
## TOPIC 00041: CHP

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingComponent CarrierNoise CalibrationNoise CompensationRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXLTE_ATTR_CHP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. RFMXLTE_ATTR_CHP_AMPLITUDE_CORRECTION_T

### CHP

#### Groups

- Averaging
- Component Carrier
- Noise Calibration
- Noise Compensation
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_CHP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. |
| RFMXLTE_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. |
| RFMXLTE_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE | Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. |
| RFMXLTE_ATTR_CHP_MEASUREMENT_ENABLED | Specifies whether to enable the channel power measurement. |
| RFMXLTE_ATTR_CHP_MEASUREMENT_MODE | Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the CHP measurement. |
| RFMXLTE_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH | Specifies the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp_1ga245f1dec497f364904ca534c3bf255b0.html language=enus -->
## TOPIC 00042: RFMXLTE_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp_1ga245f1dec497f364904ca534c3bf255b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp_1ga245f1dec497f364904ca534c3bf255b0.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. SyntaxRFMXLTE_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPENumeric V

### RFMXLTE_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE

Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval.

#### Syntax

RFMXLTE_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158040 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Refer to the [LTE Channel Power](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-channel-power.html) topic for more information about CHP IBW types.

The default value is **Signal Bandwidth**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_SIGNAL_BANDWIDTH | 0 (0x0) | The IBW excludes the guard bands at the edges of the carrier or subblock. |
| RFMXLTE_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_CHANNEL_BANDWIDTH | 1 (0x1) | The IBW includes the guard bands at the edges of the carrier or subblock. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp_1ga37418e197c256ccba6ca8a727218720d.html language=enus -->
## TOPIC 00043: RFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp_1ga37418e197c256ccba6ca8a727218720d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp_1ga37418e197c256ccba6ca8a727218720d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the CHP measurement. SyntaxRFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To3158019int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threads

### RFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the CHP measurement.

#### Syntax

RFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158019 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp_1ga5a667b153cddcb5e8f082781f2474d08.html language=enus -->
## TOPIC 00044: RFMXLTE_ATTR_CHP_MEASUREMENT_MODE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp_1ga5a667b153cddcb5e8f082781f2474d08.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp_1ga5a667b153cddcb5e8f082781f2474d08.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxRFMXLTE_ATTR_CHP_MEASUREMENT_MODENumeric ValueData TypeAccessApplies To3158052in

### RFMXLTE_ATTR_CHP_MEASUREMENT_MODE

Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the [Noise Compensation Algorithm](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/noise-compensation-algorithm.html) topic for more information.

#### Syntax

RFMXLTE_ATTR_CHP_MEASUREMENT_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158052 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_CHP_MEASUREMENT_MODE_MEASURE | 0 (0x0) | CHP measurement is performed on the acquired signal. |
| RFMXLTE_VAL_CHP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR | 1 (0x1) | Manual noise calibration of the signal analyzer is performed for the CHP measurement. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp_1ga9680f13cf1dfb746929c7a510615f127.html language=enus -->
## TOPIC 00045: RFMXLTE_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp_1ga9680f13cf1dfb746929c7a510615f127.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp_1ga9680f13cf1dfb746929c7a510615f127.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRFMXL

### RFMXLTE_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXLTE_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158051 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXLTE_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp_1gab41db77f1f286cf01d314179e76539fe.html language=enus -->
## TOPIC 00046: RFMXLTE_ATTR_CHP_MEASUREMENT_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp_1gab41db77f1f286cf01d314179e76539fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp_1gab41db77f1f286cf01d314179e76539fe.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the channel power measurement. SyntaxRFMXLTE_ATTR_CHP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To3158016int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selec

### RFMXLTE_ATTR_CHP_MEASUREMENT_ENABLED

Specifies whether to enable the channel power measurement.

#### Syntax

RFMXLTE_ATTR_CHP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158016 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp_1gad55af23cb51b2faf8329797b8c1bea0e.html language=enus -->
## TOPIC 00047: RFMXLTE_ATTR_CHP_ALL_TRACES_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp_1gad55af23cb51b2faf8329797b8c1bea0e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp_1gad55af23cb51b2faf8329797b8c1bea0e.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. SyntaxRFMXLTE_ATTR_CHP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To3158036int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the

### RFMXLTE_ATTR_CHP_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement.

#### Syntax

RFMXLTE_ATTR_CHP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158036 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp_1gaea4554baa1d39b7da7bb7ad26eee7873.html language=enus -->
## TOPIC 00048: RFMXLTE_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp_1gaea4554baa1d39b7da7bb7ad26eee7873.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp_1gaea4554baa1d39b7da7bb7ad26eee7873.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. SyntaxRFMXLTE_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTHNumeric ValueData TypeAc

### RFMXLTE_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH

Specifies the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

#### Syntax

RFMXLTE_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158050 | float64 | Read-Only | Subblock |

#### Remarks

Use "subblock<n>" as the selector string to read this result.

The default value is 0.

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp__averaging.html language=enus -->
## TOPIC 00049: Averaging

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp__averaging.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_CHP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXLTE_ATTR_CHP_AVERAGING_ENABLED attribute to True. RFMXLTE_ATTR_CHP_AVERAGING_ENABLEDSpecifies whether to enable averaging for the CHP measurement. RFMXLT

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_CHP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXLTE_ATTR_CHP_AVERAGING_ENABLED attribute to True. |
| RFMXLTE_ATTR_CHP_AVERAGING_ENABLED | Specifies whether to enable averaging for the CHP measurement. |
| RFMXLTE_ATTR_CHP_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1ga428cf6dd9fc83ad284e1736e0c91be61.html language=enus -->
## TOPIC 00050: RFMXLTE_ATTR_CHP_AVERAGING_COUNT

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1ga428cf6dd9fc83ad284e1736e0c91be61.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1ga428cf6dd9fc83ad284e1736e0c91be61.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXLTE_ATTR_CHP_AVERAGING_ENABLED attribute to True. SyntaxRFMXLTE_ATTR_CHP_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To3158022int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXLTE_ATTR_CHP_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXLTE_ATTR_CHP_AVERAGING_ENABLED](group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1ga530159183f44379fddbd06cbaac4431b.html) attribute to **True**.

#### Syntax

RFMXLTE_ATTR_CHP_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158022 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1ga530159183f44379fddbd06cbaac4431b.html language=enus -->
## TOPIC 00051: RFMXLTE_ATTR_CHP_AVERAGING_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1ga530159183f44379fddbd06cbaac4431b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1ga530159183f44379fddbd06cbaac4431b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the CHP measurement. SyntaxRFMXLTE_ATTR_CHP_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To3158023int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXLTE_ATTR_CHP_AVERAGING_ENABLED

Specifies whether to enable averaging for the CHP measurement.

#### Syntax

RFMXLTE_ATTR_CHP_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158023 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_CHP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXLTE_VAL_CHP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The CHP measurement uses the value of the RFMXLTE_ATTR_CHP_AVERAGING_COUNT attribute as the number of acquisitions over which the CHP measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1gae2d18096198077408bdcf45d9f75418d.html language=enus -->
## TOPIC 00052: RFMXLTE_ATTR_CHP_AVERAGING_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1gae2d18096198077408bdcf45d9f75418d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp__averaging_1gae2d18096198077408bdcf45d9f75418d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. SyntaxRFMXLTE_ATTR_CHP_AVERAGING_TYPENumeric ValueData TypeAccessApplies To3158025int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this

### RFMXLTE_ATTR_CHP_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement.

#### Syntax

RFMXLTE_ATTR_CHP_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158025 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_CHP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXLTE_VAL_CHP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXLTE_VAL_CHP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXLTE_VAL_CHP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXLTE_VAL_CHP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp__component__carrier.html language=enus -->
## TOPIC 00053: Component Carrier

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp__component__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp__component__carrier.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTHSpecifies the integration bandwidth of a component carrier. This value is expressed in Hz. AttachmentsNone

### Component Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH | Specifies the integration bandwidth of a component carrier. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp__component__carrier_1gaa6357a03c45dec54d042fa0fd8035234.html language=enus -->
## TOPIC 00054: RFMXLTE_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp__component__carrier_1gaa6357a03c45dec54d042fa0fd8035234.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp__component__carrier_1gaa6357a03c45dec54d042fa0fd8035234.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of a component carrier. This value is expressed in Hz. SyntaxRFMXLTE_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To3158018float64Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to

### RFMXLTE_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

Specifies the integration bandwidth of a component carrier. This value is expressed in Hz.

#### Syntax

RFMXLTE_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3158018 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

The default value is 9 MHz.

Parent topic:

Component Carrier

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__chp__noise__calibration.html language=enus -->
## TOPIC 00055: Noise Calibration

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__chp__noise__calibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__chp__noise__calibration.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingGroup membersNameDescriptionRFMXLTE_ATTR_CHP_NOISE_CALIBRATION_MODESpecifies whether the noise calibration and measurement is performed automatically by the measurement or initiated by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more

### Noise Calibration

#### Groups

- Averaging

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_MODE | Specifies whether the noise calibration and measurement is performed automatically by the measurement or initiated by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__pdsch_1ga5a650910f2f603f2d104c7aaf98410b4.html language=enus -->
## TOPIC 00056: RFMXLTE_ATTR_NUMBER_OF_PDSCH_CHANNELS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__pdsch_1ga5a650910f2f603f2d104c7aaf98410b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__pdsch_1ga5a650910f2f603f2d104c7aaf98410b4.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of physical downlink shared channel (PDSCH) allocations in a subframe. SyntaxRFMXLTE_ATTR_NUMBER_OF_PDSCH_CHANNELSNumeric ValueData TypeAccessApplies To3145801int32Read/WriteSubframeRemarks Use "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subf

### RFMXLTE_ATTR_NUMBER_OF_PDSCH_CHANNELS

Specifies the number of physical downlink shared channel (PDSCH) allocations in a subframe.

#### Syntax

RFMXLTE_ATTR_NUMBER_OF_PDSCH_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145801 | int32 | Read/Write | Subframe |

#### Remarks

Use "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<<i>l</i>>" as the selector string to configure or read this attribute.

The default value is 1. Valid values are 0 to 100, inclusive.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__pdsch_1ga676a000d2954a0a2b8081ee93242826a.html language=enus -->
## TOPIC 00057: RFMXLTE_ATTR_PDSCH_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__pdsch_1ga676a000d2954a0a2b8081ee93242826a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__pdsch_1ga676a000d2954a0a2b8081ee93242826a.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the RFMXLTE_ATTR_DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO attribute to calculate the Rb. Refer to section 3.3 of the 3

### RFMXLTE_ATTR_PDSCH_POWER

Specifies the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the [RFMXLTE_ATTR_DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO](group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined_1ga4e172d867cfb5ea23eb8edbfc552d50c.html) attribute to calculate the Rb. Refer to section 3.3 of the *3GPP 36.521* specification for more information about Ra.

#### Syntax

RFMXLTE_ATTR_PDSCH_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145804 | float64 | Read/Write | PDSCH |

#### Remarks

Use "PDSCH<<i>m</i>>" or "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<<i>l</i>>/PDSCH<<i>m</i>>" as the selector string to configure or read this attribute.

The default value is 0.

Parent topic:

PDSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__phich.html language=enus -->
## TOPIC 00058: PHICH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__phich.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__phich.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_PHICH_DURATIONSpecifies the physical hybrid-ARQ indicator channel (PHICH) duration. RFMXLTE_ATTR_PHICH_POWERSpecifies the power of all BPSK symbols in a physical hybrid-ARQ indicator channel (PHICH) sequence. This value is expressed in dB. RFMXLTE_A

### PHICH

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_PHICH_DURATION | Specifies the physical hybrid-ARQ indicator channel (PHICH) duration. |
| RFMXLTE_ATTR_PHICH_POWER | Specifies the power of all BPSK symbols in a physical hybrid-ARQ indicator channel (PHICH) sequence. This value is expressed in dB. |
| RFMXLTE_ATTR_PHICH_RESOURCE | Specifies the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This attribute is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. |

#### Attachments

None

Parent topic:

User Defined

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__phich_1ga8391e55d874e37717d9049a1d6438a68.html language=enus -->
## TOPIC 00059: RFMXLTE_ATTR_PHICH_RESOURCE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__phich_1ga8391e55d874e37717d9049a1d6438a68.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__downlink__user__defined__phich_1ga8391e55d874e37717d9049a1d6438a68.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This attribute is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. SyntaxRFMXLTE_ATTR_PHICH_RESO

### RFMXLTE_ATTR_PHICH_RESOURCE

Specifies the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This attribute is used to calculate number of PHICH resource groups. Refer to section 6.9 of the *3GPP 36.211* specification for more information about PHICH.

#### Syntax

RFMXLTE_ATTR_PHICH_RESOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145798 | int32 | Read/Write | Subframe |

#### Remarks

Use "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<<i>l</i>>" as the selector string to configure or read this attribute.

The default value is **1/6**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE_SIXTH | 0 (0x0) | Specifies the PHICH resource value is 1/6. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_HALF | 1 (0x1) | Specifies the PHICH resource value is 1/2. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE | 2 (0x2) | Specifies the PHICH resource value is 1. |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_TWO | 3 (0x3) | Specifies the PHICH resource value is 2. |

Parent topic:

PHICH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__downlink_1ga56ad67f7b38781ddfb96bc47f37b1204.html language=enus -->
## TOPIC 00060: RFMXLTE_ATTR_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__downlink_1ga56ad67f7b38781ddfb96bc47f37b1204.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__downlink_1ga56ad67f7b38781ddfb96bc47f37b1204.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the downlink channel configuration mode for NB-IoT. SyntaxRFMXLTE_ATTR_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODENumeric ValueData TypeAccessApplies To3162244int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instan

### RFMXLTE_ATTR_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE

Specifies the downlink channel configuration mode for NB-IoT.

#### Syntax

RFMXLTE_ATTR_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162244 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Test Model**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE_USER_DEFINED | 1 (0x1) | You have to manually set all the signals and channels. |
| RFMXLTE_VAL_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL | 2 (0x2) | Configures all the signals and channels automatically according to the 3GPP NB-IoT test model specification. |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1ga5fbc41339f07d85718cca6870319b711.html language=enus -->
## TOPIC 00061: RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1ga5fbc41339f07d85718cca6870319b711.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1ga5fbc41339f07d85718cca6870319b711.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). SyntaxRFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONESNumeric ValueData TypeAccessApplies To3162211int32Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>/c

### RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES

Specifies the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH).

#### Syntax

RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162211 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is 1.

For Format 1 and 15 kHz subcarrier spacing, the valid values are 1, 3, 6, and 12.

For Format 1, 3.75 kHz subcarrier spacing, and Format 2, the valid value is 1.

Parent topic:

NPUSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1gad4cdc305cb221ee0e6145791a2e2394b.html language=enus -->
## TOPIC 00062: RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1gad4cdc305cb221ee0e6145791a2e2394b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1gad4cdc305cb221ee0e6145791a2e2394b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). This attribute is valid when RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES is equal to 1 and RFMXLTE_ATTR_NPUSCH_FORMAT is equal to 1. The modulation type for other configurations is defined in Table 10.1.3.2

### RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE

Specifies the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). This attribute is valid when [RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES](group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1ga5fbc41339f07d85718cca6870319b711.html) is equal to 1 and [RFMXLTE_ATTR_NPUSCH_FORMAT](group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1gad7be9832301b5753d6ccdcc95f5ecce6.html) is equal to 1. The modulation type for other configurations is defined in Table 10.1.3.2-1 of the *3GPP TS 36.211* specification.

#### Syntax

RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162212 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is **BPSK**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_NPUSCH_MODULATION_TYPE_BPSK | 0 (0x0) | Specifies a BPSK modulation scheme. |
| RFMXLTE_VAL_NPUSCH_MODULATION_TYPE_QPSK | 1 (0x1) | Specifies a QPSK modulation scheme. |

Parent topic:

NPUSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink_1ga79701786570728418227c2c14b30074c.html language=enus -->
## TOPIC 00063: RFMXLTE_ATTR_UPLINK_SEQUENCE_HOPPING_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink_1ga79701786570728418227c2c14b30074c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink_1ga79701786570728418227c2c14b30074c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the base sequence number hopping for the demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. This attribute is only valid only when you set the RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS attribute to a value greater

### RFMXLTE_ATTR_UPLINK_SEQUENCE_HOPPING_ENABLED

Specifies whether the base sequence number hopping for the demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the *3GPP TS 36.211* specification. This attribute is only valid only when you set the [RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS](group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga97521db28048de61a5815678ff7a7448.html) attribute to a value greater than 5.

#### Syntax

RFMXLTE_ATTR_UPLINK_SEQUENCE_HOPPING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145754 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_UPLINK_SEQUENCE_HOPPING_ENABLED_FALSE | 0 (0x0) | The measurement uses zero as the base sequence number for all the slots. |
| RFMXLTE_VAL_UPLINK_SEQUENCE_HOPPING_ENABLED_TRUE | 1 (0x1) | Calculates the base sequence number for each slot, as defined in the section 5.5.1.4 of 3GPP 36.211 specification. |

Parent topic:

Uplink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch.html language=enus -->
## TOPIC 00064: PUSCH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_DMRS_OCC_ENABLEDSpecifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this attribute to TRUE for multi antenna cases. RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD

### PUSCH

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_DMRS_OCC_ENABLED | Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this attribute to TRUE for multi antenna cases. |
| RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD | Specifies the cyclic shift field in uplink-related DCI format. When the RFMXLTE_ATTR_DMRS_OCC_ENABLED attribute is set to True,. |
| RFMXLTE_ATTR_PUSCH_DELTA_SEQUENCE_SHIFT | Specifies the physical uplink shared channel (PUSCH) delta sequence shift, which is used to calculate cyclic shift of the demodulation reference signal (DMRS). Refer to section 5.5.2.1.1 of the 3GPP TS 36.211 specification for more information about the PUSCH delta sequence shift. |
| RFMXLTE_ATTR_PUSCH_MODULATION_TYPE | Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. |
| RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS | Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. |
| RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS | Specifies the number of resource allocation clusters, with each cluster including one or more consecutive resource blocks. Refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification for more information about the number of channels in the physical uplink shared channel (PUSCH). |
| RFMXLTE_ATTR_PUSCH_N_DMRS_1 | Specifies the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. |
| RFMXLTE_ATTR_PUSCH_N_DMRS_2 | Specifies the n_DMRS_2 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a slot. The valid values for this attribute are, as defined in table 5.5.2.1.1-1 of the 3GPP TS 36.211 specification. |
| RFMXLTE_ATTR_PUSCH_POWER | Specifies the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. |
| RFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET | Specifies the starting resource block number of a physical uplink shared channel (PUSCH) cluster. |

#### Attachments

None

Parent topic:

Uplink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga3d7d2b631191ff36f75af79a270552cb.html language=enus -->
## TOPIC 00065: RFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga3d7d2b631191ff36f75af79a270552cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga3d7d2b631191ff36f75af79a270552cb.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting resource block number of a physical uplink shared channel (PUSCH) cluster. SyntaxRFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSETNumeric ValueData TypeAccessApplies To3145758int32Read/WriteClusterRemarks Use "cluster<<i>l</i>>" or "carrier<k>" or "subblock<n>/carrier<k>"/cluster<l>" a

### RFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

Specifies the starting resource block number of a physical uplink shared channel (PUSCH) cluster.

#### Syntax

RFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145758 | int32 | Read/Write | Cluster |

#### Remarks

Use "cluster<<i>l</i>>" or "carrier<k>" or "subblock<n>/carrier<k>"/cluster<*l*>" as the selector string to configure or read this attribute.

The default value is 0.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga5ea7c448dea459e3efacd0ed0e34898c.html language=enus -->
## TOPIC 00066: RFMXLTE_ATTR_DMRS_OCC_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga5ea7c448dea459e3efacd0ed0e34898c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga5ea7c448dea459e3efacd0ed0e34898c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this attribute to TRUE for multi antenna cases. SyntaxRFMXLTE_ATTR_DMRS_OCC_ENABLEDNumeric ValueData TypeAccessApplies To3145809int32Read/WriteCarrierRe

### RFMXLTE_ATTR_DMRS_OCC_ENABLED

Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this attribute to **TRUE** for multi antenna cases.

#### Syntax

RFMXLTE_ATTR_DMRS_OCC_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145809 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_DMRS_OCC_ENABLED_FALSE | 0 (0x0) | The measurement ignores the RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD and uses the RFMXLTE_ATTR_PUSCH_N_DMRS_2 field for DMRS calculations. |
| RFMXLTE_VAL_DMRS_OCC_ENABLED_TRUE | 1 (0x1) | The measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the value of PUSCH n_DMRS_2 and [w(0) w(1)] for DMRS signal based on the values you set for the Cyclic Shift Field and RFMXLTE_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE. |

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga97521db28048de61a5815678ff7a7448.html language=enus -->
## TOPIC 00067: RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga97521db28048de61a5815678ff7a7448.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga97521db28048de61a5815678ff7a7448.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. SyntaxRFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKSNumeric ValueData TypeAccessApplies To3145762int32Read/WriteClusterRemarks Use "cluster<<i>l</i>>" or "carrier<k>" or "subblock<n>/carrier<k>"/cl

### RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster.

#### Syntax

RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145762 | int32 | Read/Write | Cluster |

#### Remarks

Use "cluster<<i>l</i>>" or "carrier<k>" or "subblock<n>/carrier<k>"/cluster<*l*>" as the selector string to configure or read this attribute.

The default value is -1. If you set this attribute to -1, all available resource blocks for the specified bandwidth are configured.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1gad4b790f54bf7bf80560a18f652ecba99.html language=enus -->
## TOPIC 00068: RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1gad4b790f54bf7bf80560a18f652ecba99.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1gad4b790f54bf7bf80560a18f652ecba99.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the cyclic shift field in uplink-related DCI format. When the RFMXLTE_ATTR_DMRS_OCC_ENABLED attribute is set to True,. SyntaxRFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELDNumeric ValueData TypeAccessApplies To3145810int32Read/WriteCarrierRemarks the measurement uses the table 5.5.2.1.1-1 of 3GPP 36

### RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD

Specifies the cyclic shift field in uplink-related DCI format. When the [RFMXLTE_ATTR_DMRS_OCC_ENABLED](group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__pusch_1ga5ea7c448dea459e3efacd0ed0e34898c.html) attribute is set to **True**,.

#### Syntax

RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145810 | int32 | Read/Write | Carrier |

#### Remarks

the measurement uses the table 5.5.2.1.1-1 of *3GPP 36.211* specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with [RFMXLTE_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE](group____root__ni_r_fmx_l_t_e__attributes_1ga24a24797a97396a5bd86f4260daf3b06.html).

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is 0. Valid values are 0 to 7, inclusive.

Parent topic:

PUSCH

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga02c8c36588016e24cb31b4e860881de6.html language=enus -->
## TOPIC 00069: RFMXLTE_ATTR_SRS_SUBFRAME6_N_RA

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga02c8c36588016e24cb31b4e860881de6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga02c8c36588016e24cb31b4e860881de6.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5. SyntaxRFMXLTE_ATTR_SRS_SUBFRAME6_N_RANumeric ValueData TypeAccessApplies To3145784int32Read/WriteCarrierRemarks Use "carrier<k>" or "sub

### RFMXLTE_ATTR_SRS_SUBFRAME6_N_RA

Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5.

#### Syntax

RFMXLTE_ATTR_SRS_SUBFRAME6_N_RA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145784 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is 0. Valid values are 0 to 6.

Parent topic:

SRS

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga11207b020a5f652bc48c0a348f2d8baf.html language=enus -->
## TOPIC 00070: RFMXLTE_ATTR_SRS_SUBFRAME_CONFIGURATION

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga11207b020a5f652bc48c0a348f2d8baf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga11207b020a5f652bc48c0a348f2d8baf.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SRS subframe configuration specified in the Table 5.5.3.3-1 of 3GPP 36.211 specification. It is a cell-specific attribute. This attribute defines the subframes that are reserved for SRS transmission in a given cell. SyntaxRFMXLTE_ATTR_SRS_SUBFRAME_CONFIGURATIONNumeric ValueData TypeAcc

### RFMXLTE_ATTR_SRS_SUBFRAME_CONFIGURATION

Specifies the SRS subframe configuration specified in the Table 5.5.3.3-1 of *3GPP 36.211* specification. It is a cell-specific attribute. This attribute defines the subframes that are reserved for SRS transmission in a given cell.

#### Syntax

RFMXLTE_ATTR_SRS_SUBFRAME_CONFIGURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145774 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is 0. When you set the [RFMXLTE_ATTR_DUPLEX_SCHEME](group____root__ni_r_fmx_l_t_e__attributes_1gab346ce526a57059115f151e4bb5d17d8.html) attribute to **FDD**, valid values are from 0 to 14, and when you set the Duplex Scheme attribute to **TDD**, valid values are from 0 to 13.

Parent topic:

SRS

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga41e3990c45485743df8a18d01ecaaede.html language=enus -->
## TOPIC 00071: RFMXLTE_ATTR_SRS_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga41e3990c45485743df8a18d01ecaaede.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga41e3990c45485743df8a18d01ecaaede.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB. SyntaxRFMXLTE_ATTR_SRS_POWERNumeric ValueData TypeAccessApplies To3145785float64Read/WriteCarrierRemarks Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure o

### RFMXLTE_ATTR_SRS_POWER

Specifies the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB.

#### Syntax

RFMXLTE_ATTR_SRS_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145785 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is 0.

Parent topic:

SRS

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga5e83f5971540114afcdc570c8bfafbec.html language=enus -->
## TOPIC 00072: RFMXLTE_ATTR_SRS_N_SRS_CS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga5e83f5971540114afcdc570c8bfafbec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga5e83f5971540114afcdc570c8bfafbec.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the cyclic shift value n[SRS ]SyntaxRFMXLTE_ATTR_SRS_N_SRS_CSNumeric ValueData TypeAccessApplies To3145779int32Read/WriteCarrierRemarks^CS used for generating SRS base sequence. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details.Use "carrier<k>" or "subblock<n>/carrier<

### RFMXLTE_ATTR_SRS_N_SRS_CS

Specifies the cyclic shift value *n<sub>SRS</sub>*

#### Syntax

RFMXLTE_ATTR_SRS_N_SRS_CS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145779 | int32 | Read/Write | Carrier |

#### Remarks

<sup>CS</sup> used for generating SRS base sequence. Refer to section 5.5.3.2 of *3GPP 36.211* specification for more details.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is 0. Valid values are from 0 to 7, inclusive.

Parent topic:

SRS

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga618cea211a6cb9b2a6d2924ad65f5e9e.html language=enus -->
## TOPIC 00073: RFMXLTE_ATTR_SRS_N_RRC

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga618cea211a6cb9b2a6d2924ad65f5e9e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__component__carrier__uplink__srs_1ga618cea211a6cb9b2a6d2924ad65f5e9e.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SRS frequency domain position n[RRC ]SyntaxRFMXLTE_ATTR_SRS_N_RRCNumeric ValueData TypeAccessApplies To3145778int32Read/WriteCarrierRemarks . Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details.Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to co

### RFMXLTE_ATTR_SRS_N_RRC

Specifies the SRS frequency domain position *n<sub>RRC</sub>*

#### Syntax

RFMXLTE_ATTR_SRS_N_RRC

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145778 | int32 | Read/Write | Carrier |

#### Remarks

. Refer to section 5.5.3.2 of *3GPP 36.211* specification for more details.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this attribute.

The default value is 0. Valid values are from 0 to 23, inclusive.

Parent topic:

SRS

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga53d3cef654bbd59a593979dc34bd48df.html language=enus -->
## TOPIC 00074: RFMXLTE_ATTR_MODACC_ALL_TRACES_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga53d3cef654bbd59a593979dc34bd48df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga53d3cef654bbd59a593979dc34bd48df.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. SyntaxRFMXLTE_ATTR_MODACC_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To3162125int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute f

### RFMXLTE_ATTR_MODACC_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.

#### Syntax

RFMXLTE_ATTR_MODACC_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162125 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga65079c937b9e1c84846bd23510eb4fec.html language=enus -->
## TOPIC 00075: RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga65079c937b9e1c84846bd23510eb4fec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga65079c937b9e1c84846bd23510eb4fec.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. SyntaxRFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODENumeric ValueData TypeAccessApplies To3162115int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal

### RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE

Specifies whether the measurement is performed from the frame or the slot boundary.

#### Syntax

RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162115 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Refer to the [LTE Modulation Accuracy](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-modulation-accuracy.html) topic for more information about synchronization mode.

Slot

Note

When you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Downlink**, the measurement supports only **Frame** synchronization mode.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute, starting at the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute from the frame boundary. When you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to Digital Edge, the measurement expects a trigger at the frame boundary. |
| RFMXLTE_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected, and the measurement is performed over the ModAcc Meas Length attribute starting at the ModAcc Meas Offset attribute from the slot boundary. When you set the Trigger Type attribute to Digital Edge, the measurement expects a trigger at any slot boundary. |
| RFMXLTE_VAL_MODACC_SYNCHRONIZATION_MODE_MARKER | 2 (0x2) | The measurement expects a marker (trigger) at the frame boundary from the user. The measurement takes advantage of triggered acquisitions to reduce processing resulting in faster measurement time. Measurement is performed over the ModAcc Meas Length attribute starting at ModAcc Meas Offset attribute from the frame boundary. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc_1gae276c492691d99063b3f177977305da2.html language=enus -->
## TOPIC 00076: RFMXLTE_ATTR_MODACC_FFT_WINDOW_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc_1gae276c492691d99063b3f177977305da2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc_1gae276c492691d99063b3f177977305da2.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type used for the EVM calculation for the ModAcc measurement. SyntaxRFMXLTE_ATTR_MODACC_FFT_WINDOW_TYPENumeric ValueData TypeAccessApplies To3162168int32Read/WriteN/ARemarks Refer to the LTE Modulation Accuracy topic for more information about FFT window type.The default val

### RFMXLTE_ATTR_MODACC_FFT_WINDOW_TYPE

Specifies the FFT window type used for the EVM calculation for the ModAcc measurement.

#### Syntax

RFMXLTE_ATTR_MODACC_FFT_WINDOW_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162168 | int32 | Read/Write | N/A |

#### Remarks

Refer to the [LTE Modulation Accuracy](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-modulation-accuracy.html) topic for more information about FFT window type.

The default value is **Custom**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP | 0 (0x0) | The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The FFT window positions are specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. Refer to the Annexe E.3.2 of 3GPP TS 36.521 specification for more information on the FFT window. |
| RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM | 1 (0x1) | Only one FFT window position is used for the EVM calculation. FFT window position is specified by RFMXLTE_ATTR_MODACC_FFT_WINDOW_OFFSET attribute. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__iq__impairments_1ga6a96731842e873f7cba9b6e811c38d81.html language=enus -->
## TOPIC 00077: RFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__iq__impairments_1ga6a96731842e873f7cba9b6e811c38d81.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__iq__impairments_1ga6a96731842e873f7cba9b6e811c38d81.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to estimate IQ origin offset. SyntaxRFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLEDNumeric ValueData TypeAccessApplies To3162233int32Read/WriteN/ARemarksIQ origin offset estimation is supported only when you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to Uplink or Sidelin

### RFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED

Specifies whether to estimate IQ origin offset.

#### Syntax

RFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162233 | int32 | Read/Write | N/A |

#### Remarks

Note

IQ origin offset estimation is supported only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink** or **Sidelink** .

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_FALSE | 0 (0x0) | IQ origin offset estimation and correction is disabled. |
| RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_TRUE | 1 (0x1) | IQ origin offset estimation and correction is enabled. |

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__iq__impairments_1ga84a4be770b5b798473b3a02a7a3fd024.html language=enus -->
## TOPIC 00078: RFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__iq__impairments_1ga84a4be770b5b798473b3a02a7a3fd024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__iq__impairments_1ga84a4be770b5b798473b3a02a7a3fd024.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable IQ gain imbalance correction. SyntaxRFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLEDNumeric ValueData TypeAccessApplies To3162235int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance.

### RFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED

Specifies whether to enable IQ gain imbalance correction.

#### Syntax

RFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162235 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE | 0 (0x0) | IQ gain imbalance correction is disabled. |
| RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_TRUE | 1 (0x1) | IQ gain imbalance correction is enabled. |

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results.html language=enus -->
## TOPIC 00079: Results

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDownlinkSidelinkSpectral FlatnessUplinkGroup membersNameDescriptionRFMXLTE_ATTR_MODACC_RESULTS_IN_BAND_EMISSION_MARGINReturns the in-band emission margin. This value is expressed in dB. RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVMReturns the maximum value of the peak EVMs calculated

### Results

#### Groups

- Downlink
- Sidelink
- Spectral Flatness
- Uplink

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_MODACC_RESULTS_IN_BAND_EMISSION_MARGIN | Returns the in-band emission margin. This value is expressed in dB. |
| RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM | Returns the maximum value of the peak EVMs calculated on all the configured channels over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_MAGNITUDE_ERROR | Returns the peak value of the composite magnitude error calculated over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute on all the configured channels. |
| RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_PHASE_ERROR | Returns the peak value of phase error calculated over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute on all thee configured channels. This value is expressed in degrees. |
| RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_FREQUENCY_ERROR | Returns the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in Hz. |
| RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_IQ_ORIGIN_OFFSET | Returns the estimated maximum IQ origin offset over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBc. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_FREQUENCY_ERROR | Returns the estimated carrier frequency offset averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in Hz. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE | Returns the estimated I/Q gain imbalance averaged over the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET | Returns the estimated I/Q origin offset averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBc. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_TIMING_SKEW | Returns the estimated IQ timing skew averaged over measured length. IQ timing skew is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_QUADRATURE_ERROR | Returns the estimated quadrature error averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in degrees. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_COMPOSITE_EVM | Returns the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_COMPOSITE_MAGNITUDE_ERROR | Returns the RMS mean value of the composite magnitude error calculated over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute on all the configured channels. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_COMPOSITE_PHASE_ERROR | Returns the RMS mean value of the composite phase error calculated over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute on all the configured channels. This value is expressed in degrees. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_SYMBOL_CLOCK_ERROR | Returns the estimated symbol clock error averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in ppm. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_TIME_OFFSET | Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. This value is expressed in seconds. |
| RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX | Returns the slot index where the RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM occurs. |
| RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX | Returns the subcarrier index where the RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM for ModAcc occurs. |
| RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SYMBOL_INDEX | Returns the symbol index of the RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_IQ_GAIN_IMBALANCE | Returns the estimated I/Q gain imbalance averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dB. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured in the subblock. |
| RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_IQ_ORIGIN_OFFSET | Returns the estimated I/Q origin offset averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute in the subblock. This value is expressed in dBc. |
| RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR | Returns the estimated quadrature error averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga0d47a96168f68d23a6eccdb04b04c989.html language=enus -->
## TOPIC 00080: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_TIME_OFFSET

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga0d47a96168f68d23a6eccdb04b04c989.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga0d47a96168f68d23a6eccdb04b04c989.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE attribute. This value is expressed in seconds. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MEAN_TIME_OFFSETNumeric ValueData TypeAccessA

### RFMXLTE_ATTR_MODACC_RESULTS_MEAN_TIME_OFFSET

Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of [RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga65079c937b9e1c84846bd23510eb4fec.html) attribute. This value is expressed in seconds.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_TIME_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162151 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga2638bbf5d5fe42ca6dd7346196172557.html language=enus -->
## TOPIC 00081: RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga2638bbf5d5fe42ca6dd7346196172557.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga2638bbf5d5fe42ca6dd7346196172557.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subcarrier index where the RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM for ModAcc occurs. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEXNumeric ValueData TypeAccessApplies To3162133int32Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>/carrier<k>"

### RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX

Returns the subcarrier index where the [RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM](group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gafefe38878077ed3cf2034adea7aacd23.html) for ModAcc occurs.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162133 | int32 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga2b9feb1f642327ccb0b47c3b6c3d3627.html language=enus -->
## TOPIC 00082: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga2b9feb1f642327ccb0b47c3b6c3d3627.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga2b9feb1f642327ccb0b47c3b6c3d3627.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated I/Q gain imbalance averaged over the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_GAI

### RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE

Returns the estimated I/Q gain imbalance averaged over the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html). The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162148 | float64 | Read-Only | Carrier |

#### Remarks

Note

When you set the [RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH](group____root__ni_r_fmx_l_t_e__attributes__component__carrier_1ga670f71a39fab2b7edb0fe4096f2892d1.html) attribute to **200.0 k** and the [RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES](group____root__ni_r_fmx_l_t_e__attributes__component__carrier__nbiot__npusch_1ga5fbc41339f07d85718cca6870319b711.html) attribute to 12, this result is available. For other values of NPUSCH Num Tones, this result will be reported as NaN.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga4ad914ccb47d27bd12520cc288cf2ea3.html language=enus -->
## TOPIC 00083: RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga4ad914ccb47d27bd12520cc288cf2ea3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga4ad914ccb47d27bd12520cc288cf2ea3.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated quadrature error averaged over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in t

### RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR

Returns the estimated quadrature error averaged over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162177 | float64 | Read-Only | Subblock |

#### Remarks

This result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink** and the [RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga5d643b5746c2f72fdd88fc489c5d66e8.html) attribute to **LO per Subblock**. Otherwise, this parameter returns NaN, as measurement of this result is currently not supported.

Use "subblock<n>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga52adfcb83a088200cd745fce9d811203.html language=enus -->
## TOPIC 00084: RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga52adfcb83a088200cd745fce9d811203.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga52adfcb83a088200cd745fce9d811203.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated maximum IQ origin offset over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBc. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To3162160float64Read-OnlyCarrierRemarks

### RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_IQ_ORIGIN_OFFSET

Returns the estimated maximum IQ origin offset over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute. This value is expressed in dBc.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162160 | float64 | Read-Only | Carrier |

#### Remarks

This result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink** or **NB-IoT Downlink**.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga7461600be093af5b766e0aa46178ff32.html language=enus -->
## TOPIC 00085: RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_FREQUENCY_ERROR

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga7461600be093af5b766e0aa46178ff32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga7461600be093af5b766e0aa46178ff32.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in Hz. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_FREQUENCY_ERRORNumeri

### RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_FREQUENCY_ERROR

Returns the estimated maximum carrier frequency offset per slot in case of **Uplink** and per subframe in case of **Downlink** over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162243 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga8cca5d53f952c9d1ba1a67898504a756.html language=enus -->
## TOPIC 00086: RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_MAGNITUDE_ERROR

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga8cca5d53f952c9d1ba1a67898504a756.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1ga8cca5d53f952c9d1ba1a67898504a756.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value of the composite magnitude error calculated over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute on all the configured channels. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To3162171flo

### RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_MAGNITUDE_ERROR

Returns the peak value of the composite magnitude error calculated over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute on all the configured channels.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162171 | float64 | Read-Only | Carrier |

#### Remarks

When you set the [RFMXLTE_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga38ac29765674be0a00483d3ff897ed09.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

This result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink**.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gaa9158241e8a9258453585fc4d2b9183b.html language=enus -->
## TOPIC 00087: RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_PHASE_ERROR

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gaa9158241e8a9258453585fc4d2b9183b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gaa9158241e8a9258453585fc4d2b9183b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value of phase error calculated over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute on all thee configured channels. This value is expressed in degrees. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_PHASE_ERRORNumeric ValueData TypeAccessAppli

### RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_PHASE_ERROR

Returns the peak value of phase error calculated over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute on all thee configured channels. This value is expressed in degrees.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162173 | float64 | Read-Only | Carrier |

#### Remarks

This result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink**.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gac2bc9e867a14b6324c323140576c4f41.html language=enus -->
## TOPIC 00088: RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gac2bc9e867a14b6324c323140576c4f41.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gac2bc9e867a14b6324c323140576c4f41.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the slot index where the RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM occurs. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEXNumeric ValueData TypeAccessApplies To3162131int32Read-OnlyCarrierRemarks Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string

### RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX

Returns the slot index where the [RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM](group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gafefe38878077ed3cf2034adea7aacd23.html) occurs.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162131 | int32 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gafefe38878077ed3cf2034adea7aacd23.html language=enus -->
## TOPIC 00089: RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gafefe38878077ed3cf2034adea7aacd23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results_1gafefe38878077ed3cf2034adea7aacd23.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the peak EVMs calculated on all the configured channels over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVMNumeric ValueData TypeAccessApplies To3162128float64Read-OnlyCarrierRemar

### RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM

Returns the maximum value of the peak EVMs calculated on all the configured channels over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162128 | float64 | Read-Only | Carrier |

#### Remarks

When you set the [RFMXLTE_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga38ac29765674be0a00483d3ff897ed09.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink.html language=enus -->
## TOPIC 00090: Downlink

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNPDSCHPDSCHGroup membersNameDescriptionRFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_DETECTED_CELL_IDReturns the detected cell ID value. RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_NRS_TRANSMIT_POWERReturns the mean value of power calculated on NB-IoT downlink reference signal (NRS) resource elements over the

### Downlink

#### Groups

- NPDSCH
- PDSCH

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_DETECTED_CELL_ID | Returns the detected cell ID value. |
| RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_NRS_TRANSMIT_POWER | Returns the mean value of power calculated on NB-IoT downlink reference signal (NRS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. |
| RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER | Returns the mean value of power calculated in one OFDM symbol over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. |
| RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER | Returns the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_CSRS_EVM | Returns the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NPSS_EVM | Returns the mean value of RMS EVMs calculated on NB-IoT primary synchronization signal (NPSS) channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NRS_EVM | Returns the mean value of RMS EVMs calculated on NRS resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NSSS_EVM | Returns the mean value of RMS EVMs calculated on NB-IoT secondary synchronization signal (NSSS) channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PBCH_EVM | Returns the mean value of RMS EVMs calculated on PBCH channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PCFICH_EVM | Returns the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PDCCH_EVM | Returns the mean value of RMS EVMs calculated on PDCCH channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PHICH_EVM | Returns the mean value of RMS EVMs calculated on PHICH channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PSS_EVM | Returns the mean value of RMS EVMs calculated on primary synchronization signal (PSS) channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_SSS_EVM | Returns the mean value of RMS EVMs calculated on secondary synchronization signal (SSS) channel over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1ga29f0a744497569d1672612076c7a37c6.html language=enus -->
## TOPIC 00091: RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NRS_EVM

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1ga29f0a744497569d1672612076c7a37c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1ga29f0a744497569d1672612076c7a37c6.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on NRS resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NRS_EVMNumeric ValueData TypeAccessApplies To3162259float64Read-OnlyCarrierRemarks When you set the RFMX

### RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NRS_EVM

Returns the mean value of RMS EVMs calculated on NRS resource elements over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NRS_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162259 | float64 | Read-Only | Carrier |

#### Remarks

When you set the [RFMXLTE_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga38ac29765674be0a00483d3ff897ed09.html) attribute to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the measurement returns this result in dB.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1ga7c81c2d0f019c989e35899e5e93b6d2f.html language=enus -->
## TOPIC 00092: RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1ga7c81c2d0f019c989e35899e5e93b6d2f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1ga7c81c2d0f019c989e35899e5e93b6d2f.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of power calculated in one OFDM symbol over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWERNumeric ValueData TypeAccessApplies To3162194float64Rea

### RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER

Returns the mean value of power calculated in one OFDM symbol over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute. This value is expressed in dBm.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162194 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1gab31f2bc943f16f7d48b203fef791ed76.html language=enus -->
## TOPIC 00093: RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1gab31f2bc943f16f7d48b203fef791ed76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__modacc__results__downlink_1gab31f2bc943f16f7d48b203fef791ed76.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. SyntaxRFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWERNumeric ValueData TypeAc

### RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER

Returns the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) attribute. This value is expressed in dBm.

#### Syntax

RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3162193 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__obw__sweep__time_1ga10912534e8cc634b7b09e9f393dbe7ef.html language=enus -->
## TOPIC 00094: RFMXLTE_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__obw__sweep__time_1ga10912534e8cc634b7b09e9f393dbe7ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__obw__sweep__time_1ga10912534e8cc634b7b09e9f393dbe7ef.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXLTE_ATTR_OBW_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To3170319int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXLTE_ATTR_OBW_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXLTE_ATTR_OBW_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3170319 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXLTE_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time of 1 ms. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__pvt_1ga076a455fccba83567922db245ba5ce85.html language=enus -->
## TOPIC 00095: RFMXLTE_ATTR_PVT_OFF_POWER_EXCLUSION_AFTER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__pvt_1ga076a455fccba83567922db245ba5ce85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__pvt_1ga076a455fccba83567922db245ba5ce85.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time excluded from the Off region after the burst. This value is expressed in seconds. SyntaxRFMXLTE_ATTR_PVT_OFF_POWER_EXCLUSION_AFTERNumeric ValueData TypeAccessApplies To3182614float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute f

### RFMXLTE_ATTR_PVT_OFF_POWER_EXCLUSION_AFTER

Specifies the time excluded from the Off region after the burst. This value is expressed in seconds.

#### Syntax

RFMXLTE_ATTR_PVT_OFF_POWER_EXCLUSION_AFTER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3182614 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Refer to the [LTE PVT (Power Vs Time) Measurement](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-power-vs-time.html) topic for more information about OFF power exclusion.

The default value is 0.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__pvt_1ga4882cbb8131df2cc5127f27517a0a491.html language=enus -->
## TOPIC 00096: RFMXLTE_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__pvt_1ga4882cbb8131df2cc5127f27517a0a491.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__pvt_1ga4882cbb8131df2cc5127f27517a0a491.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. SyntaxRFMXLTE_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To3182604int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. Th

### RFMXLTE_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement.

#### Syntax

RFMXLTE_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3182604 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__pvt__averaging_1ga0f24169625130ea992bdeb218e84d8d4.html language=enus -->
## TOPIC 00097: RFMXLTE_ATTR_PVT_AVERAGING_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__pvt__averaging_1ga0f24169625130ea992bdeb218e84d8d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__pvt__averaging_1ga0f24169625130ea992bdeb218e84d8d4.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement. SyntaxRFMXLTE_ATTR_PVT_AVERAGING_TYPENumeric ValueData TypeAccessApplies To3182602int32Read/WriteN/ARemarks You do not need to use a selector string t

### RFMXLTE_ATTR_PVT_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement.

#### Syntax

RFMXLTE_ATTR_PVT_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3182602 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_PVT_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXLTE_VAL_PVT_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__pvt__results_1ga7cb917ea02dc7df865ea04eb7c65a9de.html language=enus -->
## TOPIC 00098: RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_BEFORE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__pvt__results_1ga7cb917ea02dc7df865ea04eb7c65a9de.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__pvt__results_1ga7cb917ea02dc7df865ea04eb7c65a9de.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power in the segment before the captured burst. The segment is defined as one subframe prior to the burst for the FDD mode and 10 SC-FDMA symbols prior to the burst for the TDD mode. This value is expressed in dBm. SyntaxRFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_BEFORENumeric

### RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_BEFORE

Returns the mean power in the segment before the captured burst. The segment is defined as one subframe prior to the burst for the FDD mode and 10 SC-FDMA symbols prior to the burst for the TDD mode. This value is expressed in dBm.

#### Syntax

RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_BEFORE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3182608 | float64 | Read-Only | Carrier |

#### Remarks

Refer to the [LTE PVT (Power Vs Time) Measurement](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-power-vs-time.html) topic for more information about OFF Power.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__pvt__results_1gae299ddbe31f93a7d08033c9d0c20b3f4.html language=enus -->
## TOPIC 00099: RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__pvt__results_1gae299ddbe31f93a7d08033c9d0c20b3f4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__pvt__results_1gae299ddbe31f93a7d08033c9d0c20b3f4.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the subframes within the captured burst. This value is expressed in dBm. The average power excludes the transient period of 20 micro seconds at the beginning. SyntaxRFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWERNumeric ValueData TypeAccessApplies To3182610float64Read-On

### RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER

Returns the average power of the subframes within the captured burst. This value is expressed in dBm. The average power excludes the transient period of 20 micro seconds at the beginning.

#### Syntax

RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3182610 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem_1ga4863d76dd77279403a7991f93a771b35.html language=enus -->
## TOPIC 00100: RFMXLTE_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem_1ga4863d76dd77279403a7991f93a771b35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem_1ga4863d76dd77279403a7991f93a771b35.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of the subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. SyntaxRFMXLTE_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTHNumeric ValueData TypeAc

### RFMXLTE_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

Returns the integration bandwidth of the subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

#### Syntax

RFMXLTE_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178577 | float64 | Read-Only | Subblock |

#### Remarks

Use "subblock<n>" as the selector string to read this result.

The default value is 0.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem_1ga5517ec1ce2b5970a7458c0d946802d07.html language=enus -->
## TOPIC 00101: RFMXLTE_ATTR_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem_1ga5517ec1ce2b5970a7458c0d946802d07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem_1ga5517ec1ce2b5970a7458c0d946802d07.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth. SyntaxRFMXLTE_ATTR_SEM_SUBBLOCK_AGGREGATED_CHA

### RFMXLTE_ATTR_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH

Returns the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth.

#### Syntax

RFMXLTE_ATTR_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178578 | float64 | Read-Only | Subblock |

#### Remarks

Use "subblock<n>" as the selector string to read this result.

The default value is 0.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem__averaging_1gaf959bf3d41c99380294980e5dfb83655.html language=enus -->
## TOPIC 00102: RFMXLTE_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem__averaging_1gaf959bf3d41c99380294980e5dfb83655.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem__averaging_1gaf959bf3d41c99380294980e5dfb83655.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. SyntaxRFMXLTE_ATTR_SEM_AVERAGING_TYPENumeric ValueData TypeAccessApplies To3178529int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this

### RFMXLTE_ATTR_SEM_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.

#### Syntax

RFMXLTE_ATTR_SEM_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178529 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXLTE_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXLTE_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXLTE_VAL_SEM_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXLTE_VAL_SEM_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1ga56ca7fcb69cd54d6aba695c311f455ed.html language=enus -->
## TOPIC 00103: RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1ga56ca7fcb69cd54d6aba695c311f455ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1ga56ca7fcb69cd54d6aba695c311f455ed.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the o

### RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB.

#### Syntax

RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178549 | float64 | Read-Only | Offset |

#### Remarks

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information about SEM offsets.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gaba20552f063a057948f523b943d5afee.html language=enus -->
## TOPIC 00104: RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gaba20552f063a057948f523b943d5afee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gaba20552f063a057948f523b943d5afee.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If

### RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB.

#### Syntax

RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178551 | float64 | Read-Only | Offset |

#### Remarks

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information about SEM offsets.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gac1d21c5dfba36e66bd2a562f043b15c3.html language=enus -->
## TOPIC 00105: RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gac1d21c5dfba36e66bd2a562f043b15c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gac1d21c5dfba36e66bd2a562f043b15c3.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the RFMXLTE_ATTR_SEM_UPLINK_MASK_TYPE attribute. SyntaxRFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To3178557int32Read-OnlyOff

### RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the [RFMXLTE_ATTR_SEM_UPLINK_MASK_TYPE](group____root__ni_r_fmx_l_t_e__attributes__sem_1gaab54fbdc3ac40374cb507b135dc83221.html) attribute.

#### Syntax

RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178557 | int32 | Read-Only | Offset |

#### Remarks

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information about SEM mask.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |
| RFMXLTE_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gafd5c37f33533041cf1a10f26d59aa62d.html language=enus -->
## TOPIC 00106: RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gafd5c37f33533041cf1a10f26d59aa62d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem__results__lower__offset_1gafd5c37f33533041cf1a10f26d59aa62d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.

### RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

Returns the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB.

#### Syntax

RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178555 | float64 | Read-Only | Offset |

#### Remarks

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information about SEM offsets.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem__results__upper__offset_1ga8a847bd3af1e457f0813d5760fe722ff.html language=enus -->
## TOPIC 00107: RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem__results__upper__offset_1ga8a847bd3af1e457f0813d5760fe722ff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem__results__upper__offset_1ga8a847bd3af1e457f0813d5760fe722ff.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.

### RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

Returns the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB.

#### Syntax

RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178568 | float64 | Read-Only | Offset |

#### Remarks

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information about SEM offsets.

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__sem__sweep__time_1gadaaca00f0d5b444cf2b27acd70ce0237.html language=enus -->
## TOPIC 00108: RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__sem__sweep__time_1gadaaca00f0d5b444cf2b27acd70ce0237.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__sem__sweep__time_1gadaaca00f0d5b444cf2b27acd70ce0237.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXLTE_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To3178534float64Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXLTE_ATTR_SEM_SWEEP_TIME_AUTO](group____root__ni_r_fmx_l_t_e__attributes__sem__sweep__time_1ga09bb892d10a5b19d0f7b1eefe6194205.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3178534 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 ms.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotphase_1ga6f6e4145b911dc29e8034bed905ad6b6.html language=enus -->
## TOPIC 00109: RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotphase_1ga6f6e4145b911dc29e8034bed905ad6b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotphase_1ga6f6e4145b911dc29e8034bed905ad6b6.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPhase measurement. SyntaxRFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To3186688int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

Specifies whether to enable the SlotPhase measurement.

#### Syntax

RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3186688 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotphase_1ga84eddcff0ea7cfd25f6ca0983a700fb8.html language=enus -->
## TOPIC 00110: RFMXLTE_ATTR_SLOTPHASE_EXCLUSION_PERIOD_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotphase_1ga84eddcff0ea7cfd25f6ca0983a700fb8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotphase_1ga84eddcff0ea7cfd25f6ca0983a700fb8.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to exclude some portions of the slots when calculating the phase. This attribute is valid only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. SyntaxRFMXLTE_ATTR_SLOTPHASE_EXCL

### RFMXLTE_ATTR_SLOTPHASE_EXCLUSION_PERIOD_ENABLED

Specifies whether to exclude some portions of the slots when calculating the phase. This attribute is valid only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the *3GPP 36.521-1* specification for more information about the exclusion.

#### Syntax

RFMXLTE_ATTR_SLOTPHASE_EXCLUSION_PERIOD_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3186695 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_SLOTPHASE_EXCLUSION_PERIOD_ENABLED_FALSE | 0 (0x0) | Phase is calculated on complete slots. |
| RFMXLTE_VAL_SLOTPHASE_EXCLUSION_PERIOD_ENABLED_TRUE | 1 (0x1) | Phase is calculated on truncated slots. The power changes at the slot boundaries are detected by the measurement, and the defined 3GPP specification period is excluded from the slots being measured. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotphase_1gad2901e2db97595687e60bcd0c7142c9c.html language=enus -->
## TOPIC 00111: RFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotphase_1gad2901e2db97595687e60bcd0c7142c9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotphase_1gad2901e2db97595687e60bcd0c7142c9c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. SyntaxRFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLEDNumeric ValueData TypeAccess

### RFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED

Specifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

#### Syntax

RFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3186696 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_FALSE | 0 (0x0) | The Sample Clock error is estimated independently. |
| RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_TRUE | 1 (0x1) | The Sample Clock error is estimated from carrier frequency offset. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotphase_1gaf2d55e33b09e208d9a7a42e6ed333e7d.html language=enus -->
## TOPIC 00112: RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_OFFSET

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotphase_1gaf2d55e33b09e208d9a7a42e6ed333e7d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotphase_1gaf2d55e33b09e208d9a7a42e6ed333e7d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the RFMXLTE_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE attribute. SyntaxRFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To3

### RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [RFMXLTE_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_l_t_e__attributes__slotphase_1gaa0d6b57784ad1c426ce57c08be561c0a.html) attribute.

#### Syntax

RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3186690 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. Valid values are 0 to 19, inclusive.

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga473c33fb1c47a35de8ec408c97d0b9e4.html language=enus -->
## TOPIC 00113: RFMXLTE_ATTR_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga473c33fb1c47a35de8ec408c97d0b9e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga473c33fb1c47a35de8ec408c97d0b9e4.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. SyntaxRFMXLTE_ATTR_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLEDNumer

### RFMXLTE_ATTR_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED

Specifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

#### Syntax

RFMXLTE_ATTR_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3190789 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED_FALSE | 0 (0x0) | The Sample Clock error is estimated independently. |
| RFMXLTE_VAL_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED_TRUE | 1 (0x1) | The Sample Clock error is estimated from carrier frequency offset. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga54f2905f42cdffcff3da2b16d5f1b3c1.html language=enus -->
## TOPIC 00114: RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga54f2905f42cdffcff3da2b16d5f1b3c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga54f2905f42cdffcff3da2b16d5f1b3c1.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of subframes to be measured. This value is expressed in subframe. SyntaxRFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To3190787int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default si

### RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

Specifies the number of subframes to be measured. This value is expressed in subframe.

#### Syntax

RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3190787 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga941e1c3c7afc2b737cff11418a01bc93.html language=enus -->
## TOPIC 00115: RFMXLTE_ATTR_SLOTPOWER_SPECTRUM_INVERTED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga941e1c3c7afc2b737cff11418a01bc93.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga941e1c3c7afc2b737cff11418a01bc93.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. SyntaxRFMXLTE_ATTR_SLOTPOWER_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To3190790int32Read/WriteN/ARemarks You do not need to

### RFMXLTE_ATTR_SLOTPOWER_SPECTRUM_INVERTED

Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

#### Syntax

RFMXLTE_ATTR_SLOTPOWER_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3190790 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXLTE_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The spectrum of the measured signal is not inverted. |
| RFMXLTE_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The measured signal is inverted and the measurement corrects the signal by swapping the I and the Q components. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga95c4b1d33b656f776b7377871a7c6704.html language=enus -->
## TOPIC 00116: RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga95c4b1d33b656f776b7377871a7c6704.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotpower_1ga95c4b1d33b656f776b7377871a7c6704.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPower measurement. SyntaxRFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To3190784int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sel

### RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

Specifies whether to enable the SlotPower measurement.

#### Syntax

RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3190784 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__slotpower_1gab15841df5025266c89f9645e6234262e.html language=enus -->
## TOPIC 00117: RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__slotpower_1gab15841df5025266c89f9645e6234262e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__slotpower_1gab15841df5025266c89f9645e6234262e.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. SyntaxRFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To3190786int32Read/WriteN/ARemarks You do not need to use a selector str

### RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe.

#### Syntax

RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3190786 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__trigger.html language=enus -->
## TOPIC 00118: Trigger

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__trigger.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXLTE_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples. |
| RFMXLTE_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__trigger__digital__edge.html language=enus -->
## TOPIC 00119: Digital Edge

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__trigger__digital__edge.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_EDGESpecifies the active edge for the trigger. This attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to Digital Edge. RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_SOURCESpecifies the source terminal for the digit

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_EDGE | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to Digital Edge. |
| RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE | Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to Digital Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__trigger__iq__power__edge_1ga3fb820efdd3e9529ac286d83d52fb9be.html language=enus -->
## TOPIC 00120: RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__trigger__iq__power__edge_1ga3fb820efdd3e9529ac286d83d52fb9be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__trigger__iq__power__edge_1ga3fb820efdd3e9529ac286d83d52fb9be.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level Type attribute to Absolute. The device asserts the trigger when the signal exceed

### RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE](group____root__ni_r_fmx_l_t_e__attributes__trigger__iq__power__edge_1ga5e50e107bc2049e7b8121b3753d29e97.html) attribute to **Relative** and in dBm when you set the IQ Power Edge Level Type attribute to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the [RFMXLTE_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_l_t_e__attributes__trigger_1gad02cce8e5be360141b43b576898f6b5b.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145736 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00121: Minimum Quiet Time

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODESpecifies w

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__trigger__minimum__quiet__time_1gad08584dbda4bcc94972c6ede530388b1.html language=enus -->
## TOPIC 00122: RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__trigger__minimum__quiet__time_1gad08584dbda4bcc94972c6ede530388b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__trigger__minimum__quiet__time_1gad08584dbda4bcc94972c6ede530388b1.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. SyntaxRFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONNumeric ValueData TypeAccessApplies To3145740float64Read/WriteN/ARemarks If you set the

### RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

#### Syntax

RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3145740 | float64 | Read/Write | N/A |

#### Remarks

If you set the [RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE](group____root__ni_r_fmx_l_t_e__attributes__trigger__iq__power__edge_1ga68836a801eab118f1b725b388c53b3cf.html) attribute to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__txp.html language=enus -->
## TOPIC 00123: TXP

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__txp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__txp.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingResultsGroup membersNameDescriptionRFMXLTE_ATTR_TXP_ALL_TRACES_ENABLEDEnables the traces to be stored and retrieved after the TXP measurement is performed. RFMXLTE_ATTR_TXP_MEASUREMENT_ENABLEDSpecifies whether to enable the Transmit Power (TXP) measurement. RFMXLTE_ATTR_TXP_MEASUREMEN

### TXP

#### Groups

- Averaging
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXLTE_ATTR_TXP_ALL_TRACES_ENABLED | Enables the traces to be stored and retrieved after the TXP measurement is performed. |
| RFMXLTE_ATTR_TXP_MEASUREMENT_ENABLED | Specifies whether to enable the Transmit Power (TXP) measurement. |
| RFMXLTE_ATTR_TXP_MEASUREMENT_INTERVAL | Specifies the measurement interval. This value is expressed in seconds. |
| RFMXLTE_ATTR_TXP_MEASUREMENT_OFFSET | Specifies the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. |
| RFMXLTE_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism inside TXP measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__attributes__txp_1ga364e505b263bace0e91140caf21a66e5.html language=enus -->
## TOPIC 00124: RFMXLTE_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__attributes__txp_1ga364e505b263bace0e91140caf21a66e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__attributes__txp_1ga364e505b263bace0e91140caf21a66e5.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism inside TXP measurement. SyntaxRFMXLTE_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To3203080int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default si

### RFMXLTE_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism inside TXP measurement.

#### Syntax

RFMXLTE_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3203080 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The number of threads must range from 1 to the number of physical cores. The default value is 1.

The number of threads set used in calculations is not guaranteed. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions_1ga07e4ea26545d5f597677fc560de71715.html language=enus -->
## TOPIC 00125: RFmxLTE_Initialize

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions_1ga07e4ea26545d5f597677fc560de71715.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions_1ga07e4ea26545d5f597677fc560de71715.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxLTE_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSes

### RFmxLTE_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxLTE_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

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
| isNewSession | [out] | int32 * | Returns RFMXLTE_VAL_TRUE if the function created a new session, or RFMXLTE_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html language=enus -->
## TOPIC 00126: RFmxLTE_GetError

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxLTE_GetError(niRFmxInstrHan

### RFmxLTE_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxLTE_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxLTE_GetErrorString](group____root__ni_r_fmx_l_t_e__functions_1ga069a232c01b68a43e6bf92e620a33833.html) function if the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function does not return an error message.

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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced.html language=enus -->
## TOPIC 00127: Advanced

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAnalyze2ListGroup membersNameDescriptionRFmxLTE_AbortMeasurementsStops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxLTE_Initiate function or measurement read functions. Calling this fu

### Advanced

#### Groups

- Analyze2
- List

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxLTE_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error. |
| RFmxLTE_ClearAllNamedResults | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxLTE_ClearNamedResult | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxLTE_ClearNoiseCalibrationDatabase | Clears the noise calibration database used for noise compensation. |
| RFmxLTE_CloneSignalConfiguration | Creates a new instance of a signal by copying all the attribute values from an existing signal instance. |
| RFmxLTE_CreateSignalConfiguration | Creates a new instance of a signal. |
| RFmxLTE_DeleteSignalConfiguration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxLTE_GetAllNamedResultNames | Returns the named result names of the signal that you specify in the Selector String parameter. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced_1gae6007633f7813b2eca6a27b11aafa5cb.html language=enus -->
## TOPIC 00128: RFmxLTE_AbortMeasurements

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced_1gae6007633f7813b2eca6a27b11aafa5cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced_1gae6007633f7813b2eca6a27b11aafa5cb.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxLTE_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is

### RFmxLTE_AbortMeasurements

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxLTE_Initiate](group____root__ni_r_fmx_l_t_e__functions_1ga49982698f31e94727df963b6e8dc3530.html) function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxLTE_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced_1gafbc60fea0f28b4fc0102b3a44eb322e5.html language=enus -->
## TOPIC 00129: RFmxLTE_ClearNoiseCalibrationDatabase

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced_1gafbc60fea0f28b4fc0102b3a44eb322e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced_1gafbc60fea0f28b4fc0102b3a44eb322e5.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the noise calibration database used for noise compensation. Syntaxint32 __stdcall RFmxLTE_ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx sessio

### RFmxLTE_ClearNoiseCalibrationDatabase

Clears the noise calibration database used for noise compensation.

#### Syntax

int32 __stdcall RFmxLTE_ClearNoiseCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2.html language=enus -->
## TOPIC 00130: Analyze2

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxLTE_AnalyzeIQ1WaveformPerforms the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or

### Analyze2

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxLTE_AnalyzeIQ1WaveformSplit | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxLTE_AnalyzeSpectrum1Waveform | Performs the enabled measurements on the spectrum waveform that you specify in Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either Spectral or IQ or Spectral. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1ga16e61c12c32aeb3876719db351314b93.html language=enus -->
## TOPIC 00131: RFmxLTE_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1ga16e61c12c32aeb3876719db351314b93.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1ga16e61c12c32aeb3876719db351314b93.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxLTE_AnalyzeIQ1WaveformSplit

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxLTE_AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqI[], float32 iqQ[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

When using the Analysis-Only mode in RFmxLTE, RFmx ignores RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxLTE_Commit](group____root__ni_r_fmx_l_t_e__functions__utility_1ga907fd4039c4f92314615b22b56613df6.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1ga7522692dfa29d6956ad338cf1aebd59c.html language=enus -->
## TOPIC 00132: RFmxLTE_AnalyzeSpectrum1Waveform

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1ga7522692dfa29d6956ad338cf1aebd59c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1ga7522692dfa29d6956ad338cf1aebd59c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum waveform that you specify in Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function o

### RFmxLTE_AnalyzeSpectrum1Waveform

Performs the enabled measurements on the spectrum waveform that you specify in **Spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **Spectral** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxLTE_AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxLTE_Commit](group____root__ni_r_fmx_l_t_e__functions__utility_1ga907fd4039c4f92314615b22b56613df6.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | [in] | float64 | This parameter specifies the frequency interval between data points in the spectrum. |
| spectrum | [in] | float32[] | This parameter contains the real-value power spectrum. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1gacf9d630efebfc2d914138e4ce6df1bc9.html language=enus -->
## TOPIC 00133: RFmxLTE_AnalyzeIQ1Waveform

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1gacf9d630efebfc2d914138e4ce6df1bc9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced__analyze2_1gacf9d630efebfc2d914138e4ce6df1bc9.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxLTE_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxLTE_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

When using the Analysis-Only mode in RFmxLTE, RFmx ignores RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxLTE_Commit](group____root__ni_r_fmx_l_t_e__functions__utility_1ga907fd4039c4f92314615b22b56613df6.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced__list.html language=enus -->
## TOPIC 00134: List

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced__list.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced__list.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxLTE_BuildListStepStringCreates the list step string. RFmxLTE_BuildListStringCreates the list string. RFmxLTE_CreateListCreates a new list instance. Call the RFmxLTE_CreateListStep function to add steps to the list. Alternatively, you can also specify the num

### List

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_BuildListStepString | Creates the list step string. |
| RFmxLTE_BuildListString | Creates the list string. |
| RFmxLTE_CreateList | Creates a new list instance. Call the RFmxLTE_CreateListStep function to add steps to the list. Alternatively, you can also specify the number of list steps using the RFMXLTE_ATTR_NUMBER_OF_STEPS attribute. |
| RFmxLTE_CreateListStep | Creates a new list step instance in a list. |
| RFmxLTE_DeleteList | Deletes the list instance and all the list steps that you specify in the List Name parameter. When a list step is deleted, all the instances of attributes associated with the list step are also removed. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced__list_1ga5b41608d54a13107a1bcaa1af71a30fb.html language=enus -->
## TOPIC 00135: RFmxLTE_CreateList

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced__list_1ga5b41608d54a13107a1bcaa1af71a30fb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced__list_1ga5b41608d54a13107a1bcaa1af71a30fb.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new list instance. Call the RFmxLTE_CreateListStep function to add steps to the list. Alternatively, you can also specify the number of list steps using the RFMXLTE_ATTR_NUMBER_OF_STEPS attribute. Syntaxint32 __stdcall RFmxLTE_CreateList(niRFmxInstrHandle instrumentHandle, char listName[])

### RFmxLTE_CreateList

Creates a new list instance. Call the [RFmxLTE_CreateListStep](group____root__ni_r_fmx_l_t_e__functions__advanced__list_1ga96dbd2a39653adf567859ee1024c749c.html) function to add steps to the list. Alternatively, you can also specify the number of list steps using the [RFMXLTE_ATTR_NUMBER_OF_STEPS](group____root__ni_r_fmx_l_t_e__attributes__list_1gaafc657ba9d508e2a448ba5ccbf12340a.html) attribute.

#### Syntax

int32 __stdcall RFmxLTE_CreateList(niRFmxInstrHandle instrumentHandle, char listName[])

#### Remarks

**Supported devices:**PXIe-5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| listName | [in] | char[] | This parameter specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix.Example:"list::samplelist1""samplelist1"You can use the RFmxLTE_BuildListString function to build the list name. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__advanced__list_1ga96dbd2a39653adf567859ee1024c749c.html language=enus -->
## TOPIC 00136: RFmxLTE_CreateListStep

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__advanced__list_1ga96dbd2a39653adf567859ee1024c749c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__advanced__list_1ga96dbd2a39653adf567859ee1024c749c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new list step instance in a list. Syntaxint32 __stdcall RFmxLTE_CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *createdStepIndex)RemarksSupported devices:PXIe-5840/5841/5842/5860ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxLTE_CreateListStep

Creates a new list step instance in a list.

#### Syntax

int32 __stdcall RFmxLTE_CreateListStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *createdStepIndex)

#### Remarks

**Supported devices:**PXIe-5840/5841/5842/5860

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the list name. This input accepts the list name with or without the "list::" prefix.The default value is "" (empty string).Example:"list::samplelist1""samplelist1" |
| createdStepIndex | [out] | int32 * | Returns the created list step index. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__build__string_1ga1d88b3f3e773cc73a216afccf63eeb28.html language=enus -->
## TOPIC 00137: RFmxLTE_BuildOffsetString

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__build__string_1ga1d88b3f3e773cc73a216afccf63eeb28.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__build__string_1ga1d88b3f3e773cc73a216afccf63eeb28.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an offset string to use as a selector string with SEM and ACP offset configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxLTE_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionType

### RFmxLTE_BuildOffsetString

Creates an offset string to use as a selector string with SEM and ACP offset configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxLTE_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| offsetNumber | [in] | int32 | This parameter specifies the offset number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__build__string_1gadaf716530254e85eb47b7e47eacdb571.html language=enus -->
## TOPIC 00138: RFmxLTE_BuildCarrierString

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__build__string_1gadaf716530254e85eb47b7e47eacdb571.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__build__string_1gadaf716530254e85eb47b7e47eacdb571.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch attributes and functions. Syntaxint32 __stdcall RFmxLTE_BuildCarrierString(char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirec

### RFmxLTE_BuildCarrierString

Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxLTE_BuildCarrierString(char selectorString[], int32 carrierNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| carrierNumber | [in] | int32 | This parameter specifies the carrier number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration_1ga613c44426ad44ea9e77893926ee56ca9.html language=enus -->
## TOPIC 00139: RFmxLTE_CfgRFAttenuation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration_1ga613c44426ad44ea9e77893926ee56ca9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration_1ga613c44426ad44ea9e77893926ee56ca9.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the nominal attenuation and the RFmx driver setting. Syntaxint32 __stdcall RFmxLTE_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the RF

### RFmxLTE_CfgRFAttenuation

Configures the nominal attenuation and the RFmx driver setting.

#### Syntax

int32 __stdcall RFmxLTE_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgRFAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_rf_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxLTE_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| rfAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver computes the RF attenuation.ValueDescriptionRFMXLTE_VAL_RF_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter.RFMXLTE_VAL_RF_ATTENUATION_AUTO_TRUE (1)Specifies that the RFmx driver computes the RF attenuation automatically. |
| Value | Description |  |  |
| RFMXLTE_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. |  |  |
| RFMXLTE_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that the RFmx driver computes the RF attenuation automatically. |  |  |
| rfAttenuationValue | [in] | float64 | Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain when the rfAttenuationAuto parameter is set to RFMXLTE_VAL_RF_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration_1ga92a8a2fc3020ff46e80d924c6913831d.html language=enus -->
## TOPIC 00140: RFmxLTE_CfgNumberOfComponentCarriers

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration_1ga92a8a2fc3020ff46e80d924c6913831d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration_1ga92a8a2fc3020ff46e80d924c6913831d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of component carriers within a subblock. Syntaxint32 __stdcall RFmxLTE_CfgNumberOfComponentCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfComponentCarriers)RemarksUse "subblock<n>" as the selector string to configure this function.ParametersNa

### RFmxLTE_CfgNumberOfComponentCarriers

Configures the number of component carriers within a subblock.

#### Syntax

int32 __stdcall RFmxLTE_CfgNumberOfComponentCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfComponentCarriers)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| numberOfComponentCarriers | [in] | int32 | This parameter specifies the number of component carriers configured within a subblock. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration_1ga947ea994124b9a15eecb3b36ac88f743.html language=enus -->
## TOPIC 00141: RFmxLTE_CfgTransmitAntennaToAnalyze

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration_1ga947ea994124b9a15eecb3b36ac88f743.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration_1ga947ea994124b9a15eecb3b36ac88f743.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the current physical antenna of the DUT in the MIMO setup being tested. Syntaxint32 __stdcall RFmxLTE_CfgTransmitAntennaToAnalyze(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 transmitAntennaToAnalyze)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstr

### RFmxLTE_CfgTransmitAntennaToAnalyze

Configures the current physical antenna of the DUT in the MIMO setup being tested.

#### Syntax

int32 __stdcall RFmxLTE_CfgTransmitAntennaToAnalyze(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 transmitAntennaToAnalyze)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| transmitAntennaToAnalyze | [in] | int32 | This parameter specifies the physical antenna connected to the analyzer. The default value is 0. Valid values are from 0 to N-1, where N is the number of DUT antennas. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration_1ga9f7a5a9db4daeff10c4cf3a1aed34c6d.html language=enus -->
## TOPIC 00142: RFmxLTE_CfgDownlinkAutoCellIDDetectionEnabled

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration_1ga9f7a5a9db4daeff10c4cf3a1aed34c6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration_1ga9f7a5a9db4daeff10c4cf3a1aed34c6d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the cell ID is configured by the user or auto-detected by the measurement. Syntaxint32 __stdcall RFmxLTE_CfgDownlinkAutoCellIDDetectionEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoCellIdDetectionEnabled)ParametersNameDirectionTypeDescriptioninstrume

### RFmxLTE_CfgDownlinkAutoCellIDDetectionEnabled

Configures whether the cell ID is configured by the user or auto-detected by the measurement.

#### Syntax

int32 __stdcall RFmxLTE_CfgDownlinkAutoCellIDDetectionEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoCellIdDetectionEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| autoCellIdDetectionEnabled | [in] | int32 | This parameter specifies whether to enable autodetection the of cell ID. If signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of the cell ID is not possible. The default value is True.NameValueDescriptionRFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_FALSE0 (0x0)The measurement uses the cell ID you configure.RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_TRUE1 (0x1)The measurement auto detects the cell ID. |
| Name | Value | Description |  |
| RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_FALSE | 0 (0x0) | The measurement uses the cell ID you configure. |  |
| RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_TRUE | 1 (0x1) | The measurement auto detects the cell ID. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration_1gaa599b9b588da3aa4cefb37c781040e17.html language=enus -->
## TOPIC 00143: RFmxLTE_CfgDownlinkTestModel

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration_1gaa599b9b588da3aa4cefb37c781040e17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration_1gaa599b9b588da3aa4cefb37c781040e17.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the EUTRA test model type. Syntaxint32 __stdcall RFmxLTE_CfgDownlinkTestModel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 downlinkTestModel)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.ParametersNameDirectionTyp

### RFmxLTE_CfgDownlinkTestModel

Configures the EUTRA test model type.

#### Syntax

int32 __stdcall RFmxLTE_CfgDownlinkTestModel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 downlinkTestModel)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| downlinkTestModel | [in] | int32 | This parameter specifies the EUTRA test model type when you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to Test Model. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. The default value is TM1.1.NameValueDescriptionRFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_10 (0x0)Specifies an E-UTRA Test Model 1.1.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_21 (0x1)Specifies an E-UTRA Test Model 1.2.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM22 (0x2)Specifies an E-UTRA Test Model 2.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2A3 (0x3)Specifies an E-UTRA Test Model 2a.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_14 (0x4)Specifies an E-UTRA Test Model 3.1.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_25 (0x5)Specifies an E-UTRA Test Model 3.2.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_36 (0x6)Specifies an E-UTRA Test Model 3.3.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1A7 (0x7)Specifies an E-UTRA Test Model 3.1a.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2B8 (0x8)Specifies an E-UTRA Test Model 2b.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1B9 (0x9)Specifies an E-UTRA Test Model 3.1b. |
| Name | Value | Description |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_1 | 0 (0x0) | Specifies an E-UTRA Test Model 1.1. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_2 | 1 (0x1) | Specifies an E-UTRA Test Model 1.2. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2 | 2 (0x2) | Specifies an E-UTRA Test Model 2. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2A | 3 (0x3) | Specifies an E-UTRA Test Model 2a. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1 | 4 (0x4) | Specifies an E-UTRA Test Model 3.1. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_2 | 5 (0x5) | Specifies an E-UTRA Test Model 3.2. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_3 | 6 (0x6) | Specifies an E-UTRA Test Model 3.3. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1A | 7 (0x7) | Specifies an E-UTRA Test Model 3.1a. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2B | 8 (0x8) | Specifies an E-UTRA Test Model 2b. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1B | 9 (0x9) | Specifies an E-UTRA Test Model 3.1b. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration_1gaf86e6ee23ad55b78d057cace79dad38c.html language=enus -->
## TOPIC 00144: RFmxLTE_CfgRF

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration_1gaf86e6ee23ad55b78d057cace79dad38c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration_1gaf86e6ee23ad55b78d057cace79dad38c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF attributes of the signal specified by the selector string. Syntaxint32 __stdcall RFmxLTE_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)ParametersNameDirectionTypeDescriptioninstrumentHan

### RFmxLTE_CfgRF

Configures the RF attributes of the signal specified by the selector string.

#### Syntax

int32 __stdcall RFmxLTE_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the center frequency of the acquired RF signal for a single carrier. The parameter specifies the reference frequency of the subblock for intra-band carrier aggregation. The default value of this parameter is hardware dependent. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__acp_1gaa172aeb13fc0bf6431ba3419022bedf8.html language=enus -->
## TOPIC 00145: RFmxLTE_ACPCfgNumberOfEUTRAOffsets

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__acp_1gaa172aeb13fc0bf6431ba3419022bedf8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__acp_1gaa172aeb13fc0bf6431ba3419022bedf8.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED attribute to True. Syntaxint32 __stdcall RFmxLTE_ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selecto

### RFmxLTE_ACPCfgNumberOfEUTRAOffsets

Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the [RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED](group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html) attribute to **True**.

#### Syntax

int32 __stdcall RFmxLTE_ACPCfgNumberOfEUTRAOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfEUTRAOffsets)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| numberOfEUTRAOffsets | [in] | int32 | This parameter specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled attribute to True.In case of non-contiguous carrier aggregation, the configured value will be used only for the outer offsets and the offset channels in the gap region are defined as per the 3GPP specification. Offset integration bandwidth and offset power reference for the outer E-UTRA offsets are set according to the value of RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION attribute.The default value is 0, when carrier bandwidth is 200 kHz. The default value is 2 for downlink and 1 for uplink, otherwise. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__acp_1gac6ba3daf5a2d92c8860fbf230355cb3f.html language=enus -->
## TOPIC 00146: RFmxLTE_ACPCfgNumberOfGSMOffsets

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__acp_1gac6ba3daf5a2d92c8860fbf230355cb3f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__acp_1gac6ba3daf5a2d92c8860fbf230355cb3f.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of GSM adjacent channels of the subblock, when you set the RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED attribute to True. Syntaxint32 __stdcall RFmxLTE_ACPCfgNumberOfGSMOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfGsmOffsets)Remar

### RFmxLTE_ACPCfgNumberOfGSMOffsets

Configures the number of GSM adjacent channels of the subblock, when you set the [RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED](group____root__ni_r_fmx_l_t_e__attributes__acp__offset_1ga7038eacab2b05ad4f0076f318eca9798.html) attribute to **True**.

#### Syntax

int32 __stdcall RFmxLTE_ACPCfgNumberOfGSMOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfGsmOffsets)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| numberOfGsmOffsets | [in] | int32 | This parameter specifies the number of GSM adjacent channel offsets to be configured when you set the RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH to 200.0 k and when you set the ACP Configurable Number of Offset Enabled attribute to True.The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center.The default value is 1, when you set the CC Bandwidth attribute to is 200.0 k. The default value is 0, otherwise. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__arrays_1ga43373473588fd9e44b45f6b36039fd9f.html language=enus -->
## TOPIC 00147: RFmxLTE_CfgDownlinkTestModelArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__arrays_1ga43373473588fd9e44b45f6b36039fd9f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__arrays_1ga43373473588fd9e44b45f6b36039fd9f.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the EUTRA test model type for each component carrier within the subblock. Syntaxint32 __stdcall RFmxLTE_CfgDownlinkTestModelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 downlinkTestModel[], int32 numberOfElements)ParametersNameDirectionTypeDescription

### RFmxLTE_CfgDownlinkTestModelArray

Configures an array of the EUTRA test model type for each component carrier within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_CfgDownlinkTestModelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 downlinkTestModel[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| downlinkTestModel | [in] | int32[] | This parameter specifies the array of EUTRA test model types when you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to Test Model. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. The default value is TM1.1.NameValueDescriptionRFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_10 (0x0)Specifies an E-UTRA Test Model 1.1.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_21 (0x1)Specifies an E-UTRA Test Model 1.2.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM22 (0x2)Specifies an E-UTRA Test Model 2.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2A3 (0x3)Specifies an E-UTRA Test Model 2a.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_14 (0x4)Specifies an E-UTRA Test Model 3.1.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_25 (0x5)Specifies an E-UTRA Test Model 3.2.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_36 (0x6)Specifies an E-UTRA Test Model 3.3.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1A7 (0x7)Specifies an E-UTRA Test Model 3.1a.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2B8 (0x8)Specifies an E-UTRA Test Model 2b.RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1B9 (0x9)Specifies an E-UTRA Test Model 3.1b. |
| Name | Value | Description |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_1 | 0 (0x0) | Specifies an E-UTRA Test Model 1.1. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_2 | 1 (0x1) | Specifies an E-UTRA Test Model 1.2. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2 | 2 (0x2) | Specifies an E-UTRA Test Model 2. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2A | 3 (0x3) | Specifies an E-UTRA Test Model 2a. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1 | 4 (0x4) | Specifies an E-UTRA Test Model 3.1. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_2 | 5 (0x5) | Specifies an E-UTRA Test Model 3.2. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_3 | 6 (0x6) | Specifies an E-UTRA Test Model 3.3. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1A | 7 (0x7) | Specifies an E-UTRA Test Model 3.1a. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2B | 8 (0x8) | Specifies an E-UTRA Test Model 2b. |  |
| RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1B | 9 (0x9) | Specifies an E-UTRA Test Model 3.1b. |  |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Arrays

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__arrays_1ga7b7ec2efb98689fd32bf90de52cdd4e7.html language=enus -->
## TOPIC 00148: RFmxLTE_CfgComponentCarrierArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__arrays_1ga7b7ec2efb98689fd32bf90de52cdd4e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__arrays_1ga7b7ec2efb98689fd32bf90de52cdd4e7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of bandwidths, carrier offset frequencies, and cell IDs of component carriers. Syntaxint32 __stdcall RFmxLTE_CfgComponentCarrierArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierBandwidth[], float64 componentCarrierFrequency[], int32 cellId[

### RFmxLTE_CfgComponentCarrierArray

Configures an array of bandwidths, carrier offset frequencies, and cell IDs of component carriers.

#### Syntax

int32 __stdcall RFmxLTE_CfgComponentCarrierArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 componentCarrierBandwidth[], float64 componentCarrierFrequency[], int32 cellId[], int32 numberOfElements)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| componentCarrierBandwidth | [in] | float64[] | This parameter specifies the array of channel bandwidths of the signal being measured. The default value is 10 M.Name (Value)Description200.0 k (2e5)Indicates a channel bandwidth of 200 kHz. This value indicates that the received signal is an NB-IoT stand-alone signal.1.4 M (1.4e6)Indicates a channel bandwidth of 1.4 MHz.3.0 M (3e6)Indicates a channel bandwidth of 3 MHz.5.0 M (5e6)Indicates a channel bandwidth of 5 MHz.10.0 M (10e6)Indicates a channel bandwidth of 10 MHz.15.0 M (15e6)Indicates a channel bandwidth of 15 MHz.20.0 M (20e6)Indicates a channel bandwidth of 20 MHz. |
| Name (Value) | Description |  |  |
| 200.0 k (2e5) | Indicates a channel bandwidth of 200 kHz. This value indicates that the received signal is an NB-IoT stand-alone signal. |  |  |
| 1.4 M (1.4e6) | Indicates a channel bandwidth of 1.4 MHz. |  |  |
| 3.0 M (3e6) | Indicates a channel bandwidth of 3 MHz. |  |  |
| 5.0 M (5e6) | Indicates a channel bandwidth of 5 MHz. |  |  |
| 10.0 M (10e6) | Indicates a channel bandwidth of 10 MHz. |  |  |
| 15.0 M (15e6) | Indicates a channel bandwidth of 15 MHz. |  |  |
| 20.0 M (20e6) | Indicates a channel bandwidth of 20 MHz. |  |  |
| componentCarrierFrequency | [in] | float64[] | This parameter specifies the array of offsets of the component carrier from the subblock center frequency that you configure in the RFMXLTE_ATTR_CENTER_FREQUENCY attribute. This parameter is applicable only if you set the RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE attribute to User. The default value is 0. |
| cellId | [in] | int32[] | This parameter specifies the array of the physical layer cell identities. The default value is 0. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Arrays

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga2fb178ebf28c0e89647226afe108abb5.html language=enus -->
## TOPIC 00149: RFmxLTE_CfgPCFICH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga2fb178ebf28c0e89647226afe108abb5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga2fb178ebf28c0e89647226afe108abb5.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the CFI and Power parameters of the physical control format indicator channel (PCFICH). Syntaxint32 __stdcall RFmxLTE_CfgPCFICH(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 cfi, float64 power)RemarksUse "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock

### RFmxLTE_CfgPCFICH

Configures the **CFI** and **Power** parameters of the physical control format indicator channel (PCFICH).

#### Syntax

int32 __stdcall RFmxLTE_CfgPCFICH(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 cfi, float64 power)

#### Remarks

Use "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<<i>l</i>>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0/subframe0""signal::sig1/subblock0/carrier0/subframe0"You can use the RFmxLTE_BuildSubframeString function to build the selector string. |
| cfi | [in] | int32 | This parameter specifies the control format indicator (CFI) carried by PCFICH. CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. The default value is 1. |
| power | [in] | float64 | This parameter specifies the power of the PCFICH relative to the power of the cell-specific reference signal. This value is expressed in dB. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga3e700f8dfb9c7b84b54982e85910beb2.html language=enus -->
## TOPIC 00150: RFmxLTE_CfgDownlinkSynchronizationSignal

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga3e700f8dfb9c7b84b54982e85910beb2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga3e700f8dfb9c7b84b54982e85910beb2.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization signal power relative to the cell-specific reference signal. Syntaxint32 __stdcall RFmxLTE_CfgDownlinkSynchronizationSignal(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 pssPower, float64 sssPower)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>"

### RFmxLTE_CfgDownlinkSynchronizationSignal

Configures the synchronization signal power relative to the cell-specific reference signal.

#### Syntax

int32 __stdcall RFmxLTE_CfgDownlinkSynchronizationSignal(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 pssPower, float64 sssPower)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| pssPower | [in] | float64 | This parameter specifies the power of the primary synchronization signal (PSS) relative to the power of the cell-specific reference signal. This value is expressed in dB. The default value is 0. |
| sssPower | [in] | float64 | This parameter specifies the power of the secondary synchronization signal (SSS) relative to the power of the cell-specific reference signal. This value is expressed in dB. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga44148e1586998938d560b13a068b780f.html language=enus -->
## TOPIC 00151: RFmxLTE_CfgNumberOfPDSCHChannels

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga44148e1586998938d560b13a068b780f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga44148e1586998938d560b13a068b780f.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of different physical downlink shared channel (PDSCH) allocations in a subframe. Syntaxint32 __stdcall RFmxLTE_CfgNumberOfPDSCHChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfPDSCHChannels)RemarksUse "subframe<<i>l</i>>" or "carrier<k>" or "sub

### RFmxLTE_CfgNumberOfPDSCHChannels

Configures the number of different physical downlink shared channel (PDSCH) allocations in a subframe.

#### Syntax

int32 __stdcall RFmxLTE_CfgNumberOfPDSCHChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfPDSCHChannels)

#### Remarks

Use "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<<i>l</i>>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0/subframe0""signal::sig1/subblock0/carrier0/subframe0"You can use the RFmxLTE_BuildSubframeString function to build the selector string. |
| numberOfPDSCHChannels | [in] | int32 | This parameter specifies the number of PDSCH allocations in a subframe. The default value is 1. Valid values are 0 to 100, inclusive. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga468edf35459b9f3fb1bd547408a5268b.html language=enus -->
## TOPIC 00152: RFmxLTE_CfgPDSCH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga468edf35459b9f3fb1bd547408a5268b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga468edf35459b9f3fb1bd547408a5268b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the codeword0 modulation type, resource block, and relative power of a physical downlink shared channel (PDSCH) allocation. Syntaxint32 __stdcall RFmxLTE_CfgPDSCH(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 cw0ModulationType, char resourceBlockAllocation[], float64 po

### RFmxLTE_CfgPDSCH

Configures the codeword0 modulation type, resource block, and relative power of a physical downlink shared channel (PDSCH) allocation.

#### Syntax

int32 __stdcall RFmxLTE_CfgPDSCH(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 cw0ModulationType, char resourceBlockAllocation[], float64 power)

#### Remarks

Use "PDSCH<<i>m</i>>" or "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<<i>l</i>>/PDSCH<<i>m</i>>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number, carrier number, subframe number, and PDSCH number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0/subframe0/PDSCH0""signal::sig1/subblock0/carrier0/subframe0/PDSCH0"You can use the RFmxLTE_BuildPDSCHString function to build the selector string. |
| cw0ModulationType | [in] | int32 | This parameter specifies the modulation type of Codeword0 PDSCH allocation. The default value is QPSK.NameValueDescriptionRFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QPSK0 (0x0)Specifies a QPSK modulation scheme.RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM161 (0x1)Specifies a 16-QAM modulation scheme.RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM642 (0x2)Specifies a 64-QAM modulation scheme.RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM2563 (0x3)Specifies a 256-QAM modulation scheme.RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM10244 (0x4)Specifies a 1024-QAM modulation scheme. |
| Name | Value | Description |  |
| RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QPSK | 0 (0x0) | Specifies a QPSK modulation scheme. |  |
| RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM16 | 1 (0x1) | Specifies a 16-QAM modulation scheme. |  |
| RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM64 | 2 (0x2) | Specifies a 64-QAM modulation scheme. |  |
| RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM256 | 3 (0x3) | Specifies a 256-QAM modulation scheme. |  |
| RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM1024 | 4 (0x4) | Specifies a 1024-QAM modulation scheme. |  |
| resourceBlockAllocation | [in] | char[] | This parameter specifies the resource blocks of the PDSCH allocation. The default value is 0 - 49.The following string formats are supported for this parameter:1) RBStartValue1-RBStopValue1,RBStartValue2-RBStopValue22) RB1,RB23) RBStartValue1-RBStopValue1, RB1,RBStartValue2-RBStopValue2,RB2For example: If the RB allocation is 0-5,7,8,10-15, the RB allocation string specifies contiguous resource blocks from 0 to 5, resource block 7, resource block 8, and contiguous resource blocks from 10 to 15. |
| power | [in] | float64 | This parameter specifies the PDSCH power level (ρa) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the RFMXLTE_ATTR_DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO attribute to calculate ρb. Refer to section 3.3 of the 3GPP 36.521 specifications for more information about ρa. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga50f310bd263ffe4a9b6c8e1893b2e903.html language=enus -->
## TOPIC 00153: RFmxLTE_CfgCellSpecificRatio

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga50f310bd263ffe4a9b6c8e1893b2e903.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga50f310bd263ffe4a9b6c8e1893b2e903.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the cell specific ratio parameter. Syntaxint32 __stdcall RFmxLTE_CfgCellSpecificRatio(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 cellSpecificRatio)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.ParametersNameDire

### RFmxLTE_CfgCellSpecificRatio

Configures the **cell specific ratio** parameter.

#### Syntax

int32 __stdcall RFmxLTE_CfgCellSpecificRatio(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 cellSpecificRatio)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| cellSpecificRatio | [in] | int32 | This parameter specifies the ratio ρb/ρa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 Specifications. This parameter determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. The default value is P_B=0.NameValueDescriptionRFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B00 (0x0)Specifies a ratio of 1 for one antenna port and 5/4 for two or four antenna ports.RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B11 (0x1)Specifies a ratio of 4/5 for one antenna port and 1 for two or four antenna ports.RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B22 (0x2)Specifies a ratio of 3/5 for one antenna port and 3/4 for two or four antenna ports.RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B33 (0x3)Specifies a ratio of 2/5 for one antenna port and 1/2 for two or four antenna ports. |
| Name | Value | Description |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B0 | 0 (0x0) | Specifies a ratio of 1 for one antenna port and 5/4 for two or four antenna ports. |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B1 | 1 (0x1) | Specifies a ratio of 4/5 for one antenna port and 1 for two or four antenna ports. |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B2 | 2 (0x2) | Specifies a ratio of 3/5 for one antenna port and 3/4 for two or four antenna ports. |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B3 | 3 (0x3) | Specifies a ratio of 2/5 for one antenna port and 1/2 for two or four antenna ports. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga67f015fd60199062dc9c11e3e3e75bbd.html language=enus -->
## TOPIC 00154: RFmxLTE_CfgPHICH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga67f015fd60199062dc9c11e3e3e75bbd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga67f015fd60199062dc9c11e3e3e75bbd.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Resource, Duration, and Power parameters of the physical hybrid-ARQ indicator channel (PHICH). Syntaxint32 __stdcall RFmxLTE_CfgPHICH(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 resource, int32 duration, float64 power)RemarksUse "subframe<<i>l</i>>" or "carrier<k>

### RFmxLTE_CfgPHICH

Configures the **Resource**, **Duration**, and **Power** parameters of the physical hybrid-ARQ indicator channel (PHICH).

#### Syntax

int32 __stdcall RFmxLTE_CfgPHICH(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 resource, int32 duration, float64 power)

#### Remarks

Use "subframe<<i>l</i>>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<<i>l</i>>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used.Example:"subblock0/carrier0/subframe0""signal::sig1/subblock0/carrier0/subframe0"You can use the RFmxLTE_BuildSubframeString function to build the selector string. |
| resource | [in] | int32 | This parameter specifies the PHICH resource value. This value is expressed in Ng. This parameter is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. The default value is 1/6.NameValueDescriptionRFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE_SIXTH0 (0x0)Specifies the PHICH resource value is 1/6.RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_HALF1 (0x1)Specifies the PHICH resource value is 1/2.RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE2 (0x2)Specifies the PHICH resource value is 1.RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_TWO3 (0x3)Specifies the PHICH resource value is 2. |
| Name | Value | Description |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE_SIXTH | 0 (0x0) | Specifies the PHICH resource value is 1/6. |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_HALF | 1 (0x1) | Specifies the PHICH resource value is 1/2. |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE | 2 (0x2) | Specifies the PHICH resource value is 1. |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_TWO | 3 (0x3) | Specifies the PHICH resource value is 2. |  |
| duration | [in] | int32 | This parameter specifies the PHICH duration. The default value is Normal.NameValueDescriptionRFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_DURATION_NORMAL0 (0x0)Orthogonal sequences of length 4 is used to extract PHICH. |
| Name | Value | Description |  |
| RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_DURATION_NORMAL | 0 (0x0) | Orthogonal sequences of length 4 is used to extract PHICH. |  |
| power | [in] | float64 | This parameter specifies the power of all BPSK symbols in a PHICH sequence. This value is expressed in dB. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga67f11fa66a524d90d7827aa40a5c37b1.html language=enus -->
## TOPIC 00155: RFmxLTE_CfgPDCCH

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga67f11fa66a524d90d7827aa40a5c37b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga67f11fa66a524d90d7827aa40a5c37b1.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the physical downlink control channel (PDCCH) power relative to the cell-specific reference signal. Syntaxint32 __stdcall RFmxLTE_CfgPDCCH(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 pdcchPower)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" as the selector stri

### RFmxLTE_CfgPDCCH

Configures the physical downlink control channel (PDCCH) power relative to the cell-specific reference signal.

#### Syntax

int32 __stdcall RFmxLTE_CfgPDCCH(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 pdcchPower)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| pdcchPower | [in] | float64 | This parameter specifies the power of the PDCCH relative to the power of the cell-specific reference signal. This value is expressed in dB. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga69c86c04996a040d6ffa5cca45dd40a5.html language=enus -->
## TOPIC 00156: RFmxLTE_CfgDownlinkAutoChannelDetection

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga69c86c04996a040d6ffa5cca45dd40a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__downlink_1ga69c86c04996a040d6ffa5cca45dd40a5.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the values of physical downlink shared channel (PDSCH) parameters, control channel signal powers, and physical control format indicator channel (PCFICH) CFI are configured by a user or auto-detected by the measurement. The measurement ignores this function, when you set the RFMXLT

### RFmxLTE_CfgDownlinkAutoChannelDetection

Configures whether the values of physical downlink shared channel (PDSCH) parameters, control channel signal powers, and physical control format indicator channel (PCFICH) CFI are configured by a user or auto-detected by the measurement. The measurement ignores this function, when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink**.

#### Syntax

int32 __stdcall RFmxLTE_CfgDownlinkAutoChannelDetection(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoPDSCHChannelDetectionEnabled, int32 autoControlChannelPowerDetectionEnabled, int32 autoPcfichcfiDetectionEnabled, int32 reserved)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| autoPDSCHChannelDetectionEnabled | [in] | int32 | This parameter specifies whether the values of the RFMXLTE_ATTR_PDSCH_RESOURCE_BLOCK_ALLOCATION attribute, the corresponding RFMXLTE_ATTR_PDSCH_CW0_MODULATION_TYPE attribute, and the RFMXLTE_ATTR_PDSCH_POWER attribute are auto-detected by the measurement or user-specified.This parameter is not valid, when you set the RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE attribute to Test Model.NameValueDescriptionRFMXLTE_VAL_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED_FALSE0 (0x0)The measurement uses the values of the PDSCH RB Allocation attribute, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power attribute that you specify.RFMXLTE_VAL_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED_TRUE1 (0x1)The measurement uses the values of the PDSCH RB Allocation attribute, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power attribute that are auto-detected. |
| Name | Value | Description |  |
| RFMXLTE_VAL_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED_FALSE | 0 (0x0) | The measurement uses the values of the PDSCH RB Allocation attribute, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power attribute that you specify. |  |
| RFMXLTE_VAL_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED_TRUE | 1 (0x1) | The measurement uses the values of the PDSCH RB Allocation attribute, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power attribute that are auto-detected. |  |
| autoControlChannelPowerDetectionEnabled | [in] | int32 | This parameter specifies whether the value of RFMXLTE_ATTR_PSS_POWER, RFMXLTE_ATTR_SSS_POWER, RFMXLTE_ATTR_PBCH_POWER, RFMXLTE_ATTR_PDCCH_POWER, and RFMXLTE_ATTR_PCFICH_POWER attributes are auto-detected by the measurement or user-specified. Currently, auto-detection of RFMXLTE_ATTR_PHICH_POWER attribute is not supported.This parameter is not valid, when you set the DL Ch Configuration Mode attribute to Test Model.NameValueDescriptionRFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_FALSE0 (0x0)The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, PHICH Power, and PCFICH Power attributes that you specify are used for the measurement.RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_TRUE1 (0x1)The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, and PCFICH Power attributes are auto-detected and used for the measurement. |
| Name | Value | Description |  |
| RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_FALSE | 0 (0x0) | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, PHICH Power, and PCFICH Power attributes that you specify are used for the measurement. |  |
| RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_TRUE | 1 (0x1) | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, and PCFICH Power attributes are auto-detected and used for the measurement. |  |
| autoPcfichcfiDetectionEnabled | [in] | int32 | This parameter specifies whether the value of RFMXLTE_ATTR_PCFICH_CFI attribute is auto-detected by the measurement or user-specified.This parameter is not valid, when you set the DL Ch Configuration Mode attribute to Test Model.NameValueDescriptionRFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_FALSE0 (0x0)The value of PCFICH CFI attribute used for the measurement is specified by you.RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_TRUE1 (0x1)The value of PCFICH CFI attribute used for the measurement is auto-detected. This value is obtained by decoding the PCFICH channel. |
| Name | Value | Description |  |
| RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_FALSE | 0 (0x0) | The value of PCFICH CFI attribute used for the measurement is specified by you. |  |
| RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_TRUE | 1 (0x1) | The value of PCFICH CFI attribute used for the measurement is auto-detected. This value is obtained by decoding the PCFICH channel. |  |
| reserved | [in] | int32 | This parameter is not supported in this release and it is reserved for future enhancements. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Downlink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__sidelink.html language=enus -->
## TOPIC 00157: Sidelink

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__sidelink.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__sidelink.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxLTE_CfgPSSCHModulationTypeConfigures the modulation scheme used in the physical sidelink shared channel (PSSCH) of the signal being measured. RFmxLTE_CfgPSSCHResourceBlocksConfigures the start and number of resource blocks allocated for the physical sidelink

### Sidelink

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_CfgPSSCHModulationType | Configures the modulation scheme used in the physical sidelink shared channel (PSSCH) of the signal being measured. |
| RFmxLTE_CfgPSSCHResourceBlocks | Configures the start and number of resource blocks allocated for the physical sidelink shared channel (PSSCH) allocation. |

#### Attachments

None

Parent topic:

Channelconfig

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__sidelink_1ga5694187f66ce7525285c232e0d77cdb1.html language=enus -->
## TOPIC 00158: RFmxLTE_CfgPSSCHResourceBlocks

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__sidelink_1ga5694187f66ce7525285c232e0d77cdb1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__channelconfig__sidelink_1ga5694187f66ce7525285c232e0d77cdb1.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and number of resource blocks allocated for the physical sidelink shared channel (PSSCH) allocation. Syntaxint32 __stdcall RFmxLTE_CfgPSSCHResourceBlocks(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 resourceBlockOffset, int32 numberOfResourceBlocks)RemarksUse

### RFmxLTE_CfgPSSCHResourceBlocks

Configures the start and number of resource blocks allocated for the physical sidelink shared channel (PSSCH) allocation.

#### Syntax

int32 __stdcall RFmxLTE_CfgPSSCHResourceBlocks(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 resourceBlockOffset, int32 numberOfResourceBlocks)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| resourceBlockOffset | [in] | int32 | This parameter specifies the starting resource block number of the PSSCH allocation. The default value is 0. |
| numberOfResourceBlocks | [in] | int32 | This parameter specifies the number of consecutive resource blocks in the PSSCH allocation. The default value is -1. If you set this parameter to -1, all available resource blocks for the specified bandwidth are configured. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Sidelink

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__frequency_1gabe3e8a1b5a202f43599917bfc59c1879.html language=enus -->
## TOPIC 00159: RFmxLTE_CfgFrequencyEARFCN

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__frequency_1gabe3e8a1b5a202f43599917bfc59c1879.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__frequency_1gabe3e8a1b5a202f43599917bfc59c1879.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency. Syntaxint32 __stdcall RFmxLTE_CfgFrequencyEARFCN(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection,

### RFmxLTE_CfgFrequencyEARFCN

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency.

#### Syntax

int32 __stdcall RFmxLTE_CfgFrequencyEARFCN(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 band, int32 earfcn)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| linkDirection | [in] | int32 | This parameter specifies the link direction of the received signal. The default value is Uplink.NameValueDescriptionRFMXLTE_VAL_LINK_DIRECTION_DOWNLINK0 (0x0)The measurement uses 3GPP LTE downlink specification to measure the received signal.RFMXLTE_VAL_LINK_DIRECTION_UPLINK1 (0x1)The measurement uses 3GPP LTE uplink specification to measure the received signal.RFMXLTE_VAL_LINK_DIRECTION_SIDELINK2 (0x2)The measurement uses 3GPP LTE sidelink specifications to measure the received signal. |
| Name | Value | Description |  |
| RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK | 0 (0x0) | The measurement uses 3GPP LTE downlink specification to measure the received signal. |  |
| RFMXLTE_VAL_LINK_DIRECTION_UPLINK | 1 (0x1) | The measurement uses 3GPP LTE uplink specification to measure the received signal. |  |
| RFMXLTE_VAL_LINK_DIRECTION_SIDELINK | 2 (0x2) | The measurement uses 3GPP LTE sidelink specifications to measure the received signal. |  |
| band | [in] | int32 | This parameter specifies the E-UTRA operating frequency band of a subblock as defined in section 5.2 of the 3GPP TS 36.521 specification. Valid values are from 1 to 256, inclusive. The default value is 1. |
| earfcn | [in] | int32 | This parameter specifies the evolved universal terrestrial radio access (E-UTRA) absolute radio frequency channel number. The default value is 18100. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1ga6cedac397d45d9d309590c7a61288090.html language=enus -->
## TOPIC 00160: RFmxLTE_ModAccCfgFFTWindowPosition

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1ga6cedac397d45d9d309590c7a61288090.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1ga6cedac397d45d9d309590c7a61288090.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the FFT window position used for an EVM calculation. Syntaxint32 __stdcall RFmxLTE_ModAccCfgFFTWindowPosition(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindowType, float64 fftWindowOffset, float64 fftWindowLength)RemarksRefer to the LTE Modulation Accuracy topic

### RFmxLTE_ModAccCfgFFTWindowPosition

Configures the FFT window position used for an EVM calculation.

#### Syntax

int32 __stdcall RFmxLTE_ModAccCfgFFTWindowPosition(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindowType, float64 fftWindowOffset, float64 fftWindowLength)

#### Remarks

Refer to the [LTE Modulation Accuracy](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-modulation-accuracy.html) topic for more information about FFT window position.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| fftWindowType | [in] | int32 | This parameter specifies the FFT window type used for an EVM calculation. The default value is Custom.NameValueDescriptionRFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP0 (0x0)The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The FFT window positions are specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. Refer to the Annexe E.3.2 of 3GPP TS 36.521 specification for more information on the FFT window.RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM1 (0x1)Only one FFT window position is used for the EVM calculation. FFT window position is specified by RFMXLTE_ATTR_MODACC_FFT_WINDOW_OFFSET attribute. |
| Name | Value | Description |  |
| RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP | 0 (0x0) | The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The FFT window positions are specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. Refer to the Annexe E.3.2 of 3GPP TS 36.521 specification for more information on the FFT window. |  |
| RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM | 1 (0x1) | Only one FFT window position is used for the EVM calculation. FFT window position is specified by RFMXLTE_ATTR_MODACC_FFT_WINDOW_OFFSET attribute. |  |
| fftWindowOffset | [in] | float64 | This parameter specifies the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this parameter to 0, the EVM window starts from the end of cyclic prefix. If you set this parameter to 100, the EVM window starts from the beginning of cyclic prefix.The default value is 50. Valid values are 0 to 100, inclusive. |
| fftWindowLength | [in] | float64 | This parameter specifies the FFT window length. This value is expressed in a percentage of the cyclic prefix length. This parameter is used when you set the ModAcc FFT Window Type parameter to 3GPP, where you need to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2.The default value is -1. Valid values are -1 to 100, inclusive. When this attribute is set to -1, the RFmx populates the FFT Window Length based on carrier bandwidth automatically, as given in the3GPP 36.104 specification, Annexe E.5.1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1ga7e3faa317294294e3353910c78b555b8.html language=enus -->
## TOPIC 00161: RFmxLTE_ModAccCfgCommonClockSourceEnabled

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1ga7e3faa317294294e3353910c78b555b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1ga7e3faa317294294e3353910c78b555b8.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and specifies whether same Reference Clock is used for local oscillator and D/A converter. Syntaxint32 __stdcall RFmxLTE_ModAccCfgCommonClockSourceEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 commonClockSourceEnabled)RemarksThe modacc measur

### RFmxLTE_ModAccCfgCommonClockSourceEnabled

Configures the Reference Clock and specifies whether same Reference Clock is used for local oscillator and D/A converter.

#### Syntax

int32 __stdcall RFmxLTE_ModAccCfgCommonClockSourceEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 commonClockSourceEnabled)

#### Remarks

The modacc measurement ignores this function, when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Downlink**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| commonClockSourceEnabled | [in] | int32 | This parameter specifies whether the same Reference Clock is used for the local oscillator and the D/A converter. When the same Reference Clock is used, the carrier frequency offset is proportional to the Sample Clock error. The default value is True.NameValueDescriptionRFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE0 (0x0)The Sample Clock error is estimated independently.RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE1 (0x1)The Sample Clock error is estimated from carrier frequency offset. |
| Name | Value | Description |  |
| RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE | 0 (0x0) | The Sample Clock error is estimated independently. |  |
| RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE | 1 (0x1) | The Sample Clock error is estimated from carrier frequency offset. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gac10bf6ffb7d86607b64749e8810ec93d.html language=enus -->
## TOPIC 00162: RFmxLTE_ModAccCfgInBandEmissionMaskType

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gac10bf6ffb7d86607b64749e8810ec93d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gac10bf6ffb7d86607b64749e8810ec93d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the In-Band Emission Mask Type parameter to be used. Syntaxint32 __stdcall RFmxLTE_ModAccCfgInBandEmissionMaskType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 inBandEmissionMaskType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parame

### RFmxLTE_ModAccCfgInBandEmissionMaskType

Configures the **In-Band Emission Mask Type** parameter to be used.

#### Syntax

int32 __stdcall RFmxLTE_ModAccCfgInBandEmissionMaskType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 inBandEmissionMaskType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| inBandEmissionMaskType | [in] | int32 | This parameter specifies the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results.Refer to section 6.5.2.3.5 of the 3GPP 36.521-1 specification for more information.The default value is Release 8-10 for bandwidths other than 200 KHz and RFMXLTE_ATTR_LINK_DIRECTION is False. It is Release 11 Onwards, otherwise.NameValueDescriptionRFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_8_100 (0x0)Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification.RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS1 (0x1)Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |
| Name | Value | Description |  |
| RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_8_10 | 0 (0x0) | Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification. |  |
| RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS | 1 (0x1) | Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gac3e95aadc0e122afa2a8c188f3914791.html language=enus -->
## TOPIC 00163: RFmxLTE_ModAccCfgAveraging

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gac3e95aadc0e122afa2a8c188f3914791.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gac3e95aadc0e122afa2a8c188f3914791.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ModAcc measurement. Syntaxint32 __stdcall RFmxLTE_ModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifie

### RFmxLTE_ModAccCfgAveraging

Configures averaging for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxLTE_ModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE1 (0x1)The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the RFMXLTE_ATTR_MODACC_AVERAGING_COUNT attribute. |
| Name | Value | Description |  |
| RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the RFMXLTE_ATTR_MODACC_AVERAGING_COUNT attribute. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gadc25f627b619b7420a8bef7247d51856.html language=enus -->
## TOPIC 00164: RFmxLTE_ModAccCfgFFTWindowOffset

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gadc25f627b619b7420a8bef7247d51856.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__modacc_1gadc25f627b619b7420a8bef7247d51856.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the position of the FFT window that is used to calculate the EVM. Syntaxint32 __stdcall RFmxLTE_ModAccCfgFFTWindowOffset(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 fftWindowOffset)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxLTE_ModAccCfgFFTWindowOffset

Configures the position of the FFT window that is used to calculate the EVM.

#### Syntax

int32 __stdcall RFmxLTE_ModAccCfgFFTWindowOffset(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 fftWindowOffset)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| fftWindowOffset | [in] | float64 | This parameter specifies the position of the FFT window that is used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this parameter to 0, the EVM window starts from the end of cyclic prefix. If you set this parameter to 100, the EVM window starts from the beginning of cyclic prefix. The default value is 50. Valid values are 0 to 100, inclusive. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__nb__iot_1ga7488a70a6e7ffb154a58f3a968d9b4d6.html language=enus -->
## TOPIC 00165: RFmxLTE_CfgNPUSCHStartingSlot

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__nb__iot_1ga7488a70a6e7ffb154a58f3a968d9b4d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__nb__iot_1ga7488a70a6e7ffb154a58f3a968d9b4d6.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the starting slot of the NPUSCH burst. Syntaxint32 __stdcall RFmxLTE_CfgNPUSCHStartingSlot(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 startingSlot)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.ParametersNameDire

### RFmxLTE_CfgNPUSCHStartingSlot

Configures the starting slot of the NPUSCH burst.

#### Syntax

int32 __stdcall RFmxLTE_CfgNPUSCHStartingSlot(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 startingSlot)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| startingSlot | [in] | int32 | This parameter specifies the starting slot number of the NPUSCH burst. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Nb Iot

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__nb__iot_1gae4f70cd7f0a1a08329d7453418fba855.html language=enus -->
## TOPIC 00166: RFmxLTE_CfgNBIoTComponentCarrier

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__nb__iot_1gae4f70cd7f0a1a08329d7453418fba855.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__nb__iot_1gae4f70cd7f0a1a08329d7453418fba855.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Ncell ID and Uplink Subcarrier Spacing parameters for the NB-IoT signal. Syntaxint32 __stdcall RFmxLTE_CfgNBIoTComponentCarrier(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 nCellId, int32 uplinkSubcarrierSpacing)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" a

### RFmxLTE_CfgNBIoTComponentCarrier

Configures the Ncell ID and Uplink Subcarrier Spacing parameters for the NB-IoT signal.

#### Syntax

int32 __stdcall RFmxLTE_CfgNBIoTComponentCarrier(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 nCellId, int32 uplinkSubcarrierSpacing)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| nCellId | [in] | int32 | This parameter specifies the narrowband physical layer cell identity. The default value is 0. Valid values are 0 to 503, inclusive. |
| uplinkSubcarrierSpacing | [in] | int32 | This parameter specifies the subcarrier bandwidth of an NB-IoT signal. This parameter specifies the spacing between adjacent subcarriers. The default value is 15 kHz.NameValueDescriptionRFMXLTE_VAL_NB_IOT_UPLINK_SUBCARRIER_SPACING_15KHZ0 (0x0)The subcarrier spacing is 15 kHz.RFMXLTE_VAL_NB_IOT_UPLINK_SUBCARRIER_SPACING_3_75KHZ1 (0x1)The subcarrier spacing is 3.75 kHz. |
| Name | Value | Description |  |
| RFMXLTE_VAL_NB_IOT_UPLINK_SUBCARRIER_SPACING_15KHZ | 0 (0x0) | The subcarrier spacing is 15 kHz. |  |
| RFMXLTE_VAL_NB_IOT_UPLINK_SUBCARRIER_SPACING_3_75KHZ | 1 (0x1) | The subcarrier spacing is 3.75 kHz. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Nb Iot

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__obw_1ga85446b90c3bcdbf0701e6d50b4313492.html language=enus -->
## TOPIC 00167: RFmxLTE_OBWCfgSweepTime

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__obw_1ga85446b90c3bcdbf0701e6d50b4313492.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__obw_1ga85446b90c3bcdbf0701e6d50b4313492.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxLTE_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refn

### RFmxLTE_OBWCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxLTE_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.NameValueDescriptionRFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXLTE_ATTR_OBW_SWEEP_TIME_INTERVAL attribute.RFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement uses a sweep time of 1 ms. |
| Name | Value | Description |  |
| RFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXLTE_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |  |
| RFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time of 1 ms. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__obw_1gabda2669db7e76b5e868d581d46a26190.html language=enus -->
## TOPIC 00168: RFmxLTE_OBWCfgRBWFilter

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__obw_1gabda2669db7e76b5e868d581d46a26190.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__obw_1gabda2669db7e76b5e868d581d46a26190.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxLTE_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session ref

### RFmxLTE_OBWCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxLTE_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.NameValueDescriptionRFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXLTE_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute.RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE1 (0x1)The measurement computes the RBW. |
| Name | Value | Description |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXLTE_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | The measurement computes the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the resolution bandwidth (RBW) filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is performed.RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)An RBW filter with a Gaussian response is applied.RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FLAT2 (0x2)An RBW filter with a flat response is applied. |
| Name | Value | Description |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__pvt.html language=enus -->
## TOPIC 00169: PVT

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__pvt.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxLTE_PVTCfgAveragingConfigures averaging for the power versus time (PVT) measurement. RFmxLTE_PVTCfgMeasurementMethodConfigures the method for performing the power versus time (PVT) measurement. RFmxLTE_PVTCfgOFFPowerExclusionPeriodsConfigures the OFF power e

### PVT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_PVTCfgAveraging | Configures averaging for the power versus time (PVT) measurement. |
| RFmxLTE_PVTCfgMeasurementMethod | Configures the method for performing the power versus time (PVT) measurement. |
| RFmxLTE_PVTCfgOFFPowerExclusionPeriods | Configures the OFF power exclusion periods for the power versus time (PVT) measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga172787f9eec5050a5eb33797124a58c7.html language=enus -->
## TOPIC 00170: RFmxLTE_PVTCfgOFFPowerExclusionPeriods

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga172787f9eec5050a5eb33797124a58c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga172787f9eec5050a5eb33797124a58c7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the OFF power exclusion periods for the power versus time (PVT) measurement. Syntaxint32 __stdcall RFmxLTE_PVTCfgOFFPowerExclusionPeriods(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offPowerExclusionBefore, float64 offPowerExclusionAfter)RemarksRefer to the LTE PVT

### RFmxLTE_PVTCfgOFFPowerExclusionPeriods

Configures the OFF power exclusion periods for the power versus time (PVT) measurement.

#### Syntax

int32 __stdcall RFmxLTE_PVTCfgOFFPowerExclusionPeriods(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offPowerExclusionBefore, float64 offPowerExclusionAfter)

#### Remarks

Refer to the [LTE PVT (Power Vs Time) Measurement](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-power-vs-time.html) topic for more information about OFF power exclusion periods.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| offPowerExclusionBefore | [in] | float64 | This parameter specifies the time excluded from the OFF region before the burst. This value is expressed in seconds. The default value is 0. |
| offPowerExclusionAfter | [in] | float64 | This parameter specifies the time excluded from the OFF region after the burst. This value is expressed in seconds. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga36219ff303345fdac79101fe3d1ba0fd.html language=enus -->
## TOPIC 00171: RFmxLTE_PVTCfgAveraging

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga36219ff303345fdac79101fe3d1ba0fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga36219ff303345fdac79101fe3d1ba0fd.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the power versus time (PVT) measurement. Syntaxint32 __stdcall RFmxLTE_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFm

### RFmxLTE_PVTCfgAveraging

Configures averaging for the power versus time (PVT) measurement.

#### Syntax

int32 __stdcall RFmxLTE_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXLTE_VAL_PVT_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXLTE_VAL_PVT_AVERAGING_ENABLED_TRUE1 (0x1)The PVT measurement uses the value of the RFMXLTE_ATTR_PVT_AVERAGING_COUNT attribute as the number of acquisitions over which the PVT measurement is averaged. |
| Name | Value | Description |  |
| RFMXLTE_VAL_PVT_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXLTE_VAL_PVT_AVERAGING_ENABLED_TRUE | 1 (0x1) | The PVT measurement uses the value of the RFMXLTE_ATTR_PVT_AVERAGING_COUNT attribute as the number of acquisitions over which the PVT measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXLTE_VAL_PVT_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXLTE_VAL_PVT_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale. |
| Name | Value | Description |  |
| RFMXLTE_VAL_PVT_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXLTE_VAL_PVT_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga56469568bdcc173a2f4aca2dfd59ff3f.html language=enus -->
## TOPIC 00172: RFmxLTE_PVTCfgMeasurementMethod

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga56469568bdcc173a2f4aca2dfd59ff3f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__pvt_1ga56469568bdcc173a2f4aca2dfd59ff3f.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the power versus time (PVT) measurement. Syntaxint32 __stdcall RFmxLTE_PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)RemarksRefer to the LTE PVT (Power Vs Time) Measurement topic for more information ab

### RFmxLTE_PVTCfgMeasurementMethod

Configures the method for performing the power versus time (PVT) measurement.

#### Syntax

int32 __stdcall RFmxLTE_PVTCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Remarks

Refer to the [LTE PVT (Power Vs Time) Measurement](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-power-vs-time.html) topic for more information about measurement method.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method for performing the PVT measurement. The default value is Normal.NameValueDescriptionRFMXLTE_VAL_PVT_MEASUREMENT_METHOD_NORMAL0 (0x0)The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required.RFMXLTE_VAL_PVT_MEASUREMENT_METHOD_DYNAMIC_RANGE1 (0x1)The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644/5645/5646, PXIe-5840/5841/5842/5860 |
| Name | Value | Description |  |
| RFMXLTE_VAL_PVT_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. |  |
| RFMXLTE_VAL_PVT_MEASUREMENT_METHOD_DYNAMIC_RANGE | 1 (0x1) | The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644/5645/5646, PXIe-5840/5841/5842/5860 |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__sem_1gaeeafec96be5ad337c27d401500451f22.html language=enus -->
## TOPIC 00173: RFmxLTE_SEMCfgDownlinkMask

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__sem_1gaeeafec96be5ad337c27d401500451f22.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__sem_1gaeeafec96be5ad337c27d401500451f22.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Downlink Mask Type, Delta F_max, and Aggregated Maximum Output Power parameters for the SEM measurement in LTE downlink. Syntaxint32 __stdcall RFmxLTE_SEMCfgDownlinkMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 downlinkMaskType, float64 deltaFMaximum, float64 a

### RFmxLTE_SEMCfgDownlinkMask

Configures the **Downlink Mask Type**, **Delta F_max**, and **Aggregated Maximum Output Power** parameters for the SEM measurement in LTE downlink.

#### Syntax

int32 __stdcall RFmxLTE_SEMCfgDownlinkMask(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 downlinkMaskType, float64 deltaFMaximum, float64 aggregatedMaximumPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| downlinkMaskType | [in] | int32 | This parameter specifies the standard-defined spectrum emission mask used in the measurement for the downlink. You must set the mask type to CUSTOM to configure the custom offsets and the masks. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. The default value is eNodeB Category Based. Valid values are 0, 1, and 5.NameValueDescriptionRFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_ENODEB_CATEGORY_BASED0 (0x0)The limits are applied based on RFMXLTE_ATTR_ENODEB_CATEGORY attribute.RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_BAND461 (0x1)The limits are applied based on Band 46 test requirements.RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_CUSTOM5 (0x5)You need to configure the RFMXLTE_ATTR_SEM_NUMBER_OF_OFFSETS, RFMXLTE_ATTR_SEM_OFFSET_START_FREQUENCY, RFMXLTE_ATTR_SEM_OFFSET_STOP_FREQUENCY,RFMXLTE_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START, RFMXLTE_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP, RFMXLTE_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START,RFMXLTE_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP, RFMXLTE_ATTR_SEM_OFFSET_SIDEBAND, RFMXLTE_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH, RFMXLTE_ATTR_SEM_OFFSET_RBW_FILTER_TYPE, and RFMXLTE_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL attributes for each offset. |
| Name | Value | Description |  |
| RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_ENODEB_CATEGORY_BASED | 0 (0x0) | The limits are applied based on RFMXLTE_ATTR_ENODEB_CATEGORY attribute. |  |
| RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_BAND46 | 1 (0x1) | The limits are applied based on Band 46 test requirements. |  |
| RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_CUSTOM | 5 (0x5) | You need to configure the RFMXLTE_ATTR_SEM_NUMBER_OF_OFFSETS, RFMXLTE_ATTR_SEM_OFFSET_START_FREQUENCY, RFMXLTE_ATTR_SEM_OFFSET_STOP_FREQUENCY,RFMXLTE_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START, RFMXLTE_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP, RFMXLTE_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START,RFMXLTE_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP, RFMXLTE_ATTR_SEM_OFFSET_SIDEBAND, RFMXLTE_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH, RFMXLTE_ATTR_SEM_OFFSET_RBW_FILTER_TYPE, and RFMXLTE_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL attributes for each offset. |  |
| deltaFMaximum | [in] | float64 | This parameter specifies the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. The default value is 15 MHz. The minimum value is 9.5 MHz. |
| aggregatedMaximumPower | [in] | float64 | This parameter specifies the aggregated maximum output power of all the transmit antenna connectors. This value is expressed in dBm. The default value is 0. Valid values are within 20, inclusive. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array.html language=enus -->
## TOPIC 00174: Array

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxLTE_SEMCfgComponentCarrierMaximumOutputPowerArrayConfigures the array of maximum output power of the component carrier. RFmxLTE_SEMCfgOffsetAbsoluteLimitArrayConfigures the array of the start limit and the stop limit of the offset segments. RFmxLTE_SEMCfgOff

### Array

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_SEMCfgComponentCarrierMaximumOutputPowerArray | Configures the array of maximum output power of the component carrier. |
| RFmxLTE_SEMCfgOffsetAbsoluteLimitArray | Configures the array of the start limit and the stop limit of the offset segments. |
| RFmxLTE_SEMCfgOffsetBandwidthIntegralArray | Configures the array of the bandwidth integral of the offset segments. |
| RFmxLTE_SEMCfgOffsetFrequencyArray | Configures the arrays of the start and stop frequencies and the sideband of an offset segment. |
| RFmxLTE_SEMCfgOffsetLimitFailMaskArray | Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. |
| RFmxLTE_SEMCfgOffsetRBWFilterArray | Configures the offset RBW and the offset RBW filter type arrays. |
| RFmxLTE_SEMCfgOffsetRelativeLimitArray | Configures the array of start and stop relative limits of the offset segments. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1ga65a74e1b97df9d1c67771adc85c02b16.html language=enus -->
## TOPIC 00175: RFmxLTE_SEMCfgOffsetBandwidthIntegralArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1ga65a74e1b97df9d1c67771adc85c02b16.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1ga65a74e1b97df9d1c67771adc85c02b16.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of the bandwidth integral of the offset segments. Syntaxint32 __stdcall RFmxLTE_SEMCfgOffsetBandwidthIntegralArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetBandwidthIntegral[], int32 numberOfElements)RemarksUse "subblock<n>" as the selector string t

### RFmxLTE_SEMCfgOffsetBandwidthIntegralArray

Configures the array of the bandwidth integral of the offset segments.

#### Syntax

int32 __stdcall RFmxLTE_SEMCfgOffsetBandwidthIntegralArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetBandwidthIntegral[], int32 numberOfElements)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| offsetBandwidthIntegral | [in] | int32[] | This parameter specifies the array of the resolution values of the spectrum to compare with the spectral mask limits as an integer multiple of the RBW. The default value is 1.When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and an RBW. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1ga92256480ac2cc23303f9629d8e47646d.html language=enus -->
## TOPIC 00176: RFmxLTE_SEMCfgOffsetLimitFailMaskArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1ga92256480ac2cc23303f9629d8e47646d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1ga92256480ac2cc23303f9629d8e47646d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. Syntaxint32 __stdcall RFmxLTE_SEMCfgOffsetLimitFailMaskArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask[], int32 numberOfElements)R

### RFmxLTE_SEMCfgOffsetLimitFailMaskArray

Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status.

#### Syntax

int32 __stdcall RFmxLTE_SEMCfgOffsetLimitFailMaskArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 limitFailMask[], int32 numberOfElements)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| limitFailMask | [in] | int32[] | This parameter specifies the array of criterion to determine the measurement fail status. The default value is Absolute.Note When you set the RFMXLTE_ATTR_LINK_DIRECTION attribute to Downlink, all the values of limit fail mask are supported but when you set the Link Direction attribute to Uplink, the measurement internally sets the value of limit fail mask to Absolute.NameValueDescriptionRFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_AND_REL0 (0x0)Specifies the fail in measurement if the power in the segment exceeds both the absolute and relative masks.RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_OR_REL1 (0x1)Specifies the fail in measurement if the power in the segment exceeds either the absolute or relative mask.RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE2 (0x2)Specifies the fail in measurement if the power in the segment exceeds the absolute mask.RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_RELATIVE3 (0x3)Specifies the fail in measurement if the power in the segment exceeds the relative mask. |
| Name | Value | Description |  |
| RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_AND_REL | 0 (0x0) | Specifies the fail in measurement if the power in the segment exceeds both the absolute and relative masks. |  |
| RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_OR_REL | 1 (0x1) | Specifies the fail in measurement if the power in the segment exceeds either the absolute or relative mask. |  |
| RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE | 2 (0x2) | Specifies the fail in measurement if the power in the segment exceeds the absolute mask. |  |
| RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_RELATIVE | 3 (0x3) | Specifies the fail in measurement if the power in the segment exceeds the relative mask. |  |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1gadc165528971a95df4ddb5fee84d2d9eb.html language=enus -->
## TOPIC 00177: RFmxLTE_SEMCfgOffsetRBWFilterArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1gadc165528971a95df4ddb5fee84d2d9eb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1gadc165528971a95df4ddb5fee84d2d9eb.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset RBW and the offset RBW filter type arrays. Syntaxint32 __stdcall RFmxLTE_SEMCfgOffsetRBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW[], int32 offsetRBWFilterType[], int32 numberOfElements)RemarksUse "subblock<n>" as the selector strin

### RFmxLTE_SEMCfgOffsetRBWFilterArray

Configures the offset RBW and the offset RBW filter type arrays.

#### Syntax

int32 __stdcall RFmxLTE_SEMCfgOffsetRBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetRBW[], int32 offsetRBWFilterType[], int32 numberOfElements)

#### Remarks

Use "subblock<n>" as the selector string to configure from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| offsetRBW | [in] | float64[] | This parameter specifies the array of the RBW filter bandwidth values used to sweep the acquired offset segment, when you set the SEM Offset RBW Auto attribute to False. This value is expressed in Hz. The default value is 30000. |
| offsetRBWFilterType | [in] | int32[] | This parameter specifies the array of the shape of a digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is performed.RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)The RBW filter has a Gaussian response.RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT2 (0x2)The RBW filter has a flat response. |
| Name | Value | Description |  |
| RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |  |
| RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |  |
| RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |  |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1gaf20ac8fc005c412e68ec5a479c3f7a74.html language=enus -->
## TOPIC 00178: RFmxLTE_SEMCfgOffsetAbsoluteLimitArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1gaf20ac8fc005c412e68ec5a479c3f7a74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__sem__array_1gaf20ac8fc005c412e68ec5a479c3f7a74.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of the start limit and the stop limit of the offset segments. Syntaxint32 __stdcall RFmxLTE_SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetAbsoluteLimitStart[], float64 offsetAbsoluteLimitStop[], int32 numberOfElements)Rem

### RFmxLTE_SEMCfgOffsetAbsoluteLimitArray

Configures the array of the start limit and the stop limit of the offset segments.

#### Syntax

int32 __stdcall RFmxLTE_SEMCfgOffsetAbsoluteLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetAbsoluteLimitStart[], float64 offsetAbsoluteLimitStop[], int32 numberOfElements)

#### Remarks

Use "subblock<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"subblock0""signal::sig1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| offsetAbsoluteLimitStart | [in] | float64[] | This parameter specifies the array of the absolute power limits corresponding to the beginning of an offset segment. This value is expressed in dBm. The default value is -16.5. |
| offsetAbsoluteLimitStop | [in] | float64[] | This parameter specifies the array of the absolute power limits corresponding to the end of an offset segment. This value is expressed in dBm. The default value is -16.5. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__slotpower_1ga7693d58f414b5fa753616526aaa1fb4c.html language=enus -->
## TOPIC 00179: RFmxLTE_SlotPowerCfgMeasurementInterval

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__slotpower_1ga7693d58f414b5fa753616526aaa1fb4c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__slotpower_1ga7693d58f414b5fa753616526aaa1fb4c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Measurement Offset and Measurement Length parameters of SlotPower measurement. Syntaxint32 __stdcall RFmxLTE_SlotPowerCfgMeasurementInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementOffset, int32 measurementLength)ParametersNameDirectionTypeDescripti

### RFmxLTE_SlotPowerCfgMeasurementInterval

Configures the **Measurement Offset** and **Measurement Length** parameters of SlotPower measurement.

#### Syntax

int32 __stdcall RFmxLTE_SlotPowerCfgMeasurementInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframes. The default value is 0. |
| measurementLength | [in] | int32 | This parameter specifies the number of subframes to be measured. This value is expressed in subframes. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1ga439b378529e8055a7a66c2dbe2194b39.html language=enus -->
## TOPIC 00180: RFmxLTE_CfgDigitalEdgeTrigger

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1ga439b378529e8055a7a66c2dbe2194b39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1ga439b378529e8055a7a66c2dbe2194b39.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxLTE_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableT

### RFmxLTE_CfgDigitalEdgeTrigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxLTE_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital edge trigger. This parameter is used when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to Digital Edge. The default value of this parameter is hardware dependent.Name (Value)DescriptionPFI0 (PFI0)The trigger is received on PFI 0.PFI1 (PFI1)The trigger is received on PFI 1.PXI_Trig0 (PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1 (PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2 (PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3 (PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4 (PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5 (PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6 (PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7 (PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR (PXI_STAR)The trigger is received on the PXI star trigger line.PXIe_DStarB (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line.TimerEvent (TimerEvent)The trigger is received from the Timer Event. |
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
| TimerEvent (TimerEvent) | The trigger is received from the Timer Event. |  |  |
| digitalEdge | [in] | int32 | This parameter specifies the source terminal for the digital edge trigger. This parameter is used when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to Digital Edge. The default value is Rising Edge.NameValueDescriptionRFMXLTE_VAL_DIGITAL_EDGE_RISING_EDGE0 (0x0)The trigger asserts on the rising edge of the signal.RFMXLTE_VAL_DIGITAL_EDGE_FALLING_EDGE1 (0x1)The trigger asserts on the falling edge of the signal. |
| Name | Value | Description |  |
| RFMXLTE_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |  |
| RFMXLTE_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1ga8a6078242cdecf4d9b5a78248011f3a4.html language=enus -->
## TOPIC 00181: RFmxLTE_DisableTrigger

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1ga8a6078242cdecf4d9b5a78248011f3a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1ga8a6078242cdecf4d9b5a78248011f3a4.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxLTE_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrument

### RFmxLTE_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxLTE_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1gade679b5975e1eacbd5d3b6b7e59d49f7.html language=enus -->
## TOPIC 00182: RFmxLTE_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1gade679b5975e1eacbd5d3b6b7e59d49f7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__configuration__trigger_1gade679b5975e1eacbd5d3b6b7e59d49f7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. Syntaxint32 __stdcall RFmxLTE_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPo

### RFmxLTE_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxLTE_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 iqPowerEdgeLevelType, int32 enableTrigger)

#### Remarks

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. This parameter is used only when you set the RFMXLTE_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. The default value of this parameter is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This parameter is used only when you set the Trigger Type attribute to IQ Power Edge. The default value is Rising Slope.NameValueDescriptionRFMXLTE_VAL_IQ_POWER_EDGE_RISING_SLOPE0 (0x0)The trigger asserts when the signal power is rising.RFMXLTE_VAL_IQ_POWER_EDGE_FALLING_SLOPE1 (0x1)The trigger asserts when the signal power is falling. |
| Name | Value | Description |  |
| RFMXLTE_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |  |
| RFMXLTE_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |  |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative, and this value is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. This parameter is used only when you set the Trigger Type attribute to IQ Power Edge. The default value of this parameter is hardware dependent. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
| triggerMinQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto.NameValueDescriptionRFMXLTE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL0 (0x0)The minimum quiet time for triggering is the value of the RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute.RFMXLTE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO1 (0x1)The measurement computes the minimum quiet time used for triggering. |
| Name | Value | Description |  |
| RFMXLTE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |  |
| RFMXLTE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |  |
| triggerMinQuietTimeDuration | [in] | float64 | This parameter specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet above the trigger level.The default value of this parameter is hardware dependent. |
| iqPowerEdgeLevelType | [in] | int32 | This parameter specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type attribute to IQ Power Edge.NameValueDescriptionRFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE0 (0x0)The IQ Power Edge Level attribute is relative to the value of the RFMXLTE_ATTR_REFERENCE_LEVEL attribute.RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE1 (0x1)The IQ Power Edge Level attribute specifies the absolute power. |
| Name | Value | Description |  |
| RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The IQ Power Edge Level attribute is relative to the value of the RFMXLTE_ATTR_REFERENCE_LEVEL attribute. |  |
| RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |  |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__chp_1gaa84a3911f13cb4dcd7964fcb1f3c7e6c.html language=enus -->
## TOPIC 00183: RFmxLTE_CHPFetchTotalAggregatedPower

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__chp_1gaa84a3911f13cb4dcd7964fcb1f3c7e6c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__chp_1gaa84a3911f13cb4dcd7964fcb1f3c7e6c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the sum of powers in all the subblocks. Syntaxint32 __stdcall RFmxLTE_CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramet

### RFmxLTE_CHPFetchTotalAggregatedPower

Fetches the sum of powers in all the subblocks.

#### Syntax

int32 __stdcall RFmxLTE_CHPFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAggregatedPower | [out] | float64 * | This parameter returns the sum of powers of all the frequency bins over the integration bandwidth of subblock. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power in the subblock gaps.When you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, the parameter returns the total integrated power in dBm of all the active carriers measured. When you set the ACP Pwr Units attribute to dBm/Hz, the parameter returns the power spectral density in dBm/Hz based on the power in all the active carriers measured. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga1573c7d02befb675faa0a0318c9cb8e1.html language=enus -->
## TOPIC 00184: RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga1573c7d02befb675faa0a0318c9cb8e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga1573c7d02befb675faa0a0318c9cb8e1.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of detected cell IDs for all the component carriers within the subblock. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedCellId[], int32 arraySize, int32 *actualArraySize)

### RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray

Fetches the array of detected cell IDs for all the component carriers within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedCellId[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedCellId | [out] | int32[] | This parameter returns the array of the detected cell ID values. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga1ff8c4c2c293cd5ddd86880a0c4e62c8.html language=enus -->
## TOPIC 00185: RFmxLTE_ModAccFetchInBandEmissionMarginArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga1ff8c4c2c293cd5ddd86880a0c4e62c8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga1ff8c4c2c293cd5ddd86880a0c4e62c8.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of margins on non allocated resource blocks (RBs) in the uplink signal for all component carriers within the subblock. Syntaxint32 __stdcall RFmxLTE_ModAccFetchInBandEmissionMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 inBandEmissio

### RFmxLTE_ModAccFetchInBandEmissionMarginArray

Returns an array of margins on non allocated resource blocks (RBs) in the uplink signal for all component carriers within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchInBandEmissionMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 inBandEmissionMargin[], int32 arraySize, int32 *actualArraySize)

#### Remarks

The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink**.

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| inBandEmissionMargin | [out] | float64[] | This parameter returns the array of the in-band emission margins. The margin is the least difference between the in-band emission measurement trace and limit trace. The limit is defined in section 6.5.2.3.5 of the 3GPP TS 36.521 specification. The in-band emissions are a measure of the interference falling into the non-allocated resources blocks. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga25517396806eb7b24e830963f3f438ff.html language=enus -->
## TOPIC 00186: RFmxLTE_ModAccFetchDownlinkPCFICHConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga25517396806eb7b24e830963f3f438ff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga25517396806eb7b24e830963f3f438ff.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PCFICH constellation trace for the control channels. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkPCFICHConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pcfichConstellation[], int32 arraySize, int32 *actualArraySize)RemarksUse

### RFmxLTE_ModAccFetchDownlinkPCFICHConstellation

Fetches the PCFICH constellation trace for the control channels.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPCFICHConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pcfichConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pcfichConstellation | [out] | NIComplexSingle[] | This parameter returns the PCFICH constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga2f0aa1530ee5febcd27532aabaec0611.html language=enus -->
## TOPIC 00187: RFmxLTE_ModAccFetchPDSCH1024QAMConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga2f0aa1530ee5febcd27532aabaec0611.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga2f0aa1530ee5febcd27532aabaec0611.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32 *actualArraySize)RemarksU

### RFmxLTE_ModAccFetchPDSCH1024QAMConstellation

Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam1024Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam1024Constellation | [out] | NIComplexSingle[] | This parameter returns the 1024 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga31598da8eb68a283d3ff1307e64245fd.html language=enus -->
## TOPIC 00188: RFmxLTE_ModAccFetchPUSCHDMRSEVM

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga31598da8eb68a283d3ff1307e64245fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga31598da8eb68a283d3ff1307e64245fd.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM values calculated on PUSCH DMRS calculated over the length of the measurement. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPUSCHDMRSEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSDMRSEVM, float64 *maximumPeakDMRSEVM)RemarksUse "carrier<k>

### RFmxLTE_ModAccFetchPUSCHDMRSEVM

Fetches the EVM values calculated on PUSCH DMRS calculated over the length of the measurement.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDMRSEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSDMRSEVM, float64 *maximumPeakDMRSEVM)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSDMRSEVM | [out] | float64 * | This parameter returns the mean value of RMS EVMs calculated on PUSCH DMRS over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dB or in percentage. |
| maximumPeakDMRSEVM | [out] | float64 * | This parameter returns the maximum value of peak EVMs calculated on PUSCH DMRS over the slots specified by the ModAcc Meas Length attribute. This value is expressed in dB or in percentage. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga32e53b99eb6d20c5f957724a2cc9ddac.html language=enus -->
## TOPIC 00189: RFmxLTE_ModAccFetchPDSCH16QAMConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga32e53b99eb6d20c5f957724a2cc9ddac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga32e53b99eb6d20c5f957724a2cc9ddac.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 16 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH16QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32 *a

### RFmxLTE_ModAccFetchPDSCH16QAMConstellationSplit

Fetches the physical downlink shared channel (PDSCH) 16 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH16QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam16ConstellationI[], float32 qam16ConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam16ConstellationI | [out] | float32[] | This parameter Returns the real part of 16 QAM constellation trace. |
| qam16ConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of 16 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga44a94ecff9b9c264d0b9d46a0e466e90.html language=enus -->
## TOPIC 00190: RFmxLTE_ModAccFetchPDSCH64QAMConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga44a94ecff9b9c264d0b9d46a0e466e90.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga44a94ecff9b9c264d0b9d46a0e466e90.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 64 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH64QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64ConstellationI[], float32 qam64ConstellationQ[], int32 arraySize, int32 *a

### RFmxLTE_ModAccFetchPDSCH64QAMConstellationSplit

Fetches the physical downlink shared channel (PDSCH) 64 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH64QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam64ConstellationI[], float32 qam64ConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam64ConstellationI | [out] | float32[] | This parameter Returns the real part of 64 QAM constellation trace. |
| qam64ConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of 64 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga45eb1f551769d6d6e210d6c5a0377a3c.html language=enus -->
## TOPIC 00191: RFmxLTE_ModAccFetchPDSCH256QAMConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga45eb1f551769d6d6e210d6c5a0377a3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga45eb1f551769d6d6e210d6c5a0377a3c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 256 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH256QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32 *actualArraySize)RemarksUse

### RFmxLTE_ModAccFetchPDSCH256QAMConstellation

Fetches the physical downlink shared channel (PDSCH) 256 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH256QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam256Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam256Constellation | [out] | NIComplexSingle[] | This parameter returns the 256 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga471d18cd6bd02c0d55fec70aed3e0aff.html language=enus -->
## TOPIC 00192: RFmxLTE_ModAccFetchPDSCH64QAMConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga471d18cd6bd02c0d55fec70aed3e0aff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga471d18cd6bd02c0d55fec70aed3e0aff.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 64 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH64QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "ca

### RFmxLTE_ModAccFetchPDSCH64QAMConstellation

Fetches the physical downlink shared channel (PDSCH) 64 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH64QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam64Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam64Constellation | [out] | NIComplexSingle[] | This parameter returns the 64 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga48bcd1f70b657f05e0243ead45c2a934.html language=enus -->
## TOPIC 00193: RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga48bcd1f70b657f05e0243ead45c2a934.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga48bcd1f70b657f05e0243ead45c2a934.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PHICH constellation trace for the control channels. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 phichConstellationI[], float32 phichConstellationQ[], int32 arraySize, int32 *a

### RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit

Fetches the PHICH constellation trace for the control channels.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 phichConstellationI[], float32 phichConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| phichConstellationI | [out] | float32[] | This parameter Returns the real part of PHICH constellation trace. |
| phichConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PHICH constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6420cb401940768f274f2418de689062.html language=enus -->
## TOPIC 00194: RFmxLTE_ModAccFetchNRSConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6420cb401940768f274f2418de689062.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6420cb401940768f274f2418de689062.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for a narrow-band reference signal. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNRSConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 nrsConstellationI[], float32 nrsConstellationQ[], int32 arraySize, int32 *actualArray

### RFmxLTE_ModAccFetchNRSConstellationSplit

Fetches the constellation trace for a narrow-band reference signal.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNRSConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 nrsConstellationI[], float32 nrsConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| nrsConstellationI | [out] | float32[] | This parameter returns NRS constellation trace. |
| nrsConstellationQ | [out] | float32[] | This parameter returns NRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga65b074b754d77d694aae753d004bfdae.html language=enus -->
## TOPIC 00195: RFmxLTE_ModAccFetchPDSCH256QAMConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga65b074b754d77d694aae753d004bfdae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga65b074b754d77d694aae753d004bfdae.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 256 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH256QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256ConstellationI[], float32 qam256ConstellationQ[], int32 arraySize, int3

### RFmxLTE_ModAccFetchPDSCH256QAMConstellationSplit

Fetches the physical downlink shared channel (PDSCH) 256 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH256QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam256ConstellationI[], float32 qam256ConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam256ConstellationI | [out] | float32[] | This parameter Returns the real part of 256 QAM constellation trace. |
| qam256ConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of 256 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga69556c4f78bab3a39f12bf6301183d42.html language=enus -->
## TOPIC 00196: RFmxLTE_ModAccFetchPDSCH16QAMConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga69556c4f78bab3a39f12bf6301183d42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga69556c4f78bab3a39f12bf6301183d42.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 16 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH16QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "ca

### RFmxLTE_ModAccFetchPDSCH16QAMConstellation

Fetches the physical downlink shared channel (PDSCH) 16 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH16QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam16Constellation | [out] | NIComplexSingle[] | This parameter returns the 16 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6d4219d34cb319932ca434388190b07d.html language=enus -->
## TOPIC 00197: RFmxLTE_ModAccFetchNPUSCHConstellationTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6d4219d34cb319932ca434388190b07d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6d4219d34cb319932ca434388190b07d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recovered narrowband physical uplink shared channel (NPUSCH) constellation points. The constellation points of different slots in the measurement length are concatenated. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNPUSCHConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxLTE_ModAccFetchNPUSCHConstellationTrace

Returns the recovered narrowband physical uplink shared channel (NPUSCH) constellation points. The constellation points of different slots in the measurement length are concatenated.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNPUSCHConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle dataConstellation[], int32 dataConstellationArraySize, int32 *dataConstellationActualArraySize, NIComplexSingle dmrsConstellation[], int32 dmrsConstellationArraySize, int32 *dmrsConstellationActualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dataConstellation | [out] | NIComplexSingle[] | This parameter returns the data constellation trace. |
| dataConstellationArraySize | [in] | int32 | Specifies the size of the DataConstellation array. Set the DataConstellationArraySize parameter to 0 to get the size of the DataConstellation array in the DataConstellationActualArraySize parameter. |
| dataConstellationActualArraySize | [out] | int32 * | Returns the actual size of dataConstellation array, if you pass NULL to all output array parameters, and set the dataConstellationArraySize parameter to 0. |
| dmrsConstellation | [out] | NIComplexSingle[] | This parameter returns the demodulation reference signal (DMRS) constellation trace. |
| dmrsConstellationArraySize | [in] | int32 | Specifies the size of the DMRSConstellation array. Set the DMRSConstellationArraySize parameter to 0 to get the size of the DMRSConstellation array in the DMRSConstellationActualArraySize parameter. |
| dmrsConstellationActualArraySize | [out] | int32 * | Returns the actual size of DMRSConstellation array, if you pass NULL to all output array parameters, and set the DMRSConstellationArraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6dc008ce72622e5fafdf6775684e1a5f.html language=enus -->
## TOPIC 00198: RFmxLTE_ModAccFetchNBSynchronizationSignalConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6dc008ce72622e5fafdf6775684e1a5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga6dc008ce72622e5fafdf6775684e1a5f.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellations traces for NPSS and NSSS. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNBSynchronizationSignalConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle nSSSConstellation[], int32 nSSSConstellationArraySize, int32 *nSSSConstellati

### RFmxLTE_ModAccFetchNBSynchronizationSignalConstellation

Fetches the constellations traces for NPSS and NSSS.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNBSynchronizationSignalConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle nSSSConstellation[], int32 nSSSConstellationArraySize, int32 *nSSSConstellationActualArraySize, NIComplexSingle nPSSConstellation[], int32 nPSSConstellationArraySize, int32 *nPSSConstellationActualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| nSSSConstellation | [out] | NIComplexSingle[] | This parameter returns NSSS constellation trace. |
| nSSSConstellationArraySize | [in] | int32 | Specifies the size of the NSSSConstellation array. Set the NSSSConstellationArraySize parameter to 0 to get the size of the NSSSConstellation array in the NSSSConstellationActualArraySize parameter. |
| nSSSConstellationActualArraySize | [out] | int32 * | Returns the actual size of NSSSConstellation array, if you pass NULL to all output array parameters, and set the NSSSConstellationArraySize parameter to 0. |
| nPSSConstellation | [out] | NIComplexSingle[] | This parameter returns NPSS constellation trace. |
| nPSSConstellationArraySize | [in] | int32 | Specifies the size of the NPSSConstellation array. Set the NPSSConstellationArraySize parameter to 0 to get the size of the NPSSConstellation array in the NPSSConstellationActualArraySize parameter. |
| nPSSConstellationActualArraySize | [out] | int32 * | Returns the actual size of NPSSConstellation array, if you pass NULL to all output array parameters, and set the NPSSConstellationArraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga729383b59172268129f4fa2805d4a10b.html language=enus -->
## TOPIC 00199: RFmxLTE_ModAccFetchEVMHighPerSymbolTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga729383b59172268129f4fa2805d4a10b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga729383b59172268129f4fa2805d4a10b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2. Syntaxint32 __stdcall RFmxLTE_ModAccFetchEVMHighPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float

### RFmxLTE_ModAccFetchEVMHighPerSymbolTrace

Returns the EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchEVMHighPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evmHighPerSymbol[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| evmHighPerSymbol | [out] | float32[] | This parameter returns the array of the EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C+W/2. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga72f433195d281af891d89c22e2d6becb.html language=enus -->
## TOPIC 00200: RFmxLTE_ModAccFetchPDSCHEVM

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga72f433195d281af891d89c22e2d6becb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga72f433195d281af891d89c22e2d6becb.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) EVMs. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCHEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSEVM, float64 *meanRMSQPSKEVM, float64 *meanRms16QAMEVM, float64 *meanRms64QAMEVM, float64 *meanRms2

### RFmxLTE_ModAccFetchPDSCHEVM

Fetches the physical downlink shared channel (PDSCH) EVMs.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCHEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSEVM, float64 *meanRMSQPSKEVM, float64 *meanRms16QAMEVM, float64 *meanRms64QAMEVM, float64 *meanRms256QAMEVM)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSEVM | [out] | float64 * | This parameter returns the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRMSQPSKEVM | [out] | float64 * | This parameter returns the mean value of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRms16QAMEVM | [out] | float64 * | This parameter returns the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRms64QAMEVM | [out] | float64 * | This parameter returns the mean value of RMS EVMs calculated on all 64QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRms256QAMEVM | [out] | float64 * | This parameter returns the mean value of RMS EVMs calculated on all 256QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga7595f47750852b1098e93fed1d563173.html language=enus -->
## TOPIC 00201: RFmxLTE_ModAccFetchMaximumEVMHighPerSymbolTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga7595f47750852b1098e93fed1d563173.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga7595f47750852b1098e93fed1d563173.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2. Syntaxint32 __stdcall RFmxLTE_ModAccFetchMaximumEVMHighPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, flo

### RFmxLTE_ModAccFetchMaximumEVMHighPerSymbolTrace

Returns the maximum EVM per symbol trace for all the configured slots. The EVM is obtained by using the FFT window position, Delta_C+W/2.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMHighPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumEVMHighPerSymbol[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| maximumEVMHighPerSymbol | [out] | float32[] | This parameter returns the array of the maximum EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C+W/2. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga77412727f7eab064e631b2f82efef591.html language=enus -->
## TOPIC 00202: RFmxLTE_ModAccFetchDownlinkPBCHConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga77412727f7eab064e631b2f82efef591.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga77412727f7eab064e631b2f82efef591.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PBCH constellation trace for the control channels. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkPBCHConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchConstellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carri

### RFmxLTE_ModAccFetchDownlinkPBCHConstellation

Fetches the PBCH constellation trace for the control channels.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPBCHConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pbchConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pbchConstellation | [out] | NIComplexSingle[] | This parameter returns the PBCH constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga7944794181ad4074446a737a4c55705d.html language=enus -->
## TOPIC 00203: RFmxLTE_ModAccFetchDownlinkPCFICHConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga7944794181ad4074446a737a4c55705d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga7944794181ad4074446a737a4c55705d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PCFICH constellation trace for the control channels. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkPCFICHConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pcfichConstellationI[], float32 pcfichConstellationQ[], int32 arraySize, int3

### RFmxLTE_ModAccFetchDownlinkPCFICHConstellationSplit

Fetches the PCFICH constellation trace for the control channels.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPCFICHConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pcfichConstellationI[], float32 pcfichConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pcfichConstellationI | [out] | float32[] | This parameter Returns the real part of PCFICH constellation trace. |
| pcfichConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PCFICH constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga83b082eb5fdd192196dbeee168d1e431.html language=enus -->
## TOPIC 00204: RFmxLTE_ModAccFetchNRSConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga83b082eb5fdd192196dbeee168d1e431.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga83b082eb5fdd192196dbeee168d1e431.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for a narrow-band reference signal. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNRSConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle nrsConstellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>

### RFmxLTE_ModAccFetchNRSConstellation

Fetches the constellation trace for a narrow-band reference signal.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNRSConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle nrsConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| nrsConstellation | [out] | NIComplexSingle[] | This parameter returns NRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8919888146bc8214ad5d63acc09966d0.html language=enus -->
## TOPIC 00205: RFmxLTE_ModAccFetchPSSCHConstellationTraceSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8919888146bc8214ad5d63acc09966d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8919888146bc8214ad5d63acc09966d0.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recovered physical sidelink shared channel (PSSCH) constellation points. The constellation points of different slots in the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH are concatenated. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPSSCHConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, c

### RFmxLTE_ModAccFetchPSSCHConstellationTraceSplit

Returns the recovered physical sidelink shared channel (PSSCH) constellation points. The constellation points of different slots in the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) are concatenated.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPSSCHConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 dataConstellationI[], float32 dataConstellationQ[], float32 dmrsConstellationI[], float32 dmrsConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dataConstellationI | [out] | float32[] | This parameter Returns the real part of PSSCH data constellation trace. |
| dataConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PSSCH data constellation trace. |
| dmrsConstellationI | [out] | float32[] | This parameter Returns the real part of PSSCH demodulation reference signal (DMRS) constellation trace. |
| dmrsConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PSSCH demodulation reference signal (DMRS) constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8a7462ffe2b9c4759f6ca890c2dc2c5f.html language=enus -->
## TOPIC 00206: RFmxLTE_ModAccFetchNPDSCH16QAMConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8a7462ffe2b9c4759f6ca890c2dc2c5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8a7462ffe2b9c4759f6ca890c2dc2c5f.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the narrow-band physical downlink shared channel (NPDSCH) 16 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNPDSCH16QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32 *actualArraySize)

### RFmxLTE_ModAccFetchNPDSCH16QAMConstellation

Fetches the narrow-band physical downlink shared channel (NPDSCH) 16 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNPDSCH16QAMConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qam16Constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam16Constellation | [out] | NIComplexSingle[] | This parameter returns the 16 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8f67a4d74e51024ef9e03ce4ad5ae315.html language=enus -->
## TOPIC 00207: RFmxLTE_ModAccFetchSpectralFlatnessArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8f67a4d74e51024ef9e03ce4ad5ae315.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1ga8f67a4d74e51024ef9e03ce4ad5ae315.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of spectral flatness measurements of all component carriers within the subblock. Syntaxint32 __stdcall RFmxLTE_ModAccFetchSpectralFlatnessArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 range1MaximumToRange1Minimum[], float64 range2Maximum

### RFmxLTE_ModAccFetchSpectralFlatnessArray

Returns the arrays of spectral flatness measurements of all component carriers within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchSpectralFlatnessArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 range1MaximumToRange1Minimum[], float64 range2MaximumToRange2Minimum[], float64 range1MaximumToRange2Minimum[], float64 range2MaximumToRange1Minimum[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| range1MaximumToRange1Minimum | [out] | float64[] | This parameter returns the array of the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. The frequency Range1 is as defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange2Minimum | [out] | float64[] | This parameter returns the array of the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range2. The frequency Range2 is defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range1MaximumToRange2Minimum | [out] | float64[] | This parameter returns the array of the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Range2. The frequency Range1 and 2 are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange1Minimum | [out] | float64[] | This parameter returns the array of the peak-to-peak ripple of the EVM equalizer coefficients from frequency Range2 to frequency Range1. The frequency Range1 and 2 are defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaa92dbd119ea540926805877086463be5.html language=enus -->
## TOPIC 00208: RFmxLTE_ModAccFetchEVMPerSlotTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaa92dbd119ea540926805877086463be5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaa92dbd119ea540926805877086463be5.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM of each slot averaged across all the symbols within the slots and all the allocated subcarriers. Syntaxint32 __stdcall RFmxLTE_ModAccFetchEVMPerSlotTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rmsEVMPerSlot[], int

### RFmxLTE_ModAccFetchEVMPerSlotTrace

Returns the EVM of each slot averaged across all the symbols within the slots and all the allocated subcarriers.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchEVMPerSlotTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rmsEVMPerSlot[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<k>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM slot position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| rmsEVMPerSlot | [out] | float32[] | This parameter returns the EVM of each slot averaged across all the symbols within the slots and all the allocated subcarriers. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaaee4f9a0b79204bbf94a93f15b4f310e.html language=enus -->
## TOPIC 00209: RFmxLTE_ModAccFetchSRSConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaaee4f9a0b79204bbf94a93f15b4f310e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaaee4f9a0b79204bbf94a93f15b4f310e.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the SRS channel. Syntaxint32 __stdcall RFmxLTE_ModAccFetchSRSConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle srsConstellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<k>" or "subblock<

### RFmxLTE_ModAccFetchSRSConstellation

Fetches the constellation trace for the SRS channel.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchSRSConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle srsConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| srsConstellation | [out] | NIComplexSingle[] | This parameter returns the SRS constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab0845bb211c9bee5fd0931e285de6276.html language=enus -->
## TOPIC 00210: RFmxLTE_ModAccFetchPSSCHSymbolPower

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab0845bb211c9bee5fd0931e285de6276.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab0845bb211c9bee5fd0931e285de6276.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPSSCHSymbolPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *psschMeanDataPower, float64 *psschMeanDMRSPower)RemarksUse "c

### RFmxLTE_ModAccFetchPSSCHSymbolPower

Fetches the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPSSCHSymbolPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *psschMeanDataPower, float64 *psschMeanDMRSPower)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| psschMeanDataPower | [out] | float64 * | This parameter returns the mean value of the power calculated on the PSSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. |
| psschMeanDMRSPower | [out] | float64 * | This parameter returns the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length attribute. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab1353bdd92b8e4f898b7cc7f077f0d57.html language=enus -->
## TOPIC 00211: RFmxLTE_ModAccFetchDownlinkTransmitPower

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab1353bdd92b8e4f898b7cc7f077f0d57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab1353bdd92b8e4f898b7cc7f077f0d57.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference signal power and the OFDM symbol transmit power. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkTransmitPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rsTransmitPower, float64 *ofdmSymbolTransmitPower, float64 *reserved1, float64 *r

### RFmxLTE_ModAccFetchDownlinkTransmitPower

Fetches the reference signal power and the OFDM symbol transmit power.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkTransmitPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rsTransmitPower, float64 *ofdmSymbolTransmitPower, float64 *reserved1, float64 *reserved2)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rsTransmitPower | [out] | float64 * | This parameter returns the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. |
| ofdmSymbolTransmitPower | [out] | float64 * | This parameter returns the mean power value calculated in one OFDM symbol over the slots specified by the ModAcc Meas Length attribute. This value is expressed in dBm. |
| reserved1 | [out] | float64 * | This parameter this result is not supported in this release and it is reserved for future enhancements. |
| reserved2 | [out] | float64 * | This parameter this result is not supported in this release and it is reserved for future enhancements. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab26ffb1a21dfcbb7ec81b4369c832991.html language=enus -->
## TOPIC 00212: RFmxLTE_ModAccFetchSRSEVMArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab26ffb1a21dfcbb7ec81b4369c832991.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab26ffb1a21dfcbb7ec81b4369c832991.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of SRS EVMs for all the component carriers within the subblock. This value is expressed in percentage or dB. Syntaxint32 __stdcall RFmxLTE_ModAccFetchSRSEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSSRSEVM[], float64 meanSRSPowe

### RFmxLTE_ModAccFetchSRSEVMArray

Fetches the array of SRS EVMs for all the component carriers within the subblock. This value is expressed in percentage or dB.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchSRSEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSSRSEVM[], float64 meanSRSPower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSSRSEVM | [out] | float64[] | This parameter returns the array of mean values of RMS EVMs calculated on the SRS symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanSRSPower | [out] | float64[] | This parameter returns the array of mean values of power calculated on SRS over the slots specified by the ModAcc Meas Length attribute. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab2ab3dcbc3e38c08ce91cfbecb347934.html language=enus -->
## TOPIC 00213: RFmxLTE_ModAccFetchMaximumEVMPerSymbolTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab2ab3dcbc3e38c08ce91cfbecb347934.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab2ab3dcbc3e38c08ce91cfbecb347934.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value of an EVM for each symbol computed across all the allocated subcarriers. Syntaxint32 __stdcall RFmxLTE_ModAccFetchMaximumEVMPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumEVMPerSymbol[], int32

### RFmxLTE_ModAccFetchMaximumEVMPerSymbolTrace

Returns the peak value of an EVM for each symbol computed across all the allocated subcarriers.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumEVMPerSymbol[], int32 arraySize, int32 *actualArraySize)

#### Remarks

The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink**.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| maximumEVMPerSymbol | [out] | float32[] | This parameter returns the peak value of an EVM for each symbol computed across all the allocated subcarriers. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab40e9472593c2c8263e8a12500770669.html language=enus -->
## TOPIC 00214: RFmxLTE_ModAccFetchDownlinkDetectedCellID

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab40e9472593c2c8263e8a12500770669.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab40e9472593c2c8263e8a12500770669.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected cell ID. This function is valid only when the measured signal contains primary synchronization signal (PSS) and secondary synchronization signal (SSS). Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellID(niRFmxInstrHandle instrumentHandle, char selectorString[], floa

### RFmxLTE_ModAccFetchDownlinkDetectedCellID

Fetches the detected cell ID. This function is valid only when the measured signal contains primary synchronization signal (PSS) and secondary synchronization signal (SSS).

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellID(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedCellId)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedCellId | [out] | int32 * | This parameter returns the detected cell ID value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab43354faaa581b13f906fc50b6a2be1d.html language=enus -->
## TOPIC 00215: RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab43354faaa581b13f906fc50b6a2be1d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab43354faaa581b13f906fc50b6a2be1d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS mean value of the magnitude error for each symbol computed over all the allocated subcarriers and within the measurement length. Syntaxint32 __stdcall RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float6

### RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace

Returns the RMS mean value of the magnitude error for each symbol computed over all the allocated subcarriers and within the measurement length.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rmsMagnitudeErrorPerSymbol[], int32 arraySize, int32 *actualArraySize)

#### Remarks

The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink**.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| rmsMagnitudeErrorPerSymbol | [out] | float32[] | This parameter returns the RMS mean value of the magnitude error for each symbol computed over all the allocated subcarriers and within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab43e4ecde36c3315a24383cb1a0a401d.html language=enus -->
## TOPIC 00216: RFmxLTE_ModAccFetchDownlinkPBCHConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab43e4ecde36c3315a24383cb1a0a401d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab43e4ecde36c3315a24383cb1a0a401d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PBCH constellation trace for the control channels. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkPBCHConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchConstellationI[], float32 pbchConstellationQ[], int32 arraySize, int32 *actua

### RFmxLTE_ModAccFetchDownlinkPBCHConstellationSplit

Fetches the PBCH constellation trace for the control channels.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPBCHConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pbchConstellationI[], float32 pbchConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pbchConstellationI | [out] | float32[] | This parameter Returns the real part of PBCH constellation trace. |
| pbchConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of PBCH constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab4acd34bd85b23eba5a9db4bb58d7946.html language=enus -->
## TOPIC 00217: RFmxLTE_ModAccFetchPUSCHConstellationTraceSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab4acd34bd85b23eba5a9db4bb58d7946.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab4acd34bd85b23eba5a9db4bb58d7946.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recovered physical uplink shared channel (PUSCH) constellation points. The constellation points of different slots in the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH are concatenated. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPUSCHConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, cha

### RFmxLTE_ModAccFetchPUSCHConstellationTraceSplit

Returns the recovered physical uplink shared channel (PUSCH) constellation points. The constellation points of different slots in the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) are concatenated.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPUSCHConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 dataConstellationI[], float32 dataConstellationQ[], int32 dataConstellationArraySize, int32 *dataConstellationActualArraySize, float32 dmrsConstellationI[], float32 dmrsConstellationQ[], int32 dmrsConstellationArraySize, int32 *dmrsConstellationActualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dataConstellationI | [out] | float32[] | This parameter Returns the real part of data constellation trace. |
| dataConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of data constellation trace. |
| dataConstellationArraySize | [in] | int32 | This parameter returns the demodulation reference signal (DMRS) constellation trace. |
| dataConstellationActualArraySize | [out] | int32 * | Returns the actual size of dataConstellation array, if you pass NULL to all output array parameters, and set the dataConstellationArraySize parameter to 0. |
| dmrsConstellationI | [out] | float32[] | This parameter Returns the real part of demodulation reference signal (DMRS) constellation trace. |
| dmrsConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of demodulation reference signal (DMRS) constellation trace. |
| dmrsConstellationArraySize | [in] | int32 | Specifies the size of the DMRSConstellation array. Set the DMRSConstellationArraySize parameter to 0 to get the size of the DMRSConstellation array in the DMRSConstellationActualArraySize parameter. |
| dmrsConstellationActualArraySize | [out] | int32 * | Returns the actual size of DMRSConstellation array, if you pass NULL to all output array parameters, and set the DMRSConstellationArraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab6af7c422372cac8b819b9ba64aca4ea.html language=enus -->
## TOPIC 00218: RFmxLTE_ModAccFetchPDSCH1024QAMEVM

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab6af7c422372cac8b819b9ba64aca4ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gab6af7c422372cac8b819b9ba64aca4ea.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 1024QAM EVMs. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRms1024QAMEVM)RemarksUse "carrier<k>" or "subblock<n>/carrier<k>" as the selector strin

### RFmxLTE_ModAccFetchPDSCH1024QAMEVM

Fetches the physical downlink shared channel (PDSCH) 1024QAM EVMs.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRms1024QAMEVM)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRms1024QAMEVM | [out] | float64 * | This parameter returns a mean value of the calculated RMS EVMs on all 1024QAM modulated PDSCH resource blocks over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaba5405ca51578dd87664c3d4a21d7a9c.html language=enus -->
## TOPIC 00219: RFmxLTE_ModAccFetchNBSynchronizationSignalConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaba5405ca51578dd87664c3d4a21d7a9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaba5405ca51578dd87664c3d4a21d7a9c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellations traces for NPSS and NSSS. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNBSynchronizationSignalConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 nSSSConstellationI[], float32 nSSSConstellationQ[], int32 nSSSConstellationArray

### RFmxLTE_ModAccFetchNBSynchronizationSignalConstellationSplit

Fetches the constellations traces for NPSS and NSSS.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNBSynchronizationSignalConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 nSSSConstellationI[], float32 nSSSConstellationQ[], int32 nSSSConstellationArraySize, int32 *nSSSConstellationActualArraySize, float32 nPSSConstellationI[], float32 nPSSConstellationQ[], int32 nPSSConstellationArraySize, int32 *nPSSConstellationActualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| nSSSConstellationI | [out] | float32[] | This parameter returns NSSS constellation trace. |
| nSSSConstellationQ | [out] | float32[] | This parameter returns NSSS constellation trace. |
| nSSSConstellationArraySize | [in] | int32 | Specifies the size of the NSSSConstellation array. Set the NSSSConstellationArraySize parameter to 0 to get the size of the NSSSConstellation array in the NSSSConstellationActualArraySize parameter. |
| nSSSConstellationActualArraySize | [out] | int32 * | Returns the actual size of NSSSConstellation array, if you pass NULL to all output array parameters, and set the NSSSConstellationArraySize parameter to 0. |
| nPSSConstellationI | [out] | float32[] | This parameter returns NPSS constellation trace. |
| nPSSConstellationQ | [out] | float32[] | This parameter returns NPSS constellation trace. |
| nPSSConstellationArraySize | [in] | int32 | Specifies the size of the NPSSConstellation array. Set the NPSSConstellationArraySize parameter to 0 to get the size of the NPSSConstellation array in the NPSSConstellationActualArraySize parameter. |
| nPSSConstellationActualArraySize | [out] | int32 * | Returns the actual size of NPSSConstellation array, if you pass NULL to all output array parameters, and set the NPSSConstellationArraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaba78acbb7d7723d42bb9bb560007c5e0.html language=enus -->
## TOPIC 00220: RFmxLTE_ModAccFetchNPDSCHQPSKConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaba78acbb7d7723d42bb9bb560007c5e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaba78acbb7d7723d42bb9bb560007c5e0.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the narrow-band physical downlink shared channel (NPDSCH) QPSK trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNPDSCHQPSKConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize,

### RFmxLTE_ModAccFetchNPDSCHQPSKConstellationSplit

Fetches the narrow-band physical downlink shared channel (NPDSCH) QPSK trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNPDSCHQPSKConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qpskConstellationI[], float32 qpskConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qpskConstellationI | [out] | float32[] | This parameter Returns the real part of QPSK constellation trace. |
| qpskConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of QPSK constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac38dab56c7d87a39eddcb54b6ae17de7.html language=enus -->
## TOPIC 00221: RFmxLTE_ModAccFetchNPDSCHQPSKConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac38dab56c7d87a39eddcb54b6ae17de7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac38dab56c7d87a39eddcb54b6ae17de7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the narrow-band physical downlink shared channel (NPDSCH) QPSK trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchNPDSCHQPSKConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32 *actualArraySize)Rema

### RFmxLTE_ModAccFetchNPDSCHQPSKConstellation

Fetches the narrow-band physical downlink shared channel (NPDSCH) QPSK trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchNPDSCHQPSKConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qpskConstellation | [out] | NIComplexSingle[] | This parameter returns the QPSK constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac4542233638eac918c75a8e137450941.html language=enus -->
## TOPIC 00222: RFmxLTE_ModAccFetchSubblockInBandEmissionMargin

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac4542233638eac918c75a8e137450941.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac4542233638eac918c75a8e137450941.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin on non-allocated resource blocks (RBs) within the subblock aggregated bandwidth. This value is expressed in dB. Syntaxint32 __stdcall RFmxLTE_ModAccFetchSubblockInBandEmissionMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *subblockInBand

### RFmxLTE_ModAccFetchSubblockInBandEmissionMargin

Returns the margin on non-allocated resource blocks (RBs) within the subblock aggregated bandwidth. This value is expressed in dB.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchSubblockInBandEmissionMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *subblockInBandEmissionMargin)

#### Remarks

The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink** and the [RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE](group____root__ni_r_fmx_l_t_e__attributes__advanced_1ga5d643b5746c2f72fdd88fc489c5d66e8.html) attribute to **LO per Subblock**.

Refer to section 6.5.2A.3 of the *3GPP TS 36.521* specification for more information about in-band emission margin.

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| subblockInBandEmissionMargin | [out] | float64 * | This parameter returns the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB.The margin is the lowest difference between the in-band emission measurement trace and the limit trace. The limit is defined in section 6.5.2A.3 of the 3GPP TS 36.521 specification.The in-band emissions are a measure of the interference in the non-allocated resources blocks. This result is valid only when you set the RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE attribute to LO per Subblock. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac489a7b154aeb2ade7683c00da505a52.html language=enus -->
## TOPIC 00223: RFmxLTE_ModAccFetchDownlinkTransmitPowerArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac489a7b154aeb2ade7683c00da505a52.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac489a7b154aeb2ade7683c00da505a52.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of reference signal powers and the OFDM symbol transmit powers for all the component carriers within the subblock. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkTransmitPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 rsTransmitPower

### RFmxLTE_ModAccFetchDownlinkTransmitPowerArray

Fetches the array of reference signal powers and the OFDM symbol transmit powers for all the component carriers within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkTransmitPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 rsTransmitPower[], float64 ofdmSymbolTransmitPower[], float64 reserved1[], float64 reserved2[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rsTransmitPower | [out] | float64[] | This parameter returns the array of mean values of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. |
| ofdmSymbolTransmitPower | [out] | float64[] | This parameter returns the array the mean value of power calculated in one OFDM symbol over the slots specified by the ModAcc Meas Length attribute. This value is expressed in dBm. |
| reserved1 | [out] | float64[] | This parameter this result is not supported in this release and it is reserved for future enhancements. |
| reserved2 | [out] | float64[] | This parameter this result is not supported in this release and it is reserved for future enhancements. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac74682785422cce73434292e705a17af.html language=enus -->
## TOPIC 00224: RFmxLTE_ModAccFetchMaximumEVMLowPerSymbolTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac74682785422cce73434292e705a17af.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac74682785422cce73434292e705a17af.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C-W/2. Syntaxint32 __stdcall RFmxLTE_ModAccFetchMaximumEVMLowPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64

### RFmxLTE_ModAccFetchMaximumEVMLowPerSymbolTrace

Returns the maximum EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C-W/2.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMLowPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumEVMLowPerSymbol[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Refer to the [LTE Modulation Accuracy](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-modulation-accuracy.html) topic for more information.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| maximumEVMLowPerSymbol | [out] | float32[] | This parameter returns the array of the maximum EVM per symbol trace for all the configured slots. The EVM is obtained by using FFT window position, Delta_C-W/2. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac9b1c5c4e3e2fb4d1652e434a7764d6d.html language=enus -->
## TOPIC 00225: RFmxLTE_ModAccFetchCompositeEVMArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac9b1c5c4e3e2fb4d1652e434a7764d6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gac9b1c5c4e3e2fb4d1652e434a7764d6d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the composite EVM for ModAcc measurements. Syntaxint32 __stdcall RFmxLTE_ModAccFetchCompositeEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSCompositeEVM[], float64 maximumPeakCompositeEVM[], float64 meanFrequencyError[], int32

### RFmxLTE_ModAccFetchCompositeEVMArray

Returns an array of the composite EVM for ModAcc measurements.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchCompositeEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSCompositeEVM[], float64 maximumPeakCompositeEVM[], float64 meanFrequencyError[], int32 peakCompositeEVMSymbolIndex[], int32 peakCompositeEVMSubcarrierIndex[], int32 peakCompositeEVMSlotIndex[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSCompositeEVM | [out] | float64[] | This parameter returns the array of the mean value of the RMS EVMs calculated on all configured channels over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| maximumPeakCompositeEVM | [out] | float64[] | This parameter returns the array of the maximum value of peak EVMs calculated on all configured channels over the slots specified by the ModAcc Meas Length attribute. |
| meanFrequencyError | [out] | float64[] | This parameter returns the array of the estimated carrier frequency offset averaged over the slots specified by the ModAcc Meas Length attribute. |
| peakCompositeEVMSymbolIndex | [out] | int32[] | This parameter returns the array of the symbol index where the ModAcc maximum peak composite EVM occurs. |
| peakCompositeEVMSubcarrierIndex | [out] | int32[] | This parameter returns the array of the subcarrier index of the RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM attribute. |
| peakCompositeEVMSlotIndex | [out] | int32[] | This parameter returns the array of the slot index where the ModAcc maximum peak composite EVM occurs. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacbb59b1b0807591f0db7e6a80c6a6d16.html language=enus -->
## TOPIC 00226: RFmxLTE_ModAccFetchDownlinkPHICHConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacbb59b1b0807591f0db7e6a80c6a6d16.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacbb59b1b0807591f0db7e6a80c6a6d16.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PHICH constellation trace for the control channels. Syntaxint32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle phichConstellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "ca

### RFmxLTE_ModAccFetchDownlinkPHICHConstellation

Fetches the PHICH constellation trace for the control channels.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle phichConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| phichConstellation | [out] | NIComplexSingle[] | This parameter returns the PHICH constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacc5ef30ff5e8fbd32036c9b128da2c74.html language=enus -->
## TOPIC 00227: RFmxLTE_ModAccFetchPSSCHDMRSEVMArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacc5ef30ff5e8fbd32036c9b128da2c74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacc5ef30ff5e8fbd32036c9b128da2c74.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of the EVM values calculated on PSSCH DMRS over the length of the measurement. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPSSCHDMRSEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 psschMeanRMSDMRSEVM[], float64 psschMaximumPeakDMRSEVM[], in

### RFmxLTE_ModAccFetchPSSCHDMRSEVMArray

Fetches the array of the EVM values calculated on PSSCH DMRS over the length of the measurement.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPSSCHDMRSEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 psschMeanRMSDMRSEVM[], float64 psschMaximumPeakDMRSEVM[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

When you set the [RFMXLTE_ATTR_MODACC_EVM_UNIT](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga38ac29765674be0a00483d3ff897ed09.html) attribute to **Percentage**, the function returns the results as a percentage. When you set the ModAcc EVM Unit attribute to **dB**, the function returns the results in dB.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| psschMeanRMSDMRSEVM | [out] | float64[] | This parameter returns the array of the mean value of the RMS EVMs calculated on the PSSCH DMRS symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. |
| psschMaximumPeakDMRSEVM | [out] | float64[] | This parameter returns the array of the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacf09bb5603a1f2eba1f698f55a1f63d4.html language=enus -->
## TOPIC 00228: RFmxLTE_ModAccFetchCSRSEVM

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacf09bb5603a1f2eba1f698f55a1f63d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gacf09bb5603a1f2eba1f698f55a1f63d4.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the cell-specific reference signal EVM. Syntaxint32 __stdcall RFmxLTE_ModAccFetchCSRSEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSCSRSEVM)RemarksUse "offset<k>" or "subblock<n>/offset<k>" as the selector string to read results from this func

### RFmxLTE_ModAccFetchCSRSEVM

Fetches the cell-specific reference signal EVM.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchCSRSEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSCSRSEVM)

#### Remarks

Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSCSRSEVM | [out] | float64 * | This parameter returns the mean value of RMS EVMs calculated on Reference Signal (RS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gad2030f08d2d08576e349a278033797ae.html language=enus -->
## TOPIC 00229: RFmxLTE_ModAccFetchPDSCH1024QAMConstellationSplit

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gad2030f08d2d08576e349a278033797ae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gad2030f08d2d08576e349a278033797ae.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize,

### RFmxLTE_ModAccFetchPDSCH1024QAMConstellationSplit

Fetches the physical downlink shared channel (PDSCH) 1024 QAM trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMConstellationSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 qam1024ConstellationI[], float32 qam1024ConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qam1024ConstellationI | [out] | float32[] | This parameter Returns the real part of 1024 QAM constellation trace. |
| qam1024ConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of 1024 QAM constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gad96807680f3acf22d05ffc2c0f507e24.html language=enus -->
## TOPIC 00230: RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gad96807680f3acf22d05ffc2c0f507e24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gad96807680f3acf22d05ffc2c0f507e24.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. Syntaxint32 __stdcall RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace

Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumFrequencyErrorPerSlot[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<k>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM slot position corresponding to the RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| maximumFrequencyErrorPerSlot | [out] | float32[] | This parameter returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae377da517bce05828287fce7b77b304c.html language=enus -->
## TOPIC 00231: RFmxLTE_ModAccFetchSpectralFlatness

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae377da517bce05828287fce7b77b304c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae377da517bce05828287fce7b77b304c.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectral flatness measurements of the component carrier. Syntaxint32 __stdcall RFmxLTE_ModAccFetchSpectralFlatness(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *range1MaximumToRange1Minimum, float64 *range2MaximumToRange2Minimum, float64 *range1Maxi

### RFmxLTE_ModAccFetchSpectralFlatness

Returns the spectral flatness measurements of the component carrier.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchSpectralFlatness(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *range1MaximumToRange1Minimum, float64 *range2MaximumToRange2Minimum, float64 *range1MaximumToRange2Minimum, float64 *range2MaximumToRange1Minimum)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| range1MaximumToRange1Minimum | [out] | float64 * | This parameter returns the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. The frequency Range1 is as defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange2Minimum | [out] | float64 * | This parameter returns the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range2. The frequency Range2 is defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range1MaximumToRange2Minimum | [out] | float64 * | This parameter returns the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Range2. The frequency Range1 and 2 are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |
| range2MaximumToRange1Minimum | [out] | float64 * | This parameter returns the peak-to-peak ripple of the EVM equalizer coefficients from frequency Range2 to frequency Range1. The frequency Range1 and 2 are defined in section 6.5.2.4.5 of the 3GPP TS 36.521 specification. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae561a15477393db4a65ad39783523b79.html language=enus -->
## TOPIC 00232: RFmxLTE_ModAccFetchPDSCHQPSKConstellation

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae561a15477393db4a65ad39783523b79.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae561a15477393db4a65ad39783523b79.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the physical downlink shared channel (PDSCH) QPSK trace. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCHQPSKConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrie

### RFmxLTE_ModAccFetchPDSCHQPSKConstellation

Fetches the physical downlink shared channel (PDSCH) QPSK trace.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCHQPSKConstellation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle qpskConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| qpskConstellation | [out] | NIComplexSingle[] | This parameter returns the QPSK constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae641eb78d4a8b8f74dbb8f967c01ca8d.html language=enus -->
## TOPIC 00233: RFmxLTE_ModAccFetchPSSCHSymbolPowerArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae641eb78d4a8b8f74dbb8f967c01ca8d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gae641eb78d4a8b8f74dbb8f967c01ca8d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPSSCHSymbolPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 psschMeanDataPower[], float64 psschMeanDMRSP

### RFmxLTE_ModAccFetchPSSCHSymbolPowerArray

Fetches the array of the physical sidelink shared channel (PSSCH) data symbols power and DMRS symbols power.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPSSCHSymbolPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 psschMeanDataPower[], float64 psschMeanDMRSPower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| psschMeanDataPower | [out] | float64[] | This parameter returns the array of the mean value of the power calculated on the PSSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. This value is expressed in dBm. |
| psschMeanDMRSPower | [out] | float64[] | This parameter returns the array of the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length attribute. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaedb1d226d13304e06e4e077cdc8fb762.html language=enus -->
## TOPIC 00234: RFmxLTE_ModAccFetchPDSCHEVMArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaedb1d226d13304e06e4e077cdc8fb762.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaedb1d226d13304e06e4e077cdc8fb762.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of physical downlink shared channel (PDSCH) EVM for all the component carriers within the subblock. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCHEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSEVM[], float64 meanRMSQPSKEVM[], flo

### RFmxLTE_ModAccFetchPDSCHEVMArray

Fetches the array of physical downlink shared channel (PDSCH) EVM for all the component carriers within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCHEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSEVM[], float64 meanRMSQPSKEVM[], float64 meanRms16QAMEVM[], float64 meanRms64QAMEVM[], float64 meanRms256QAMEVM[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSEVM | [out] | float64[] | This parameter returns the array of mean values of RMS EVMs calculated on the PDSCH data symbols over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRMSQPSKEVM | [out] | float64[] | This parameter returns the array of mean values of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRms16QAMEVM | [out] | float64[] | This parameter returns the array of mean values of RMS EVMs calculated on all 16 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRms64QAMEVM | [out] | float64[] | This parameter returns the array of mean values of RMS EVMs calculated on all 64 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| meanRms256QAMEVM | [out] | float64[] | This parameter returns the array of mean values of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length attribute. When you set the ModAcc EVM Unit attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaf4bfb88aadbc814d7279a2d81ede07ed.html language=enus -->
## TOPIC 00235: RFmxLTE_ModAccFetchCSRSEVMArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaf4bfb88aadbc814d7279a2d81ede07ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaf4bfb88aadbc814d7279a2d81ede07ed.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of CSRS EVMs for all the component carriers within the subblock. Syntaxint32 __stdcall RFmxLTE_ModAccFetchCSRSEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSCSRSEVM[], int32 arraySize, int32 *actualArraySize)RemarksUse "subblock<

### RFmxLTE_ModAccFetchCSRSEVMArray

Fetches the array of CSRS EVMs for all the component carriers within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchCSRSEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRMSCSRSEVM[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSCSRSEVM | [out] | float64[] | This parameter returns the array of mean values of RMS EVMs calculated on Reference Signal (RS) resource elements over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to Percentage, the measurement is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaf51ed44b0ed4d5ce652872a497d4ef9e.html language=enus -->
## TOPIC 00236: RFmxLTE_ModAccFetchPDSCH1024QAMEVMArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaf51ed44b0ed4d5ce652872a497d4ef9e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaf51ed44b0ed4d5ce652872a497d4ef9e.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of physical downlink shared channel (PDSCH) 1024QAM EVMs for all the component carriers within the subblock. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRms1024QAMEVM[], int32 a

### RFmxLTE_ModAccFetchPDSCH1024QAMEVMArray

Fetches an array of physical downlink shared channel (PDSCH) 1024QAM EVMs for all the component carriers within the subblock.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 meanRms1024QAMEVM[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRms1024QAMEVM | [out] | float64[] | This parameter returns an array of mean values of the calculated RMS EVMs on all 1024QAM modulated PDSCH resource blocks over the slots specified by the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH attribute. When you set the RFMXLTE_ATTR_MODACC_EVM_UNIT attribute to Percentage, the result is returned in percentage. When you set the ModAcc EVM Unit attribute to dB, the measurement is returned in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gafbfaf436645612d90a209498e34a8d60.html language=enus -->
## TOPIC 00237: RFmxLTE_ModAccFetchMaximumEVMPerSubcarrierTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gafbfaf436645612d90a209498e34a8d60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gafbfaf436645612d90a209498e34a8d60.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value of an EVM for each allocated subcarrier computed across all the symbols within the value of the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH. Syntaxint32 __stdcall RFmxLTE_ModAccFetchMaximumEVMPerSubcarrierTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 time

### RFmxLTE_ModAccFetchMaximumEVMPerSubcarrierTrace

Returns the peak value of an EVM for each allocated subcarrier computed across all the symbols within the value of the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html).

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMPerSubcarrierTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 maximumEVMPerSubcarrier[], int32 arraySize, int32 *actualArraySize)

#### Remarks

The function result is valid only when you set the [RFMXLTE_ATTR_LINK_DIRECTION](group____root__ni_r_fmx_l_t_e__attributes_1gab9ef7530248a56a26813b9e087b7ca8b.html) attribute to **Uplink**.

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting subcarrier position corresponding to the RB offset of the signal being measured. |
| dx | [out] | float64 * | This parameter returns 1 as the value. |
| maximumEVMPerSubcarrier | [out] | float32[] | This parameter returns the peak value of an EVM for each allocated subcarrier computed across all the symbols within the ModAcc Meas Length. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaff445ed097c38148dc6072db575cfdd7.html language=enus -->
## TOPIC 00238: RFmxLTE_ModAccFetchPSSCHConstellationTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaff445ed097c38148dc6072db575cfdd7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__modacc_1gaff445ed097c38148dc6072db575cfdd7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recovered physical sidelink shared channel (PSSCH) constellation points. The constellation points of different slots in the RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH are concatenated. Syntaxint32 __stdcall RFmxLTE_ModAccFetchPSSCHConstellationTrace(niRFmxInstrHandle instrumentHandle, char s

### RFmxLTE_ModAccFetchPSSCHConstellationTrace

Returns the recovered physical sidelink shared channel (PSSCH) constellation points. The constellation points of different slots in the [RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH](group____root__ni_r_fmx_l_t_e__attributes__modacc_1ga4425255730fe33ec745c7dd17f7c8d60.html) are concatenated.

#### Syntax

int32 __stdcall RFmxLTE_ModAccFetchPSSCHConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle dataConstellation[], NIComplexSingle dmrsConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| dataConstellation | [out] | NIComplexSingle[] | This parameter returns the PSSCH data constellation trace. |
| dmrsConstellation | [out] | NIComplexSingle[] | This parameter returns the PSSCH demodulation reference signal (DMRS) constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1ga33d5dc25e88162d78c930a615d13a05d.html language=enus -->
## TOPIC 00239: RFmxLTE_PVTFetchMeasurement

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1ga33d5dc25e88162d78c930a615d13a05d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1ga33d5dc25e88162d78c930a615d13a05d.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement. Syntaxint32 __stdcall RFmxLTE_PVTFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *meanAbsoluteOffPowerBefore, float64 *meanAbsoluteOffPowerAfter, float64 *meanAbsoluteOnPower, float64 *burstWidth)

### RFmxLTE_PVTFetchMeasurement

Returns the measurement.

#### Syntax

int32 __stdcall RFmxLTE_PVTFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *meanAbsoluteOffPowerBefore, float64 *meanAbsoluteOffPowerAfter, float64 *meanAbsoluteOnPower, float64 *burstWidth)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| meanAbsoluteOffPowerBefore | [out] | float64 * | This parameter returns the mean power in the segment before the captured burst. The segment is defined as one subframe prior to the burst for the FDD mode and 10 SCFDMA symbols prior to the burst for the TDD mode. This value is expressed in dBm. |
| meanAbsoluteOffPowerAfter | [out] | float64 * | This parameter returns the mean power in the segment after the captured burst. This value is expressed in dBm.The segment is defined as one subframe long excluding a transient period of 20 μs at the beginning. This value is expressed in dBm. |
| meanAbsoluteOnPower | [out] | float64 * | This parameter returns the average power of the subframes within the captured burst, excluding a transient period of 20 μs at the beginning. This value is expressed in dBm. |
| burstWidth | [out] | float64 * | This parameter returns the width of the captured burst. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1gaa1653df4091071d1658f35e436edc4c7.html language=enus -->
## TOPIC 00240: RFmxLTE_PVTFetchMeasurementArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1gaa1653df4091071d1658f35e436edc4c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1gaa1653df4091071d1658f35e436edc4c7.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement array. Syntaxint32 __stdcall RFmxLTE_PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 meanAbsoluteOffPowerBefore[], float64 meanAbsoluteOffPowerAfter[], float64 meanAbsoluteOnPower[], float

### RFmxLTE_PVTFetchMeasurementArray

Returns the measurement array.

#### Syntax

int32 __stdcall RFmxLTE_PVTFetchMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 meanAbsoluteOffPowerBefore[], float64 meanAbsoluteOffPowerAfter[], float64 meanAbsoluteOnPower[], float64 burstWidth[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read this result.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| meanAbsoluteOffPowerBefore | [out] | float64[] | This parameter returns the array of the mean power in the segment before the captured burst. The segment is defined as one subframe prior to the burst for the FDD mode and 10 SCFDMA symbols prior to the burst for the TDD mode. This value is expressed in dBm. |
| meanAbsoluteOffPowerAfter | [out] | float64[] | This parameter returns the array of the mean power in the segment after the captured burst. This value is expressed in dBm.The segment is defined as one subframe long excluding a transient period of 20 μs at the beginning. |
| meanAbsoluteOnPower | [out] | float64[] | This parameter returns the array of the average power of the subframes within the captured burst, excluding a transient period of 20 μs at the beginning. This value is expressed in dBm. |
| burstWidth | [out] | float64[] | This parameter returns the array of the width of the captured burst. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1gaef747a945e299623a0fe80d7bf4e9981.html language=enus -->
## TOPIC 00241: RFmxLTE_PVTFetchSignalPowerTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1gaef747a945e299623a0fe80d7bf4e9981.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__pvt_1gaef747a945e299623a0fe80d7bf4e9981.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instantaneous signal power trace along with absolute limit for each segment in the trace as specified by section 6.5.2.4.5 of the 3GPP 36.521. This value is expressed in dBm. Syntaxint32 __stdcall RFmxLTE_PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxLTE_PVTFetchSignalPowerTrace

Returns the instantaneous signal power trace along with absolute limit for each segment in the trace as specified by section 6.5.2.4.5 of the *3GPP 36.521*. This value is expressed in dBm.

#### Syntax

int32 __stdcall RFmxLTE_PVTFetchSignalPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 signalPower[], float32 absoluteLimit[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0".Example:"subblock0/carrier0""signal::sig1/subblock0/carrier0""result::r1/subblock0/carrier0""signal::sig1/result::r1/subblock0/carrier0"You can use the RFmxLTE_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns start time of the signal. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the time bin spacing. This value is expressed in seconds. |
| signalPower | [out] | float32[] | This parameter returns the instantaneous signal power trace. This value is expressed in dBm. |
| absoluteLimit | [out] | float32[] | This parameter returns the instantaneous signal power trace. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__sem.html language=enus -->
## TOPIC 00242: SEM

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__sem.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxLTE_SEMFetchComponentCarrierMeasurementReturns the absolute power and relative power measured in the component carrier. The relative power is relative to subblock power. RFmxLTE_SEMFetchComponentCarrierMeasurementArrayReturns an array of the absolute powers

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_SEMFetchComponentCarrierMeasurement | Returns the absolute power and relative power measured in the component carrier. The relative power is relative to subblock power. |
| RFmxLTE_SEMFetchComponentCarrierMeasurementArray | Returns an array of the absolute powers and relative powers measured in the component carriers. The relative power is relative to subblock power. |
| RFmxLTE_SEMFetchLowerOffsetMargin | Returns the measurement status, margin, frequency at margin, and the absolute and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power. |
| RFmxLTE_SEMFetchLowerOffsetMarginArray | Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for lower offset segments. The relative power is relative to the total aggregated power. |
| RFmxLTE_SEMFetchLowerOffsetPower | Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. |
| RFmxLTE_SEMFetchLowerOffsetPowerArray | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. |
| RFmxLTE_SEMFetchMeasurementStatus | Returns the overall measurement status based on the standard mask type that you configure. |
| RFmxLTE_SEMFetchSpectrum | Fetches the spectrum used for the SEM measurement. |
| RFmxLTE_SEMFetchSubblockMeasurement | Returns the power, integration bandwidth and center frequency of the subblock. |
| RFmxLTE_SEMFetchTotalAggregatedPower | Returns the sum of powers of all subblocks. |
| RFmxLTE_SEMFetchUpperOffsetMargin | Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power. |
| RFmxLTE_SEMFetchUpperOffsetMarginArray | Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power. |
| RFmxLTE_SEMFetchUpperOffsetPower | Returns the total absolute and relative powers, peak, absolute, and relative powers, and frequency at peak absolute power of upper offset segment. The relative power is relative to total aggregated power. |
| RFmxLTE_SEMFetchUpperOffsetPowerArray | Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1ga88d9014bc081b6402135e54ccd7307de.html language=enus -->
## TOPIC 00243: RFmxLTE_SEMFetchTotalAggregatedPower

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1ga88d9014bc081b6402135e54ccd7307de.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1ga88d9014bc081b6402135e54ccd7307de.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers of all subblocks. Syntaxint32 __stdcall RFmxLTE_SEMFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter s

### RFmxLTE_SEMFetchTotalAggregatedPower

Returns the sum of powers of all subblocks.

#### Syntax

int32 __stdcall RFmxLTE_SEMFetchTotalAggregatedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAggregatedPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalAggregatedPower | [out] | float64 * | This parameter returns the sum of powers of all the frequency bins over the integration bandwidth of subblock. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power in the subblock gaps.When you set the RFMXLTE_ATTR_ACP_POWER_UNITS attribute to dBm, the parameter returns the total integrated power in dBm of all the active carriers measured. When you set the ACP Pwr Units attribute to dBm/Hz, the parameter returns the power spectral density in dBm/Hz based on the power in all the active carriers measured. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gabd4dd45ff99b357577f524c09ecdd7fa.html language=enus -->
## TOPIC 00244: RFmxLTE_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gabd4dd45ff99b357577f524c09ecdd7fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gabd4dd45ff99b357577f524c09ecdd7fa.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power. Syntaxint32 __stdcall RFmxLTE_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle,

### RFmxLTE_SEMFetchUpperOffsetMarginArray

Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power.

#### Syntax

int32 __stdcall RFmxLTE_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64[] | This parameter returns the array of margins from the standard defined absolute limit mask for upper offset. The margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequency at which the margin occurs in the upper offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurs in the upper (positive) offset segment relative to the value returned by the RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gac19efc1a51d29f7b1b901d90110f412b.html language=enus -->
## TOPIC 00245: RFmxLTE_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gac19efc1a51d29f7b1b901d90110f412b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gac19efc1a51d29f7b1b901d90110f412b.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power. Syntaxint32 __stdcall RFmxLTE_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instr

### RFmxLTE_SEMFetchLowerOffsetPowerArray

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power.

#### Syntax

int32 __stdcall RFmxLTE_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns the array of lower (negative) offset segment powers. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns the array of powers in the lower (negative) offset segment relative to the value returned by the RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| absolutePeakPower | [out] | float64[] | This parameter returns the array of peak powers in the lower (negative) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| peakFrequency | [out] | float64[] | This parameter returns the array of frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| relativePeakPower | [out] | float64[] | This parameter returns the array of peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr attribute. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gaf8d365c080aa759a38497ffd96103a3e.html language=enus -->
## TOPIC 00246: RFmxLTE_SEMFetchUpperOffsetMargin

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gaf8d365c080aa759a38497ffd96103a3e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__sem_1gaf8d365c080aa759a38497ffd96103a3e.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power. Syntaxint32 __stdcall RFmxLTE_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxLTE_SEMFetchUpperOffsetMargin

Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power.

#### Syntax

int32 __stdcall RFmxLTE_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read results from this function.

Refer to the [LTE Uplink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-uplink-spectral-emission-mask.html) and [LTE Downlink Spectral Emission Mask](https://www.ni.com/docs/en-US/bundle/rfmx-lte/page/lte-downlink-spectral-emission-mask.html) topics for more information.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"subblock0/offset0""signal::sig1/subblock0/offset0""signal::sig1/result::r1/subblock0/offset0""result::r1/subblock0/offset0"You can use the RFmxLTE_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the measurement status indicating whether the power before and after the burst is within the standard defined limit.NameValueDescriptionRFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64 * | This parameter returns the margin from the standard defined absolute limit mask for upper offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurs in the upper offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurs in the upper (positive) offset segment relative to the value returned by the RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER attribute. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__txp_1ga543ab8173eab4ee6e66578574432c5e2.html language=enus -->
## TOPIC 00247: RFmxLTE_TXPFetchMeasurement

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__txp_1ga543ab8173eab4ee6e66578574432c5e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__txp_1ga543ab8173eab4ee6e66578574432c5e2.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power and peak power of the the signal over which power measurments are performed. Syntaxint32 __stdcall RFmxLTE_TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averagePowerMean, float64 *peakPowerMaximum)RemarksUse "subblo

### RFmxLTE_TXPFetchMeasurement

Fetches the average power and peak power of the the signal over which power measurments are performed.

#### Syntax

int32 __stdcall RFmxLTE_TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averagePowerMean, float64 *peakPowerMaximum)

#### Remarks

Use "subblock<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0".Example:"subblock0""signal::sig1/subblock0""result::r1/subblock0""signal::sig1/result::r1/subblock0"You can use the RFmxLTE_BuildSubblockString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| averagePowerMean | [out] | float64 * | This parameter returns the average power of the the signal over which power measurments are performed. This value is expressed in dBm. |
| peakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the the signal over which power measurments are performed. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__fetch__txp_1gaad11d769633ede255e28fd7b3de651f6.html language=enus -->
## TOPIC 00248: RFmxLTE_TXPFetchPowerTrace

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__fetch__txp_1gaad11d769633ede255e28fd7b3de651f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__fetch__txp_1gaad11d769633ede255e28fd7b3de651f6.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches power versus time trace. Syntaxint32 __stdcall RFmxLTE_TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]n

### RFmxLTE_TXPFetchPowerTrace

Fetches power versus time trace.

#### Syntax

int32 __stdcall RFmxLTE_TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxLTE_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| power | [out] | float32[] | This parameter returns the measured average power at each time instance, in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxLTE_GetError](group____root__ni_r_fmx_l_t_e__functions_1gac5a321c2c8a1d57e387698a0bc656853.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__select__measurement.html language=enus -->
## TOPIC 00249: Select Measurement

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__select__measurement.html
- document_id: `rfmxlte-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxLTE_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxLTE_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxlte-c-api-ref path=group____root__ni_r_fmx_l_t_e__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00250: Set and Get Attributes

- bundle_id: `rfmxlte-c-api-ref`
- source_path: `group____root__ni_r_fmx_l_t_e__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_l_t_e__functions__set__and__get__attributes.html
- document_id: `rfmxlte-c-api-ref`
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
