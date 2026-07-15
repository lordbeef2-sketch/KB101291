# NI DOCUMENT BUNDLE: rfmxspecan-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxspecan-c-api-ref start=251 end=500 -->
<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__segment.html language=enus -->
## TOPIC 00251: Segment

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__segment.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__segment.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsRBW FilterGroup membersNameDescriptionRFMXSPECAN_ATTR_POWERLIST_SEGMENT_FREQUENCYSpecifies an array of expected carrier frequencies for the RF signal to be acquired, each corresponding to a segment, to which the signal analyzer tunes. This value is expressed in Hz. RFMXSPECAN_ATTR_POWERLIST_SE

### Segment

#### Groups

- RBW Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_POWERLIST_SEGMENT_FREQUENCY | Specifies an array of expected carrier frequencies for the RF signal to be acquired, each corresponding to a segment, to which the signal analyzer tunes. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_POWERLIST_SEGMENT_LENGTH | Specifies an array of durations, each corresponding to a segment, where each value must be at least the sum of RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_LENGTH and RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_OFFSET when the RFMXSPECAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute is set to TimerEvent. This value is expressed in seconds. |
| RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_LENGTH | Specifies an array of durations, each corresponding to a segment, over which the power value is computed. This value is expressed in seconds. |
| RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_OFFSET | Specifies an array of time offsets from the start of each segment, over which the power value is computed. This value is expressed in seconds. |
| RFMXSPECAN_ATTR_POWERLIST_SEGMENT_REFERENCE_LEVEL | Specifies an array of reference levels, each representing the maximum expected power of the RF input signal for its corresponding segment. This value is configured in dBm for RF devices. |
| RFMXSPECAN_ATTR_POWERLIST_SEGMENT_TRIGGER_TYPE | Specifies an array of trigger type, each corresponding to a segment. |

#### Attachments

None

Parent topic:

PowerList

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga18b7a2be9e0bdc4cb3128b6415f84db6.html language=enus -->
## TOPIC 00252: RFMXSPECAN_ATTR_POWERLIST_SEGMENT_REFERENCE_LEVEL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga18b7a2be9e0bdc4cb3128b6415f84db6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga18b7a2be9e0bdc4cb3128b6415f84db6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of reference levels, each representing the maximum expected power of the RF input signal for its corresponding segment. This value is configured in dBm for RF devices. SyntaxRFMXSPECAN_ATTR_POWERLIST_SEGMENT_REFERENCE_LEVELNumeric ValueData TypeAccessApplies To1376261AdoubleRead/W

### RFMXSPECAN_ATTR_POWERLIST_SEGMENT_REFERENCE_LEVEL

Specifies an array of reference levels, each representing the maximum expected power of the RF input signal for its corresponding segment. This value is configured in dBm for RF devices.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_SEGMENT_REFERENCE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376261 | Adouble | Read/Write | N/A |

#### Remarks

RFmx returns an error if the size of the configured values is smaller than the [RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS](group____root__ni_r_fmx_spec_an__attributes__powerlist_1gaa05ec5a76376c68c36c90273630aa120.html). You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga3b65f8bad31c534d2a3d6e92b704b188.html language=enus -->
## TOPIC 00253: RFMXSPECAN_ATTR_POWERLIST_SEGMENT_LENGTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga3b65f8bad31c534d2a3d6e92b704b188.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga3b65f8bad31c534d2a3d6e92b704b188.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of durations, each corresponding to a segment, where each value must be at least the sum of RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_LENGTH and RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_OFFSET when the RFMXSPECAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute is set to TimerE

### RFMXSPECAN_ATTR_POWERLIST_SEGMENT_LENGTH

Specifies an array of durations, each corresponding to a segment, where each value must be at least the sum of [RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_LENGTH](group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1gaa1f7872ebfcff821839d41d7a0c1e3b5.html) and [RFMXSPECAN_ATTR_POWERLIST_SEGMENT_MEASUREMENT_OFFSET](group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1gad946047197af909308d855231583bdab.html) when the [RFMXSPECAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE](group____root__ni_r_fmx_spec_an__attributes__trigger__digital__edge_1ga634d0fa444bd49fb057cb7b2ffdf08c5.html) attribute is set to **TimerEvent**. This value is expressed in seconds.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_SEGMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376259 | Adouble | Read/Write | N/A |

#### Remarks

RFmx returns an error if the size of the configured values is smaller than the [RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS](group____root__ni_r_fmx_spec_an__attributes__powerlist_1gaa05ec5a76376c68c36c90273630aa120.html). You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga7a6fcfcf833e4f31721b835a0a52b281.html language=enus -->
## TOPIC 00254: RFMXSPECAN_ATTR_POWERLIST_SEGMENT_TRIGGER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga7a6fcfcf833e4f31721b835a0a52b281.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__segment_1ga7a6fcfcf833e4f31721b835a0a52b281.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of trigger type, each corresponding to a segment. SyntaxRFMXSPECAN_ATTR_POWERLIST_SEGMENT_TRIGGER_TYPENumeric ValueData TypeAccessApplies To1376267Aint32Read/WriteN/ARemarks RFmx returns an error if the size of the configured values is smaller than the RFMXSPECAN_ATTR_POWERLIST_NU

### RFMXSPECAN_ATTR_POWERLIST_SEGMENT_TRIGGER_TYPE

Specifies an array of trigger type, each corresponding to a segment.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_SEGMENT_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376267 | Aint32 | Read/Write | N/A |

#### Remarks

RFmx returns an error if the size of the configured values is smaller than the [RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS](group____root__ni_r_fmx_spec_an__attributes__powerlist_1gaa05ec5a76376c68c36c90273630aa120.html). You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

