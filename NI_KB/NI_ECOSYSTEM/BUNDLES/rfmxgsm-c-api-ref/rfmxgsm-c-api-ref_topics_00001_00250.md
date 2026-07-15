# NI DOCUMENT BUNDLE: rfmxgsm-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxgsm-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes.html language=enus -->
## TOPIC 00001: Attributes

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedModAccORFSPVTTriggerGroup membersNameDescriptionRFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLEDSpecifies whether the measurement automatically detects the training sequence code (TSC). RFMXGSM_ATTR_BANDSpecifies the operation band. RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPESpecifies the method us

### Attributes

#### Groups

- Advanced
- ModAcc
- ORFS
- PVT
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED | Specifies whether the measurement automatically detects the training sequence code (TSC). |
| RFMXGSM_ATTR_BAND | Specifies the operation band. |
| RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE | Specifies the method used to synchronize the burst. |
| RFMXGSM_ATTR_BURST_TYPE | Specifies the burst type. |
| RFMXGSM_ATTR_CENTER_FREQUENCY | Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| RFMXGSM_ATTR_EXTERNAL_ATTENUATION | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| RFMXGSM_ATTR_HB_FILTER_WIDTH | Specifies the filter width when you set the RFMXGSM_ATTR_BURST_TYPE attribute to HB. |
| RFMXGSM_ATTR_LINK_DIRECTION | Specifies the source of the signal to be measured. |
| RFMXGSM_ATTR_MODULATION_TYPE | Specifies the modulation scheme used for the signal. |
| RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS | Specifies the number of time slots to be measured. |
| RFMXGSM_ATTR_POWER_CONTROL_LEVEL | Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. |
| RFMXGSM_ATTR_REFERENCE_LEVEL | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
| RFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOM | Specifies the margin RFmx adds to the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| RFMXGSM_ATTR_RESULT_FETCH_TIMEOUT | Specifies the time to wait before results are available in the RFmxGSM Attribute. This value is expressed in seconds. |
| RFMXGSM_ATTR_SELECTED_PORTS | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| RFMXGSM_ATTR_SIGNAL_STRUCTURE | Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the RFMXGSM_ATTR_TRIGGER_TYPE to IQ Power Edge and None, respectively. |
| RFMXGSM_ATTR_TIMING_ADVANCE | Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. |
| RFMXGSM_ATTR_TSC | Specifies the training sequence code (TSC) to use. This attribute is applicable only when you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to TSC and the RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED attribute to False. For access burst TSC0, TSC1, and TSC2 are applicable. |

#### Attachments

None

Parent topic:

niRFmxGSM.h

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga0c985553813f235ed45cfa7dac1e0c24.html language=enus -->
## TOPIC 00002: RFMXGSM_ATTR_TSC

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga0c985553813f235ed45cfa7dac1e0c24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga0c985553813f235ed45cfa7dac1e0c24.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the training sequence code (TSC) to use. This attribute is applicable only when you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to TSC and the RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED attribute to False. For access burst TSC0, TSC1, and TSC2 are applicable. SyntaxRFMXGSM_ATTR_

### RFMXGSM_ATTR_TSC

Specifies the training sequence code (TSC) to use. This attribute is applicable only when you set the [RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE](group____root__ni_r_fmx_g_s_m__attributes_1ga6b9444dca24a6c6407eccb31c18a70a7.html) attribute to **TSC** and the [RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED](group____root__ni_r_fmx_g_s_m__attributes_1ga7c5bf22fb4db12fd3b6f043f08a0a41d.html) attribute to **False**. For access burst **TSC0**, **TSC1**, and **TSC2** are applicable.

#### Syntax

RFMXGSM_ATTR_TSC

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194324 | int32 | Read/Write | Slot |

#### Remarks

Use "slot<n>" as the selector string to configure or read this attribute.

The default value is **TSC0**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_TSC0 | 0 (0x0) | The measurement uses training sequence code 0. |
| RFMXGSM_VAL_TSC1 | 1 (0x1) | The measurement uses training sequence code 1. |
| RFMXGSM_VAL_TSC2 | 2 (0x2) | The measurement uses training sequence code 2. |
| RFMXGSM_VAL_TSC3 | 3 (0x3) | The measurement uses training sequence code 3. |
| RFMXGSM_VAL_TSC4 | 4 (0x4) | The measurement uses training sequence code 4. |
| RFMXGSM_VAL_TSC5 | 5 (0x5) | The measurement uses training sequence code 5. |
| RFMXGSM_VAL_TSC6 | 6 (0x6) | The measurement uses training sequence code 6. |
| RFMXGSM_VAL_TSC7 | 7 (0x7) | The measurement uses training sequence code 7. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga223894ff269f00e623c7f2c242b7d4d6.html language=enus -->
## TOPIC 00003: RFMXGSM_ATTR_REFERENCE_LEVEL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga223894ff269f00e623c7f2c242b7d4d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga223894ff269f00e623c7f2c242b7d4d6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V[pk-pk] for baseband devices. SyntaxRFMXGSM_ATTR_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To4194306float64Read/WriteN/ARemarks You do not need

### RFMXGSM_ATTR_REFERENCE_LEVEL

Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

#### Syntax

RFMXGSM_ATTR_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194306 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga30a2a0a35d448053ad3c04a09d59f539.html language=enus -->
## TOPIC 00004: RFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga30a2a0a35d448053ad3c04a09d59f539.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga30a2a0a35d448053ad3c04a09d59f539.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin RFmx adds to the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxRFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOMNumeric ValueData TypeAccessApplies To4198396float64Read/WriteN/ARemar

### RFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOM

Specifies the margin RFmx adds to the [RFMXGSM_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_g_s_m__attributes_1ga223894ff269f00e623c7f2c242b7d4d6.html) attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

RFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198396 | float64 | Read/Write | N/A |

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

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga4c0f6bf3e1bd54696157e942143eca47.html language=enus -->
## TOPIC 00005: RFMXGSM_ATTR_MODULATION_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga4c0f6bf3e1bd54696157e942143eca47.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga4c0f6bf3e1bd54696157e942143eca47.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation scheme used for the signal. SyntaxRFMXGSM_ATTR_MODULATION_TYPENumeric ValueData TypeAccessApplies To4194320int32Read/WriteSlotRemarks Use "slot<n>" as the selector string to configure or read this attribute.The default value is 8PSK.NameValueDescriptionRFMXGSM_VAL_MODULATION

### RFMXGSM_ATTR_MODULATION_TYPE

Specifies the modulation scheme used for the signal.

#### Syntax

RFMXGSM_ATTR_MODULATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194320 | int32 | Read/Write | Slot |

#### Remarks

Use "slot<n>" as the selector string to configure or read this attribute.

The default value is **8PSK**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_MODULATION_TYPE_GMSK | 0 (0x0) | The modulation type is Gaussian minimum shift keying. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to NB or AB. |
| RFMXGSM_VAL_MODULATION_TYPE_8PSK | 1 (0x1) | The modulation type is 8-PSK. This value is valid only when you set the Burst Type attribute to NB. |
| RFMXGSM_VAL_MODULATION_TYPE_QPSK | 2 (0x2) | The modulation type is QPSK. This value is valid only when you set the Burst Type attribute to HB. |
| RFMXGSM_VAL_MODULATION_TYPE_16QAM | 3 (0x3) | The modulation type is 16-QAM. |
| RFMXGSM_VAL_MODULATION_TYPE_32QAM | 4 (0x4) | The modulation type is 32-QAM. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga4d347e6ced67c8d45e118925266d1edf.html language=enus -->
## TOPIC 00006: RFMXGSM_ATTR_BAND

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga4d347e6ced67c8d45e118925266d1edf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga4d347e6ced67c8d45e118925266d1edf.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operation band. SyntaxRFMXGSM_ATTR_BANDNumeric ValueData TypeAccessApplies To4194318int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the strin

### RFMXGSM_ATTR_BAND

Specifies the operation band.

#### Syntax

RFMXGSM_ATTR_BAND

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194318 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **PGSM**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_BAND_PGSM | 0 (0x0) | The operation band is Primary GSM in the 900 MHz band. |
| RFMXGSM_VAL_BAND_EGSM | 1 (0x1) | The operation band is Extended GSM in the 900 MHz band. |
| RFMXGSM_VAL_BAND_RGSM | 2 (0x2) | The operation band is Railway GSM in the 900 MHz band. |
| RFMXGSM_VAL_BAND_DCS1800 | 3 (0x3) | The operation band is GSM in the 1800 MHz band. |
| RFMXGSM_VAL_BAND_PCS1900 | 4 (0x4) | The operation band is GSM in the 1900 MHz band. |
| RFMXGSM_VAL_BAND_GSM450 | 5 (0x5) | The operation band is GSM in the 450 MHz band. |
| RFMXGSM_VAL_BAND_GSM480 | 6 (0x6) | The operation band is GSM in the 480 MHz band. |
| RFMXGSM_VAL_BAND_GSM850 | 7 (0x7) | The operation band is GSM in the 850 MHz band. |
| RFMXGSM_VAL_BAND_GSM750 | 8 (0x8) | The operation band is GSM in the 750 MHz band. |
| RFMXGSM_VAL_BAND_TGSM810 | 9 (0x9) | The operation band is terrestrial GSM in the 810 MHz band. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga518a3b2ec0898ddc36e5cd2bc1854bc8.html language=enus -->
## TOPIC 00007: RFMXGSM_ATTR_BURST_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga518a3b2ec0898ddc36e5cd2bc1854bc8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga518a3b2ec0898ddc36e5cd2bc1854bc8.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the burst type. SyntaxRFMXGSM_ATTR_BURST_TYPENumeric ValueData TypeAccessApplies To4194321int32Read/WriteSlotRemarks Use "slot<n>" as the selector string to configure or read this attribute.The default value is NB.NameValueDescriptionRFMXGSM_VAL_BURST_TYPE_NB0 (0x0)The burst type is Normal

### RFMXGSM_ATTR_BURST_TYPE

Specifies the burst type.

#### Syntax

RFMXGSM_ATTR_BURST_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194321 | int32 | Read/Write | Slot |

#### Remarks

Use "slot<n>" as the selector string to configure or read this attribute.

The default value is **NB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_BURST_TYPE_NB | 0 (0x0) | The burst type is Normal Burst. |
| RFMXGSM_VAL_BURST_TYPE_HB | 1 (0x1) | The burst type is Higher Symbol Rate Burst. |
| RFMXGSM_VAL_BURST_TYPE_AB | 2 (0x2) | The burst type is Access Burst. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga5bc92802201e4764cb626cb758031c26.html language=enus -->
## TOPIC 00008: RFMXGSM_ATTR_HB_FILTER_WIDTH

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga5bc92802201e4764cb626cb758031c26.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga5bc92802201e4764cb626cb758031c26.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the filter width when you set the RFMXGSM_ATTR_BURST_TYPE attribute to HB. SyntaxRFMXGSM_ATTR_HB_FILTER_WIDTHNumeric ValueData TypeAccessApplies To4194322int32Read/WriteSlotRemarks Use "slot<n>" as the selector string to configure or read this attribute.The default value is Narrow.NameValu

### RFMXGSM_ATTR_HB_FILTER_WIDTH

Specifies the filter width when you set the [RFMXGSM_ATTR_BURST_TYPE](group____root__ni_r_fmx_g_s_m__attributes_1ga518a3b2ec0898ddc36e5cd2bc1854bc8.html) attribute to **HB**.

#### Syntax

RFMXGSM_ATTR_HB_FILTER_WIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194322 | int32 | Read/Write | Slot |

#### Remarks

Use "slot<n>" as the selector string to configure or read this attribute.

The default value is **Narrow**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_HB_FILTER_WIDTH_NARROW | 0 (0x0) | The measurement uses a narrow filter. |
| RFMXGSM_VAL_HB_FILTER_WIDTH_WIDE | 1 (0x1) | The measurement uses a wide filter. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga6b9444dca24a6c6407eccb31c18a70a7.html language=enus -->
## TOPIC 00009: RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga6b9444dca24a6c6407eccb31c18a70a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga6b9444dca24a6c6407eccb31c18a70a7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used to synchronize the burst. SyntaxRFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPENumeric ValueData TypeAccessApplies To4194326int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE

Specifies the method used to synchronize the burst.

#### Syntax

RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194326 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **TSC**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_BURST_SYNC_TYPE_TSC | 0 (0x0) | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE | 1 (0x1) | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. |
| RFMXGSM_VAL_BURST_SYNC_TYPE_NONE | 2 (0x2) | Sets the T0 point to 273.23 microseconds after the trigger. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga6bd8613ce699d1d13226dd2473fc7c17.html language=enus -->
## TOPIC 00010: RFMXGSM_ATTR_SIGNAL_STRUCTURE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga6bd8613ce699d1d13226dd2473fc7c17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga6bd8613ce699d1d13226dd2473fc7c17.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the RFMXGSM_ATTR_TRIGGER_TYPE to IQ Power Edge and None, respectively. SyntaxRFMXGSM_ATTR_SIGNAL_STRUCTURENumeric ValueData TypeAccessApplies To4194327int32Read/WriteN/ARemarks You do not need to us

### RFMXGSM_ATTR_SIGNAL_STRUCTURE

Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the [RFMXGSM_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html) to **IQ Power Edge** and **None**, respectively.

#### Syntax

RFMXGSM_ATTR_SIGNAL_STRUCTURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194327 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Bursted**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_SIGNAL_STRUCTURE_BURSTED | 0 (0x0) | The signal is bursted. |
| RFMXGSM_VAL_SIGNAL_STRUCTURE_CONTINUOUS | 1 (0x1) | The signal is continuous. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga7c5bf22fb4db12fd3b6f043f08a0a41d.html language=enus -->
## TOPIC 00011: RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga7c5bf22fb4db12fd3b6f043f08a0a41d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga7c5bf22fb4db12fd3b6f043f08a0a41d.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement automatically detects the training sequence code (TSC). SyntaxRFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLEDNumeric ValueData TypeAccessApplies To4194323int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default s

### RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED

Specifies whether the measurement automatically detects the training sequence code (TSC).

#### Syntax

RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194323 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE | 0 (0x0) | The measurement uses the value that you configure using the RFMXGSM_ATTR_TSC attribute. |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE | 1 (0x1) | The measurement detects the TSC in the burst. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga893b33fad308b7c6b198ca977a7310c3.html language=enus -->
## TOPIC 00012: RFMXGSM_ATTR_POWER_CONTROL_LEVEL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga893b33fad308b7c6b198ca977a7310c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga893b33fad308b7c6b198ca977a7310c3.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. SyntaxRFMXGSM_ATTR_POWER_CONTROL_LEVELNumeric ValueData TypeAccessApplies To4194325int32Read/WriteSlotRemarks Use "slot<n>" as the selector string to confi

### RFMXGSM_ATTR_POWER_CONTROL_LEVEL

Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the *3GPP TS 45.005 v8.0.0 specifications*.

#### Syntax

RFMXGSM_ATTR_POWER_CONTROL_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194325 | int32 | Read/Write | Slot |

#### Remarks

Use "slot<n>" as the selector string to configure or read this attribute.

The default value is 0. Valid values are 0 to 31, inclusive.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1ga97308745a6f99989854d748d4d5e06c9.html language=enus -->
## TOPIC 00013: RFMXGSM_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1ga97308745a6f99989854d748d4d5e06c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1ga97308745a6f99989854d748d4d5e06c9.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxGSM Attribute. This value is expressed in seconds. SyntaxRFMXGSM_ATTR_RESULT_FETCH_TIMEOUTNumeric ValueData TypeAccessApplies To4243456float64Read/WriteN/ARemarks Set this value to a time longer than expected for fetching the measure

### RFMXGSM_ATTR_RESULT_FETCH_TIMEOUT

Specifies the time to wait before results are available in the RFmxGSM Attribute. This value is expressed in seconds.

#### Syntax

RFMXGSM_ATTR_RESULT_FETCH_TIMEOUT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4243456 | float64 | Read/Write | N/A |

#### Remarks

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxGSM Attribute waits until the measurement is complete.

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1gab140f0bdf3a41715ca27b8f149e4a05d.html language=enus -->
## TOPIC 00014: RFMXGSM_ATTR_LINK_DIRECTION

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1gab140f0bdf3a41715ca27b8f149e4a05d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1gab140f0bdf3a41715ca27b8f149e4a05d.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the signal to be measured. SyntaxRFMXGSM_ATTR_LINK_DIRECTIONNumeric ValueData TypeAccessApplies To4194317int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to the Selector String topic

### RFMXGSM_ATTR_LINK_DIRECTION

Specifies the source of the signal to be measured.

#### Syntax

RFMXGSM_ATTR_LINK_DIRECTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194317 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Uplink**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK | 0 (0x0) | The source is a base transceiver station. |
| RFMXGSM_VAL_LINK_DIRECTION_UPLINK | 1 (0x1) | The source is a mobile station. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1gab8916cd4cd54565a67082f7629e9b41b.html language=enus -->
## TOPIC 00015: RFMXGSM_ATTR_SELECTED_PORTS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1gab8916cd4cd54565a67082f7629e9b41b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1gab8916cd4cd54565a67082f7629e9b41b.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. SyntaxRFMXGSM_ATTR_SELECTED_PORTSNumeric ValueData TypeAccessApplies To4198397char[]Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXGSM_ATTR_SELECTED_PORTS

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr_GetAvailablePorts](/csh?context=rfmxinstr_rfmxinstrcref_function_get_available_ports) function to get the valid port names.

#### Syntax

RFMXGSM_ATTR_SELECTED_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198397 | char[] | Read/Write | N/A |

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

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1gac9cd2ddaf7f78bd343f0c111e69159bf.html language=enus -->
## TOPIC 00016: RFMXGSM_ATTR_TIMING_ADVANCE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1gac9cd2ddaf7f78bd343f0c111e69159bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1gac9cd2ddaf7f78bd343f0c111e69159bf.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst. SyntaxRFMXGSM_ATTR_TIMING_ADVANCENumeric ValueData TypeAccessApplies To4194328int32Read/WriteSlotRemarks You do not need to use a Selector String to configure or read this attribute for the defa

### RFMXGSM_ATTR_TIMING_ADVANCE

Specifies the timing advance value as specified in the 3GPP TS 45.010 specification for GSM access burst.

#### Syntax

RFMXGSM_ATTR_TIMING_ADVANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194328 | int32 | Read/Write | Slot |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1gaef9f666f3c849e727ac6c9f60baa133c.html language=enus -->
## TOPIC 00017: RFMXGSM_ATTR_CENTER_FREQUENCY

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1gaef9f666f3c849e727ac6c9f60baa133c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1gaef9f666f3c849e727ac6c9f60baa133c.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. SyntaxRFMXGSM_ATTR_CENTER_FREQUENCYNumeric ValueData TypeAccessApplies To4194305float64Read/WriteN/ARemarks You do not need to use a Selector String to conf

### RFMXGSM_ATTR_CENTER_FREQUENCY

Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

#### Syntax

RFMXGSM_ATTR_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194305 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1gafbf850a558ab937d73dfec8e323c63b5.html language=enus -->
## TOPIC 00018: RFMXGSM_ATTR_EXTERNAL_ATTENUATION

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1gafbf850a558ab937d73dfec8e323c63b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1gafbf850a558ab937d73dfec8e323c63b5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. SyntaxRFMXGSM_

### RFMXGSM_ATTR_EXTERNAL_ATTENUATION

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

#### Syntax

RFMXGSM_ATTR_EXTERNAL_ATTENUATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194307 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes_1gafc24c2235a8f97b2f4a44161b6d78ef8.html language=enus -->
## TOPIC 00019: RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes_1gafc24c2235a8f97b2f4a44161b6d78ef8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes_1gafc24c2235a8f97b2f4a44161b6d78ef8.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of time slots to be measured. SyntaxRFMXGSM_ATTR_NUMBER_OF_TIMESLOTSNumeric ValueData TypeAccessApplies To4194319int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to the Selector String t

### RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS

Specifies the number of time slots to be measured.

#### Syntax

RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194319 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__advanced.html language=enus -->
## TOPIC 00020: Advanced

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__advanced.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVELSpecifies the initial reference level the RFmxGSM_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGESpecifies the set of

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL | Specifies the initial reference level the RFmxGSM_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. |
| RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE | Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__advanced_1ga373b891375b525fbc3367334dc2a2a42.html language=enus -->
## TOPIC 00021: RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__advanced_1ga373b891375b525fbc3367334dc2a2a42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__advanced_1ga373b891375b525fbc3367334dc2a2a42.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of attributes that are considered by RFmx in the locked signal configuration state. SyntaxRFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGENumeric ValueData TypeAccessApplies To4247555int32Read/WriteN/ARemarks If your test system performs the same measurement at different selected ports, m

### RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE

Specifies the set of attributes that are considered by RFmx in the locked signal configuration state.

#### Syntax

RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4247555 | int32 | Read/Write | N/A |

#### Remarks

