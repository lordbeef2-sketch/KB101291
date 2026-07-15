# NI DOCUMENT BUNDLE: ni-dmm-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-c-api-ref start=1 end=96 -->
<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-DMM C API Reference

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-DMM C API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes_1gadee0cc512f455c271e35df26483dd65c.html language=enus -->
## TOPIC 00002: NIDMM_ATTR_IO_SESSION

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes_1gadee0cc512f455c271e35df26483dd65c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes_1gadee0cc512f455c271e35df26483dd65c.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The I/O session used to communicate with the instrument. SyntaxNIDMM_ATTR_IO_SESSIONNumeric ValueData TypeAccessApplies To1050322ViSessionRead-OnlyN/A

### NIDMM_ATTR_IO_SESSION

The I/O session used to communicate with the instrument.

#### Syntax

NIDMM_ATTR_IO_SESSION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050322 | ViSession | Read-Only | N/A |

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration.html language=enus -->
## TOPIC 00003: Configuration

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedMeasurement OptionsGroup membersNameDescriptionNIDMM_ATTR_AUTO_RANGE_VALUESpecifies the value of the range. If auto ranging is enabled, shows the actual value of the active range. The value of this attribute is set during a read operation. NIDMM_ATTR_FUNCTIONSpecifies the measurement f

### Configuration

#### Groups

- Advanced
- Measurement Options

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_AUTO_RANGE_VALUE | Specifies the value of the range. If auto ranging is enabled, shows the actual value of the active range. The value of this attribute is set during a read operation. |
| NIDMM_ATTR_FUNCTION | Specifies the measurement function. |
| NIDMM_ATTR_RANGE | Specifies the measurement range. Use positive values to represent the absolute value of the maximum expected measurement. The value is in units appropriate for the current value of the NIDMM_ATTR_FUNCTION attribute. For example, if NIDMM_ATTR_FUNCTION is set to NIDMM_VAL_DC_VOLTS, the units are volts. |
| NIDMM_ATTR_RESOLUTION_ABSOLUTE | Specifies the measurement resolution in absolute units. Setting this attribute to higher values increases the measurement accuracy. Setting this attribute to lower values increases the measurement speed. |
| NIDMM_ATTR_RESOLUTION_DIGITS | Specifies the measurement resolution in digits. Setting this attribute to higher values increases the measurement accuracy. Setting this attribute to lower values increases the measurement speed. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration_1ga00623fb2f436640440f40d4f7f16d3db.html language=enus -->
## TOPIC 00004: NIDMM_ATTR_RANGE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration_1ga00623fb2f436640440f40d4f7f16d3db.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration_1ga00623fb2f436640440f40d4f7f16d3db.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement range. Use positive values to represent the absolute value of the maximum expected measurement. The value is in units appropriate for the current value of the NIDMM_ATTR_FUNCTION attribute. For example, if NIDMM_ATTR_FUNCTION is set to NIDMM_VAL_DC_VOLTS, the units are volt

### NIDMM_ATTR_RANGE

Specifies the measurement range. Use positive values to represent the absolute value of the maximum expected measurement. The value is in units appropriate for the current value of the [NIDMM_ATTR_FUNCTION](group____root__nidmm__attributes__configuration_1ga1bfcd876e310fd57abfb66401acbb29f.html) attribute. For example, if [NIDMM_ATTR_FUNCTION](group____root__nidmm__attributes__configuration_1ga1bfcd876e310fd57abfb66401acbb29f.html) is set to **NIDMM_VAL_DC_VOLTS**, the units are volts.

#### Syntax

NIDMM_ATTR_RANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250002 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

The NI 4065 only supports Auto Range when the trigger and sample trigger are set to IMMEDIATE.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_AUTO_RANGE_ON | IVIDMM_VAL_AUTO_RANGE_ON | NI-DMM performs an Auto Range before acquiring the measurement. |
| NIDMM_VAL_AUTO_RANGE_OFF | IVIDMM_VAL_AUTO_RANGE_OFF | NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed. |
| NIDMM_VAL_AUTO_RANGE_ONCE | IVIDMM_VAL_AUTO_RANGE_ONCE | NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed. |

**High-Level Functions**:

- [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html)
- [niDMM_ConfigureMeasurementAbsolute](group____root__nidmm__functions__configuration_1ga57e31e207dd625df961781698ede1c6e.html)

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration_1ga1bfcd876e310fd57abfb66401acbb29f.html language=enus -->
## TOPIC 00005: NIDMM_ATTR_FUNCTION

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration_1ga1bfcd876e310fd57abfb66401acbb29f.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration_1ga1bfcd876e310fd57abfb66401acbb29f.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement function. SyntaxNIDMM_ATTR_FUNCTIONNumeric ValueData TypeAccessApplies To1250001ViInt32Read/WriteN/ARemarksIf you are setting this attribute directly, you must also set the NIDMM_ATTR_OPERATION_MODE attribute, which controls whether the DMM takes standard single or multipoi

### NIDMM_ATTR_FUNCTION

Specifies the measurement function.

#### Syntax

NIDMM_ATTR_FUNCTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250001 | ViInt32 | Read/Write | N/A |

#### Remarks

Note

If you are setting this attribute directly, you must also set the [NIDMM_ATTR_OPERATION_MODE](group____root__nidmm__attributes__configuration__advanced_1ga86fc3674cd8b0d0bce0198dc523728f0.html) attribute, which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform. If you are programming attributes directly, you must set the [NIDMM_ATTR_OPERATION_MODE](group____root__nidmm__attributes__configuration__advanced_1ga86fc3674cd8b0d0bce0198dc523728f0.html) attribute before setting other configuration attributes. If the [NIDMM_ATTR_OPERATION_MODE](group____root__nidmm__attributes__configuration__advanced_1ga86fc3674cd8b0d0bce0198dc523728f0.html) attribute is set to **NIDMM_VAL_WAVEFORM_MODE**, the only valid function types are **NIDMM_VAL_WAVEFORM_VOLTAGE** and **NIDMM_VAL_WAVEFORM_CURRENT**. Set the [NIDMM_ATTR_OPERATION_MODE](group____root__nidmm__attributes__configuration__advanced_1ga86fc3674cd8b0d0bce0198dc523728f0.html) attribute to **NIDMM_VAL_IVIDMM_MODE** to set all other function values.

**Defined Values**

| Name | Default Value | Description | Devices supported |
| --- | --- | --- | --- |
| NIDMM_VAL_DC_VOLTS | 1 | DC Voltage | All |
| NIDMM_VAL_AC_VOLTS | 2 | AC Voltage with AC Coupling | All |
| NIDMM_VAL_DC_CURRENT | 3 | DC Current | All |
| NIDMM_VAL_AC_CURRENT | 4 | AC Current | All |
| NIDMM_VAL_2_WIRE_RES | 5 | 2-Wire Resistance | All |
| NIDMM_VAL_4_WIRE_RES | 101 | 4-Wire Resistance | NI 4065, NI 4070/4071/4072, NI 4080/4081/4082 |
| NIDMM_VAL_FREQ | 104 | Frequency | NI 4070/4071/4072 and NI 4080/4081/4082 |
| NIDMM_VAL_PERIOD | 105 | Period | NI 4070/4071/4072 and NI 4080/4081/4082 |
| NIDMM_VAL_AC_VOLTS_DC_COUPLED | 1001 | AC Voltage with DC Coupling | NI 4070/4071/4072 and NI 4080/4081/4082 |
| NIDMM_VAL_DIODE | 1002 | Diode | All |
| NIDMM_VAL_WAVEFORM_VOLTAGE | 1003 | Waveform Voltage | NI 4070/4071/4072 and NI 4080/4081/4082 |
| NIDMM_VAL_WAVEFORM_CURRENT | 1004 | Waveform Current | NI 4070/4071/4072 and NI 4080/4081/4082 |
| NIDMM_VAL_CAPACITANCE | 1005 | Capacitance | NI 4072 and NI 4082 |
| NIDMM_VAL_INDUCTANCE | 1006 | Inductance | NI 4072 and NI 4082 |

**High-Level Functions**:

- [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html)
- [niDMM_ConfigureMeasurementAbsolute](group____root__nidmm__functions__configuration_1ga57e31e207dd625df961781698ede1c6e.html)
- [niDMM_ConfigureWaveformAcquisition](group____root__nidmm__functions__configuration_1gafcb170823681b23a5581215fdbe85e71.html)

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration_1ga2c80606597a33ae338751851c1c3c0b9.html language=enus -->
## TOPIC 00006: NIDMM_ATTR_AUTO_RANGE_VALUE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration_1ga2c80606597a33ae338751851c1c3c0b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration_1ga2c80606597a33ae338751851c1c3c0b9.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the range. If auto ranging is enabled, shows the actual value of the active range. The value of this attribute is set during a read operation. SyntaxNIDMM_ATTR_AUTO_RANGE_VALUENumeric ValueData TypeAccessApplies To1250331ViReal64Read-OnlyN/ARemarksHigh-Level Functions:niDMM_Ge

### NIDMM_ATTR_AUTO_RANGE_VALUE

Specifies the value of the range. If auto ranging is enabled, shows the actual value of the active range. The value of this attribute is set during a read operation.

#### Syntax

NIDMM_ATTR_AUTO_RANGE_VALUE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250331 | ViReal64 | Read-Only | N/A |

#### Remarks

**High-Level Functions**:

- [niDMM_GetAutoRangeValue](group____root__nidmm__functions__configuration__actual__values_1gaddfc3b3752e68a499f32c86970be325d.html)

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration_1gae49a6cec56bb0a37bf1b8dc43f0d7435.html language=enus -->
## TOPIC 00007: NIDMM_ATTR_RESOLUTION_DIGITS

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration_1gae49a6cec56bb0a37bf1b8dc43f0d7435.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration_1gae49a6cec56bb0a37bf1b8dc43f0d7435.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement resolution in digits. Setting this attribute to higher values increases the measurement accuracy. Setting this attribute to lower values increases the measurement speed. SyntaxNIDMM_ATTR_RESOLUTION_DIGITSNumeric ValueData TypeAccessApplies To1250003ViReal64Read/WriteN/ARema

### NIDMM_ATTR_RESOLUTION_DIGITS

Specifies the measurement resolution in digits. Setting this attribute to higher values increases the measurement accuracy. Setting this attribute to lower values increases the measurement speed.

#### Syntax

NIDMM_ATTR_RESOLUTION_DIGITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250003 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

NI-DMM ignores this attribute for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the [NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE](group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gaeb9bf1dd158a5d137d2e94639fe9fd16.html) attribute.

**High-Level Functions**:

- [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html)
- [niDMM_ConfigureMeasurementAbsolute](group____root__nidmm__functions__configuration_1ga57e31e207dd625df961781698ede1c6e.html)

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration_1gae69d9233c3a8f5c43bdfabf4b5aa09d4.html language=enus -->
## TOPIC 00008: NIDMM_ATTR_RESOLUTION_ABSOLUTE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration_1gae69d9233c3a8f5c43bdfabf4b5aa09d4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration_1gae69d9233c3a8f5c43bdfabf4b5aa09d4.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement resolution in absolute units. Setting this attribute to higher values increases the measurement accuracy. Setting this attribute to lower values increases the measurement speed. SyntaxNIDMM_ATTR_RESOLUTION_ABSOLUTENumeric ValueData TypeAccessApplies To1250008ViReal64Read/Wr

### NIDMM_ATTR_RESOLUTION_ABSOLUTE

Specifies the measurement resolution in absolute units. Setting this attribute to higher values increases the measurement accuracy. Setting this attribute to lower values increases the measurement speed.

#### Syntax

NIDMM_ATTR_RESOLUTION_ABSOLUTE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250008 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

NI-DMM ignores this attribute for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the [NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE](group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gaeb9bf1dd158a5d137d2e94639fe9fd16.html) attribute.

**High-Level Functions**:

- [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html)
- [niDMM_ConfigureMeasurementAbsolute](group____root__nidmm__functions__configuration_1ga57e31e207dd625df961781698ede1c6e.html)

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__advanced.html language=enus -->
## TOPIC 00009: Advanced

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__advanced.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_APERTURE_TIMESpecifies the measurement aperture time for the current configuration. Aperture time is specified in units set by NIDMM_ATTR_APERTURE_TIME_UNITS. To override the default aperture, set this attribute to the desired aperture time after call

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_APERTURE_TIME | Specifies the measurement aperture time for the current configuration. Aperture time is specified in units set by NIDMM_ATTR_APERTURE_TIME_UNITS. To override the default aperture, set this attribute to the desired aperture time after calling niDMM_ConfigureMeasurementDigits. To return to the default, set this attribute to NIDMM_VAL_APERTURE_TIME_AUTO (-1). |
| NIDMM_ATTR_APERTURE_TIME_UNITS | Specifies the units of aperture time for the current configuration. |
| NIDMM_ATTR_NUMBER_OF_AVERAGES | Specifies the number of averages to perform in a measurement. For the NI 4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture time is not set to AUTO and Auto Zero is ON. The default is 1. |
| NIDMM_ATTR_OPERATION_MODE | Specifies how the DMM acquires data. |
| NIDMM_ATTR_SETTLE_TIME | Specifies the settling time in seconds. To override the default settling time, set this attribute. To return to the default, set this attribute to NIDMM_VAL_SETTLE_TIME_AUTO (-1). |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__advanced_1ga5f2b0c9f460a432ae149a8232c968a6d.html language=enus -->
## TOPIC 00010: NIDMM_ATTR_APERTURE_TIME_UNITS

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__advanced_1ga5f2b0c9f460a432ae149a8232c968a6d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__advanced_1ga5f2b0c9f460a432ae149a8232c968a6d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of aperture time for the current configuration. SyntaxNIDMM_ATTR_APERTURE_TIME_UNITSNumeric ValueData TypeAccessApplies To1250322ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_SECONDS0 (0x0)SecondsNIDMM_VAL_POWER_LINE_CYCLES1 (0x1)Powerline CyclesHigh-Lev

### NIDMM_ATTR_APERTURE_TIME_UNITS

Specifies the units of aperture time for the current configuration.

#### Syntax

NIDMM_ATTR_APERTURE_TIME_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250322 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_SECONDS | 0 (0x0) | Seconds |
| NIDMM_VAL_POWER_LINE_CYCLES | 1 (0x1) | Powerline Cycles |

**High-Level Functions**:

- [niDMM_GetApertureTimeInfo](group____root__nidmm__functions__configuration__actual__values_1gaccf0af289155ab67728ac7e08884e176.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__advanced_1ga86fc3674cd8b0d0bce0198dc523728f0.html language=enus -->
## TOPIC 00011: NIDMM_ATTR_OPERATION_MODE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__advanced_1ga86fc3674cd8b0d0bce0198dc523728f0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__advanced_1ga86fc3674cd8b0d0bce0198dc523728f0.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the DMM acquires data. SyntaxNIDMM_ATTR_OPERATION_MODENumeric ValueData TypeAccessApplies To1150014ViInt32Read/WriteN/ARemarks When you call niDMM_ConfigureMeasurementDigits, NI-DMM sets this attribute to NIDMM_VAL_IVIDMM_MODE. When you call niDMM_ConfigureWaveformAcquisition, NI-DMM s

### NIDMM_ATTR_OPERATION_MODE

Specifies how the DMM acquires data.

#### Syntax

NIDMM_ATTR_OPERATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150014 | ViInt32 | Read/Write | N/A |

#### Remarks

When you call [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html), NI-DMM sets this attribute to **NIDMM_VAL_IVIDMM_MODE**. When you call [niDMM_ConfigureWaveformAcquisition](group____root__nidmm__functions__configuration_1gafcb170823681b23a5581215fdbe85e71.html), NI-DMM sets this attribute to **NIDMM_VAL_WAVEFORM_MODE**. If you are programming attributes directly, you must set this attribute before setting other configuration attributes.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_IVIDMM_MODE | 0 (0x0) | Single or multipoint measurements—when the NIDMM_ATTR_TRIGGER_COUNT and NIDMM_ATTR_SAMPLE_COUNT attributes are both set to 1, the NI 4065 and NI 4070/4071/4072 take a single-point measurement; otherwise, NI-DMM takes multipoint measurements. |
| NIDMM_VAL_WAVEFORM_MODE | 1 (0x1) | Waveform Mode configures the NI 4070/4071/4072 to take waveform measurements. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__advanced_1ga8ea3129602cc3ee4569b05035c059d0d.html language=enus -->
## TOPIC 00012: NIDMM_ATTR_NUMBER_OF_AVERAGES

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__advanced_1ga8ea3129602cc3ee4569b05035c059d0d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__advanced_1ga8ea3129602cc3ee4569b05035c059d0d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of averages to perform in a measurement. For the NI 4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture time is not set to AUTO and Auto Zero is ON. The default is 1. SyntaxNIDMM_ATTR_NUMBER_OF_AVERAGESNumeric ValueData TypeAccessApplies To1150032ViInt32Read/Wri

### NIDMM_ATTR_NUMBER_OF_AVERAGES

Specifies the number of averages to perform in a measurement. For the NI 4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture time is not set to AUTO and Auto Zero is ON. The default is 1.

#### Syntax

NIDMM_ATTR_NUMBER_OF_AVERAGES

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150032 | ViInt32 | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__advanced_1gab8b03d980680fac114f03567a3777264.html language=enus -->
## TOPIC 00013: NIDMM_ATTR_APERTURE_TIME

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__advanced_1gab8b03d980680fac114f03567a3777264.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__advanced_1gab8b03d980680fac114f03567a3777264.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement aperture time for the current configuration. Aperture time is specified in units set by NIDMM_ATTR_APERTURE_TIME_UNITS. To override the default aperture, set this attribute to the desired aperture time after calling niDMM_ConfigureMeasurementDigits. To return to the default

### NIDMM_ATTR_APERTURE_TIME

Specifies the measurement aperture time for the current configuration. Aperture time is specified in units set by [NIDMM_ATTR_APERTURE_TIME_UNITS](group____root__nidmm__attributes__configuration__advanced_1ga5f2b0c9f460a432ae149a8232c968a6d.html). To override the default aperture, set this attribute to the desired aperture time after calling [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html). To return to the default, set this attribute to **NIDMM_VAL_APERTURE_TIME_AUTO** (-1).

#### Syntax

NIDMM_ATTR_APERTURE_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250321 | ViReal64 | Read/Write | N/A |

#### Remarks

Any number of powerline cycles (PLCs) within the minimum and maximum ranges is allowed on the NI 4080/4081/4082 and NI 4070/4071/4072.

On the NI 4065, the minimum aperture time is 333 µs, and the maximum aperture time is 78.2 s. If setting the number of averages directly, the total measurement time is aperture time X the number of averages, which must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs, or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples of 1.11 ms, the value will be coerced up to the next supported aperture time.

**High-Level Functions**:

- [niDMM_GetApertureTimeInfo](group____root__nidmm__functions__configuration__actual__values_1gaccf0af289155ab67728ac7e08884e176.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__advanced_1gaeb74d4e976a946505bcbabb260d1384b.html language=enus -->
## TOPIC 00014: NIDMM_ATTR_SETTLE_TIME

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__advanced_1gaeb74d4e976a946505bcbabb260d1384b.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__advanced_1gaeb74d4e976a946505bcbabb260d1384b.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the settling time in seconds. To override the default settling time, set this attribute. To return to the default, set this attribute to NIDMM_VAL_SETTLE_TIME_AUTO (-1). SyntaxNIDMM_ATTR_SETTLE_TIMENumeric ValueData TypeAccessApplies To1150028ViReal64Read/WriteN/A

### NIDMM_ATTR_SETTLE_TIME

Specifies the settling time in seconds. To override the default settling time, set this attribute. To return to the default, set this attribute to **NIDMM_VAL_SETTLE_TIME_AUTO** (-1).

#### Syntax

NIDMM_ATTR_SETTLE_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150028 | ViReal64 | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options.html language=enus -->
## TOPIC 00015: Measurement Options

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCapacitance and InductanceTemperatureGroup membersNameDescriptionNIDMM_ATTR_AC_MAX_FREQSpecifies the maximum frequency component of the input signal for AC measurements. This attribute is used only for error checking and verifies that the value of this parameter is less than the maximum freque

### Measurement Options

#### Groups

- Capacitance and Inductance
- Temperature

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_AC_MAX_FREQ | Specifies the maximum frequency component of the input signal for AC measurements. This attribute is used only for error checking and verifies that the value of this parameter is less than the maximum frequency of the device. This attribute affects the DMM only when you set the NIDMM_ATTR_FUNCTION attribute to AC measurements. The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz–100 kHz for the NI 4065. |
| NIDMM_ATTR_AC_MIN_FREQ | Specifies the minimum frequency component of the input signal for AC measurements. This attribute affects the DMM only when you set the NIDMM_ATTR_FUNCTION attribute to AC measurements. The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz–100 kHz for the NI 4065. |
| NIDMM_ATTR_ADC_CALIBRATION | For the NI 4080/4081/4082 and the NI 4070/4071/4072, specifies the ADC calibration mode. |
| NIDMM_ATTR_AUTO_ZERO | Specifies the Auto Zero mode. |
| NIDMM_ATTR_CURRENT_SOURCE | Specifies the current source provided during diode measurements. |
| NIDMM_ATTR_DC_NOISE_REJECTION | Specifies the DC noise rejection mode. |
| NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE_VALUE | For the NI 4080/4081/4082 and the NI 4070/4071/4072, specifies the value of the frequency voltage range. If Auto Ranging, shows the actual value of the active frequency voltage range. If not Auto Ranging, the value is the same as that of NIDMM_ATTR_FREQ_VOLTAGE_RANGE. |
| NIDMM_ATTR_FREQ_VOLTAGE_RANGE | For the NI 4070/4071/4072, specifies the maximum amplitude of the input signal for frequency measurements. |
| NIDMM_ATTR_INPUT_RESISTANCE | Specifies the input resistance of the instrument. |
| NIDMM_ATTR_OFFSET_COMP_OHMS | For the NI 4080/4081/4082 and NI 4070/4071/4072 only, enables or disables offset compensated ohms. |
| NIDMM_ATTR_POWERLINE_FREQ | Specifies the powerline frequency. The NI 4065, NI 4070/4071/4072, and the NI 4080/4081/4082 use this value to select a timebase for setting the NIDMM_ATTR_APERTURE_TIME attribute in powerline cycles (PLCs). |
| NIDMM_ATTR_SHUNT_VALUE | For the NI 4050 only, specifies the shunt resistance value. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1ga20add9f3a5a460ffe4377e83c846438e.html language=enus -->
## TOPIC 00016: NIDMM_ATTR_AC_MAX_FREQ

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1ga20add9f3a5a460ffe4377e83c846438e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1ga20add9f3a5a460ffe4377e83c846438e.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum frequency component of the input signal for AC measurements. This attribute is used only for error checking and verifies that the value of this parameter is less than the maximum frequency of the device. This attribute affects the DMM only when you set the NIDMM_ATTR_FUNCTION a

### NIDMM_ATTR_AC_MAX_FREQ

Specifies the maximum frequency component of the input signal for AC measurements. This attribute is used only for error checking and verifies that the value of this parameter is less than the maximum frequency of the device. This attribute affects the DMM only when you set the [NIDMM_ATTR_FUNCTION](group____root__nidmm__attributes__configuration_1ga1bfcd876e310fd57abfb66401acbb29f.html) attribute to AC measurements. The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz–100 kHz for the NI 4065.

#### Syntax

NIDMM_ATTR_AC_MAX_FREQ

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250007 | ViReal64 | Read/Write | N/A |

#### Remarks

**High-Level Functions**:

- [niDMM_ConfigureACBandwidth](group____root__nidmm__functions__configuration_1ga29195e4e069e8ba75741476a3138f47a.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1ga2a0e96830fda4400d5377598aa0bfb37.html language=enus -->
## TOPIC 00017: NIDMM_ATTR_CURRENT_SOURCE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1ga2a0e96830fda4400d5377598aa0bfb37.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1ga2a0e96830fda4400d5377598aa0bfb37.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current source provided during diode measurements. SyntaxNIDMM_ATTR_CURRENT_SOURCENumeric ValueData TypeAccessApplies To1150025ViReal64Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_1_MICROAMP1e-06NI 4080/4081/4082 and NI 4070/4071/4072 onlyNIDMM_VAL_10_MICROAMP1e-05N

### NIDMM_ATTR_CURRENT_SOURCE

Specifies the current source provided during diode measurements.

#### Syntax

NIDMM_ATTR_CURRENT_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150025 | ViReal64 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_1_MICROAMP | 1e-06 | NI 4080/4081/4082 and NI 4070/4071/4072 only |
| NIDMM_VAL_10_MICROAMP | 1e-05 | NI 4080/4081/4082 and NI 4070/4071/4072 only |
| NIDMM_VAL_100_MICROAMP | 0.0001 | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 |
| NIDMM_VAL_1_MILLIAMP | 0.001 | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 |

**High-Level Functions**:

- [niDMM_ConfigureCurrentSource](group____root__nidmm__functions__configuration_1ga4694b4ed6faf28f2d235d28d93a739f9.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1ga2c9f36e1d26f9f0af085047f387190d4.html language=enus -->
## TOPIC 00018: NIDMM_ATTR_FREQ_VOLTAGE_RANGE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1ga2c9f36e1d26f9f0af085047f387190d4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1ga2c9f36e1d26f9f0af085047f387190d4.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4070/4071/4072, specifies the maximum amplitude of the input signal for frequency measurements. SyntaxNIDMM_ATTR_FREQ_VOLTAGE_RANGENumeric ValueData TypeAccessApplies To1250101ViReal64Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_AUTO_RANGE_ONIVIDMM_VAL_AUTO_RANGE_ONCon

### NIDMM_ATTR_FREQ_VOLTAGE_RANGE

For the NI 4070/4071/4072, specifies the maximum amplitude of the input signal for frequency measurements.

#### Syntax

NIDMM_ATTR_FREQ_VOLTAGE_RANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250101 | ViReal64 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_AUTO_RANGE_ON | IVIDMM_VAL_AUTO_RANGE_ON | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement. |
| NIDMM_VAL_AUTO_RANGE_OFF | IVIDMM_VAL_AUTO_RANGE_OFF | Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range. |

Note

Not supported on the NI 4080/4081/4082. These devices must be set to a valid value.

**High-Level Functions**:

- [niDMM_ConfigureFrequencyVoltageRange](group____root__nidmm__functions__configuration_1ga4eb3ebe8c031ca3a46c0ac641303e88f.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1ga2f0d79b124dce873665134c94d250d70.html language=enus -->
## TOPIC 00019: NIDMM_ATTR_ADC_CALIBRATION

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1ga2f0d79b124dce873665134c94d250d70.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1ga2f0d79b124dce873665134c94d250d70.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4080/4081/4082 and the NI 4070/4071/4072, specifies the ADC calibration mode. SyntaxNIDMM_ATTR_ADC_CALIBRATIONNumeric ValueData TypeAccessApplies To1150022ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_ADC_CALIBRATION_AUTO-1 (-0x1)The DMM enables or disables ADC C

### NIDMM_ATTR_ADC_CALIBRATION

For the NI 4080/4081/4082 and the NI 4070/4071/4072, specifies the ADC calibration mode.

#### Syntax

NIDMM_ATTR_ADC_CALIBRATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150022 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_ADC_CALIBRATION_AUTO | -1 (-0x1) | The DMM enables or disables ADC Calibration based on the configured function and resolution. |
| NIDMM_VAL_ADC_CALIBRATION_OFF | 0 (0x0) | The DMM does not compensate for changes to the gain. |
| NIDMM_VAL_ADC_CALIBRATION_ON | 1 (0x1) | The DMM measures an internal reference to calculate the correct gain for the measurement. |

**High-Level Functions**:

- [niDMM_ConfigureADCCalibration](group____root__nidmm__functions__configuration_1ga01f2931e3f609e32ac57d42486bcc02f.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1ga60efe5c9df55623e43aaab312bd338cb.html language=enus -->
## TOPIC 00020: NIDMM_ATTR_INPUT_RESISTANCE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1ga60efe5c9df55623e43aaab312bd338cb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1ga60efe5c9df55623e43aaab312bd338cb.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input resistance of the instrument. SyntaxNIDMM_ATTR_INPUT_RESISTANCENumeric ValueData TypeAccessApplies To1150029ViReal64Read/WriteN/ARemarksDefined ValuesNIDMM_VAL_1_MEGAOHM1000000.001 MΩNIDMM_VAL_10_MEGAOHM10000000.0010 MΩNIDMM_VAL_GREATER_THAN_10_GIGAOHM10000000000.00>10 GΩ

### NIDMM_ATTR_INPUT_RESISTANCE

Specifies the input resistance of the instrument.

#### Syntax

NIDMM_ATTR_INPUT_RESISTANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150029 | ViReal64 | Read/Write | N/A |

#### Remarks

**Defined Values**

|  |  |  |
| --- | --- | --- |
| NIDMM_VAL_1_MEGAOHM | 1000000.00 | 1 MΩ |
| NIDMM_VAL_10_MEGAOHM | 10000000.00 | 10 MΩ |
| NIDMM_VAL_GREATER_THAN_10_GIGAOHM | 10000000000.00 | >10 GΩ |

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1ga7c3b9eda8978b29c7d476fc5987e4511.html language=enus -->
## TOPIC 00021: NIDMM_ATTR_POWERLINE_FREQ

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1ga7c3b9eda8978b29c7d476fc5987e4511.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1ga7c3b9eda8978b29c7d476fc5987e4511.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the powerline frequency. The NI 4065, NI 4070/4071/4072, and the NI 4080/4081/4082 use this value to select a timebase for setting the NIDMM_ATTR_APERTURE_TIME attribute in powerline cycles (PLCs). SyntaxNIDMM_ATTR_POWERLINE_FREQNumeric ValueData TypeAccessApplies To1250333ViReal64Read/Wri

### NIDMM_ATTR_POWERLINE_FREQ

Specifies the powerline frequency. The NI 4065, NI 4070/4071/4072, and the NI 4080/4081/4082 use this value to select a timebase for setting the [NIDMM_ATTR_APERTURE_TIME](group____root__nidmm__attributes__configuration__advanced_1gab8b03d980680fac114f03567a3777264.html) attribute in powerline cycles (PLCs).

#### Syntax

NIDMM_ATTR_POWERLINE_FREQ

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250333 | ViReal64 | Read/Write | N/A |

#### Remarks

After configuring powerline frequency, set the [NIDMM_ATTR_APERTURE_TIME_UNITS](group____root__nidmm__attributes__configuration__advanced_1ga5f2b0c9f460a432ae149a8232c968a6d.html) attribute to PLCs. When setting the [NIDMM_ATTR_APERTURE_TIME](group____root__nidmm__attributes__configuration__advanced_1gab8b03d980680fac114f03567a3777264.html) attribute, select the number of PLCs for the powerline frequency. For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_50_HERTZ | 50.0 | 50 Hz |
| NIDMM_VAL_60_HERTZ | 60.0 | 60 Hz |

Note

For 400 Hz powerline frequency, use the 50 Hz setting.

**High-Level Functions**:

- [niDMM_ConfigurePowerLineFrequency](group____root__nidmm__functions__configuration_1ga9ac1c85f8bb4dcc47a40cd9ffb4a2840.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1gabd43f445a96d6be967e6abf6a8467458.html language=enus -->
## TOPIC 00022: NIDMM_ATTR_AUTO_ZERO

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1gabd43f445a96d6be967e6abf6a8467458.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1gabd43f445a96d6be967e6abf6a8467458.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Auto Zero mode. SyntaxNIDMM_ATTR_AUTO_ZERONumeric ValueData TypeAccessApplies To1250332ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_AUTO_ZERO_AUTO-1 (-0x1)NI-DMM chooses the Auto Zero setting based on the configured function and resolution.NIDMM_VAL_AUTO_ZERO

### NIDMM_ATTR_AUTO_ZERO

Specifies the Auto Zero mode.

#### Syntax

NIDMM_ATTR_AUTO_ZERO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250332 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_AUTO_ZERO_AUTO | -1 (-0x1) | NI-DMM chooses the Auto Zero setting based on the configured function and resolution. |
| NIDMM_VAL_AUTO_ZERO_OFF | 0 (0x0) | Disables Auto Zero. Note: The NI 4065 does not support this setting. |
| NIDMM_VAL_AUTO_ZERO_ON | 1 (0x1) | The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading. Note: For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement. |
| NIDMM_VAL_AUTO_ZERO_ONCE | 2 (0x2) | The DMM internally disconnects the input signal following the first measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading and each measurement that follows. Note: The NI 4060/4065 does not support this setting. |

**High-Level Functions**:

- [niDMM_ConfigureAutoZeroMode](group____root__nidmm__functions__configuration_1ga02d637ef47ad5d3b65cdd334f3a0c608.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1gabd81cae19cfda72c89a704704494a388.html language=enus -->
## TOPIC 00023: NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE_VALUE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1gabd81cae19cfda72c89a704704494a388.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1gabd81cae19cfda72c89a704704494a388.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4080/4081/4082 and the NI 4070/4071/4072, specifies the value of the frequency voltage range. If Auto Ranging, shows the actual value of the active frequency voltage range. If not Auto Ranging, the value is the same as that of NIDMM_ATTR_FREQ_VOLTAGE_RANGE. SyntaxNIDMM_ATTR_FREQ_VOLTAGE_A

### NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE_VALUE

For the NI 4080/4081/4082 and the NI 4070/4071/4072, specifies the value of the frequency voltage range. If Auto Ranging, shows the actual value of the active frequency voltage range. If not Auto Ranging, the value is the same as that of [NIDMM_ATTR_FREQ_VOLTAGE_RANGE](group____root__nidmm__attributes__configuration__measurement__options_1ga2c9f36e1d26f9f0af085047f387190d4.html).

#### Syntax

NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE_VALUE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150044 | ViReal64 | Read-Only | N/A |

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1gad84112e4c817e74b26e266c535e144ae.html language=enus -->
## TOPIC 00024: NIDMM_ATTR_SHUNT_VALUE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1gad84112e4c817e74b26e266c535e144ae.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1gad84112e4c817e74b26e266c535e144ae.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4050 only, specifies the shunt resistance value. SyntaxNIDMM_ATTR_SHUNT_VALUENumeric ValueData TypeAccessApplies To1150003ViReal64Read/WriteN/ARemarksThe NI 4050 requires an external shunt resistor for current measurements. This attribute should be set to the value of the shunt resistor.

### NIDMM_ATTR_SHUNT_VALUE

For the NI 4050 only, specifies the shunt resistance value.

#### Syntax

NIDMM_ATTR_SHUNT_VALUE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150003 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

The NI 4050 requires an external shunt resistor for current measurements. This attribute should be set to the value of the shunt resistor.

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1gae2c9bdf790c30fd80cdfe8b693b35c20.html language=enus -->
## TOPIC 00025: NIDMM_ATTR_AC_MIN_FREQ

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1gae2c9bdf790c30fd80cdfe8b693b35c20.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1gae2c9bdf790c30fd80cdfe8b693b35c20.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum frequency component of the input signal for AC measurements. This attribute affects the DMM only when you set the NIDMM_ATTR_FUNCTION attribute to AC measurements. The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz–100 kHz for the NI 4065.

### NIDMM_ATTR_AC_MIN_FREQ

Specifies the minimum frequency component of the input signal for AC measurements. This attribute affects the DMM only when you set the [NIDMM_ATTR_FUNCTION](group____root__nidmm__attributes__configuration_1ga1bfcd876e310fd57abfb66401acbb29f.html) attribute to AC measurements. The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz–100 kHz for the NI 4065.

#### Syntax

NIDMM_ATTR_AC_MIN_FREQ

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250006 | ViReal64 | Read/Write | N/A |

#### Remarks

**High-Level Functions**:

- [niDMM_ConfigureACBandwidth](group____root__nidmm__functions__configuration_1ga29195e4e069e8ba75741476a3138f47a.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1gaec7ea397739a2b8b026fa5c30cc186df.html language=enus -->
## TOPIC 00026: NIDMM_ATTR_DC_NOISE_REJECTION

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1gaec7ea397739a2b8b026fa5c30cc186df.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1gaec7ea397739a2b8b026fa5c30cc186df.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DC noise rejection mode. SyntaxNIDMM_ATTR_DC_NOISE_REJECTIONNumeric ValueData TypeAccessApplies To1150026ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_DCNR_AUTO-1 (-0x1)The driver chooses the DC noise rejection setting based on the configured function and reso

### NIDMM_ATTR_DC_NOISE_REJECTION

Specifies the DC noise rejection mode.

#### Syntax

NIDMM_ATTR_DC_NOISE_REJECTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150026 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_DCNR_AUTO | -1 (-0x1) | The driver chooses the DC noise rejection setting based on the configured function and resolution. |
| NIDMM_VAL_DCNR_NORMAL | 0 (0x0) | NI-DMM weighs all samples equally. |
| NIDMM_VAL_DCNR_SECOND_ORDER | 1 (0x1) | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a triangular weighing function. |
| NIDMM_VAL_DCNR_HIGH_ORDER | 2 (0x2) | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a bell-curve weighing function. Note: The NI 4065 does not support this setting. |

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options_1gaeebcfa711f47bad5bb8fc33f6c5950b5.html language=enus -->
## TOPIC 00027: NIDMM_ATTR_OFFSET_COMP_OHMS

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options_1gaeebcfa711f47bad5bb8fc33f6c5950b5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options_1gaeebcfa711f47bad5bb8fc33f6c5950b5.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4080/4081/4082 and NI 4070/4071/4072 only, enables or disables offset compensated ohms. SyntaxNIDMM_ATTR_OFFSET_COMP_OHMSNumeric ValueData TypeAccessApplies To1150023ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_OFFSET_COMP_OHMS_OFF0 (0x0)Off disablesOffset Compe

### NIDMM_ATTR_OFFSET_COMP_OHMS

For the NI 4080/4081/4082 and NI 4070/4071/4072 only, enables or disables offset compensated ohms.

#### Syntax

NIDMM_ATTR_OFFSET_COMP_OHMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150023 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_OFFSET_COMP_OHMS_OFF | 0 (0x0) | Off disablesOffset Compensated Ohms. |
| NIDMM_VAL_OFFSET_COMP_OHMS_ON | 1 (0x1) | On enablesOffset Compensated Ohms. |

**High-Level Functions**:

- [niDMM_ConfigureOffsetCompOhms](group____root__nidmm__functions__configuration_1gadf456a71ebdd5d5252672f56657da973.html)

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e.html language=enus -->
## TOPIC 00028: Short Cable Compensation Values

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_SHORT_CABLE_COMP_REACTANCEFor the NI 4082 and NI 4072 only, represents the reactive part (reactance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place. NIDMM_

### Short Cable Compensation Values

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE | For the NI 4082 and NI 4072 only, represents the reactive part (reactance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place. |
| NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE | For the NI 4082 and NI 4072 only, represents the active part (resistance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place. |

#### Attachments

None

Parent topic:

Capacitance and Inductance

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e_1ga77c12e2c1b469c2886f04925fb8d33f5.html language=enus -->
## TOPIC 00029: NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e_1ga77c12e2c1b469c2886f04925fb8d33f5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e_1ga77c12e2c1b469c2886f04925fb8d33f5.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, represents the reactive part (reactance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place. SyntaxNIDMM_ATTR_SHORT_CABLE_COMP_REACTANCENumeric ValueData TypeAccessApplies To

### NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE

For the NI 4082 and NI 4072 only, represents the reactive part (reactance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place.

#### Syntax

NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150046 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

Changing the function or the range through this attribute or through [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html) resets the value of this attribute to the default value.

**High-Level Functions**:

- [niDMM_ConfigureShortCableCompValues](group____root__nidmm__functions__configuration__measurement__options__capacitance__and__inductance_1gabf18abea8d7bf411d7a0b7d8a83e3fcb.html)

Parent topic:

Short Cable Compensation Values

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e_1gafafdbe84ac9ddf28f72a6ec154ae74ad.html language=enus -->
## TOPIC 00030: NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e_1gafafdbe84ac9ddf28f72a6ec154ae74ad.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inducta7dd8f90a98247548d31115395b861f3e_1gafafdbe84ac9ddf28f72a6ec154ae74ad.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, represents the active part (resistance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place. SyntaxNIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCENumeric ValueData TypeAccessApplies To

### NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE

For the NI 4082 and NI 4072 only, represents the active part (resistance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place.

#### Syntax

NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150047 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

Changing the function or the range through this attribute or through [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html) resets the value of this attribute to the default value.

**High-Level Functions**:

- [niDMM_ConfigureShortCableCompValues](group____root__nidmm__functions__configuration__measurement__options__capacitance__and__inductance_1gabf18abea8d7bf411d7a0b7d8a83e3fcb.html)

Parent topic:

Short Cable Compensation Values

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367.html language=enus -->
## TOPIC 00031: Open Cable Compensation Values

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCEFor the NI 4082 and NI 4072 only, specifies the active part (conductance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place. NIDMM

### Open Cable Compensation Values

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE | For the NI 4082 and NI 4072 only, specifies the active part (conductance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place. |
| NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE | For the NI 4082 and NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place. |

#### Attachments

None

Parent topic:

Capacitance and Inductance

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367_1gaa3149b53febce32c161dc6723769a0bb.html language=enus -->
## TOPIC 00032: NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367_1gaa3149b53febce32c161dc6723769a0bb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367_1gaa3149b53febce32c161dc6723769a0bb.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, specifies the active part (conductance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place. SyntaxNIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCENumeric ValueData TypeAccessApplies T

### NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE

For the NI 4082 and NI 4072 only, specifies the active part (conductance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place.

#### Syntax

NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150049 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

Changing the function or the range through this attribute or through [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html) resets the value of this attribute to the default value.

**High-Level Functions**:

- [niDMM_ConfigureOpenCableCompValues](group____root__nidmm__functions__configuration__measurement__options__capacitance__and__inductance_1ga8999ada91280336adc9922e97aed3624.html)

Parent topic:

Open Cable Compensation Values

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367_1gabb59aebc75beacf501e94b671c0fb6af.html language=enus -->
## TOPIC 00033: NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367_1gabb59aebc75beacf501e94b671c0fb6af.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductad9b5fcf2b3cffbdd919859ec35f40367_1gabb59aebc75beacf501e94b671c0fb6af.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place. SyntaxNIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCENumeric ValueData TypeAccessApplies

### NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE

For the NI 4082 and NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place.

#### Syntax

NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150048 | ViReal64 | Read/Write | N/A |

#### Remarks

Note

Changing the function or the range through this attribute or through [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html) resets the value of this attribute to the default value.

**High-Level Functions**:

- [niDMM_ConfigureOpenCableCompValues](group____root__nidmm__functions__configuration__measurement__options__capacitance__and__inductance_1ga8999ada91280336adc9922e97aed3624.html)

Parent topic:

Open Cable Compensation Values

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance.html language=enus -->
## TOPIC 00034: Capacitance and Inductance

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedOpen Cable Compensation ValuesShort Cable Compensation ValuesGroup membersNameDescriptionNIDMM_ATTR_CABLE_COMP_TYPEFor the NI 4082 and NI 4072 only, specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. NIDM

### Capacitance and Inductance

#### Groups

- Advanced
- Open Cable Compensation Values
- Short Cable Compensation Values

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_CABLE_COMP_TYPE | For the NI 4082 and NI 4072 only, specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. |
| NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE | For the NI 4082 and NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading. |

#### Attachments

None

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gabe5a1e3b560e5296ba16d9da6c79654d.html language=enus -->
## TOPIC 00035: NIDMM_ATTR_CABLE_COMP_TYPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gabe5a1e3b560e5296ba16d9da6c79654d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gabe5a1e3b560e5296ba16d9da6c79654d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. SyntaxNIDMM_ATTR_CABLE_COMP_TYPENumeric ValueData TypeAccessApplies To1150045ViInt32Read/WriteN/ARemarksChanging the function or the

### NIDMM_ATTR_CABLE_COMP_TYPE

For the NI 4082 and NI 4072 only, specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range.

#### Syntax

NIDMM_ATTR_CABLE_COMP_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150045 | ViInt32 | Read/Write | N/A |

#### Remarks

Note

Changing the function or the range through this attribute or through [niDMM_ConfigureMeasurementDigits](group____root__nidmm__functions__configuration_1ga303cf7761fdf850c80abae33618e08cf.html) resets the value of this attribute to the default value.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_CABLE_COMP_NONE | 0 (0x0) | No Cable Compensation |
| NIDMM_VAL_CABLE_COMP_OPEN | 1 (0x1) | Open Cable Compensation |
| NIDMM_VAL_CABLE_COMP_SHORT | 2 (0x2) | Short Cable Compensation |
| NIDMM_VAL_CABLE_COMP_OPEN_AND_SHORT | 3 (0x3) | Open and Short Cable Compensation |

**High-Level Functions**:

- [niDMM_ConfigureCableCompType](group____root__nidmm__functions__configuration__measurement__options__capacitance__and__inductance_1ga30c322fecbbe295de79dad2b51986dcf.html)

Parent topic:

Capacitance and Inductance

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gaeb9bf1dd158a5d137d2e94639fe9fd16.html language=enus -->
## TOPIC 00036: NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gaeb9bf1dd158a5d137d2e94639fe9fd16.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance_1gaeb9bf1dd158a5d137d2e94639fe9fd16.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading. SyntaxNIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGENumeric ValueData TypeAccessApplies To1150055ViInt32Read/WriteN/A

### NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE

For the NI 4082 and NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.

#### Syntax

NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150055 | ViInt32 | Read/Write | N/A |

Parent topic:

Capacitance and Inductance

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced.html language=enus -->
## TOPIC 00037: Advanced

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_DC_BIASFor the NI 4082 and NI 4072 only, controls the available DC bias for capacitance measurements. NIDMM_ATTR_LC_CALCULATION_MODELFor the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_DC_BIAS | For the NI 4082 and NI 4072 only, controls the available DC bias for capacitance measurements. |
| NIDMM_ATTR_LC_CALCULATION_MODEL | For the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance and inductance measurements. |

#### Attachments

None

Parent topic:

Capacitance and Inductance

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced_1ga3bb99feef3b846779d373239f74ad79c.html language=enus -->
## TOPIC 00038: NIDMM_ATTR_DC_BIAS

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced_1ga3bb99feef3b846779d373239f74ad79c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced_1ga3bb99feef3b846779d373239f74ad79c.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, controls the available DC bias for capacitance measurements. SyntaxNIDMM_ATTR_DC_BIASNumeric ValueData TypeAccessApplies To1150053ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_DC_BIAS_OFF0 (0x0)NI-DMM programs the device not to use the DC b

### NIDMM_ATTR_DC_BIAS

For the NI 4082 and NI 4072 only, controls the available DC bias for capacitance measurements.

#### Syntax

NIDMM_ATTR_DC_BIAS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150053 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_DC_BIAS_OFF | 0 (0x0) | NI-DMM programs the device not to use the DC bias. |
| NIDMM_VAL_DC_BIAS_ON | 1 (0x1) | NI-DMM programs the device to use the DC bias. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced_1ga564312bbb488d643380c788167269d41.html language=enus -->
## TOPIC 00039: NIDMM_ATTR_LC_CALCULATION_MODEL

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced_1ga564312bbb488d643380c788167269d41.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__capacitance__and__inductance__advanced_1ga564312bbb488d643380c788167269d41.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance and inductance measurements. SyntaxNIDMM_ATTR_LC_CALCULATION_MODELNumeric ValueData TypeAccessApplies To1150052ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VA

### NIDMM_ATTR_LC_CALCULATION_MODEL

For the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance and inductance measurements.

#### Syntax

NIDMM_ATTR_LC_CALCULATION_MODEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150052 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_CALC_MODEL_AUTO | -1 (-0x1) | NI-DMM chooses the algorithm based on function and range. |
| NIDMM_VAL_CALC_MODEL_SERIES | 0 (0x0) | NI-DMM uses the series impedance model to calculate capacitance and inductance. |
| NIDMM_VAL_CALC_MODEL_PARALLEL | 1 (0x1) | NI-DMM uses the parallel admittance model to calculate capacitance and inductance. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature.html language=enus -->
## TOPIC 00040: Temperature

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_TEMP_RTD_ASpecifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is 3.9083e-3 (Pt3851). NIDMM_ATTR_TEMP_RTD_BSpecifies the Callendar-Van Dusen B coefficient for RTD scaling when t

### Temperature

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_TEMP_RTD_A | Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is 3.9083e-3 (Pt3851). |
| NIDMM_ATTR_TEMP_RTD_B | Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is -5.775e-7(Pt3851). |
| NIDMM_ATTR_TEMP_RTD_C | Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is -4.183e-12(Pt3851). |
| NIDMM_ATTR_TEMP_RTD_RES | Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs, including custom RTDs. The default value is 100 (Ω). |
| NIDMM_ATTR_TEMP_RTD_TYPE | Specifies the type of RTD used to measure temperature. The default value is NIDMM_VAL_TEMP_RTD_PT3851. |
| NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC | Specifies the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. The default value is 25.0 (°C). |
| NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE | Specifies the type of reference junction to be used in the reference junction compensation of a thermocouple. The only supported value, NIDMM_VAL_TEMP_REF_JUNC_FIXED, is fixed. |
| NIDMM_ATTR_TEMP_TC_TYPE | Specifies the type of thermocouple used to measure the temperature. The default value is NIDMM_VAL_TEMP_TC_J. |
| NIDMM_ATTR_TEMP_THERMISTOR_A | Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type property is set to Custom. The default value is 0.0010295 (44006). |
| NIDMM_ATTR_TEMP_THERMISTOR_B | Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type proerty is set to Custom. The default value is 0.0002391 (44006). |
| NIDMM_ATTR_TEMP_THERMISTOR_C | Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type property is set to Custom. The default value is 1.568e-7 (44006). |
| NIDMM_ATTR_TEMP_THERMISTOR_TYPE | Specifies the type of thermistor used to measure the temperature. The default value is NIDMM_VAL_TEMP_THERMISTOR_44006. |
| NIDMM_ATTR_TEMP_TRANSDUCER_TYPE | Specifies the type of device used to measure the temperature. The default value is NIDMM_VAL_THERMOCOUPLE. |

#### Attachments

None

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga04bf469970ada62a6009ea65e776b9f1.html language=enus -->
## TOPIC 00041: NIDMM_ATTR_TEMP_RTD_B

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga04bf469970ada62a6009ea65e776b9f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga04bf469970ada62a6009ea65e776b9f1.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is -5.775e-7(Pt3851). SyntaxNIDMM_ATTR_TEMP_RTD_BNumeric ValueData TypeAccessApplies To1150122ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_RTD_B

Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is -5.775e-7(Pt3851).

#### Syntax

NIDMM_ATTR_TEMP_RTD_B

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150122 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga29bd6d51871465daf98c62d931c93a1d.html language=enus -->
## TOPIC 00042: NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga29bd6d51871465daf98c62d931c93a1d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga29bd6d51871465daf98c62d931c93a1d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of reference junction to be used in the reference junction compensation of a thermocouple. The only supported value, NIDMM_VAL_TEMP_REF_JUNC_FIXED, is fixed. SyntaxNIDMM_ATTR_TEMP_TC_REF_JUNC_TYPENumeric ValueData TypeAccessApplies To1250232ViInt32Read/WriteN/A

### NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE

Specifies the type of reference junction to be used in the reference junction compensation of a thermocouple. The only supported value, **NIDMM_VAL_TEMP_REF_JUNC_FIXED**, is fixed.

#### Syntax

NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250232 | ViInt32 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga4584a6dc9cba56418e48c9e9518ef904.html language=enus -->
## TOPIC 00043: NIDMM_ATTR_TEMP_THERMISTOR_A

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga4584a6dc9cba56418e48c9e9518ef904.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga4584a6dc9cba56418e48c9e9518ef904.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type property is set to Custom. The default value is 0.0010295 (44006). SyntaxNIDMM_ATTR_TEMP_THERMISTOR_ANumeric ValueData TypeAccessApplies To1150125ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_THERMISTOR_A

Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type property is set to Custom. The default value is 0.0010295 (44006).

#### Syntax

NIDMM_ATTR_TEMP_THERMISTOR_A

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150125 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga72f956510af5cd4782bb5cd815d14a72.html language=enus -->
## TOPIC 00044: NIDMM_ATTR_TEMP_THERMISTOR_TYPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga72f956510af5cd4782bb5cd815d14a72.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga72f956510af5cd4782bb5cd815d14a72.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of thermistor used to measure the temperature. The default value is NIDMM_VAL_TEMP_THERMISTOR_44006. SyntaxNIDMM_ATTR_TEMP_THERMISTOR_TYPENumeric ValueData TypeAccessApplies To1150124ViInt32Read/WriteN/ARemarksDefined ValuesThermistor TypeValue25 °CNIDMM_VAL_TEMP_THERMISTOR_CUSTOM

### NIDMM_ATTR_TEMP_THERMISTOR_TYPE

Specifies the type of thermistor used to measure the temperature. The default value is **NIDMM_VAL_TEMP_THERMISTOR_44006**.

#### Syntax

NIDMM_ATTR_TEMP_THERMISTOR_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150124 | ViInt32 | Read/Write | N/A |

#### Remarks

| Defined Values | Thermistor Type | Value | 25 °C |
| --- | --- | --- | --- |
| NIDMM_VAL_TEMP_THERMISTOR_CUSTOM | Custom | 0 | - |
| NIDMM_VAL_TEMP_THERMISTOR_44004 | 44004 | 1 | 2.25 k |
| NIDMM_VAL_TEMP_THERMISTOR_44006 | 44006 | 2 | 10 k |
| NIDMM_VAL_TEMP_THERMISTOR_44007 | 44007 | 3 | 5 k |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga7a505f672b1d9c381aeaecace5348383.html language=enus -->
## TOPIC 00045: NIDMM_ATTR_TEMP_RTD_TYPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga7a505f672b1d9c381aeaecace5348383.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga7a505f672b1d9c381aeaecace5348383.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of RTD used to measure temperature. The default value is NIDMM_VAL_TEMP_RTD_PT3851. SyntaxNIDMM_ATTR_TEMP_RTD_TYPENumeric ValueData TypeAccessApplies To1150120ViInt32Read/WriteN/ARemarksEnumStandardsMaterialTCRTypical R[0] (Ω)Callendar-Van Dusen CoefficientNotesNIDMM_VAL_TEMP_RTD_

### NIDMM_ATTR_TEMP_RTD_TYPE

Specifies the type of RTD used to measure temperature. The default value is **NIDMM_VAL_TEMP_RTD_PT3851**.

#### Syntax

NIDMM_ATTR_TEMP_RTD_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150120 | ViInt32 | Read/Write | N/A |

#### Remarks

| Enum | Standards | Material | TCR | Typical R0 (Ω) | Callendar-Van Dusen Coefficient | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| NIDMM_VAL_TEMP_RTD_CUSTOM | - | Varies | Varies | 100 Ω | A = user defined \| B = user defined \| C = user defined | User defines Callendar-Van Dusen A, B, and C coefficients with the NIDMM_ATTR_TEMP_RTD_A, NIDMM_ATTR_TEMP_RTD_B, and NIDMM_ATTR_TEMP_RTD_C attributes, respectively. |
| NIDMM_VAL_TEMP_RTD_PT3851 | IEC-751 \| DIN 43760 \| BS 1904 \| ASTM-E1137 \| EN-60751 | Platinum | 3851 | 100 Ω \| 1000 Ω | A = 3.9083 × 10–3 \| B = –5.775×10–7 \| C = –4.183×10–12 | Most common RTDs |
| NIDMM_VAL_TEMP_RTD_PT3750 | Low-cost vendor compliant RTD* | Platinum | 3750 | 1000 Ω | A = 3.81 × 10–3 \| B = –6.02×10–7 \| C = –6.0×10–12 | Low-cost RTD |
| NIDMM_VAL_TEMP_RTD_PT3916 | JISC 1604 | Platinum | 3916 | 100 Ω | A = 3.9739 × 10–3 \| B = –5.870×10–7 \| C = –4.4 ×10–12 | Used primarily in Japan |
| NIDMM_VAL_TEMP_RTD_PT3920 | US Industrial Standard D-100 \| American | Platinum | 3920 | 100 Ω | A = 3.9787 × 10–3 \| B = –5.8686×10–7 \| C = –4.167 ×10–12 | Low-cost RTD |
| NIDMM_VAL_TEMP_RTD_PT3911 | US Industrial Standard \| American | Platinum | 3911 | 100 Ω | A = 3.9692 × 10–3 \| B = –5.8495×10–7 \| C = –4.233 ×10–12 | Low-cost RTD |
| NIDMM_VAL_TEMP_RTD_PT3928 | ITS-90 | Platinum | 3928 | 100 Ω | A = 3.9888 × 10–3 \| B = –5.915×10–7 \| C = –3.85 ×10–12 | The definition of temperature |

*No standard. Check the Temperature Coefficient of Resistance (TCR).

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga86bb308ad0e2036ca6eb11a110dbc848.html language=enus -->
## TOPIC 00046: NIDMM_ATTR_TEMP_THERMISTOR_C

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga86bb308ad0e2036ca6eb11a110dbc848.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga86bb308ad0e2036ca6eb11a110dbc848.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type property is set to Custom. The default value is 1.568e-7 (44006). SyntaxNIDMM_ATTR_TEMP_THERMISTOR_CNumeric ValueData TypeAccessApplies To1150127ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_THERMISTOR_C

Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type property is set to Custom. The default value is 1.568e-7 (44006).

#### Syntax

NIDMM_ATTR_TEMP_THERMISTOR_C

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150127 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga87525f29a17b01d8c4fd8bb5d78f2c34.html language=enus -->
## TOPIC 00047: NIDMM_ATTR_TEMP_RTD_A

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga87525f29a17b01d8c4fd8bb5d78f2c34.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga87525f29a17b01d8c4fd8bb5d78f2c34.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is 3.9083e-3 (Pt3851). SyntaxNIDMM_ATTR_TEMP_RTD_ANumeric ValueData TypeAccessApplies To1150121ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_RTD_A

Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is 3.9083e-3 (Pt3851).

#### Syntax

NIDMM_ATTR_TEMP_RTD_A

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150121 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga8f84b8298ffab6163d0e85a69977e919.html language=enus -->
## TOPIC 00048: NIDMM_ATTR_TEMP_TRANSDUCER_TYPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga8f84b8298ffab6163d0e85a69977e919.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1ga8f84b8298ffab6163d0e85a69977e919.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of device used to measure the temperature. The default value is NIDMM_VAL_THERMOCOUPLE. SyntaxNIDMM_ATTR_TEMP_TRANSDUCER_TYPENumeric ValueData TypeAccessApplies To1250201ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_THERMOCOUPLE1 (0x1)ThermocoupleNIDMM_VA

### NIDMM_ATTR_TEMP_TRANSDUCER_TYPE

Specifies the type of device used to measure the temperature. The default value is **NIDMM_VAL_THERMOCOUPLE**.

#### Syntax

NIDMM_ATTR_TEMP_TRANSDUCER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250201 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_THERMOCOUPLE | 1 (0x1) | Thermocouple |
| NIDMM_VAL_THERMISTOR | 2 (0x2) | Thermistor |
| NIDMM_VAL_2_WIRE_RTD | 3 (0x3) | 2-wire RTD |
| NIDMM_VAL_4_WIRE_RTD | 4 (0x4) | 4-wire RTD |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1gaafb8a118648be6039922092b32fce9ce.html language=enus -->
## TOPIC 00049: NIDMM_ATTR_TEMP_RTD_RES

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1gaafb8a118648be6039922092b32fce9ce.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1gaafb8a118648be6039922092b32fce9ce.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs, including custom RTDs. The default value is 100 (Ω). SyntaxNIDMM_ATTR_TEMP_RTD_RESNumeric ValueData TypeAccessApplies To1250242ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_RTD_RES

Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs, including custom RTDs. The default value is 100 (Ω).

#### Syntax

NIDMM_ATTR_TEMP_RTD_RES

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250242 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1gaccc09b3e1f90da3646fa610bc2982e7a.html language=enus -->
## TOPIC 00050: NIDMM_ATTR_TEMP_THERMISTOR_B

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1gaccc09b3e1f90da3646fa610bc2982e7a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1gaccc09b3e1f90da3646fa610bc2982e7a.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type proerty is set to Custom. The default value is 0.0002391 (44006). SyntaxNIDMM_ATTR_TEMP_THERMISTOR_BNumeric ValueData TypeAccessApplies To1150126ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_THERMISTOR_B

Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type proerty is set to Custom. The default value is 0.0002391 (44006).

#### Syntax

NIDMM_ATTR_TEMP_THERMISTOR_B

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150126 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1gad2923828ae23d589a3a7baf7681a0d7d.html language=enus -->
## TOPIC 00051: NIDMM_ATTR_TEMP_RTD_C

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1gad2923828ae23d589a3a7baf7681a0d7d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1gad2923828ae23d589a3a7baf7681a0d7d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is -4.183e-12(Pt3851). SyntaxNIDMM_ATTR_TEMP_RTD_CNumeric ValueData TypeAccessApplies To1150123ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_RTD_C

Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property is set to Custom. The default value is -4.183e-12(Pt3851).

#### Syntax

NIDMM_ATTR_TEMP_RTD_C

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150123 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1gad2fca31173fe47913d482eeab54213e8.html language=enus -->
## TOPIC 00052: NIDMM_ATTR_TEMP_TC_TYPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1gad2fca31173fe47913d482eeab54213e8.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1gad2fca31173fe47913d482eeab54213e8.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of thermocouple used to measure the temperature. The default value is NIDMM_VAL_TEMP_TC_J. SyntaxNIDMM_ATTR_TEMP_TC_TYPENumeric ValueData TypeAccessApplies To1250231ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_TEMP_TC_B1 (0x1)Thermocouple type BNIDMM_VAL

### NIDMM_ATTR_TEMP_TC_TYPE

Specifies the type of thermocouple used to measure the temperature. The default value is **NIDMM_VAL_TEMP_TC_J**.

#### Syntax

NIDMM_ATTR_TEMP_TC_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250231 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_TEMP_TC_B | 1 (0x1) | Thermocouple type B |
| NIDMM_VAL_TEMP_TC_E | 4 (0x4) | Thermocouple type E |
| NIDMM_VAL_TEMP_TC_J | 6 (0x6) | Thermocouple type J |
| NIDMM_VAL_TEMP_TC_K | 7 (0x7) | Thermocouple type K |
| NIDMM_VAL_TEMP_TC_N | 8 (0x8) | Thermocouple type N |
| NIDMM_VAL_TEMP_TC_R | 9 (0x9) | Thermocouple type R |
| NIDMM_VAL_TEMP_TC_S | 10 (0xa) | Thermocouple type S |
| NIDMM_VAL_TEMP_TC_T | 11 (0xb) | Thermocouple type T |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__configuration__measurement__options__temperature_1gae19210a944b35ae6c0fc127bbad6dcf3.html language=enus -->
## TOPIC 00053: NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__configuration__measurement__options__temperature_1gae19210a944b35ae6c0fc127bbad6dcf3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__configuration__measurement__options__temperature_1gae19210a944b35ae6c0fc127bbad6dcf3.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. The default value is 25.0 (°C). SyntaxNIDMM_ATTR_TEMP_TC_FIXED_REF_JUNCNumeric ValueData TypeAccessApplies To1250233ViReal64Read/WriteN/A

### NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC

Specifies the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. The default value is 25.0 (°C).

#### Syntax

NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250233 | ViReal64 | Read/Write | N/A |

Parent topic:

Temperature

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__advanced__session__information.html language=enus -->
## TOPIC 00054: Advanced Session Information

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__advanced__session__information.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__advanced__session__information.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_DRIVER_SETUPThis attribute indicates the Driver Setup string that the user specified when initializing the driver. Some cases exist where the end-user must specify instrument driver options at initialization time. An example of this is specifying a pa

### Advanced Session Information

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_DRIVER_SETUP | This attribute indicates the Driver Setup string that the user specified when initializing the driver. Some cases exist where the end-user must specify instrument driver options at initialization time. An example of this is specifying a particular instrument model from among a family of instruments that the driver supports. This is useful when using simulation. The end-user can specify driver-specific options through the DriverSetup keyword in the Option_String parameter in niDMM_InitWithOptions. If the user does not specify a Driver Setup string, this attribute returns an empty string. |
| NIDMM_ATTR_IO_RESOURCE_DESCRIPTOR | The resource descriptor the driver uses to identify the physical device. |
| NIDMM_ATTR_LOGICAL_NAME | A string containing the logical name of the instrument. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__advanced__session__information_1gabda02fa5a6dc3ad29467bbf7c582956b.html language=enus -->
## TOPIC 00055: NIDMM_ATTR_LOGICAL_NAME

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__advanced__session__information_1gabda02fa5a6dc3ad29467bbf7c582956b.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__advanced__session__information_1gabda02fa5a6dc3ad29467bbf7c582956b.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the logical name of the instrument. SyntaxNIDMM_ATTR_LOGICAL_NAMENumeric ValueData TypeAccessApplies To1050305ViStringRead-OnlyN/A

### NIDMM_ATTR_LOGICAL_NAME

A string containing the logical name of the instrument.

#### Syntax

NIDMM_ATTR_LOGICAL_NAME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050305 | ViString | Read-Only | N/A |

Parent topic:

Advanced Session Information

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga0425db6e146ec5a1d32dd07b79f1f67a.html language=enus -->
## TOPIC 00056: NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga0425db6e146ec5a1d32dd07b79f1f67a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga0425db6e146ec5a1d32dd07b79f1f67a.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The prefix for the specific instrument driver. The name of each user-callable function in this driver starts with this prefix. The prefix can be up to a maximum of eight characters. SyntaxNIDMM_ATTR_SPECIFIC_DRIVER_PREFIXNumeric ValueData TypeAccessApplies To1050302ViStringRead-OnlyN/A

### NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX

The prefix for the specific instrument driver. The name of each user-callable function in this driver starts with this prefix. The prefix can be up to a maximum of eight characters.

#### Syntax

NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050302 | ViString | Read-Only | N/A |

Parent topic:

Driver Identification

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga233808cd0978178ad59a5dbce355cba5.html language=enus -->
## TOPIC 00057: NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga233808cd0978178ad59a5dbce355cba5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga233808cd0978178ad59a5dbce355cba5.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The major version number of the class specification for the specific driver. SyntaxNIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSIONNumeric ValueData TypeAccessApplies To1050515ViInt32Read-OnlyN/A

### NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION

The major version number of the class specification for the specific driver.

#### Syntax

NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050515 | ViInt32 | Read-Only | N/A |

Parent topic:

Driver Identification

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga80df0592d54549319b86bbfb8a9d90aa.html language=enus -->
## TOPIC 00058: NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga80df0592d54549319b86bbfb8a9d90aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1ga80df0592d54549319b86bbfb8a9d90aa.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the vendor of the specific driver. SyntaxNIDMM_ATTR_SPECIFIC_DRIVER_VENDORNumeric ValueData TypeAccessApplies To1050513ViStringRead-OnlyN/A

### NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR

A string containing the vendor of the specific driver.

#### Syntax

NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050513 | ViString | Read-Only | N/A |

Parent topic:

Driver Identification

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1gaba0be655050a777421e793fc789002bf.html language=enus -->
## TOPIC 00059: NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1gaba0be655050a777421e793fc789002bf.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__driver__identification_1gaba0be655050a777421e793fc789002bf.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The minor version number of the class specification for the specific driver. SyntaxNIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSIONNumeric ValueData TypeAccessApplies To1050516ViInt32Read-OnlyN/A

### NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION

The minor version number of the class specification for the specific driver.

#### Syntax

NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050516 | ViInt32 | Read-Only | N/A |

Parent topic:

Driver Identification

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__instrument__capabilities.html language=enus -->
## TOPIC 00060: Instrument Capabilities

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__instrument__capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__instrument__capabilities.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_CHANNEL_COUNTIndicates the number of channels that the specific instrument driver supports. For each attribute for which the IVI_VAL_MULTI_CHANNEL flag attribute is set, the IVI engine maintains a separate cache value for each channel. AttachmentsNone

### Instrument Capabilities

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_CHANNEL_COUNT | Indicates the number of channels that the specific instrument driver supports. For each attribute for which the IVI_VAL_MULTI_CHANNEL flag attribute is set, the IVI engine maintains a separate cache value for each channel. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__instrument__capabilities_1ga7426b5de403aec75303a4f8a84aaf153.html language=enus -->
## TOPIC 00061: NIDMM_ATTR_CHANNEL_COUNT

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__instrument__capabilities_1ga7426b5de403aec75303a4f8a84aaf153.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__instrument__capabilities_1ga7426b5de403aec75303a4f8a84aaf153.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of channels that the specific instrument driver supports. For each attribute for which the IVI_VAL_MULTI_CHANNEL flag attribute is set, the IVI engine maintains a separate cache value for each channel. SyntaxNIDMM_ATTR_CHANNEL_COUNTNumeric ValueData TypeAccessApplies To1050203Vi

### NIDMM_ATTR_CHANNEL_COUNT

Indicates the number of channels that the specific instrument driver supports. For each attribute for which the IVI_VAL_MULTI_CHANNEL flag attribute is set, the IVI engine maintains a separate cache value for each channel.

#### Syntax

NIDMM_ATTR_CHANNEL_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050203 | ViInt32 | Read-Only | N/A |

Parent topic:

Instrument Capabilities

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification.html language=enus -->
## TOPIC 00062: Instrument Identification

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_CONFIG_PRODUCT_NUMBERThe PCI product ID. NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISIONA string containing the instrument firmware revision number. NIDMM_ATTR_INSTRUMENT_MANUFACTURERA string containing the manufacturer of the instrument. NIDMM_ATTR_INSTRUMEN

### Instrument Identification

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_CONFIG_PRODUCT_NUMBER | The PCI product ID. |
| NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION | A string containing the instrument firmware revision number. |
| NIDMM_ATTR_INSTRUMENT_MANUFACTURER | A string containing the manufacturer of the instrument. |
| NIDMM_ATTR_INSTRUMENT_MODEL | A string containing the instrument model. |
| NIDMM_ATTR_SERIAL_NUMBER | A string containing the serial number of the instrument. This attribute corresponds to the serial number label that is attached to most products. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1ga0edabc633b8983da2b6c4edf42215a6e.html language=enus -->
## TOPIC 00063: NIDMM_ATTR_INSTRUMENT_MANUFACTURER

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1ga0edabc633b8983da2b6c4edf42215a6e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1ga0edabc633b8983da2b6c4edf42215a6e.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the manufacturer of the instrument. SyntaxNIDMM_ATTR_INSTRUMENT_MANUFACTURERNumeric ValueData TypeAccessApplies To1050511ViStringRead-OnlyN/A

### NIDMM_ATTR_INSTRUMENT_MANUFACTURER

A string containing the manufacturer of the instrument.

#### Syntax

NIDMM_ATTR_INSTRUMENT_MANUFACTURER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050511 | ViString | Read-Only | N/A |

Parent topic:

Instrument Identification

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1gae0e26e94ca998b04418eb30dd9f861ae.html language=enus -->
## TOPIC 00064: NIDMM_ATTR_INSTRUMENT_MODEL

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1gae0e26e94ca998b04418eb30dd9f861ae.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1gae0e26e94ca998b04418eb30dd9f861ae.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the instrument model. SyntaxNIDMM_ATTR_INSTRUMENT_MODELNumeric ValueData TypeAccessApplies To1050512ViStringRead-OnlyN/A

### NIDMM_ATTR_INSTRUMENT_MODEL

A string containing the instrument model.

#### Syntax

NIDMM_ATTR_INSTRUMENT_MODEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050512 | ViString | Read-Only | N/A |

Parent topic:

Instrument Identification

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1gae968e048b103858075bccbdbf9c994d4.html language=enus -->
## TOPIC 00065: NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1gae968e048b103858075bccbdbf9c994d4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__instrument__identification_1gae968e048b103858075bccbdbf9c994d4.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the instrument firmware revision number. SyntaxNIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISIONNumeric ValueData TypeAccessApplies To1050510ViStringRead-OnlyN/ARemarksHigh-Level Functions:niDMM_revision_query

### NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION

A string containing the instrument firmware revision number.

#### Syntax

NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050510 | ViString | Read-Only | N/A |

#### Remarks

**High-Level Functions**:

- [niDMM_revision_query](group____root__nidmm__functions__utility_1gaac28514579ed2de97dfd45b91b4a6d67.html)

Parent topic:

Instrument Identification

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities.html language=enus -->
## TOPIC 00066: Specific Driver Capabilities

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_GROUP_CAPABILITIESA string containing the capabilities and extension groups supported by the specific driver. NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELSA string containing the instrument models supported by the specific driver. AttachmentsNone

### Specific Driver Capabilities

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_GROUP_CAPABILITIES | A string containing the capabilities and extension groups supported by the specific driver. |
| NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS | A string containing the instrument models supported by the specific driver. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities_1ga5bc4c67ae003110fb47d587292a7197d.html language=enus -->
## TOPIC 00067: NIDMM_ATTR_GROUP_CAPABILITIES

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities_1ga5bc4c67ae003110fb47d587292a7197d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities_1ga5bc4c67ae003110fb47d587292a7197d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the capabilities and extension groups supported by the specific driver. SyntaxNIDMM_ATTR_GROUP_CAPABILITIESNumeric ValueData TypeAccessApplies To1050401ViStringRead-OnlyN/A

### NIDMM_ATTR_GROUP_CAPABILITIES

A string containing the capabilities and extension groups supported by the specific driver.

#### Syntax

NIDMM_ATTR_GROUP_CAPABILITIES

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050401 | ViString | Read-Only | N/A |

Parent topic:

Specific Driver Capabilities

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities_1gaddede69dbabecde313e22ff82ac2fa89.html language=enus -->
## TOPIC 00068: NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities_1gaddede69dbabecde313e22ff82ac2fa89.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__specific__driver__capabilities_1gaddede69dbabecde313e22ff82ac2fa89.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the instrument models supported by the specific driver. SyntaxNIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELSNumeric ValueData TypeAccessApplies To1050327ViStringRead-OnlyN/A

### NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS

A string containing the instrument models supported by the specific driver.

#### Syntax

NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050327 | ViString | Read-Only | N/A |

Parent topic:

Specific Driver Capabilities

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__user__options.html language=enus -->
## TOPIC 00069: User Options

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__user__options.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__user__options.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_CACHESpecifies whether to cache the value of attributes. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, it significantly increases execution

### User Options

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_CACHE | Specifies whether to cache the value of attributes. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, it significantly increases execution speed. The instrument driver can choose to always cache or to never cache particular attributes regardless of the setting of this attribute. The default value is VI_TRUE (1). Use the niDMM_InitWithOptions function to override this setting. |
| NIDMM_ATTR_INTERCHANGE_CHECK | Specifies whether to perform interchangeability checking and log interchangeability warnings when you call niDMM functions. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Use niDMM_GetNextInterchangeWarning to extract interchange warnings. Use niDMM_ClearInterchangeWarnings to clear the list of interchangeability warnings without reading them. Interchangeability checking examines the attributes in a capability group only if you specify a value for at least one attribute within that group. Interchangeability warnings can occur when an attribute affects the behavior of the instrument and you have not set that attribute, or the attribute has been invalidated since you set it. |
| NIDMM_ATTR_QUERY_INSTRUMENT_STATUS | Specifies whether the instrument driver queries the instrument status after each operation. Querying the instrument status is very useful for debugging. After the user program is validated, this attribute can be set to VI_FALSE (0) to disable status checking and maximize performance. The instrument driver can choose to ignore status checking for particular attributes regardless of the setting of this attribute. The default value is VI_TRUE (1). Use niDMM_InitWithOptions to override this setting. |
| NIDMM_ATTR_RANGE_CHECK | Specifies whether to validate attribute values and function parameters. If enabled, the instrument driver validates the parameter values passed to driver functions. Range checking parameters is very useful for debugging. After the user program is validated, this attribute can be set to VI_FALSE (0) to disable range checking and maximize performance. The default value is VI_TRUE (1). Use the niDMM_InitWithOptions function to override this setting. |
| NIDMM_ATTR_RECORD_COERCIONS | Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 attributes. Call niDMM_GetNextCoercionRecord to extract and delete the oldest coercion record from the list. The default value is VI_FALSE (0). Use the niDMM_InitWithOptions function to override this setting. |
| NIDMM_ATTR_SIMULATE | Specifies whether or not to simulate instrument driver I/O operations. If simulation is enabled, instrument driver functions perform range checking and call IVI Get and Set functions, but they do not perform instrument I/O. For output parameters that represent instrument data, the instrument driver functions return calculated values. The default value is VI_FALSE (0). Use the niDMM_InitWithOptions function to override this setting. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1ga6553fcc3a6421ececf8f1bcbaf271c35.html language=enus -->
## TOPIC 00070: NIDMM_ATTR_RANGE_CHECK

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1ga6553fcc3a6421ececf8f1bcbaf271c35.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1ga6553fcc3a6421ececf8f1bcbaf271c35.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to validate attribute values and function parameters. If enabled, the instrument driver validates the parameter values passed to driver functions. Range checking parameters is very useful for debugging. After the user program is validated, this attribute can be set to VI_FALSE (0)

### NIDMM_ATTR_RANGE_CHECK

Specifies whether to validate attribute values and function parameters. If enabled, the instrument driver validates the parameter values passed to driver functions. Range checking parameters is very useful for debugging. After the user program is validated, this attribute can be set to VI_FALSE (0) to disable range checking and maximize performance. The default value is VI_TRUE (1). Use the [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html) function to override this setting.

#### Syntax

NIDMM_ATTR_RANGE_CHECK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050002 | ViBoolean | Read/Write | N/A |

#### Remarks

**High-Level Functions**:

- [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html)

Parent topic:

User Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1ga99bd8400a88708a6210dc75177c3ab3c.html language=enus -->
## TOPIC 00071: NIDMM_ATTR_QUERY_INSTRUMENT_STATUS

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1ga99bd8400a88708a6210dc75177c3ab3c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1ga99bd8400a88708a6210dc75177c3ab3c.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the instrument driver queries the instrument status after each operation. Querying the instrument status is very useful for debugging. After the user program is validated, this attribute can be set to VI_FALSE (0) to disable status checking and maximize performance. The instrument

### NIDMM_ATTR_QUERY_INSTRUMENT_STATUS

Specifies whether the instrument driver queries the instrument status after each operation. Querying the instrument status is very useful for debugging. After the user program is validated, this attribute can be set to VI_FALSE (0) to disable status checking and maximize performance. The instrument driver can choose to ignore status checking for particular attributes regardless of the setting of this attribute. The default value is VI_TRUE (1). Use [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html) to override this setting.

#### Syntax

NIDMM_ATTR_QUERY_INSTRUMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050003 | ViBoolean | Read/Write | N/A |

#### Remarks

**High-Level Functions**:

- [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html)

Parent topic:

User Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gabfe497b41f7f71250256162146f8c8fa.html language=enus -->
## TOPIC 00072: NIDMM_ATTR_SIMULATE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gabfe497b41f7f71250256162146f8c8fa.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gabfe497b41f7f71250256162146f8c8fa.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether or not to simulate instrument driver I/O operations. If simulation is enabled, instrument driver functions perform range checking and call IVI Get and Set functions, but they do not perform instrument I/O. For output parameters that represent instrument data, the instrument driver

### NIDMM_ATTR_SIMULATE

Specifies whether or not to simulate instrument driver I/O operations. If simulation is enabled, instrument driver functions perform range checking and call IVI Get and Set functions, but they do not perform instrument I/O. For output parameters that represent instrument data, the instrument driver functions return calculated values. The default value is VI_FALSE (0). Use the [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html) function to override this setting.

#### Syntax

NIDMM_ATTR_SIMULATE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050005 | ViBoolean | Read/Write | N/A |

#### Remarks

Note

Simulate can only be set within the [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html) function. The attribute value cannot be changed outside of the function.

**High-Level Functions**:

- [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html)

Parent topic:

User Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gada5104e6a69e8004f5787ddcde40614c.html language=enus -->
## TOPIC 00073: NIDMM_ATTR_RECORD_COERCIONS

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gada5104e6a69e8004f5787ddcde40614c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gada5104e6a69e8004f5787ddcde40614c.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 attributes. Call niDMM_GetNextCoercionRecord to extract and delete the oldest coercion record from the list. The default value is VI_FALSE (0). Use the niDMM_InitWithOptions function to override th

### NIDMM_ATTR_RECORD_COERCIONS

Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 attributes. Call [niDMM_GetNextCoercionRecord](group____root__nidmm__functions__utility__coercion__info_1gaab5bff9e6a4c3ee7dcbcbcfb99ba4975.html) to extract and delete the oldest coercion record from the list. The default value is VI_FALSE (0). Use the [niDMM_InitWithOptions](group____root__nidmm__functions__init__and__close_1ga37fc7589699ef16ff85d4c5796dda25b.html) function to override this setting.

#### Syntax

NIDMM_ATTR_RECORD_COERCIONS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050006 | ViBoolean | Read/Write | N/A |

Parent topic:

User Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gadd722cbed23251ceaab7f816b9181532.html language=enus -->
## TOPIC 00074: NIDMM_ATTR_INTERCHANGE_CHECK

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gadd722cbed23251ceaab7f816b9181532.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__inherent__ivi__attributes__user__options_1gadd722cbed23251ceaab7f816b9181532.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to perform interchangeability checking and log interchangeability warnings when you call niDMM functions. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Use niDMM_GetNextInterchangeWarning to extract inte

### NIDMM_ATTR_INTERCHANGE_CHECK

Specifies whether to perform interchangeability checking and log interchangeability warnings when you call niDMM functions. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Use [niDMM_GetNextInterchangeWarning](group____root__nidmm__functions__utility__interchangeability__info_1gac3b9fda01009a9105a4399927c0fc0bd.html) to extract interchange warnings. Use [niDMM_ClearInterchangeWarnings](group____root__nidmm__functions__utility__interchangeability__info_1ga17f9f8a7111717ee46562113282b2c29.html) to clear the list of interchangeability warnings without reading them. Interchangeability checking examines the attributes in a capability group only if you specify a value for at least one attribute within that group. Interchangeability warnings can occur when an attribute affects the behavior of the instrument and you have not set that attribute, or the attribute has been invalidated since you set it.

#### Syntax

NIDMM_ATTR_INTERCHANGE_CHECK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050021 | ViBoolean | Read/Write | N/A |

#### Remarks

**Defined Values**

|  |  |  |
| --- | --- | --- |
| VI_FALSE (default) | 0 | False |
| VI_TRUE | 1 | True |

**High-Level Functions**:

- [niDMM_GetNextInterchangeWarning](group____root__nidmm__functions__utility__interchangeability__info_1gac3b9fda01009a9105a4399927c0fc0bd.html)
- [niDMM_ClearInterchangeWarnings](group____root__nidmm__functions__utility__interchangeability__info_1ga17f9f8a7111717ee46562113282b2c29.html)

Parent topic:

User Options

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__multi__point__acquisition_1ga331bbbb4fd4f28b75c527ce0c366f295.html language=enus -->
## TOPIC 00075: NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__multi__point__acquisition_1ga331bbbb4fd4f28b75c527ce0c366f295.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__multi__point__acquisition_1ga331bbbb4fd4f28b75c527ce0c366f295.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge of the signal from the specified sample trigger source on which the DMM is triggered. SyntaxNIDMM_ATTR_SAMPLE_TRIGGER_SLOPENumeric ValueData TypeAccessApplies To1150010ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_POSITIVE0 (0x0)Rising Edge: The driver tr

### NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE

Specifies the edge of the signal from the specified sample trigger source on which the DMM is triggered.

#### Syntax

NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150010 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_POSITIVE | 0 (0x0) | Rising Edge: The driver triggers on the rising edge of the trigger signal. |
| NIDMM_VAL_NEGATIVE | 1 (0x1) | Falling Edge (default): The driver triggers on the falling edge of the trigger signal. |

Parent topic:

Multi Point Acquisition

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__multi__point__acquisition_1ga751b27c60d840c78549f5ae6881c84fa.html language=enus -->
## TOPIC 00076: NIDMM_ATTR_SAMPLE_INTERVAL

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__multi__point__acquisition_1ga751b27c60d840c78549f5ae6881c84fa.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__multi__point__acquisition_1ga751b27c60d840c78549f5ae6881c84fa.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time in seconds the DMM waits between measurement cycles. This attribute only applies when the NIDMM_ATTR_SAMPLE_TRIGGER attribute is set to INTERVAL. The default value (–1) ensures that the DMM settles for a recommended time, which is the same as using an immediate trigger.

### NIDMM_ATTR_SAMPLE_INTERVAL

Specifies the amount of time in seconds the DMM waits between measurement cycles. This attribute only applies when the [NIDMM_ATTR_SAMPLE_TRIGGER](group____root__nidmm__attributes__multi__point__acquisition_1ga26124054ec7546eac6f1653aa20b6e12.html) attribute is set to INTERVAL. The default value (–1) ensures that the DMM settles for a recommended time, which is the same as using an immediate trigger.

#### Syntax

NIDMM_ATTR_SAMPLE_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250303 | ViReal64 | Read/Write | N/A |

#### Remarks

The NI 4065, NI 4070/4071/4072, and the NI 4080/4081/4082 use the value specified in this attribute as additional delay. On these devices, the onboard timing resolution is 34.72 ns and the valid range is 0–149 s.

Only positive values are valid when setting the sample interval.

**High-Level Functions**:

- [niDMM_ConfigureMultiPoint](group____root__nidmm__functions__configuration_1gafa8c63af0899ee7c9208c2ff01d0e2ef.html)

Parent topic:

Multi Point Acquisition

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__multi__point__acquisition_1gaa530bee8d5ae4bca424e2c30c88f1730.html language=enus -->
## TOPIC 00077: NIDMM_ATTR_SAMPLE_COUNT

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__multi__point__acquisition_1gaa530bee8d5ae4bca424e2c30c88f1730.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__multi__point__acquisition_1gaa530bee8d5ae4bca424e2c30c88f1730.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of measurements the DMM takes each time it receives a trigger in Multiple Point Acquisitions. SyntaxNIDMM_ATTR_SAMPLE_COUNTNumeric ValueData TypeAccessApplies To1250301ViInt32Read/WriteN/ARemarksHigh-Level Functions:niDMM_ConfigureMultiPoint

### NIDMM_ATTR_SAMPLE_COUNT

Specifies the number of measurements the DMM takes each time it receives a trigger in [Multiple Point Acquisitions](https://www.ni.com/docs/en-US/bundle/ni-dmm/page/multiple-point-acquisitions.html).

#### Syntax

NIDMM_ATTR_SAMPLE_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250301 | ViInt32 | Read/Write | N/A |

#### Remarks

**High-Level Functions**:

- [niDMM_ConfigureMultiPoint](group____root__nidmm__functions__configuration_1gafa8c63af0899ee7c9208c2ff01d0e2ef.html)

Parent topic:

Multi Point Acquisition

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__multi__point__acquisition__advanced.html language=enus -->
## TOPIC 00078: Advanced

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__multi__point__acquisition__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__multi__point__acquisition__advanced.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_BUFFER_SIZESize in samples of the internal data buffer. Maximum is 134,217,727 (0X7FFFFFF) samples. When set to NIDMM_VAL_BUFFER_SIZE_AUTO(–1), NI-DMM chooses the buffer size. NIDMM_ATTR_LATENCYSpecifies the number of measurements transferred at a tim

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_BUFFER_SIZE | Size in samples of the internal data buffer. Maximum is 134,217,727 (0X7FFFFFF) samples. When set to NIDMM_VAL_BUFFER_SIZE_AUTO(–1), NI-DMM chooses the buffer size. |
| NIDMM_ATTR_LATENCY | Specifies the number of measurements transferred at a time from the instrument to an internal buffer. When set to NIDMM_VAL_LATENCY_AUTO (-1), NI-DMM chooses the transfer size. |

#### Attachments

None

Parent topic:

Multi Point Acquisition

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__multi__point__acquisition__advanced_1gac0e5663b86151913f9326a833f6d62bb.html language=enus -->
## TOPIC 00079: NIDMM_ATTR_LATENCY

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__multi__point__acquisition__advanced_1gac0e5663b86151913f9326a833f6d62bb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__multi__point__acquisition__advanced_1gac0e5663b86151913f9326a833f6d62bb.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of measurements transferred at a time from the instrument to an internal buffer. When set to NIDMM_VAL_LATENCY_AUTO (-1), NI-DMM chooses the transfer size. SyntaxNIDMM_ATTR_LATENCYNumeric ValueData TypeAccessApplies To1150034ViInt32Read/WriteN/A

### NIDMM_ATTR_LATENCY

Specifies the number of measurements transferred at a time from the instrument to an internal buffer. When set to **NIDMM_VAL_LATENCY_AUTO** (-1), NI-DMM chooses the transfer size.

#### Syntax

NIDMM_ATTR_LATENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150034 | ViInt32 | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__multi__point__acquisition__advanced_1gaf42ef835f3d9e6a4d1cef3912d25d859.html language=enus -->
## TOPIC 00080: NIDMM_ATTR_BUFFER_SIZE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__multi__point__acquisition__advanced_1gaf42ef835f3d9e6a4d1cef3912d25d859.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__multi__point__acquisition__advanced_1gaf42ef835f3d9e6a4d1cef3912d25d859.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Size in samples of the internal data buffer. Maximum is 134,217,727 (0X7FFFFFF) samples. When set to NIDMM_VAL_BUFFER_SIZE_AUTO(–1), NI-DMM chooses the buffer size. SyntaxNIDMM_ATTR_BUFFER_SIZENumeric ValueData TypeAccessApplies To1150037ViInt32Read/WriteN/A

### NIDMM_ATTR_BUFFER_SIZE

Size in samples of the internal data buffer. Maximum is 134,217,727 (0X7FFFFFF) samples. When set to **NIDMM_VAL_BUFFER_SIZE_AUTO**(–1), NI-DMM chooses the buffer size.

#### Syntax

NIDMM_ATTR_BUFFER_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150037 | ViInt32 | Read/Write | N/A |

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__trigger.html language=enus -->
## TOPIC 00081: Trigger

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__trigger.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_MEAS_COMPLETE_DESTSpecifies the destination of the measurement complete signal. NIDMM_ATTR_MEAS_DEST_SLOPESpecifies the polarity of the generated measurement complete signal. NIDMM_ATTR_TRIGGER_DELAYSpecifies the time (in seconds) that the DMM waits a

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_MEAS_COMPLETE_DEST | Specifies the destination of the measurement complete signal. |
| NIDMM_ATTR_MEAS_DEST_SLOPE | Specifies the polarity of the generated measurement complete signal. |
| NIDMM_ATTR_TRIGGER_DELAY | Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking the measurement. (–1) signifies that AUTO DELAY is on, and (–2) signifies that AUTO DELAY is off. |
| NIDMM_ATTR_TRIGGER_SLOPE | Specifies the edge of the signal from the specified trigger source on which the DMM is triggered. |
| NIDMM_ATTR_TRIGGER_SOURCE | Specifies the trigger source. When niDMM_Initiate is called, the DMM waits for the trigger specified with this attribute. After it receives the trigger, the DMM waits the length of time specified with the NIDMM_ATTR_TRIGGER_DELAY attribute. The DMM then takes a measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__trigger_1ga3a2cf8a781d4c42325a63772031bb69d.html language=enus -->
## TOPIC 00082: NIDMM_ATTR_MEAS_COMPLETE_DEST

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__trigger_1ga3a2cf8a781d4c42325a63772031bb69d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__trigger_1ga3a2cf8a781d4c42325a63772031bb69d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination of the measurement complete signal. SyntaxNIDMM_ATTR_MEAS_COMPLETE_DESTNumeric ValueData TypeAccessApplies To1250305ViInt32Read/WriteN/ARemarksTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section.High-Level Functions:ni

### NIDMM_ATTR_MEAS_COMPLETE_DEST

Specifies the destination of the measurement complete signal.

#### Syntax

NIDMM_ATTR_MEAS_COMPLETE_DEST

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250305 | ViInt32 | Read/Write | N/A |

#### Remarks

Note

To determine which values are supported by each device, refer to the [LabWindows/CVI Trigger Routing](https://www.ni.com/docs/en-US/bundle/ni-dmm/page/labwindowscvi-trigger-routing.html) section.

**High-Level Functions**:

- [niDMM_ConfigureMeasCompleteDest](group____root__nidmm__functions__configuration__trigger_1gace458c1f945337e2b25a961fe39a46b2.html)

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__trigger_1ga6225fcae372d476927dc42697ff3e014.html language=enus -->
## TOPIC 00083: NIDMM_ATTR_MEAS_DEST_SLOPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__trigger_1ga6225fcae372d476927dc42697ff3e014.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__trigger_1ga6225fcae372d476927dc42697ff3e014.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the generated measurement complete signal. SyntaxNIDMM_ATTR_MEAS_DEST_SLOPENumeric ValueData TypeAccessApplies To1150002ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_POSITIVE0 (0x0)Rising Edge: The driver triggers on the rising edge of the trigger

### NIDMM_ATTR_MEAS_DEST_SLOPE

Specifies the polarity of the generated measurement complete signal.

#### Syntax

NIDMM_ATTR_MEAS_DEST_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150002 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_POSITIVE | 0 (0x0) | Rising Edge: The driver triggers on the rising edge of the trigger signal. |
| NIDMM_VAL_NEGATIVE | 1 (0x1) | Falling Edge (default): The driver triggers on the falling edge of the trigger signal. |

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__trigger_1ga7c7f4ceab117fbad76ea5426be6c0eea.html language=enus -->
## TOPIC 00084: NIDMM_ATTR_TRIGGER_SLOPE

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__trigger_1ga7c7f4ceab117fbad76ea5426be6c0eea.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__trigger_1ga7c7f4ceab117fbad76ea5426be6c0eea.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge of the signal from the specified trigger source on which the DMM is triggered. SyntaxNIDMM_ATTR_TRIGGER_SLOPENumeric ValueData TypeAccessApplies To1250334ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_POSITIVE0 (0x0)Rising Edge: The driver triggers on the

### NIDMM_ATTR_TRIGGER_SLOPE

Specifies the edge of the signal from the specified trigger source on which the DMM is triggered.

#### Syntax

NIDMM_ATTR_TRIGGER_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250334 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_POSITIVE | 0 (0x0) | Rising Edge: The driver triggers on the rising edge of the trigger signal. |
| NIDMM_VAL_NEGATIVE | 1 (0x1) | Falling Edge (default): The driver triggers on the falling edge of the trigger signal. |

**High-Level Functions**:

- [niDMM_ConfigureTriggerSlope](group____root__nidmm__functions__configuration__trigger_1gaa6de5febf9b7e490238c3f7e6037c9ea.html)
- [niDMM_ConfigureSampleTriggerSlope](group____root__nidmm__functions__configuration__trigger_1gaaa739402e7f6362ad3fb47bf8955ce7e.html)

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__waveform__acquisition.html language=enus -->
## TOPIC 00085: Waveform Acquisition

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__waveform__acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__waveform__acquisition.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDMM_ATTR_WAVEFORM_COUPLINGFor the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the coupling during a waveform acquisition. NIDMM_ATTR_WAVEFORM_POINTSFor the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the number of points to acquire in a wave

### Waveform Acquisition

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDMM_ATTR_WAVEFORM_COUPLING | For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the coupling during a waveform acquisition. |
| NIDMM_ATTR_WAVEFORM_POINTS | For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition. |
| NIDMM_ATTR_WAVEFORM_RATE | For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s). The valid range is 10.0–1,800,000 S/s. Values are coerced to the closest integer divisor of 1,800,000. The default value is 1,800,000. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__attributes__waveform__acquisition_1ga2d796d4b5630fedd8b90cb7f4ba4209d.html language=enus -->
## TOPIC 00086: NIDMM_ATTR_WAVEFORM_COUPLING

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__attributes__waveform__acquisition_1ga2d796d4b5630fedd8b90cb7f4ba4209d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__attributes__waveform__acquisition_1ga2d796d4b5630fedd8b90cb7f4ba4209d.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the coupling during a waveform acquisition. SyntaxNIDMM_ATTR_WAVEFORM_COUPLINGNumeric ValueData TypeAccessApplies To1150027ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDMM_VAL_WAVEFORM_COUPLING_AC0 (0x0)AC couplingNIDMM_VA

### NIDMM_ATTR_WAVEFORM_COUPLING

For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the coupling during a waveform acquisition.

#### Syntax

NIDMM_ATTR_WAVEFORM_COUPLING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150027 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDMM_VAL_WAVEFORM_COUPLING_AC | 0 (0x0) | AC coupling |
| NIDMM_VAL_WAVEFORM_COUPLING_DC | 1 (0x1) | DC coupling |

**High-Level Functions**:

- [niDMM_ConfigureWaveformCoupling](group____root__nidmm__functions__configuration_1ga6ae9f033e11d57b756c364f87cb02cbb.html)

Parent topic:

Waveform Acquisition

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions.html language=enus -->
## TOPIC 00087: Functions

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAcquisitionCalibrationConfigurationInit and CloseUtilityGroup membersNoneAttachmentsNone

### Functions

#### Groups

- Acquisition
- Calibration
- Configuration
- Init and Close
- Utility

#### Group members

None

#### Attachments

None

Parent topic:

nidmm.h

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__acquisition.html language=enus -->
## TOPIC 00088: Acquisition

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__acquisition.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsLow-Level AcquisitionGroup membersNameDescriptionniDMM_IsOverRangeTakes a measurementValue and determines if the value is a valid measurement or a value indicating that an overrange condition occurred. niDMM_IsUnderRangeTakes a measurementValue and determines if the value is a valid measuremen

### Acquisition

#### Groups

- Low-Level Acquisition

#### Group members

| Name | Description |
| --- | --- |
| niDMM_IsOverRange | Takes a measurementValue and determines if the value is a valid measurement or a value indicating that an overrange condition occurred. |
| niDMM_IsUnderRange | Takes a measurementValue and determines if the value is a valid measurement or a value indicating that an underrange condition occurred. |
| niDMM_Read | Acquires a single measurement and returns the measured value in base units. |
| niDMM_ReadMultiPoint | Acquires multiple measurements and returns an array of measured values in base units. The number of measurements the DMM makes is determined by the values you specify for the Trigger_Count and Sample_Count parameters in niDMM_ConfigureMultiPoint. |
| niDMM_ReadWaveform | For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform and returns data as an array of values or as a waveform data type. The number of elements in the waveformArray is determined by the values you specify for the Waveform_Points parameter in niDMM_ConfigureWaveformAcquisition. Measured values are in base units. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__acquisition_1gabcc3e11bef223a226e10513387863ba1.html language=enus -->
## TOPIC 00089: niDMM_Read

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__acquisition_1gabcc3e11bef223a226e10513387863ba1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__acquisition_1gabcc3e11bef223a226e10513387863ba1.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires a single measurement and returns the measured value in base units. SyntaxViStatus _VI_FUNC niDMM_Read(ViSession vi, ViInt32 maximumTime, ViReal64 *reading)ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies a particular instrument session. You obtain the Instrument_Handle parame

### niDMM_Read

Acquires a single measurement and returns the measured value in base units.

#### Syntax

ViStatus _VI_FUNC niDMM_Read(ViSession vi, ViInt32 maximumTime, ViReal64 *reading)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. You obtain the Instrument_Handle parameter from niDMM_init or niDMM_InitWithOptions. The default is None. |
| maximumTime | [in] | ViInt32 | Specifies the maximumTime allowed for this function to complete in milliseconds. If the function does not complete within this time interval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED error code. This may happen if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete.The valid range is 0—86400000. The default value is NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout automatically. |
| reading | [out] | ViReal64 * | The measured value returned from the DMM. |

#### Returns

Reports the **Status** of this operation. To obtain a text description of the status code, call [niDMM_GetErrorMessage](group____root__nidmm__functions__utility__error__handling_1gaaddeed5a573a6aa4afc5f8589ed6a131.html). To obtain additional information concerning the error condition, use [niDMM_GetError](group____root__nidmm__functions__utility__error__handling_1ga3ce9352c8cf141a6ca9710adbaba92cd.html).

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__acquisition__lowlevel__acquisition.html language=enus -->
## TOPIC 00090: Low-Level Acquisition

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__acquisition__lowlevel__acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__acquisition__lowlevel__acquisition.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDMM_AbortAborts a previously initiated measurement and returns the DMM to the Idle state. niDMM_ControlControls the DMM. Use this function if you want a parameter change to be immediately reflected in the hardware. Use this function before calling niDMM_Initia

### Low-Level Acquisition

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDMM_Abort | Aborts a previously initiated measurement and returns the DMM to the Idle state. |
| niDMM_Control | Controls the DMM. Use this function if you want a parameter change to be immediately reflected in the hardware. Use this function before calling niDMM_Initiate to make the initiate call as quickly as possible. |
| niDMM_Fetch | Returns the value from a previously initiated measurement. You must call niDMM_Initiate before calling this function. Measured value is in base units. |
| niDMM_FetchMultiPoint | / Returns an array of values from a previously initiated multipoint measurement. The number of measurements the DMM makes is determined by the values you specify for the Trigger_Count and Sample_Count parameters of niDMM_ConfigureMultiPoint. You must first call niDMM_Initiate to initiate a measurement before calling this function. Measured values are in base units. |
| niDMM_FetchWaveform | For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of values from a previously initiated waveform acquisition. You must call niDMM_Initiate before calling this function. Measured values are in base units. |
| niDMM_Initiate | Initiates an acquisition. After you call this function, the DMM leaves the Idle state and enters the Wait-for-Trigger state. If trigger is set to Immediate mode, the DMM begins acquiring measurement data. Use niDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform to retrieve the measurement data. |
| niDMM_ReadStatus | Returns measurement backlog and acquisition status. Use this function to determine how many measurements are available before calling niDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform. |

#### Attachments

None

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__calibration__calibration__utility.html language=enus -->
## TOPIC 00091: Calibration Utility

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__calibration__calibration__utility.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__calibration__calibration__utility.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDMM_GetCalCountReturns the calibration count for the specified type of calibration. niDMM_GetCalDateAndTimeReturns the date and time of the last calibration performed. niDMM_GetCalUserDefinedInfoReturns the user-defined calibration information stored in the EE

### Calibration Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDMM_GetCalCount | Returns the calibration count for the specified type of calibration. |
| niDMM_GetCalDateAndTime | Returns the date and time of the last calibration performed. |
| niDMM_GetCalUserDefinedInfo | Returns the user-defined calibration information stored in the EEPROM. |
| niDMM_GetCalUserDefinedInfoMaxSize | Returns the maximum string length that can be stored in the EEPROM. Use niDMM_SetCalUserDefinedInfo to store user-defined information. |
| niDMM_GetDevTemp | Returns the current temperature of the device. |
| niDMM_GetExtCalRecommendedInterval | Returns the recommended interval between external recalibration in months. |
| niDMM_GetLastCalTemp | Returns the temperature during the last calibration procedure. |
| niDMM_GetSelfCalSupported | Returns a Boolean value that expresses whether or not the DMM that you are using can perform self-calibration. |
| niDMM_RestoreLastExtCalConstants | Reverts the device to the calibration constants from the last complete external calibration. This function recovers the hardware if a fatal system error should occur during an external or self-calibration procedure. |
| niDMM_SetCalPassword | Changes the password required to enable external calibration functionality for the specified instrument. The maximum password string length is eight characters, excluding the termination character. "NI" is the default password. |
| niDMM_SetCalUserDefinedInfo | Stores the user-defined information in the EEPROM. Use niDMM_GetCalUserDefinedInfoMaxSize to learn the maximum string size that is allowed. If the info string size is larger than the maximum string size, NI-DMM stores as much of the information as possible, truncates the remainder, and returns a warning. |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__calibration__calibration__utility_1ga2d493dcdc64b601076366b77070bc243.html language=enus -->
## TOPIC 00092: niDMM_GetCalDateAndTime

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__calibration__calibration__utility_1ga2d493dcdc64b601076366b77070bc243.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__calibration__calibration__utility_1ga2d493dcdc64b601076366b77070bc243.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last calibration performed. SyntaxViStatus _VI_FUNC niDMM_GetCalDateAndTime(ViSession vi, ViInt32 calType, ViInt32 *month, ViInt32 *day, ViInt32 *year, ViInt32 *hour, ViInt32 *minute)RemarksThe NI 4050 and NI 4060 are not supported.ParametersNameDirectionTypeDescript

### niDMM_GetCalDateAndTime

Returns the date and time of the last calibration performed.

#### Syntax

ViStatus _VI_FUNC niDMM_GetCalDateAndTime(ViSession vi, ViInt32 calType, ViInt32 *month, ViInt32 *day, ViInt32 *year, ViInt32 *hour, ViInt32 *minute)

#### Remarks

Note

The NI 4050 and NI 4060 are not supported.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. You obtain the Instrument_Handle parameter from niDMM_init or niDMM_InitWithOptions. The default is None. |
| calType | [in] | ViInt32 | Specifies the type of calibration performed (external or self-calibration).Defined Values:NameValueDescriptionNIDMM_VAL_INTERNAL_AREA0 (0x0)Self-Calibration Note: The NI 4065 does not support self-calibration.NIDMM_VAL_EXTERNAL_AREA1 (0x1)External Calibration |
| Name | Value | Description |  |
| NIDMM_VAL_INTERNAL_AREA | 0 (0x0) | Self-Calibration Note: The NI 4065 does not support self-calibration. |  |
| NIDMM_VAL_EXTERNAL_AREA | 1 (0x1) | External Calibration |  |
| month | [out] | ViInt32 * | Indicates the month of the last calibration. |
| day | [out] | ViInt32 * | Indicates the day of the last calibration. |
| year | [out] | ViInt32 * | Indicates the year of the last calibration. |
| hour | [out] | ViInt32 * | Indicates the hour of the last calibration. |
| minute | [out] | ViInt32 * | Indicates the minute of the last calibration. |

#### Returns

Reports the **Status** of this operation. To obtain a text description of the status code, call [niDMM_GetErrorMessage](group____root__nidmm__functions__utility__error__handling_1gaaddeed5a573a6aa4afc5f8589ed6a131.html). To obtain additional information concerning the error condition, use [niDMM_GetError](group____root__nidmm__functions__utility__error__handling_1ga3ce9352c8cf141a6ca9710adbaba92cd.html).

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__calibration__calibration__utility_1ga8dc87a14de88dc535462a5b2cf0b3bfb.html language=enus -->
## TOPIC 00093: niDMM_GetDevTemp

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__calibration__calibration__utility_1ga8dc87a14de88dc535462a5b2cf0b3bfb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__calibration__calibration__utility_1ga8dc87a14de88dc535462a5b2cf0b3bfb.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature of the device. SyntaxViStatus _VI_FUNC niDMM_GetDevTemp(ViSession vi, ViString options, ViReal64 *temperature)RemarksThe NI 4050 and NI 4060 are not supported.ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies a particular instrument session. You obtain t

### niDMM_GetDevTemp

Returns the current **temperature** of the device.

#### Syntax

ViStatus _VI_FUNC niDMM_GetDevTemp(ViSession vi, ViString options, ViReal64 *temperature)

#### Remarks

Note

The NI 4050 and NI 4060 are not supported.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. You obtain the Instrument_Handle parameter from niDMM_init or niDMM_InitWithOptions. The default is None. |
| options | [in] | ViString | Reserved. |
| temperature | [out] | ViReal64 * | Returns the current temperature of the device. |

#### Returns

Reports the **Status** of this operation. To obtain a text description of the status code, call [niDMM_GetErrorMessage](group____root__nidmm__functions__utility__error__handling_1gaaddeed5a573a6aa4afc5f8589ed6a131.html). To obtain additional information concerning the error condition, use [niDMM_GetError](group____root__nidmm__functions__utility__error__handling_1ga3ce9352c8cf141a6ca9710adbaba92cd.html).

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__calibration__calibration__utility_1gae86043324c6eda7e0379152ecd4124a0.html language=enus -->
## TOPIC 00094: niDMM_GetCalUserDefinedInfoMaxSize

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__calibration__calibration__utility_1gae86043324c6eda7e0379152ecd4124a0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__calibration__calibration__utility_1gae86043324c6eda7e0379152ecd4124a0.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum string length that can be stored in the EEPROM. Use niDMM_SetCalUserDefinedInfo to store user-defined information. SyntaxViStatus _VI_FUNC niDMM_GetCalUserDefinedInfoMaxSize(ViSession vi, ViInt32 *infoSize)RemarksThe NI 4050 and NI 4060 are not supported.ParametersNameDirectionTy

### niDMM_GetCalUserDefinedInfoMaxSize

Returns the maximum string length that can be stored in the EEPROM. Use [niDMM_SetCalUserDefinedInfo](group____root__nidmm__functions__calibration__calibration__utility_1gafaac9f0ab190c5010014f0f3612d6fa8.html) to store user-defined information.

#### Syntax

ViStatus _VI_FUNC niDMM_GetCalUserDefinedInfoMaxSize(ViSession vi, ViInt32 *infoSize)

#### Remarks

Note

The NI 4050 and NI 4060 are not supported.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. You obtain the Instrument_Handle parameter from niDMM_init or niDMM_InitWithOptions. The default is None. |
| infoSize | [out] | ViInt32 * | Returns the value of maximum string length that can be stored in the EEPROM using niDMM_SetCalUserDefinedInfo. The infoSize value is given in characters, but it does not include the termination character. |

#### Returns

Reports the **Status** of this operation. To obtain a text description of the status code, call [niDMM_GetErrorMessage](group____root__nidmm__functions__utility__error__handling_1gaaddeed5a573a6aa4afc5f8589ed6a131.html). To obtain additional information concerning the error condition, use [niDMM_GetError](group____root__nidmm__functions__utility__error__handling_1ga3ce9352c8cf141a6ca9710adbaba92cd.html).

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__utility__locking.html language=enus -->
## TOPIC 00095: Locking

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__utility__locking.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__utility__locking.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDMM_LockSessionThis function obtains a multithread lock on the instrument session. Before it does so, it waits until all other execution threads have released their locks on the instrument session. niDMM_UnlockSessionThis function releases a lock that you acqu

### Locking

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDMM_LockSession | This function obtains a multithread lock on the instrument session. Before it does so, it waits until all other execution threads have released their locks on the instrument session. |
| niDMM_UnlockSession | This function releases a lock that you acquired on an instrument session using niDMM_LockSession. Refer to niDMM_LockSession for additional information on session locks. |

#### Attachments

None

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dmm-c-api-ref path=group____root__nidmm__functions__utility__locking_1ga01954f3d80251f40cfaf1b2f80c3dbc1.html language=enus -->
## TOPIC 00096: niDMM_UnlockSession

- bundle_id: `ni-dmm-c-api-ref`
- source_path: `group____root__nidmm__functions__utility__locking_1ga01954f3d80251f40cfaf1b2f80c3dbc1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-c-api-ref/raw/resource/enus/group____root__nidmm__functions__utility__locking_1ga01954f3d80251f40cfaf1b2f80c3dbc1.html
- document_id: `ni-dmm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function releases a lock that you acquired on an instrument session using niDMM_LockSession. Refer to niDMM_LockSession for additional information on session locks. SyntaxViStatus _VI_FUNC niDMM_UnlockSession(ViSession vi, ViBoolean *callerHasLock)ParametersNameDirectionTypeDescriptionvi[in]ViS

### niDMM_UnlockSession

This function releases a lock that you acquired on an instrument session using [niDMM_LockSession](group____root__nidmm__functions__utility__locking_1gabb691a610877ef4fdbe509c2e8eaea0b.html). Refer to [niDMM_LockSession](group____root__nidmm__functions__utility__locking_1gabb691a610877ef4fdbe509c2e8eaea0b.html) for additional information on session locks.

#### Syntax

ViStatus _VI_FUNC niDMM_UnlockSession(ViSession vi, ViBoolean *callerHasLock)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. You obtain the Instrument_Handle parameter from niDMM_init or niDMM_InitWithOptions. The default is None. |
| callerHasLock | [out] | ViBoolean * | This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL.Use this parameter in complex functions to keep track of whether you obtain a lock and, therefore, need to unlock the session.To use this parameter, complete the following steps:Pass the address of a local ViBoolean variable.In the declaration of the local variable, initialize it to VI_FALSE (0).Pass the address of the same local variable to any other calls you make to niDMM_LockSession or this function in the same function.The parameter is an input/output parameter. niDMM_LockSession and this function each inspect the current value and take the following actions:If the value is VI_TRUE (1), niDMM_LockSession does not lock the session again. If the value is VI_FALSE, niDMM_LockSession obtains the lock and sets the value of the parameter to VI_TRUE.If the value is VI_FALSE, this function does not attempt to unlock the session. If the value is VI_TRUE, this function releases the lock and sets the value of the parameter to VI_FALSE. Thus, you can, call this function at the end of your function without worrying about whether you actually have the lock.ExampleViStatus TestFunc (ViSession vi, ViInt32 flags){ ViStatus error = VI_SUCCESS; ViBoolean haveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr( niDMM_LockSession(vi, &haveLock)); viCheckErr( TakeAction1(vi)); if (flags & BIT_2) { viCheckErr( niDMM_UnlockSession(vi, &haveLock)); viCheckErr( TakeAction2(vi)); viCheckErr( niDMM_LockSession(vi, &haveLock)); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); } Error: /* At this point, you cannot really be sure that you have the lock. Fortunately, the haveLock variable takes care of that for you. */ niDMM_UnlockSession(vi, &haveLock); return error;} |

#### Returns

Reports the **Status** of this operation. To obtain a text description of the status code, call [niDMM_GetErrorMessage](group____root__nidmm__functions__utility__error__handling_1gaaddeed5a573a6aa4afc5f8589ed6a131.html). To obtain additional information concerning the error condition, use [niDMM_GetError](group____root__nidmm__functions__utility__error__handling_1ga3ce9352c8cf141a6ca9710adbaba92cd.html).

Parent topic:

Locking