| Name (value) | Description |
| --- | --- |
| None (0) | No Reference Trigger is configured. |
| Digital Edge (1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXSPECAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| IQ Power Edge (2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |

The default value is **None**. RFmx applies this default value for all segments when the attribute is either unconfigured or reset to its default.

Parent topic:

Segment

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__segment__rbw__filter_1ga819c226fbc6dc270ef56483f96c3e400.html language=enus -->
## TOPIC 00255: RFMXSPECAN_ATTR_POWERLIST_SEGMENT_RBW_FILTER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__segment__rbw__filter_1ga819c226fbc6dc270ef56483f96c3e400.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__segment__rbw__filter_1ga819c226fbc6dc270ef56483f96c3e400.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of digital resolution bandwidth (RBW) filter shapes, each corresponding to a segment. SyntaxRFMXSPECAN_ATTR_POWERLIST_SEGMENT_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To1376265Aint32Read/WriteN/ARemarks RFmx returns an error if the size of the configured values is smalle

### RFMXSPECAN_ATTR_POWERLIST_SEGMENT_RBW_FILTER_TYPE

Specifies an array of digital resolution bandwidth (RBW) filter shapes, each corresponding to a segment.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_SEGMENT_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376265 | Aint32 | Read/Write | N/A |

#### Remarks

RFmx returns an error if the size of the configured values is smaller than the [RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS](group____root__ni_r_fmx_spec_an__attributes__powerlist_1gaa05ec5a76376c68c36c90273630aa120.html).

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

| Name (value) | Description |
| --- | --- |
| Gaussian (1) | The RBW filter has a Gaussian response. |
| Flat (2) | The RBW filter has a flat response. |
| None (5) | The measurement does not use any RBW filtering. |
| RRC (6) | The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_POWERLIST_SEGMENT_RBW_FILTER_ALPHA attribute is used as the RBW filter. |

The default value is **Gaussian**. RFmx applies this default value for all segments when the attribute is either unconfigured or reset to its default.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem_1ga182db258a63ed4791c8b50b171dea305.html language=enus -->
## TOPIC 00256: RFMXSPECAN_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem_1ga182db258a63ed4791c8b50b171dea305.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem_1ga182db258a63ed4791c8b50b171dea305.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRF

### RFMXSPECAN_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXSPECAN_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081423 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXSPECAN_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html language=enus -->
## TOPIC 00257: RFMXSPECAN_ATTR_SEM_POWER_UNITS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for the absolute power. SyntaxRFMXSPECAN_ATTR_SEM_POWER_UNITSNumeric ValueData TypeAccessApplies To1081372int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for

### RFMXSPECAN_ATTR_SEM_POWER_UNITS

Specifies the units for the absolute power.

#### Syntax

RFMXSPECAN_ATTR_SEM_POWER_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081372 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dBm**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM | 0 (0x0) | The absolute powers are reported in dBm. |
| RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ | 1 (0x1) | The absolute powers are reported in dBm/Hz. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__averaging.html language=enus -->
## TOPIC 00258: Averaging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__averaging.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED attribute to True. RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLEDSpecifies whether to enable averaging for the SEM measuremen

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED | Specifies whether to enable averaging for the SEM measurement. |
| RFMXSPECAN_ATTR_SEM_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1ga22691a94ab1ae43e7b9abbb67c4c3259.html language=enus -->
## TOPIC 00259: RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1ga22691a94ab1ae43e7b9abbb67c4c3259.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1ga22691a94ab1ae43e7b9abbb67c4c3259.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the SEM measurement. SyntaxRFMXSPECAN_ATTR_SEM_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To1081375int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED

Specifies whether to enable averaging for the SEM measurement.

#### Syntax

RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081375 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The SEM measurement uses the RFMXSPECAN_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1ga28f8a773c2e23b1d4196e21bf4c7e1ed.html language=enus -->
## TOPIC 00260: RFMXSPECAN_ATTR_SEM_AVERAGING_COUNT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1ga28f8a773c2e23b1d4196e21bf4c7e1ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1ga28f8a773c2e23b1d4196e21bf4c7e1ed.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_SEM_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To1081374int32Read/WriteN/ARemarks You do not need to use a selector string to configure or r

### RFMXSPECAN_ATTR_SEM_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXSPECAN_ATTR_SEM_AVERAGING_ENABLED](group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1ga22691a94ab1ae43e7b9abbb67c4c3259.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_SEM_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081374 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1gae33fc8580ff1344c18d0aaf4d2c4385c.html language=enus -->
## TOPIC 00261: RFMXSPECAN_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1gae33fc8580ff1344c18d0aaf4d2c4385c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__averaging_1gae33fc8580ff1344c18d0aaf4d2c4385c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. SyntaxRFMXSPECAN_ATTR_SEM_AVERAGING_TYPENumeric ValueData TypeAccessApplies To1081377int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read t

### RFMXSPECAN_ATTR_SEM_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.

#### Syntax

RFMXSPECAN_ATTR_SEM_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081377 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier.html language=enus -->
## TOPIC 00262: Carrier

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsRBW FilterRRC FilterGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_CARRIER_CHANNEL_BANDWIDTHSpecifies the channel bandwidth of the carrier. This parameter is used to calculate the values of the RFMXSPECAN_ATTR_SEM_OFFSET_START_FREQUENCY and RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY attributes

### Carrier

#### Groups

- RBW Filter
- RRC Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_CARRIER_CHANNEL_BANDWIDTH | Specifies the channel bandwidth of the carrier. This parameter is used to calculate the values of the RFMXSPECAN_ATTR_SEM_OFFSET_START_FREQUENCY and RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY attributes when you set the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute to Carrier Edge to Meas BW Center or Carrier Edge to Meas BW Edge. |
| RFMXSPECAN_ATTR_SEM_CARRIER_ENABLED | Specifies whether to consider the carrier power as part of the total carrier power measurement. |
| RFMXSPECAN_ATTR_SEM_CARRIER_FREQUENCY | Specifies the center frequency of the carrier, relative to the RF RFMXSPECAN_ATTR_CENTER_FREQUENCY. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH | Specifies the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_NUMBER_OF_CARRIERS | Specifies the number of carriers. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1ga432819800b2ca3232a603b84dea15a91.html language=enus -->
## TOPIC 00263: RFMXSPECAN_ATTR_SEM_NUMBER_OF_CARRIERS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1ga432819800b2ca3232a603b84dea15a91.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1ga432819800b2ca3232a603b84dea15a91.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of carriers. SyntaxRFMXSPECAN_ATTR_SEM_NUMBER_OF_CARRIERSNumeric ValueData TypeAccessApplies To1081346int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for in

### RFMXSPECAN_ATTR_SEM_NUMBER_OF_CARRIERS

Specifies the number of carriers.

#### Syntax

RFMXSPECAN_ATTR_SEM_NUMBER_OF_CARRIERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081346 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1ga7e7357c5ec262a6415e30adcf328fa9a.html language=enus -->
## TOPIC 00264: RFMXSPECAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1ga7e7357c5ec262a6415e30adcf328fa9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1ga7e7357c5ec262a6415e30adcf328fa9a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To1081349float64Read/WriteCarrierRemarks Use "carrier<n>" as the Selector String to configu

### RFMXSPECAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

Specifies the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081349 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 2 MHz.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1gaaf6425e30c690a10ef284b4653647249.html language=enus -->
## TOPIC 00265: RFMXSPECAN_ATTR_SEM_CARRIER_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1gaaf6425e30c690a10ef284b4653647249.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier_1gaaf6425e30c690a10ef284b4653647249.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to consider the carrier power as part of the total carrier power measurement. SyntaxRFMXSPECAN_ATTR_SEM_CARRIER_ENABLEDNumeric ValueData TypeAccessApplies To1081347int32Read/WriteCarrierRemarks Use "carrier<n>" as the Selector String to configure or read this attribute.The default

### RFMXSPECAN_ATTR_SEM_CARRIER_ENABLED

Specifies whether to consider the carrier power as part of the total carrier power measurement.

#### Syntax

RFMXSPECAN_ATTR_SEM_CARRIER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081347 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_ENABLED_FALSE | 0 (0x0) | The carrier power is not considered as part of the total carrier power. |
| RFMXSPECAN_VAL_SEM_ENABLED_TRUE | 1 (0x1) | The carrier power is considered as part of the total carrier power. |

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter.html language=enus -->
## TOPIC 00266: RBW Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the resolution bandwidth (RBW) of the carrier. RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the resolution bandwidth (RBW) filter used t

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the resolution bandwidth (RBW) of the carrier. |
| RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal, when you set the RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITION | Specifies the bandwidth definition that you use to specify the value of the RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_TYPE | Specifies the shape of the digital resolution bandwidth (RBW) filter. |

#### Attachments

None

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga5d197049747792dbc743f9e427bf4d92.html language=enus -->
## TOPIC 00267: RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga5d197049747792dbc743f9e427bf4d92.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga5d197049747792dbc743f9e427bf4d92.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal, when you set the RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTHNumeric ValueDat

### RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired carrier signal, when you set the [RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga73cce07b7a9169e6e24d5b2b29be91f5.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081351 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 10 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga8f519dcdfa2192bb10a7b54bfa726aa0.html language=enus -->
## TOPIC 00268: RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga8f519dcdfa2192bb10a7b54bfa726aa0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga8f519dcdfa2192bb10a7b54bfa726aa0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth definition that you use to specify the value of the RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH attribute. SyntaxRFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITIONNumeric ValueData TypeAccessApplies To1081422int32Read/WriteCarrierRemarks Use "carrier<n>" as the

### RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITION

Specifies the bandwidth definition that you use to specify the value of the [RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rbw__filter_1ga5d197049747792dbc743f9e427bf4d92.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081422 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **3dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITION_3DB | 0 (0x0) | Defines the RBW in terms of the 3 dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_TYPE attribute to FFT Based, RBW is the 3 dB bandwidth of the window specified by the RFMXSPECAN_ATTR_SEM_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH | 2 (0x2) | Defines the RBW in terms of the spectrum bin width computed using an FFT when you set the SEM Carrier RBW Filter Type attribute to FFT Based. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rrc__filter.html language=enus -->
## TOPIC 00269: RRC Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rrc__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rrc__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ALPHASpecifies the roll-off factor for the root-raised-cosine (RRC) filter to apply on the acquired carrier channel before measuring the carrier channel power. RFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ENABLEDSpecifies whether

### RRC Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ALPHA | Specifies the roll-off factor for the root-raised-cosine (RRC) filter to apply on the acquired carrier channel before measuring the carrier channel power. |
| RFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ENABLED | Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel before measuring the carrier channel power. |

#### Attachments

None

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rrc__filter_1ga0bf26e9edce1b78e44b48757cd7822da.html language=enus -->
## TOPIC 00270: RFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ALPHA

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rrc__filter_1ga0bf26e9edce1b78e44b48757cd7822da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__carrier__rrc__filter_1ga0bf26e9edce1b78e44b48757cd7822da.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the roll-off factor for the root-raised-cosine (RRC) filter to apply on the acquired carrier channel before measuring the carrier channel power. SyntaxRFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ALPHANumeric ValueData TypeAccessApplies To1081354float64Read/WriteCarrierRemarks Use "carrier<n>" a

### RFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ALPHA

Specifies the roll-off factor for the root-raised-cosine (RRC) filter to apply on the acquired carrier channel before measuring the carrier channel power.

#### Syntax

RFMXSPECAN_ATTR_SEM_CARRIER_RRC_FILTER_ALPHA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081354 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.1.

Parent topic:

RRC Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__fft_1ga87873f7e1783029fa4bc18458c47a98d.html language=enus -->
## TOPIC 00271: RFMXSPECAN_ATTR_SEM_FFT_PADDING

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__fft_1ga87873f7e1783029fa4bc18458c47a98d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__fft_1ga87873f7e1783029fa4bc18458c47a98d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: SyntaxRFMXSPECAN_ATTR_SEM_FFT_PADDINGNumeric ValueData TypeAccessApplies To1081379float64Read/WriteN/ARemarks waveform size * paddingThis attribute is used only when the

### RFMXSPECAN_ATTR_SEM_FFT_PADDING

Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula:

#### Syntax

RFMXSPECAN_ATTR_SEM_FFT_PADDING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081379 | float64 | Read/Write | N/A |

#### Remarks

waveform size * padding

This attribute is used only when the acquisition span is less than the device instantaneous bandwidth of the device.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -1.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__fft_1gaf6f9d057af2bb40cd13ca3b4fc874a24.html language=enus -->
## TOPIC 00272: RFMXSPECAN_ATTR_SEM_FFT_WINDOW

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__fft_1gaf6f9d057af2bb40cd13ca3b4fc874a24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__fft_1gaf6f9d057af2bb40cd13ca3b4fc874a24.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type to use to reduce spectral leakage. SyntaxRFMXSPECAN_ATTR_SEM_FFT_WINDOWNumeric ValueData TypeAccessApplies To1081378int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selec

### RFMXSPECAN_ATTR_SEM_FFT_WINDOW

Specifies the FFT window type to use to reduce spectral leakage.

#### Syntax

RFMXSPECAN_ATTR_SEM_FFT_WINDOW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081378 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Flat Top**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_NONE | 0 (0x0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_FLAT_TOP | 1 (0x1) | Measures single-tone amplitudes accurately. |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_HANNING | 2 (0x2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_HAMMING | 3 (0x3) | Analyzes closely-spaced sine waves. |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_GAUSSIAN | 4 (0x4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_BLACKMAN | 5 (0x5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_BLACKMAN_HARRIS | 6 (0x6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| RFMXSPECAN_VAL_SEM_FFT_WINDOW_KAISER_BESSEL | 7 (0x7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset.html language=enus -->
## TOPIC 00273: Offset

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAbsolute LimitRBW FilterRelative LimitGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_NUMBER_OF_OFFSETSSpecifies the number of offset segments. RFMXSPECAN_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRALSpecifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of t

### Offset

#### Groups

- Absolute Limit
- RBW Filter
- Relative Limit

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_NUMBER_OF_OFFSETS | Specifies the number of offset segments. |
| RFMXSPECAN_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL | Specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). |
| RFMXSPECAN_ATTR_SEM_OFFSET_ENABLED | Specifies whether to enable the offset segment for SEM measurement. |
| RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION | Specifies the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels. |
| RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK | Specifies the criteria to determine the measurement fail status. |
| RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_ATTENUATION | Specifies the attenuation relative to the external attenuation specified by the RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION attribute. This value is expressed in dB. Use the SEM Offset Rel Attn attribute to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
| RFMXSPECAN_ATTR_SEM_OFFSET_SIDEBAND | Specifies whether the offset segment is present on one side, or on both sides of the carrier. |
| RFMXSPECAN_ATTR_SEM_OFFSET_START_FREQUENCY | Specifies the start frequency of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY | Specifies the stop frequency of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset_1ga58e652dcd62f4688477afeec4ceb622b.html language=enus -->
## TOPIC 00274: RFMXSPECAN_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset_1ga58e652dcd62f4688477afeec4ceb622b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset_1ga58e652dcd62f4688477afeec4ceb622b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). SyntaxRFMXSPECAN_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRALNumeric ValueData TypeAccessApplies To1081356int32Read/WriteOffsetRemarks If you set this attribute to a value gr

### RFMXSPECAN_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

Specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW).

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081356 | int32 | Read/Write | Offset |

#### Remarks

If you set this attribute to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW.

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gae852220081d78f9023c63758d9b1a051.html language=enus -->
## TOPIC 00275: RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gae852220081d78f9023c63758d9b1a051.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gae852220081d78f9023c63758d9b1a051.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop frequency of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_OFFSE

### RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY

Specifies the stop frequency of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the [RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__sem__offset_1ga714349f5363b70362f591efa4324f315.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081365 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 2 MHz.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gaefaf8f2c49478322e206666093e428f3.html language=enus -->
## TOPIC 00276: RFMXSPECAN_ATTR_SEM_OFFSET_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gaefaf8f2c49478322e206666093e428f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gaefaf8f2c49478322e206666093e428f3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the offset segment for SEM measurement. SyntaxRFMXSPECAN_ATTR_SEM_OFFSET_ENABLEDNumeric ValueData TypeAccessApplies To1081362int32Read/WriteOffsetRemarks Use "offset<n>" as the Selector String to configure or read this attribute.The default value is True.NameValueDescript

### RFMXSPECAN_ATTR_SEM_OFFSET_ENABLED

Specifies whether to enable the offset segment for SEM measurement.

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081362 | int32 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_FALSE | 0 (0x0) | Disables the offset segment for the SEM measurement. |
| RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_TRUE | 1 (0x1) | Enables the offset segment for the SEM measurement. |

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset__absolute__limit_1ga2f4136f01a84bf7d802ebaea28924771.html language=enus -->
## TOPIC 00277: RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset__absolute__limit_1ga2f4136f01a84bf7d802ebaea28924771.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset__absolute__limit_1ga2f4136f01a84bf7d802ebaea28924771.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the absolute limit mask is a flat line or a line with a slope. SyntaxRFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_MODENumeric ValueData TypeAccessApplies To1081359int32Read/WriteOffsetRemarks Use "offset<n>" as the Selector String to configure or read this attribute.The default value

### RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_MODE

Specifies whether the absolute limit mask is a flat line or a line with a slope.

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081359 | int32 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **Couple**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_OFFSET_ABSOLUTE_LIMIT_MODE_MANUAL | 0 (0x0) | The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP attribute values as the two ends is considered as the mask. |
| RFMXSPECAN_VAL_SEM_OFFSET_ABSOLUTE_LIMIT_MODE_COUPLE | 1 (0x1) | The two ends of the line are coupled to the value of the SEM Offset Abs Limit Start attribute. |

Parent topic:

Absolute Limit

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset__absolute__limit_1ga487d8e41ec51cc61923ea8129c94ff2d.html language=enus -->
## TOPIC 00278: RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset__absolute__limit_1ga487d8e41ec51cc61923ea8129c94ff2d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset__absolute__limit_1ga487d8e41ec51cc61923ea8129c94ff2d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the absolute power limit corresponding to the beginning of the offset segment. This value is expressed in dBm. This power limit is also set as the stop limit for the offset segment when you set the RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_MODE attribute to Couple. SyntaxRFMXSPECAN_ATTR_SE

### RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START

Specifies the absolute power limit corresponding to the beginning of the offset segment. This value is expressed in dBm. This power limit is also set as the stop limit for the offset segment when you set the [RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_MODE](group____root__ni_r_fmx_spec_an__attributes__sem__offset__absolute__limit_1ga2f4136f01a84bf7d802ebaea28924771.html) attribute to **Couple**.

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081360 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is -10.

Parent topic:

Absolute Limit

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter.html language=enus -->
## TOPIC 00279: RBW Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the resolution bandwidth (RBW). RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acqui

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment, when you set the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITION | Specifies the bandwidth definition which you use to specify the value of the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_TYPE | Specifies the shape of the digital resolution bandwidth (RBW) filter. |

#### Attachments

None

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1ga61a1204b1e0b51396582e449eb8a9490.html language=enus -->
## TOPIC 00280: RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1ga61a1204b1e0b51396582e449eb8a9490.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1ga61a1204b1e0b51396582e449eb8a9490.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth definition which you use to specify the value of the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH attribute. SyntaxRFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITIONNumeric ValueData TypeAccessApplies To1081421int32Read/WriteOffsetRemarks Use "offset<n>" as the Sel

### RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITION

Specifies the bandwidth definition which you use to specify the value of the [RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1gacda56ed92b38a504c107dd50176e6a20.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081421 | int32 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **3dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITION_3DB | 0 (0x0) | Defines the RBW in terms of the 3dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_TYPE attribute to FFT Based, RBW is the 3dB bandwidth of the window specified by the RFMXSPECAN_ATTR_SEM_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH | 2 (0x2) | Defines the RBW in terms of the spectrum bin width computed using FFT when you set the SEM Offset RBW Filter Type attribute to FFT Based. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1gacda56ed92b38a504c107dd50176e6a20.html language=enus -->
## TOPIC 00281: RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1gacda56ed92b38a504c107dd50176e6a20.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1gacda56ed92b38a504c107dd50176e6a20.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment, when you set the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTHNumeric ValueData

### RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment, when you set the [RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__sem__offset__rbw__filter_1ga56ed8d28b3bd5ebc6e2e0e8a4087992d.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081367 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 10 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__offset__relative__limit_1ga6cd54aa1e3f1441c7c3ac59925bcfa83.html language=enus -->
## TOPIC 00282: RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__offset__relative__limit_1ga6cd54aa1e3f1441c7c3ac59925bcfa83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__offset__relative__limit_1ga6cd54aa1e3f1441c7c3ac59925bcfa83.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the relative limit mask is a flat line or a line with a slope. SyntaxRFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_MODENumeric ValueData TypeAccessApplies To1081369int32Read/WriteOffsetRemarks Use "offset<n>" as the Selector String to configure or read this attribute.The default value

### RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_MODE

Specifies whether the relative limit mask is a flat line or a line with a slope.

#### Syntax

RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081369 | int32 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **Manual**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_MANUAL | 0 (0x0) | The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask. |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_COUPLE | 1 (0x1) | The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start attribute. |

Parent topic:

Relative Limit

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results.html language=enus -->
## TOPIC 00283: Results

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCarrierLower OffsetUpper OffsetGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUSIndicates the overall measurement status based on the measurement limits and the fail criteria that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute for each of

### Results

#### Groups

- Carrier
- Lower Offset
- Upper Offset

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS | Indicates the overall measurement status based on the measurement limits and the fail criteria that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute for each offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_FREQUENCY_RESOLUTION | Returns the frequency bin spacing of the spectrum acquired by the measurement. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER | Returns the total integrated power, in dBm, of all the enabled carriers measured when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm. Returns the power spectral density, in dBm/Hz, when you set the SEM Power Units attribute to dBm/Hz. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results_1ga2e47837f713d5f7b3f06a5b3a1487206.html language=enus -->
## TOPIC 00284: RFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results_1ga2e47837f713d5f7b3f06a5b3a1487206.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results_1ga2e47837f713d5f7b3f06a5b3a1487206.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on the measurement limits and the fail criteria that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute for each offset segment. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To1081385

### RFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS

Indicates the overall measurement status based on the measurement limits and the fail criteria that you set in the [RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK](group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gaac40f0f29976bc7320ee9ec60e5fda36.html) attribute for each offset segment.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081385 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |
| RFMXSPECAN_VAL_SEM_COMPOSITE_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results_1ga8774eef0677fc10784c03815911b53b8.html language=enus -->
## TOPIC 00285: RFMXSPECAN_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results_1ga8774eef0677fc10784c03815911b53b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results_1ga8774eef0677fc10784c03815911b53b8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total integrated power, in dBm, of all the enabled carriers measured when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm. Returns the power spectral density, in dBm/Hz, when you set the SEM Power Units attribute to dBm/Hz. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_TOTAL_CARRIER_POW

### RFMXSPECAN_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

Returns the total integrated power, in dBm, of all the enabled carriers measured when you set the [RFMXSPECAN_ATTR_SEM_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html) attribute to **dBm**. Returns the power spectral density, in dBm/Hz, when you set the SEM Power Units attribute to **dBm/Hz**.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081384 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier.html language=enus -->
## TOPIC 00286: Carrier

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_POWERReturns the carrier power. RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_FREQUENCYReturns the center frequency of the carrier relative to the RFMXSPECAN_ATTR_CENTER_FREQUENCY attribute. This value is expressed in Hz. RFMXS

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_POWER | Returns the carrier power. |
| RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_FREQUENCY | Returns the center frequency of the carrier relative to the RFMXSPECAN_ATTR_CENTER_FREQUENCY attribute. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTH | Returns the frequency range, over which the measurement integrates the carrier power. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_PEAK_ABSOLUTE_POWER | Returns the peak power in the carrier channel. |
| RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY | Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_TOTAL_RELATIVE_POWER | Returns the carrier power relative to the total carrier power of all enabled carriers. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga03fe98e5f6a55d133944796307292d4a.html language=enus -->
## TOPIC 00287: RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_PEAK_ABSOLUTE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga03fe98e5f6a55d133944796307292d4a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga03fe98e5f6a55d133944796307292d4a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power in the carrier channel. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_PEAK_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To1081391float64Read-OnlyCarrierRemarks The power is reported in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when y

### RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_PEAK_ABSOLUTE_POWER

Returns the peak power in the carrier channel.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_PEAK_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081391 | float64 | Read-Only | Carrier |

#### Remarks

The power is reported in dBm when you set the [RFMXSPECAN_ATTR_SEM_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html) attribute to **dBm**, and in dBm/Hz when you set the SEM Power Units attribute to **dBm/Hz**.

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga0b32f0514eb58179f80de1c25f98575b.html language=enus -->
## TOPIC 00288: RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga0b32f0514eb58179f80de1c25f98575b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga0b32f0514eb58179f80de1c25f98575b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To1081389float64Read-OnlyCarrierRemarks The carrier power is reported in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to dBm, and in dBm/Hz when you set the SEM Po

### RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_POWER

Returns the carrier power.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081389 | float64 | Read-Only | Carrier |

#### Remarks

The carrier power is reported in dBm when you set the [RFMXSPECAN_ATTR_SEM_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html) attribute to **dBm**, and in dBm/Hz when you set the SEM Power Units attribute to **dBm/Hz**.

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga17864f3d6e75616ba02c6110f9a26288.html language=enus -->
## TOPIC 00289: RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga17864f3d6e75616ba02c6110f9a26288.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga17864f3d6e75616ba02c6110f9a26288.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the center frequency of the carrier relative to the RFMXSPECAN_ATTR_CENTER_FREQUENCY attribute. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_FREQUENCYNumeric ValueData TypeAccessApplies To1081387float64Read-OnlyCarrierRemarks Use "carrier<n>" as the Selector Strin

### RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_FREQUENCY

Returns the center frequency of the carrier relative to the [RFMXSPECAN_ATTR_CENTER_FREQUENCY](group____root__ni_r_fmx_spec_an__attributes_1ga4cb262c24fad615157cf8eaf5bbb51df.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081387 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga6636eec5704bdb48aa461678d2a00124.html language=enus -->
## TOPIC 00290: RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga6636eec5704bdb48aa461678d2a00124.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1ga6636eec5704bdb48aa461678d2a00124.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range, over which the measurement integrates the carrier power. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To1081388float64Read-OnlyCarrierRemarks Use "carrier<n>" as the Selector String to r

### RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

Returns the frequency range, over which the measurement integrates the carrier power. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081388 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1gaff86f59978891561c0e610e4d795cb6a.html language=enus -->
## TOPIC 00291: RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_TOTAL_RELATIVE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1gaff86f59978891561c0e610e4d795cb6a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__carrier_1gaff86f59978891561c0e610e4d795cb6a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power relative to the total carrier power of all enabled carriers. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_TOTAL_RELATIVE_POWERNumeric ValueData TypeAccessApplies To1081390float64Read-OnlyCarrierRemarks Use "carrier<n>" as the Selector String to r

### RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_TOTAL_RELATIVE_POWER

Returns the carrier power relative to the total carrier power of all enabled carriers. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_CARRIER_TOTAL_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081390 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset.html language=enus -->
## TOPIC 00292: Lower Offset

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGINReturns the margin from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN | Returns the margin from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power, at which the margin occurred in the lower (negative) offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. This value is expressed in dB. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS | Indicates the lower offset segment measurement status based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_ABSOLUTE_POWER | Returns the peak power measured in the lower (negative) offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_RELATIVE_POWER | Returns the peak power measured in the lower (negative) offset segment relative to the integrated or peak power of the reference carrier. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER | Returns the index of the carrier that was used as the power reference to define the lower (negative) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_START_FREQUENCY | Returns the start frequency of the lower (negative) offset segment. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_STOP_FREQUENCY | Returns the stop frequency of the lower (negative) offset segment. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWER | Returns the power measured in the lower (negative) offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_RELATIVE_POWER | Returns the power measured in the lower (negative) offset segment relative to either the integrated or peak power of the reference carrier. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset_1ga870f305ee5db6e465d347e9a6ae90aec.html language=enus -->
## TOPIC 00293: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset_1ga870f305ee5db6e465d347e9a6ae90aec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset_1ga870f305ee5db6e465d347e9a6ae90aec.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the lower (negative) offset segment. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To1081396float64Read-OnlyOffsetRemarks The power is reported in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute to

### RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWER

Returns the power measured in the lower (negative) offset segment.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081396 | float64 | Read-Only | Offset |

#### Remarks

The power is reported in dBm when you set the [RFMXSPECAN_ATTR_SEM_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html) attribute to **dBm**, and in dBm/Hz when you set the SEM Power Units attribute to **dBm/Hz**.

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset_1gad07bc1ab8396312ffe2991650a5c26c3.html language=enus -->
## TOPIC 00294: RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset_1gad07bc1ab8396312ffe2991650a5c26c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__lower__offset_1gad07bc1ab8396312ffe2991650a5c26c3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGINNumeric Valu

### RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

Returns the margin from the limit mask value that you set in the [RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK](group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gaac40f0f29976bc7320ee9ec60e5fda36.html) attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081401 | float64 | Read-Only | Offset |

#### Remarks

When you set the SEM Offset Limit Fail Mask attribute to **Absolute**, the margin is with reference to the absolute limit mask.

When you set the SEM Offset Limit Fail Mask attribute to **Relative**, the margin is with reference to the relative limit mask.

When you set the SEM Offset Limit Fail Mask attribute to **Abs AND Rel**, the margin is the maximum of the margins referenced to the absolute and relative limit masks.

When you set the SEM Offset Limit Fail Mask attribute to **Abs OR Rel**, the margin is the minimum of the margins referenced to the absolute and relative limit masks.

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset.html language=enus -->
## TOPIC 00295: Upper Offset

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGINReturns the margin from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN | Returns the margin from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power, at which the margin occurred in the upper (positive) offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY | Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power at which the margin occurred in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. This value is expressed in dB. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS | Indicates the upper offset measurement status based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_ABSOLUTE_POWER | Returns the peak power measured in the upper (positive) offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_RELATIVE_POWER | Returns the peak power measured in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER | Returns the index of the carrier that was used as the power reference to define the upper (positive) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_START_FREQUENCY | Returns the start frequency of the upper (positive) offset segment. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCY | Returns the stop frequency of the upper (positive) offset segment. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_ABSOLUTE_POWER | Returns the offset segment power measured in the upper (positive) offset segment. |
| RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWER | Returns the power measured in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga06f2dcb1a65cdcae007e7ee007b98991.html language=enus -->
## TOPIC 00296: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_START_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga06f2dcb1a65cdcae007e7ee007b98991.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga06f2dcb1a65cdcae007e7ee007b98991.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the upper (positive) offset segment. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_START_FREQUENCYNumeric ValueData TypeAccessApplies To1081406float64Read-OnlyOffsetRemarks Use "offset<n>" as the Selector String to read this result.

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_START_FREQUENCY

Returns the start frequency of the upper (positive) offset segment. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081406 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga234d1e31a7b329a96e40c72cd710c975.html language=enus -->
## TOPIC 00297: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_ABSOLUTE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga234d1e31a7b329a96e40c72cd710c975.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga234d1e31a7b329a96e40c72cd710c975.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the offset segment power measured in the upper (positive) offset segment. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To1081409float64Read-OnlyOffsetRemarks The power is reported in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNIT

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_ABSOLUTE_POWER

Returns the offset segment power measured in the upper (positive) offset segment.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081409 | float64 | Read-Only | Offset |

#### Remarks

The power is reported in dBm when you set the [RFMXSPECAN_ATTR_SEM_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html) attribute to **dBm**, and in dBm/Hz when you set the SEM Power Units attribute to **dBm/Hz**.

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga365c56d5102d86cf8bf27c14392105d5.html language=enus -->
## TOPIC 00298: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga365c56d5102d86cf8bf27c14392105d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga365c56d5102d86cf8bf27c14392105d5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCYNumeric ValueData TypeAccessApplies To1081417float64Read-OnlyOffsetRemarks Use "offset<n>" as the Selector String to read t

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081417 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga36db84dd594ae61a49587a85f55edb4d.html language=enus -->
## TOPIC 00299: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_ABSOLUTE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga36db84dd594ae61a49587a85f55edb4d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga36db84dd594ae61a49587a85f55edb4d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper (positive) offset segment. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To1081411float64Read-OnlyOffsetRemarks The power is reported in dBm when you set the RFMXSPECAN_ATTR_SEM_POWER_UNITS attribute

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_ABSOLUTE_POWER

Returns the peak power measured in the upper (positive) offset segment.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081411 | float64 | Read-Only | Offset |

#### Remarks

The power is reported in dBm when you set the [RFMXSPECAN_ATTR_SEM_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__sem_1gac93d2c2d019fcace3b780d8bacb759ea.html) attribute to **dBm**, and in dBm/Hz when you set the SEM Power Units attribute to **dBm/Hz**.

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga87e448eeb739dc57e00b0701ea3c3185.html language=enus -->
## TOPIC 00300: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga87e448eeb739dc57e00b0701ea3c3185.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga87e448eeb739dc57e00b0701ea3c3185.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWERNumeric ValueData TypeAccessApplies To1081410float64Read-OnlyOffsetRemarks When you set the RFMXSPEC

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWER

Returns the power measured in the upper (positive) offset segment relative to the integrated or peak power of the reference carrier.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081410 | float64 | Read-Only | Offset |

#### Remarks

When you set the [RFMXSPECAN_ATTR_SEM_REFERENCE_TYPE](group____root__ni_r_fmx_spec_an__attributes__sem_1ga5b82483c3d0126584774b78065006419.html) attribute to **Integration**, the reference carrier power is the total power in the reference carrier. When you set the SEM Ref Type attribute to **Peak**, the reference carrier power is the peak power in the reference.

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga9f9b6fca154dc14ea4a16cd98fc6ca45.html language=enus -->
## TOPIC 00301: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga9f9b6fca154dc14ea4a16cd98fc6ca45.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1ga9f9b6fca154dc14ea4a16cd98fc6ca45.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To1081413float64Read-OnlyOffsetRemarks Use "offset<n>" as the Selector String to read th

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081413 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gab743961f088ce89b032472bc7a40e8b4.html language=enus -->
## TOPIC 00302: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gab743961f088ce89b032472bc7a40e8b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gab743961f088ce89b032472bc7a40e8b4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the upper (positive) offset segment. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To1081407float64Read-OnlyOffsetRemarks Use "offset<n>" as the Selector String to read this result.

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCY

Returns the stop frequency of the upper (positive) offset segment. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081407 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gad7c9f3978a7cde0aa0b544b086418661.html language=enus -->
## TOPIC 00303: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gad7c9f3978a7cde0aa0b544b086418661.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gad7c9f3978a7cde0aa0b544b086418661.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the upper offset measurement status based on measurement limits and the fail criteria that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To1081418int32Read-OnlyOf

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

Indicates the upper offset measurement status based on measurement limits and the fail criteria that you specify in the [RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK](group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gaac40f0f29976bc7320ee9ec60e5fda36.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081418 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |
| RFMXSPECAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gaedb017e765426a2cb4108f155a295b5e.html language=enus -->
## TOPIC 00304: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gaedb017e765426a2cb4108f155a295b5e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gaedb017e765426a2cb4108f155a295b5e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin from the limit mask value that you set in the RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGINNumeric Valu

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

Returns the margin from the limit mask value that you set in the [RFMXSPECAN_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK](group____root__ni_r_fmx_spec_an__attributes__sem__offset_1gaac40f0f29976bc7320ee9ec60e5fda36.html) attribute. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081414 | float64 | Read-Only | Offset |

#### Remarks

When you set the SEM Offset Limit Fail Mask attribute to **Absolute**, the margin is with reference to the absolute limit mask.

When you set the SEM Offset Limit Fail Mask attribute to **Relative**, the margin is with reference to the relative limit mask.

When you set the SEM Offset Limit Fail Mask attribute to **Abs AND Rel**, the margin is the maximum of the margin referenced to the absolute and relative limit masks.

When you set the SEM Offset Limit Fail Mask attribute to **Abs OR Rel**, the margin is the minimum of the margin referenced to the absolute and relative limit masks.

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gaf18bc46f4434a05340c6df2b2bd1e5e6.html language=enus -->
## TOPIC 00305: RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gaf18bc46f4434a05340c6df2b2bd1e5e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__results__upper__offset_1gaf18bc46f4434a05340c6df2b2bd1e5e6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the index of the carrier that was used as the power reference to define the upper (positive) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment. SyntaxRFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIERNumeric Val

### RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER

Returns the index of the carrier that was used as the power reference to define the upper (positive) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment.

#### Syntax

RFMXSPECAN_ATTR_SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081408 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time.html language=enus -->
## TOPIC 00306: Sweep Time

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTOSpecifies whether the measurement computes the sweep time. RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVALSpecifies the sweep time when you set the RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seco

### Sweep Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO | Specifies whether the measurement computes the sweep time. |
| RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVAL | Specifies the sweep time when you set the RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time_1ga7e93a7e16193242cc1de44a2452084cd.html language=enus -->
## TOPIC 00307: RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time_1ga7e93a7e16193242cc1de44a2452084cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time_1ga7e93a7e16193242cc1de44a2452084cd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To1081382float64Read/WriteN/ARemarks You do not need to use a selector string to conf

### RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO](group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time_1gaf2a6eaca40e2a750bfa223a2d0fd2c00.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081382 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.001.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time_1gaf2a6eaca40e2a750bfa223a2d0fd2c00.html language=enus -->
## TOPIC 00308: RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time_1gaf2a6eaca40e2a750bfa223a2d0fd2c00.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__sem__sweep__time_1gaf2a6eaca40e2a750bfa223a2d0fd2c00.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To1081381int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXSPECAN_ATTR_SEM_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1081381 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SEM_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_SEM_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH and RFMXSPECAN_ATTR_SEM_CARRIER_RBW_FILTER_BANDWIDTH attributes. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga5410fa95955e780a037b15151e43881d.html language=enus -->
## TOPIC 00309: RFMXSPECAN_ATTR_SPECTRUM_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga5410fa95955e780a037b15151e43881d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga5410fa95955e780a037b15151e43881d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRF

### RFMXSPECAN_ATTR_SPECTRUM_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085463 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXSPECAN_VAL_SPECTRUM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga694e24daa3f58221c90df3b62cde35eb.html language=enus -->
## TOPIC 00310: RFMXSPECAN_ATTR_SPECTRUM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga694e24daa3f58221c90df3b62cde35eb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga694e24daa3f58221c90df3b62cde35eb.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for spectrum measurement. SyntaxRFMXSPECAN_ATTR_SPECTRUM_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To1085442int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of

### RFMXSPECAN_ATTR_SPECTRUM_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for spectrum measurement.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085442 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga6cb1fbb5eec8d3d8367aa6e68a56543f.html language=enus -->
## TOPIC 00311: RFMXSPECAN_ATTR_SPECTRUM_ANALYSIS_INPUT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga6cb1fbb5eec8d3d8367aa6e68a56543f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga6cb1fbb5eec8d3d8367aa6e68a56543f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to analyze just the real I or Q component of the acquired IQ data, or analyze the complex IQ data. SyntaxRFMXSPECAN_ATTR_SPECTRUM_ANALYSIS_INPUTNumeric ValueData TypeAccessApplies To1085475int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this

### RFMXSPECAN_ATTR_SPECTRUM_ANALYSIS_INPUT

Specifies whether to analyze just the real I or Q component of the acquired IQ data, or analyze the complex IQ data.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_ANALYSIS_INPUT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085475 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **IQ**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_ANALYSIS_INPUT_IQ | 0 (0x0) | Measurement analyzes the acquired I+jQ data, resulting generally in a spectrum that is not symmetric around 0 Hz. Spectrum trace result contains both positive and negative frequencies. Since the RMS power of the complex envelope is 3.01 dB higher than that of its equivalent real RF signal, the spectrum trace result of the acquired I+jQ data is scaled by -3.01 dB. |
| RFMXSPECAN_VAL_SPECTRUM_ANALYSIS_INPUT_I_ONLY | 1 (0x1) | Measurement ignores the Q data from the acquired I+jQ data and analyzes I+j0, resulting in a spectrum that is symmetric around 0 Hz. Spectrum trace result contains positive frequencies only. Spectrum of I+j0 data is scaled by +3.01 dB to account for the power of the negative frequencies that are not returned in the spectrum trace. |
| RFMXSPECAN_VAL_SPECTRUM_ANALYSIS_INPUT_Q_ONLY | 2 (0x2) | Measurement ignores the I data from the acquired I+jQ data and analyzes Q+j0, resulting in a spectrum that is symmetric around 0 Hz. Spectrum trace result contains positive frequencies only. Spectrum of Q+j0 data is scaled by +3.01 dB to account for the power of the negative frequencies that are not returned in the spectrum trace. |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga95f6f9da73fbd1ebfb0027c9e039a73f.html language=enus -->
## TOPIC 00312: RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga95f6f9da73fbd1ebfb0027c9e039a73f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga95f6f9da73fbd1ebfb0027c9e039a73f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the spectrum measurement. SyntaxRFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1085440int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Se

### RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_ENABLED

Specifies whether to enable the spectrum measurement.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085440 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__advanced.html language=enus -->
## TOPIC 00313: Advanced

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__advanced.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZESpecifies the FFT size when you set the. AttachmentsNone

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZE | Specifies the FFT size when you set the. |

#### Attachments

None

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__detector.html language=enus -->
## TOPIC 00314: Detector

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__detector.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__detector.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SPECTRUM_DETECTOR_POINTSSpecifies the number of trace points after the detector is applied. RFMXSPECAN_ATTR_SPECTRUM_DETECTOR_TYPESpecifies the type of detector to be used. AttachmentsNone

### Detector

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPECTRUM_DETECTOR_POINTS | Specifies the number of trace points after the detector is applied. |
| RFMXSPECAN_ATTR_SPECTRUM_DETECTOR_TYPE | Specifies the type of detector to be used. |

#### Attachments

None

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__fft.html language=enus -->
## TOPIC 00315: FFT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__fft.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAPSpecifies the samples to overlap between the consecutive chunks as a percentage of the RFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZE attribute when you set the RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_METHOD attribute to Sequential

### FFT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP | Specifies the samples to overlap between the consecutive chunks as a percentage of the RFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZE attribute when you set the RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_METHOD attribute to Sequential FFT and the RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE attribute to User Defined. This value is expressed as a percentage. |
| RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE | Specifies the overlap mode when you set the RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_METHOD attribute to Sequential FFT. |
| RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_TYPE | Specifies the overlap type when you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. |
| RFMXSPECAN_ATTR_SPECTRUM_FFT_PADDING | Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: |
| RFMXSPECAN_ATTR_SPECTRUM_FFT_WINDOW | Specifies the FFT window type to use to reduce spectral leakage. |

#### Attachments

None

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1ga32af440a4949d6013d2fbb71c88f5d80.html language=enus -->
## TOPIC 00316: RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1ga32af440a4949d6013d2fbb71c88f5d80.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1ga32af440a4949d6013d2fbb71c88f5d80.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the samples to overlap between the consecutive chunks as a percentage of the RFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZE attribute when you set the RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_METHOD attribute to Sequential FFT and the RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE attribute to User D

### RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP

Specifies the samples to overlap between the consecutive chunks as a percentage of the [RFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZE](group____root__ni_r_fmx_spec_an__attributes__spectrum__advanced_1gaa01f33f7f637f766784f71b0d0997452.html) attribute when you set the [RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga171d3c77988d0145ad9afab2ea7c896b.html) attribute to **Sequential FFT** and the [RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE](group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1ga43bf03073584c77031dcf1c52367ed8a.html) attribute to **User Defined**. This value is expressed as a percentage.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085477 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1ga43bf03073584c77031dcf1c52367ed8a.html language=enus -->
## TOPIC 00317: RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1ga43bf03073584c77031dcf1c52367ed8a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1ga43bf03073584c77031dcf1c52367ed8a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the overlap mode when you set the RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_METHOD attribute to Sequential FFT. SyntaxRFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODENumeric ValueData TypeAccessApplies To1085476int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read thi

### RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE

Specifies the overlap mode when you set the [RFMXSPECAN_ATTR_SPECTRUM_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga171d3c77988d0145ad9afab2ea7c896b.html) attribute to **Sequential FFT**.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085476 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_FFT_OVERLAP_MODE_DISABLED | 0 (0x0) | Disables the overlap between the chunks. |
| RFMXSPECAN_VAL_SPECTRUM_FFT_OVERLAP_MODE_AUTOMATIC | 1 (0x1) | Measurement sets the overlap based on the value you have set for the RFMXSPECAN_ATTR_SPECTRUM_FFT_WINDOW attribute. When you set the Spectrum FFT Window attribute to any value other than None, the number of overlapped samples between consecutive chunks is set to 50% of the value of the RFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZE attribute. When you set the Spectrum FFT Window attribute to None, the chunks are not overlapped and the overlap is set to 0%. |
| RFMXSPECAN_VAL_SPECTRUM_FFT_OVERLAP_MODE_USER_DEFINED | 2 (0x2) | Measurement uses the overlap that you specify in the RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP attribute. |

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1gab18269f2cadafb3a6c692fd694359801.html language=enus -->
## TOPIC 00318: RFMXSPECAN_ATTR_SPECTRUM_FFT_PADDING

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1gab18269f2cadafb3a6c692fd694359801.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__fft_1gab18269f2cadafb3a6c692fd694359801.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula: SyntaxRFMXSPECAN_ATTR_SPECTRUM_FFT_PADDINGNumeric ValueData TypeAccessApplies To1085450float64Read/WriteN/ARemarks waveform size * paddingThis attribute is used only when

### RFMXSPECAN_ATTR_SPECTRUM_FFT_PADDING

Specifies the factor by which the time-domain waveform is zero-padded before FFT. The FFT size is given by the following formula:

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_FFT_PADDING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085450 | float64 | Read/Write | N/A |

#### Remarks

waveform size * padding

This attribute is used only when the acquisition span is less than the device instantaneous bandwidth of the device.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -1.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__calibration__averaging_1ga517df235cc73e9c0a9c1bcbf7e829f4e.html language=enus -->
## TOPIC 00319: RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__calibration__averaging_1ga517df235cc73e9c0a9c1bcbf7e829f4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__calibration__averaging_1ga517df235cc73e9c0a9c1bcbf7e829f4e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxRFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTONumeric ValueData TypeAccessApplies To1085473int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read

### RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085473 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE | 0 (0x0) | RFmx uses the averages that you set for the RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_COUNT attribute. |
| RFMXSPECAN_VAL_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE | 1 (0x1) | RFmx uses a noise calibration averaging count of 32. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__calibration__averaging_1ga88a40e29043e7b8c93aa8e9d426e472c.html language=enus -->
## TOPIC 00320: RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_COUNT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__calibration__averaging_1ga88a40e29043e7b8c93aa8e9d426e472c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__calibration__averaging_1ga88a40e29043e7b8c93aa8e9d426e472c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging count used for noise calibration when you set the RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO. SyntaxRFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To1085472int32Read/WriteN/ARemarks attribute to False.You do not ne

### RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_COUNT

Specifies the averaging count used for noise calibration when you set the [RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO](group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__calibration__averaging_1ga517df235cc73e9c0a9c1bcbf7e829f4e.html).

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_NOISE_CALIBRATION_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085472 | int32 | Read/Write | N/A |

#### Remarks

attribute to **False**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 32.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__compensation_1ga3afa2c27d1a1f9a7e391e8c76d97a0d5.html language=enus -->
## TOPIC 00321: RFMXSPECAN_ATTR_SPECTRUM_NOISE_COMPENSATION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__compensation_1ga3afa2c27d1a1f9a7e391e8c76d97a0d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__noise__compensation_1ga3afa2c27d1a1f9a7e391e8c76d97a0d5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. SyntaxRFMXSPECAN_ATTR_SPECTRUM_NOISE_COMPENSATION_TYPENumeric ValueData TypeAccessApplies To1085471int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this

### RFMXSPECAN_ATTR_SPECTRUM_NOISE_COMPENSATION_TYPE

Specifies the noise compensation type. Refer to the [Noise Compensation Algorithm](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/noise-compensation-algorithm.html) topic for more information.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_NOISE_COMPENSATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085471 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Analyzer and Termination**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION | 0 (0x0) | Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. |
| RFMXSPECAN_VAL_SPECTRUM_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY | 1 (0x1) | Compensates for the analyzer noise only. |

Parent topic:

Noise Compensation

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter.html language=enus -->
## TOPIC 00322: RBW Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the resolution bandwidth (RBW). RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION | Specifies the bandwidth definition which you use to specify the value of the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_TYPE | Specifies the shape of the digital resolution bandwidth (RBW) filter. |

#### Attachments

None

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga5401380381540999fbd9c028e3e7bfd0.html language=enus -->
## TOPIC 00323: RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga5401380381540999fbd9c028e3e7bfd0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga5401380381540999fbd9c028e3e7bfd0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessAp

### RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the [RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga6d9b9a01419e69adc1e5949bc88fdf88.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085452 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga6d9b9a01419e69adc1e5949bc88fdf88.html language=enus -->
## TOPIC 00324: RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga6d9b9a01419e69adc1e5949bc88fdf88.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga6d9b9a01419e69adc1e5949bc88fdf88.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the resolution bandwidth (RBW). SyntaxRFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To1085451int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signa

### RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the resolution bandwidth (RBW).

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085451 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga9abd76dbc4a3b3a299c4597e50980478.html language=enus -->
## TOPIC 00325: RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga9abd76dbc4a3b3a299c4597e50980478.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga9abd76dbc4a3b3a299c4597e50980478.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth definition which you use to specify the value of the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. SyntaxRFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITIONNumeric ValueData TypeAccessApplies To1085462int32Read/WriteN/ARemarks The default value is 3dB.NameValu

### RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION

Specifies the bandwidth definition which you use to specify the value of the [RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__spectrum__rbw__filter_1ga5401380381540999fbd9c028e3e7bfd0.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085462 | int32 | Read/Write | N/A |

#### Remarks

The default value is **3dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION_3DB | 0 (0x0) | Defines the RBW in terms of the 3dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_TYPE attribute to FFT Based, RBW is the 3dB bandwidth of the window specified by the RFMXSPECAN_ATTR_SPECTRUM_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION_6DB | 1 (0x1) | Defines the RBW in terms of the 6dB bandwidth of the RBW filter. When you set the Spectrum RBW Filter Type attribute to FFT Based, RBW is the 6dB bandwidth of the window specified by the Spectrum FFT Window attribute. |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH | 2 (0x2) | Defines the RBW in terms of the spectrum bin width computed using FFT when you set the Spectrum RBW Filter Type attribute to FFT Based. |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION_ENBW | 3 (0x3) | Defines the RBW in terms of the ENBW bandwidth of the RBW filter. When you set the Spectrum RBW Filter Type attribute to FFT Based, RBW is the ENBW bandwidth of the window specified by the Spectrum FFT Window attribute. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__results_1ga82d828aa175904b77d2997098693b48c.html language=enus -->
## TOPIC 00326: RFMXSPECAN_ATTR_SPECTRUM_RESULTS_FREQUENCY_RESOLUTION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__results_1ga82d828aa175904b77d2997098693b48c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__results_1ga82d828aa175904b77d2997098693b48c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency bin spacing of the spectrum acquired by the measurement. This value is expressed in Hz. This attribute is not valid if you set the RFMXSPECAN_ATTR_SPECTRUM_SPAN attribute to 0. SyntaxRFMXSPECAN_ATTR_SPECTRUM_RESULTS_FREQUENCY_RESOLUTIONNumeric ValueData TypeAccessApplies To1085

### RFMXSPECAN_ATTR_SPECTRUM_RESULTS_FREQUENCY_RESOLUTION

Returns the frequency bin spacing of the spectrum acquired by the measurement. This value is expressed in Hz. This attribute is not valid if you set the [RFMXSPECAN_ATTR_SPECTRUM_SPAN](group____root__ni_r_fmx_spec_an__attributes__spectrum_1ga64c4baebb9eb52716e194995c3077e2a.html) attribute to 0.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_RESULTS_FREQUENCY_RESOLUTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085460 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__sweep__time_1gaff27bf82d51a851edf8b9b299879ecdd.html language=enus -->
## TOPIC 00327: RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__sweep__time_1gaff27bf82d51a851edf8b9b299879ecdd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__sweep__time_1gaff27bf82d51a851edf8b9b299879ecdd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To1085454int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the S

### RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085454 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spectrum__vbw__filter_1ga5748a6777f3fba4fdbd2d32df6892387.html language=enus -->
## TOPIC 00328: RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spectrum__vbw__filter_1ga5748a6777f3fba4fdbd2d32df6892387.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spectrum__vbw__filter_1ga5748a6777f3fba4fdbd2d32df6892387.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. SyntaxRFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To1085466int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_AUTO_BANDWIDTH

Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

#### Syntax

RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1085466 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPECTRUM_VBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | Specify the video bandwidth in the RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_BANDWIDTH attribute. The RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_VBW_TO_RBW_RATIO attribute is disregarded in this mode. |
| RFMXSPECAN_VAL_SPECTRUM_VBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_VBW_TO_RBW_RATIO attribute and the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. The value of the RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_BANDWIDTH attribute is disregarded in this mode. |

Parent topic:

VBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur_1ga7bb166473bcfaaa80b24c3539f30005a.html language=enus -->
## TOPIC 00329: RFMXSPECAN_ATTR_SPUR_TRACE_RANGE_INDEX

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur_1ga7bb166473bcfaaa80b24c3539f30005a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur_1ga7bb166473bcfaaa80b24c3539f30005a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the index of the range used to store and retrieve spurious emission (Spur) traces. This attribute is not used if you set the RFMXSPECAN_ATTR_SPUR_ALL_TRACES_ENABLED to FALSE. When you set this attribute to -1, the measurement stores and retrieves traces for all enabled ranges. SyntaxRFMXSP

### RFMXSPECAN_ATTR_SPUR_TRACE_RANGE_INDEX

Specifies the index of the range used to store and retrieve spurious emission (Spur) traces. This attribute is not used if you set the [RFMXSPECAN_ATTR_SPUR_ALL_TRACES_ENABLED](group____root__ni_r_fmx_spec_an__attributes__spur_1ga9896e19251de059e572720a2c38cf177.html) to FALSE. When you set this attribute to -1, the measurement stores and retrieves traces for all enabled ranges.

#### Syntax

RFMXSPECAN_ATTR_SPUR_TRACE_RANGE_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089568 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -1.

**Supported devices**: PXIe-5665/5668

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur_1gae1a310a886c57d38eccb0b5710d34aa7.html language=enus -->
## TOPIC 00330: RFMXSPECAN_ATTR_SPUR_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur_1gae1a310a886c57d38eccb0b5710d34aa7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur_1gae1a310a886c57d38eccb0b5710d34aa7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRF

### RFMXSPECAN_ATTR_SPUR_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXSPECAN_ATTR_SPUR_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089572 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXSPECAN_VAL_SPUR_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur_1gae2e70ba20d21dae09e75604f34794d1a.html language=enus -->
## TOPIC 00331: RFMXSPECAN_ATTR_SPUR_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur_1gae2e70ba20d21dae09e75604f34794d1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur_1gae2e70ba20d21dae09e75604f34794d1a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the spurious emission (Spur) measurement. SyntaxRFMXSPECAN_ATTR_SPUR_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1089536int32Read/WriteN/ARemarks You do not need to use a selector string to read this result for default signal and result instance. Refer to the

### RFMXSPECAN_ATTR_SPUR_MEASUREMENT_ENABLED

Specifies whether to enable the spurious emission (Spur) measurement.

#### Syntax

RFMXSPECAN_ATTR_SPUR_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089536 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

The default value is FALSE.

**Supported devices**: PXIe-5665/5668

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__averaging_1ga901425805529be0587f7ab3b90013689.html language=enus -->
## TOPIC 00332: RFMXSPECAN_ATTR_SPUR_AVERAGING_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__averaging_1ga901425805529be0587f7ab3b90013689.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__averaging_1ga901425805529be0587f7ab3b90013689.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spurious emission (Spur) measurement. SyntaxRFMXSPECAN_ATTR_SPUR_AVERAGING_TYPENumeric ValueData TypeAccessApplies To1089549int32Read/WriteN/ARemarks You do not need to use a selector string

### RFMXSPECAN_ATTR_SPUR_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for spurious emission (Spur) measurement.

#### Syntax

RFMXSPECAN_ATTR_SPUR_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089549 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__averaging_1gaec385eefea319e56876b66f4fe93c09b.html language=enus -->
## TOPIC 00333: RFMXSPECAN_ATTR_SPUR_AVERAGING_COUNT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__averaging_1gaec385eefea319e56876b66f4fe93c09b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__averaging_1gaec385eefea319e56876b66f4fe93c09b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_SPUR_AVERAGING_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_SPUR_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To1089546int32Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXSPECAN_ATTR_SPUR_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXSPECAN_ATTR_SPUR_AVERAGING_ENABLED](group____root__ni_r_fmx_spec_an__attributes__spur__averaging_1ga7a36320ef7995b7a5d2fd7f7eb4a1707.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_SPUR_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089546 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

**Supported devices**: PXIe-5665/5668

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__fft.html language=enus -->
## TOPIC 00334: FFT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__fft.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SPUR_FFT_WINDOWSpecifies the FFT window type to use to reduce spectral leakage. AttachmentsNone

### FFT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPUR_FFT_WINDOW | Specifies the FFT window type to use to reduce spectral leakage. |

#### Attachments

None

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__fft_1ga4f338043ecd0afaaef22f09cac5f7f21.html language=enus -->
## TOPIC 00335: RFMXSPECAN_ATTR_SPUR_FFT_WINDOW

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__fft_1ga4f338043ecd0afaaef22f09cac5f7f21.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__fft_1ga4f338043ecd0afaaef22f09cac5f7f21.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type to use to reduce spectral leakage. SyntaxRFMXSPECAN_ATTR_SPUR_FFT_WINDOWNumeric ValueData TypeAccessApplies To1089551int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sele

### RFMXSPECAN_ATTR_SPUR_FFT_WINDOW

Specifies the FFT window type to use to reduce spectral leakage.

#### Syntax

RFMXSPECAN_ATTR_SPUR_FFT_WINDOW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089551 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Flat Top**.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_NONE | 0 (0x0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_FLAT_TOP | 1 (0x1) | Measures single-tone amplitudes accurately. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HANNING | 2 (0x2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HAMMING | 3 (0x3) | Analyzes closely-spaced sine waves. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_GAUSSIAN | 4 (0x4) | Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN | 5 (0x5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN_HARRIS | 6 (0x6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_KAISER_BESSEL | 7 (0x7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range.html language=enus -->
## TOPIC 00336: Range

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAbsolute LimitDetectorRBW FilterSweep TimeVBW FilterGroup membersNameDescriptionRFMXSPECAN_ATTR_SPUR_NUMBER_OF_RANGESSpecifies the number of ranges. RFMXSPECAN_ATTR_SPUR_RANGE_ENABLEDSpecifies whether to measure the spurious emissions (Spur) in the frequency range. RFMXSPECAN_ATTR_SPUR_RANGE_N

### Range

#### Groups

- Absolute Limit
- Detector
- RBW Filter
- Sweep Time
- VBW Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPUR_NUMBER_OF_RANGES | Specifies the number of ranges. |
| RFMXSPECAN_ATTR_SPUR_RANGE_ENABLED | Specifies whether to measure the spurious emissions (Spur) in the frequency range. |
| RFMXSPECAN_ATTR_SPUR_RANGE_NUMBER_OF_SPURS_TO_REPORT | Specifies the number of spurious emissions (Spur) that the measurement should report in the frequency range. |
| RFMXSPECAN_ATTR_SPUR_RANGE_PEAK_EXCURSION | Specifies the peak excursion value used to find the spurs in the spectrum. This value is expressed in dB. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered a spur. |
| RFMXSPECAN_ATTR_SPUR_RANGE_PEAK_THRESHOLD | Specifies the threshold level above which the measurement detects spurs in the range that you specify using the RFMXSPECAN_ATTR_SPUR_RANGE_START_FREQUENCY and RFMXSPECAN_ATTR_SPUR_RANGE_STOP_FREQUENCY attributes. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_SPUR_RANGE_RELATIVE_ATTENUATION | Specifies the attenuation relative to the external attenuation specified by the RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION attribute. This value is expressed in dB. Use the Spur Range Rel Attn attribute to compensate for the variations in external attenuation when offset segments are spread wide in frequency. |
| RFMXSPECAN_ATTR_SPUR_RANGE_START_FREQUENCY | Specifies the start of the frequency range for the measurement. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_SPUR_RANGE_STOP_FREQUENCY | Specifies the stop of the frequency range for the measurement. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga353f8da486e104aa5888b94367c963ac.html language=enus -->
## TOPIC 00337: RFMXSPECAN_ATTR_SPUR_RANGE_START_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga353f8da486e104aa5888b94367c963ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga353f8da486e104aa5888b94367c963ac.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start of the frequency range for the measurement. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_START_FREQUENCYNumeric ValueData TypeAccessApplies To1089544float64Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read this attribute.The defa

### RFMXSPECAN_ATTR_SPUR_RANGE_START_FREQUENCY

Specifies the start of the frequency range for the measurement. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089544 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 500 MHz.

**Supported devices**: PXIe-5665/5668

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga693d35ef391ab6d5dc3a51a0007c9276.html language=enus -->
## TOPIC 00338: RFMXSPECAN_ATTR_SPUR_RANGE_STOP_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga693d35ef391ab6d5dc3a51a0007c9276.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga693d35ef391ab6d5dc3a51a0007c9276.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop of the frequency range for the measurement. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To1089545float64Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read this attribute.The defaul

### RFMXSPECAN_ATTR_SPUR_RANGE_STOP_FREQUENCY

Specifies the stop of the frequency range for the measurement. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089545 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1.5 GHz.

**Supported devices**: PXIe-5665/5668

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga82abcb9713623023a593242254a71f7a.html language=enus -->
## TOPIC 00339: RFMXSPECAN_ATTR_SPUR_RANGE_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga82abcb9713623023a593242254a71f7a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga82abcb9713623023a593242254a71f7a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to measure the spurious emissions (Spur) in the frequency range. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_ENABLEDNumeric ValueData TypeAccessApplies To1089541int32Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read this attribute.The default value is True.Supp

### RFMXSPECAN_ATTR_SPUR_RANGE_ENABLED

Specifies whether to measure the spurious emissions (Spur) in the frequency range.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089541 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **True**.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_FALSE | 0 (0x0) | Disables the acquisition of the frequency range. |
| RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_TRUE | 1 (0x1) | Enables measurement of Spurs in the frequency range. |

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga942f3eeedb107dc15a1045bc5dd0b878.html language=enus -->
## TOPIC 00340: RFMXSPECAN_ATTR_SPUR_RANGE_RELATIVE_ATTENUATION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga942f3eeedb107dc15a1045bc5dd0b878.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range_1ga942f3eeedb107dc15a1045bc5dd0b878.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation relative to the external attenuation specified by the RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION attribute. This value is expressed in dB. Use the Spur Range Rel Attn attribute to compensate for the variations in external attenuation when offset segments are spread wide in freque

### RFMXSPECAN_ATTR_SPUR_RANGE_RELATIVE_ATTENUATION

Specifies the attenuation relative to the external attenuation specified by the [RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION](group____root__ni_r_fmx_spec_an__attributes_1gac9b3a86f36d174f69641a611fdf4a53b.html) attribute. This value is expressed in dB. Use the Spur Range Rel Attn attribute to compensate for the variations in external attenuation when offset segments are spread wide in frequency.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_RELATIVE_ATTENUATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089542 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

**Supported devices**: PXIe-5665/5668

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__absolute__limit_1ga3233d4d9238c07d0b4ce3226902c7c7d.html language=enus -->
## TOPIC 00341: RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOP

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__absolute__limit_1ga3233d4d9238c07d0b4ce3226902c7c7d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__absolute__limit_1ga3233d4d9238c07d0b4ce3226902c7c7d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the absolute power limit corresponding to the end of the frequency range. This value is expressed in dBm. The measurement ignores this attribute when you set the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_MODE attribute to Couple. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOPNumeric

### RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOP

Specifies the absolute power limit corresponding to the end of the frequency range. This value is expressed in dBm. The measurement ignores this attribute when you set the [RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_MODE](group____root__ni_r_fmx_spec_an__attributes__spur__range__absolute__limit_1ga43687d77b6d0253e107fbb485a6f83b9.html) attribute to **Couple**.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089554 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is -10.

**Supported devices**: PXIe-5665/5668

Parent topic:

Absolute Limit

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__detector.html language=enus -->
## TOPIC 00342: Detector

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__detector.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__detector.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_POINTSSpecifies the number of range points after the detector is applied. RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_TYPESpecifies the type of detector to be used. AttachmentsNone

### Detector

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_POINTS | Specifies the number of range points after the detector is applied. |
| RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_TYPE | Specifies the type of detector to be used. |

#### Attachments

None

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__detector_1ga6379582895b12f6560213447b05700dc.html language=enus -->
## TOPIC 00343: RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_POINTS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__detector_1ga6379582895b12f6560213447b05700dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__detector_1ga6379582895b12f6560213447b05700dc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of range points after the detector is applied. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_POINTSNumeric ValueData TypeAccessApplies To1089574int32Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read this attribute.The default value is 1001.

### RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_POINTS

Specifies the number of range points after the detector is applied.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_POINTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089574 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1001.

Parent topic:

Detector

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__detector_1ga7261db3a30b0bb9683da060366814bf2.html language=enus -->
## TOPIC 00344: RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__detector_1ga7261db3a30b0bb9683da060366814bf2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__detector_1ga7261db3a30b0bb9683da060366814bf2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of detector to be used. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_TYPENumeric ValueData TypeAccessApplies To1089573int32Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read this attribute.Refer to Spectral Measurements Concepts topic for more informati

### RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_TYPE

Specifies the type of detector to be used.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_DETECTOR_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089573 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

Refer to [Spectral Measurements Concepts](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/spectral-measurements-concepts.html) topic for more information on detector types.

The default value is **None**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_NONE | 0 (0x0) | The detector is disabled. |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_SAMPLE | 1 (0x1) | The middle sample in the bucket is detected. |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_NORMAL | 2 (0x2) | The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_PEAK | 3 (0x3) | The maximum value of the samples in the bucket is detected. |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_NEGATIVE_PEAK | 4 (0x4) | The minimum value of the samples in the bucket is detected. |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_AVERAGE_RMS | 5 (0x5) | The average RMS of all the samples in the bucket is detected. |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_AVERAGE_VOLTAGE | 6 (0x6) | The average voltage of all the samples in the bucket is detected. |
| RFMXSPECAN_VAL_SPUR_RANGE_DETECTOR_TYPE_AVERAGE_LOG | 7 (0x7) | The average log of all the samples in the bucket is detected. |

Parent topic:

Detector

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter.html language=enus -->
## TOPIC 00345: RBW Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_AUTO_BANDWIDTHSpecifies whether the measurement computes the resolution bandwidth (RBW). RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acqui

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_AUTO_BANDWIDTH | Specifies whether the measurement computes the resolution bandwidth (RBW). |
| RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_AUTO_BANDWIDTH attribute to False. |
| RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION | Specifies the bandwidth definition which you use to specify the value of the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE | Specifies the shape of the digital resolution bandwidth (RBW) filter. |

#### Attachments

None

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1ga2eac29ac1ff815bc625c3afd61aace74.html language=enus -->
## TOPIC 00346: RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1ga2eac29ac1ff815bc625c3afd61aace74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1ga2eac29ac1ff815bc625c3afd61aace74.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth definition which you use to specify the value of the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH attribute. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITIONNumeric ValueData TypeAccessApplies To1089571int32Read/WriteRangeRemarks Use "range<n>" as the Selec

### RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION

Specifies the bandwidth definition which you use to specify the value of the [RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1gad7d8ddc1592947f03737ffcb9429ea34.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089571 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **3dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_3DB | 0 (0x0) | Defines the RBW in terms of the 3dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE attribute to FFT Based, RBW is the 3dB bandwidth of the window specified by the RFMXSPECAN_ATTR_SPUR_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH | 2 (0x2) | Defines the RBW in terms of the spectrum bin width computed using FFT when you set the Spur Range RBW Filter Type attribute to FFT Based. |
| RFMXSPECAN_VAL_SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION_ENBW | 3 (0x3) | Defines the RBW in terms of the ENBW bandwidth of the RBW filter. When you set the Spur RBW Filter Type attribute to FFT Based, RBW is the ENBW bandwidth of the window specified by the Spur FFT Window attribute. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1ga9ea598fa21f98a7de4e3fd4fd782eebe.html language=enus -->
## TOPIC 00347: RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1ga9ea598fa21f98a7de4e3fd4fd782eebe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1ga9ea598fa21f98a7de4e3fd4fd782eebe.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital resolution bandwidth (RBW) filter. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To1089557int32Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read this attribute.The default value is Gaussian.Suppo

### RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE

Specifies the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089557 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **Gaussian**.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |
| RFMXSPECAN_VAL_SPUR_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXSPECAN_VAL_SPUR_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1gad7d8ddc1592947f03737ffcb9429ea34.html language=enus -->
## TOPIC 00348: RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1gad7d8ddc1592947f03737ffcb9429ea34.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1gad7d8ddc1592947f03737ffcb9429ea34.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_AUTO_BANDWIDTH attribute to False.SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To1089556float64Read/W

### RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the [RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__spur__range__rbw__filter_1gadabeb62b5a4f573568566fb706736874.html) attribute to **False.**

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089556 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 10 kHz.

**Supported devices**: PXIe-5665/5668

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__sweep__time_1ga45be1a6fff92578f94a557363ad109b4.html language=enus -->
## TOPIC 00349: RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__sweep__time_1ga45be1a6fff92578f94a557363ad109b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__sweep__time_1ga45be1a6fff92578f94a557363ad109b4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To1089558int32Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read this attribute.The default value is True.Supported devices: P

### RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089558 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **True**.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_SPUR_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH attribute. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__sweep__time_1ga5d03924fd8e0eb4173b90c36c07b4cca.html language=enus -->
## TOPIC 00350: RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__sweep__time_1ga5d03924fd8e0eb4173b90c36c07b4cca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__sweep__time_1ga5d03924fd8e0eb4173b90c36c07b4cca.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_AUTO attribute to False. This value is expressed in seconds. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To1089559float64Read/WriteRangeRemarks Use "range<n>" as the Selector S

### RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_INTERVAL

Specifies the sweep time when you set the [RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_AUTO](group____root__ni_r_fmx_spec_an__attributes__spur__range__sweep__time_1ga45be1a6fff92578f94a557363ad109b4.html) attribute to **False**. This value is expressed in seconds.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089559 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.001.

**Supported devices**: PXIe-5665/5668

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__vbw__filter_1ga40434fd28802fc741a28b050a229c90d.html language=enus -->
## TOPIC 00351: RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__vbw__filter_1ga40434fd28802fc741a28b050a229c90d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__vbw__filter_1ga40434fd28802fc741a28b050a229c90d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To1089575int32Read/WriteRangeRemarks Use "range<n>" as the Selector String to configure or read t

### RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH

Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089575 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | Specify the video bandwidth in the RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH attribute. The RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_VBW_TO_RBW_RATIO attribute is disregarded in this mode. |
| RFMXSPECAN_VAL_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH attribute and the RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH attribute. The value of the RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH attribute is disregarded in this mode. |

Parent topic:

VBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__range__vbw__filter_1gacfdddb7076402f03649704851d495ff8.html language=enus -->
## TOPIC 00352: RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__range__vbw__filter_1gacfdddb7076402f03649704851d495ff8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__range__vbw__filter_1gacfdddb7076402f03649704851d495ff8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the video bandwidth (VBW) in Hz when you set the RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH attribute to False. SyntaxRFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To1089576float64Read/WriteRangeRemarks Use "range<n>" as the Selector String to

### RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH

Specifies the video bandwidth (VBW) in Hz when you set the [RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__spur__range__vbw__filter_1ga40434fd28802fc741a28b050a229c90d.html) attribute to **False**.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089576 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 30000.

Parent topic:

VBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__results__range_1gaa2835867758bf9f64e2aa281c900bfef.html language=enus -->
## TOPIC 00353: RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MEASUREMENT_STATUS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__results__range_1gaa2835867758bf9f64e2aa281c900bfef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__results__range_1gaa2835867758bf9f64e2aa281c900bfef.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement status for the frequency range. SyntaxRFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To1089566int32Read-OnlyRangeRemarks Use "range<n>" as the Selector String to read this result.Supported devices: PXIe-5665/5668NameValueDescription

### RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MEASUREMENT_STATUS

Indicates the measurement status for the frequency range.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089566 | int32 | Read-Only | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_SPUR_RANGE_STATUS_FAIL | 0 (0x0) | The amplitude of the detected spurs is greater than the value of the RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_ABSOLUTE_LIMIT attribute. |
| RFMXSPECAN_VAL_SPUR_RANGE_STATUS_PASS | 1 (0x1) | The amplitude of the detected spurs is lower than the value of the Spur Results Spur Abs Limit attribute. |

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga1cf7379d8cee7da5e673b371ad34b68a.html language=enus -->
## TOPIC 00354: RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_AMPLITUDE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga1cf7379d8cee7da5e673b371ad34b68a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga1cf7379d8cee7da5e673b371ad34b68a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the amplitude of the detected spurious emissions (Spur). This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_AMPLITUDENumeric ValueData TypeAccessApplies To1089563float64Read-OnlySpurRemarks Use "range<n>/spur<k>" as the Selector String to read this result.Supported devi

### RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_AMPLITUDE

Returns the amplitude of the detected spurious emissions (Spur). This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_AMPLITUDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089563 | float64 | Read-Only | Spur |

#### Remarks

Use "range<n>/spur<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

**Supported devices**: PXIe-5665/5668

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga4b100d06a6b6458d5faf588f139b90c9.html language=enus -->
## TOPIC 00355: RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MARGIN

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga4b100d06a6b6458d5faf588f139b90c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga4b100d06a6b6458d5faf588f139b90c9.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the difference between the amplitude and the absolute limit of the detected spurious emissions (Spur) at the Spur frequency. SyntaxRFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MARGINNumeric ValueData TypeAccessApplies To1089565float64Read-OnlySpurRemarks Use "range<n>/spur<k>" as the Selector String t

### RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MARGIN

Returns the difference between the amplitude and the absolute limit of the detected spurious emissions (Spur) at the Spur frequency.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_MARGIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089565 | float64 | Read-Only | Spur |

#### Remarks

Use "range<n>/spur<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

**Supported devices**: PXIe-5665/5668

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga6e617e1af3ac3ac23996f53f72e74b42.html language=enus -->
## TOPIC 00356: RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_ABSOLUTE_LIMIT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga6e617e1af3ac3ac23996f53f72e74b42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__spur__results__range__spur_1ga6e617e1af3ac3ac23996f53f72e74b42.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the threshold used to calculate the margin of the detected spurious emissions (Spur). This value is expressed in dBm. The measurement calculates the threshold using the absolute limit line specified by the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_MODE attribute. SyntaxRFMXSPECAN_ATTR_SPUR_R

### RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_ABSOLUTE_LIMIT

Returns the threshold used to calculate the margin of the detected spurious emissions (Spur). This value is expressed in dBm. The measurement calculates the threshold using the absolute limit line specified by the [RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_MODE](group____root__ni_r_fmx_spec_an__attributes__spur__range__absolute__limit_1ga43687d77b6d0253e107fbb485a6f83b9.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_SPUR_RESULTS_RANGE_ABSOLUTE_LIMIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1089564 | float64 | Read-Only | Spur |

#### Remarks

Use "range<n>/spur<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

**Supported devices**: PXIe-5665/5668

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger.html language=enus -->
## TOPIC 00357: Trigger

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXSPECAN_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. RFMXSPECAN_ATTR_TRIGGER_TYPESpecifies the trigger type. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. |
| RFMXSPECAN_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger_1ga081f1c398d7937f2a28c884274b470a6.html language=enus -->
## TOPIC 00358: RFMXSPECAN_ATTR_TRIGGER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger_1ga081f1c398d7937f2a28c884274b470a6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger_1ga081f1c398d7937f2a28c884274b470a6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxRFMXSPECAN_ATTR_TRIGGER_TYPENumeric ValueData TypeAccessApplies To1048580int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about

### RFMXSPECAN_ATTR_TRIGGER_TYPE

Specifies the trigger type.

#### Syntax

RFMXSPECAN_ATTR_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1048580 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **None**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TRIGGER_TYPE_NONE | 0 (0x0) | No Reference Trigger is configured. |
| RFMXSPECAN_VAL_TRIGGER_TYPE_DIGITAL_EDGE | 1 (0x1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXSPECAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXSPECAN_VAL_TRIGGER_TYPE_IQ_POWER_EDGE | 2 (0x2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXSPECAN_VAL_TRIGGER_TYPE_SOFTWARE | 3 (0x3) | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge.html language=enus -->
## TOPIC 00359: IQ Power Edge

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVELSpecifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and is expressed in dBm when you set the IQ P

### IQ Power Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL | Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and is expressed in dBm when you set the IQ Power Edge Level Type attribute to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE | Specifies the reference for the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gabf727e88729592fdcc5bc656c9965a47.html language=enus -->
## TOPIC 00360: RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gabf727e88729592fdcc5bc656c9965a47.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gabf727e88729592fdcc5bc656c9965a47.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and is expressed in dBm when you set the IQ Power Edge Level Type attribute to Absolute. The device asserts the trigger when t

### RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE](group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gaeff1543fe85bc545d8f29c1e610de8c3.html) attribute to **Relative** and is expressed in dBm when you set the IQ Power Edge Level Type attribute to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the [RFMXSPECAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_spec_an__attributes__trigger_1ga081f1c398d7937f2a28c884274b470a6.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1048584 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gae95c5e4bec9de649a8e419ea3e8f0dc9.html language=enus -->
## TOPIC 00361: RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gae95c5e4bec9de649a8e419ea3e8f0dc9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gae95c5e4bec9de649a8e419ea3e8f0dc9.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to

### RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the [RFMXSPECAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_spec_an__attributes__trigger_1ga081f1c398d7937f2a28c884274b470a6.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1048585 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gaeb86bb7fb950f00dbec8671a6b57629b.html language=enus -->
## TOPIC 00362: RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gaeb86bb7fb950f00dbec8671a6b57629b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gaeb86bb7fb950f00dbec8671a6b57629b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To1048583char[]Read/WriteN/ARemarks You do not

### RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the [RFMXSPECAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_spec_an__attributes__trigger_1ga081f1c398d7937f2a28c884274b470a6.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1048583 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gaeff1543fe85bc545d8f29c1e610de8c3.html language=enus -->
## TOPIC 00363: RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gaeff1543fe85bc545d8f29c1e610de8c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gaeff1543fe85bc545d8f29c1e610de8c3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXSPECAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPENumeric ValueData TypeAccessAppli

### RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

Specifies the reference for the [RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gabf727e88729592fdcc5bc656c9965a47.html) attribute. The IQ Power Edge Level Type attribute is used only when you set the [RFMXSPECAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_spec_an__attributes__trigger_1ga081f1c398d7937f2a28c884274b470a6.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052671 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Absolute**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The IQ Power Edge Level attribute is relative to the value of the RFMXSPECAN_ATTR_REFERENCE_LEVEL attribute. |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00364: Minimum Quiet Time

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to Falling Slope, the signal is quiet above the trigger level. |
| RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time_1ga9329b66d86293b98ddea31d4c7322a78.html language=enus -->
## TOPIC 00365: RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time_1ga9329b66d86293b98ddea31d4c7322a78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time_1ga9329b66d86293b98ddea31d4c7322a78.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute to Rising Slope, the signal is quiet below the trigger level. If you set

### RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the [RFMXSPECAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE](group____root__ni_r_fmx_spec_an__attributes__trigger__iq__power__edge_1gae95c5e4bec9de649a8e419ea3e8f0dc9.html) attribute to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to **Falling Slope**, the signal is quiet above the trigger level.

#### Syntax

RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1048588 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time_1gad78a12001630d22e1beb959bc8b40744.html language=enus -->
## TOPIC 00366: RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time_1gad78a12001630d22e1beb959bc8b40744.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__trigger__minimum__quiet__time_1gad78a12001630d22e1beb959bc8b40744.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. SyntaxRFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODENumeric ValueData TypeAccessApplies To1048587int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defa

### RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

Specifies whether the measurement computes the minimum quiet time used for triggering.

#### Syntax

RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1048587 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Manual**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |
| RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp.html language=enus -->
## TOPIC 00367: TXP

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingRBW FilterResultsThresholdVBW FilterGroup membersNameDescriptionRFMXSPECAN_ATTR_TXP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the TXP measurement. RFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLEDSpecifies whether to enable the TXP meas

### TXP

#### Groups

- Averaging
- RBW Filter
- Results
- Threshold
- VBW Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TXP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement. |
| RFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLED | Specifies whether to enable the TXP measurement. |
| RFMXSPECAN_ATTR_TXP_MEASUREMENT_INTERVAL | Specifies the acquisition time for the TXP measurement. This value is expressed in seconds. |
| RFMXSPECAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for TXP measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp_1ga28fc1dc354085c80dda7cfc06f84384d.html language=enus -->
## TOPIC 00368: RFMXSPECAN_ATTR_TXP_MEASUREMENT_INTERVAL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp_1ga28fc1dc354085c80dda7cfc06f84384d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp_1ga28fc1dc354085c80dda7cfc06f84384d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition time for the TXP measurement. This value is expressed in seconds. SyntaxRFMXSPECAN_ATTR_TXP_MEASUREMENT_INTERVALNumeric ValueData TypeAccessApplies To1093634float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defa

### RFMXSPECAN_ATTR_TXP_MEASUREMENT_INTERVAL

Specifies the acquisition time for the TXP measurement. This value is expressed in seconds.

#### Syntax

RFMXSPECAN_ATTR_TXP_MEASUREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093634 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.001.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp_1ga434fbae2691fc13723122ac28241c56f.html language=enus -->
## TOPIC 00369: RFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp_1ga434fbae2691fc13723122ac28241c56f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp_1ga434fbae2691fc13723122ac28241c56f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the TXP measurement. SyntaxRFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1093632int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Str

### RFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLED

Specifies whether to enable the TXP measurement.

#### Syntax

RFMXSPECAN_ATTR_TXP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093632 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp_1gad6d7b81554ea3ff722c0843fbea98bd5.html language=enus -->
## TOPIC 00370: RFMXSPECAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp_1gad6d7b81554ea3ff722c0843fbea98bd5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp_1gad6d7b81554ea3ff722c0843fbea98bd5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for TXP measurement. SyntaxRFMXSPECAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To1093635int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threads y

### RFMXSPECAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for TXP measurement.

#### Syntax

RFMXSPECAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093635 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp_1gaf3320df012d135600d9bc54a15f77c5d.html language=enus -->
## TOPIC 00371: RFMXSPECAN_ATTR_TXP_ALL_TRACES_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp_1gaf3320df012d135600d9bc54a15f77c5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp_1gaf3320df012d135600d9bc54a15f77c5d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement. SyntaxRFMXSPECAN_ATTR_TXP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To1093648int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXSPECAN_ATTR_TXP_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement.

#### Syntax

RFMXSPECAN_ATTR_TXP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093648 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__averaging.html language=enus -->
## TOPIC 00372: Averaging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__averaging.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_TXP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True. RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLEDSpecifies whether to enable averaging for the TXP measuremen

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED | Specifies whether to enable averaging for the TXP measurement. |
| RFMXSPECAN_ATTR_TXP_AVERAGING_TYPE | Specifies the averaging type for the TXP measurement. The averaged power trace is used for the measurement. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga5bdd40ee5530faa798c63bc5616e8510.html language=enus -->
## TOPIC 00373: RFMXSPECAN_ATTR_TXP_AVERAGING_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga5bdd40ee5530faa798c63bc5616e8510.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga5bdd40ee5530faa798c63bc5616e8510.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for the TXP measurement. The averaged power trace is used for the measurement. SyntaxRFMXSPECAN_ATTR_TXP_AVERAGING_TYPENumeric ValueData TypeAccessApplies To1093640int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXSPECAN_ATTR_TXP_AVERAGING_TYPE

Specifies the averaging type for the TXP measurement. The averaged power trace is used for the measurement.

#### Syntax

RFMXSPECAN_ATTR_TXP_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093640 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_RMS | 0 (0x0) | The power trace is linearly averaged. |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_LOG | 1 (0x1) | The power trace is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power trace is averaged. |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The maximum instantaneous power in the power trace is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The minimum instantaneous power in the power trace is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga76b1c26daab3a47e84f31e4b216d5d76.html language=enus -->
## TOPIC 00374: RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga76b1c26daab3a47e84f31e4b216d5d76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga76b1c26daab3a47e84f31e4b216d5d76.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_TXP_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To1093637int32Read/WriteN/ARemarks You do not need to use a selector string to configure or r

### RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED](group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga8352c2976ecc6daa5f2027a8fdb7350f.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093637 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga8352c2976ecc6daa5f2027a8fdb7350f.html language=enus -->
## TOPIC 00375: RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga8352c2976ecc6daa5f2027a8fdb7350f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga8352c2976ecc6daa5f2027a8fdb7350f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the TXP measurement. SyntaxRFMXSPECAN_ATTR_TXP_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To1093638int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED

Specifies whether to enable averaging for the TXP measurement.

#### Syntax

RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093638 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TXP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXSPECAN_VAL_TXP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The TXP measurement uses the RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT attribute as the number of acquisitions over which the TXP measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter.html language=enus -->
## TOPIC 00376: RBW Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHASpecifies the roll-off factor for the root-raised-cosine (RRC) filter. RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expresse

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHA | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_TXP_RBW_FILTER_TYPE | Specifies the shape of the digital resolution bandwidth (RBW) filter. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1ga63ab4a1e8138ad6c7d0aab36857b5e50.html language=enus -->
## TOPIC 00377: RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1ga63ab4a1e8138ad6c7d0aab36857b5e50.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1ga63ab4a1e8138ad6c7d0aab36857b5e50.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To1093642float64Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093642 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 100 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1gabc7d5cf4e651d14431918feee21e275f.html language=enus -->
## TOPIC 00378: RFMXSPECAN_ATTR_TXP_RBW_FILTER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1gabc7d5cf4e651d14431918feee21e275f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1gabc7d5cf4e651d14431918feee21e275f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital resolution bandwidth (RBW) filter. SyntaxRFMXSPECAN_ATTR_TXP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To1093643int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to

### RFMXSPECAN_ATTR_TXP_RBW_FILTER_TYPE

Specifies the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

RFMXSPECAN_ATTR_TXP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093643 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_NONE | 5 (0x5) | The measurement does not use any RBW filtering. |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_RRC | 6 (0x6) | The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHA attribute is used as the RBW filter. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1gadf3c018e93019f20fe9d9e63f2f652fd.html language=enus -->
## TOPIC 00379: RFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHA

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1gadf3c018e93019f20fe9d9e63f2f652fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__rbw__filter_1gadf3c018e93019f20fe9d9e63f2f652fd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxRFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHANumeric ValueData TypeAccessApplies To1093641float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refe

### RFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHA

Specifies the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

RFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093641 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.1.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__results.html language=enus -->
## TOPIC 00380: Results

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__results.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_TXP_RESULTS_AVERAGE_MEAN_POWERReturns the mean power of the signal. This value is expressed in dBm. Only the samples above the threshold are used by the measurement when you set the RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED attribute to True. When yo

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TXP_RESULTS_AVERAGE_MEAN_POWER | Returns the mean power of the signal. This value is expressed in dBm. Only the samples above the threshold are used by the measurement when you set the RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED attribute to True. When you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True, the mean power is measured using the power trace averaged over multiple acquisitions. |
| RFMXSPECAN_ATTR_TXP_RESULTS_MAXIMUM_POWER | Returns the maximum power of the averaged power trace. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_TXP_RESULTS_MINIMUM_POWER | Returns the minimum power of the averaged power trace. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_TXP_RESULTS_PEAK_TO_AVERAGE_RATIO | Returns the ratio of the peak power of the signal to the mean power. Only the samples above the threshold are used by the measurement when you set the RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED attribute to True. When you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True, the peak and mean powers are measured using the power trace averaged over multiple acquisitions. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga138b943f5d8922c0822c6a0c7fc58801.html language=enus -->
## TOPIC 00381: RFMXSPECAN_ATTR_TXP_RESULTS_MINIMUM_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga138b943f5d8922c0822c6a0c7fc58801.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga138b943f5d8922c0822c6a0c7fc58801.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum power of the averaged power trace. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_TXP_RESULTS_MINIMUM_POWERNumeric ValueData TypeAccessApplies To1093652float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result ins

### RFMXSPECAN_ATTR_TXP_RESULTS_MINIMUM_POWER

Returns the minimum power of the averaged power trace. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_TXP_RESULTS_MINIMUM_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093652 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga1d5c030af6b60fffd7a99424bcfb664b.html language=enus -->
## TOPIC 00382: RFMXSPECAN_ATTR_TXP_RESULTS_MAXIMUM_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga1d5c030af6b60fffd7a99424bcfb664b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga1d5c030af6b60fffd7a99424bcfb664b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum power of the averaged power trace. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_TXP_RESULTS_MAXIMUM_POWERNumeric ValueData TypeAccessApplies To1093651float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result ins

### RFMXSPECAN_ATTR_TXP_RESULTS_MAXIMUM_POWER

Returns the maximum power of the averaged power trace. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_TXP_RESULTS_MAXIMUM_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093651 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga276a2eb72c7836e81280e60e2c0c01ca.html language=enus -->
## TOPIC 00383: RFMXSPECAN_ATTR_TXP_RESULTS_AVERAGE_MEAN_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga276a2eb72c7836e81280e60e2c0c01ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__results_1ga276a2eb72c7836e81280e60e2c0c01ca.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power of the signal. This value is expressed in dBm. Only the samples above the threshold are used by the measurement when you set the RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED attribute to True. When you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True, the mean power is

### RFMXSPECAN_ATTR_TXP_RESULTS_AVERAGE_MEAN_POWER

Returns the mean power of the signal. This value is expressed in dBm. Only the samples above the threshold are used by the measurement when you set the [RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED](group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1gae2bc7e4ab18f8bf177bf90fadb8ae7e5.html) attribute to **True**. When you set the [RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED](group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga8352c2976ecc6daa5f2027a8fdb7350f.html) attribute to **True**, the mean power is measured using the power trace averaged over multiple acquisitions.

#### Syntax

RFMXSPECAN_ATTR_TXP_RESULTS_AVERAGE_MEAN_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093649 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__results_1gadef5c481ebe5e7e06de14977bb17a3a4.html language=enus -->
## TOPIC 00384: RFMXSPECAN_ATTR_TXP_RESULTS_PEAK_TO_AVERAGE_RATIO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__results_1gadef5c481ebe5e7e06de14977bb17a3a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__results_1gadef5c481ebe5e7e06de14977bb17a3a4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the ratio of the peak power of the signal to the mean power. Only the samples above the threshold are used by the measurement when you set the RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED attribute to True. When you set the RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED attribute to True, the peak and mean

### RFMXSPECAN_ATTR_TXP_RESULTS_PEAK_TO_AVERAGE_RATIO

Returns the ratio of the peak power of the signal to the mean power. Only the samples above the threshold are used by the measurement when you set the [RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED](group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1gae2bc7e4ab18f8bf177bf90fadb8ae7e5.html) attribute to **True**. When you set the [RFMXSPECAN_ATTR_TXP_AVERAGING_ENABLED](group____root__ni_r_fmx_spec_an__attributes__txp__averaging_1ga8352c2976ecc6daa5f2027a8fdb7350f.html) attribute to **True**, the peak and mean powers are measured using the power trace averaged over multiple acquisitions.

#### Syntax

RFMXSPECAN_ATTR_TXP_RESULTS_PEAK_TO_AVERAGE_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093650 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__threshold.html language=enus -->
## TOPIC 00385: Threshold

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__threshold.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__threshold.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLEDSpecifies whether to enable thresholding of the acquired samples to be used for the TXP measurement. RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVELSpecifies either the relative or absolute threshold power level based on the value of the

### Threshold

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED | Specifies whether to enable thresholding of the acquired samples to be used for the TXP measurement. |
| RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL | Specifies either the relative or absolute threshold power level based on the value of the RFMXSPECAN_ATTR_TXP_THRESHOLD_TYPE attribute. |
| RFMXSPECAN_ATTR_TXP_THRESHOLD_TYPE | Specifies the reference for the power level used for thresholding. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1ga587dc71022531b890adbe8f487b99a23.html language=enus -->
## TOPIC 00386: RFMXSPECAN_ATTR_TXP_THRESHOLD_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1ga587dc71022531b890adbe8f487b99a23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1ga587dc71022531b890adbe8f487b99a23.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the power level used for thresholding. SyntaxRFMXSPECAN_ATTR_TXP_THRESHOLD_TYPENumeric ValueData TypeAccessApplies To1093646int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXSPECAN_ATTR_TXP_THRESHOLD_TYPE

Specifies the reference for the power level used for thresholding.

#### Syntax

RFMXSPECAN_ATTR_TXP_THRESHOLD_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093646 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TXP_THRESHOLD_TYPE_RELATIVE | 0 (0x0) | The threshold is relative to the peak power of the acquired samples. |
| RFMXSPECAN_VAL_TXP_THRESHOLD_TYPE_ABSOLUTE | 1 (0x1) | The threshold is the absolute power, in dBm. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1ga86f730923d2ac7068c80121c34c83a06.html language=enus -->
## TOPIC 00387: RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1ga86f730923d2ac7068c80121c34c83a06.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1ga86f730923d2ac7068c80121c34c83a06.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies either the relative or absolute threshold power level based on the value of the RFMXSPECAN_ATTR_TXP_THRESHOLD_TYPE attribute. SyntaxRFMXSPECAN_ATTR_TXP_THRESHOLD_LEVELNumeric ValueData TypeAccessApplies To1093645float64Read/WriteN/ARemarks The default value is -20.

### RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL

Specifies either the relative or absolute threshold power level based on the value of the [RFMXSPECAN_ATTR_TXP_THRESHOLD_TYPE](group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1ga587dc71022531b890adbe8f487b99a23.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093645 | float64 | Read/Write | N/A |

#### Remarks

The default value is -20.

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1gae2bc7e4ab18f8bf177bf90fadb8ae7e5.html language=enus -->
## TOPIC 00388: RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1gae2bc7e4ab18f8bf177bf90fadb8ae7e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__threshold_1gae2bc7e4ab18f8bf177bf90fadb8ae7e5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable thresholding of the acquired samples to be used for the TXP measurement. SyntaxRFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLEDNumeric ValueData TypeAccessApplies To1093644int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the

### RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED

Specifies whether to enable thresholding of the acquired samples to be used for the TXP measurement.

#### Syntax

RFMXSPECAN_ATTR_TXP_THRESHOLD_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093644 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_FALSE | 0 (0x0) | All the acquired samples are considered for the TXP measurement. |
| RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_TRUE | 1 (0x1) | The samples above the threshold level specified in the RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL attribute are considered for the TXP measurement. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter.html language=enus -->
## TOPIC 00389: VBW Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTHSpecifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. RFMXSPECAN_ATTR_TXP_VBW_FILTER_BANDWIDTHSpecifies the video bandwidth when you set the RFMXSPECAN_ATTR_TXP_V

### VBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH | Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. |
| RFMXSPECAN_ATTR_TXP_VBW_FILTER_BANDWIDTH | Specifies the video bandwidth when you set the RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH attribute to False. |
| RFMXSPECAN_ATTR_TXP_VBW_FILTER_VBW_TO_RBW_RATIO | Specifies the VBW to RBW Ratio when you set the RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH attribute to True. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter_1ga223633e96e58005e27d98931085fa079.html language=enus -->
## TOPIC 00390: RFMXSPECAN_ATTR_TXP_VBW_FILTER_VBW_TO_RBW_RATIO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter_1ga223633e96e58005e27d98931085fa079.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter_1ga223633e96e58005e27d98931085fa079.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the VBW to RBW Ratio when you set the RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH attribute to True. SyntaxRFMXSPECAN_ATTR_TXP_VBW_FILTER_VBW_TO_RBW_RATIONumeric ValueData TypeAccessApplies To1093657float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read

### RFMXSPECAN_ATTR_TXP_VBW_FILTER_VBW_TO_RBW_RATIO

Specifies the VBW to RBW Ratio when you set the [RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter_1gac42a3a22c05959c89f86c7d1126c6260.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_TXP_VBW_FILTER_VBW_TO_RBW_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093657 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 3.

Parent topic:

VBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter_1gac42a3a22c05959c89f86c7d1126c6260.html language=enus -->
## TOPIC 00391: RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter_1gac42a3a22c05959c89f86c7d1126c6260.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__txp__vbw__filter_1gac42a3a22c05959c89f86c7d1126c6260.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio. SyntaxRFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To1093655int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this at

### RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH

Specifies whether the video bandwidth (VBW) is expressed directly or computed based on the VBW to RBW ratio.

#### Syntax

RFMXSPECAN_ATTR_TXP_VBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1093655 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_TXP_VBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | Specify the video bandwidth in the RFMXSPECAN_ATTR_TXP_VBW_FILTER_BANDWIDTH attribute. The RFMXSPECAN_ATTR_TXP_VBW_FILTER_VBW_TO_RBW_RATIO attribute is disregarded in this mode. |
| RFMXSPECAN_VAL_TXP_VBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the RFMXSPECAN_ATTR_TXP_VBW_FILTER_VBW_TO_RBW_RATIO attribute and the RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH attribute. The value of the RFMXSPECAN_ATTR_TXP_VBW_FILTER_BANDWIDTH attribute is disregarded in this mode. |

Parent topic:

VBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions_1ga3103e819d6b650186e9c5868e8e3da17.html language=enus -->
## TOPIC 00392: RFmxSpecAn_Initialize

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions_1ga3103e819d6b650186e9c5868e8e3da17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions_1ga3103e819d6b650186e9c5868e8e3da17.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxSpecAn_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNew

### RFmxSpecAn_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxSpecAn_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

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
| isNewSession | [out] | int32 * | Returns RFMXSPECAN_VAL_TRUE if the function created a new session, or RFMXSPECAN_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions_1ga814821bca761db4f663ed912a66b511d.html language=enus -->
## TOPIC 00393: RFmxSpecAn_Close

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions_1ga814821bca761db4f663ed912a66b511d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions_1ga814821bca761db4f663ed912a66b511d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the device. Syntaxint32 __stdcall RFmxSpecAn_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the RFmxInstr_Close function.Enabling the SFP (Soft Front Panel) debug has a performance impact.

### RFmxSpecAn_Close

Closes the session to the device.

#### Syntax

int32 __stdcall RFmxSpecAn_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?context=rfmxinstr_rfmxinstrcref_function_close) function.

Note

Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| forceDestroy | [in] | int32 | Specifies whether to destroy the RFmx session.ValueDescriptionRFMXSPECAN_VAL_FALSE (0)Destroys the RFmx session. Call the RFmxSpecAn_Close function a number of times equal to the number of times you obtained a reference to the RFmx session.RFMXSPECAN_VAL_TRUE (1)Destroys the RFmx session. You do not have to call the RFmxSpecAn_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| Value | Description |  |  |
| RFMXSPECAN_VAL_FALSE (0) | Destroys the RFmx session. Call the RFmxSpecAn_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |  |
| RFMXSPECAN_VAL_TRUE (1) | Destroys the RFmx session. You do not have to call the RFmxSpecAn_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions_1gaae0429d77484035c5c00d9938f32ad5c.html language=enus -->
## TOPIC 00394: RFmxSpecAn_GetErrorString

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions_1gaae0429d77484035c5c00d9938f32ad5c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions_1gaae0429d77484035c5c00d9938f32ad5c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxSpecAn function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxSpecAn_GetErrorString(niRFmxInstrHand

### RFmxSpecAn_GetErrorString

Converts a status code returned by an RFmxSpecAn function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxSpecAn_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxSpecAn function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html language=enus -->
## TOPIC 00395: RFmxSpecAn_GetError

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxSpecAn_GetError(niRFmxInstr

### RFmxSpecAn_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxSpecAn_GetErrorString](group____root__ni_r_fmx_spec_an__functions_1gaae0429d77484035c5c00d9938f32ad5c.html) function if the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function does not return an error message.

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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__advanced__analyze2_1gab8d16a8c37946a5570ea44ecaf27b2fd.html language=enus -->
## TOPIC 00396: RFmxSpecAn_AnalyzeSpectrum1Waveform

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__advanced__analyze2_1gab8d16a8c37946a5570ea44ecaf27b2fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__advanced__analyze2_1gab8d16a8c37946a5570ea44ecaf27b2fd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum that you specify in the Spectrum parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only i

### RFmxSpecAn_AnalyzeSpectrum1Waveform

Performs the enabled measurements on the spectrum that you specify in the **Spectrum** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **Spectral** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxSpecAn_AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxSpecAn_Commit](group____root__ni_r_fmx_spec_an__functions__utility_1ga0b1bbff43460309542c53d46fa8abc32.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance.Example:"""result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start frequency of the spectrum. This value is expressed in Hz. |
| dx | [in] | float64 | This parameter specifies the frequency interval between data points in the spectrum. |
| spectrum | [in] | float32[] | This parameter specifies the real-value power spectrum. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__acp__array_1ga4f6fe562c16d134511aae6be40638b39.html language=enus -->
## TOPIC 00397: RFmxSpecAn_ACPCfgOffsetRRCFilterArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__acp__array_1ga4f6fe562c16d134511aae6be40638b39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__acp__array_1ga4f6fe562c16d134511aae6be40638b39.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the root raised cosine (RRC) channel filter to be applied on the offset channel before measuring channel power. Syntaxint32 __stdcall RFmxSpecAn_ACPCfgOffsetRRCFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rrcFilterEnabled[], float64 rrcAlpha[], int32 number

### RFmxSpecAn_ACPCfgOffsetRRCFilterArray

Configures the root raised cosine (RRC) channel filter to be applied on the offset channel before measuring channel power.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPCfgOffsetRRCFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rrcFilterEnabled[], float64 rrcAlpha[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| rrcFilterEnabled | [in] | int32[] | This parameter specifies whether to apply the root-raised-cosine (RRC) filter on the acquired offset channel before measuring the offset channel power. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_ACP_OFFSET_RRC_FILTER_ENABLED_FALSE0 (0x0)The channel power of the acquired offset channel is measured directly.RFMXSPECAN_VAL_ACP_OFFSET_RRC_FILTER_ENABLED_TRUE1 (0x1)The measurement applies the RRC filter on the acquired offset channel before measuring the offset channel power. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_ACP_OFFSET_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | The channel power of the acquired offset channel is measured directly. |  |
| RFMXSPECAN_VAL_ACP_OFFSET_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | The measurement applies the RRC filter on the acquired offset channel before measuring the offset channel power. |  |
| rrcAlpha | [in] | float64[] | This parameter specifies an array of roll-off factors of the root-raised-cosine (RRC) filter to apply on the acquired offset channel before measuring the offset channel power. The default value is 0.1. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__im_1ga64a48cf7ab6fae97a00ef689b60a2405.html language=enus -->
## TOPIC 00398: RFmxSpecAn_IMCfgFFT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__im_1ga64a48cf7ab6fae97a00ef689b60a2405.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__im_1ga64a48cf7ab6fae97a00ef689b60a2405.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the window and FFT to obtain a spectrum for the IM measurement. Syntaxint32 __stdcall RFmxSpecAn_IMCfgFFT(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindow, float64 fftPadding)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxSpecAn_IMCfgFFT

Configures the window and FFT to obtain a spectrum for the IM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IMCfgFFT(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindow, float64 fftPadding)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| fftWindow | [in] | int32 | This parameter specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectral Measurements Concepts topic for more information about FFT window types. The default value is Flat Top.NameValueDescriptionRFMXSPECAN_VAL_IM_FFT_WINDOW_NONE0 (0x0)Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes.RFMXSPECAN_VAL_IM_FFT_WINDOW_FLAT_TOP1 (0x1)Measures single-tone amplitudes accurately.RFMXSPECAN_VAL_IM_FFT_WINDOW_HANNING2 (0x2)Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements.RFMXSPECAN_VAL_IM_FFT_WINDOW_HAMMING3 (0x3)Analyzes closely-spaced sine waves.RFMXSPECAN_VAL_IM_FFT_WINDOW_GAUSSIAN4 (0x4)Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis.RFMXSPECAN_VAL_IM_FFT_WINDOW_BLACKMAN5 (0x5)Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate.RFMXSPECAN_VAL_IM_FFT_WINDOW_BLACKMAN_HARRIS6 (0x6)Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe.RFMXSPECAN_VAL_IM_FFT_WINDOW_KAISER_BESSEL7 (0x7)Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_NONE | 0 (0x0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_FLAT_TOP | 1 (0x1) | Measures single-tone amplitudes accurately. |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_HANNING | 2 (0x2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_HAMMING | 3 (0x3) | Analyzes closely-spaced sine waves. |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_GAUSSIAN | 4 (0x4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_BLACKMAN | 5 (0x5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_BLACKMAN_HARRIS | 6 (0x6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |  |
| RFMXSPECAN_VAL_IM_FFT_WINDOW_KAISER_BESSEL | 7 (0x7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |  |
| fftPadding | [in] | float64 | This parameter specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth. The default value is -1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__im_1ga6ed10d5ce1c4816f7309418c408fc0e6.html language=enus -->
## TOPIC 00399: RFmxSpecAn_IMCfgMeasurementMethod

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__im_1ga6ed10d5ce1c4816f7309418c408fc0e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__im_1ga6ed10d5ce1c4816f7309418c408fc0e6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the IM measurement. Syntaxint32 __stdcall RFmxSpecAn_IMCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxSpecAn_IMCfgMeasurementMethod

Configures the method for performing the IM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IMCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method for performing the IM measurement. The default value is Normal.NameValueDescriptionRFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_NORMAL0 (0x0)The IM measurement acquires the spectrum using the same signal analyzer settings across frequency bands. Use this method when the fundamental tone separation is not large. Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668.RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_DYNAMIC_RANGE1 (0x1)The IM measurement acquires a segmented spectrum using the signal analyzer specific optimizations for different frequency bands. The spectrum is acquired in segments, one per tone or intermod frequency to be measured. The span of each acquired spectral segment is equal to the frequency separation between the two input tones, or 1 MHz, whichever is smaller. Use this method to configure the IM measurement and the signal analyzer for maximum dynamic range instead of measurement speed.Supported devices: PXIe-5665/5668.RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_SEGMENTED2 (0x2)Similar to the Dynamic Range method, this method also acquires a segmented spectrum, except that signal analyzer is not explicitly configured to provide maximum dynamic range. Use this method when the frequency separation of the two input tones is large and the measurement accuracy can be traded off for measurement speed.Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The IM measurement acquires the spectrum using the same signal analyzer settings across frequency bands. Use this method when the fundamental tone separation is not large. Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668. |  |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_DYNAMIC_RANGE | 1 (0x1) | The IM measurement acquires a segmented spectrum using the signal analyzer specific optimizations for different frequency bands. The spectrum is acquired in segments, one per tone or intermod frequency to be measured. The span of each acquired spectral segment is equal to the frequency separation between the two input tones, or 1 MHz, whichever is smaller. Use this method to configure the IM measurement and the signal analyzer for maximum dynamic range instead of measurement speed.Supported devices: PXIe-5665/5668. |  |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_SEGMENTED | 2 (0x2) | Similar to the Dynamic Range method, this method also acquires a segmented spectrum, except that signal analyzer is not explicitly configured to provide maximum dynamic range. Use this method when the frequency separation of the two input tones is large and the measurement accuracy can be traded off for measurement speed.Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__im_1gaa9860b174ddb1cca280365c712fd521a.html language=enus -->
## TOPIC 00400: RFmxSpecAn_IMCfgAutoIntermodsSetup

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__im_1gaa9860b174ddb1cca280365c712fd521a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__im_1gaa9860b174ddb1cca280365c712fd521a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the measurement computes the intermod frequencies or uses manually specified frequencies. Syntaxint32 __stdcall RFmxSpecAn_IMCfgAutoIntermodsSetup(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoIntermodsSetupEnabled, int32 maximumIntermodOrder)ParametersNameD

### RFmxSpecAn_IMCfgAutoIntermodsSetup

Configures whether the measurement computes the intermod frequencies or uses manually specified frequencies.

#### Syntax

int32 __stdcall RFmxSpecAn_IMCfgAutoIntermodsSetup(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 autoIntermodsSetupEnabled, int32 maximumIntermodOrder)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| autoIntermodsSetupEnabled | [in] | int32 | This parameter specifies whether the measurement computes the intermod frequencies or uses manually specified frequencies. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_FALSE0 (0x0)The measurement uses the values that you specify for the RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY and RFMXSPECAN_ATTR_IM_UPPER_INTERMOD_FREQUENCY attributes.RFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_TRUE1 (0x1)The measurement computes the intermod frequencies. The maximum number of intermods that you can measure is based on the value of the RFMXSPECAN_ATTR_IM_MAXIMUM_INTERMOD_ORDER attribute. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_FALSE | 0 (0x0) | The measurement uses the values that you specify for the RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY and RFMXSPECAN_ATTR_IM_UPPER_INTERMOD_FREQUENCY attributes. |  |
| RFMXSPECAN_VAL_IM_AUTO_INTERMODS_SETUP_ENABLED_TRUE | 1 (0x1) | The measurement computes the intermod frequencies. The maximum number of intermods that you can measure is based on the value of the RFMXSPECAN_ATTR_IM_MAXIMUM_INTERMOD_ORDER attribute. |  |
| maximumIntermodOrder | [in] | int32 | This parameter specifies the order up to which the RFmx driver measures odd order intermodulation products when you set the Auto Intermods Setup Enabled parameter to True. The lower and upper intermodulation products are measured for each order. The default value is 3.Name (Value)Description3 (3)The RFmx driver measures third order intermodulation products.5 (5)The RFmx driver measures third and fifth order intermodulation products.7 (7)The RFmx driver measures third, fifth, and seventh order intermodulation products.9 (9)The RFmx driver measures third, fifth, seventh, and ninth order intermodulation products. |
| Name (Value) | Description |  |  |
| 3 (3) | The RFmx driver measures third order intermodulation products. |  |  |
| 5 (5) | The RFmx driver measures third and fifth order intermodulation products. |  |  |
| 7 (7) | The RFmx driver measures third, fifth, and seventh order intermodulation products. |  |  |
| 9 (9) | The RFmx driver measures third, fifth, seventh, and ninth order intermodulation products. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__im_1gab43432cf4fbe23d7755775ceb82fc2fe.html language=enus -->
## TOPIC 00401: RFmxSpecAn_IMCfgIntermod

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__im_1gab43432cf4fbe23d7755775ceb82fc2fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__im_1gab43432cf4fbe23d7755775ceb82fc2fe.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the intermod order, intermod side, lower intermod frequency, and upper intermod frequency when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to False. Syntaxint32 __stdcall RFmxSpecAn_IMCfgIntermod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 in

### RFmxSpecAn_IMCfgIntermod

Configures the intermod order, intermod side, lower intermod frequency, and upper intermod frequency when you set the [RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED](group____root__ni_r_fmx_spec_an__attributes__im_1gae977834382c65591476900915ad7ca4d.html) attribute to **False**.

#### Syntax

int32 __stdcall RFmxSpecAn_IMCfgIntermod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 intermodOrder, float64 lowerIntermodFrequency, float64 upperIntermodFrequency, int32 intermodSide, int32 intermodEnabled)

#### Remarks

Use "intermod<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and intermod number. If you do not specify the signal name, the default signal instance is used. The default value is "intermod0".Example:"intermod0""signal::sig1/intermod0"You can use the RFmxSpecAn_BuildIntermodString function to build the selector string. |
| intermodOrder | [in] | int32 | This parameter specifies the order of the intermod. The default value is 3. |
| lowerIntermodFrequency | [in] | float64 | This parameter specifies the frequency of the lower intermodulation product. This value is expressed in Hz. The default value is -3 MHz. |
| upperIntermodFrequency | [in] | float64 | This parameter specifies the frequency of the upper intermodulation product. This value is expressed in Hz. The default value is 3 MHz. |
| intermodSide | [in] | int32 | This parameter specifies whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. The default value is Both.NameValueDescriptionRFMXSPECAN_VAL_IM_INTERMOD_SIDE_LOWER0 (0x0)Measures the intermodulation product corresponding to the RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY attribute.RFMXSPECAN_VAL_IM_INTERMOD_SIDE_UPPER1 (0x1)Measures the intermodulation product corresponding to the RFMXSPECAN_ATTR_IM_UPPER_INTERMOD_FREQUENCY attribute.RFMXSPECAN_VAL_IM_INTERMOD_SIDE_BOTH2 (0x2)Measures the intermodulation product corresponding to both IM Lower Intermod Freq and IM Upper Intermod Freq attributes. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_IM_INTERMOD_SIDE_LOWER | 0 (0x0) | Measures the intermodulation product corresponding to the RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY attribute. |  |
| RFMXSPECAN_VAL_IM_INTERMOD_SIDE_UPPER | 1 (0x1) | Measures the intermodulation product corresponding to the RFMXSPECAN_ATTR_IM_UPPER_INTERMOD_FREQUENCY attribute. |  |
| RFMXSPECAN_VAL_IM_INTERMOD_SIDE_BOTH | 2 (0x2) | Measures the intermodulation product corresponding to both IM Lower Intermod Freq and IM Upper Intermod Freq attributes. |  |
| intermodEnabled | [in] | int32 | This parameter specifies whether to enable an intermod for the IM measurement. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_IM_INTERMOD_ENABLED_FALSE0 (0x0)Disables an intermod for the IM measurement. The results for the disabled intermods are displayed as NaN.RFMXSPECAN_VAL_IM_INTERMOD_ENABLED_TRUE1 (0x1)Enables an intermod for the IM measurement. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_IM_INTERMOD_ENABLED_FALSE | 0 (0x0) | Disables an intermod for the IM measurement. The results for the disabled intermods are displayed as NaN. |  |
| RFMXSPECAN_VAL_IM_INTERMOD_ENABLED_TRUE | 1 (0x1) | Enables an intermod for the IM measurement. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__iq.html language=enus -->
## TOPIC 00402: IQ

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__iq.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__iq.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_IQCfgAcquisitionConfigures the acquisition settings for the I/Q measurement. RFmxSpecAn_IQCfgBandwidthConfigures the bandwidth for the I/Q measurement. AttachmentsNone

### IQ

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_IQCfgAcquisition | Configures the acquisition settings for the I/Q measurement. |
| RFmxSpecAn_IQCfgBandwidth | Configures the bandwidth for the I/Q measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__iq_1ga498efc735e28fd849ab73f297cbf1601.html language=enus -->
## TOPIC 00403: RFmxSpecAn_IQCfgBandwidth

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__iq_1ga498efc735e28fd849ab73f297cbf1601.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__iq_1ga498efc735e28fd849ab73f297cbf1601.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the bandwidth for the I/Q measurement. Syntaxint32 __stdcall RFmxSpecAn_IQCfgBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthAuto, float64 bandwidth)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxSpecAn_IQCfgBandwidth

Configures the bandwidth for the I/Q measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IQCfgBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthAuto, float64 bandwidth)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| bandwidthAuto | [in] | int32 | This parameter specifies whether the measurement computes the minimum acquisition bandwidth. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_FALSE0 (0x0)The measurement uses the value of the RFMXSPECAN_ATTR_IQ_BANDWIDTH attribute as the minimum acquisition bandwidth.RFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_TRUE1 (0x1)The measurement uses 0.8 * sample rate as the minimum signal bandwidth. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_FALSE | 0 (0x0) | The measurement uses the value of the RFMXSPECAN_ATTR_IQ_BANDWIDTH attribute as the minimum acquisition bandwidth. |  |
| RFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_TRUE | 1 (0x1) | The measurement uses 0.8 * sample rate as the minimum signal bandwidth. |  |
| bandwidth | [in] | float64 | This parameter specifies the minimum acquisition bandwidth, in Hz, when you set the Bandwidth Auto parameter to False. The default value is 1 MHz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__iq_1gaa6c5e67929425db63ae06a0bd6cf2590.html language=enus -->
## TOPIC 00404: RFmxSpecAn_IQCfgAcquisition

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__iq_1gaa6c5e67929425db63ae06a0bd6cf2590.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__iq_1gaa6c5e67929425db63ae06a0bd6cf2590.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the acquisition settings for the I/Q measurement. Syntaxint32 __stdcall RFmxSpecAn_IQCfgAcquisition(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 sampleRate, int32 numberOfRecords, float64 acquisitionTime, float64 pretriggerTime)ParametersNameDirectionTypeDescriptioni

### RFmxSpecAn_IQCfgAcquisition

Configures the acquisition settings for the I/Q measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_IQCfgAcquisition(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 sampleRate, int32 numberOfRecords, float64 acquisitionTime, float64 pretriggerTime)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| sampleRate | [in] | float64 | This parameter specifies the acquisition sample rate, in samples per second (S/s). The default value is 50 MS/s. |
| numberOfRecords | [in] | int32 | This parameter specifies the number of records to acquire. The default value is 1. |
| acquisitionTime | [in] | float64 | This parameter specifies the acquisition time, in seconds, for the I/Q measurement. The default value is 0.001. |
| pretriggerTime | [in] | float64 | This parameter specifies the pretrigger time, in seconds, for the I/Q measurement. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf.html language=enus -->
## TOPIC 00405: NF

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsFrequency ListLossGroup membersNameDescriptionRFmxSpecAn_NFCfgAveragingConfigures averaging for the noise figure (NF) measurement. RFmxSpecAn_NFCfgColdSourceDUTSParametersConfigures the scattering parameters of the DUT as a function of the frequency, for use in the cold source measurement meth

### NF

#### Groups

- Frequency List
- Loss

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_NFCfgAveraging | Configures averaging for the noise figure (NF) measurement. |
| RFmxSpecAn_NFCfgColdSourceDUTSParameters | Configures the scattering parameters of the DUT as a function of the frequency, for use in the cold source measurement method. |
| RFmxSpecAn_NFCfgColdSourceInputTermination | Configures the characteristics of the microwave termination used as a noise source in the cold source method. |
| RFmxSpecAn_NFCfgColdSourceMode | Configures the cold source based noise figure (NF) measurement to perform the calibration step or the measurement step. |
| RFmxSpecAn_NFCfgMeasurementBandwidth | Configures the effective noise-bandwidth in which power measurements are performed in the noise figure (NF) measurement. |
| RFmxSpecAn_NFCfgMeasurementInterval | Configures the duration for which the signals are acquired at each frequency to perform the noise figure (NF) measurement. |
| RFmxSpecAn_NFCfgMeasurementMethod | Configures the noise figure (NF) measurement to use either the Y-factor or the cold source method. |
| RFmxSpecAn_NFCfgYFactorMode | Configures the Y-Factor based noise figure (NF) measurement to perform the calibration step or the measurement step. |
| RFmxSpecAn_NFCfgYFactorNoiseSourceENR | Configures excess noise ratio (ENR) and temperature of the noise source used by the Y-factor method. |
| RFmxSpecAn_NFCfgYFactorNoiseSourceLoss | Configures the ohmic loss inherent to the noise source used in the Y-Factor method that is common to the calibration and the measurement steps. |
| RFmxSpecAn_NFCfgYFactorNoiseSourceSettlingTime | Configures the time required for the acquisition to wait till the noise source used in the Y-Factor method settles to hot or cold state when the noise source is powered on or off. |
| RFmxSpecAn_NFClearCalibrationDatabase | Clear the noise figure calibration data for Cold Source and Y-Factor method. Calibration data associated with the selected VSA is cleared for the Cold Source method while calibration data associated with the noise source name and the VSA is cleared for the Y-Factor method. |
| RFmxSpecAn_NFLoadCalibrationLossFromS2p | Loads the ohmic loss data from an S2P file, as a function of frequency of the loss elements between the noise source and the input port of the analyzer during the calibration step, excluding the loss specified as the noise source loss. |
| RFmxSpecAn_NFLoadColdSourceDUTSParametersFromS2p | Loads the scattering parameter data from an S2P file and configures them as a function of frequency for use in the cold source measurement method. |
| RFmxSpecAn_NFLoadColdSourceInputTerminationFromS1p | Loads the characteristics of the microwave termination from an S1P file, which used as a noise source in the cold source method. |
| RFmxSpecAn_NFLoadDUTInputLossFromS2p | Loads the ohmic Input loss data from an S2P file and configures the loss elements between the noise source and the input port of DUT, excluding the losses that are common to the calibration step and the measurement step. |
| RFmxSpecAn_NFLoadDUTOutputLossFromS2p | Loads the ohmic Output loss data from an S2P file and configures the loss elements between the output port of the DUT and the input port of the analyzer. |
| RFmxSpecAn_NFLoadExternalPreampGainFromS2p | Loads the gain characteristics of the external preamplifier from an S2P file, as a function of frequency. The gain values are expressed in dB. |
| RFmxSpecAn_NFLoadYFactorNoiseSourceLossFromS2p | Loads the ohmic loss from an S2P file, which is inherent to the noise source used in the Y-Factor method that is common to the calibration and the measurement steps. |
| RFmxSpecAn_NFRecommendReferenceLevel | Computes and sets an appropriate reference level based on the expected maximum DUT gain, maximum DUT noise figure, and other measurement and analyzer attributes. You must not set RFMXINSTR_ATTR_MIXER_LEVEL, RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET, RFMXINSTR_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET, and RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH attributes in order to obtain an appropriate recommended reference level. |
| RFmxSpecAn_NFValidateCalibrationData | Indicates whether the calibration data is valid for the configuration specified by the signal name in the Selector string parameter. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga123c3528ba6f58d5ead49552da537049.html language=enus -->
## TOPIC 00406: RFmxSpecAn_NFLoadColdSourceInputTerminationFromS1p

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga123c3528ba6f58d5ead49552da537049.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga123c3528ba6f58d5ead49552da537049.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the characteristics of the microwave termination from an S1P file, which used as a noise source in the cold source method. Syntaxint32 __stdcall RFmxSpecAn_NFLoadColdSourceInputTerminationFromS1p(niRFmxInstrHandle instrumentHandle, char selectorString[], char terminationS1PFilePath[], float64

### RFmxSpecAn_NFLoadColdSourceInputTerminationFromS1p

Loads the characteristics of the microwave termination from an S1P file, which used as a noise source in the cold source method.

#### Syntax

int32 __stdcall RFmxSpecAn_NFLoadColdSourceInputTerminationFromS1p(niRFmxInstrHandle instrumentHandle, char selectorString[], char terminationS1PFilePath[], float64 terminationTemperature)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| terminationS1PFilePath | [in] | char[] | This parameterspecifies the path to the S1P file that contains DUT S-Parameters for the specified port. |
| terminationTemperature | [in] | float64 | This parameter specifies the physical temperature of the microwave termination used as the noise source in the cold source method. This value is expressed in kelvin. The default value is 297. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga2149d01ec9c443c2fbada2f0ec662b9a.html language=enus -->
## TOPIC 00407: RFmxSpecAn_NFCfgMeasurementMethod

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga2149d01ec9c443c2fbada2f0ec662b9a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga2149d01ec9c443c2fbada2f0ec662b9a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the noise figure (NF) measurement to use either the Y-factor or the cold source method. Syntaxint32 __stdcall RFmxSpecAn_NFCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRF

### RFmxSpecAn_NFCfgMeasurementMethod

Configures the noise figure (NF) measurement to use either the Y-factor or the cold source method.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the measurement method used to perform the NF measurement. Refer to the NF concept topic for more information. The default value is Y-Factor.NameValueDescriptionRFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_Y_FACTOR0 (0x0)The NF measurement computes the noise figure of the DUT using a noise source with a calibrated excess-noise ratio (ENR). Refer to the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE attribute for information about supported devices and their corresponding noise source type.RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_COLD_SOURCE1 (0x1)The NF measurement computes the noise figure of the DUT using a 50 ohm microwave termination as the noise source.Supported Devices: PXIe-5644/5645/5646/5840/5841/5842/5860, PXIe-5830/5831/5832 |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_Y_FACTOR | 0 (0x0) | The NF measurement computes the noise figure of the DUT using a noise source with a calibrated excess-noise ratio (ENR). Refer to the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE attribute for information about supported devices and their corresponding noise source type. |  |
| RFMXSPECAN_VAL_NF_MEASUREMENT_METHOD_COLD_SOURCE | 1 (0x1) | The NF measurement computes the noise figure of the DUT using a 50 ohm microwave termination as the noise source.Supported Devices: PXIe-5644/5645/5646/5840/5841/5842/5860, PXIe-5830/5831/5832 |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga2892729cf9bff588888f15016086cdb5.html language=enus -->
## TOPIC 00408: RFmxSpecAn_NFLoadDUTInputLossFromS2p

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga2892729cf9bff588888f15016086cdb5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga2892729cf9bff588888f15016086cdb5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the ohmic Input loss data from an S2P file and configures the loss elements between the noise source and the input port of DUT, excluding the losses that are common to the calibration step and the measurement step. Syntaxint32 __stdcall RFmxSpecAn_NFLoadDUTInputLossFromS2p(niRFmxInstrHandle in

### RFmxSpecAn_NFLoadDUTInputLossFromS2p

Loads the ohmic Input loss data from an S2P file and configures the loss elements between the noise source and the input port of DUT, excluding the losses that are common to the calibration step and the measurement step.

#### Syntax

int32 __stdcall RFmxSpecAn_NFLoadDUTInputLossFromS2p(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 dutInputLossCompensationEnabled, char dutInputLossS2PFilePath[], int32 dutInputLossSParameterOrientation, float64 dutInputLossTemperature)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| dutInputLossCompensationEnabled | [in] | int32 | This parameter specifies whether the noise figure (NF) measurement accounts for ohmic losses between the noise source and the input port of the DUT, excluding the losses that are common to calibration and the measurement steps, which are specified by the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED_FALSE0 (0x0)The NF measurement ignores the ohmic losses.RFMXSPECAN_VAL_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED_TRUE1 (0x1)The NF measurement accounts for the ohmic losses. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED_FALSE | 0 (0x0) | The NF measurement ignores the ohmic losses. |  |
| RFMXSPECAN_VAL_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED_TRUE | 1 (0x1) | The NF measurement accounts for the ohmic losses. |  |
| dutInputLossS2PFilePath | [in] | char[] | This parameterspecifies the path to the S2P file that contains DUT Input Loss for the specified port. |
| dutInputLossSParameterOrientation | [in] | int32 | This parameter specifies the orientation of the data in the S-parameter table relative to the port you specify. The default value is Port1 Towards DUT.Name (Value)DescriptionPort1 Towards DUT (0)Port 1 of the S2P is oriented towards the DUT.Port2 Towards DUT (1)Port 2 of the S2P is oriented towards the DUT. |
| Name (Value) | Description |  |  |
| Port1 Towards DUT (0) | Port 1 of the S2P is oriented towards the DUT. |  |  |
| Port2 Towards DUT (1) | Port 2 of the S2P is oriented towards the DUT. |  |  |
| dutInputLossTemperature | [in] | float64 | This parameter specifies the physical temperature of the ohmic loss elements considered in the DUT Input Loss parameter. This value is expressed in kelvin. The default value is 297. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga3e862e4f65dbdbb1d37d3b7f49b18819.html language=enus -->
## TOPIC 00409: RFmxSpecAn_NFCfgYFactorMode

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga3e862e4f65dbdbb1d37d3b7f49b18819.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga3e862e4f65dbdbb1d37d3b7f49b18819.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Y-Factor based noise figure (NF) measurement to perform the calibration step or the measurement step. Syntaxint32 __stdcall RFmxSpecAn_NFCfgYFactorMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 yFactorMode)ParametersNameDirectionTypeDescriptioninstrumentHandle[i

### RFmxSpecAn_NFCfgYFactorMode

Configures the Y-Factor based noise figure (NF) measurement to perform the calibration step or the measurement step.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgYFactorMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 yFactorMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| yFactorMode | [in] | int32 | This parameter specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor.NameValueDescriptionRFMXSPECAN_VAL_NF_Y_FACTOR_MODE_MEASURE0 (0x0)The noise figure (NF) measurement computes the noise characteristics of the DUT, compensating for the noise figure of the analyzer.RFMXSPECAN_VAL_NF_Y_FACTOR_MODE_CALIBRATE1 (0x1)The NF measurement computes the noise characteristics of the analyzer. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_NF_Y_FACTOR_MODE_MEASURE | 0 (0x0) | The noise figure (NF) measurement computes the noise characteristics of the DUT, compensating for the noise figure of the analyzer. |  |
| RFMXSPECAN_VAL_NF_Y_FACTOR_MODE_CALIBRATE | 1 (0x1) | The NF measurement computes the noise characteristics of the analyzer. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga654e28d70038474a1303950f7522c5cd.html language=enus -->
## TOPIC 00410: RFmxSpecAn_NFCfgMeasurementBandwidth

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga654e28d70038474a1303950f7522c5cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga654e28d70038474a1303950f7522c5cd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the effective noise-bandwidth in which power measurements are performed in the noise figure (NF) measurement. Syntaxint32 __stdcall RFmxSpecAn_NFCfgMeasurementBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementBandwidth)ParametersNameDirectionTypeDescr

### RFmxSpecAn_NFCfgMeasurementBandwidth

Configures the effective noise-bandwidth in which power measurements are performed in the noise figure (NF) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgMeasurementBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementBandwidth)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementBandwidth | [in] | float64 | This parameter specifies the effective noise-bandwidth in which power measurements are performed for the NF measurement. This value is expressed in Hz. The default value is 100 kHz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga679364e106ab734af30f02ac88e1a656.html language=enus -->
## TOPIC 00411: RFmxSpecAn_NFCfgYFactorNoiseSourceLoss

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga679364e106ab734af30f02ac88e1a656.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga679364e106ab734af30f02ac88e1a656.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the ohmic loss inherent to the noise source used in the Y-Factor method that is common to the calibration and the measurement steps. Syntaxint32 __stdcall RFmxSpecAn_NFCfgYFactorNoiseSourceLoss(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseSourceLossCompensationEna

### RFmxSpecAn_NFCfgYFactorNoiseSourceLoss

Configures the ohmic loss inherent to the noise source used in the Y-Factor method that is common to the calibration and the measurement steps.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgYFactorNoiseSourceLoss(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseSourceLossCompensationEnabled, float64 noiseSourceLossFrequency[], float64 noiseSourceLoss[], float64 noiseSourceLossTemperature, int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| noiseSourceLossCompensationEnabled | [in] | int32 | This parameter specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED_FALSE0 (0x0)Ohmic losses are ignored.RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED_TRUE1 (0x1)Ohmic losses are accounted for in the NF measurement. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Ohmic losses are ignored. |  |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Ohmic losses are accounted for in the NF measurement. |  |
| noiseSourceLossFrequency | [in] | float64[] | This parameter specifies the array of the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the Noise Source Loss parameter. This value is expressed in Hz. The default value is an empty array. |
| noiseSourceLoss | [in] | float64[] | This parameter specifies an array of the ohmic losses inherent to the noise source used in the Y-Factor method. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the Noise Source Loss Compensation Enabled parameter to True. The default value is an empty array.You must specify the frequencies at which the losses were measured using the Noise Source Loss Frequency parameter. |
| noiseSourceLossTemperature | [in] | float64 | This parameter specifies the physical temperature of the ohmic loss elements specified in the Noise Source Loss parameter. This value is expressed in kelvin. The default value is 297. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga6a6f81154b0741bd050f54ad40efaea3.html language=enus -->
## TOPIC 00412: RFmxSpecAn_NFRecommendReferenceLevel

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga6a6f81154b0741bd050f54ad40efaea3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga6a6f81154b0741bd050f54ad40efaea3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes and sets an appropriate reference level based on the expected maximum DUT gain, maximum DUT noise figure, and other measurement and analyzer attributes. You must not set RFMXINSTR_ATTR_MIXER_LEVEL, RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET, RFMXINSTR_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET, and RFMXINSTR

### RFmxSpecAn_NFRecommendReferenceLevel

Computes and sets an appropriate reference level based on the expected maximum DUT gain, maximum DUT noise figure, and other measurement and analyzer attributes. You must not set [RFMXINSTR_ATTR_MIXER_LEVEL](/csh?context=rfmxinstr_rfmxinstrcref_attribute_mixer_level), [RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET](/csh?context=rfmxinstr_rfmxinstrcref_attribute_mixer_level_offset), [RFMXINSTR_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET](/csh?context=rfmxinstr_rfmxinstrcref_attribute_if_output_power_level_offset), and [RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH](/csh?context=rfmxinstr_rfmxinstrcref_attribute_if_filter_bandwidth) attributes in order to obtain an appropriate recommended reference level.

#### Syntax

int32 __stdcall RFmxSpecAn_NFRecommendReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 dutMaxGain, float64 dutMaxNoiseFigure, float64 *referenceLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| dutMaxGain | [in] | float64 | This parameter returns the expected maximum gain from the DUT. This value is expressed in dB. |
| dutMaxNoiseFigure | [in] | float64 | This parameter returns the expected maximum noise figure of the DUT. This value is expressed in dB. |
| referenceLevel | [out] | float64 * | This parameter returns the recommended reference level for the NF measurement. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga778df14189f7f2db9da6f127bd3271d3.html language=enus -->
## TOPIC 00413: RFmxSpecAn_NFLoadExternalPreampGainFromS2p

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga778df14189f7f2db9da6f127bd3271d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga778df14189f7f2db9da6f127bd3271d3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the gain characteristics of the external preamplifier from an S2P file, as a function of frequency. The gain values are expressed in dB. Syntaxint32 __stdcall RFmxSpecAn_NFLoadExternalPreampGainFromS2p(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 externalPreampPresent, char

### RFmxSpecAn_NFLoadExternalPreampGainFromS2p

Loads the gain characteristics of the external preamplifier from an S2P file, as a function of frequency. The gain values are expressed in dB.

#### Syntax

int32 __stdcall RFmxSpecAn_NFLoadExternalPreampGainFromS2p(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 externalPreampPresent, char externalPreampGainS2PFilePath[], int32 externalPreampGainSParameterOrientation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| externalPreampPresent | [in] | int32 | This parameterSpecifies if an external preamplifier is present in the signal path.NameValueDescriptionRFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_FALSE0 (0x0)No external preamplifier present in the signal path.RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_TRUE1 (0x1)An external preamplifier present in the signal path. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_FALSE | 0 (0x0) | No external preamplifier present in the signal path. |  |
| RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_TRUE | 1 (0x1) | An external preamplifier present in the signal path. |  |
| externalPreampGainS2PFilePath | [in] | char[] | This parameterspecifies the path to the S2P file that contains DUT S-Parameters for the specified port. |
| externalPreampGainSParameterOrientation | [in] | int32 | This parameterspecifies the orientation of the data in the S-parameter table relative to the port you specify. The default value is Port1 Towards DUT.Name (Value)DescriptionPort1 Towards DUT (0)Port 1 of the S2P is oriented towards the DUT.Port2 Towards DUT (1)Port 2 of the S2P is oriented towards the DUT. |
| Name (Value) | Description |  |  |
| Port1 Towards DUT (0) | Port 1 of the S2P is oriented towards the DUT. |  |  |
| Port2 Towards DUT (1) | Port 2 of the S2P is oriented towards the DUT. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga785f03670ff82227e4b4cdb01e5857d5.html language=enus -->
## TOPIC 00414: RFmxSpecAn_NFCfgYFactorNoiseSourceSettlingTime

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga785f03670ff82227e4b4cdb01e5857d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga785f03670ff82227e4b4cdb01e5857d5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the time required for the acquisition to wait till the noise source used in the Y-Factor method settles to hot or cold state when the noise source is powered on or off. Syntaxint32 __stdcall RFmxSpecAn_NFCfgYFactorNoiseSourceSettlingTime(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxSpecAn_NFCfgYFactorNoiseSourceSettlingTime

Configures the time required for the acquisition to wait till the noise source used in the Y-Factor method settles to hot or cold state when the noise source is powered on or off.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgYFactorNoiseSourceSettlingTime(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 settlingTime)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| settlingTime | [in] | float64 | This parameter specifies the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is enabled or disabled. This attribute is used only when you set the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE attribute to External Noise Source. This value is expressed in seconds. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga8100c0d9cbda4970848e0edccad9a079.html language=enus -->
## TOPIC 00415: RFmxSpecAn_NFCfgMeasurementInterval

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga8100c0d9cbda4970848e0edccad9a079.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga8100c0d9cbda4970848e0edccad9a079.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the duration for which the signals are acquired at each frequency to perform the noise figure (NF) measurement. Syntaxint32 __stdcall RFmxSpecAn_NFCfgMeasurementInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval)ParametersNameDirectionTypeDescr

### RFmxSpecAn_NFCfgMeasurementInterval

Configures the duration for which the signals are acquired at each frequency to perform the noise figure (NF) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgMeasurementInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementInterval | [in] | float64 | This parameter specifies the duration for which signals are acquired at each frequency which you specify in the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in seconds. The default value is 1 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga8d515b1c927188b52dd2a31d23ac31f1.html language=enus -->
## TOPIC 00416: RFmxSpecAn_NFClearCalibrationDatabase

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga8d515b1c927188b52dd2a31d23ac31f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1ga8d515b1c927188b52dd2a31d23ac31f1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clear the noise figure calibration data for Cold Source and Y-Factor method. Calibration data associated with the selected VSA is cleared for the Cold Source method while calibration data associated with the noise source name and the VSA is cleared for the Y-Factor method. Syntaxint32 __stdcall RFmx

### RFmxSpecAn_NFClearCalibrationDatabase

Clear the noise figure calibration data for Cold Source and Y-Factor method. Calibration data associated with the selected VSA is cleared for the Cold Source method while calibration data associated with the noise source name and the VSA is cleared for the Y-Factor method.

#### Syntax

int32 __stdcall RFmxSpecAn_NFClearCalibrationDatabase(niRFmxInstrHandle instrumentHandle, char calibrationSetupId[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| calibrationSetupId | [in] | char[] | This parameter associates a unique string identifier with the hardware setup used to perform calibration for the NF measurement. The default value is an empty string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gab6d64c90137f1ae46fdd26ad2be8915e.html language=enus -->
## TOPIC 00417: RFmxSpecAn_NFCfgColdSourceDUTSParameters

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gab6d64c90137f1ae46fdd26ad2be8915e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gab6d64c90137f1ae46fdd26ad2be8915e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the scattering parameters of the DUT as a function of the frequency, for use in the cold source measurement method. Syntaxint32 __stdcall RFmxSpecAn_NFCfgColdSourceDUTSParameters(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 dutSParametersFrequency[], float64 dutS21[]

### RFmxSpecAn_NFCfgColdSourceDUTSParameters

Configures the scattering parameters of the DUT as a function of the frequency, for use in the cold source measurement method.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgColdSourceDUTSParameters(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 dutSParametersFrequency[], float64 dutS21[], float64 dutS12[], float64 dutS11[], float64 dutS22[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| dutSParametersFrequency | [in] | float64[] | This parameter specifies the array of frequencies corresponding to the s-parameters of the DUT specified by the DUT S21, DUT S12, DUT S11, and DUT S22 parameters. This value is expressed in Hz. The default value is an empty array. |
| dutS21 | [in] | float64[] | This parameter specifies an array of the gains of the DUT as a function of frequency, when the output port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUT S-Parameters Frequency parameter. The default value is an empty array. |
| dutS12 | [in] | float64[] | This parameter specifies an array of the input-isolations of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUT S-Parameters Frequency parameter. The default value is an empty array. |
| dutS11 | [in] | float64[] | This parameter specifies an array of the input-reflections of the DUT as a function of frequency, when the output port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUT S-Parameters Frequency parameter. The default value is an empty array. |
| dutS22 | [in] | float64[] | This parameter specifies an array of the output-reflections of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the DUT S-Parameters Frequency parameter. The default value is an empty array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gac2dbdbd93e37030b03ce1777569852b0.html language=enus -->
## TOPIC 00418: RFmxSpecAn_NFValidateCalibrationData

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gac2dbdbd93e37030b03ce1777569852b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gac2dbdbd93e37030b03ce1777569852b0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the calibration data is valid for the configuration specified by the signal name in the Selector string parameter. Syntaxint32 __stdcall RFmxSpecAn_NFValidateCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *calibrationDataValid)ParametersNameDirecti

### RFmxSpecAn_NFValidateCalibrationData

Indicates whether the calibration data is valid for the configuration specified by the signal name in the **Selector string** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_NFValidateCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *calibrationDataValid)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| calibrationDataValid | [out] | int32 * | This parameter returns whether the calibration data is valid.Name (Value)DescriptionFalse (0)Returns false if the calibration data is not present for one or more frequency points in the list or if the difference between the current device temperature and the calibration temperature exceeds the tolerance specified by the NF Device Temperature Tolerance attribute.True (1)Returns true if the calibration data is present for all of the frequencies in the list. |
| Name (Value) | Description |  |  |
| False (0) | Returns false if the calibration data is not present for one or more frequency points in the list or if the difference between the current device temperature and the calibration temperature exceeds the tolerance specified by the NF Device Temperature Tolerance attribute. |  |  |
| True (1) | Returns true if the calibration data is present for all of the frequencies in the list. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gaf56f32dd44e5f5aee79a0db88cbcb431.html language=enus -->
## TOPIC 00419: RFmxSpecAn_NFCfgAveraging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gaf56f32dd44e5f5aee79a0db88cbcb431.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf_1gaf56f32dd44e5f5aee79a0db88cbcb431.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the noise figure (NF) measurement. Syntaxint32 __stdcall RFmxSpecAn_NFCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxSpecAn_NFCfgAveraging

Configures averaging for the noise figure (NF) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_NF_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_TRUE1 (0x1)The NF measurement uses the value of the RFMXSPECAN_ATTR_NF_AVERAGING_COUNT attribute as the number of acquisitions for each frequency which you specify in the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, over which the NF measurement is averaged. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_TRUE | 1 (0x1) | The NF measurement uses the value of the RFMXSPECAN_ATTR_NF_AVERAGING_COUNT attribute as the number of acquisitions for each frequency which you specify in the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, over which the NF measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__nf__loss_1ga739d770aa53ac98d481f5ca51262cff1.html language=enus -->
## TOPIC 00420: RFmxSpecAn_NFCfgDUTOutputLoss

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__nf__loss_1ga739d770aa53ac98d481f5ca51262cff1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__nf__loss_1ga739d770aa53ac98d481f5ca51262cff1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the ohmic loss, as a function of frequency, of the loss elements between the output port of the DUT and the input port of the analyzer. Syntaxint32 __stdcall RFmxSpecAn_NFCfgDUTOutputLoss(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 dutOutputLossCompensationEnabled, fl

### RFmxSpecAn_NFCfgDUTOutputLoss

Configures the ohmic loss, as a function of frequency, of the loss elements between the output port of the DUT and the input port of the analyzer.

#### Syntax

int32 __stdcall RFmxSpecAn_NFCfgDUTOutputLoss(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 dutOutputLossCompensationEnabled, float64 dutOutputLossFrequency[], float64 dutOutputLoss[], float64 dutOutputLossTemperature, int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| dutOutputLossCompensationEnabled | [in] | int32 | This parameter specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_FALSE0 (0x0)The NF measurement ignores ohmic losses.RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_TRUE1 (0x1)The NF measurement accounts for the ohmic losses. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_FALSE | 0 (0x0) | The NF measurement ignores ohmic losses. |  |
| RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_TRUE | 1 (0x1) | The NF measurement accounts for the ohmic losses. |  |
| dutOutputLossFrequency | [in] | float64[] | This parameter specifies the array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS attribute. This value is expressed in Hz. The default value is an empty array. |
| dutOutputLoss | [in] | float64[] | This parameter specifies the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the DUT Output Loss Compensation Enabled parameter to True. The default value is an empty array.Specify the array of frequencies at which the losses were measured using the DUT Output Loss Frequency parameter. |
| dutOutputLossTemperature | [in] | float64 | This parameter specifies the physical temperature of the ohmic loss elements specified by the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS attribute. This value is expressed in kelvin. The default value is 297. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Loss

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__obw.html language=enus -->
## TOPIC 00421: OBW

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__obw.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_OBWCfgAveragingConfigures averaging for the occupied bandwidth (OBW) measurement. RFmxSpecAn_OBWCfgBandwidthPercentageConfigures the percentage of the total power that is contained in the occupied bandwidth (OBW). RFmxSpecAn_OBWCfgFFTConfigures window

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_OBWCfgAveraging | Configures averaging for the occupied bandwidth (OBW) measurement. |
| RFmxSpecAn_OBWCfgBandwidthPercentage | Configures the percentage of the total power that is contained in the occupied bandwidth (OBW). |
| RFmxSpecAn_OBWCfgFFT | Configures window and FFT to obtain a spectrum for the occupied bandwidth (OBW) measurement. |
| RFmxSpecAn_OBWCfgPowerUnits | Configures the units for the absolute power. |
| RFmxSpecAn_OBWCfgRBWFilter | Configures the resolution bandwidth (RBW) filter. |
| RFmxSpecAn_OBWCfgSpan | Configures the frequency range, in Hz, around the center frequency, to acquire for the measurement. |
| RFmxSpecAn_OBWCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__obw_1ga335b16a6628ece2747d9e79f1f6efcda.html language=enus -->
## TOPIC 00422: RFmxSpecAn_OBWCfgAveraging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__obw_1ga335b16a6628ece2747d9e79f1f6efcda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__obw_1ga335b16a6628ece2747d9e79f1f6efcda.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the occupied bandwidth (OBW) measurement. Syntaxint32 __stdcall RFmxSpecAn_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]n

### RFmxSpecAn_OBWCfgAveraging

Configures averaging for the occupied bandwidth (OBW) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE1 (0x1)The OBW measurement uses the RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE | 1 (0x1) | The OBW measurement uses the RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectral Measurements Concepts topic for more information about averaging types. The default value is RMS.NameValueDescriptionRFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MAXIMUM3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MINIMUM4 (0x4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__obw_1ga395614852bd7b1af892554448f41bc07.html language=enus -->
## TOPIC 00423: RFmxSpecAn_OBWCfgRBWFilter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__obw_1ga395614852bd7b1af892554448f41bc07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__obw_1ga395614852bd7b1af892554448f41bc07.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. Syntaxint32 __stdcall RFmxSpecAn_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter spec

### RFmxSpecAn_OBWCfgRBWFilter

Configures the resolution bandwidth (RBW) filter.

#### Syntax

int32 __stdcall RFmxSpecAn_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Spectral Measurements Concepts topic for more details on RBW and sweep time. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_OBW_RBW_AUTO_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute.RFMXSPECAN_VAL_OBW_RBW_AUTO_TRUE1 (0x1)The measurement computes the RBW. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_OBW_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXSPECAN_VAL_OBW_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the response of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is performed.RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)The RBW filter has a Gaussian response.RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FLAT2 (0x2)The RBW filter has a flat response. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |  |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |  |
| RFMXSPECAN_VAL_OBW_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gaa08a6e173eac11ad19e5bf29357a3e79.html language=enus -->
## TOPIC 00424: RFmxSpecAn_OBWCfgBandwidthPercentage

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gaa08a6e173eac11ad19e5bf29357a3e79.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gaa08a6e173eac11ad19e5bf29357a3e79.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the percentage of the total power that is contained in the occupied bandwidth (OBW). Syntaxint32 __stdcall RFmxSpecAn_OBWCfgBandwidthPercentage(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 bandwidthPercentage)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]

### RFmxSpecAn_OBWCfgBandwidthPercentage

Configures the percentage of the total power that is contained in the occupied bandwidth (OBW).

#### Syntax

int32 __stdcall RFmxSpecAn_OBWCfgBandwidthPercentage(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 bandwidthPercentage)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| bandwidthPercentage | [in] | float64 | This parameter specifies the percentage of the total power that is contained in the OBW. The default value is 99%. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gaa751051718c7b838f290e01e624a08ba.html language=enus -->
## TOPIC 00425: RFmxSpecAn_OBWCfgSweepTime

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gaa751051718c7b838f290e01e624a08ba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gaa751051718c7b838f290e01e624a08ba.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxSpecAn_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxSpecAn_OBWCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxSpecAn_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_OBW_SWEEP_TIME_INTERVAL attribute.RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |  |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time, in seconds, when you set the Sweep Time Auto parameter to False. The default value is 1 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gafd20e65f12393a5633e093380185a0db.html language=enus -->
## TOPIC 00426: RFmxSpecAn_OBWCfgPowerUnits

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gafd20e65f12393a5633e093380185a0db.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__obw_1gafd20e65f12393a5633e093380185a0db.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the units for the absolute power. Syntaxint32 __stdcall RFmxSpecAn_OBWCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Inst

### RFmxSpecAn_OBWCfgPowerUnits

Configures the units for the absolute power.

#### Syntax

int32 __stdcall RFmxSpecAn_OBWCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| powerUnits | [in] | int32 | This parameter specifies the units for the absolute power. The default value is dBm.NameValueDescriptionRFMXSPECAN_VAL_OBW_POWER_UNITS_DBM0 (0x0)The absolute powers are reported in dBm.RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ1 (0x1)The absolute powers are reported in dBm/Hz. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM | 0 (0x0) | The absolute powers are reported in dBm. |  |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ | 1 (0x1) | The absolute powers are reported in dBm/Hz. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__pavt.html language=enus -->
## TOPIC 00427: PAVT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__pavt.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__pavt.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsArraySegment Start TimeGroup membersNameDescriptionRFmxSpecAn_PAVTCfgMeasurementBandwidthConfigures the measurement bandwidth. RFmxSpecAn_PAVTCfgMeasurementIntervalConfigures the measurement offset and measurement length for the segments. RFmxSpecAn_PAVTCfgMeasurementIntervalModeConfigures the

### PAVT

#### Groups

- Array
- Segment Start Time

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_PAVTCfgMeasurementBandwidth | Configures the measurement bandwidth. |
| RFmxSpecAn_PAVTCfgMeasurementInterval | Configures the measurement offset and measurement length for the segments. |
| RFmxSpecAn_PAVTCfgMeasurementIntervalMode | Configures the measurement interval mode. |
| RFmxSpecAn_PAVTCfgMeasurementLocationType | Configures the measurement location type for the segments. |
| RFmxSpecAn_PAVTCfgNumberOfSegments | Configures the number of segments. |
| RFmxSpecAn_PAVTCfgSegmentMeasurementInterval | Configures the segment measurement offset and length for the segments. |
| RFmxSpecAn_PAVTCfgSegmentType | Configures the segment type. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga12f26d95322c65ad8e2f3523e630546b.html language=enus -->
## TOPIC 00428: RFmxSpecAn_PAVTCfgMeasurementBandwidth

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga12f26d95322c65ad8e2f3523e630546b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga12f26d95322c65ad8e2f3523e630546b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement bandwidth. Syntaxint32 __stdcall RFmxSpecAn_PAVTCfgMeasurementBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementBandwidth)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx sess

### RFmxSpecAn_PAVTCfgMeasurementBandwidth

Configures the measurement bandwidth.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTCfgMeasurementBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementBandwidth)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementBandwidth | [in] | float64 | This parameter specifies the bandwidth over which the signal is measured. This value is expressed in Hz. The default value is 10 MHz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga319dd4482421b81511570ff0f0ffbb65.html language=enus -->
## TOPIC 00429: RFmxSpecAn_PAVTCfgSegmentType

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga319dd4482421b81511570ff0f0ffbb65.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga319dd4482421b81511570ff0f0ffbb65.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the segment type. Syntaxint32 __stdcall RFmxSpecAn_PAVTCfgSegmentType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 segmentType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle

### RFmxSpecAn_PAVTCfgSegmentType

Configures the segment type.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTCfgSegmentType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 segmentType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0".Example:"segment0""signal::sig1/segment0"You can use the RFmxSpecAn_BuildSegmentString function to build the selector string. |
| segmentType | [in] | int32 | This parameter specifies the type of segment. The default value is Phase and Amplitude.NameValueDescriptionRFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_PHASE_AND_AMPLITUDE0 (0x0)Phase and amplitude is measured in this segment.RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_AMPLITUDE1 (0x1)Amplitude is measured in this segment.RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_FREQUENCY_ERROR_MEASUREMENT2 (0x2)Frequency error is measured in this segment. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_PHASE_AND_AMPLITUDE | 0 (0x0) | Phase and amplitude is measured in this segment. |  |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_AMPLITUDE | 1 (0x1) | Amplitude is measured in this segment. |  |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_FREQUENCY_ERROR_MEASUREMENT | 2 (0x2) | Frequency error is measured in this segment. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga69a2fd42c07ebc52c86d6131a3c25b3b.html language=enus -->
## TOPIC 00430: RFmxSpecAn_PAVTCfgMeasurementLocationType

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga69a2fd42c07ebc52c86d6131a3c25b3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__pavt_1ga69a2fd42c07ebc52c86d6131a3c25b3b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement location type for the segments. Syntaxint32 __stdcall RFmxSpecAn_PAVTCfgMeasurementLocationType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLocationType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxSpecAn_PAVTCfgMeasurementLocationType

Configures the measurement location type for the segments.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTCfgMeasurementLocationType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLocationType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementLocationType | [in] | int32 | This parameter specifies whether the location at which the segment is measured is indicated by time or trigger. The default value is Time.NameValueDescriptionRFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TIME0 (0x0)The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME attribute. The number of segments is equal to the number of segment start times.RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TRIGGER1 (0x1)The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TIME | 0 (0x0) | The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME attribute. The number of segments is equal to the number of segment start times. |  |
| RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TRIGGER | 1 (0x1) | The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__pavt__array.html language=enus -->
## TOPIC 00431: Array

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__pavt__array.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__pavt__array.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_PAVTCfgSegmentMeasurementIntervalArrayConfigures an array of segment measurement offsets and lengths for the segments. RFmxSpecAn_PAVTCfgSegmentTypeArrayConfigures an array of segment types. AttachmentsNone

### Array

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_PAVTCfgSegmentMeasurementIntervalArray | Configures an array of segment measurement offsets and lengths for the segments. |
| RFmxSpecAn_PAVTCfgSegmentTypeArray | Configures an array of segment types. |

#### Attachments

None

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__pavt__segment__start__time_1gaebaadb142db34de9596ce94ae51d6ef4.html language=enus -->
## TOPIC 00432: RFmxSpecAn_PAVTCfgSegmentStartTimeStep

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__pavt__segment__start__time_1gaebaadb142db34de9596ce94ae51d6ef4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__pavt__segment__start__time_1gaebaadb142db34de9596ce94ae51d6ef4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the list of the segment start times based on Segment0 Start Time and Segment Interval. This function is used when the segments to be measured have equal duration. Syntaxint32 __stdcall RFmxSpecAn_PAVTCfgSegmentStartTimeStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32

### RFmxSpecAn_PAVTCfgSegmentStartTimeStep

Configures the list of the segment start times based on **Segment0 Start Time** and **Segment Interval**. This function is used when the segments to be measured have equal duration.

#### Syntax

int32 __stdcall RFmxSpecAn_PAVTCfgSegmentStartTimeStep(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfSegments, float64 segment0StartTime, float64 segmentInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfSegments | [in] | int32 | This parameter specifies the number of segments to be measured. The default value is 1. |
| segment0StartTime | [in] | float64 | This parameter specifies the start time for segment0. This value is expressed in seconds. |
| segmentInterval | [in] | float64 | This parameter specifies the difference in the start times between consecutive segments. This value is expressed in seconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Segment Start Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise.html language=enus -->
## TOPIC 00433: PhaseNoise

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_PhaseNoiseCfgAutoRangeConfigures the offset range and the RBW percentage when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Auto. RFmxSpecAn_PhaseNoiseCfgAveragingMultiplierConfigures the averaging multiplier. RFmxSpecAn_PhaseNo

### PhaseNoise

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_PhaseNoiseCfgAutoRange | Configures the offset range and the RBW percentage when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Auto. |
| RFmxSpecAn_PhaseNoiseCfgAveragingMultiplier | Configures the averaging multiplier. |
| RFmxSpecAn_PhaseNoiseCfgCancellation | Configures phase noise cancellation for the measurement. |
| RFmxSpecAn_PhaseNoiseCfgIntegratedNoise | Configures the integrated noise ranges. The smoothed log plot trace is used when computing integrated measurements. |
| RFmxSpecAn_PhaseNoiseCfgNumberOfRanges | Configures the number of offset ranges when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. |
| RFmxSpecAn_PhaseNoiseCfgRangeArray | Configures an array of the offset range, RBW percentage and averaging count when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. |
| RFmxSpecAn_PhaseNoiseCfgRangeDefinition | Specifies how the measurement computes offset subranges. |
| RFmxSpecAn_PhaseNoiseCfgSmoothing | Configures the smoothing type and smoothing percentage used to smoothen the measured log plot trace. |
| RFmxSpecAn_PhaseNoiseCfgSpotNoiseFrequencyList | Configures a list of frequencies at which the phase noise values are to be read using the smoothed log plot trace. |
| RFmxSpecAn_PhaseNoiseCfgSpurRemoval | Configures enabling or disabling of the spur removal and the peak excursion to use when spur removal is enabled. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga0987d744459da9e4f776ee3e383e19a5.html language=enus -->
## TOPIC 00434: RFmxSpecAn_PhaseNoiseCfgSpotNoiseFrequencyList

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga0987d744459da9e4f776ee3e383e19a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga0987d744459da9e4f776ee3e383e19a5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a list of frequencies at which the phase noise values are to be read using the smoothed log plot trace. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseCfgSpotNoiseFrequencyList(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 frequencyList[], int32 arraySize)ParametersNameDi

### RFmxSpecAn_PhaseNoiseCfgSpotNoiseFrequencyList

Configures a list of frequencies at which the phase noise values are to be read using the smoothed log plot trace.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseCfgSpotNoiseFrequencyList(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 frequencyList[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| frequencyList | [in] | float64[] | This parameter specifies an array of offset frequencies at which the corresponding phase noise is measured using the smoothed log plot trace. This value is expressed in Hz. The default value is an empty array. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga30603884162e5992af37833e4e7715cd.html language=enus -->
## TOPIC 00435: RFmxSpecAn_PhaseNoiseCfgRangeDefinition

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga30603884162e5992af37833e4e7715cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga30603884162e5992af37833e4e7715cd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the measurement computes offset subranges. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseCfgRangeDefinition(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rangeDefinition)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies

### RFmxSpecAn_PhaseNoiseCfgRangeDefinition

Specifies how the measurement computes offset subranges.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseCfgRangeDefinition(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rangeDefinition)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| rangeDefinition | [in] | int32 | This parameter specifies how the measurement computes offset subranges.NameValueDescriptionRFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_MANUAL0 (0x0)Specify the offset sub-ranges used for the measurement. Use the RFMXSPECAN_ATTR_PHASENOISE_RANGE_START_FREQUENCY attribute and the RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY attribute to configure single or multiple range start and range stop frequencies.RFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_AUTO1 (0x1)Measurement computes offset sub-ranges by dividing the user configured offset range into multiple decade sub-ranges. The range is specified by the RFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCY and the RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY attributes. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_MANUAL | 0 (0x0) | Specify the offset sub-ranges used for the measurement. Use the RFMXSPECAN_ATTR_PHASENOISE_RANGE_START_FREQUENCY attribute and the RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY attribute to configure single or multiple range start and range stop frequencies. |  |
| RFMXSPECAN_VAL_PHASENOISE_RANGE_DEFINITION_AUTO | 1 (0x1) | Measurement computes offset sub-ranges by dividing the user configured offset range into multiple decade sub-ranges. The range is specified by the RFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCY and the RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY attributes. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga543f8496a7c97cd934457c56c68e1cde.html language=enus -->
## TOPIC 00436: RFmxSpecAn_PhaseNoiseCfgNumberOfRanges

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga543f8496a7c97cd934457c56c68e1cde.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1ga543f8496a7c97cd934457c56c68e1cde.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offset ranges when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseCfgNumberOfRanges(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfRanges)ParametersNameDirectionTypeDescription

### RFmxSpecAn_PhaseNoiseCfgNumberOfRanges

Configures the number of offset ranges when you set the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga2760aff00c7960526c3bcfc3a8b607b4.html) attribute to **Manual**.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseCfgNumberOfRanges(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfRanges)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfRanges | [in] | int32 | This parameter specifies the number of manual ranges. The default value is 1.Name (Value)DescriptionNone (0)Integrated noise measurement is not computed.Measurement (1)The complete log plot frequency range, considered as a single range, is used for computing integrated measurements.Custom (2)The measurement range(s) specified by PhaseNoise Integrated Noise Start Freq attribute and the PhaseNoise Integrated Noise Stop Freq attribute is used for computing integrated measurements. |
| Name (Value) | Description |  |  |
| None (0) | Integrated noise measurement is not computed. |  |  |
| Measurement (1) | The complete log plot frequency range, considered as a single range, is used for computing integrated measurements. |  |  |
| Custom (2) | The measurement range(s) specified by PhaseNoise Integrated Noise Start Freq attribute and the PhaseNoise Integrated Noise Stop Freq attribute is used for computing integrated measurements. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gab488891c109f23c1d7626e56b57bbcca.html language=enus -->
## TOPIC 00437: RFmxSpecAn_PhaseNoiseCfgSpurRemoval

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gab488891c109f23c1d7626e56b57bbcca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gab488891c109f23c1d7626e56b57bbcca.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures enabling or disabling of the spur removal and the peak excursion to use when spur removal is enabled. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseCfgSpurRemoval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spurRemovalEnabled, float64 peakExcursion)ParametersNameDirectio

### RFmxSpecAn_PhaseNoiseCfgSpurRemoval

Configures enabling or disabling of the spur removal and the peak excursion to use when spur removal is enabled.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseCfgSpurRemoval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spurRemovalEnabled, float64 peakExcursion)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| spurRemovalEnabled | [in] | int32 | This parameter specifies whether the spur removal is enabled or disabled.NameValueDescriptionRFMXSPECAN_VAL_PHASENOISE_SPUR_REMOVAL_ENABLED_FALSE0 (0x0)Disables spur removal on the log plot trace.RFMXSPECAN_VAL_PHASENOISE_SPUR_REMOVAL_ENABLED_TRUE1 (0x1)Enables spur removal on the log plot trace. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_PHASENOISE_SPUR_REMOVAL_ENABLED_FALSE | 0 (0x0) | Disables spur removal on the log plot trace. |  |
| RFMXSPECAN_VAL_PHASENOISE_SPUR_REMOVAL_ENABLED_TRUE | 1 (0x1) | Enables spur removal on the log plot trace. |  |
| peakExcursion | [in] | float64 | This parameter specifies the peak excursion to be used when spur detection is performed. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gadb6750d4a8351698bbee15afdb5f83e9.html language=enus -->
## TOPIC 00438: RFmxSpecAn_PhaseNoiseCfgRangeArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gadb6750d4a8351698bbee15afdb5f83e9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gadb6750d4a8351698bbee15afdb5f83e9.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the offset range, RBW percentage and averaging count when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseCfgRangeArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 rangeStartFrequenc

### RFmxSpecAn_PhaseNoiseCfgRangeArray

Configures an array of the offset range, RBW percentage and averaging count when you set the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga2760aff00c7960526c3bcfc3a8b607b4.html) attribute to **Manual**.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseCfgRangeArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 rangeStartFrequency[], float64 rangeStopFrequency[], float64 rangeRBWPercentage[], int32 rangeAveragingCount[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| rangeStartFrequency | [in] | float64[] | This parameter specifies the start frequency of the offset frequency for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Auto. This value is expressed in Hz. The default value is 1000.. |
| rangeStopFrequency | [in] | float64[] | This parameter Specifies the stop offset frequency for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. This value is expressed in Hz. The default value is 1000000. |
| rangeRBWPercentage | [in] | float64[] | This parameter specifies the RBW as a percentage of the start frequency of the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. This value is expressed as a percentage. The default value is 10. |
| rangeAveragingCount | [in] | int32[] | This parameter specifies the averaging count for the specified range. The default value is 10. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gaf605d2bc5fa6d359c2ea2e85b99d4d4e.html language=enus -->
## TOPIC 00439: RFmxSpecAn_PhaseNoiseCfgSmoothing

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gaf605d2bc5fa6d359c2ea2e85b99d4d4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__phasenoise_1gaf605d2bc5fa6d359c2ea2e85b99d4d4e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the smoothing type and smoothing percentage used to smoothen the measured log plot trace. Syntaxint32 __stdcall RFmxSpecAn_PhaseNoiseCfgSmoothing(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 smoothingType, float64 smoothingPercentage)ParametersNameDirectionTypeDescript

### RFmxSpecAn_PhaseNoiseCfgSmoothing

Configures the smoothing type and smoothing percentage used to smoothen the measured log plot trace.

#### Syntax

int32 __stdcall RFmxSpecAn_PhaseNoiseCfgSmoothing(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 smoothingType, float64 smoothingPercentage)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| smoothingType | [in] | int32 | This parameter specifies the smoothing type used to smoothen the measured log plot trace. The default value is Logarithmic.NameValueDescriptionRFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_NONE0 (0x0)Smoothing is disabled.RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LINEAR1 (0x1)Performs linear moving average filtering on the measured phase noise log plot trace.RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LOGARITHMIC2 (0x2)Performs logarithmic moving average filtering on the measured phase noise log plot trace.RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_MEDIAN3 (0x3)Performs moving median filtering on the measured phase noise log plot trace. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_NONE | 0 (0x0) | Smoothing is disabled. |  |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LINEAR | 1 (0x1) | Performs linear moving average filtering on the measured phase noise log plot trace. |  |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_LOGARITHMIC | 2 (0x2) | Performs logarithmic moving average filtering on the measured phase noise log plot trace. |  |
| RFMXSPECAN_VAL_PHASENOISE_SMOOTHING_TYPE_MEDIAN | 3 (0x3) | Performs moving median filtering on the measured phase noise log plot trace. |  |
| smoothingPercentage | [in] | float64 | This parameter specifies the number of points to use in the moving average filter as a percentage of total number of points in the log plot trace. This value is expressed as a percentage. The default value is 2. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__powelist.html language=enus -->
## TOPIC 00440: Powelist

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__powelist.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__powelist.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_PowerListCfgRBWFilterArrayConfigures array of the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter, each corresponding to a segment. AttachmentsNone

### Powelist

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_PowerListCfgRBWFilterArray | Configures array of the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter, each corresponding to a segment. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem.html language=enus -->
## TOPIC 00441: SEM

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsArrayGroup membersNameDescriptionRFmxSpecAn_SEMCfgAveragingConfigures averaging for the spectral emission mask (SEM) measurement. RFmxSpecAn_SEMCfgCarrierChannelBandwidthConfigures the channel bandwidth of the carrier. RFmxSpecAn_SEMCfgCarrierEnabledConfigures whether to consider the carrier p

### SEM

#### Groups

- Array

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_SEMCfgAveraging | Configures averaging for the spectral emission mask (SEM) measurement. |
| RFmxSpecAn_SEMCfgCarrierChannelBandwidth | Configures the channel bandwidth of the carrier. |
| RFmxSpecAn_SEMCfgCarrierEnabled | Configures whether to consider the carrier power as part of total carrier power measurement. Use "carrier<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgCarrierFrequency | Configures the center frequency, in Hz, of the carrier, relative to the RF center frequency. |
| RFmxSpecAn_SEMCfgCarrierIntegrationBandwidth | Configures the frequency range, in Hz, over which the measurement integrates the carrier power. Use "carrier<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgCarrierRBWFilter | Configures the resolution bandwidth (RBW) filter of the carrier signal. Use "carrier<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgCarrierRRCFilter | Configures the root raised cosine (RRC) channel filter to apply on the acquired carrier channel before measuring the channel power. RRC alpha is the filter roll off. Use "carrier<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgFFT | Configures window and FFT to obtain a spectrum for the spectral emission mask (SEM) measurement. |
| RFmxSpecAn_SEMCfgNumberOfCarriers | Configures the number of carriers for the spectral emission mask (SEM) measurement. |
| RFmxSpecAn_SEMCfgNumberOfOffsets | Configures the number of offset segments for the spectral emission mask (SEM) measurement. |
| RFmxSpecAn_SEMCfgOffsetAbsoluteLimit | Configures the absolute limit mode and specifies the absolute power limits corresponding to the beginning and end of the offset segment. Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgOffsetBandwidthIntegral | Configures the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgOffsetFrequency | Configures the offset frequency start and stop values and specifies whether the offset segment is present on one side, or on both sides of the carriers. Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgOffsetFrequencyDefinition | Configures the offset frequency definition for the SEM measurement. Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgOffsetLimitFailMask | Specifies the criteria to determine the measurement fail status. Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgOffsetRBWFilter | Configures the resolution bandwidth (RBW) filter of the offset segment. Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgOffsetRelativeAttenuation | Configures the attenuation, in dB, relative to the external attenuation. Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgOffsetRelativeLimit | Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. Use "offset<n>" as the selector string to configure this function. |
| RFmxSpecAn_SEMCfgPowerUnits | Configures the units for the absolute power. |
| RFmxSpecAn_SEMCfgReferenceType | Configures whether the power reference is the integrated power or the peak power in the closest carrier channel. |
| RFmxSpecAn_SEMCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga104617fdfc37c7ec2f9b089a0d314a7c.html language=enus -->
## TOPIC 00442: RFmxSpecAn_SEMCfgOffsetFrequency

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga104617fdfc37c7ec2f9b089a0d314a7c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga104617fdfc37c7ec2f9b089a0d314a7c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset frequency start and stop values and specifies whether the offset segment is present on one side, or on both sides of the carriers. Use "offset<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetFrequency(niRFmxInstrHandle instrum

### RFmxSpecAn_SEMCfgOffsetFrequency

Configures the offset frequency start and stop values and specifies whether the offset segment is present on one side, or on both sides of the carriers. Use "offset<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 offsetStartFrequency, float64 offsetStopFrequency, int32 offsetEnabled, int32 offsetSideband)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used.Example:"offset0""signal::sig1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| offsetStartFrequency | [in] | float64 | This parameter specifies the start frequency, in Hz, of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the RFMXSPECAN_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION attribute. The default value is 1 MHz. |
| offsetStopFrequency | [in] | float64 | This parameter specifies the stop frequency, in Hz, of the offset segment relative to the closest configured carrier channel bandwidth center or carrier channel bandwidth edge based on the value of the SEM Offset Freq Definition attribute. The default value is 2 MHz. |
| offsetEnabled | [in] | int32 | This parameter specifies whether to enable the offset segment for the SEM measurement. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SEM_OFFSET_ENABLED_FALSE0 (0x0)Disables the offset segment for the SEM measurement.RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_TRUE1 (0x1)Enables the offset segment for the SEM measurement. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_FALSE | 0 (0x0) | Disables the offset segment for the SEM measurement. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_ENABLED_TRUE | 1 (0x1) | Enables the offset segment for the SEM measurement. |  |
| offsetSideband | [in] | int32 | This parameter specifies whether the offset segment is present on one side, or on both sides of the carriers. The default value is Both.NameValueDescriptionRFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE0 (0x0)Configures a lower offset segment to the left of the leftmost carrier.RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_POSITIVE1 (0x1)Configures an upper offset segment to the right of the rightmost carrier.RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_BOTH2 (0x2)Configures both negative and positive offset segments. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE | 0 (0x0) | Configures a lower offset segment to the left of the leftmost carrier. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_POSITIVE | 1 (0x1) | Configures an upper offset segment to the right of the rightmost carrier. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_SIDEBAND_BOTH | 2 (0x2) | Configures both negative and positive offset segments. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga2c5eeed80e3801470e22ddfa964da4ba.html language=enus -->
## TOPIC 00443: RFmxSpecAn_SEMCfgPowerUnits

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga2c5eeed80e3801470e22ddfa964da4ba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga2c5eeed80e3801470e22ddfa964da4ba.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the units for the absolute power. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Inst

### RFmxSpecAn_SEMCfgPowerUnits

Configures the units for the absolute power.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnits)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| powerUnits | [in] | int32 | This parameter specifies the units for the absolute power. The default value is dBm.NameValueDescriptionRFMXSPECAN_VAL_SEM_POWER_UNITS_DBM0 (0x0)The absolute powers are reported in dBm.RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ1 (0x1)The absolute powers are reported in dBm/Hz. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM | 0 (0x0) | The absolute powers are reported in dBm. |  |
| RFMXSPECAN_VAL_SEM_POWER_UNITS_DBM_PER_HZ | 1 (0x1) | The absolute powers are reported in dBm/Hz. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga456275aa6c24986449f61a2326784be7.html language=enus -->
## TOPIC 00444: RFmxSpecAn_SEMCfgOffsetFrequencyDefinition

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga456275aa6c24986449f61a2326784be7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga456275aa6c24986449f61a2326784be7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the offset frequency definition for the SEM measurement. Use "offset<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetFrequencyDefinition(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetFrequencyDefinition)Parameter

### RFmxSpecAn_SEMCfgOffsetFrequencyDefinition

Configures the offset frequency definition for the SEM measurement. Use "offset<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetFrequencyDefinition(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 offsetFrequencyDefinition)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the Selector String comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "offset0".Example:"offset0""signal::sig1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| offsetFrequencyDefinition | [in] | int32 | This parameter specifies the definition of the start frequency and stop frequency of the offset segments from the nearest carrier channels. The default value is Carrier Center to Meas BW Center.NameValueDescriptionRFMXSPECAN_VAL_SEM_CARRIER_CENTER_TO_MEASUREMENT_BANDWIDTH_CENTER0 (0x0)The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the center of the offset segment measurement bandwidth. Measurement Bandwidth = Resolution Bandwidth * Bandwidth Integral.RFMXSPECAN_VAL_SEM_CARRIER_CENTER_TO_MEASUREMENT_BANDWIDTH_EDGE1 (0x1)The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the nearest edge of the offset segment measurement bandwidth.RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_CENTER2 (0x2)The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the center of the nearest offset segment measurement bandwidth.RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_EDGE3 (0x3)The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the edge of the nearest offset segment measurement bandwidth. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_CARRIER_CENTER_TO_MEASUREMENT_BANDWIDTH_CENTER | 0 (0x0) | The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the center of the offset segment measurement bandwidth. Measurement Bandwidth = Resolution Bandwidth * Bandwidth Integral. |  |
| RFMXSPECAN_VAL_SEM_CARRIER_CENTER_TO_MEASUREMENT_BANDWIDTH_EDGE | 1 (0x1) | The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the nearest edge of the offset segment measurement bandwidth. |  |
| RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_CENTER | 2 (0x2) | The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the center of the nearest offset segment measurement bandwidth. |  |
| RFMXSPECAN_VAL_SEM_CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_EDGE | 3 (0x3) | The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the edge of the nearest offset segment measurement bandwidth. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga7b529ab3e9623c6b3df1b9f7e9e53de4.html language=enus -->
## TOPIC 00445: RFmxSpecAn_SEMCfgAveraging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga7b529ab3e9623c6b3df1b9f7e9e53de4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1ga7b529ab3e9623c6b3df1b9f7e9e53de4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the spectral emission mask (SEM) measurement. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[

### RFmxSpecAn_SEMCfgAveraging

Configures averaging for the spectral emission mask (SEM) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_TRUE1 (0x1)The SEM measurement uses the RFMXSPECAN_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The SEM measurement uses the RFMXSPECAN_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectral Measurements Concepts topic for more information about averaging types. The default value is RMS.NameValueDescriptionRFMXSPECAN_VAL_SEM_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MINIMUM4 (0x4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_SEM_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa15f099009696ae2a1c60a42b29d00b2.html language=enus -->
## TOPIC 00446: RFmxSpecAn_SEMCfgNumberOfCarriers

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa15f099009696ae2a1c60a42b29d00b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa15f099009696ae2a1c60a42b29d00b2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of carriers for the spectral emission mask (SEM) measurement. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgNumberOfCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThi

### RFmxSpecAn_SEMCfgNumberOfCarriers

Configures the number of carriers for the spectral emission mask (SEM) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgNumberOfCarriers(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCarriers)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfCarriers | [in] | int32 | This parameter specifies the number of carriers. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa24b21d6a1510ba050be57640c710cc8.html language=enus -->
## TOPIC 00447: RFmxSpecAn_SEMCfgOffsetRelativeAttenuation

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa24b21d6a1510ba050be57640c710cc8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa24b21d6a1510ba050be57640c710cc8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the attenuation, in dB, relative to the external attenuation. Use "offset<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeAttenuation)Paramete

### RFmxSpecAn_SEMCfgOffsetRelativeAttenuation

Configures the attenuation, in dB, relative to the external attenuation. Use "offset<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 relativeAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used.Example:"offset0""signal::sig1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| relativeAttenuation | [in] | float64 | This parameter specifies the attenuation, in dB, relative to the external attenuation. Use this parameter to compensate for variations in external attenuation when the offset channels are spread wide in frequency. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa65e691fc93308f66a10420a98e1d289.html language=enus -->
## TOPIC 00448: RFmxSpecAn_SEMCfgOffsetRelativeLimit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa65e691fc93308f66a10420a98e1d289.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaa65e691fc93308f66a10420a98e1d289.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. Use "offset<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, c

### RFmxSpecAn_SEMCfgOffsetRelativeLimit

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. Use "offset<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 relativeLimitMode, float64 relativeLimitStart, float64 relativeLimitStop)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used.Example:"offset0""signal::sig1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| relativeLimitMode | [in] | int32 | This parameter specifies whether the relative limit mask is a flat line or a line with a slope. The default value is Manual.NameValueDescriptionRFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_MANUAL0 (0x0)The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask.RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_COUPLE1 (0x1)The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start attribute. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_MANUAL | 0 (0x0) | The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_COUPLE | 1 (0x1) | The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start attribute. |  |
| relativeLimitStart | [in] | float64 | This parameter specifies the relative power limit, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the Relative Limit Mode parameter to Couple. The default value is -20. |
| relativeLimitStop | [in] | float64 | This parameter specifies the relative power limit, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the Relative Limit Mode parameter to Couple. The default value is -30. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaae733bd675a4f70493e16650c020a11d.html language=enus -->
## TOPIC 00449: RFmxSpecAn_SEMCfgCarrierEnabled

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaae733bd675a4f70493e16650c020a11d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gaae733bd675a4f70493e16650c020a11d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to consider the carrier power as part of total carrier power measurement. Use "carrier<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgCarrierEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 carrierEnabled)Param

### RFmxSpecAn_SEMCfgCarrierEnabled

Configures whether to consider the carrier power as part of total carrier power measurement. Use "carrier<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgCarrierEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 carrierEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"carrier0""signal::sig1/carrier0"You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| carrierEnabled | [in] | int32 | This parameter specifies whether to consider the carrier power as part of total carrier power measurement. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SEM_ENABLED_FALSE0 (0x0)The carrier power is not considered as part of the total carrier power.RFMXSPECAN_VAL_SEM_ENABLED_TRUE1 (0x1)The carrier power is considered as part of the total carrier power. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_ENABLED_FALSE | 0 (0x0) | The carrier power is not considered as part of the total carrier power. |  |
| RFMXSPECAN_VAL_SEM_ENABLED_TRUE | 1 (0x1) | The carrier power is considered as part of the total carrier power. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gac11656286629959d2c4f5748a9fdb90d.html language=enus -->
## TOPIC 00450: RFmxSpecAn_SEMCfgOffsetBandwidthIntegral

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gac11656286629959d2c4f5748a9fdb90d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gac11656286629959d2c4f5748a9fdb90d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). Use "offset<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandl

### RFmxSpecAn_SEMCfgOffsetBandwidthIntegral

Configures the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the resolution bandwidth (RBW). Use "offset<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetBandwidthIntegral(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandwidthIntegral)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used.Example:"offset0""signal::sig1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| bandwidthIntegral | [in] | int32 | This parameter specifies the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. If you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gace9d92982d1812048a470a7d5fc8c192.html language=enus -->
## TOPIC 00451: RFmxSpecAn_SEMCfgNumberOfOffsets

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gace9d92982d1812048a470a7d5fc8c192.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gace9d92982d1812048a470a7d5fc8c192.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offset segments for the spectral emission mask (SEM) measurement. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHand

### RFmxSpecAn_SEMCfgNumberOfOffsets

Configures the number of offset segments for the spectral emission mask (SEM) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfOffsets | [in] | int32 | This parameter specifies the number of offset segments. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gad40711274f2068b12db3489940841023.html language=enus -->
## TOPIC 00452: RFmxSpecAn_SEMCfgCarrierFrequency

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gad40711274f2068b12db3489940841023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gad40711274f2068b12db3489940841023.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency, in Hz, of the carrier, relative to the RF center frequency. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgCarrierFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 carrierFrequency)RemarksUse "carrier< <i> n </i> >" as the selector string to config

### RFmxSpecAn_SEMCfgCarrierFrequency

Configures the center frequency, in Hz, of the carrier, relative to the RF center frequency.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgCarrierFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 carrierFrequency)

#### Remarks

Use "carrier< 
<i> 
n 
</i> 
>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used.Example:"carrier0""signal::sig1/carrier0"You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| carrierFrequency | [in] | float64 | This parameter specifies the center frequency, in Hz, of the carrier, relative to the RF RFMXSPECAN_ATTR_CENTER_FREQUENCY. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gae46ca3cc9eabba5edaa193c6ad320836.html language=enus -->
## TOPIC 00453: RFmxSpecAn_SEMCfgOffsetAbsoluteLimit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gae46ca3cc9eabba5edaa193c6ad320836.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gae46ca3cc9eabba5edaa193c6ad320836.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the absolute limit mode and specifies the absolute power limits corresponding to the beginning and end of the offset segment. Use "offset<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetAbsoluteLimit(niRFmxInstrHandle instrumentHandle, c

### RFmxSpecAn_SEMCfgOffsetAbsoluteLimit

Configures the absolute limit mode and specifies the absolute power limits corresponding to the beginning and end of the offset segment. Use "offset<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetAbsoluteLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 absoluteLimitMode, float64 absoluteLimitStart, float64 absoluteLimitStop)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used.Example:"offset0""signal::sig1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| absoluteLimitMode | [in] | int32 | This parameter specifies whether the absolute limit mask is a flat line or a line with a slope. The default value is Couple.NameValueDescriptionRFMXSPECAN_VAL_SEM_OFFSET_ABSOLUTE_LIMIT_MODE_MANUAL0 (0x0)The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP attribute values as the two ends is considered as the mask.RFMXSPECAN_VAL_SEM_OFFSET_ABSOLUTE_LIMIT_MODE_COUPLE1 (0x1)The two ends of the line are coupled to the value of the SEM Offset Abs Limit Start attribute. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_OFFSET_ABSOLUTE_LIMIT_MODE_MANUAL | 0 (0x0) | The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP attribute values as the two ends is considered as the mask. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_ABSOLUTE_LIMIT_MODE_COUPLE | 1 (0x1) | The two ends of the line are coupled to the value of the SEM Offset Abs Limit Start attribute. |  |
| absoluteLimitStart | [in] | float64 | This parameter specifies the absolute power limit, in dBm, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the Absolute Limit Mode parameter to Couple. The default value is -10. |
| absoluteLimitStop | [in] | float64 | This parameter specifies the absolute power limit, in dBm, corresponding to the end of the offset segment. This parameter is ignored when you set the Absolute Limit Mode parameter to Couple. The default value is -10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gae5f3c1dbf177ddf754d08e3d2f1cd2a8.html language=enus -->
## TOPIC 00454: RFmxSpecAn_SEMCfgOffsetRBWFilter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gae5f3c1dbf177ddf754d08e3d2f1cd2a8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem_1gae5f3c1dbf177ddf754d08e3d2f1cd2a8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter of the offset segment. Use "offset<n>" as the selector string to configure this function. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType

### RFmxSpecAn_SEMCfgOffsetRBWFilter

Configures the resolution bandwidth (RBW) filter of the offset segment. Use "offset<n>" as the selector string to configure this function.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and offset number. If you do not specify the signal name, the default signal instance is used.Example:"offset0""signal::sig1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the SEM topic for more details on RBW and sweep time. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SEM_RBW_AUTO_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH attribute.RFMXSPECAN_VAL_SEM_RBW_AUTO_TRUE1 (0x1)The measurement computes the RBW. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXSPECAN_VAL_SEM_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth, in Hz, of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment, when you set the RBW Auto parameter to False. The default value is 10 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the response of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is performed.RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)The RBW filter has a Gaussian response.RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FLAT2 (0x2)The RBW filter has a flat response. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |  |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |  |
| RFMXSPECAN_VAL_SEM_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__sem__array_1ga93361200e7fe3412c9a7716f3d7ccbaf.html language=enus -->
## TOPIC 00455: RFmxSpecAn_SEMCfgOffsetRelativeLimitArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__sem__array_1ga93361200e7fe3412c9a7716f3d7ccbaf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__sem__array_1ga93361200e7fe3412c9a7716f3d7ccbaf.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment. Syntaxint32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 relativeLimitMode[], float64 relat

### RFmxSpecAn_SEMCfgOffsetRelativeLimitArray

Configures the relative limit mode and specifies the relative power limits corresponding to the beginning and end of the offset segment.

#### Syntax

int32 __stdcall RFmxSpecAn_SEMCfgOffsetRelativeLimitArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 relativeLimitMode[], float64 relativeLimitStart[], float64 relativeLimitStop[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| relativeLimitMode | [in] | int32[] | This parameter specifies whether the relative limit mask is a flat line or a line with a slope. The default value is Manual.NameValueDescriptionRFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_MANUAL0 (0x0)The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask.RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_COUPLE1 (0x1)The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start attribute. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_MANUAL | 0 (0x0) | The line specified by the RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START and RFMXSPECAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP attribute values as the two ends is considered as the mask. |  |
| RFMXSPECAN_VAL_SEM_OFFSET_RELATIVE_LIMIT_MODE_COUPLE | 1 (0x1) | The two ends of the line are coupled to the value of the SEM Offset Rel Limit Start attribute. |  |
| relativeLimitStart | [in] | float64[] | This parameter specifies the array of relative power limits, in dB, corresponding to the beginning of the offset segment. The value of this parameter is also set as the stop limit for the offset segment when you set the Relative Limit Mode parameter to Couple. The default value is -20. |
| relativeLimitStop | [in] | float64[] | This parameter specifies the array of relative power limits, in dB, corresponding to the end of the offset segment. This parameter is ignored if you set the Relative Limit Mode parameter to Couple. The default value is -30. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum.html language=enus -->
## TOPIC 00456: Spectrum

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_SpectrumCfgAveragingConfigures averaging for the spectrum measurement. RFmxSpecAn_SpectrumCfgDetectorConfigures the detector settings, including detector type and the number of points to be detected. RFmxSpecAn_SpectrumCfgFFTConfigures window and FFT

### Spectrum

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_SpectrumCfgAveraging | Configures averaging for the spectrum measurement. |
| RFmxSpecAn_SpectrumCfgDetector | Configures the detector settings, including detector type and the number of points to be detected. |
| RFmxSpecAn_SpectrumCfgFFT | Configures window and FFT to obtain a spectrum for the spectrum measurement. |
| RFmxSpecAn_SpectrumCfgFrequencyStartStop | Configures the start frequency and stop frequency for the spectrum measurement. |
| RFmxSpecAn_SpectrumCfgMeasurementMethod | Configures the method for performing the Spectrum measurement. |
| RFmxSpecAn_SpectrumCfgNoiseCompensationEnabled | Configures compensation of the spectrum for the inherent noise floor of the signal analyzer. |
| RFmxSpecAn_SpectrumCfgPowerUnits | Configures the units for the absolute power. |
| RFmxSpecAn_SpectrumCfgRBWFilter | Configures the resolution bandwidth (RBW) filter. |
| RFmxSpecAn_SpectrumCfgSpan | Configures the frequency range, in Hz, around the center frequency, to acquire for the spectrum measurement. |
| RFmxSpecAn_SpectrumCfgSweepTime | Configures the sweep time. |
| RFmxSpecAn_SpectrumCfgVBWFilter | Configures the VBW settings including VBW Auto, VBW(Hz) and VBW to RBW ratio. |
| RFmxSpecAn_SpectrumValidateNoiseCalibrationData | Indicates whether calibration data is valid for the configuration specified by the signal name in the Selector string parameter. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga0c3eabc6629ec3414fa55d9ff11cd720.html language=enus -->
## TOPIC 00457: RFmxSpecAn_SpectrumValidateNoiseCalibrationData

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga0c3eabc6629ec3414fa55d9ff11cd720.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga0c3eabc6629ec3414fa55d9ff11cd720.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether calibration data is valid for the configuration specified by the signal name in the Selector string parameter. Syntaxint32 __stdcall RFmxSpecAn_SpectrumValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *noiseCalibrationDataValid)Parameter

### RFmxSpecAn_SpectrumValidateNoiseCalibrationData

Indicates whether calibration data is valid for the configuration specified by the signal name in the **Selector string** parameter.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumValidateNoiseCalibrationData(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *noiseCalibrationDataValid)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| noiseCalibrationDataValid | [out] | int32 * | This parameter returns whether the calibration data is valid.Name (Value)DescriptionFalse (0)Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range.True (1)Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |
| Name (Value) | Description |  |  |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |  |  |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga16d71bdafb7be1d3f31941519e5e9356.html language=enus -->
## TOPIC 00458: RFmxSpecAn_SpectrumCfgPowerUnits

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga16d71bdafb7be1d3f31941519e5e9356.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga16d71bdafb7be1d3f31941519e5e9356.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the units for the absolute power. Syntaxint32 __stdcall RFmxSpecAn_SpectrumCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spectrumPowerUnits)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxSpecAn_SpectrumCfgPowerUnits

Configures the units for the absolute power.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumCfgPowerUnits(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 spectrumPowerUnits)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| spectrumPowerUnits | [in] | int32 | This parameter specifies the units for the absolute power. The default value is dBm.NameValueDescriptionRFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM0 (0x0)The absolute powers are reported in dBm.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM_PER_HZ1 (0x1)The absolute powers are reported in dBm/Hz.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBW2 (0x2)The absolute powers are reported in dBW.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBV3 (0x3)The absolute powers are reported in dBV.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBMV4 (0x4)The absolute powers are reported in dBmV.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBUV5 (0x5)The absolute powers are reported in dBuV.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_WATTS6 (0x6)The absolute powers are reported in W.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS7 (0x7)The absolute powers are reported in volts.RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS_SQUARED8 (0x8)The absolute powers are reported in volts2. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM | 0 (0x0) | The absolute powers are reported in dBm. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBM_PER_HZ | 1 (0x1) | The absolute powers are reported in dBm/Hz. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBW | 2 (0x2) | The absolute powers are reported in dBW. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBV | 3 (0x3) | The absolute powers are reported in dBV. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBMV | 4 (0x4) | The absolute powers are reported in dBmV. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_DBUV | 5 (0x5) | The absolute powers are reported in dBuV. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_WATTS | 6 (0x6) | The absolute powers are reported in W. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS | 7 (0x7) | The absolute powers are reported in volts. |  |
| RFMXSPECAN_VAL_SPECTRUM_POWER_UNITS_VOLTS_SQUARED | 8 (0x8) | The absolute powers are reported in volts2. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga392a74a6fb0604c1a9ff0e3cb5cb98d4.html language=enus -->
## TOPIC 00459: RFmxSpecAn_SpectrumCfgRBWFilter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga392a74a6fb0604c1a9ff0e3cb5cb98d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga392a74a6fb0604c1a9ff0e3cb5cb98d4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. Syntaxint32 __stdcall RFmxSpecAn_SpectrumCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter

### RFmxSpecAn_SpectrumCfgRBWFilter

Configures the resolution bandwidth (RBW) filter.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the Spectral Measurements Concepts topic for more details on RBW and sweep time. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute.RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_TRUE1 (0x1)The measurement computes the RBW. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the response of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is performed.RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)The RBW filter has a Gaussian response.RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FLAT2 (0x2)The RBW filter has a flat response. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |  |
| RFMXSPECAN_VAL_SPECTRUM_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga5e7f81f7d54c8e80902f73bba79e4e74.html language=enus -->
## TOPIC 00460: RFmxSpecAn_SpectrumCfgSweepTime

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga5e7f81f7d54c8e80902f73bba79e4e74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1ga5e7f81f7d54c8e80902f73bba79e4e74.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxSpecAn_SpectrumCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx sess

### RFmxSpecAn_SpectrumCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_INTERVAL attribute.RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_INTERVAL attribute. |  |
| RFMXSPECAN_VAL_SPECTRUM_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH attribute. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time, in seconds, when you set the Sweep Time Auto parameter to False. The default value is 1 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gac4b424cfa0a07fb8e9dda39af63d97d1.html language=enus -->
## TOPIC 00461: RFmxSpecAn_SpectrumCfgMeasurementMethod

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gac4b424cfa0a07fb8e9dda39af63d97d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gac4b424cfa0a07fb8e9dda39af63d97d1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the Spectrum measurement. Syntaxint32 __stdcall RFmxSpecAn_SpectrumCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter sp

### RFmxSpecAn_SpectrumCfgMeasurementMethod

Configures the method for performing the Spectrum measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementMethod | [in] | int32 | This parameter specifies the method for performing the Spectrum measurement. The default value is Normal.NameValueDescriptionRFMXSPECAN_VAL_SPECTRUM_MEASUREMENT_METHOD_NORMAL0 (0x0)The Spectrum measurement acquires the spectrum using the same signal analyzer setting across frequency bands.\| RFMXSPECAN_VAL_SPECTRUM_MEASUREMENT_METHOD_SEQUENTIAL_FFT \| 2 (0x2) \| The Spectrum measurement acquires I/Q samples for a duration specified by the RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_INTERVAL attribute. These samples are divided into smaller chunks. If the attribute RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH is True, The size of each chunk is defined by the RFMXSPECAN_ATTR_SPECTRUM_SEQUENTIAL_FFT_SIZE attribute. If the attribute Spectrum RBW Auto is False, the Spectrum Sequential FFT Size is auto computed based on the configured RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_BANDWIDTH. The overlap between the chunks is defined by the RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_MODE attribute. FFT is computed on each of these chunks. The resultant FFTs are averaged as per the configured averaging type in the attribute RFMXSPECAN_ATTR_SPECTRUM_FFT_OVERLAP_TYPEto get the spectrum. Sequential FFT method should be used for the following scenarios.While performing fast Spectrum measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced.When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used.For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following attributes have limited support when you set the Spectrum Measurement Method attribute to Sequential FFT.\| Property \| Supported Value \|\|-----------------------------------------------—\|------------------—\|\| RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_AUTO_BANDWIDTH \| True \|\| RFMXSPECAN_ATTR_SPECTRUM_RBW_FILTER_TYPE \| FFT Based \|\| RFMXSPECAN_ATTR_SPECTRUM_SWEEP_TIME_AUTO \| False \|\| RFMXSPECAN_ATTR_SPECTRUM_AVERAGING_COUNT \| >=1 \|\| RFMXSPECAN_ATTR_SPECTRUM_NUMBER_OF_ANALYSIS_THREADS \| >=1 \|\| RFMXSPECAN_ATTR_SPECTRUM_AMPLITUDE_CORRECTION_TYPE \| RF Center Frequency \|\| RFMXSPECAN_ATTR_SPECTRUM_VBW_FILTER_VBW_TO_RBW_RATIO \| >=3 \|Note For multi-span FFT, the averaging count should be 1.\| |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPECTRUM_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The Spectrum measurement acquires the spectrum using the same signal analyzer setting across frequency bands. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gad88714fe7c8870fb5ca9b9390222f0fc.html language=enus -->
## TOPIC 00462: RFmxSpecAn_SpectrumCfgFFT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gad88714fe7c8870fb5ca9b9390222f0fc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gad88714fe7c8870fb5ca9b9390222f0fc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures window and FFT to obtain a spectrum for the spectrum measurement. Syntaxint32 __stdcall RFmxSpecAn_SpectrumCfgFFT(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindow, float64 fftPadding)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxSpecAn_SpectrumCfgFFT

Configures window and FFT to obtain a spectrum for the spectrum measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumCfgFFT(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindow, float64 fftPadding)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| fftWindow | [in] | int32 | This parameter specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectral Measurements Concepts topic for more information about FFT window types. The default value is Flat Top.NameValueDescriptionRFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_NONE0 (0x0)Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes.RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_FLAT_TOP1 (0x1)Measures single-tone amplitudes accurately.RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_HANNING2 (0x2)Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements.RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_HAMMING3 (0x3)Analyzes closely-spaced sine waves.RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_GAUSSIAN4 (0x4)Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis.RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_BLACKMAN5 (0x5)Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate.RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_BLACKMAN_HARRIS6 (0x6)Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe.RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_KAISER_BESSEL7 (0x7)Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_NONE | 0 (0x0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_FLAT_TOP | 1 (0x1) | Measures single-tone amplitudes accurately. |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_HANNING | 2 (0x2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_HAMMING | 3 (0x3) | Analyzes closely-spaced sine waves. |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_GAUSSIAN | 4 (0x4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_BLACKMAN | 5 (0x5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_BLACKMAN_HARRIS | 6 (0x6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |  |
| RFMXSPECAN_VAL_SPECTRUM_FFT_WINDOW_KAISER_BESSEL | 7 (0x7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |  |
| fftPadding | [in] | float64 | This parameter specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: FFT size = waveform size * padding. This parameter is used only when the acquisition span is less than the device instantaneous bandwidth. The default value is -1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gaf5e39024b1c7cf9bb22b4d167f748a19.html language=enus -->
## TOPIC 00463: RFmxSpecAn_SpectrumCfgDetector

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gaf5e39024b1c7cf9bb22b4d167f748a19.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spectrum_1gaf5e39024b1c7cf9bb22b4d167f748a19.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the detector settings, including detector type and the number of points to be detected. Syntaxint32 __stdcall RFmxSpecAn_SpectrumCfgDetector(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 detectorType, int32 detectorPoints)ParametersNameDirectionTypeDescriptioninstrument

### RFmxSpecAn_SpectrumCfgDetector

Configures the detector settings, including detector type and the number of points to be detected.

#### Syntax

int32 __stdcall RFmxSpecAn_SpectrumCfgDetector(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 detectorType, int32 detectorPoints)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| detectorType | [in] | int32 | This parameter specifies the type of detector to be used. The default value is None. Refer to Spectral Measurements Concepts topic for more information on detectors.NameValueDescriptionRFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_NONE0 (0x0)The detector is disabled.RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_SAMPLE1 (0x1)The middle sample in the bucket is detected.RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_NORMAL2 (0x2)The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets.RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_PEAK3 (0x3)The maximum value of the samples in the bucket is detected.RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_NEGATIVE_PEAK4 (0x4)The minimum value of the samples in the bucket is detected.RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_AVERAGE_RMS5 (0x5)The average RMS of all the samples in the bucket is detected.RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_AVERAGE_VOLTAGE6 (0x6)The average voltage of all the samples in the bucket is detected.RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_AVERAGE_LOG7 (0x7)The average log of all the samples in the bucket is detected. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_NONE | 0 (0x0) | The detector is disabled. |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_SAMPLE | 1 (0x1) | The middle sample in the bucket is detected. |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_NORMAL | 2 (0x2) | The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_PEAK | 3 (0x3) | The maximum value of the samples in the bucket is detected. |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_NEGATIVE_PEAK | 4 (0x4) | The minimum value of the samples in the bucket is detected. |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_AVERAGE_RMS | 5 (0x5) | The average RMS of all the samples in the bucket is detected. |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_AVERAGE_VOLTAGE | 6 (0x6) | The average voltage of all the samples in the bucket is detected. |  |
| RFMXSPECAN_VAL_SPECTRUM_DETECTOR_TYPE_AVERAGE_LOG | 7 (0x7) | The average log of all the samples in the bucket is detected. |  |
| detectorPoints | [in] | int32 | This parameter specifies the number of points after the detector is applied. The default value is 1001. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spectrum

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga420dadbd1c46d5ee8d907da28945f500.html language=enus -->
## TOPIC 00464: RFmxSpecAn_SpurCfgFFTWindowType

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga420dadbd1c46d5ee8d907da28945f500.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga420dadbd1c46d5ee8d907da28945f500.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the FFT window to obtain a spectrum for the spurious emission (Spur) measurement. Supported devices: PXIe-5665, PXIe-5668. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgFFTWindowType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindow)ParametersNameDirectionTypeDescriptio

### RFmxSpecAn_SpurCfgFFTWindowType

Configures the FFT window to obtain a spectrum for the spurious emission (Spur) measurement. **Supported devices:** PXIe-5665, PXIe-5668.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgFFTWindowType(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 fftWindow)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| fftWindow | [in] | int32 | This parameter specifies the FFT window type to use to reduce spectral leakage. Refer to the Window and FFT section of the Spectral Measurements Concepts topic for more information about FFT window types. The default value is Flat Top.NameValueDescriptionRFMXSPECAN_VAL_SPUR_FFT_WINDOW_NONE0 (0x0)Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes.RFMXSPECAN_VAL_SPUR_FFT_WINDOW_FLAT_TOP1 (0x1)Measures single-tone amplitudes accurately.RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HANNING2 (0x2)Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements.RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HAMMING3 (0x3)Analyzes closely-spaced sine waves.RFMXSPECAN_VAL_SPUR_FFT_WINDOW_GAUSSIAN4 (0x4)Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis.RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN5 (0x5)Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate.RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN_HARRIS6 (0x6)Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe.RFMXSPECAN_VAL_SPUR_FFT_WINDOW_KAISER_BESSEL7 (0x7)Separates two tones with frequencies close to each other but with widely-differing amplitudes. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_NONE | 0 (0x0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_FLAT_TOP | 1 (0x1) | Measures single-tone amplitudes accurately. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HANNING | 2 (0x2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_HAMMING | 3 (0x3) | Analyzes closely-spaced sine waves. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_GAUSSIAN | 4 (0x4) | Provides a balance of spectral leakage, frequency resolution, and amplitude attenuation. This windowing is useful for time-frequency analysis. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN | 5 (0x5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_BLACKMAN_HARRIS | 6 (0x6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |  |
| RFMXSPECAN_VAL_SPUR_FFT_WINDOW_KAISER_BESSEL | 7 (0x7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga60355649b34e507518723ffea855ae7b.html language=enus -->
## TOPIC 00465: RFmxSpecAn_SpurCfgRangeNumberOfSpursToReport

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga60355649b34e507518723ffea855ae7b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga60355649b34e507518723ffea855ae7b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of Spurs that the measurement should report in the frequency range. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgRangeNumberOfSpursToReport(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfSpursToReport)RemarksUse "range< <i> n </i> >" as the selector string t

### RFmxSpecAn_SpurCfgRangeNumberOfSpursToReport

Specifies the number of Spurs that the measurement should report in the frequency range.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgRangeNumberOfSpursToReport(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfSpursToReport)

#### Remarks

Use "range< 
<i> 
n 
</i> 
>" as the selector string to configure this function.

**Supported devices:** PXIe-5665, PXIe-5668

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0".Example:"range0""signal::sig1/range0"You can use the RFmxSpecAn_BuildRangeString2 function to build the selector string. |
| numberOfSpursToReport | [in] | int32 | This parameter specifies the number of Spurs that the measurement should report in the frequency range. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga64cd8d7192b094560204d06bf2e5ded3.html language=enus -->
## TOPIC 00466: RFmxSpecAn_SpurCfgRangeFrequency

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga64cd8d7192b094560204d06bf2e5ded3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga64cd8d7192b094560204d06bf2e5ded3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency start and stop values of the range. Use "range<n>" as the selector string to configure this function. Supported devices: PXIe-5665, PXIe-5668. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgRangeFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 startFrequ

### RFmxSpecAn_SpurCfgRangeFrequency

Configures the frequency start and stop values of the range. Use "range<n>" as the selector string to configure this function. **Supported devices:** PXIe-5665, PXIe-5668.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgRangeFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 startFrequency, float64 stopFrequency, int32 rangeEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0".Example:"range0""signal::sig1/range0"You can use the RFmxSpecAn_BuildRangeString2 function to build the selector string. |
| startFrequency | [in] | float64 | This parameter specifies the start of the frequency range, in Hz, for the measurement. The default value is 500 MHz. |
| stopFrequency | [in] | float64 | This parameter specifies the stop of the frequency range, in Hz, for the measurement. The default value is 1.5 GHz. |
| rangeEnabled | [in] | int32 | This parameter specifies whether to measure the Spurs in the frequency range. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SPUR_RANGE_ENABLED_FALSE0 (0x0)Disables the acquisition of the frequency range.RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_TRUE1 (0x1)Enables measurement of Spurs in the frequency range. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_FALSE | 0 (0x0) | Disables the acquisition of the frequency range. |  |
| RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_TRUE | 1 (0x1) | Enables measurement of Spurs in the frequency range. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga682d5411c1a954f456eee0dc9bd1c6dd.html language=enus -->
## TOPIC 00467: RFmxSpecAn_SpurCfgRangePeakCriteria

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga682d5411c1a954f456eee0dc9bd1c6dd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga682d5411c1a954f456eee0dc9bd1c6dd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur). Syntaxint32 __stdcall RFmxSpecAn_SpurCfgRangePeakCriteria(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 threshold, float64 excursion)RemarksUse "ran

### RFmxSpecAn_SpurCfgRangePeakCriteria

Configures the peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur).

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgRangePeakCriteria(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 threshold, float64 excursion)

#### Remarks

Use "range< 
<i> 
n 
</i> 
>" as the selector string to configure this function.

**Supported devices:** PXIe-5665, PXIe-5668

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0".Example:"range0""signal::sig1/range0"You can use the RFmxSpecAn_BuildRangeString2 function to build the selector string. |
| threshold | [in] | float64 | This parameter specifies the threshold level, in dBm, above which the measurement detects spurs in the range. The default value is -200. |
| excursion | [in] | float64 | This parameter specifies the peak excursion to be used when spur detection is performed. The default value is 6.Refer to the Phase Noise topic for more information on spur removal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga8245d89eb44d24da6cac1609dfa8c8cd.html language=enus -->
## TOPIC 00468: RFmxSpecAn_SpurCfgRangeAbsoluteLimit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga8245d89eb44d24da6cac1609dfa8c8cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1ga8245d89eb44d24da6cac1609dfa8c8cd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the absolute power limits corresponding to the beginning and end of the frequency range. Use "range<n>" as the selector string to configure this function. Supported devices: PXIe-5665, PXIe-5668. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgRangeAbsoluteLimit(niRFmxInstrHandle instrumentHandle

### RFmxSpecAn_SpurCfgRangeAbsoluteLimit

Configures the absolute power limits corresponding to the beginning and end of the frequency range. Use "range<n>" as the selector string to configure this function. **Supported devices:** PXIe-5665, PXIe-5668.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgRangeAbsoluteLimit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 absoluteLimitMode, float64 absoluteLimitStart, float64 absoluteLimitStop)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and range number. If you do not specify the signal name, the default signal instance is used. The default value is "range0".Example:"range0""signal::sig1/range0"You can use the RFmxSpecAn_BuildRangeString2 function to build the selector string. |
| absoluteLimitMode | [in] | int32 | This parameter specifies whether the absolute limit threshold is a flat line or a line with a slope. The default value is Couple.NameValueDescriptionRFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_MANUAL0 (0x0)The line specified by the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_START and RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOP attribute values as the two ends is considered as the threshold.RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_COUPLE1 (0x1)The two ends of the line are coupled to the value of the Spur Range Abs Limit Start attribute. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_MANUAL | 0 (0x0) | The line specified by the RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_START and RFMXSPECAN_ATTR_SPUR_RANGE_ABSOLUTE_LIMIT_STOP attribute values as the two ends is considered as the threshold. |  |
| RFMXSPECAN_VAL_SPUR_ABSOLUTE_LIMIT_MODE_COUPLE | 1 (0x1) | The two ends of the line are coupled to the value of the Spur Range Abs Limit Start attribute. |  |
| absoluteLimitStart | [in] | float64 | This parameter specifies the absolute power limit, in dBm, corresponding to the beginning of the frequency range. The value of this parameter is also set as the absolute power limit for the range when you set the Absolute Limit Mode parameter to Couple. The default value is -10. |
| absoluteLimitStop | [in] | float64 | This parameter specifies the absolute power limit, in dBm, corresponding to the end of the frequency range. This parameter is ignored when you set the Absolute Limit Mode parameter to Couple. The default value is -10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gaa48436a85d64b5bb38750f96163171fb.html language=enus -->
## TOPIC 00469: RFmxSpecAn_SpurCfgNumberOfRanges

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gaa48436a85d64b5bb38750f96163171fb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gaa48436a85d64b5bb38750f96163171fb.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of ranges. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgNumberOfRanges(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfRanges)Remarks Supported devices: PXIe-5665, PXIe-5668ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxSpecAn_SpurCfgNumberOfRanges

Configures the number of ranges.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgNumberOfRanges(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfRanges)

#### Remarks

**Supported devices:** PXIe-5665, PXIe-5668

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| numberOfRanges | [in] | int32 | This parameter specifies the number of ranges. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gaf29b666b4bc1d8aa409f43110a78747c.html language=enus -->
## TOPIC 00470: RFmxSpecAn_SpurCfgTraceRangeIndex

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gaf29b666b4bc1d8aa409f43110a78747c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gaf29b666b4bc1d8aa409f43110a78747c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the index of the range used to store and retrieve the spurious emission (Spur) trace. Supported devices: PXIe-5665, PXIe-5668. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgTraceRangeIndex(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 traceRangeIndex)ParametersNameDirectionTyp

### RFmxSpecAn_SpurCfgTraceRangeIndex

Specifies the index of the range used to store and retrieve the spurious emission (Spur) trace. **Supported devices:** PXIe-5665, PXIe-5668.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgTraceRangeIndex(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 traceRangeIndex)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| traceRangeIndex | [in] | int32 | This parameter specifies the index of the range used to store and retrieve Spur traces. This parameter is not used if you set the RFMXSPECAN_ATTR_SPUR_ALL_TRACES_ENABLED to FALSE. When you set this parameter to -1, the measurement stores and retrieves traces for all enabled ranges. The default value is -1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gafa383efd2b6a6a87e84ebbb2ae180657.html language=enus -->
## TOPIC 00471: RFmxSpecAn_SpurCfgAveraging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gafa383efd2b6a6a87e84ebbb2ae180657.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur_1gafa383efd2b6a6a87e84ebbb2ae180657.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the spurious emission (Spur) measurement. Supported devices: PXIe-5665, PXIe-5668. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDir

### RFmxSpecAn_SpurCfgAveraging

Configures averaging for the spurious emission (Spur) measurement. **Supported devices:** PXIe-5665, PXIe-5668.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_TRUE1 (0x1)The Spur measurement uses the RFMXSPECAN_ATTR_SPUR_AVERAGING_COUNT attribute as the number of acquisitions over which the Spur measurement is averaged. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_ENABLED_TRUE | 1 (0x1) | The Spur measurement uses the RFMXSPECAN_ATTR_SPUR_AVERAGING_COUNT attribute as the number of acquisitions over which the Spur measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectral Measurements Concepts topic for more information about averaging types. The default value is RMS.NameValueDescriptionRFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MAXIMUM3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MINIMUM4 (0x4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_SPUR_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Spur

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1ga1616366a270bae84f4c013970f5ce259.html language=enus -->
## TOPIC 00472: RFmxSpecAn_SpurCfgRangeFrequencyArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1ga1616366a270bae84f4c013970f5ce259.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1ga1616366a270bae84f4c013970f5ce259.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency start and stop values and specifies whether to enable measurement of the spurious emissions (Spur) in the frequency range. Supported devices: PXIe-5665, PXIe-5668. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgRangeFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorSt

### RFmxSpecAn_SpurCfgRangeFrequencyArray

Configures the frequency start and stop values and specifies whether to enable measurement of the spurious emissions (Spur) in the frequency range. **Supported devices:** PXIe-5665, PXIe-5668.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgRangeFrequencyArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 startFrequency[], float64 stopFrequency[], int32 rangeEnabled[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| startFrequency | [in] | float64[] | This parameter specifies the array of start frequencies of the frequency range, in Hz, for the measurement. The default value is 500 MHz. |
| stopFrequency | [in] | float64[] | This parameter specifies the array of stop frequencies of the frequency range, in Hz, for the measurement. The default value is 1.5 GHz. |
| rangeEnabled | [in] | int32[] | This parameter specifies whether to measure the Spur in the frequency range. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SPUR_RANGE_ENABLED_FALSE0 (0x0)Disables the acquisition of the frequency range.RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_TRUE1 (0x1)Enables measurement of Spurs in the frequency range. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_FALSE | 0 (0x0) | Disables the acquisition of the frequency range. |  |
| RFMXSPECAN_VAL_SPUR_RANGE_ENABLED_TRUE | 1 (0x1) | Enables measurement of Spurs in the frequency range. |  |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1ga92885a5701bc51493fd92496fd3fa711.html language=enus -->
## TOPIC 00473: RFmxSpecAn_SpurCfgRangeVBWFilterArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1ga92885a5701bc51493fd92496fd3fa711.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1ga92885a5701bc51493fd92496fd3fa711.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the VBW settings, including VBW Auto, VBW, and VBW to RBW ratio for the specified range. Syntaxint32 __stdcall RFmxSpecAn_SpurCfgRangeVBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 vbwAuto[], float64 vbw[], float64 vbwToRBWRatio[], int32 number

### RFmxSpecAn_SpurCfgRangeVBWFilterArray

Configures an array of the VBW settings, including VBW Auto, VBW, and VBW to RBW ratio for the specified range.

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgRangeVBWFilterArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 vbwAuto[], float64 vbw[], float64 vbwToRBWRatio[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| vbwAuto | [in] | int32[] | This parameter specifies whether the VBW is expressed directly or computed based on VBW to RBW ratio. The default value is True.NameValueDescriptionRFMXSPECAN_VAL_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH_FALSE0 (0x0)Specify the video bandwidth in the RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH attribute. The RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_VBW_TO_RBW_RATIO attribute is disregarded in this mode.RFMXSPECAN_VAL_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH_TRUE1 (0x1)Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH attribute and the RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH attribute. The value of the RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH attribute is disregarded in this mode. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | Specify the video bandwidth in the RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH attribute. The RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_VBW_TO_RBW_RATIO attribute is disregarded in this mode. |  |
| RFMXSPECAN_VAL_SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | Specify video bandwidth in terms of the VBW to RBW ratio. The value of the video bandwidth is then computed by using the RFMXSPECAN_ATTR_SPUR_RANGE_RBW_FILTER_BANDWIDTH attribute and the RFMXSPECAN_ATTR_TXP_RBW_FILTER_BANDWIDTH attribute. The value of the RFMXSPECAN_ATTR_SPUR_RANGE_VBW_FILTER_BANDWIDTH attribute is disregarded in this mode. |  |
| vbw | [in] | float64[] | This parameter specifies the video bandwidth when you set the VBW Auto parameter to False. This value is expressed in Hz. The default value is 30KHz. |
| vbwToRBWRatio | [in] | float64[] | This parameter specifies the VBW to RBW Ratio when you set the VBW Auto parameter to True. The default value is 3. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1gaf8cec103ac51c543d3e605e946c18dfa.html language=enus -->
## TOPIC 00474: RFmxSpecAn_SpurCfgRangePeakCriteriaArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1gaf8cec103ac51c543d3e605e946c18dfa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__spur__array_1gaf8cec103ac51c543d3e605e946c18dfa.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures arrays of peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur). Syntaxint32 __stdcall RFmxSpecAn_SpurCfgRangePeakCriteriaArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 threshold[], float64 excursion[],

### RFmxSpecAn_SpurCfgRangePeakCriteriaArray

Configures arrays of peak threshold and peak excursion criteria which a peak should meet to be classified as a spurious emission (Spur).

#### Syntax

int32 __stdcall RFmxSpecAn_SpurCfgRangePeakCriteriaArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 threshold[], float64 excursion[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| threshold | [in] | float64[] | This parameter specifies the array of threshold levels, in dBm, above which the measurement detects spurs in the range. The default value is -200. |
| excursion | [in] | float64[] | This parameter specifies the array of peak excursion values, in dB, used to find the spurs in the spectrum. The signal should rise and fall by at least the peak excursion value, above the threshold, to be considered as a spur. The default value is 0. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Array

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga01ad23e3c1858acffa810f056c93a81e.html language=enus -->
## TOPIC 00475: RFmxSpecAn_CfgDigitalEdgeTrigger

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga01ad23e3c1858acffa810f056c93a81e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga01ad23e3c1858acffa810f056c93a81e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxSpecAn_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enab

### RFmxSpecAn_CfgDigitalEdgeTrigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxSpecAn_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Remarks

Spectral measurements are sometimes implemented with multiple acquisitions and therefore will require that digital triggers are sent for each acquisition. Multiple factors, including the desired span versus the realtime bandwidth of the hardware, affect the number of acquisitions. RFmx recommends repeating the generation until the measurement is completed in order to ensure that all the acquisitions are triggered.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital edge trigger. The default of this attribute is hardware dependent.Name (Value)DescriptionPFI0 (PFI0)The trigger is received on PFI 0.PFI1 (PFI1)The trigger is received on PFI 1.PXI_Trig0 (PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1 (PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2 (PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3 (PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4 (PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5 (PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6 (PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7 (PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR (PXI_STAR)The trigger is received on the PXI star trigger line.PXIe_DStarB (PXIe_DStarB )The trigger is received on the PXIe DStar B trigger line.TimerEvent (TimerEvent)The trigger is received from the timer event. |
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
| PXIe_DStarB (PXIe_DStarB ) | The trigger is received on the PXIe DStar B trigger line. |  |  |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |  |  |
| digitalEdge | [in] | int32 | This parameter specifies the trigger edge to detect. The default value is Rising Edge.NameValueDescriptionRFMXSPECAN_VAL_DIGITAL_EDGE_RISING_EDGE0 (0x0)The trigger asserts on the rising edge of the signal.RFMXSPECAN_VAL_DIGITAL_EDGE_FALLING_EDGE1 (0x1)The trigger asserts on the falling edge of the signal. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |  |
| RFMXSPECAN_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga49ef9339d126ac2962f0858b3936adea.html language=enus -->
## TOPIC 00476: RFmxSpecAn_DisableTrigger

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga49ef9339d126ac2962f0858b3936adea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga49ef9339d126ac2962f0858b3936adea.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxSpecAn_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrum

### RFmxSpecAn_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxSpecAn_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga73049b253e63b01b7f70a938db0ec04a.html language=enus -->
## TOPIC 00477: RFmxSpecAn_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga73049b253e63b01b7f70a938db0ec04a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1ga73049b253e63b01b7f70a938db0ec04a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. Syntaxint32 __stdcall RFmxSpecAn_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], float64

### RFmxSpecAn_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxSpecAn_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], float64 iqPowerEdgeLevel, int32 iqPowerEdgeSlope, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 enableTrigger)

#### Remarks

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. The default of this attribute is hardware dependent. |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this attribute is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope.NameValueDescriptionRFMXSPECAN_VAL_IQ_POWER_EDGE_RISING_SLOPE0 (0x0)The trigger asserts when the signal power is rising.RFMXSPECAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE1 (0x1)The trigger asserts when the signal power is falling. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |  |
| RFMXSPECAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| triggerMinQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual.NameValueDescriptionRFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL0 (0x0)The minimum quiet time for triggering is the value of the RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute.RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO1 (0x1)The measurement computes the minimum quiet time used for triggering. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXSPECAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |  |
| RFMXSPECAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |  |
| triggerMinQuietTimeDuration | [in] | float64 | This parameter specifies the duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q Power Edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this attribute is hardware dependent. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1gab11fb2033d263d6fc3f51cfa26bd2047.html language=enus -->
## TOPIC 00478: RFmxSpecAn_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1gab11fb2033d263d6fc3f51cfa26bd2047.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__trigger_1gab11fb2033d263d6fc3f51cfa26bd2047.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxSpecAn_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescription

### RFmxSpecAn_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxSpecAn_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__txp.html language=enus -->
## TOPIC 00479: TXP

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__txp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__txp.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_TXPCfgAveragingConfigures averaging for the transmit power (TXP) measurement. RFmxSpecAn_TXPCfgMeasurementIntervalSpecifies the acquisition time, in seconds, for the transmit power (TXP) measurement. RFmxSpecAn_TXPCfgRBWFilterConfigures the resolution

### TXP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_TXPCfgAveraging | Configures averaging for the transmit power (TXP) measurement. |
| RFmxSpecAn_TXPCfgMeasurementInterval | Specifies the acquisition time, in seconds, for the transmit power (TXP) measurement. |
| RFmxSpecAn_TXPCfgRBWFilter | Configures the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter. |
| RFmxSpecAn_TXPCfgThreshold | Configures the threshold level for the samples that need to be considered for the transmit power (TXP) measurement. Enable the threshold when analyzing burst signals or signals with dead time. |
| RFmxSpecAn_TXPCfgVBWFilter | Configures VBW settings including the VBW mode, video bandwidth (VBW), and the VBW to RBW ratio. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__txp_1ga03d3963743f0232932c8583f46c02531.html language=enus -->
## TOPIC 00480: RFmxSpecAn_TXPCfgMeasurementInterval

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__txp_1ga03d3963743f0232932c8583f46c02531.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__txp_1ga03d3963743f0232932c8583f46c02531.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition time, in seconds, for the transmit power (TXP) measurement. Syntaxint32 __stdcall RFmxSpecAn_TXPCfgMeasurementInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInst

### RFmxSpecAn_TXPCfgMeasurementInterval

Specifies the acquisition time, in seconds, for the transmit power (TXP) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_TXPCfgMeasurementInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| measurementInterval | [in] | float64 | This parameter specifies the acquisition time, in seconds, for the measurement. The default value is 1 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__txp_1ga983d4a42c9fc6e1280aa3912e33e3862.html language=enus -->
## TOPIC 00481: RFmxSpecAn_TXPCfgAveraging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__txp_1ga983d4a42c9fc6e1280aa3912e33e3862.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__txp_1ga983d4a42c9fc6e1280aa3912e33e3862.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the transmit power (TXP) measurement. Syntaxint32 __stdcall RFmxSpecAn_TXPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFm

### RFmxSpecAn_TXPCfgAveraging

Configures averaging for the transmit power (TXP) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_TXPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_TXP_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXSPECAN_VAL_TXP_AVERAGING_ENABLED_TRUE1 (0x1)The TXP measurement uses the RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT attribute as the number of acquisitions over which the TXP measurement is averaged. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_TXP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXSPECAN_VAL_TXP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The TXP measurement uses the RFMXSPECAN_ATTR_TXP_AVERAGING_COUNT attribute as the number of acquisitions over which the TXP measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging the power over multiple acquisitions. The averaged power trace is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS.NameValueDescriptionRFMXSPECAN_VAL_TXP_AVERAGING_TYPE_RMS0 (0x0)The power trace is linearly averaged.RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_LOG1 (0x1)The power trace is averaged in a logarithmic scale.RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power trace is averaged.RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_MAXIMUM3 (0x3)The maximum instantaneous power in the power trace is retained from one acquisition to the next.RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_MINIMUM4 (0x4)The minimum instantaneous power in the power trace is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_RMS | 0 (0x0) | The power trace is linearly averaged. |  |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_LOG | 1 (0x1) | The power trace is averaged in a logarithmic scale. |  |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power trace is averaged. |  |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The maximum instantaneous power in the power trace is retained from one acquisition to the next. |  |
| RFMXSPECAN_VAL_TXP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The minimum instantaneous power in the power trace is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__txp_1gac988c0e6be933086caf92a490480be7e.html language=enus -->
## TOPIC 00482: RFmxSpecAn_TXPCfgRBWFilter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__txp_1gac988c0e6be933086caf92a490480be7e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__txp_1gac988c0e6be933086caf92a490480be7e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter. Syntaxint32 __stdcall RFmxSpecAn_TXPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 rbw, int32 rbwFilterType, float64 rrcAlpha)ParametersNameDirectionTypeD

### RFmxSpecAn_TXPCfgRBWFilter

Configures the resolution bandwidth (RBW) filter to measure the power of the signal as seen through this filter.

#### Syntax

int32 __stdcall RFmxSpecAn_TXPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 rbw, int32 rbwFilterType, float64 rrcAlpha)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| rbw | [in] | float64 | This parameter specifies the bandwidth, in Hz, of the resolution bandwidth (RBW) filter used to measure the signal. The default value is 100 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)The RBW filter has a Gaussian response.RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_FLAT2 (0x2)The RBW filter has a flat response.RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_NONE5 (0x5)The measurement does not use any RBW filtering.RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_RRC6 (0x6)The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHA attribute is used as the RBW filter. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |  |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |  |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_NONE | 5 (0x5) | The measurement does not use any RBW filtering. |  |
| RFMXSPECAN_VAL_TXP_RBW_FILTER_TYPE_RRC | 6 (0x6) | The RRC filter with the roll-off specified by the RFMXSPECAN_ATTR_TXP_RBW_FILTER_ALPHA attribute is used as the RBW filter. |  |
| rrcAlpha | [in] | float64 | This parameter specifies the roll-off factor for the root-raised-cosine (RRC) filter. The default value is 0.1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__configuration__txp_1gaf71137f2611e7fb7b8977059b2d41b56.html language=enus -->
## TOPIC 00483: RFmxSpecAn_TXPCfgThreshold

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__configuration__txp_1gaf71137f2611e7fb7b8977059b2d41b56.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__configuration__txp_1gaf71137f2611e7fb7b8977059b2d41b56.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the threshold level for the samples that need to be considered for the transmit power (TXP) measurement. Enable the threshold when analyzing burst signals or signals with dead time. Syntaxint32 __stdcall RFmxSpecAn_TXPCfgThreshold(niRFmxInstrHandle instrumentHandle, char selectorString[],

### RFmxSpecAn_TXPCfgThreshold

Configures the threshold level for the samples that need to be considered for the transmit power (TXP) measurement. Enable the threshold when analyzing burst signals or signals with dead time.

#### Syntax

int32 __stdcall RFmxSpecAn_TXPCfgThreshold(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 thresholdEnabled, float64 thresholdLevel, int32 thresholdType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| thresholdEnabled | [in] | int32 | This parameter specifies whether to enable thresholding of the acquired samples to be used for the measurement. The default value is False.NameValueDescriptionRFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_FALSE0 (0x0)All the acquired samples are considered for the TXP measurement.RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_TRUE1 (0x1)The samples above the threshold level specified in the RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL attribute are considered for the TXP measurement. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_FALSE | 0 (0x0) | All the acquired samples are considered for the TXP measurement. |  |
| RFMXSPECAN_VAL_TXP_THRESHOLD_ENABLED_TRUE | 1 (0x1) | The samples above the threshold level specified in the RFMXSPECAN_ATTR_TXP_THRESHOLD_LEVEL attribute are considered for the TXP measurement. |  |
| thresholdLevel | [in] | float64 | This parameter specifies either the relative or absolute threshold power level based on the value of the Threshold Type parameter. The default value is -20 dB. |
| thresholdType | [in] | int32 | This parameter specifies the reference for the power level used for thresholding. The default value is Relative.NameValueDescriptionRFMXSPECAN_VAL_TXP_THRESHOLD_TYPE_RELATIVE0 (0x0)The threshold is relative to the peak power of the acquired samples.RFMXSPECAN_VAL_TXP_THRESHOLD_TYPE_ABSOLUTE1 (0x1)The threshold is the absolute power, in dBm. |
| Name | Value | Description |  |
| RFMXSPECAN_VAL_TXP_THRESHOLD_TYPE_RELATIVE | 0 (0x0) | The threshold is relative to the peak power of the acquired samples. |  |
| RFMXSPECAN_VAL_TXP_THRESHOLD_TYPE_ABSOLUTE | 1 (0x1) | The threshold is the absolute power, in dBm. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch.html language=enus -->
## TOPIC 00484: Fetch

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPAMPMApply DPDCCDFCHPDPDFCntHarmIDPDIMIQNFOBWPAVTPhaseNoisePowerListSEMSpectrumSpurTXPGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- ACP
- AMPM
- Apply DPD
- CCDF
- CHP
- DPD
- FCnt
- Harm
- IDPD
- IM
- IQ
- NF
- OBW
- PAVT
- PhaseNoise
- PowerList
- SEM
- Spectrum
- Spur
- TXP

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp.html language=enus -->
## TOPIC 00485: ACP

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_ACPFetchAbsolutePowersTraceFetches the absolute powers trace for adjacent channel power (ACP) measurement. RFmxSpecAn_ACPFetchCarrierMeasurementReturns the measured carrier power. RFmxSpecAn_ACPFetchFrequencyResolutionReturns the frequency resolution,

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_ACPFetchAbsolutePowersTrace | Fetches the absolute powers trace for adjacent channel power (ACP) measurement. |
| RFmxSpecAn_ACPFetchCarrierMeasurement | Returns the measured carrier power. |
| RFmxSpecAn_ACPFetchFrequencyResolution | Returns the frequency resolution, in Hz, of the spectrum acquired by the measurement. |
| RFmxSpecAn_ACPFetchOffsetMeasurement | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. The relative powers are not measured if you set the RFMXSPECAN_ATTR_ACP_CARRIER_MODE attribute to Passive. |
| RFmxSpecAn_ACPFetchOffsetMeasurementArray | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. The relative powers are not measured if you set the RFMXSPECAN_ATTR_ACP_CARRIER_MODE attribute for the reference carrier to Passive. |
| RFmxSpecAn_ACPFetchRelativePowersTrace | Fetches the relative powers trace for adjacent channel power (ACP) measurement. |
| RFmxSpecAn_ACPFetchSpectrum | Fetches the spectrum used for adjacent channel power (ACP) measurement. |
| RFmxSpecAn_ACPFetchTotalCarrierPower | Fetches the total integrated power of all the active carriers measured when you set the RFMXSPECAN_ATTR_ACP_POWER_UNITS attribute to dBm. This function returns the power spectral density based on the power in all the active carriers measured when you set the ACP Power Units attribute to dBm/Hz. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga21588594fd45ee52f4f558b65324863d.html language=enus -->
## TOPIC 00486: RFmxSpecAn_ACPFetchRelativePowersTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga21588594fd45ee52f4f558b65324863d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga21588594fd45ee52f4f558b65324863d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for adjacent channel power (ACP) measurement. Syntaxint32 __stdcall RFmxSpecAn_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 ar

### RFmxSpecAn_ACPFetchRelativePowersTrace

Fetches the relative powers trace for adjacent channel power (ACP) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| relativePowersTrace | [out] | float32[] | This parameter returns the relative power, in dB, measured in each channel relative to power reference carrier. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga50d57edcc355f863c60e6871e18c6014.html language=enus -->
## TOPIC 00487: RFmxSpecAn_ACPFetchOffsetMeasurement

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga50d57edcc355f863c60e6871e18c6014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga50d57edcc355f863c60e6871e18c6014.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. The relative powers are not measured if you set the RFMXSPECAN_ATTR_ACP_CARRIER_MODE attribute to Passive. Syntaxint32 __stdcall

### RFmxSpecAn_ACPFetchOffsetMeasurement

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. The relative powers are not measured if you set the [RFMXSPECAN_ATTR_ACP_CARRIER_MODE](group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1ga86e939a2166da710ed615565009630f6.html) attribute to **Passive**.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerRelativePower, float64 *upperRelativePower, float64 *lowerAbsolutePower, float64 *upperAbsolutePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxSpecAn_BuildOffsetString2 function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64 * | This parameter returns the lower offset channel power, in dB, measured relative to the integrated power of the RFMXSPECAN_ATTR_ACP_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER attribute. |
| upperRelativePower | [out] | float64 * | This parameter returns the upper offset channel power, in dB, measured relative to the integrated power of the RFMXSPECAN_ATTR_ACP_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER attribute. |
| lowerAbsolutePower | [out] | float64 * | This parameter returns the lower offset channel power. |
| upperAbsolutePower | [out] | float64 * | This parameter returns the upper offset channel power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga5aa85c293efb8bbd7ff098667b996a36.html language=enus -->
## TOPIC 00488: RFmxSpecAn_ACPFetchOffsetMeasurementArray

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga5aa85c293efb8bbd7ff098667b996a36.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga5aa85c293efb8bbd7ff098667b996a36.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. The relative powers are not measured if you set the RFMXSPECAN_ATTR_ACP_CARRIER_MODE attribute for the reference carrier to Passi

### RFmxSpecAn_ACPFetchOffsetMeasurementArray

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier. The relative powers are not measured if you set the [RFMXSPECAN_ATTR_ACP_CARRIER_MODE](group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1ga86e939a2166da710ed615565009630f6.html) attribute for the reference carrier to **Passive**.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64[] | This parameter returns the array of lower offset channel powers, in dB, measured relative to the integrated power of the RFMXSPECAN_ATTR_ACP_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER attribute. |
| upperRelativePower | [out] | float64[] | This parameter returns the array of upper offset channel powers, in dB, measured relative to the integrated power of the RFMXSPECAN_ATTR_ACP_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER attribute. |
| lowerAbsolutePower | [out] | float64[] | This parameter returns the array of lower offset channel powers. |
| upperAbsolutePower | [out] | float64[] | This parameter returns the array of upper offset channel powers. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga5ef3e8570b8c518f0ba164479df7e30c.html language=enus -->
## TOPIC 00489: RFmxSpecAn_ACPFetchAbsolutePowersTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga5ef3e8570b8c518f0ba164479df7e30c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga5ef3e8570b8c518f0ba164479df7e30c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for adjacent channel power (ACP) measurement. Syntaxint32 __stdcall RFmxSpecAn_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 ar

### RFmxSpecAn_ACPFetchAbsolutePowersTrace

Fetches the absolute powers trace for adjacent channel power (ACP) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency of the channel. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| absolutePowersTrace | [out] | float32[] | This parameter returns the integrated power in dBm, or power spectral density in dBm/Hz, in the channel based on the power units specified. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga769f57530d6314381aacd6be1f433f3b.html language=enus -->
## TOPIC 00490: RFmxSpecAn_ACPFetchTotalCarrierPower

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga769f57530d6314381aacd6be1f433f3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1ga769f57530d6314381aacd6be1f433f3b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total integrated power of all the active carriers measured when you set the RFMXSPECAN_ATTR_ACP_POWER_UNITS attribute to dBm. This function returns the power spectral density based on the power in all the active carriers measured when you set the ACP Power Units attribute to dBm/Hz. Synt

### RFmxSpecAn_ACPFetchTotalCarrierPower

Fetches the total integrated power of all the active carriers measured when you set the [RFMXSPECAN_ATTR_ACP_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__acp_1gadd1a9ec0d09a6cbe69f9057850cf0477.html) attribute to **dBm**. This function returns the power spectral density based on the power in all the active carriers measured when you set the ACP Power Units attribute to **dBm/Hz**.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalCarrierPower | [out] | float64 * | This parameter returns the total integrated power of all the active carriers measured when you set the ACP Power Units attribute to dBm. This parameter returns the power spectral density based on the power in all the active carriers measured when you set the ACP Power Units attribute to dBm/Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gab93d2a2ab5ead2898e30122c4e729e53.html language=enus -->
## TOPIC 00491: RFmxSpecAn_ACPFetchSpectrum

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gab93d2a2ab5ead2898e30122c4e729e53.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gab93d2a2ab5ead2898e30122c4e729e53.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for adjacent channel power (ACP) measurement. Syntaxint32 __stdcall RFmxSpecAn_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDi

### RFmxSpecAn_ACPFetchSpectrum

Fetches the spectrum used for adjacent channel power (ACP) measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gae966bb5730798e86884dcd35d6fdce8e.html language=enus -->
## TOPIC 00492: RFmxSpecAn_ACPFetchCarrierMeasurement

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gae966bb5730798e86884dcd35d6fdce8e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gae966bb5730798e86884dcd35d6fdce8e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured carrier power. Syntaxint32 __stdcall RFmxSpecAn_ACPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *totalRelativePower, float64 *carrierOffset, float64 *integrationBandwidth)RemarksUse "carrier<

### RFmxSpecAn_ACPFetchCarrierMeasurement

Returns the measured carrier power.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *totalRelativePower, float64 *carrierOffset, float64 *integrationBandwidth)

#### Remarks

Use "carrier< 
<i> 
n 
</i> 
>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxSpecAn_BuildCarrierString2 function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64 * | This parameter returns the measured carrier power. The carrier power is reported in dBm or dBm/Hz based on the value of the RFMXSPECAN_ATTR_ACP_POWER_UNITS attribute. |
| totalRelativePower | [out] | float64 * | This parameter returns the carrier power, in dB, measured relative to the total carrier power of all active carriers. |
| carrierOffset | [out] | float64 * | This parameter returns the center frequency, in Hz, of the carrier relative to the RFMXSPECAN_ATTR_CENTER_FREQUENCY attribute. |
| integrationBandwidth | [out] | float64 * | This parameter returns the frequency range, in Hz, over which the measurement integrates the carrier power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gaecdec0019f2db697563cecb515ff92fe.html language=enus -->
## TOPIC 00493: RFmxSpecAn_ACPFetchFrequencyResolution

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gaecdec0019f2db697563cecb515ff92fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__acp_1gaecdec0019f2db697563cecb515ff92fe.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency resolution, in Hz, of the spectrum acquired by the measurement. Syntaxint32 __stdcall RFmxSpecAn_ACPFetchFrequencyResolution(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *frequencyResolution)ParametersNameDirectionTypeDescriptioninstrument

### RFmxSpecAn_ACPFetchFrequencyResolution

Returns the frequency resolution, in Hz, of the spectrum acquired by the measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_ACPFetchFrequencyResolution(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *frequencyResolution)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| frequencyResolution | [out] | float64 * | This parameter returns the frequency bin spacing, in Hz, of the spectrum acquired by the measurement. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm.html language=enus -->
## TOPIC 00494: AMPM

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxSpecAn_AMPMFetchAMToAMTraceFetches the AM to AM trace, where the Reference Powers array forms the x-axis of the trace; and the Measured AM to AM and Curve Fit AM to AM arrays form the y-axis of the trace. RFmxSpecAn_AMPMFetchAMToPMTraceFetches the AM to PM t

### AMPM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxSpecAn_AMPMFetchAMToAMTrace | Fetches the AM to AM trace, where the Reference Powers array forms the x-axis of the trace; and the Measured AM to AM and Curve Fit AM to AM arrays form the y-axis of the trace. |
| RFmxSpecAn_AMPMFetchAMToPMTrace | Fetches the AM to PM trace, where the Reference Powers array forms the x-axis of the trace; and the Measured AM to PM and Curve Fit AM to PM arrays form the y-axis of the trace. |
| RFmxSpecAn_AMPMFetchCompressionPoints | Fetches the compression points. |
| RFmxSpecAn_AMPMFetchCurveFitCoefficients | Fetches the coefficients of the polynomials that approximate the AM-to-AM and AM-to-PM responses of the device under test. |
| RFmxSpecAn_AMPMFetchCurveFitResidual | Fetches the polynomial approximation residuals for AM-to-AM and AM-to-PM response of the device under test. |
| RFmxSpecAn_AMPMFetchDUTCharacteristics | Fetches the mean linear gain, 1 dB compression point, and mean RMS EVM of the DUT. |
| RFmxSpecAn_AMPMFetchError | Fetches the maximum gain error range, phase error range, and mean phase error for the DUT. |
| RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveform | Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement. |
| RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveformSplit | Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement. |
| RFmxSpecAn_AMPMFetchProcessedReferenceWaveform | Fetches the segment of the reference waveform used to perform the AMPM measurement. |
| RFmxSpecAn_AMPMFetchProcessedReferenceWaveformSplit | Fetches the segment of the reference waveform used to perform the AMPM measurement. |
| RFmxSpecAn_AMPMFetchRelativePhaseTrace | Fetches the phase of the processed mean acquired waveform relative to the processed reference waveform. |
| RFmxSpecAn_AMPMFetchRelativePowerTrace | Fetches the power of the processed mean acquired waveform relative to the processed reference waveform. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga076fa1ab182b5be8efadbf241d3ff043.html language=enus -->
## TOPIC 00495: RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveformSplit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga076fa1ab182b5be8efadbf241d3ff043.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga076fa1ab182b5be8efadbf241d3ff043.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *

### RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveformSplit

Fetches the averaged acquired waveform, corrected for frequency, phase and DC offsets, used to perform the AMPM measurement.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 processedMeanAcquiredWaveformI[], float32 processedMeanAcquiredWaveformQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| processedMeanAcquiredWaveformI | [out] | float32[] | This parameter Returns the real part of complex baseband samples, in volts. |
| processedMeanAcquiredWaveformQ | [out] | float32[] | This parameter Returns the imaginary part of complex baseband samples, in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga1ffb36b8a9a2febbdf6d2c7bfd10350f.html language=enus -->
## TOPIC 00496: RFmxSpecAn_AMPMFetchRelativePowerTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga1ffb36b8a9a2febbdf6d2c7bfd10350f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga1ffb36b8a9a2febbdf6d2c7bfd10350f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power of the processed mean acquired waveform relative to the processed reference waveform. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchRelativePowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 relativePower[], int32 ar

### RFmxSpecAn_AMPMFetchRelativePowerTrace

Fetches the power of the processed mean acquired waveform relative to the processed reference waveform.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchRelativePowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| relativePower | [out] | float32[] | This parameter returns the instantaneous relative power, in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga479930e14b096a7e72543ee212a80c5a.html language=enus -->
## TOPIC 00497: RFmxSpecAn_AMPMFetchAMToPMTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga479930e14b096a7e72543ee212a80c5a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga479930e14b096a7e72543ee212a80c5a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the AM to PM trace, where the Reference Powers array forms the x-axis of the trace; and the Measured AM to PM and Curve Fit AM to PM arrays form the y-axis of the trace. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchAMToPMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 t

### RFmxSpecAn_AMPMFetchAMToPMTrace

Fetches the AM to PM trace, where the **Reference Powers** array forms the x-axis of the trace; and the **Measured AM to PM** and **Curve Fit AM to PM** arrays form the y-axis of the trace.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchAMToPMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 referencePowers[], float32 measuredAMToPM[], float32 curveFitAMToPM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| referencePowers | [out] | float32[] | This parameter returns the array of reference powers. This value is expressed in dBm.Reference Powers are the instantaneous powers at the input port of the DUT when you set the RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE attribute to Input, and Reference Powers are the instantaneous powers at the output port of the DUT when you set the AMPM Ref Pwr Type attribute to Output. |
| measuredAMToPM | [out] | float32[] | This parameter returns the polynomial fit phase distortion values corresponding to the reference powers. This value is expressed in degrees. |
| curveFitAMToPM | [out] | float32[] | This parameter returns the phase distortion values corresponding to the reference powers. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga5100cf1bd5487a092121e043c85bcffe.html language=enus -->
## TOPIC 00498: RFmxSpecAn_AMPMFetchRelativePhaseTrace

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga5100cf1bd5487a092121e043c85bcffe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga5100cf1bd5487a092121e043c85bcffe.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase of the processed mean acquired waveform relative to the processed reference waveform. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchRelativePhaseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 relativePhase[], int32 ar

### RFmxSpecAn_AMPMFetchRelativePhaseTrace

Fetches the phase of the processed mean acquired waveform relative to the processed reference waveform.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchRelativePhaseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 relativePhase[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| relativePhase | [out] | float32[] | This parameter returns the instantaneous relative phase. This value is expressed in degree. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga823916193fba4829bc901001095f53e4.html language=enus -->
## TOPIC 00499: RFmxSpecAn_AMPMFetchDUTCharacteristics

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga823916193fba4829bc901001095f53e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga823916193fba4829bc901001095f53e4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean linear gain, 1 dB compression point, and mean RMS EVM of the DUT. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchDUTCharacteristics(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanLinearGain, float64 *onedBCompressionPoint, float64 *meanRMSEVM)Par

### RFmxSpecAn_AMPMFetchDUTCharacteristics

Fetches the mean linear gain, 1 dB compression point, and mean RMS EVM of the DUT.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchDUTCharacteristics(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanLinearGain, float64 *onedBCompressionPoint, float64 *meanRMSEVM)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanLinearGain | [out] | float64 * | This parameter returns the average linear gain, in dB, of the device under test, computed by rejecting signal samples suffering gain compression. |
| onedBCompressionPoint | [out] | float64 * | This parameter returns the theoretical output power, in dBm, at which gain of the device under test drops by 1 dB from its mean linear gain. This parameter returns NaN when the AM-to-AM characteristics of the device under test are flat. |
| meanRMSEVM | [out] | float64 * | This parameter returns the ratio, as a percentage, of l2 norm of difference between the normalized reference and acquired waveforms, to the l2 norm of the normalized reference waveform. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga832ffc07ed686585beb9d43bbf1d9e64.html language=enus -->
## TOPIC 00500: RFmxSpecAn_AMPMFetchCurveFitCoefficients

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga832ffc07ed686585beb9d43bbf1d9e64.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__functions__fetch__ampm_1ga832ffc07ed686585beb9d43bbf1d9e64.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the coefficients of the polynomials that approximate the AM-to-AM and AM-to-PM responses of the device under test. Syntaxint32 __stdcall RFmxSpecAn_AMPMFetchCurveFitCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 amToAMCoefficients[], float32

### RFmxSpecAn_AMPMFetchCurveFitCoefficients

Fetches the coefficients of the polynomials that approximate the AM-to-AM and AM-to-PM responses of the device under test.

#### Syntax

int32 __stdcall RFmxSpecAn_AMPMFetchCurveFitCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 amToAMCoefficients[], float32 amToPMCoefficients[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxSpecAn_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| amToAMCoefficients | [out] | float32[] | This parameter returns the coefficients of the polynomial that approximates the AM-to-AM characteristic of the device under test. |
| amToPMCoefficients | [out] | float32[] | This parameter returns the coefficients of the polynomial that approximates the AM-to-PM characteristic of the device under test. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxSpecAn_GetError](group____root__ni_r_fmx_spec_an__functions_1gae89188af832ecaa1a37a01299cea95e7.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

AMPM