If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this attribute can help achieve faster measurements. When you set this attribute to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this attribute, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](https://www.ni.com/docs/en-US/bundle/rfmx-wcdma-prop/page/rfmxwcdmaprop/limitations.html) topic.

You can also use this attribute to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr attributes from a locked configuration.

NI recommends you use this attribute in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this attribute to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this attribute if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality attributes while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this attribute in the selector string input. You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED | 0 (0x0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr attributes or in personality attributes will be applied during RFmx Commit. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE | 1 (0x1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr attributes or personality attributes will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr attributes. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY | 2 (0x2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the RFMXGSM_ATTR_CENTER_FREQUENCY and RFMXGSM_ATTR_EXTERNAL_ATTENUATION attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL | 3 (0x3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the RFMXGSM_ATTR_REFERENCE_LEVEL attribute value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL | 4 (0x4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL | 5 (0x5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation attribute value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__advanced_1ga6541550042d6d954d53b917eb4b84f39.html language=enus -->
## TOPIC 00022: RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__advanced_1ga6541550042d6d954d53b917eb4b84f39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__advanced_1ga6541550042d6d954d53b917eb4b84f39.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial reference level the RFmxGSM_AutoLevel function uses to estimate the peak power of the input signal. This value is expressed in dBm. SyntaxRFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To4247552float64Read/WriteN/ARemarks You do not need to u

### RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

Specifies the initial reference level the [RFmxGSM_AutoLevel](group____root__ni_r_fmx_g_s_m__functions__configuration_1ga87296023c7b16287e9d8910d34b5fff5.html) function uses to estimate the peak power of the input signal. This value is expressed in dBm.

#### Syntax

RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4247552 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 30.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc.html language=enus -->
## TOPIC 00023: ModAcc

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingResultsGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLEDSpecifies whether to enable droop com

### ModAcc

#### Groups

- Averaging
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. |
| RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED | Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. |
| RFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLED | Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. |
| RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| RFMXGSM_ATTR_MODACC_MEASUREMENT_OFFSET | Specifies the offset, relative to the trigger of the timeslot to be measured. |
| RFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga0894dbe6e58a3a810912018d7fa9a814.html language=enus -->
## TOPIC 00024: RFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga0894dbe6e58a3a810912018d7fa9a814.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga0894dbe6e58a3a810912018d7fa9a814.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the ModAcc measurement. SyntaxRFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To4198407int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of th

### RFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the ModAcc measurement.

#### Syntax

RFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198407 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga30b6d9f8e3cc17c05032825e37b00642.html language=enus -->
## TOPIC 00025: RFMXGSM_ATTR_MODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga30b6d9f8e3cc17c05032825e37b00642.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga30b6d9f8e3cc17c05032825e37b00642.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset, relative to the trigger of the timeslot to be measured. SyntaxRFMXGSM_ATTR_MODACC_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To4198443int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instanc

### RFMXGSM_ATTR_MODACC_MEASUREMENT_OFFSET

Specifies the offset, relative to the trigger of the timeslot to be measured.

#### Syntax

RFMXGSM_ATTR_MODACC_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198443 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0, ([RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS](group____root__ni_r_fmx_g_s_m__attributes_1gafc24c2235a8f97b2f4a44161b6d78ef8.html) -1)].

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga329596c0c00f21d49dbc81d2a5a98419.html language=enus -->
## TOPIC 00026: RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga329596c0c00f21d49dbc81d2a5a98419.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga329596c0c00f21d49dbc81d2a5a98419.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxRFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVALNumeric ValueData TypeAccessApplies To4198442int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribut

### RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL

Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198442 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default Value is **'Number of Timeslots'**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_MODACC_MEASUREMENT_INTERVAL_NUMBER_OF_TIMESLOTS | 0 (0x0) | The measurement includes all timeslots defined by the RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS attribute. |
| RFMXGSM_VAL_MODACC_MEASUREMENT_INTERVAL_TIMESLOT_AT_OFFSET | 1 (0x1) | The measurement is performed only on the timeslot specified by the RFMXGSM_ATTR_MODACC_MEASUREMENT_OFFSET attribute. This attribute is applicable only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge or Digital Edge . |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga4ea154d20c22a7eafd400623575db8e5.html language=enus -->
## TOPIC 00027: RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga4ea154d20c22a7eafd400623575db8e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga4ea154d20c22a7eafd400623575db8e5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. SyntaxRFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLEDNumeric ValueData TypeA

### RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED

Specifies whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results.

#### Syntax

RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198405 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables power droop compensation in the EVM measurement. |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables power droop compensation in the EVM measurement. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc_1gad5bd85bdf69fd49e156b3f7106d7d688.html language=enus -->
## TOPIC 00028: RFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc_1gad5bd85bdf69fd49e156b3f7106d7d688.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc_1gad5bd85bdf69fd49e156b3f7106d7d688.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal. SyntaxRFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To4198400int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the defau

### RFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLED

Specifies whether to enable modulation accuracy (ModAcc) measurements on the acquired signal.

#### Syntax

RFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198400 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc_1gaf7b88a25674e1d2832fef27f00669df7.html language=enus -->
## TOPIC 00029: RFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc_1gaf7b88a25674e1d2832fef27f00669df7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc_1gaf7b88a25674e1d2832fef27f00669df7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. SyntaxRFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To4198406int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or

### RFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

#### Syntax

RFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198406 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging.html language=enus -->
## TOPIC 00030: Averaging

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED attribute to True. RFMXGSM_ATTR_MODACC_AVERAGING_ENABLEDSpecifies whether to enable averaging for the modulation acc

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED attribute to True. |
| RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED | Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging_1gad6bf0dcace4b152b002b6306c374869f.html language=enus -->
## TOPIC 00031: RFMXGSM_ATTR_MODACC_AVERAGING_COUNT

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging_1gad6bf0dcace4b152b002b6306c374869f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging_1gad6bf0dcace4b152b002b6306c374869f.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED attribute to True. SyntaxRFMXGSM_ATTR_MODACC_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To4198404int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or r

### RFMXGSM_ATTR_MODACC_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging_1gaec560168547b75ddfec0934d27010a16.html) attribute to **True**.

#### Syntax

RFMXGSM_ATTR_MODACC_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198404 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging_1gaec560168547b75ddfec0934d27010a16.html language=enus -->
## TOPIC 00032: RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging_1gaec560168547b75ddfec0934d27010a16.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__averaging_1gaec560168547b75ddfec0934d27010a16.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement. SyntaxRFMXGSM_ATTR_MODACC_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To4198402int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signa

### RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED

Specifies whether to enable averaging for the modulation accuracy (ModAcc) measurement.

#### Syntax

RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198402 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement is averaged over multiple acquisitions. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results.html language=enus -->
## TOPIC 00033: Results

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsEVMIQ Gain ImbalanceIQ Origin OffsetPFERGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSCReturns the detected training sequence code (TSC) if you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to TSC. AttachmentsNone

### Results

#### Groups

- EVM
- IQ Gain Imbalance
- IQ Origin Offset
- PFER

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC | Returns the detected training sequence code (TSC) if you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to TSC. |

#### Attachments

None

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results_1ga352fd07dedd21f88f13662d11ebf7eea.html language=enus -->
## TOPIC 00034: RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results_1ga352fd07dedd21f88f13662d11ebf7eea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results_1ga352fd07dedd21f88f13662d11ebf7eea.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected training sequence code (TSC) if you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to TSC. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSCNumeric ValueData TypeAccessApplies To4198433int32Read-OnlySlotRemarks Use "slot<n>" as the selector string to read this result.Whe

### RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC

Returns the detected training sequence code (TSC) if you set the [RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE](group____root__ni_r_fmx_g_s_m__attributes_1ga6b9444dca24a6c6407eccb31c18a70a7.html) attribute to **TSC**.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198433 | int32 | Read-Only | Slot |

#### Remarks

Use "slot<n>" as the selector string to read this result.

When the [RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL](group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga329596c0c00f21d49dbc81d2a5a98419.html) attribute is set to **Timeslot at Offset**, Detected TSC array has one element and the Detected TSC is returned at index 0.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN | -1 (-0x1) | The synchronization is not found, and measurements correspond to best estimate of synchronization. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 | 0 (0x0) | The detected TSC is TSC0. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 | 1 (0x1) | The detected TSC is TSC1. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 | 2 (0x2) | The detected TSC is TSC2. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 | 3 (0x3) | The detected TSC is TSC3. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 | 4 (0x4) | The detected TSC is TSC4. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 | 5 (0x5) | The detected TSC is TSC5. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 | 6 (0x6) | The detected TSC is TSC6. |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 | 7 (0x7) | The detected TSC is TSC7. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm.html language=enus -->
## TOPIC 00035: EVM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAmplitude DroopFrequency ErrorMagnitude ErrorPhase ErrorGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVMReturns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The attribute returns

### EVM

#### Groups

- Amplitude Droop
- Frequency Error
- Magnitude Error
- Phase Error

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM | Returns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM | Returns the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM | Returns the maximum of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_EVM | Returns the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVM | Returns the mean of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL | Returns the symbol number in the useful portion of the burst corresponding to RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM result. The attribute returns this result for ModAcc EDGE/EGPRS measurements. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga0bc325ecbf89a8c79408fb3186606735.html language=enus -->
## TOPIC 00036: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga0bc325ecbf89a8c79408fb3186606735.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga0bc325ecbf89a8c79408fb3186606735.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVMNumeric ValueData TypeAccessApplies To4198409float64Read-OnlyN/ARema

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM

Returns the maximum of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198409 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga3d26a786c0afdb1b8f346d4fb59f2578.html language=enus -->
## TOPIC 00037: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga3d26a786c0afdb1b8f346d4fb59f2578.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga3d26a786c0afdb1b8f346d4fb59f2578.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVMNumeric ValueData TypeAccessApplies To4198408float64Read-OnlyN/ARemarks Yo

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVM

Returns the mean of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198408 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga4588f5028868383faf0d7f3133a10cfe.html language=enus -->
## TOPIC 00038: RFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga4588f5028868383faf0d7f3133a10cfe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga4588f5028868383faf0d7f3133a10cfe.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol number in the useful portion of the burst corresponding to RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM result. The attribute returns this result for ModAcc EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOLNumeric ValueData TypeAccessApplies To4198

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL

Returns the symbol number in the useful portion of the burst corresponding to [RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM](group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga572fa8dfa63bef18a12e1e7588bf270d.html) result. The attribute returns this result for ModAcc EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198413 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga572fa8dfa63bef18a12e1e7588bf270d.html language=enus -->
## TOPIC 00039: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga572fa8dfa63bef18a12e1e7588bf270d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga572fa8dfa63bef18a12e1e7588bf270d.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVMNumeric ValueData TypeAccessApplies To4198411float64Read-OnlyN/AR

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM

Returns the maximum of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198411 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga5a319a6c78d3a93756c549320aa61319.html language=enus -->
## TOPIC 00040: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_EVM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga5a319a6c78d3a93756c549320aa61319.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1ga5a319a6c78d3a93756c549320aa61319.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_EVMNumeric ValueData TypeAccessApplies To4198410float64Read-OnlyN/ARemarks

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_EVM

Returns the mean of the peak EVM values over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198410 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1gac3fbc5ee849efdd35c10fbf6830938f5.html language=enus -->
## TOPIC 00041: RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1gac3fbc5ee849efdd35c10fbf6830938f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm_1gac3fbc5ee849efdd35c10fbf6830938f5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVMNumeric ValueData TypeAccessApplies To41984

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM

Returns the EVM value at which no more than 5% of the symbols have an EVM exceeding this value. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198412 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop.html language=enus -->
## TOPIC 00042: Amplitude Droop

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOPReturns the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements. RFMXGSM_ATTR_MODACC_RE

### Amplitude Droop

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOP | Returns the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP | Returns the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements. |

#### Attachments

None

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop_1ga103d10e12e1ce7bfc928407bb0a20b57.html language=enus -->
## TOPIC 00043: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOP

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop_1ga103d10e12e1ce7bfc928407bb0a20b57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop_1ga103d10e12e1ce7bfc928407bb0a20b57.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOPNumeric ValueData TypeAccessApplies To4198421float64Re

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOP

Returns the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198421 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Amplitude Droop

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop_1gac212f2ea91afbc78a2559236d8095dd8.html language=enus -->
## TOPIC 00044: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop_1gac212f2ea91afbc78a2559236d8095dd8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__amplitude__droop_1gac212f2ea91afbc78a2559236d8095dd8.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOPNumeric ValueData TypeAccessApplies To4198420float64Read-Onl

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP

Returns the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198420 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Amplitude Droop

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error.html language=enus -->
## TOPIC 00045: Frequency Error

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERRORReturns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements. RFMXGSM_ATTR_MODACC_RESULTS_E

### Frequency Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERROR | Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR | Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements. |

#### Attachments

None

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error_1ga151df2dd2ca9a8e17e65e50a64f3886e.html language=enus -->
## TOPIC 00046: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error_1ga151df2dd2ca9a8e17e65e50a64f3886e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error_1ga151df2dd2ca9a8e17e65e50a64f3886e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To4198419float64Read-Only

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERROR

Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198419 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Frequency Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error_1ga5d78ffe785e3fd9e1b7baf29e1b0c42c.html language=enus -->
## TOPIC 00047: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error_1ga5d78ffe785e3fd9e1b7baf29e1b0c42c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__frequency__error_1ga5d78ffe785e3fd9e1b7baf29e1b0c42c.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To4198418float64Read-OnlyN/ARem

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR

Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198418 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Frequency Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error.html language=enus -->
## TOPIC 00048: Magnitude Error

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_MAGNITUDE_ERRORReturns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAc

### Magnitude Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_MAGNITUDE_ERROR | Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_MAGNITUDE_ERROR | Returns the maximum of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_MAGNITUDE_ERROR | Returns the maximum of peak magnitude error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR | Returns the mean of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_MAGNITUDE_ERROR | Returns the mean of peak magnitude error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. |

#### Attachments

None

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga113287c084917f7f9a6d4629cfb43745.html language=enus -->
## TOPIC 00049: RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_MAGNITUDE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga113287c084917f7f9a6d4629cfb43745.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga113287c084917f7f9a6d4629cfb43745.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. SyntaxRFMXGSM_ATTR_MODACC_RESULT

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_MAGNITUDE_ERROR

Returns the measured magnitude error value multiplied by 100, at which, no more than 5 percent of the symbols have magnitude error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198437 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Magnitude Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga1702cf8553a1af0569b5fcc30765f00f.html language=enus -->
## TOPIC 00050: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_MAGNITUDE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga1702cf8553a1af0569b5fcc30765f00f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga1702cf8553a1af0569b5fcc30765f00f.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of peak magnitude error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To41

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_MAGNITUDE_ERROR

Returns the mean of peak magnitude error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198435 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Magnitude Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga31218ea926f3f8902e096b8283064296.html language=enus -->
## TOPIC 00051: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_MAGNITUDE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga31218ea926f3f8902e096b8283064296.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga31218ea926f3f8902e096b8283064296.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To4198415flo

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_MAGNITUDE_ERROR

Returns the maximum of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198415 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Magnitude Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga6f7c7b421238d5193f1dfc92f668146b.html language=enus -->
## TOPIC 00052: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga6f7c7b421238d5193f1dfc92f668146b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1ga6f7c7b421238d5193f1dfc92f668146b.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplies To4198414float64Re

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR

Returns the mean of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198414 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Magnitude Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1gad82f6e80794dec86b58a52fa2e280e16.html language=enus -->
## TOPIC 00053: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_MAGNITUDE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1gad82f6e80794dec86b58a52fa2e280e16.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__magnitude__error_1gad82f6e80794dec86b58a52fa2e280e16.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of peak magnitude error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_MAGNITUDE_ERRORNumeric ValueData TypeAccessApplie

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_MAGNITUDE_ERROR

Returns the maximum of peak magnitude error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured as a percentage.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_MAGNITUDE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198436 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Magnitude Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error.html language=enus -->
## TOPIC 00054: Phase Error

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_PHASE_ERRORReturns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measuremen

### Phase Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_PHASE_ERROR | Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_PHASE_ERROR | Returns the maximum of peak phase error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR | Returns the maximum of the RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_PHASE_ERROR | Returns the mean of peak phase error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. |
| RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PHASE_ERROR | Returns the mean of RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for EDGE/EGPRS measurements. |

#### Attachments

None

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga177bd0d2f61f7d0e271dcc37de083b9a.html language=enus -->
## TOPIC 00055: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga177bd0d2f61f7d0e271dcc37de083b9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga177bd0d2f61f7d0e271dcc37de083b9a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of peak phase error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198438float64R

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_PHASE_ERROR

Returns the mean of peak phase error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198438 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. &gt;

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga1f06c3dc7e0735aaaedf7d8174970cd7.html language=enus -->
## TOPIC 00056: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga1f06c3dc7e0735aaaedf7d8174970cd7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga1f06c3dc7e0735aaaedf7d8174970cd7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198416float64Read-OnlyN/ARem

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PHASE_ERROR

Returns the mean of RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198416 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga6975107c301ca7866faaa07f32249b06.html language=enus -->
## TOPIC 00057: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga6975107c301ca7866faaa07f32249b06.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1ga6975107c301ca7866faaa07f32249b06.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for EDGE/EGPRS measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198417float64Read-

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR

Returns the maximum of the RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198417 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1gacb62452a07c74bf5436adc14a72fd23c.html language=enus -->
## TOPIC 00058: RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1gacb62452a07c74bf5436adc14a72fd23c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1gacb62452a07c74bf5436adc14a72fd23c.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PE

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_PHASE_ERROR

Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198440 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1gaf70594be72c977e96e56be1f379b32ea.html language=enus -->
## TOPIC 00059: RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1gaf70594be72c977e96e56be1f379b32ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__evm__phase__error_1gaf70594be72c977e96e56be1f379b32ea.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of peak phase error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198439fl

### RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_PHASE_ERROR

Returns the maximum of peak phase error values over all the measured time slots. This result is returned while performing ModAcc measurement on EDGE/EGPRS. This value is measured in degrees.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198439 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance.html language=enus -->
## TOPIC 00060: IQ Gain Imbalance

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCEReturns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. RF

### IQ Gain Imbalance

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE | Returns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE | Returns the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance_1ga334108d02996c8207ad1e3931ceb89bf.html language=enus -->
## TOPIC 00061: RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance_1ga334108d02996c8207ad1e3931ceb89bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance_1ga334108d02996c8207ad1e3931ceb89bf.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To41

### RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE

Returns the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198429 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

IQ Gain Imbalance

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance_1gadaa0395e26447be73e2b994df7a25f4a.html language=enus -->
## TOPIC 00062: RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance_1gadaa0395e26447be73e2b994df7a25f4a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__gain__imbalance_1gadaa0395e26447be73e2b994df7a25f4a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplie

### RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

Returns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198430 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

IQ Gain Imbalance

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset.html language=enus -->
## TOPIC 00063: IQ Origin Offset

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSETReturns the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offse

### IQ Origin Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET | Returns the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The attribute returns this result for GSM/EDGE/EGPRS measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET | Returns the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The attribute returns this result for GSM/EDGE/EGPRS measurements. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset_1ga6f8ef6a945d58f54e353ef0f9dbf98c5.html language=enus -->
## TOPIC 00064: RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset_1ga6f8ef6a945d58f54e353ef0f9dbf98c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset_1ga6f8ef6a945d58f54e353ef0f9dbf98c5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The attribute returns this result for GSM/EDGE/EGPRS measurements. SyntaxRF

### RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

Returns the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The attribute returns this result for GSM/EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198432 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

IQ Origin Offset

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset_1gacf56288c9c23783bb5e43006d816f563.html language=enus -->
## TOPIC 00065: RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset_1gacf56288c9c23783bb5e43006d816f563.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__iq__origin__offset_1gacf56288c9c23783bb5e43006d816f563.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The attribute returns this result for GSM/EDGE/EGPRS measurements. SyntaxRFMXG

### RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET

Returns the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The attribute returns this result for GSM/EDGE/EGPRS measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198431 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

IQ Origin Offset

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer.html language=enus -->
## TOPIC 00066: PFER

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsFrequency ErrorPhase ErrorGroup membersNoneAttachmentsNone

### PFER

#### Groups

- Frequency Error
- Phase Error

#### Group members

None

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error.html language=enus -->
## TOPIC 00067: Frequency Error

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERRORReturns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements. RFMXGSM_ATTR_MODACC_RESULTS_

### Frequency Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR | Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR | Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements. |

#### Attachments

None

Parent topic:

PFER

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error_1ga8a3a213fafaeee16c70c5d72604b121b.html language=enus -->
## TOPIC 00068: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error_1ga8a3a213fafaeee16c70c5d72604b121b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error_1ga8a3a213fafaeee16c70c5d72604b121b.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To4198428float64Read-Onl

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR

Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198428 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Frequency Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error_1ga8aa0958883113496ac69cb59d275e74f.html language=enus -->
## TOPIC 00069: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error_1ga8aa0958883113496ac69cb59d275e74f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__frequency__error_1ga8aa0958883113496ac69cb59d275e74f.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERRORNumeric ValueData TypeAccessApplies To4198427float64Read-OnlyN/ARe

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR

Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The attribute returns this result for GSM ModAcc measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198427 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Frequency Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error.html language=enus -->
## TOPIC 00070: Phase Error

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_MODACC_RESULTS_PFER_95TH_PERCENTILE_PHASE_ERRORReturns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measureme

### Phase Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_95TH_PERCENTILE_PHASE_ERROR | Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR | Returns the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_RMS_PHASE_ERROR | Returns the maximum of the RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR | Returns the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR | Returns the mean of RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. |
| RFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL | Returns the symbol number in the useful portion of the burst corresponding to the phase error value in the RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR result. The attribute returns this result for GSM ModAcc measurements. |

#### Attachments

None

Parent topic:

PFER

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga4f44e5c12e576b776e5aa85afb4eb34c.html language=enus -->
## TOPIC 00071: RFMXGSM_ATTR_MODACC_RESULTS_PFER_95TH_PERCENTILE_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga4f44e5c12e576b776e5aa85afb4eb34c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga4f44e5c12e576b776e5aa85afb4eb34c.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_95TH_PERCENTI

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_95TH_PERCENTILE_PHASE_ERROR

Returns the measured phase error value multiplied by 100, at which, no more than 5 percent of the symbols have phase error exceeding this value. This result is returned while performing ModAcc measurement on GSM. This value is measured in degrees.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_95TH_PERCENTILE_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198441 | float64 | Read-Only | N/A |

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga5042df7bb46bf466c54281ae6c21b325.html language=enus -->
## TOPIC 00072: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_RMS_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga5042df7bb46bf466c54281ae6c21b325.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga5042df7bb46bf466c54281ae6c21b325.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_RMS_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198423float64

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_RMS_PHASE_ERROR

Returns the maximum of the RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_RMS_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198423 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga72a4541ef217ebcdffb54656169f19bf.html language=enus -->
## TOPIC 00073: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga72a4541ef217ebcdffb54656169f19bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga72a4541ef217ebcdffb54656169f19bf.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198424float64Read-OnlyN/

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR

Returns the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198424 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga97df6374bd325de3f2897d2b751e724b.html language=enus -->
## TOPIC 00074: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga97df6374bd325de3f2897d2b751e724b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga97df6374bd325de3f2897d2b751e724b.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198422float64Read-OnlyN

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR

Returns the mean of RMS values of phase error over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198422 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga9afe695930b02081d93937d99f162235.html language=enus -->
## TOPIC 00075: RFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga9afe695930b02081d93937d99f162235.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1ga9afe695930b02081d93937d99f162235.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol number in the useful portion of the burst corresponding to the phase error value in the RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR result. The attribute returns this result for GSM ModAcc measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOLNu

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL

Returns the symbol number in the useful portion of the burst corresponding to the phase error value in the [RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR](group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1gae53a267e238c2722924b4afa3409fbf3.html) result. The attribute returns this result for GSM ModAcc measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198426 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1gae53a267e238c2722924b4afa3409fbf3.html language=enus -->
## TOPIC 00076: RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1gae53a267e238c2722924b4afa3409fbf3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__modacc__results__pfer__phase__error_1gae53a267e238c2722924b4afa3409fbf3.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements. SyntaxRFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERRORNumeric ValueData TypeAccessApplies To4198425float64Read-

### RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR

Returns the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. The attribute returns this result for GSM ModAcc measurements.

#### Syntax

RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198425 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs.html language=enus -->
## TOPIC 00077: ORFS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingEvaluation SymbolsModulationSwitchingGroup membersNameDescriptionRFMXGSM_ATTR_ORFS_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLEDSpecifie

### ORFS

#### Groups

- Averaging
- Evaluation Symbols
- Modulation
- Switching

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_ORFS_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. |
| RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLED | Specifies whether to enable the output radio frequency spectrum (ORFS) measurement. |
| RFMXGSM_ATTR_ORFS_MEASUREMENT_INTERVAL | Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. |
| RFMXGSM_ATTR_ORFS_MEASUREMENT_OFFSET | Specifies the offset, relative to the trigger, of the timeslot to be measured. |
| RFMXGSM_ATTR_ORFS_MEASUREMENT_TYPE | Specifies the type of spectral distortion to be measured. |
| RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. |
| RFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. |
| RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE | Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga0039de8c02f6d3452405122c707cf09d.html language=enus -->
## TOPIC 00078: RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga0039de8c02f6d3452405122c707cf09d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga0039de8c02f6d3452405122c707cf09d.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. SyntaxRFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODENumeric ValueData TypeAccessApplies To4202503int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read

### RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE

Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

#### Syntax

RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202503 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Standard**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_STANDARD | 0 (0x0) | Uses the list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_SHORT | 1 (0x1) | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM | 2 (0x2) | Uses the list of frequencies that is configured using the RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray and RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray functions for measurement of spectrum produced by modulation and switching measurements. |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga1e60373dd27ec9be07cc6edc448183b9.html language=enus -->
## TOPIC 00079: RFMXGSM_ATTR_ORFS_MEASUREMENT_OFFSET

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga1e60373dd27ec9be07cc6edc448183b9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga1e60373dd27ec9be07cc6edc448183b9.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset, relative to the trigger, of the timeslot to be measured. SyntaxRFMXGSM_ATTR_ORFS_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To4202534int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance

### RFMXGSM_ATTR_ORFS_MEASUREMENT_OFFSET

Specifies the offset, relative to the trigger, of the timeslot to be measured.

#### Syntax

RFMXGSM_ATTR_ORFS_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202534 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0, ([RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS](group____root__ni_r_fmx_g_s_m__attributes_1gafc24c2235a8f97b2f4a44161b6d78ef8.html) -1)].

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga6b77e0681bc1b0f410a21d3d878c59d1.html language=enus -->
## TOPIC 00080: RFMXGSM_ATTR_ORFS_MEASUREMENT_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga6b77e0681bc1b0f410a21d3d878c59d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga6b77e0681bc1b0f410a21d3d878c59d1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of spectral distortion to be measured. SyntaxRFMXGSM_ATTR_ORFS_MEASUREMENT_TYPENumeric ValueData TypeAccessApplies To4202501int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXGSM_ATTR_ORFS_MEASUREMENT_TYPE

Specifies the type of spectral distortion to be measured.

#### Syntax

RFMXGSM_ATTR_ORFS_MEASUREMENT_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202501 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Modulation and Switching**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING | 0 (0x0) | Measures the spectrum on the modulated part and the switching part of the waveform. |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION | 1 (0x1) | Measures the spectrum on the modulated part of the waveform. |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_SWITCHING | 2 (0x2) | Measures the spectrum on the switching part of the waveform. |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga753e1113d967859adb0efa77c95297fa.html language=enus -->
## TOPIC 00081: RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga753e1113d967859adb0efa77c95297fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga753e1113d967859adb0efa77c95297fa.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. SyntaxRFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To420250

### RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets.

#### Syntax

RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202502 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

**Supported Devices**: PXIe-5663/5665/5668R, PXIe-5830/5831/5832

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables compensation of the channel powers for the signal analyzer noise floor. |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga7f68f1488b032e509c84750414c4fb39.html language=enus -->
## TOPIC 00082: RFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga7f68f1488b032e509c84750414c4fb39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga7f68f1488b032e509c84750414c4fb39.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement. SyntaxRFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To4202517int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of ph

### RFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

RFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202517 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1gaa98f1ccdece7431272c0ae37d7a0fc06.html language=enus -->
## TOPIC 00083: RFMXGSM_ATTR_ORFS_MEASUREMENT_INTERVAL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1gaa98f1ccdece7431272c0ae37d7a0fc06.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1gaa98f1ccdece7431272c0ae37d7a0fc06.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. SyntaxRFMXGSM_ATTR_ORFS_MEASUREMENT_INTERVALNumeric ValueData TypeAccessApplies To4202533int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute

### RFMXGSM_ATTR_ORFS_MEASUREMENT_INTERVAL

Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots.

#### Syntax

RFMXGSM_ATTR_ORFS_MEASUREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202533 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default Value is **'Number of Timeslots'**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_MEASUREMENT_INTERVAL_NUMBER_OF_TIMESLOTS | 0 (0x0) | The measurement includes all timeslots defined by the RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS attribute. |
| RFMXGSM_VAL_ORFS_MEASUREMENT_INTERVAL_TIMESLOT_AT_OFFSET | 1 (0x1) | The measurement is performed only on the timeslot specified by the RFMXGSM_ATTR_ORFS_MEASUREMENT_OFFSET attribute. This attribute is applicable only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge or Digital Edge . |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1gab7f83fef94f802f93dc61163d465d4cd.html language=enus -->
## TOPIC 00084: RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1gab7f83fef94f802f93dc61163d465d4cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1gab7f83fef94f802f93dc61163d465d4cd.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the output radio frequency spectrum (ORFS) measurement. SyntaxRFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To4202496int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal in

### RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLED

Specifies whether to enable the output radio frequency spectrum (ORFS) measurement.

#### Syntax

RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202496 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs_1gac5a58d91bfa1385bfa0718b1aad9b8bc.html language=enus -->
## TOPIC 00085: RFMXGSM_ATTR_ORFS_ALL_TRACES_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs_1gac5a58d91bfa1385bfa0718b1aad9b8bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs_1gac5a58d91bfa1385bfa0718b1aad9b8bc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement. SyntaxRFMXGSM_ATTR_ORFS_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To4202516int32Read/WriteN/ARemarks You do not need to use a Selector String to conf

### RFMXGSM_ATTR_ORFS_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the output radio frequency spectrum (ORFS) measurement.

#### Syntax

RFMXGSM_ATTR_ORFS_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202516 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging.html language=enus -->
## TOPIC 00086: Averaging

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_ORFS_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED attribute to True. RFMXGSM_ATTR_ORFS_AVERAGING_ENABLEDSpecifies whether to enable averaging for the output radio frequen

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_ORFS_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED attribute to True. |
| RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED | Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. |
| RFMXGSM_ATTR_ORFS_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. |

#### Attachments

None

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1ga7d46a734d5a0d8f73e6165ab7cad73f6.html language=enus -->
## TOPIC 00087: RFMXGSM_ATTR_ORFS_AVERAGING_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1ga7d46a734d5a0d8f73e6165ab7cad73f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1ga7d46a734d5a0d8f73e6165ab7cad73f6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. SyntaxRFMXGSM_ATTR_ORFS_AVERAGING_TYPENumeric ValueData TypeAccessApplies To4202499int32Read/WriteN/ARemarks You do not need to use a S

### RFMXGSM_ATTR_ORFS_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

RFMXGSM_ATTR_ORFS_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202499 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Log**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_AVERAGING_TYPE_RMS | 0 (0x0) | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXGSM_VAL_ORFS_AVERAGING_TYPE_LOG | 1 (0x1) | The measurement averages the power spectrum in a logarithmic scale. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1gaabce36c04982a70cd6b314e2e09d99d7.html language=enus -->
## TOPIC 00088: RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1gaabce36c04982a70cd6b314e2e09d99d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1gaabce36c04982a70cd6b314e2e09d99d7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. SyntaxRFMXGSM_ATTR_ORFS_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To4202498int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the defau

### RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED

Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202498 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement is averaged over multiple acquisitions. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1gad10331418da024fd2f607069ab2881f0.html language=enus -->
## TOPIC 00089: RFMXGSM_ATTR_ORFS_AVERAGING_COUNT

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1gad10331418da024fd2f607069ab2881f0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1gad10331418da024fd2f607069ab2881f0.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED attribute to True. SyntaxRFMXGSM_ATTR_ORFS_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To4202500int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read

### RFMXGSM_ATTR_ORFS_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED](group____root__ni_r_fmx_g_s_m__attributes__orfs__averaging_1gaabce36c04982a70cd6b314e2e09d99d7.html) attribute to **True**.

#### Syntax

RFMXGSM_ATTR_ORFS_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202500 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols.html language=enus -->
## TOPIC 00090: Evaluation Symbols

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSCSpecifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation. RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPESpecifies the modulation power measurements that will u

### Evaluation Symbols

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC | Specifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation. |
| RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPE | Specifies the modulation power measurements that will use the part of burst configured using the RFmxGSM_ORFSCfgEvaluationSymbols. |
| RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_START | Specifies the start position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. |
| RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOP | Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. |

#### Attachments

None

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1ga7947ea5128bc4b4295d143c39df4207e.html language=enus -->
## TOPIC 00091: RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_START

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1ga7947ea5128bc4b4295d143c39df4207e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1ga7947ea5128bc4b4295d143c39df4207e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. SyntaxRFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STARTNumeric ValueData TypeAccessApplies To4202513float64Read/WriteN/ARemarks You do not need to use a Selector String to configure or rea

### RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_START

Specifies the start position within the useful part of the burst, in percentage, for measuring ORFS due to modulation.

#### Syntax

RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_START

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202513 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 50.

Parent topic:

Evaluation Symbols

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1ga8244f8684fbcff380afce51a68143e3c.html language=enus -->
## TOPIC 00092: RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1ga8244f8684fbcff380afce51a68143e3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1ga8244f8684fbcff380afce51a68143e3c.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation power measurements that will use the part of burst configured using the RFmxGSM_ORFSCfgEvaluationSymbols. SyntaxRFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPENumeric ValueData TypeAccessApplies To4202532int32Read/WriteN/ARemarks You do not need to use a selector string to config

### RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPE

Specifies the modulation power measurements that will use the part of burst configured using the [RFmxGSM_ORFSCfgEvaluationSymbols](group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga5ddcc0c21e158adca71ac6e1e6baa477.html).

#### Syntax

RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202532 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Offset**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_SCOPE_OFFSET | 0 (0x0) | Modulation Offset Power measurements will only use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols function. Modulation Carrier Power measurement will use all of the useful part of the burst. |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_SCOPE_OFFSET_AND_CARRIER | 1 (0x1) | Modulation Offset and Carrier Power measurements will both use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols function. |

Parent topic:

Evaluation Symbols

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1gaa24ad213eb23a7cf8771a76ef78f59e9.html language=enus -->
## TOPIC 00093: RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOP

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1gaa24ad213eb23a7cf8771a76ef78f59e9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1gaa24ad213eb23a7cf8771a76ef78f59e9.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. SyntaxRFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOPNumeric ValueData TypeAccessApplies To4202515float64Read/WriteN/ARemarks You do not need to use a Selector String to configure or read

### RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOP

Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation.

#### Syntax

RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202515 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 90.

Parent topic:

Evaluation Symbols

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1gacac68a89c0790d739e34024770aca473.html language=enus -->
## TOPIC 00094: RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1gacac68a89c0790d739e34024770aca473.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__evaluation__symbols_1gacac68a89c0790d739e34024770aca473.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation. SyntaxRFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSCNumeric ValueData TypeAccessApplies To4202514int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or r

### RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC

Specifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation.

#### Syntax

RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202514 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_FALSE | 0 (0x0) | The TSC portion of the burst will be excluded while performing the ORFS measurement. |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_TRUE | 1 (0x1) | The TSC portion of the burst will be included while performing the ORFS measurement. |

Parent topic:

Evaluation Symbols

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation.html language=enus -->
## TOPIC 00095: Modulation

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_ORFS_MODULATION_CARRIER_RBWSpecifies the RBW used for measuring modulation carrier power in Hz. RFMXGSM_ATTR_ORFS_MODULATION_NUMBER_OF_OFFSETSSpecifies the number of positive frequency offsets relative to the frequency of the carrier for the measure

### Modulation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_ORFS_MODULATION_CARRIER_RBW | Specifies the RBW used for measuring modulation carrier power in Hz. |
| RFMXGSM_ATTR_ORFS_MODULATION_NUMBER_OF_OFFSETS | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. |
| RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_FREQUENCY | Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. |
| RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBW | Specifies the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga0bd35d7b75dcfa1bf6d92fe16bad6735.html language=enus -->
## TOPIC 00096: RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_FREQUENCY

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga0bd35d7b75dcfa1bf6d92fe16bad6735.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga0bd35d7b75dcfa1bf6d92fe16bad6735.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz. SyntaxRFMXGSM_ATTR_ORFS_MODULATION_OFFSET_FREQUENCYNumeric ValueData TypeAccessApplies To4202526ViReal32Read/WriteOffsetRemarks Use "offset<n>" as the sele

### RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_FREQUENCY

Specifies the value of positive frequency offset for which to measure the spectrum due to modulation measurement. This value is expressed in Hz.

#### Syntax

RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202526 | ViReal32 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the selector string to configure or read this attribute.

The default value is 0.

Parent topic:

Modulation

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga51a3dbfebb5edb2f2424aa3ddf174346.html language=enus -->
## TOPIC 00097: RFMXGSM_ATTR_ORFS_MODULATION_NUMBER_OF_OFFSETS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga51a3dbfebb5edb2f2424aa3ddf174346.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga51a3dbfebb5edb2f2424aa3ddf174346.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation. SyntaxRFMXGSM_ATTR_ORFS_MODULATION_NUMBER_OF_OFFSETSNumeric ValueData TypeAccessApplies To4202525int32Read/WriteN/ARemarks You do not need to use a Selec

### RFMXGSM_ATTR_ORFS_MODULATION_NUMBER_OF_OFFSETS

Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to modulation.

#### Syntax

RFMXGSM_ATTR_ORFS_MODULATION_NUMBER_OF_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202525 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Modulation

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga64a65503f4c27f6f24ff65e67a5bd9d7.html language=enus -->
## TOPIC 00098: RFMXGSM_ATTR_ORFS_MODULATION_CARRIER_RBW

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga64a65503f4c27f6f24ff65e67a5bd9d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1ga64a65503f4c27f6f24ff65e67a5bd9d7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RBW used for measuring modulation carrier power in Hz. SyntaxRFMXGSM_ATTR_ORFS_MODULATION_CARRIER_RBWNumeric ValueData TypeAccessApplies To4202507float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Re

### RFMXGSM_ATTR_ORFS_MODULATION_CARRIER_RBW

Specifies the RBW used for measuring modulation carrier power in Hz.

#### Syntax

RFMXGSM_ATTR_ORFS_MODULATION_CARRIER_RBW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202507 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 30kHz.

Parent topic:

Modulation

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1gadb2f16427b6ca6cab305b2a1de88a413.html language=enus -->
## TOPIC 00099: RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBW

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1gadb2f16427b6ca6cab305b2a1de88a413.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__modulation_1gadb2f16427b6ca6cab305b2a1de88a413.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz. SyntaxRFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBWNumeric ValueData TypeAccessApplies To4202527float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to configure or read this attr

### RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBW

Specifies the resolution bandwidth used for ORFS due to modulation measurement. This value is expressed in Hz.

#### Syntax

RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202527 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to configure or read this attribute.

The default value is 30000.

Parent topic:

Modulation

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__switching.html language=enus -->
## TOPIC 00100: Switching

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__switching.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__switching.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_ORFS_SWITCHING_CARRIER_RBWSpecifies the RBW used for measuring switching carrier power in Hz. RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETSSpecifies the number of positive frequency offsets relative to the frequency of the carrier for the measuremen

### Switching

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_ORFS_SWITCHING_CARRIER_RBW | Specifies the RBW used for measuring switching carrier power in Hz. |
| RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETS | Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. |
| RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCY | Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. |
| RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_RBW | Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga14b96fa8bcd2873fe8351194162bbe16.html language=enus -->
## TOPIC 00101: RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_RBW

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga14b96fa8bcd2873fe8351194162bbe16.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga14b96fa8bcd2873fe8351194162bbe16.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. SyntaxRFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_RBWNumeric ValueData TypeAccessApplies To4202530float64Read-OnlyOffsetRemarks Use "offset<n>" as the selector string to configure or read this attrib

### RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_RBW

Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz.

#### Syntax

RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_RBW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202530 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the selector string to configure or read this attribute.

The default value is 30kHz.

Parent topic:

Switching

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga5064c15e17c2dddbbd558dd59d6bcdb5.html language=enus -->
## TOPIC 00102: RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga5064c15e17c2dddbbd558dd59d6bcdb5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga5064c15e17c2dddbbd558dd59d6bcdb5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching. SyntaxRFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETSNumeric ValueData TypeAccessApplies To4202528int32Read/WriteN/ARemarks You do not need to use a Selecto

### RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETS

Specifies the number of positive frequency offsets relative to the frequency of the carrier for the measurement of the spectrum due to switching.

#### Syntax

RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202528 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Switching

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga58dd19ab4472baadffb5a8d35f10eee7.html language=enus -->
## TOPIC 00103: RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCY

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga58dd19ab4472baadffb5a8d35f10eee7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1ga58dd19ab4472baadffb5a8d35f10eee7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz. SyntaxRFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCYNumeric ValueData TypeAccessApplies To4202529ViReal32Read/WriteOffsetRemarks Use "offset<n>" as the select

### RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCY

Specifies the value of positive frequency offset for which to measure the spectrum due to switching measurement. This value is expressed in Hz.

#### Syntax

RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202529 | ViReal32 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the selector string to configure or read this attribute.

The default value is 0.

Parent topic:

Switching

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1gaa2febbd004ac8d9ed5093bd3a25aa0f2.html language=enus -->
## TOPIC 00104: RFMXGSM_ATTR_ORFS_SWITCHING_CARRIER_RBW

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1gaa2febbd004ac8d9ed5093bd3a25aa0f2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__orfs__switching_1gaa2febbd004ac8d9ed5093bd3a25aa0f2.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RBW used for measuring switching carrier power in Hz. SyntaxRFMXGSM_ATTR_ORFS_SWITCHING_CARRIER_RBWNumeric ValueData TypeAccessApplies To4202510float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refe

### RFMXGSM_ATTR_ORFS_SWITCHING_CARRIER_RBW

Specifies the RBW used for measuring switching carrier power in Hz.

#### Syntax

RFMXGSM_ATTR_ORFS_SWITCHING_CARRIER_RBW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4202510 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 300kHz.

Parent topic:

Switching

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt.html language=enus -->
## TOPIC 00105: PVT

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingRBW FilterResultsGroup membersNameDescriptionRFMXGSM_ATTR_PVT_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLEDSpecifies whether to enable the power versus

### PVT

#### Groups

- Averaging
- RBW Filter
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_PVT_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. |
| RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLED | Specifies whether to enable the power versus time (PVT) measurement. |
| RFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga1d62631946cb9afa0d1220b319ef005f.html language=enus -->
## TOPIC 00106: RFMXGSM_ATTR_PVT_ALL_TRACES_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga1d62631946cb9afa0d1220b319ef005f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga1d62631946cb9afa0d1220b319ef005f.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. SyntaxRFMXGSM_ATTR_PVT_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To4206601int32Read/WriteN/ARemarks The default value is FALSE.

### RFMXGSM_ATTR_PVT_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

#### Syntax

RFMXGSM_ATTR_PVT_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206601 | int32 | Read/Write | N/A |

#### Remarks

The default value is FALSE.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga4d735bb36bbb40b3b8d1a7c867cfcd21.html language=enus -->
## TOPIC 00107: RFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga4d735bb36bbb40b3b8d1a7c867cfcd21.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga4d735bb36bbb40b3b8d1a7c867cfcd21.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. SyntaxRFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To4206602int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. Th

### RFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement.

#### Syntax

RFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206602 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga851287c13c840f0d9eb20e36fe90af07.html language=enus -->
## TOPIC 00108: RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga851287c13c840f0d9eb20e36fe90af07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt_1ga851287c13c840f0d9eb20e36fe90af07.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the power versus time (PVT) measurement. SyntaxRFMXGSM_ATTR_PVT_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To4206592int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to

### RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLED

Specifies whether to enable the power versus time (PVT) measurement.

#### Syntax

RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206592 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging.html language=enus -->
## TOPIC 00109: Averaging

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_PVT_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_PVT_AVERAGING_ENABLED attribute to True. RFMXGSM_ATTR_PVT_AVERAGING_ENABLEDSpecifies whether to enable averaging for the power versus time (PVT)

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_PVT_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_PVT_AVERAGING_ENABLED attribute to True. |
| RFMXGSM_ATTR_PVT_AVERAGING_ENABLED | Specifies whether to enable averaging for the power versus time (PVT) measurement. |
| RFMXGSM_ATTR_PVT_AVERAGING_TYPE | Specifies the averaging type for multiple acquisitions. |

#### Attachments

None

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1ga68c26cfa17eccea765100d5d103b6c24.html language=enus -->
## TOPIC 00110: RFMXGSM_ATTR_PVT_AVERAGING_COUNT

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1ga68c26cfa17eccea765100d5d103b6c24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1ga68c26cfa17eccea765100d5d103b6c24.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXGSM_ATTR_PVT_AVERAGING_ENABLED attribute to True. SyntaxRFMXGSM_ATTR_PVT_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To4206597int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read th

### RFMXGSM_ATTR_PVT_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXGSM_ATTR_PVT_AVERAGING_ENABLED](group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1gaa220ef4a7e216a8cc802c297f18daf55.html) attribute to **True**.

#### Syntax

RFMXGSM_ATTR_PVT_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206597 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1gaa220ef4a7e216a8cc802c297f18daf55.html language=enus -->
## TOPIC 00111: RFMXGSM_ATTR_PVT_AVERAGING_ENABLED

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1gaa220ef4a7e216a8cc802c297f18daf55.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1gaa220ef4a7e216a8cc802c297f18daf55.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the power versus time (PVT) measurement. SyntaxRFMXGSM_ATTR_PVT_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To4206594int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instan

### RFMXGSM_ATTR_PVT_AVERAGING_ENABLED

Specifies whether to enable averaging for the power versus time (PVT) measurement.

#### Syntax

RFMXGSM_ATTR_PVT_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206594 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement is averaged over multiple acquisitions. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1gae1135498cec81c325ea9a63bc2790279.html language=enus -->
## TOPIC 00112: RFMXGSM_ATTR_PVT_AVERAGING_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1gae1135498cec81c325ea9a63bc2790279.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__averaging_1gae1135498cec81c325ea9a63bc2790279.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for multiple acquisitions. SyntaxRFMXGSM_ATTR_PVT_AVERAGING_TYPENumeric ValueData TypeAccessApplies To4206596int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to the Selector Stri

### RFMXGSM_ATTR_PVT_AVERAGING_TYPE

Specifies the averaging type for multiple acquisitions.

#### Syntax

RFMXGSM_ATTR_PVT_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206596 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS | 0 (0x0) | The power at each sample interval is linearly averaged from one acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG | 1 (0x1) | The power at each sample interval is averaged on a logarithmic scale from one acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power at each sample interval is retained from one acquisition to the next acquisition. |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power at each sample interval is retained from one acquisition to the next acquisition. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__rbw__filter.html language=enus -->
## TOPIC 00113: RBW Filter

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__rbw__filter.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTHSpecifies the RBW Filter Bandwidth in Hz. AttachmentsNone

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTH | Specifies the RBW Filter Bandwidth in Hz. |

#### Attachments

None

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__rbw__filter_1ga2373a2ea0fe6c8d1c36b0bc2eade56e4.html language=enus -->
## TOPIC 00114: RFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__rbw__filter_1ga2373a2ea0fe6c8d1c36b0bc2eade56e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__rbw__filter_1ga2373a2ea0fe6c8d1c36b0bc2eade56e4.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RBW Filter Bandwidth in Hz. SyntaxRFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To4206599float64Read/WriteN/ARemarks The default value is 500 kHz

### RFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTH

Specifies the RBW Filter Bandwidth in Hz.

#### Syntax

RFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206599 | float64 | Read/Write | N/A |

#### Remarks

The default value is 500 kHz

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results.html language=enus -->
## TOPIC 00115: Results

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsSlotGroup membersNameDescriptionRFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUSIndicates the overall measurement status based on standard-defined limits. AttachmentsNone

### Results

#### Groups

- Slot

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUS | Indicates the overall measurement status based on standard-defined limits. |

#### Attachments

None

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results_1ga568f5349b5ddee23eda4d77609050308.html language=enus -->
## TOPIC 00116: RFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results_1ga568f5349b5ddee23eda4d77609050308.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results_1ga568f5349b5ddee23eda4d77609050308.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on standard-defined limits. SyntaxRFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To4206603int32Read-OnlyN/ARemarks You do not need to use a Selector String to read this result for the default signal and result instances.

### RFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

Indicates the overall measurement status based on standard-defined limits.

#### Syntax

RFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206603 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |
| RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_PASS | 1 (0x1) | The measurement passed because the average power of all slots is within the standard-defined limits. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot.html language=enus -->
## TOPIC 00117: Slot

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_PVT_RESULTS_SLOT_AVERAGE_POWERReturns the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_THRESHOLDReturns the threshold that the power versus t

### Slot

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_PVT_RESULTS_SLOT_AVERAGE_POWER | Returns the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. |
| RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_THRESHOLD | Returns the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. |
| RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_WIDTH | Returns the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. |
| RFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWER | Returns the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. |
| RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS | Indicates the power versus time (PVT) measurement status for a particular slot. |
| RFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWER | Returns the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga4a384da348f583b5cc8c67408d26a115.html language=enus -->
## TOPIC 00118: RFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWER

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga4a384da348f583b5cc8c67408d26a115.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga4a384da348f583b5cc8c67408d26a115.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. SyntaxRFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWERNumeric ValueData TypeAccessApplies To4206607float64Read-OnlySlotRemarks Use "slot<n>" as the selector string to read t

### RFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWER

Returns the minimum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm.

#### Syntax

RFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206607 | float64 | Read-Only | Slot |

#### Remarks

Use "slot<n>" as the selector string to read this attribute.

Parent topic:

Slot

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga83523a140458bf80c369ce22fdba9353.html language=enus -->
## TOPIC 00119: RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_THRESHOLD

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga83523a140458bf80c369ce22fdba9353.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga83523a140458bf80c369ce22fdba9353.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm. SyntaxRFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_THRESHOLDNumeric ValueData TypeAccessApplies To4206608float64Read-OnlySlotRemarks Use "slot<n>" as the selector string to

### RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_THRESHOLD

Returns the threshold that the power versus time (PVT) measurement uses to determine the burst validity. This value is expressed in dBm.

#### Syntax

RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_THRESHOLD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206608 | float64 | Read-Only | Slot |

#### Remarks

Use "slot<n>" as the selector string to read this attribute.

Parent topic:

Slot

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga85b64e57fc0d29db95a6fd07c9286a53.html language=enus -->
## TOPIC 00120: RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga85b64e57fc0d29db95a6fd07c9286a53.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga85b64e57fc0d29db95a6fd07c9286a53.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power versus time (PVT) measurement status for a particular slot. SyntaxRFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To4206609int32Read-OnlySlotRemarks Use "slot<n>" as the selector string to read this attribute.NameValueDescriptionRFMXGSM_VAL_PVT

### RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS

Indicates the power versus time (PVT) measurement status for a particular slot.

#### Syntax

RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206609 | int32 | Read-Only | Slot |

#### Remarks

Use "slot<n>" as the selector string to read this attribute.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The average power for at least one slot is outside the standard-defined limits. |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS | 1 (0x1) | The average power for each slot is within the standard-defined limits. |

Parent topic:

Slot

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga88555528fc212b45afebb4bef9def3fe.html language=enus -->
## TOPIC 00121: RFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWER

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga88555528fc212b45afebb4bef9def3fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1ga88555528fc212b45afebb4bef9def3fe.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. SyntaxRFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWERNumeric ValueData TypeAccessApplies To4206606float64Read-OnlySlotRemarks Use "slot<n>" as the selector string to read t

### RFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWER

Returns the maximum power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm.

#### Syntax

RFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206606 | float64 | Read-Only | Slot |

#### Remarks

Use "slot<n>" as the selector string to read this attribute.

Parent topic:

Slot

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1gac227a2795a3e0f78dbabb47987bcd6e4.html language=enus -->
## TOPIC 00122: RFMXGSM_ATTR_PVT_RESULTS_SLOT_AVERAGE_POWER

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1gac227a2795a3e0f78dbabb47987bcd6e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1gac227a2795a3e0f78dbabb47987bcd6e4.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm. SyntaxRFMXGSM_ATTR_PVT_RESULTS_SLOT_AVERAGE_POWERNumeric ValueData TypeAccessApplies To4206604float64Read-OnlySlotRemarks Use "slot<n>" as the selector string to read this

### RFMXGSM_ATTR_PVT_RESULTS_SLOT_AVERAGE_POWER

Returns the mean power of the signal, averaged over the corresponding slots of each acquisition. This value is expressed in dBm.

#### Syntax

RFMXGSM_ATTR_PVT_RESULTS_SLOT_AVERAGE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206604 | float64 | Read-Only | Slot |

#### Remarks

Use "slot<n>" as the selector string to read this attribute.

Parent topic:

Slot

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1gaed28237819c6f6fd281a6418ce8ab14c.html language=enus -->
## TOPIC 00123: RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_WIDTH

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1gaed28237819c6f6fd281a6418ce8ab14c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__pvt__results__slot_1gaed28237819c6f6fd281a6418ce8ab14c.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds. SyntaxRFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_WIDTHNumeric ValueData TypeAccessApplies To4206605float64Read-OnlySlotRemarks Use "slot<n>" as the selector string to read this attribute.

### RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_WIDTH

Returns the burst width for the slot where the -3 dB transition points occur. This value is expressed in seconds.

#### Syntax

RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_WIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4206605 | float64 | Read-Only | Slot |

#### Remarks

Use "slot<n>" as the selector string to read this attribute.

Parent topic:

Slot

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger.html language=enus -->
## TOPIC 00124: Trigger

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXGSM_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. RFMXGSM_ATTR_TRIGGER_TYPESpecifies the trigger type. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. |
| RFMXGSM_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html language=enus -->
## TOPIC 00125: RFMXGSM_ATTR_TRIGGER_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxRFMXGSM_ATTR_TRIGGER_TYPENumeric ValueData TypeAccessApplies To4194308int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the

### RFMXGSM_ATTR_TRIGGER_TYPE

Specifies the trigger type.

#### Syntax

RFMXGSM_ATTR_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194308 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **IQ Power Edge**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_TRIGGER_TYPE_NONE | 0 (0x0) | No Reference Trigger is configured. |
| RFMXGSM_VAL_TRIGGER_TYPE_DIGITAL_EDGE | 1 (0x1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE | 2 (0x2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXGSM_VAL_TRIGGER_TYPE_SOFTWARE | 3 (0x3) | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger_1gad8dd359e585aa178fe21f27c22adf386.html language=enus -->
## TOPIC 00126: RFMXGSM_ATTR_TRIGGER_DELAY

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger_1gad8dd359e585aa178fe21f27c22adf386.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger_1gad8dd359e585aa178fe21f27c22adf386.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger delay time. This value is expressed in seconds. SyntaxRFMXGSM_ATTR_TRIGGER_DELAYNumeric ValueData TypeAccessApplies To4194314float64Read/WriteN/ARemarks If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires pos

### RFMXGSM_ATTR_TRIGGER_DELAY

Specifies the trigger delay time. This value is expressed in seconds.

#### Syntax

RFMXGSM_ATTR_TRIGGER_DELAY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194314 | float64 | Read/Write | N/A |

#### Remarks

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge.html language=enus -->
## TOPIC 00127: Digital Edge

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGESpecifies the active edge for the trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to Digital Edge. RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCESpecifies the source terminal for the digit

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to Digital Edge. |
| RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE | Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to Digital Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge_1ga025592a149fec122a3346cbadabd36c6.html language=enus -->
## TOPIC 00128: RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge_1ga025592a149fec122a3346cbadabd36c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge_1ga025592a149fec122a3346cbadabd36c6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGENumeric ValueData TypeAccessApplies To4194310int32Read/WriteN/ARemarks You do not need to use a Selector String to

### RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

Specifies the active edge for the trigger. This attribute is used only when you set the [RFMXGSM_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html) attribute to **Digital Edge**.

#### Syntax

RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194310 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |
| RFMXGSM_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge_1gae436aa41a5693a4779a4a9496771b747.html language=enus -->
## TOPIC 00129: RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge_1gae436aa41a5693a4779a4a9496771b747.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__digital__edge_1gae436aa41a5693a4779a4a9496771b747.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To4194309char[]Read/WriteN/ARemarks You do not need to use a

### RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the [RFMXGSM_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html) attribute to **Digital Edge**.

#### Syntax

RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194309 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge.html language=enus -->
## TOPIC 00130: IQ Power Edge

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVELSpecifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level Typ

### IQ Power Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL | Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level Type attribute to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE | Specifies the reference for the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute with the slope you specify. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga0d2c50d725a1566cdca5a154694f4878.html language=enus -->
## TOPIC 00131: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga0d2c50d725a1566cdca5a154694f4878.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga0d2c50d725a1566cdca5a154694f4878.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPENumeric ValueData TypeAccessApplies To4198

### RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

Specifies the reference for the [RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga2d342b81eddfdb7f84b1745ed87c7c58.html) attribute. The IQ Power Edge Level Type attribute is used only when you set the [RFMXGSM_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4198399 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The value of the IQ Power Edge Level attribute is relative to the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. |
| RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga2d342b81eddfdb7f84b1745ed87c7c58.html language=enus -->
## TOPIC 00132: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga2d342b81eddfdb7f84b1745ed87c7c58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga2d342b81eddfdb7f84b1745ed87c7c58.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level Type attribute to Absolute. The device asserts the trigger when the signal exceed

### RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga0d2c50d725a1566cdca5a154694f4878.html) attribute to **Relative** and in dBm when you set the IQ Power Edge Level Type attribute to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the [RFMXGSM_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194312 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1gaa5bcb647e98edc09ae0a79713f4261f4.html language=enus -->
## TOPIC 00133: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1gaa5bcb647e98edc09ae0a79713f4261f4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1gaa5bcb647e98edc09ae0a79713f4261f4.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To4194311char[]Read/WriteN/ARemarks You do not need

### RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the [RFMXGSM_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194311 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1gac24bef5b8de2e1c3525753ae2a342db3.html language=enus -->
## TOPIC 00134: RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1gac24bef5b8de2e1c3525753ae2a342db3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1gac24bef5b8de2e1c3525753ae2a342db3.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute with the slope you specify. This attribute is used

### RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1ga2d342b81eddfdb7f84b1745ed87c7c58.html) attribute with the slope you specify. This attribute is used only when you set the [RFMXGSM_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_g_s_m__attributes__trigger_1ga4ea036adef6cb407842899748626f100.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194313 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |
| RFMXGSM_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00135: Minimum Quiet Time

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODESpecifies w

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time_1ga205cafa54cd84c7172d0a21242d67239.html language=enus -->
## TOPIC 00136: RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time_1ga205cafa54cd84c7172d0a21242d67239.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time_1ga205cafa54cd84c7172d0a21242d67239.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxRFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODENumeric ValueData TypeAccessApplies To4194315int32Read/WriteN/ARemarks You do not need to use a Selector String to configure or read this attribute for the default

### RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194315 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time_1ga4b389deadb3a43348eadc278f9ffcbf0.html language=enus -->
## TOPIC 00137: RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time_1ga4b389deadb3a43348eadc278f9ffcbf0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__attributes__trigger__minimum__quiet__time_1ga4b389deadb3a43348eadc278f9ffcbf0.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. SyntaxRFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONNumeric ValueData TypeAccessApplies To4194316float64Read/WriteN/ARemarks If you set the

### RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

#### Syntax

RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4194316 | float64 | Read/Write | N/A |

#### Remarks

If you set the [RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE](group____root__ni_r_fmx_g_s_m__attributes__trigger__iq__power__edge_1gac24bef5b8de2e1c3525753ae2a342db3.html) attribute to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions.html language=enus -->
## TOPIC 00138: Functions

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedBuild StringConfigurationFetchSelect MeasurementSet and Get AttributesUtilityGroup membersNameDescriptionRFmxGSM_CloseCloses the session to the device. RFmxGSM_GetErrorRetrieves and then clears the error information for the session or the current execution thread. You must provide a ch

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
| RFmxGSM_Close | Closes the session to the device. |
| RFmxGSM_GetError | Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxGSM_GetErrorString | Converts a status code returned by an RFmxGSM function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxGSM_Initialize | Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. |
| RFmxGSM_Initiate | Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the RFmxGSM_WaitForMeasurementComplete function or RFmxGSM_CheckMeasurementStatus function. |

#### Attachments

None

Parent topic:

niRFmxGSM.h

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions_1ga001a404a8a9f3273e897293b3d277ae1.html language=enus -->
## TOPIC 00139: RFmxGSM_GetErrorString

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions_1ga001a404a8a9f3273e897293b3d277ae1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions_1ga001a404a8a9f3273e897293b3d277ae1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxGSM function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxGSM_GetErrorString(niRFmxInstrHandle ins

### RFmxGSM_GetErrorString

Converts a status code returned by an RFmxGSM function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxGSM function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html language=enus -->
## TOPIC 00140: RFmxGSM_GetError

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxGSM_GetError(niRFmxInstrHan

### RFmxGSM_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxGSM_GetErrorString](group____root__ni_r_fmx_g_s_m__functions_1ga001a404a8a9f3273e897293b3d277ae1.html) function if the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function does not return an error message.

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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions_1ga238434c5965e22ce849f557252113cbe.html language=enus -->
## TOPIC 00141: RFmxGSM_Initiate

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions_1ga238434c5965e22ce849f557252113cbe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions_1ga238434c5965e22ce849f557252113cbe.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in

### RFmxGSM_Initiate

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxGSM_WaitForMeasurementComplete](group____root__ni_r_fmx_g_s_m__functions__utility_1gacbc41fa3fccc5ac797a954b8a8f18034.html) function or [RFmxGSM_CheckMeasurementStatus](group____root__ni_r_fmx_g_s_m__functions__utility_1gacec6c52c15959eb2f9d02479f22dbe00.html) function.

#### Syntax

int32 __stdcall RFmxGSM_Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance.Example:"""result::r1""r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions_1ga78f84231a947025476838d6c87fb8a34.html language=enus -->
## TOPIC 00142: RFmxGSM_Close

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions_1ga78f84231a947025476838d6c87fb8a34.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions_1ga78f84231a947025476838d6c87fb8a34.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the device. Syntaxint32 __stdcall RFmxGSM_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the RFmxInstr_Close function.Enabling the SFP (Soft Front Panel) debug has a performance impact. For

### RFmxGSM_Close

Closes the session to the device.

#### Syntax

int32 __stdcall RFmxGSM_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?context=rfmxinstr_rfmxinstrcref_function_close) function.

Note

Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| forceDestroy | [in] | int32 | Specifies whether to destroy the RFmx session.ValueDescriptionRFMXGSM_VAL_FALSE (0)Destroys the RFmx session. Call the RFmxGSM_Close function a number of times equal to the number of times you obtained a reference to the RFmx session.RFMXGSM_VAL_TRUE (1)Destroys the RFmx session. You do not have to call the RFmxGSM_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| Value | Description |  |  |
| RFMXGSM_VAL_FALSE (0) | Destroys the RFmx session. Call the RFmxGSM_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |  |
| RFMXGSM_VAL_TRUE (1) | Destroys the RFmx session. You do not have to call the RFmxGSM_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions_1gaa8ea14a1eb1781d209127fa33f7ba03e.html language=enus -->
## TOPIC 00143: RFmxGSM_Initialize

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions_1gaa8ea14a1eb1781d209127fa33f7ba03e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions_1gaa8ea14a1eb1781d209127fa33f7ba03e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxGSM_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSes

### RFmxGSM_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxGSM_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

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
| isNewSession | [out] | int32 * | Returns RFMXGSM_VAL_TRUE if the function created a new session, or RFMXGSM_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced.html language=enus -->
## TOPIC 00144: Advanced

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_AbortMeasurementsStops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. This acquisition and measurements were previously initiated by the RFmxGSM_Initiate function. Calling this function

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_AbortMeasurements | Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. This acquisition and measurements were previously initiated by the RFmxGSM_Initiate function. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error. |
| RFmxGSM_AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is IQ. |
| RFmxGSM_AnalyzeIQ1WaveformSplit | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is IQ. |
| RFmxGSM_ClearAllNamedResults | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxGSM_ClearNamedResult | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxGSM_CloneSignalConfiguration | Creates a new instance of a signal by copying all the attribute values from an existing signal instance. |
| RFmxGSM_CreateSignalConfiguration | Creates a new instance of a signal. |
| RFmxGSM_DeleteSignalConfiguration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxGSM_GetAllNamedResultNames | Returns all the named result names of the signal that you specify in the Selector String parameter. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga1a26a4948dafda1c5eb8109449994626.html language=enus -->
## TOPIC 00145: RFmxGSM_CloneSignalConfiguration

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga1a26a4948dafda1c5eb8109449994626.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga1a26a4948dafda1c5eb8109449994626.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the attribute values from an existing signal instance. Syntaxint32 __stdcall RFmxGSM_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niR

### RFmxGSM_CloneSignalConfiguration

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Syntax

int32 __stdcall RFmxGSM_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| oldSignalName | [in] | char[] | This parameter specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::OldSigName""OldSigName" |
| newSignalName | [in] | char[] | This parameter specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::NewSigName""NewSigName" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga35b5d07736f0415ae0b5ff5314ba23f8.html language=enus -->
## TOPIC 00146: RFmxGSM_CreateSignalConfiguration

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga35b5d07736f0415ae0b5ff5314ba23f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga35b5d07736f0415ae0b5ff5314ba23f8.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxGSM_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtai

### RFmxGSM_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxGSM_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga55172502df9a41d68f4cf965423ccf77.html language=enus -->
## TOPIC 00147: RFmxGSM_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga55172502df9a41d68f4cf965423ccf77.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga55172502df9a41d68f4cf965423ccf77.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxGSM_AnalyzeIQ1WaveformSplit

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is **IQ**.

#### Syntax

int32 __stdcall RFmxGSM_AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqI[], float32 iqQ[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxGSM_Commit](group____root__ni_r_fmx_g_s_m__functions__utility_1gabfb36f46527de57744bd6afb786ab791.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iqI | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqQ | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga57ea4bdb2bdde0429357025b6b725d0a.html language=enus -->
## TOPIC 00148: RFmxGSM_ClearAllNamedResults

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga57ea4bdb2bdde0429357025b6b725d0a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga57ea4bdb2bdde0429357025b6b725d0a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxGSM_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RF

### RFmxGSM_ClearAllNamedResults

Clears all results for the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxGSM_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga627049884d77027f9673d00b51d51176.html language=enus -->
## TOPIC 00149: RFmxGSM_GetAllNamedResultNames

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga627049884d77027f9673d00b51d51176.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga627049884d77027f9673d00b51d51176.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxGSM_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *de

### RFmxGSM_GetAllNamedResultNames

Returns all the named result names of the signal that you specify in the Selector String parameter.

#### Syntax

int32 __stdcall RFmxGSM_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9c2cfa10fbd051236dc14dd5114c75c1.html language=enus -->
## TOPIC 00150: RFmxGSM_AnalyzeIQ1Waveform

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9c2cfa10fbd051236dc14dd5114c75c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9c2cfa10fbd051236dc14dd5114c75c1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxGSM_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is **IQ**.

#### Syntax

int32 __stdcall RFmxGSM_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxGSM_Commit](group____root__ni_r_fmx_g_s_m__functions__utility_1gabfb36f46527de57744bd6afb786ab791.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9f392eca7d43871b580d55f9fb1c12b2.html language=enus -->
## TOPIC 00151: RFmxGSM_DeleteSignalConfiguration

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9f392eca7d43871b580d55f9fb1c12b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9f392eca7d43871b580d55f9fb1c12b2.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. Syntaxint32 __stdcall RFmxGSM_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx se

### RFmxGSM_DeleteSignalConfiguration

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

#### Syntax

int32 __stdcall RFmxGSM_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9fca90cdbd3f3ee2d0b9c1dfe08dd843.html language=enus -->
## TOPIC 00152: RFmxGSM_AbortMeasurements

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9fca90cdbd3f3ee2d0b9c1dfe08dd843.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1ga9fca90cdbd3f3ee2d0b9c1dfe08dd843.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. This acquisition and measurements were previously initiated by the RFmxGSM_Initiate function. Calling this function is optional, unless you want to stop a measurement before it i

### RFmxGSM_AbortMeasurements

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. This acquisition and measurements were previously initiated by the [RFmxGSM_Initiate](group____root__ni_r_fmx_g_s_m__functions_1ga238434c5965e22ce849f557252113cbe.html) function. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxGSM_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__advanced_1gad9a455a771bb0a5f65e69e410bd724b1.html language=enus -->
## TOPIC 00153: RFmxGSM_ClearNamedResult

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__advanced_1gad9a455a771bb0a5f65e69e410bd724b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__advanced_1gad9a455a771bb0a5f65e69e410bd724b1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. Syntaxint32 __stdcall RFmxGSM_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFm

### RFmxGSM_ClearNamedResult

Clears a result instance specified by the result name in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxGSM_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__build__string.html language=enus -->
## TOPIC 00154: Build String

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__build__string.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_BuildOffsetStringCreates an offset string to be used as the selector string with configuration or fetch attributes and functions. RFmxGSM_BuildSignalStringCreates selector string for use with configuration or fetch attributes and functions. RFmxGSM_Build

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_BuildOffsetString | Creates an offset string to be used as the selector string with configuration or fetch attributes and functions. |
| RFmxGSM_BuildSignalString | Creates selector string for use with configuration or fetch attributes and functions. |
| RFmxGSM_BuildSlotString | Creates a slot string to be used as the selector string with configuration or fetch attributes and functions. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__build__string_1ga0929e90ada77f9b0d3c3111ee22696c3.html language=enus -->
## TOPIC 00155: RFmxGSM_BuildSignalString

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__build__string_1ga0929e90ada77f9b0d3c3111ee22696c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__build__string_1ga0929e90ada77f9b0d3c3111ee22696c3.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxGSM_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])ParametersNameDirectionTypeDescriptionsignalName[in]char[]This parameter speci

### RFmxGSM_BuildSignalString

Creates selector string for use with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxGSM_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default is "" (empty string).Example:"signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default is "" (empty string).Example:"result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__build__string_1ga6333f0edcafe5c87c341c94b13838384.html language=enus -->
## TOPIC 00156: RFmxGSM_BuildSlotString

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__build__string_1ga6333f0edcafe5c87c341c94b13838384.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__build__string_1ga6333f0edcafe5c87c341c94b13838384.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a slot string to be used as the selector string with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxGSM_BuildSlotString(char selectorString[], int32 slotNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorS

### RFmxGSM_BuildSlotString

Creates a slot string to be used as the selector string with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxGSM_BuildSlotString(char selectorString[], int32 slotNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| slotNumber | [in] | int32 | This parameter specifies the slot number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__build__string_1gaa73d370f897f0cb9dee37be65e176e04.html language=enus -->
## TOPIC 00157: RFmxGSM_BuildOffsetString

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__build__string_1gaa73d370f897f0cb9dee37be65e176e04.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__build__string_1gaa73d370f897f0cb9dee37be65e176e04.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an offset string to be used as the selector string with configuration or fetch attributes and functions. Syntaxint32 __stdcall RFmxGSM_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionse

### RFmxGSM_BuildOffsetString

Creates an offset string to be used as the selector string with configuration or fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxGSM_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| offsetNumber | [in] | int32 | This parameter specifies the offset number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration.html language=enus -->
## TOPIC 00158: Configuration

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsFrequencyModAccORFSPVTTriggerGroup membersNameDescriptionRFmxGSM_AutoLevelExamines the input signal to calculate the peak power level and sets it as the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. RFmx

### Configuration

#### Groups

- Frequency
- ModAcc
- ORFS
- PVT
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. |
| RFmxGSM_CfgAutoTSCDetectionEnabled | Configures whether to auto detect the training sequence code (TSC). |
| RFmxGSM_CfgBand | Configures the band of operation. |
| RFmxGSM_CfgBurstSynchronizationType | Configures the burst synchronization type. |
| RFmxGSM_CfgExternalAttenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
| RFmxGSM_CfgFrequencyReference | Configures the Reference Clock and the frequency reference source. |
| RFmxGSM_CfgLinkDirection | Configures the source of the signal to be measured. |
| RFmxGSM_CfgMechanicalAttenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxGSM_CfgNumberOfTimeslots | Configures the number of time slots to be measured. |
| RFmxGSM_CfgPowerControlLevel | Configures the power control level corresponding to the transmitted power. |
| RFmxGSM_CfgRF | Configures the RF attributes of the signal specified by the selector string. |
| RFmxGSM_CfgRFAttenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxGSM_CfgReferenceLevel | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| RFmxGSM_CfgSignalType | Configures the signal type. |
| RFmxGSM_CfgTSC | Configures the training sequence code (TSC) in the burst. |
| RFmxGSM_SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxGSM Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga13916e0f4cfb6a36c268b488c9aff5a6.html language=enus -->
## TOPIC 00159: RFmxGSM_CfgPowerControlLevel

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga13916e0f4cfb6a36c268b488c9aff5a6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga13916e0f4cfb6a36c268b488c9aff5a6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power control level corresponding to the transmitted power. Syntaxint32 __stdcall RFmxGSM_CfgPowerControlLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerControlLevel)RemarksUse "slot<n>" as the selector string to configure this function.ParametersNameDirect

### RFmxGSM_CfgPowerControlLevel

Configures the power control level corresponding to the transmitted power.

#### Syntax

int32 __stdcall RFmxGSM_CfgPowerControlLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerControlLevel)

#### Remarks

Use "slot<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all".Example:"slot0""slot::all""signal::sig1/slot0"You can use the RFmxGSM_BuildSlotString function to build the selector string. |
| powerControlLevel | [in] | int32 | This parameter specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga31f7f7a8f0c62a45915f4cba4e6d2e30.html language=enus -->
## TOPIC 00160: RFmxGSM_CfgBand

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga31f7f7a8f0c62a45915f4cba4e6d2e30.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga31f7f7a8f0c62a45915f4cba4e6d2e30.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the band of operation. Syntaxint32 __stdcall RFmxGSM_CfgBand(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 band)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtained

### RFmxGSM_CfgBand

Configures the band of operation.

#### Syntax

int32 __stdcall RFmxGSM_CfgBand(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 band)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| band | [in] | int32 | This parameter specifies the band of operation. The default value is PGSM.NameValueDescriptionRFMXGSM_VAL_BAND_PGSM0 (0x0)The operation band is Primary GSM in the 900 MHz band.RFMXGSM_VAL_BAND_EGSM1 (0x1)The operation band is Extended GSM in the 900 MHz band.RFMXGSM_VAL_BAND_RGSM2 (0x2)The operation band is Railway GSM in the 900 MHz band.RFMXGSM_VAL_BAND_DCS18003 (0x3)The operation band is GSM in the 1800 MHz band.RFMXGSM_VAL_BAND_PCS19004 (0x4)The operation band is GSM in the 1900 MHz band.RFMXGSM_VAL_BAND_GSM4505 (0x5)The operation band is GSM in the 450 MHz band.RFMXGSM_VAL_BAND_GSM4806 (0x6)The operation band is GSM in the 480 MHz band.RFMXGSM_VAL_BAND_GSM8507 (0x7)The operation band is GSM in the 850 MHz band.RFMXGSM_VAL_BAND_GSM7508 (0x8)The operation band is GSM in the 750 MHz band.RFMXGSM_VAL_BAND_TGSM8109 (0x9)The operation band is terrestrial GSM in the 810 MHz band. |
| Name | Value | Description |  |
| RFMXGSM_VAL_BAND_PGSM | 0 (0x0) | The operation band is Primary GSM in the 900 MHz band. |  |
| RFMXGSM_VAL_BAND_EGSM | 1 (0x1) | The operation band is Extended GSM in the 900 MHz band. |  |
| RFMXGSM_VAL_BAND_RGSM | 2 (0x2) | The operation band is Railway GSM in the 900 MHz band. |  |
| RFMXGSM_VAL_BAND_DCS1800 | 3 (0x3) | The operation band is GSM in the 1800 MHz band. |  |
| RFMXGSM_VAL_BAND_PCS1900 | 4 (0x4) | The operation band is GSM in the 1900 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM450 | 5 (0x5) | The operation band is GSM in the 450 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM480 | 6 (0x6) | The operation band is GSM in the 480 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM850 | 7 (0x7) | The operation band is GSM in the 850 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM750 | 8 (0x8) | The operation band is GSM in the 750 MHz band. |  |
| RFMXGSM_VAL_BAND_TGSM810 | 9 (0x9) | The operation band is terrestrial GSM in the 810 MHz band. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga362758b662d00164624f98d4fe7455b3.html language=enus -->
## TOPIC 00161: RFmxGSM_CfgNumberOfTimeslots

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga362758b662d00164624f98d4fe7455b3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga362758b662d00164624f98d4fe7455b3.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of time slots to be measured. Syntaxint32 __stdcall RFmxGSM_CfgNumberOfTimeslots(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfTimeslots)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx sessi

### RFmxGSM_CfgNumberOfTimeslots

Configures the number of time slots to be measured.

#### Syntax

int32 __stdcall RFmxGSM_CfgNumberOfTimeslots(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfTimeslots)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| numberOfTimeslots | [in] | int32 | This parameter specifies the number of time slots to be measured. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4c3d4ebd977f69024982aa6543c646cc.html language=enus -->
## TOPIC 00162: RFmxGSM_CfgAutoTSCDetectionEnabled

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4c3d4ebd977f69024982aa6543c646cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4c3d4ebd977f69024982aa6543c646cc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to auto detect the training sequence code (TSC). Syntaxint32 __stdcall RFmxGSM_CfgAutoTSCDetectionEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoTscDetectionEnabled)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parame

### RFmxGSM_CfgAutoTSCDetectionEnabled

Configures whether to auto detect the training sequence code (TSC).

#### Syntax

int32 __stdcall RFmxGSM_CfgAutoTSCDetectionEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoTscDetectionEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| autoTscDetectionEnabled | [in] | int32 | This parameter specifies whether to auto detect the TSC. The default value is True.NameValueDescriptionRFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE0 (0x0)The measurement uses the value that you configure using the RFMXGSM_ATTR_TSC attribute.RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE1 (0x1)The measurement detects the TSC in the burst. |
| Name | Value | Description |  |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE | 0 (0x0) | The measurement uses the value that you configure using the RFMXGSM_ATTR_TSC attribute. |  |
| RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE | 1 (0x1) | The measurement detects the TSC in the burst. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4cf98b716320777ce4ebc84784c38a99.html language=enus -->
## TOPIC 00163: RFmxGSM_CfgRFAttenuation

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4cf98b716320777ce4ebc84784c38a99.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4cf98b716320777ce4ebc84784c38a99.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the nominal attenuation and the RFmx driver setting. Syntaxint32 __stdcall RFmxGSM_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the RF

### RFmxGSM_CfgRFAttenuation

Configures the nominal attenuation and the RFmx driver setting.

#### Syntax

int32 __stdcall RFmxGSM_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgRFAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_rf_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| rfAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver computes the RF attenuation.ValueDescriptionRFMXGSM_VAL_RF_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter.RFMXGSM_VAL_RF_ATTENUATION_AUTO_TRUE (1)Specifies that the RFmx driver computes the RF attenuation automatically. |
| Value | Description |  |  |
| RFMXGSM_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. |  |  |
| RFMXGSM_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that the RFmx driver computes the RF attenuation automatically. |  |  |
| rfAttenuationValue | [in] | float64 | Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain when the rfAttenuationAuto parameter is set to RFMXGSM_VAL_RF_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4d85e4cec88ddb373adb2113ae6e985f.html language=enus -->
## TOPIC 00164: RFmxGSM_CfgRF

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4d85e4cec88ddb373adb2113ae6e985f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga4d85e4cec88ddb373adb2113ae6e985f.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF attributes of the signal specified by the selector string. Syntaxint32 __stdcall RFmxGSM_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)ParametersNameDirectionTypeDescriptioninstrumentHan

### RFmxGSM_CfgRF

Configures the RF attributes of the signal specified by the selector string.

#### Syntax

int32 __stdcall RFmxGSM_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. The default of this attribute is hardware dependent. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this attribute is hardware dependent. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the External Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga578da889eee1ef92409f2652a9489f23.html language=enus -->
## TOPIC 00165: RFmxGSM_CfgSignalType

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga578da889eee1ef92409f2652a9489f23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga578da889eee1ef92409f2652a9489f23.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal type. Syntaxint32 __stdcall RFmxGSM_CfgSignalType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 modulationType, int32 burstType, int32 hbFilterWidth)RemarksUse "slot<n>" as the selector string to configure this function.ParametersNameDirectionTypeDescriptioni

### RFmxGSM_CfgSignalType

Configures the signal type.

#### Syntax

int32 __stdcall RFmxGSM_CfgSignalType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 modulationType, int32 burstType, int32 hbFilterWidth)

#### Remarks

Use "slot<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all".Example:"slot0""slot::all""signal::sig1/slot0"You can use the RFmxGSM_BuildSlotString function to build the selector string. |
| modulationType | [in] | int32 | This parameter specifies the modulation type of the signal. The default value is 8PSK.NameValueDescriptionRFMXGSM_VAL_MODULATION_TYPE_GMSK0 (0x0)The modulation type is Gaussian minimum shift keying. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to NB or AB.RFMXGSM_VAL_MODULATION_TYPE_8PSK1 (0x1)The modulation type is 8-PSK. This value is valid only when you set the Burst Type attribute to NB.RFMXGSM_VAL_MODULATION_TYPE_QPSK2 (0x2)The modulation type is QPSK. This value is valid only when you set the Burst Type attribute to HB.RFMXGSM_VAL_MODULATION_TYPE_16QAM3 (0x3)The modulation type is 16-QAM.RFMXGSM_VAL_MODULATION_TYPE_32QAM4 (0x4)The modulation type is 32-QAM. |
| Name | Value | Description |  |
| RFMXGSM_VAL_MODULATION_TYPE_GMSK | 0 (0x0) | The modulation type is Gaussian minimum shift keying. This value is valid only when you set the RFMXGSM_ATTR_BURST_TYPE attribute to NB or AB. |  |
| RFMXGSM_VAL_MODULATION_TYPE_8PSK | 1 (0x1) | The modulation type is 8-PSK. This value is valid only when you set the Burst Type attribute to NB. |  |
| RFMXGSM_VAL_MODULATION_TYPE_QPSK | 2 (0x2) | The modulation type is QPSK. This value is valid only when you set the Burst Type attribute to HB. |  |
| RFMXGSM_VAL_MODULATION_TYPE_16QAM | 3 (0x3) | The modulation type is 16-QAM. |  |
| RFMXGSM_VAL_MODULATION_TYPE_32QAM | 4 (0x4) | The modulation type is 32-QAM. |  |
| burstType | [in] | int32 | This parameter specifies the burst type. The default value is NB.NameValueDescriptionRFMXGSM_VAL_BURST_TYPE_NB0 (0x0)The burst type is Normal Burst.RFMXGSM_VAL_BURST_TYPE_HB1 (0x1)The burst type is Higher Symbol Rate Burst.RFMXGSM_VAL_BURST_TYPE_AB2 (0x2)The burst type is Access Burst. |
| Name | Value | Description |  |
| RFMXGSM_VAL_BURST_TYPE_NB | 0 (0x0) | The burst type is Normal Burst. |  |
| RFMXGSM_VAL_BURST_TYPE_HB | 1 (0x1) | The burst type is Higher Symbol Rate Burst. |  |
| RFMXGSM_VAL_BURST_TYPE_AB | 2 (0x2) | The burst type is Access Burst. |  |
| hbFilterWidth | [in] | int32 | This parameter specifies the filter width when you set the Burst Type parameter to HB. The default value is Narrow.NameValueDescriptionRFMXGSM_VAL_HB_FILTER_WIDTH_NARROW0 (0x0)The measurement uses a narrow filter.RFMXGSM_VAL_HB_FILTER_WIDTH_WIDE1 (0x1)The measurement uses a wide filter. |
| Name | Value | Description |  |
| RFMXGSM_VAL_HB_FILTER_WIDTH_NARROW | 0 (0x0) | The measurement uses a narrow filter. |  |
| RFMXGSM_VAL_HB_FILTER_WIDTH_WIDE | 1 (0x1) | The measurement uses a wide filter. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga6273309935bfdde20de953a146934d7f.html language=enus -->
## TOPIC 00166: RFmxGSM_CfgMechanicalAttenuation

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga6273309935bfdde20de953a146934d7f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga6273309935bfdde20de953a146934d7f.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxGSM_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wrappe

### RFmxGSM_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxGSM_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga6d49d17fc4c6513ac14590f4c9cfe5d1.html language=enus -->
## TOPIC 00167: RFmxGSM_CfgTSC

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga6d49d17fc4c6513ac14590f4c9cfe5d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga6d49d17fc4c6513ac14590f4c9cfe5d1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the training sequence code (TSC) in the burst. Syntaxint32 __stdcall RFmxGSM_CfgTSC(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 tsc)RemarksUse "slot<n>" as the selector string to configure this function.ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxI

### RFmxGSM_CfgTSC

Configures the training sequence code (TSC) in the burst.

#### Syntax

int32 __stdcall RFmxGSM_CfgTSC(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 tsc)

#### Remarks

Use "slot<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all".Example:"slot0""slot::all""signal::sig1/slot0"You can use the RFmxGSM_BuildSlotString function to build the selector string. |
| tsc | [in] | int32 | This parameter specifies the training sequence code in the burst. For access burst TSC0, TSC1, and TSC2 are applicable. The default value is TSC0.NameValueDescriptionRFMXGSM_VAL_TSC00 (0x0)The measurement uses training sequence code 0.RFMXGSM_VAL_TSC11 (0x1)The measurement uses training sequence code 1.RFMXGSM_VAL_TSC22 (0x2)The measurement uses training sequence code 2.RFMXGSM_VAL_TSC33 (0x3)The measurement uses training sequence code 3.RFMXGSM_VAL_TSC44 (0x4)The measurement uses training sequence code 4.RFMXGSM_VAL_TSC55 (0x5)The measurement uses training sequence code 5.RFMXGSM_VAL_TSC66 (0x6)The measurement uses training sequence code 6.RFMXGSM_VAL_TSC77 (0x7)The measurement uses training sequence code 7. |
| Name | Value | Description |  |
| RFMXGSM_VAL_TSC0 | 0 (0x0) | The measurement uses training sequence code 0. |  |
| RFMXGSM_VAL_TSC1 | 1 (0x1) | The measurement uses training sequence code 1. |  |
| RFMXGSM_VAL_TSC2 | 2 (0x2) | The measurement uses training sequence code 2. |  |
| RFMXGSM_VAL_TSC3 | 3 (0x3) | The measurement uses training sequence code 3. |  |
| RFMXGSM_VAL_TSC4 | 4 (0x4) | The measurement uses training sequence code 4. |  |
| RFMXGSM_VAL_TSC5 | 5 (0x5) | The measurement uses training sequence code 5. |  |
| RFMXGSM_VAL_TSC6 | 6 (0x6) | The measurement uses training sequence code 6. |  |
| RFMXGSM_VAL_TSC7 | 7 (0x7) | The measurement uses training sequence code 7. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga87296023c7b16287e9d8910d34b5fff5.html language=enus -->
## TOPIC 00168: RFmxGSM_AutoLevel

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga87296023c7b16287e9d8910d34b5fff5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga87296023c7b16287e9d8910d34b5fff5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. Syntaxint32 __stdcall RFmxGSM_AutoLevel(niRFmxInstrHandle instrumentHandle, char sel

### RFmxGSM_AutoLevel

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXGSM_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_g_s_m__attributes_1ga223894ff269f00e623c7f2c242b7d4d6.html) attribute. Use this function to help calculate an approximate setting for the reference level.

#### Syntax

int32 __stdcall RFmxGSM_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64 *referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the [RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](group____root__ni_r_fmx_g_s_m__attributes__advanced_1ga6541550042d6d954d53b917eb4b84f39.html) attribute. Call this function after configuring all signal attributes.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmx GSM Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function, thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| measurementInterval | [in] | float64 | This parameter specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 4.6 ms.Auto Level function does not use any trigger for acquisition. It ignores the user-configured trigger attributes. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | [out] | float64 * | This parameter returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga87299abb3ce0178f894edb44bd888e5b.html language=enus -->
## TOPIC 00169: RFmxGSM_CfgBurstSynchronizationType

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga87299abb3ce0178f894edb44bd888e5b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga87299abb3ce0178f894edb44bd888e5b.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the burst synchronization type. Syntaxint32 __stdcall RFmxGSM_CfgBurstSynchronizationType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 burstSynchronizationType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx

### RFmxGSM_CfgBurstSynchronizationType

Configures the burst synchronization type.

#### Syntax

int32 __stdcall RFmxGSM_CfgBurstSynchronizationType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 burstSynchronizationType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| burstSynchronizationType | [in] | int32 | This parameter specifies the method used to synchronize the burst. The default value is TSC.NameValueDescriptionRFMXGSM_VAL_BURST_SYNC_TYPE_TSC0 (0x0)Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC.RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE1 (0x1)Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope.RFMXGSM_VAL_BURST_SYNC_TYPE_NONE2 (0x2)Sets the T0 point to 273.23 microseconds after the trigger. |
| Name | Value | Description |  |
| RFMXGSM_VAL_BURST_SYNC_TYPE_TSC | 0 (0x0) | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |  |
| RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE | 1 (0x1) | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. |  |
| RFMXGSM_VAL_BURST_SYNC_TYPE_NONE | 2 (0x2) | Sets the T0 point to 273.23 microseconds after the trigger. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga8c7beae3d7ee56ae5f6f0813c33d45a7.html language=enus -->
## TOPIC 00170: RFmxGSM_CfgFrequencyReference

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga8c7beae3d7ee56ae5f6f0813c33d45a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga8c7beae3d7ee56ae5f6f0813c33d45a7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxGSM_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Instrume

### RFmxGSM_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxGSM_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXGSM_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXGSM_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXGSM_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXGSM_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXGSM_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXGSM_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXGSM_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXGSM_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXGSM_VAL_CLK_IN_STR or RFMXGSM_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1ga905646d34ebba30ef629d6060ee2ad75.html language=enus -->
## TOPIC 00171: RFmxGSM_CfgExternalAttenuation

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1ga905646d34ebba30ef629d6060ee2ad75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1ga905646d34ebba30ef629d6060ee2ad75.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. Syntaxint32 __stdcall RFmxGSM_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)ParametersNameDirectionTypeDescriptioninstrumentHandle[i

### RFmxGSM_CfgExternalAttenuation

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

#### Syntax

int32 __stdcall RFmxGSM_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the External Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1gac718f119f7420304338dfd8f7309c90d.html language=enus -->
## TOPIC 00172: RFmxGSM_CfgReferenceLevel

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1gac718f119f7420304338dfd8f7309c90d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1gac718f119f7420304338dfd8f7309c90d.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level, which represents the maximum expected power of an RF input signal. Syntaxint32 __stdcall RFmxGSM_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHa

### RFmxGSM_CfgReferenceLevel

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Syntax

int32 __stdcall RFmxGSM_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this attribute is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1gacd836ed4974e7b0aa617aecaaf430630.html language=enus -->
## TOPIC 00173: RFmxGSM_CfgLinkDirection

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1gacd836ed4974e7b0aa617aecaaf430630.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1gacd836ed4974e7b0aa617aecaaf430630.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the source of the signal to be measured. Syntaxint32 __stdcall RFmxGSM_CfgLinkDirection(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnu

### RFmxGSM_CfgLinkDirection

Configures the source of the signal to be measured.

#### Syntax

int32 __stdcall RFmxGSM_CfgLinkDirection(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| linkDirection | [in] | int32 | This parameter specifies the source of the signal to be measured. The default value is Uplink.NameValueDescriptionRFMXGSM_VAL_LINK_DIRECTION_DOWNLINK0 (0x0)The source is a base transceiver station.RFMXGSM_VAL_LINK_DIRECTION_UPLINK1 (0x1)The source is a mobile station. |
| Name | Value | Description |  |
| RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK | 0 (0x0) | The source is a base transceiver station. |  |
| RFMXGSM_VAL_LINK_DIRECTION_UPLINK | 1 (0x1) | The source is a mobile station. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration_1gaceb3e6a5a077c85b772b68713cecaf35.html language=enus -->
## TOPIC 00174: RFmxGSM_SendSoftwareEdgeTrigger

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration_1gaceb3e6a5a077c85b772b68713cecaf35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration_1gaceb3e6a5a077c85b772b68713cecaf35.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxGSM Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. Syntaxint32 __stdcall RFmxGSM_SendSoftwareEdgeTrigger(niRFm

### RFmxGSM_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use the RFmxGSM Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger.

#### Syntax

int32 __stdcall RFmxGSM_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [RFmxGSM_Initiate](group____root__ni_r_fmx_g_s_m__functions_1ga238434c5965e22ce849f557252113cbe.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__frequency.html language=enus -->
## TOPIC 00175: Frequency

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__frequency.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_CfgFrequencyConfigures the center frequency of the RF signal to acquire. RFmxGSM_CfgFrequencyARFCNConfigures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction. AttachmentsNone

### Frequency

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_CfgFrequency | Configures the center frequency of the RF signal to acquire. |
| RFmxGSM_CfgFrequencyARFCN | Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__frequency_1ga313687e0f8677c2a974045ea7337b9d6.html language=enus -->
## TOPIC 00176: RFmxGSM_CfgFrequencyARFCN

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__frequency_1ga313687e0f8677c2a974045ea7337b9d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__frequency_1ga313687e0f8677c2a974045ea7337b9d6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction. Syntaxint32 __stdcall RFmxGSM_CfgFrequencyARFCN(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 band, int32 arfcn)ParametersNameDirectionTypeDescriptionins

### RFmxGSM_CfgFrequencyARFCN

Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction.

#### Syntax

int32 __stdcall RFmxGSM_CfgFrequencyARFCN(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 band, int32 arfcn)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| linkDirection | [in] | int32 | This parameter specifies the source of the signal to be measured. The default value is Uplink.NameValueDescriptionRFMXGSM_VAL_LINK_DIRECTION_DOWNLINK0 (0x0)The source is a base transceiver station.RFMXGSM_VAL_LINK_DIRECTION_UPLINK1 (0x1)The source is a mobile station. |
| Name | Value | Description |  |
| RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK | 0 (0x0) | The source is a base transceiver station. |  |
| RFMXGSM_VAL_LINK_DIRECTION_UPLINK | 1 (0x1) | The source is a mobile station. |  |
| band | [in] | int32 | This parameter specifies the band of operation. The default value is PGSM.NameValueDescriptionRFMXGSM_VAL_BAND_PGSM0 (0x0)The operation band is Primary GSM in the 900 MHz band.RFMXGSM_VAL_BAND_EGSM1 (0x1)The operation band is Extended GSM in the 900 MHz band.RFMXGSM_VAL_BAND_RGSM2 (0x2)The operation band is Railway GSM in the 900 MHz band.RFMXGSM_VAL_BAND_DCS18003 (0x3)The operation band is GSM in the 1800 MHz band.RFMXGSM_VAL_BAND_PCS19004 (0x4)The operation band is GSM in the 1900 MHz band.RFMXGSM_VAL_BAND_GSM4505 (0x5)The operation band is GSM in the 450 MHz band.RFMXGSM_VAL_BAND_GSM4806 (0x6)The operation band is GSM in the 480 MHz band.RFMXGSM_VAL_BAND_GSM8507 (0x7)The operation band is GSM in the 850 MHz band.RFMXGSM_VAL_BAND_GSM7508 (0x8)The operation band is GSM in the 750 MHz band.RFMXGSM_VAL_BAND_TGSM8109 (0x9)The operation band is terrestrial GSM in the 810 MHz band. |
| Name | Value | Description |  |
| RFMXGSM_VAL_BAND_PGSM | 0 (0x0) | The operation band is Primary GSM in the 900 MHz band. |  |
| RFMXGSM_VAL_BAND_EGSM | 1 (0x1) | The operation band is Extended GSM in the 900 MHz band. |  |
| RFMXGSM_VAL_BAND_RGSM | 2 (0x2) | The operation band is Railway GSM in the 900 MHz band. |  |
| RFMXGSM_VAL_BAND_DCS1800 | 3 (0x3) | The operation band is GSM in the 1800 MHz band. |  |
| RFMXGSM_VAL_BAND_PCS1900 | 4 (0x4) | The operation band is GSM in the 1900 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM450 | 5 (0x5) | The operation band is GSM in the 450 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM480 | 6 (0x6) | The operation band is GSM in the 480 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM850 | 7 (0x7) | The operation band is GSM in the 850 MHz band. |  |
| RFMXGSM_VAL_BAND_GSM750 | 8 (0x8) | The operation band is GSM in the 750 MHz band. |  |
| RFMXGSM_VAL_BAND_TGSM810 | 9 (0x9) | The operation band is terrestrial GSM in the 810 MHz band. |  |
| arfcn | [in] | int32 | This parameter specifies the ARFCN. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__frequency_1ga8f4bbd5cf3d29fd219298ed45103a664.html language=enus -->
## TOPIC 00177: RFmxGSM_CfgFrequency

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__frequency_1ga8f4bbd5cf3d29fd219298ed45103a664.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__frequency_1ga8f4bbd5cf3d29fd219298ed45103a664.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency of the RF signal to acquire. Syntaxint32 __stdcall RFmxGSM_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx sess

### RFmxGSM_CfgFrequency

Configures the center frequency of the RF signal to acquire.

#### Syntax

int32 __stdcall RFmxGSM_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. The default of this attribute is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__modacc.html language=enus -->
## TOPIC 00178: ModAcc

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__modacc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_ModAccCfgAveragingConfigures averaging for the modulation accuracy (ModAcc) measurement. RFmxGSM_ModAccCfgDroopCompensationEnabledConfigures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. AttachmentsNone

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_ModAccCfgAveraging | Configures averaging for the modulation accuracy (ModAcc) measurement. |
| RFmxGSM_ModAccCfgDroopCompensationEnabled | Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__modacc_1gac3dce9ee72e85650d95a79c8d9ee2c36.html language=enus -->
## TOPIC 00179: RFmxGSM_ModAccCfgDroopCompensationEnabled

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__modacc_1gac3dce9ee72e85650d95a79c8d9ee2c36.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__modacc_1gac3dce9ee72e85650d95a79c8d9ee2c36.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. Syntaxint32 __stdcall RFmxGSM_ModAccCfgDroopCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 droopCompensationEnabled)ParametersNameDirectionTypeDescriptioninstrument

### RFmxGSM_ModAccCfgDroopCompensationEnabled

Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement.

#### Syntax

int32 __stdcall RFmxGSM_ModAccCfgDroopCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 droopCompensationEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| droopCompensationEnabled | [in] | int32 | This parameter specifies whether to enable droop compensation for the ModAcc measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. The default value is False.NameValueDescriptionRFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE0 (0x0)Disables power droop compensation in the EVM measurement.RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE1 (0x1)Enables power droop compensation in the EVM measurement. |
| Name | Value | Description |  |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables power droop compensation in the EVM measurement. |  |
| RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables power droop compensation in the EVM measurement. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__modacc_1gaf473c47d424d0db5f7ff56a47989785a.html language=enus -->
## TOPIC 00180: RFmxGSM_ModAccCfgAveraging

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__modacc_1gaf473c47d424d0db5f7ff56a47989785a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__modacc_1gaf473c47d424d0db5f7ff56a47989785a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the modulation accuracy (ModAcc) measurement. Syntaxint32 __stdcall RFmxGSM_ModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleT

### RFmxGSM_ModAccCfgAveraging

Configures averaging for the modulation accuracy (ModAcc) measurement.

#### Syntax

int32 __stdcall RFmxGSM_ModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE1 (0x1)The measurement is averaged over multiple acquisitions. |
| Name | Value | Description |  |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement is averaged over multiple acquisitions. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs.html language=enus -->
## TOPIC 00181: ORFS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_ORFSCfgAveragingConfigures averaging for the output radio frequency spectrum (ORFS) measurement. RFmxGSM_ORFSCfgEvaluationSymbolsConfigures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, b

### ORFS

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_ORFSCfgAveraging | Configures averaging for the output radio frequency spectrum (ORFS) measurement. |
| RFmxGSM_ORFSCfgEvaluationSymbols | Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average. |
| RFmxGSM_ORFSCfgMeasurementType | Configures the type of spectral distortion to be measured. |
| RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to Custom. |
| RFmxGSM_ORFSCfgNoiseCompensationEnabled | Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxGSM_ORFSCfgOffsetFrequencyMode | Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
| RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to Custom. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga1ffb15249fdb0e1c86271b89fdababc1.html language=enus -->
## TOPIC 00182: RFmxGSM_ORFSCfgAveraging

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga1ffb15249fdb0e1c86271b89fdababc1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga1ffb15249fdb0e1c86271b89fdababc1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the output radio frequency spectrum (ORFS) measurement. Syntaxint32 __stdcall RFmxGSM_ORFSCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumen

### RFmxGSM_ORFSCfgAveraging

Configures averaging for the output radio frequency spectrum (ORFS) measurement.

#### Syntax

int32 __stdcall RFmxGSM_ORFSCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXGSM_VAL_ORFS_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_TRUE1 (0x1)The measurement is averaged over multiple acquisitions. |
| Name | Value | Description |  |
| RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement is averaged over multiple acquisitions. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is Log.NameValueDescriptionRFMXGSM_VAL_ORFS_AVERAGING_TYPE_RMS0 (0x0)The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor.RFMXGSM_VAL_ORFS_AVERAGING_TYPE_LOG1 (0x1)The measurement averages the power spectrum in a logarithmic scale. |
| Name | Value | Description |  |
| RFMXGSM_VAL_ORFS_AVERAGING_TYPE_RMS | 0 (0x0) | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXGSM_VAL_ORFS_AVERAGING_TYPE_LOG | 1 (0x1) | The measurement averages the power spectrum in a logarithmic scale. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga55703ab1e8ca8261bbffb3e4463b011d.html language=enus -->
## TOPIC 00183: RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga55703ab1e8ca8261bbffb3e4463b011d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga55703ab1e8ca8261bbffb3e4463b011d.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to Custom. Syntaxint32 __stdcall RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray(niRFmxInstrHan

### RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the [RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE](group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga0039de8c02f6d3452405122c707cf09d.html) attribute to **Custom**.

#### Syntax

int32 __stdcall RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float32 switchingCustomOffsetFrequency[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| switchingCustomOffsetFrequency | [in] | float32[] | This parameter specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga5ddcc0c21e158adca71ac6e1e6baa477.html language=enus -->
## TOPIC 00184: RFmxGSM_ORFSCfgEvaluationSymbols

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga5ddcc0c21e158adca71ac6e1e6baa477.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga5ddcc0c21e158adca71ac6e1e6baa477.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a

### RFmxGSM_ORFSCfgEvaluationSymbols

Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average.

#### Syntax

int32 __stdcall RFmxGSM_ORFSCfgEvaluationSymbols(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 evaluationSymbolsStart, int32 evaluationSymbolsIncludeTsc, float64 evaluationSymbolsStop)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| evaluationSymbolsStart | [in] | float64 | This parameter specifies the start position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. The default value is 50. |
| evaluationSymbolsIncludeTsc | [in] | int32 | This parameter specifies whether to include the TSC portion of burst in the ORFS measurement. The default value is False.NameValueDescriptionRFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_FALSE0 (0x0)The TSC portion of the burst will be excluded while performing the ORFS measurement.RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_TRUE1 (0x1)The TSC portion of the burst will be included while performing the ORFS measurement. |
| Name | Value | Description |  |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_FALSE | 0 (0x0) | The TSC portion of the burst will be excluded while performing the ORFS measurement. |  |
| RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_TRUE | 1 (0x1) | The TSC portion of the burst will be included while performing the ORFS measurement. |  |
| evaluationSymbolsStop | [in] | float64 | This parameter specifies the stop position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. The default value is 90. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga685ce512ba2b77c1ab95f18d3e540196.html language=enus -->
## TOPIC 00185: RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga685ce512ba2b77c1ab95f18d3e540196.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga685ce512ba2b77c1ab95f18d3e540196.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to Custom. Syntaxint32 __stdcall RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray(niRFmxInstrH

### RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the [RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE](group____root__ni_r_fmx_g_s_m__attributes__orfs_1ga0039de8c02f6d3452405122c707cf09d.html) attribute to **Custom**.

#### Syntax

int32 __stdcall RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float32 modulationCustomOffsetFrequency[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| modulationCustomOffsetFrequency | [in] | float32[] | This parameter specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of modulation when you set the RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE attribute to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga81aafd1feffeb1968f259bf143447e66.html language=enus -->
## TOPIC 00186: RFmxGSM_ORFSCfgOffsetFrequencyMode

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga81aafd1feffeb1968f259bf143447e66.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1ga81aafd1feffeb1968f259bf143447e66.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. Syntaxint32 __stdcall RFmxGSM_ORFSCfgOffsetFrequencyMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetFrequencyMode)ParametersNameDirectionTypeDescrip

### RFmxGSM_ORFSCfgOffsetFrequencyMode

Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

#### Syntax

int32 __stdcall RFmxGSM_ORFSCfgOffsetFrequencyMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetFrequencyMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| offsetFrequencyMode | [in] | int32 | This parameter specifies the list of frequency offsets for which you can perform the ORFS measurements. The default value is Standard.NameValueDescriptionRFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_STANDARD0 (0x0)Uses the list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement.RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_SHORT1 (0x1)Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement.RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM2 (0x2)Uses the list of frequencies that is configured using the RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray and RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray functions for measurement of spectrum produced by modulation and switching measurements. |
| Name | Value | Description |  |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_STANDARD | 0 (0x0) | Uses the list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |  |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_SHORT | 1 (0x1) | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |  |
| RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM | 2 (0x2) | Uses the list of frequencies that is configured using the RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray and RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray functions for measurement of spectrum produced by modulation and switching measurements. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1gaefdd0601bd7b1e62dd713fa3e15fa157.html language=enus -->
## TOPIC 00187: RFmxGSM_ORFSCfgNoiseCompensationEnabled

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1gaefdd0601bd7b1e62dd713fa3e15fa157.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1gaefdd0601bd7b1e62dd713fa3e15fa157.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Syntaxint32 __stdcall RFmxGSM_ORFSCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)ParametersNameDirectionTypeDesc

### RFmxGSM_ORFSCfgNoiseCompensationEnabled

Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

#### Syntax

int32 __stdcall RFmxGSM_ORFSCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| noiseCompensationEnabled | [in] | int32 | This parameter specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False.NameValueDescriptionRFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE0 (0x0)Disables compensation of the channel powers for the signal analyzer noise floor.RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE1 (0x1)Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |
| Name | Value | Description |  |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables compensation of the channel powers for the signal analyzer noise floor. |  |
| RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1gafbe9a49921bd8deeb5c45ad72cf57ab2.html language=enus -->
## TOPIC 00188: RFmxGSM_ORFSCfgMeasurementType

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1gafbe9a49921bd8deeb5c45ad72cf57ab2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__orfs_1gafbe9a49921bd8deeb5c45ad72cf57ab2.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of spectral distortion to be measured. Syntaxint32 __stdcall RFmxGSM_ORFSCfgMeasurementType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFm

### RFmxGSM_ORFSCfgMeasurementType

Configures the type of spectral distortion to be measured.

#### Syntax

int32 __stdcall RFmxGSM_ORFSCfgMeasurementType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| measurementType | [in] | int32 | This parameter specifies the type of spectral distortion to be measured. The default value is Modulation and Switching.NameValueDescriptionRFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING0 (0x0)Measures the spectrum on the modulated part and the switching part of the waveform.RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION1 (0x1)Measures the spectrum on the modulated part of the waveform.RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_SWITCHING2 (0x2)Measures the spectrum on the switching part of the waveform. |
| Name | Value | Description |  |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING | 0 (0x0) | Measures the spectrum on the modulated part and the switching part of the waveform. |  |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION | 1 (0x1) | Measures the spectrum on the modulated part of the waveform. |  |
| RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_SWITCHING | 2 (0x2) | Measures the spectrum on the switching part of the waveform. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__pvt.html language=enus -->
## TOPIC 00189: PVT

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__pvt.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_PVTCfgAveragingConfigures averaging for the power versus time (PVT) measurement. AttachmentsNone

### PVT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_PVTCfgAveraging | Configures averaging for the power versus time (PVT) measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__pvt_1gab4ad0aae3fd7769d522f3a14f6175cff.html language=enus -->
## TOPIC 00190: RFmxGSM_PVTCfgAveraging

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__pvt_1gab4ad0aae3fd7769d522f3a14f6175cff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__pvt_1gab4ad0aae3fd7769d522f3a14f6175cff.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the power versus time (PVT) measurement. Syntaxint32 __stdcall RFmxGSM_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFm

### RFmxGSM_PVTCfgAveraging

Configures averaging for the power versus time (PVT) measurement.

#### Syntax

int32 __stdcall RFmxGSM_PVTCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE1 (0x1)The measurement is averaged over multiple acquisitions. |
| Name | Value | Description |  |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement is averaged over multiple acquisitions. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS0 (0x0)The power at each sample interval is linearly averaged from one acquisition to the next acquisition.RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG1 (0x1)The power at each sample interval is averaged on a logarithmic scale from one acquisition to the next acquisition.RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM3 (0x3)The peak power at each sample interval is retained from one acquisition to the next acquisition.RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM4 (0x4)The lowest power at each sample interval is retained from one acquisition to the next acquisition. |
| Name | Value | Description |  |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS | 0 (0x0) | The power at each sample interval is linearly averaged from one acquisition to the next acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG | 1 (0x1) | The power at each sample interval is averaged on a logarithmic scale from one acquisition to the next acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power at each sample interval is retained from one acquisition to the next acquisition. |  |
| RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The lowest power at each sample interval is retained from one acquisition to the next acquisition. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__trigger.html language=enus -->
## TOPIC 00191: Trigger

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__trigger.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_CfgDigitalEdgeTriggerConfigures the device to wait for a digital edge trigger and then marks a reference point within the record. RFmxGSM_CfgIQPowerEdgeTriggerConfigures the device to wait for the complex power of the I/Q data to cross the specified thre

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_CfgDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| RFmxGSM_CfgIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst. |
| RFmxGSM_CfgSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| RFmxGSM_DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga1f5518625adce5d35153113100dc244e.html language=enus -->
## TOPIC 00192: RFmxGSM_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga1f5518625adce5d35153113100dc244e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga1f5518625adce5d35153113100dc244e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxGSM_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptionins

### RFmxGSM_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxGSM_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga3b6c6797f79ce0595c22b579ad8e3ad6.html language=enus -->
## TOPIC 00193: RFmxGSM_DisableTrigger

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga3b6c6797f79ce0595c22b579ad8e3ad6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga3b6c6797f79ce0595c22b579ad8e3ad6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxGSM_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrument

### RFmxGSM_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxGSM_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga8d0bf3e6cc42467bc78f3c8e226a0e95.html language=enus -->
## TOPIC 00194: RFmxGSM_CfgDigitalEdgeTrigger

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga8d0bf3e6cc42467bc78f3c8e226a0e95.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1ga8d0bf3e6cc42467bc78f3c8e226a0e95.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxGSM_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableT

### RFmxGSM_CfgDigitalEdgeTrigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxGSM_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital-edge trigger. The default of this attribute is hardware dependent.Name (Value)DescriptionPFI0 (PFI0)The trigger is received on PFI 0.PFI1 (PFI1)The trigger is received on PFI 1.PXI_Trig0 (PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1 (PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2 (PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3 (PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4 (PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5 (PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6 (PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7 (PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR (PXI_STAR)The trigger is received on the PXI star trigger line. |
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
| digitalEdge | [in] | int32 | This parameter specifies the active edge for the trigger. This parameter is used only when you set the RFMXGSM_ATTR_TRIGGER_TYPE attribute to Digital Edge. The default value is Rising Edge.NameValueDescriptionRFMXGSM_VAL_DIGITAL_EDGE_RISING_EDGE0 (0x0)The trigger asserts on the rising edge of the signal.RFMXGSM_VAL_DIGITAL_EDGE_FALLING_EDGE1 (0x1)The trigger asserts on the falling edge of the signal. |
| Name | Value | Description |  |
| RFMXGSM_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |  |
| RFMXGSM_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1gadc85f636fe32ffd6493085a9bf59c1a3.html language=enus -->
## TOPIC 00195: RFmxGSM_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1gadc85f636fe32ffd6493085a9bf59c1a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__configuration__trigger_1gadc85f636fe32ffd6493085a9bf59c1a3.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The qu

### RFmxGSM_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

#### Syntax

int32 __stdcall RFmxGSM_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. The default of this attribute is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQ Power Edge Level parameter with the slope you specify. The default value is Rising Slope.NameValueDescriptionRFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE0 (0x0)The trigger asserts when the signal power is rising.RFMXGSM_VAL_IQ_POWER_EDGE_FALLING_SLOPE1 (0x1)The trigger asserts when the signal power is falling. |
| Name | Value | Description |  |
| RFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |  |
| RFMXGSM_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |  |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative; and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this attribute is hardware dependent. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| minimumQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto.NameValueDescriptionRFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL0 (0x0)The minimum quiet time for triggering is the value of the RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute.RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO1 (0x1)The measurement computes the minimum quiet time used for triggering. |
| Name | Value | Description |  |
| RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |  |
| RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |  |
| minimumQuietTime | [in] | float64 | This parameter specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet above the trigger level. The default value is 582 µs. |
| iqPowerEdgeLevelType | [in] | int32 | This parameter specifies the reference for the IQ Power Edge Level parameter. The default value is Relative.NameValueDescriptionRFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE0 (0x0)The value of the IQ Power Edge Level attribute is relative to the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute.RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE1 (0x1)The IQ Power Edge Level attribute specifies the absolute power. |
| Name | Value | Description |  |
| RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The value of the IQ Power Edge Level attribute is relative to the value of the RFMXGSM_ATTR_REFERENCE_LEVEL attribute. |  |
| RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |  |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch.html language=enus -->
## TOPIC 00196: Fetch

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsModAccORFSPVTGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- ModAcc
- ORFS
- PVT

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc.html language=enus -->
## TOPIC 00197: ModAcc

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_ModAccFetchConstellationTraceFetches the constellation trace concatenated over all the measured time slots for the last acquisition. RFmxGSM_ModAccFetchConstellationTraceSplitFetches the constellation trace concatenated over all the measured time slots f

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_ModAccFetchConstellationTrace | Fetches the constellation trace concatenated over all the measured time slots for the last acquisition. |
| RFmxGSM_ModAccFetchConstellationTraceSplit | Fetches the constellation trace concatenated over all the measured time slots for the last acquisition. |
| RFmxGSM_ModAccFetchDemodulatedBits | Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition. |
| RFmxGSM_ModAccFetchDetectedTSC | Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. |
| RFmxGSM_ModAccFetchDetectedTSCArray | Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. |
| RFmxGSM_ModAccFetchEVM | Fetches the EVM measurement results for EDGE/EGPRS. |
| RFmxGSM_ModAccFetchEVMAmplitudeDroop | Fetches the amplitude droop measurement results for EDGE/EGPRS. |
| RFmxGSM_ModAccFetchEVMMagnitudeError | Fetches the magnitude error measurement results for EDGE/EGPRS. |
| RFmxGSM_ModAccFetchEVMPhaseError | Fetches the phase error measurement results for EDGE/EGPRS. |
| RFmxGSM_ModAccFetchEVMTrace | Fetches the EDGE/EGPRS RMS EVM trace concatenated over all the measured time slots for the last acquisition. |
| RFmxGSM_ModAccFetchIQImpairments | Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS. |
| RFmxGSM_ModAccFetchMagnitudeErrorTrace | Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition. |
| RFmxGSM_ModAccFetchPFER | Fetches the phase and frequency error measurement results for GSM. |
| RFmxGSM_ModAccFetchPhaseErrorTrace | Fetches the phase error trace concatenated over all the measured time slots for the last acquisition. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga052fea241dd701713d2177ec6034a11e.html language=enus -->
## TOPIC 00198: RFmxGSM_ModAccFetchMagnitudeErrorTrace

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga052fea241dd701713d2177ec6034a11e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga052fea241dd701713d2177ec6034a11e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition. Syntaxint32 __stdcall RFmxGSM_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeErr

### RFmxGSM_ModAccFetchMagnitudeErrorTrace

Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| magnitudeError | [out] | float32[] | This parameter returns an array of magnitude error values measured at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga21be54bbbdf51151793f0b105879205a.html language=enus -->
## TOPIC 00199: RFmxGSM_ModAccFetchConstellationTrace

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga21be54bbbdf51151793f0b105879205a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga21be54bbbdf51151793f0b105879205a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace concatenated over all the measured time slots for the last acquisition. Syntaxint32 __stdcall RFmxGSM_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellationTrace[], int32 arraySize, int32

### RFmxGSM_ModAccFetchConstellationTrace

Fetches the constellation trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellationTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellationTrace | [out] | NIComplexSingle[] | This parameter returns the constellation trace concatenated over all the measured time slots for the last acquisition. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga4f733cf4979d9c5fad05bf8dc48b91e1.html language=enus -->
## TOPIC 00200: RFmxGSM_ModAccFetchEVMAmplitudeDroop

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga4f733cf4979d9c5fad05bf8dc48b91e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga4f733cf4979d9c5fad05bf8dc48b91e1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the amplitude droop measurement results for EDGE/EGPRS. Syntaxint32 __stdcall RFmxGSM_ModAccFetchEVMAmplitudeDroop(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanAmplitudeDroop, float64 *maximumAmplitudeDroop)ParametersNameDirectionTypeDescriptionins

### RFmxGSM_ModAccFetchEVMAmplitudeDroop

Fetches the amplitude droop measurement results for EDGE/EGPRS.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchEVMAmplitudeDroop(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanAmplitudeDroop, float64 *maximumAmplitudeDroop)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanAmplitudeDroop | [out] | float64 * | This parameter returns the mean of amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. |
| maximumAmplitudeDroop | [out] | float64 * | This parameter returns the maximum of amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga5743e0fc566d33471148714ae6f8960e.html language=enus -->
## TOPIC 00201: RFmxGSM_ModAccFetchDetectedTSC

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga5743e0fc566d33471148714ae6f8960e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga5743e0fc566d33471148714ae6f8960e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. Syntaxint32 __stdcall RFmxGSM_ModAccFetchDetectedTSC(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedTsc)RemarksUse "slot<n>" as the selector string to read results from

### RFmxGSM_ModAccFetchDetectedTSC

Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchDetectedTSC(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedTsc)

#### Remarks

Use "slot<n>" as the selector string to read results from this function.

When the [RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL](group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga329596c0c00f21d49dbc81d2a5a98419.html) attribute is set to **Timeslot at Offset**, Detected TSC array has one element and the Detected TSC is returned at index 0.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"slot0""signal::sig1/slot0""result::r1/slot0""signal::sig1/result::r1/slot0"You can use the RFmxGSM_BuildSlotString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedTsc | [out] | int32 * | This parameter returns the detected TSC when you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to TSC.NameValueDescriptionRFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN-1 (-0x1)The synchronization is not found, and measurements correspond to best estimate of synchronization.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC00 (0x0)The detected TSC is TSC0.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC11 (0x1)The detected TSC is TSC1.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC22 (0x2)The detected TSC is TSC2.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC33 (0x3)The detected TSC is TSC3.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC44 (0x4)The detected TSC is TSC4.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC55 (0x5)The detected TSC is TSC5.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC66 (0x6)The detected TSC is TSC6.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC77 (0x7)The detected TSC is TSC7. |
| Name | Value | Description |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN | -1 (-0x1) | The synchronization is not found, and measurements correspond to best estimate of synchronization. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 | 0 (0x0) | The detected TSC is TSC0. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 | 1 (0x1) | The detected TSC is TSC1. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 | 2 (0x2) | The detected TSC is TSC2. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 | 3 (0x3) | The detected TSC is TSC3. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 | 4 (0x4) | The detected TSC is TSC4. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 | 5 (0x5) | The detected TSC is TSC5. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 | 6 (0x6) | The detected TSC is TSC6. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 | 7 (0x7) | The detected TSC is TSC7. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga5cebe87e8db25f6fcd3a0805e3db0654.html language=enus -->
## TOPIC 00202: RFmxGSM_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga5cebe87e8db25f6fcd3a0805e3db0654.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga5cebe87e8db25f6fcd3a0805e3db0654.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace concatenated over all the measured time slots for the last acquisition. Syntaxint32 __stdcall RFmxGSM_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationTraceI[], float32 constellationTra

### RFmxGSM_ModAccFetchConstellationTraceSplit

Fetches the constellation trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationTraceI[], float32 constellationTraceQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellationTraceI | [out] | float32[] | This parameter Returns the real part of constellation trace concatenated over all the measured time slots for the last acquisition. |
| constellationTraceQ | [out] | float32[] | This parameter Returns the imaginary part of constellation trace concatenated over all the measured time slots for the last acquisition. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga65fa26f0bb833bc4ed90f88b42219a17.html language=enus -->
## TOPIC 00203: RFmxGSM_ModAccFetchEVMTrace

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga65fa26f0bb833bc4ed90f88b42219a17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga65fa26f0bb833bc4ed90f88b42219a17.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EDGE/EGPRS RMS EVM trace concatenated over all the measured time slots for the last acquisition. Syntaxint32 __stdcall RFmxGSM_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *

### RFmxGSM_ModAccFetchEVMTrace

Fetches the EDGE/EGPRS RMS EVM trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| evm | [out] | float32[] | This parameter returns the EVM trace measured at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga735fdcbd4c49c5f24c00c8496fe36348.html language=enus -->
## TOPIC 00204: RFmxGSM_ModAccFetchIQImpairments

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga735fdcbd4c49c5f24c00c8496fe36348.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga735fdcbd4c49c5f24c00c8496fe36348.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS. Syntaxint32 __stdcall RFmxGSM_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanIQGainImbalance, float64 *maximumIQGainImbalance, float64 *meanIQOrigin

### RFmxGSM_ModAccFetchIQImpairments

Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanIQGainImbalance, float64 *maximumIQGainImbalance, float64 *meanIQOriginOffset, float64 *maximumIQOriginOffset)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanIQGainImbalance | [out] | float64 * | This parameter returns the mean of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| maximumIQGainImbalance | [out] | float64 * | This parameter returns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
| meanIQOriginOffset | [out] | float64 * | This parameter returns the mean of I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |
| maximumIQOriginOffset | [out] | float64 * | This parameter returns the maximum of I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga77d2de83933a2ae8a543e1164e3500f3.html language=enus -->
## TOPIC 00205: RFmxGSM_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga77d2de83933a2ae8a543e1164e3500f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga77d2de83933a2ae8a543e1164e3500f3.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace concatenated over all the measured time slots for the last acquisition. Syntaxint32 __stdcall RFmxGSM_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize,

### RFmxGSM_ModAccFetchPhaseErrorTrace

Fetches the phase error trace concatenated over all the measured time slots for the last acquisition.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in symbols. |
| phaseError | [out] | float32[] | This parameter returns an array of phase error values measured at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga8707ce28afb2dea8615673d739d2ba42.html language=enus -->
## TOPIC 00206: RFmxGSM_ModAccFetchEVMPhaseError

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga8707ce28afb2dea8615673d739d2ba42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga8707ce28afb2dea8615673d739d2ba42.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error measurement results for EDGE/EGPRS. Syntaxint32 __stdcall RFmxGSM_ModAccFetchEVMPhaseError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanPhaseError, float64 *maximumPhaseError)ParametersNameDirectionTypeDescriptioninstrumentHandle[in

### RFmxGSM_ModAccFetchEVMPhaseError

Fetches the phase error measurement results for EDGE/EGPRS.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchEVMPhaseError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanPhaseError, float64 *maximumPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanPhaseError | [out] | float64 * | This parameter returns the mean of RMS values of phase error over all the measured time slots. This value is expressed in degrees. |
| maximumPhaseError | [out] | float64 * | This parameter returns the maximum of RMS values of phase error over all the measured time slots. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga881e054811e08814ff1c6ca117f822d1.html language=enus -->
## TOPIC 00207: RFmxGSM_ModAccFetchEVMMagnitudeError

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga881e054811e08814ff1c6ca117f822d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1ga881e054811e08814ff1c6ca117f822d1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error measurement results for EDGE/EGPRS. Syntaxint32 __stdcall RFmxGSM_ModAccFetchEVMMagnitudeError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanMagnitudeError, float64 *maximumMagnitudeError)ParametersNameDirectionTypeDescriptionins

### RFmxGSM_ModAccFetchEVMMagnitudeError

Fetches the magnitude error measurement results for EDGE/EGPRS.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchEVMMagnitudeError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanMagnitudeError, float64 *maximumMagnitudeError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanMagnitudeError | [out] | float64 * | This parameter returns the mean of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. |
| maximumMagnitudeError | [out] | float64 * | This parameter returns the maximum of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaa0a3572ac29ae351ed1f840667ae872e.html language=enus -->
## TOPIC 00208: RFmxGSM_ModAccFetchDetectedTSCArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaa0a3572ac29ae351ed1f840667ae872e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaa0a3572ac29ae351ed1f840667ae872e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. Syntaxint32 __stdcall RFmxGSM_ModAccFetchDetectedTSCArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedTsc[], int32 arraySize, int32 *actualArraySize)RemarksWhen

### RFmxGSM_ModAccFetchDetectedTSCArray

Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchDetectedTSCArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedTsc[], int32 arraySize, int32 *actualArraySize)

#### Remarks

When the [RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL](group____root__ni_r_fmx_g_s_m__attributes__modacc_1ga329596c0c00f21d49dbc81d2a5a98419.html) attribute is set to **Timeslot at Offset**, Detected TSC array has one element and the Detected TSC is returned at index 0.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedTsc | [out] | int32[] | This parameter returns an array of the detected TSCs when you set the RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE attribute to TSC.NameValueDescriptionRFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN-1 (-0x1)The synchronization is not found, and measurements correspond to best estimate of synchronization.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC00 (0x0)The detected TSC is TSC0.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC11 (0x1)The detected TSC is TSC1.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC22 (0x2)The detected TSC is TSC2.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC33 (0x3)The detected TSC is TSC3.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC44 (0x4)The detected TSC is TSC4.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC55 (0x5)The detected TSC is TSC5.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC66 (0x6)The detected TSC is TSC6.RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC77 (0x7)The detected TSC is TSC7. |
| Name | Value | Description |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN | -1 (-0x1) | The synchronization is not found, and measurements correspond to best estimate of synchronization. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0 | 0 (0x0) | The detected TSC is TSC0. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1 | 1 (0x1) | The detected TSC is TSC1. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2 | 2 (0x2) | The detected TSC is TSC2. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3 | 3 (0x3) | The detected TSC is TSC3. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4 | 4 (0x4) | The detected TSC is TSC4. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5 | 5 (0x5) | The detected TSC is TSC5. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6 | 6 (0x6) | The detected TSC is TSC6. |  |
| RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7 | 7 (0x7) | The detected TSC is TSC7. |  |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaccb7d1594724270b70b68c08ab84e7c1.html language=enus -->
## TOPIC 00209: RFmxGSM_ModAccFetchDemodulatedBits

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaccb7d1594724270b70b68c08ab84e7c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaccb7d1594724270b70b68c08ab84e7c1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition. Syntaxint32 __stdcall RFmxGSM_ModAccFetchDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 demodulatedBits[], int32 arraySize, int32 *actualArr

### RFmxGSM_ModAccFetchDemodulatedBits

Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 demodulatedBits[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| demodulatedBits | [out] | int8[] | This parameter returns an array of demodulated bits concatenated over all the measured time slots for the last acquisition. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gace4dace15dcb744188eb5bfb6f8eadba.html language=enus -->
## TOPIC 00210: RFmxGSM_ModAccFetchEVM

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gace4dace15dcb744188eb5bfb6f8eadba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gace4dace15dcb744188eb5bfb6f8eadba.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM measurement results for EDGE/EGPRS. Syntaxint32 __stdcall RFmxGSM_ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSEVM, float64 *maximumRMSEVM, float64 *meanPeakEVM, float64 *maximumPeakEVM, float64 *ninetyFifthPercentileEVM,

### RFmxGSM_ModAccFetchEVM

Fetches the EVM measurement results for EDGE/EGPRS.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSEVM, float64 *maximumRMSEVM, float64 *meanPeakEVM, float64 *maximumPeakEVM, float64 *ninetyFifthPercentileEVM, float64 *meanFrequencyError, int32 *peakEVMSymbol)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSEVM | [out] | float64 * | This parameter returns the mean of RMS EVM values over all the measured time slots. This value is expressed as a percentage. |
| maximumRMSEVM | [out] | float64 * | This parameter returns the maximum of RMS EVM values over all the measured time slots. This value is expressed as a percentage. |
| meanPeakEVM | [out] | float64 * | This parameter returns the mean of peak EVM values over all the measured time slots. This value is expressed as a percentage. |
| maximumPeakEVM | [out] | float64 * | This parameter returns the maximum of peak EVM values over all the measured time slots. This value is expressed as a percentage. |
| ninetyFifthPercentileEVM | [out] | float64 * | This parameter returns the EVM value, at which no more than 5 percent of the symbols have an EVM exceeding this value. This value is expressed as a percentage. |
| meanFrequencyError | [out] | float64 * | This parameter returns the mean of frequency error values over all the measured time slots. This value is expressed in Hz. |
| peakEVMSymbol | [out] | int32 * | This parameter returns the symbol number in the useful portion of the burst corresponding to Maximum Peak EVM parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaed0aee87535e4a773ffb8e45c2975196.html language=enus -->
## TOPIC 00211: RFmxGSM_ModAccFetchPFER

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaed0aee87535e4a773ffb8e45c2975196.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__modacc_1gaed0aee87535e4a773ffb8e45c2975196.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase and frequency error measurement results for GSM. Syntaxint32 __stdcall RFmxGSM_ModAccFetchPFER(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSPhaseError, float64 *maximumRMSPhaseError, float64 *meanPeakPhaseError, float64 *maximumPeakPha

### RFmxGSM_ModAccFetchPFER

Fetches the phase and frequency error measurement results for GSM.

#### Syntax

int32 __stdcall RFmxGSM_ModAccFetchPFER(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSPhaseError, float64 *maximumRMSPhaseError, float64 *meanPeakPhaseError, float64 *maximumPeakPhaseError, float64 *meanFrequencyError, int32 *peakSymbol)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSPhaseError | [out] | float64 * | This parameter returns the mean of RMS phase error values over all the measured time slots. This value is expressed in degrees. |
| maximumRMSPhaseError | [out] | float64 * | This parameter returns the maximum of RMS phase error values over all the measured time slots. This value is expressed in degrees. |
| meanPeakPhaseError | [out] | float64 * | This parameter returns the mean of peak phase error values over all the measured time slots. This value is expressed in degrees. |
| maximumPeakPhaseError | [out] | float64 * | This parameter returns the maximum of peak phase error values over all the measured time slots. This value is expressed in degrees. |
| meanFrequencyError | [out] | float64 * | This parameter returns the mean of frequency error values over all the measured time slots. This value is expressed in Hz. |
| peakSymbol | [out] | int32 * | This parameter returns the symbol number in the useful portion of the burst corresponding to phase error value in the Maximum Peak Phase Error parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__orfs.html language=enus -->
## TOPIC 00212: ORFS

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__orfs.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__orfs.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_ORFSFetchModulationPowerTraceFetches the modulation power trace and frequency offset. RFmxGSM_ORFSFetchModulationResultsArrayReturns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The rel

### ORFS

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_ORFSFetchModulationPowerTrace | Fetches the modulation power trace and frequency offset. |
| RFmxGSM_ORFSFetchModulationResultsArray | Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier. |
| RFmxGSM_ORFSFetchSwitchingPowerTrace | Fetches the switching power trace and frequency offsets. |
| RFmxGSM_ORFSFetchSwitchingResultsArray | Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1ga3120e08010a2f4fba72a819d48467dd2.html language=enus -->
## TOPIC 00213: RFmxGSM_ORFSFetchSwitchingPowerTrace

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1ga3120e08010a2f4fba72a819d48467dd2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1ga3120e08010a2f4fba72a819d48467dd2.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the switching power trace and frequency offsets. Syntaxint32 __stdcall RFmxGSM_ORFSFetchSwitchingPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 offsetFrequency[], float32 absolutePower[], float32 relativePower[], int32 arraySize, int32 *actualA

### RFmxGSM_ORFSFetchSwitchingPowerTrace

Fetches the switching power trace and frequency offsets.

#### Syntax

int32 __stdcall RFmxGSM_ORFSFetchSwitchingPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 offsetFrequency[], float32 absolutePower[], float32 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| offsetFrequency | [out] | float32[] | This parameter returns an array of switching offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
| absolutePower | [out] | float32[] | This parameter returns an array of absolute powers corresponding to the switching offset frequency list. This value is expressed in dBm. |
| relativePower | [out] | float32[] | This parameter returns an array of relative powers corresponding to the switching offset frequencies. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1ga85ed73736acae16d931d658c482cad8e.html language=enus -->
## TOPIC 00214: RFmxGSM_ORFSFetchSwitchingResultsArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1ga85ed73736acae16d931d658c482cad8e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1ga85ed73736acae16d931d658c482cad8e.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier. Syntaxint32 __stdcall RFmxGSM_ORFSFetchSwitchingResultsArray(niRFmxInstrHandle instrumen

### RFmxGSM_ORFSFetchSwitchingResultsArray

Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier.

#### Syntax

int32 __stdcall RFmxGSM_ORFSFetchSwitchingResultsArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *switchingCarrierPower, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| switchingCarrierPower | [out] | float64 * | This parameter returns the switching carrier power. This value is expressed in dBm. |
| lowerRelativePower | [out] | float64[] | This parameter returns an array of relative powers measured at the negative switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
| upperRelativePower | [out] | float64[] | This parameter returns an array of relative powers measured at the positive switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
| lowerAbsolutePower | [out] | float64[] | This parameter returns an array of absolute powers measured at the negative switching offset frequencies. This value is expressed in dBm. |
| upperAbsolutePower | [out] | float64[] | This parameter returns an array of absolute powers measured at the positive switching offset frequencies. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1gaf7bb9e2fb37e3d54c6a8d34ad44b787f.html language=enus -->
## TOPIC 00215: RFmxGSM_ORFSFetchModulationPowerTrace

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1gaf7bb9e2fb37e3d54c6a8d34ad44b787f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1gaf7bb9e2fb37e3d54c6a8d34ad44b787f.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the modulation power trace and frequency offset. Syntaxint32 __stdcall RFmxGSM_ORFSFetchModulationPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 offsetFrequency[], float32 absolutePower[], float32 relativePower[], int32 arraySize, int32 *actual

### RFmxGSM_ORFSFetchModulationPowerTrace

Fetches the modulation power trace and frequency offset.

#### Syntax

int32 __stdcall RFmxGSM_ORFSFetchModulationPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 offsetFrequency[], float32 absolutePower[], float32 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| offsetFrequency | [out] | float32[] | This parameter returns an array of modulation offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
| absolutePower | [out] | float32[] | This parameter returns an array of absolute powers corresponding to the modulation offset frequency list. This value is expressed in dBm. |
| relativePower | [out] | float32[] | This parameter returns an array of relative powers corresponding to modulation offset frequency list. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1gafbf79b93f5d69d3277bdefdbada52148.html language=enus -->
## TOPIC 00216: RFmxGSM_ORFSFetchModulationResultsArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1gafbf79b93f5d69d3277bdefdbada52148.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__orfs_1gafbf79b93f5d69d3277bdefdbada52148.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier. Syntaxint32 __stdcall RFmxGSM_ORFSFetchModulationResultsArray(niRFmxInstrHandle instr

### RFmxGSM_ORFSFetchModulationResultsArray

Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier.

#### Syntax

int32 __stdcall RFmxGSM_ORFSFetchModulationResultsArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *modulationCarrierPower, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| modulationCarrierPower | [out] | float64 * | This parameter returns the modulation carrier power. This value is expressed in dBm. |
| lowerRelativePower | [out] | float64[] | This parameter returns an array of relative powers measured at the negative modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
| upperRelativePower | [out] | float64[] | This parameter returns an array of relative powers measured at the positive modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
| lowerAbsolutePower | [out] | float64[] | This parameter returns an array of absolute powers measured at the negative modulation offset frequencies. This value is expressed in dBm. |
| upperAbsolutePower | [out] | float64[] | This parameter returns an array of absolute powers measured at the positive modulation offset frequencies. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__pvt.html language=enus -->
## TOPIC 00217: PVT

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__pvt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__pvt.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_PVTFetchMeasurementStatusFetches the overall PVT measurement status based on the standard defined measurement limits. RFmxGSM_PVTFetchPowerTraceFetches the upper mask, signal power, and lower mask trace. RFmxGSM_PVTFetchSlotMeasurementFetches the measure

### PVT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_PVTFetchMeasurementStatus | Fetches the overall PVT measurement status based on the standard defined measurement limits. |
| RFmxGSM_PVTFetchPowerTrace | Fetches the upper mask, signal power, and lower mask trace. |
| RFmxGSM_PVTFetchSlotMeasurement | Fetches the measurement results for a single-slot PVT measurement. |
| RFmxGSM_PVTFetchSlotMeasurementArray | Fetches the PVT measurement results for each slot. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1ga7bd17792923d3e5f09c098ab4849efa7.html language=enus -->
## TOPIC 00218: RFmxGSM_PVTFetchMeasurementStatus

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1ga7bd17792923d3e5f09c098ab4849efa7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1ga7bd17792923d3e5f09c098ab4849efa7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall PVT measurement status based on the standard defined measurement limits. Syntaxint32 __stdcall RFmxGSM_PVTFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)ParametersNameDirectionTypeDescriptioninstrumentHa

### RFmxGSM_PVTFetchMeasurementStatus

Fetches the overall PVT measurement status based on the standard defined measurement limits.

#### Syntax

int32 __stdcall RFmxGSM_PVTFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1/result::r1""signal::sig1""result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter indicates the overall measurement status based on standard-defined limits.NameValueDescriptionRFMXGSM_VAL_PVT_MEASUREMENT_STATUS_FAIL0 (0x0)The measurement failed because the average power of at least one slot is outside the standard-defined limits.RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_PASS1 (0x1)The measurement passed because the average power of all slots is within the standard-defined limits. |
| Name | Value | Description |  |
| RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |  |
| RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_PASS | 1 (0x1) | The measurement passed because the average power of all slots is within the standard-defined limits. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1ga7f4e0cf96ebc548f23d4cab404b12f25.html language=enus -->
## TOPIC 00219: RFmxGSM_PVTFetchSlotMeasurementArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1ga7f4e0cf96ebc548f23d4cab404b12f25.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1ga7f4e0cf96ebc548f23d4cab404b12f25.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PVT measurement results for each slot. Syntaxint32 __stdcall RFmxGSM_PVTFetchSlotMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotAveragePower[], float64 slotBurstWidth[], int32 slotMeasurementStatus[], float64 slotMaximumPower[], f

### RFmxGSM_PVTFetchSlotMeasurementArray

Fetches the PVT measurement results for each slot.

#### Syntax

int32 __stdcall RFmxGSM_PVTFetchSlotMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotAveragePower[], float64 slotBurstWidth[], int32 slotMeasurementStatus[], float64 slotMaximumPower[], float64 slotMinimumPower[], float64 slotBurstThreshold[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| slotAveragePower | [out] | float64[] | This parameter returns an array of mean powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstWidth | [out] | float64[] | This parameter returns an array of burst widths for the slots where the -3 dB transition points occur. This value is expressed in seconds. |
| slotMeasurementStatus | [out] | int32[] | This parameter indicates an array of PVT measurement statuses for multiple slots.NameValueDescriptionRFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL0 (0x0)The average power for at least one slot is outside the standard-defined limits.RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS1 (0x1)The average power for each slot is within the standard-defined limits. |
| Name | Value | Description |  |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The average power for at least one slot is outside the standard-defined limits. |  |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS | 1 (0x1) | The average power for each slot is within the standard-defined limits. |  |
| slotMaximumPower | [out] | float64[] | This parameter returns an array of maximum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotMinimumPower | [out] | float64[] | This parameter returns an array of minimum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstThreshold | [out] | float64[] | This parameter returns an array of thresholds that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1gabe51becf2cb934373c1f0bac94b355ba.html language=enus -->
## TOPIC 00220: RFmxGSM_PVTFetchSlotMeasurement

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1gabe51becf2cb934373c1f0bac94b355ba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1gabe51becf2cb934373c1f0bac94b355ba.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement results for a single-slot PVT measurement. Syntaxint32 __stdcall RFmxGSM_PVTFetchSlotMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *slotAveragePower, float64 *slotBurstWidth, int32 *slotMeasurementStatus, float64 *slotMaximumP

### RFmxGSM_PVTFetchSlotMeasurement

Fetches the measurement results for a single-slot PVT measurement.

#### Syntax

int32 __stdcall RFmxGSM_PVTFetchSlotMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *slotAveragePower, float64 *slotBurstWidth, int32 *slotMeasurementStatus, float64 *slotMaximumPower, float64 *slotMinimumPower, float64 *slotBurstThreshold)

#### Remarks

Use "slot<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"slot0""signal::sig1/slot0""result::r1/slot0""signal::sig1/result::r1/slot0"You can use the RFmxGSM_BuildSlotString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| slotAveragePower | [out] | float64 * | This parameter returns the mean power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstWidth | [out] | float64 * | This parameter returns the burst width of the slot where the -3 dB transition points occur. This value is expressed in seconds. |
| slotMeasurementStatus | [out] | int32 * | This parameter indicates the PVT measurement status for a particular slot.NameValueDescriptionRFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL0 (0x0)The average power for at least one slot is outside the standard-defined limits.RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS1 (0x1)The average power for each slot is within the standard-defined limits. |
| Name | Value | Description |  |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The average power for at least one slot is outside the standard-defined limits. |  |
| RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS | 1 (0x1) | The average power for each slot is within the standard-defined limits. |  |
| slotMaximumPower | [out] | float64 * | This parameter returns the maximum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotMinimumPower | [out] | float64 * | This parameter returns the minimum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
| slotBurstThreshold | [out] | float64 * | This parameter returns the threshold that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1gac915cb3be91c1e872d1b83bf9135d8b6.html language=enus -->
## TOPIC 00221: RFmxGSM_PVTFetchPowerTrace

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1gac915cb3be91c1e872d1b83bf9135d8b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__fetch__pvt_1gac915cb3be91c1e872d1b83bf9135d8b6.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the upper mask, signal power, and lower mask trace. Syntaxint32 __stdcall RFmxGSM_PVTFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 upperMask[], float32 signalPower[], float32 lowerMask[], int32 arraySize, int32 *

### RFmxGSM_PVTFetchPowerTrace

Fetches the upper mask, signal power, and lower mask trace.

#### Syntax

int32 __stdcall RFmxGSM_PVTFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 upperMask[], float32 signalPower[], float32 lowerMask[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string).Example:"signal::sig1/result::r1""signal::sig1""result::r1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| upperMask | [out] | float32[] | This parameter returns an array of upper mask values measured at each time instance. |
| signalPower | [out] | float32[] | This parameter returns an array of upper mask values measured at each time instance. |
| lowerMask | [out] | float32[] | This parameter returns an array of upper mask values measured at each time instance. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__select__measurement.html language=enus -->
## TOPIC 00222: Select Measurement

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__select__measurement.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__select__measurement_1gaac96a382d76d48161161c8447b5cd8ca.html language=enus -->
## TOPIC 00223: RFmxGSM_SelectMeasurements

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__select__measurement_1gaac96a382d76d48161161c8447b5cd8ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__select__measurement_1gaac96a382d76d48161161c8447b5cd8ca.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxGSM_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescripti

### RFmxGSM_SelectMeasurements

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxGSM_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).Example:"signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array.Name (Value)DescriptionModAcc (0)Enables the modulation accuracy (ModAcc) measurement.ORFS (1)Enables the output radio frequency spectrum (ORFS) measurement.PVT (2)Enables the power versus time (PVT) measurement. |
| Name (Value) | Description |  |  |
| ModAcc (0) | Enables the modulation accuracy (ModAcc) measurement. |  |  |
| ORFS (1) | Enables the output radio frequency spectrum (ORFS) measurement. |  |  |
| PVT (2) | Enables the power versus time (PVT) measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurement. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00224: Set and Get Attributes

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes.html
- document_id: `rfmxgsm-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00225: Get Attributes

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxGSM_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer fo

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxGSM_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxGSM_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxGSM_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxGSM_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxGSM_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxGSM_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxGSM_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxGSM_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxGSM_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxGSM_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga02410427db68f15ed90fb69011ca6239.html language=enus -->
## TOPIC 00226: RFmxGSM_GetAttributeI16

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga02410427db68f15ed90fb69011ca6239.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga02410427db68f15ed90fb69011ca6239.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx ses

### RFmxGSM_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga047ca5b246059352926aefe4c3d72328.html language=enus -->
## TOPIC 00227: RFmxGSM_GetAttributeF32

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga047ca5b246059352926aefe4c3d72328.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga047ca5b246059352926aefe4c3d72328.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdent

### RFmxGSM_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga08d3ee422985bba0425651bfa9e894b5.html language=enus -->
## TOPIC 00228: RFmxGSM_GetAttributeU8

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga08d3ee422985bba0425651bfa9e894b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga08d3ee422985bba0425651bfa9e894b5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the R

### RFmxGSM_GetAttributeU8

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga17b9e555d81443e1797b76ce7d8d2923.html language=enus -->
## TOPIC 00229: RFmxGSM_GetAttributeI64

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga17b9e555d81443e1797b76ce7d8d2923.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga17b9e555d81443e1797b76ce7d8d2923.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx ses

### RFmxGSM_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga259dbb3a36c3308da0627ccd2cf47359.html language=enus -->
## TOPIC 00230: RFmxGSM_GetAttributeU64Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga259dbb3a36c3308da0627ccd2cf47359.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga259dbb3a36c3308da0627ccd2cf47359.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxGSM_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga3254dcbbf38c2c94716c513f85b664f5.html language=enus -->
## TOPIC 00231: RFmxGSM_GetAttributeU32Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga3254dcbbf38c2c94716c513f85b664f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga3254dcbbf38c2c94716c513f85b664f5.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxGSM_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga5d92362b65bbddb4ef0235f226f192bf.html language=enus -->
## TOPIC 00232: RFmxGSM_GetAttributeI8

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga5d92362b65bbddb4ef0235f226f192bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga5d92362b65bbddb4ef0235f226f192bf.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxGSM_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga61c7406680ec2dad3edabf0e2b9bfe88.html language=enus -->
## TOPIC 00233: RFmxGSM_GetAttributeI32Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga61c7406680ec2dad3edabf0e2b9bfe88.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga61c7406680ec2dad3edabf0e2b9bfe88.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxGSM_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga77c3ada4c43bd68af87fdd8f6d98cedf.html language=enus -->
## TOPIC 00234: RFmxGSM_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga77c3ada4c43bd68af87fdd8f6d98cedf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga77c3ada4c43bd68af87fdd8f6d98cedf.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxGSM_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga7a7bdd952ace80a93c06bd6c3b42aaa4.html language=enus -->
## TOPIC 00235: RFmxGSM_GetAttributeU8Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga7a7bdd952ace80a93c06bd6c3b42aaa4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga7a7bdd952ace80a93c06bd6c3b42aaa4.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxGSM_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga829642512f41dac9c611b8096b009be7.html language=enus -->
## TOPIC 00236: RFmxGSM_GetAttributeF64Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga829642512f41dac9c611b8096b009be7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1ga829642512f41dac9c611b8096b009be7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxGSM_GetAttributeF64Array

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaaae77fc3a12a04ee82f132baaf60aecc.html language=enus -->
## TOPIC 00237: RFmxGSM_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaaae77fc3a12a04ee82f132baaf60aecc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaaae77fc3a12a04ee82f132baaf60aecc.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxGSM_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gab0ed64170fe624bee482bb97cfc38c35.html language=enus -->
## TOPIC 00238: RFmxGSM_GetAttributeU32

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gab0ed64170fe624bee482bb97cfc38c35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gab0ed64170fe624bee482bb97cfc38c35.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies t

### RFmxGSM_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gac3cecc382e755de7de4ec954bed05d40.html language=enus -->
## TOPIC 00239: RFmxGSM_GetAttributeString

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gac3cecc382e755de7de4ec954bed05d40.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gac3cecc382e755de7de4ec954bed05d40.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxGSM_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gae2b2039487b56455d2e2062b65b41d59.html language=enus -->
## TOPIC 00240: RFmxGSM_GetAttributeU16

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gae2b2039487b56455d2e2062b65b41d59.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gae2b2039487b56455d2e2062b65b41d59.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies t

### RFmxGSM_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gae3a13829271dbb7f3657e041035fb85a.html language=enus -->
## TOPIC 00241: RFmxGSM_GetAttributeI8Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gae3a13829271dbb7f3657e041035fb85a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gae3a13829271dbb7f3657e041035fb85a.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxGSM_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaeba28a489c76e95d595cb91070df2284.html language=enus -->
## TOPIC 00242: RFmxGSM_GetAttributeF32Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaeba28a489c76e95d595cb91070df2284.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaeba28a489c76e95d595cb91070df2284.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxGSM_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf6515a447ff5563558676ef1af76c1e1.html language=enus -->
## TOPIC 00243: RFmxGSM_GetAttributeI64Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf6515a447ff5563558676ef1af76c1e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf6515a447ff5563558676ef1af76c1e1.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxGSM_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf822e5c7094e4cc84130fbd97f2f2110.html language=enus -->
## TOPIC 00244: RFmxGSM_GetAttributeI32

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf822e5c7094e4cc84130fbd97f2f2110.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf822e5c7094e4cc84130fbd97f2f2110.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx ses

### RFmxGSM_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf86c42a0ee7c07856232f026836ba649.html language=enus -->
## TOPIC 00245: RFmxGSM_GetAttributeF64

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf86c42a0ee7c07856232f026836ba649.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__get__attributes_1gaf86c42a0ee7c07856232f026836ba649.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxGSM_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdent

### RFmxGSM_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxGSM_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00246: Set Attributes

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxGSM_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxGSM_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxGSM_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxGSM_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxGSM_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxGSM_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxGSM_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxGSM_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxGSM_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxGSM_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxGSM_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxGSM_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxGSM_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxGSM_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga075496759feca3b33b7ffed3386f0fb2.html language=enus -->
## TOPIC 00247: RFmxGSM_SetAttributeF32Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga075496759feca3b33b7ffed3386f0fb2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga075496759feca3b33b7ffed3386f0fb2.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char

### RFmxGSM_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga0afd25ab00f05b88f66c0cf7cc0c4787.html language=enus -->
## TOPIC 00248: RFmxGSM_SetAttributeU64Array

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga0afd25ab00f05b88f66c0cf7cc0c4787.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga0afd25ab00f05b88f66c0cf7cc0c4787.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxGSM_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selec

### RFmxGSM_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga0ea55282fa0bb42597009d90c5197df7.html language=enus -->
## TOPIC 00249: RFmxGSM_SetAttributeI16

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga0ea55282fa0bb42597009d90c5197df7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga0ea55282fa0bb42597009d90c5197df7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session

### RFmxGSM_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxgsm-c-api-ref path=group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga11f2bbbd356426a9f62e0903313ab4c7.html language=enus -->
## TOPIC 00250: RFmxGSM_SetAttributeI8

- bundle_id: `rfmxgsm-c-api-ref`
- source_path: `group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga11f2bbbd356426a9f62e0903313ab4c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_g_s_m__functions__set__and__get__attributes__set__attributes_1ga11f2bbbd356426a9f62e0903313ab4c7.html
- document_id: `rfmxgsm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxGSM_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. Yo

### RFmxGSM_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxGSM_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxGSM_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxGSM_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxGSM_GetError](group____root__ni_r_fmx_g_s_m__functions_1ga1f2b4eb48888feace9931d2abaa2a577.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes
