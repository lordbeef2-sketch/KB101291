# NI DOCUMENT BUNDLE: ni-dcpower-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-c-api-ref start=1 end=142 -->
<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-DCPower C API Reference

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-DCPower C API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__compensation__open.html language=enus -->
## TOPIC 00002: Open

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__compensation__open.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__compensation__open.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLEDSpecifies whether to apply open LCR compensation data to LCR measurements. NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCESpecifies the conductance, in siemens, of the circuit used for open LCR compensation. NIDCPOWER_ATTR_LCR_OPE

### Open

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | Specifies whether to apply open LCR compensation data to LCR measurements. |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | Specifies the conductance, in siemens, of the circuit used for open LCR compensation. |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | Specifies the susceptance, in siemens, of the circuit used for open LCR compensation. |

#### Attachments

None

Parent topic:

Compensation

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__dc__bias_1ga6cc83e3a1b028bfeccbe737489bd3b07.html language=enus -->
## TOPIC 00003: NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__dc__bias_1ga6cc83e3a1b028bfeccbe737489bd3b07.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__dc__bias_1ga6cc83e3a1b028bfeccbe737489bd3b07.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DC bias voltage level, in volts, when the NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE is set to NIDCPOWER_VAL_DC_BIAS_VOLTAGE. SyntaxNIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVELNumeric ValueData TypeAccessApplies To1150214ViReal64Read/WriteChannelsRemarksThis attribute is not supported by all instru

### NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL

Specifies the DC bias voltage level, in volts, when the [NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE](group____root__nidcpower__attributes__lcr__dc__bias_1gab2840289ef1270b260652b387c6eb3a9.html) is set to **NIDCPOWER_VAL_DC_BIAS_VOLTAGE**.

#### Syntax

NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150214 | ViReal64 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all instruments. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported instruments.

**Valid Values:**

-40 V to 40 V

Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by instrument.

Parent topic:

DC Bias

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__dc__bias_1gab2840289ef1270b260652b387c6eb3a9.html language=enus -->
## TOPIC 00004: NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__dc__bias_1gab2840289ef1270b260652b387c6eb3a9.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__dc__bias_1gab2840289ef1270b260652b387c6eb3a9.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to apply DC bias for LCR measurements. SyntaxNIDCPOWER_ATTR_LCR_DC_BIAS_SOURCENumeric ValueData TypeAccessApplies To1150213ViInt32Read/WriteChannelsRemarksThis attribute is not supported by all instruments. Refer to Supported Attributes by Device for information about supported instrum

### NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE

Specifies how to apply DC bias for LCR measurements.

#### Syntax

NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150213 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all instruments. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported instruments.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_DC_BIAS_OFF | 1065 (0x429) | Disables DC bias in LCR mode. |
| NIDCPOWER_VAL_DC_BIAS_VOLTAGE | 1066 (0x42a) | Applies a constant voltage bias, as defined by the NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL attribute. |
| NIDCPOWER_VAL_DC_BIAS_CURRENT | 1067 (0x42b) | Applies a constant current bias, as defined by the NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL attribute. |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by instrument.

Parent topic:

DC Bias

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__dc__bias__advanced.html language=enus -->
## TOPIC 00005: Advanced

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__dc__bias__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__dc__bias__advanced.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGESpecifies the current range, in amps, that defines the values to which you can set the LCR DC bias current level (NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL) for the specified channel(s). NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | Specifies the current range, in amps, that defines the values to which you can set the LCR DC bias current level (NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL) for the specified channel(s). |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the transient response values for DC bias or applies the transient response you set manually. |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | Specifies the current range, in volts, that defines the values to which you can set the LCR DC bias voltage level (NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL) for the specified channel(s). |

#### Attachments

None

Parent topic:

DC Bias

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__dc__bias__advanced_1gada966ff0989477572c963827e326f75c.html language=enus -->
## TOPIC 00006: NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__dc__bias__advanced_1gada966ff0989477572c963827e326f75c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__dc__bias__advanced_1gada966ff0989477572c963827e326f75c.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the transient response values for DC bias or applies the transient response you set manually. SyntaxNIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSENumeric ValueData TypeAccessApplies To1150347ViInt32Read/Wr

### NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE

For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the transient response values for DC bias or applies the transient response you set manually.

#### Syntax

NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150347 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all instruments. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported instruments.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_LCR_DC_BIAS_TRANSIENT_RESPONSE_NORMAL | 1151 (0x47f) | NI-DCPower automatically applies transient response values for DC bias. |
| NIDCPOWER_VAL_LCR_DC_BIAS_TRANSIENT_RESPONSE_CUSTOM | 1152 (0x480) | NI-DCPower applies the transient response that you set manually with NIDCPOWER_ATTR_TRANSIENT_RESPONSE for DC bias. |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__impedance__range.html language=enus -->
## TOPIC 00007: Impedance Range

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__impedance__range.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__impedance__range.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedGroup membersNameDescriptionNIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGEDefines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement. NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGESpecifies the impedance range the channel uses for LCR measureme

### Impedance Range

#### Groups

- Advanced

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement. |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | Specifies the impedance range the channel uses for LCR measurements. |

#### Attachments

None

Parent topic:

LCR

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__impedance__range_1gac82a8faaa13e70b56c47284f2e365cc8.html language=enus -->
## TOPIC 00008: NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__impedance__range_1gac82a8faaa13e70b56c47284f2e365cc8.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__impedance__range_1gac82a8faaa13e70b56c47284f2e365cc8.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement. SyntaxNIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGENumeric ValueData TypeAccessApplies To1150216ViInt32Read/WriteChannelsRemarks Impedance autoranging may be enabled only when both:The

### NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE

Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement.

#### Syntax

NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150216 | ViInt32 | Read/Write | Channels |

#### Remarks

Impedance autoranging may be enabled only when both:

- The [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute is set to **NIDCPOWER_VAL_SINGLE_POINT**
- The [NIDCPOWER_ATTR_MEASURE_WHEN](group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html) attribute is set to a value other than **NIDCPOWER_VAL_ON_MEASURE_TRIGGER**

You can read [NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE](group____root__nidcpower__attributes__lcr__impedance__range_1gad8b868e8015c15f492a7862f21145352.html) back after a measurement to determine the actual range used.

When enabled, impedance autoranging overrides impedance range settings you configure manually with any other attributes.

Note

When using a load with unknown impedance, you can set this attribute to **NIDCPOWER_VAL_AUTO_RANGE_ON** to determine the correct impedance range for the load. When you know the load impedance, you can achieve faster performance by setting this attribute to **NIDCPOWER_VAL_AUTO_RANGE_OFF** and setting [NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE](group____root__nidcpower__attributes__lcr__impedance__range__advanced_1ga5c881673d73723ef1cb8b8527b504695.html) to **NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION**.

Note

This attribute is not supported by all instruments. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported instruments.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_AUTO_RANGE_OFF | 1068 (0x42c) | Disables automatic selection of the impedance range. Channel(s) use the impedance range you specify with the NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE attribute. |
| NIDCPOWER_VAL_AUTO_RANGE_ON | 1070 (0x42e) | Channel(s) automatically select the optimal NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE for the measured signal. |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by instrument.

Parent topic:

Impedance Range

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__impedance__range_1gad8b868e8015c15f492a7862f21145352.html language=enus -->
## TOPIC 00009: NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__impedance__range_1gad8b868e8015c15f492a7862f21145352.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__impedance__range_1gad8b868e8015c15f492a7862f21145352.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the impedance range the channel uses for LCR measurements. SyntaxNIDCPOWER_ATTR_LCR_IMPEDANCE_RANGENumeric ValueData TypeAccessApplies To1150217ViReal64Read/WriteChannelsRemarksThis attribute is not supported by all instruments. Refer to Supported Attributes by Device for information about

### NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE

Specifies the impedance range the channel uses for LCR measurements.

#### Syntax

NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150217 | ViReal64 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all instruments. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported instruments.

**Valid Values:**

0 ohms to +inf ohms

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by instrument.

Parent topic:

Impedance Range

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__lcr__impedance__range__advanced.html language=enus -->
## TOPIC 00010: Advanced

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__lcr__impedance__range__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__lcr__impedance__range__advanced.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCESpecifies how the impedance range for LCR measurements is determined. NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCESpecifies the load capacitance, in farads and assuming a series model, of the DUT in order to compute the impedance

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | Specifies how the impedance range for LCR measurements is determined. |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | Specifies the load capacitance, in farads and assuming a series model, of the DUT in order to compute the impedance range when NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE is set to NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION. |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | Specifies the load inductance, in henrys and assuming a series model, of the DUT in order to compute the impedance range when NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE is set to NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION. |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | Specifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE is set to NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION. |

#### Attachments

None

Parent topic:

Impedance Range

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__measure_1gab6536fbe5d8169f4336897f70bdb91f9.html language=enus -->
## TOPIC 00011: NIDCPOWER_ATTR_POWER_LINE_FREQUENCY

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__measure_1gab6536fbe5d8169f4336897f70bdb91f9.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__measure_1gab6536fbe5d8169f4336897f70bdb91f9.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the NIDCPOWER_ATTR_APERTURE_TIME attribute in power line cycles (PLCs). SyntaxNIDCPOWER_ATTR_POWER_LINE_FREQUENCYNumeric ValueData TypeAccessApplies To1150020ViReal64Read/WriteCha

### NIDCPOWER_ATTR_POWER_LINE_FREQUENCY

Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the [NIDCPOWER_ATTR_APERTURE_TIME](group____root__nidcpower__attributes__measure_1gab760c7ee177e019e2215ac903971146f.html) attribute in power line cycles (PLCs).

#### Syntax

NIDCPOWER_ATTR_POWER_LINE_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150020 | ViReal64 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Refer to the measurement configuration and timing topics and DC noise rejection topics of supported devices for more information about how to configure your measurements.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_50_HERTZ | 50.0 | Specifies a power line frequency of 50 Hz. |
| NIDCPOWER_VAL_60_HERTZ | 60.0 | Specifies a power line frequency of 60 Hz. |

**Default Value:****NIDCPOWER_VAL_60_HERTZ**

**High-Level Functions**:

- [niDCPower_ConfigurePowerLineFrequency](group____root__nidcpower__functions__measure_1gac16f93e6ed9d982f96ef79f71737406a.html)

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__measure_1gab760c7ee177e019e2215ac903971146f.html language=enus -->
## TOPIC 00012: NIDCPOWER_ATTR_APERTURE_TIME

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__measure_1gab760c7ee177e019e2215ac903971146f.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__measure_1gab760c7ee177e019e2215ac903971146f.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the NIDCPOWER_ATTR_APERTURE_TIME_UNITS attribute. SyntaxNIDCPOWER_ATTR_APERTURE_TIMENumeric ValueData TypeAccessApplies To1150058ViReal64Read/WriteChannelsRemarksThis attribute is no

### NIDCPOWER_ATTR_APERTURE_TIME

Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the [NIDCPOWER_ATTR_APERTURE_TIME_UNITS](group____root__nidcpower__attributes__measure_1ga58143c56c5d895035c0758b4c1895433.html) attribute.

#### Syntax

NIDCPOWER_ATTR_APERTURE_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150058 | ViReal64 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

**High-Level Functions**:

- [niDCPower_ConfigureApertureTime](group____root__nidcpower__functions__measure_1gafe38997daa8b7c96f02f68b3f3f46f27.html)

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__measure_1gadbe41a22d6b7505cb57ea046f4ed205e.html language=enus -->
## TOPIC 00013: NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__measure_1gadbe41a22d6b7505cb57ea046f4ed205e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__measure_1gadbe41a22d6b7505cb57ea046f4ed205e.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to take continuous measurements. Call the niDCPower_AbortWithChannels function to stop continuous measurements. When this attribute is set to VI_FALSE and the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SINGLE_POINT, the NIDCPOWER_ATTR_MEASURE_WHEN attribute must b

### NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE

Specifies whether to take continuous measurements. Call the [niDCPower_AbortWithChannels](group____root__nidcpower__functions__control_1ga1f65932d785595695b117e36a76877a0.html) function to stop continuous measurements. When this attribute is set to VI_FALSE and the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute is set to **NIDCPOWER_VAL_SINGLE_POINT**, the [NIDCPOWER_ATTR_MEASURE_WHEN](group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html) attribute must be set to **NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE** or **NIDCPOWER_VAL_ON_MEASURE_TRIGGER**. When this attribute is set to VI_FALSE and the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute is set to **NIDCPOWER_VAL_SEQUENCE**, the [NIDCPOWER_ATTR_MEASURE_WHEN](group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html) attribute must be set to **NIDCPOWER_VAL_ON_MEASURE_TRIGGER**.

#### Syntax

NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150064 | ViBoolean | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**Defined Values:**

|  |  |
| --- | --- |
| VI_FALSE (0) | Allows continuous measurement. |
| VI_TRUE (1) | Does not allow continuous measurement. |

**Default Value:** VI_TRUE

**Related Topics:**

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html language=enus -->
## TOPIC 00014: NIDCPOWER_ATTR_MEASURE_WHEN

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when the measure unit should acquire measurements. Unless this attribute is configured to NIDCPOWER_VAL_ON_MEASURE_TRIGGER, the NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE attribute is ignored. SyntaxNIDCPOWER_ATTR_MEASURE_WHENNumeric ValueData TypeAccessApplies To1150057ViInt32Read/WriteChannelsR

### NIDCPOWER_ATTR_MEASURE_WHEN

Specifies when the measure unit should acquire measurements. Unless this attribute is configured to **NIDCPOWER_VAL_ON_MEASURE_TRIGGER**, the [NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE](group____root__nidcpower__attributes__triggers__measure__trigger_1gacc64477fd3b17bbf1e098e4698233acb.html) attribute is ignored.

#### Syntax

NIDCPOWER_ATTR_MEASURE_WHEN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150057 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE | 1025 (0x401) | Acquires a measurement after each Source Complete event. |
| NIDCPOWER_VAL_ON_DEMAND | 1026 (0x402) | Acquires a measurement when the niDCPower_Measure function or niDCPower_MeasureMultiple function is called. |
| NIDCPOWER_VAL_ON_MEASURE_TRIGGER | 1027 (0x403) | Acquires a measurement when a Measure trigger is received. |

**Default Value:** If the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute is set to **NIDCPOWER_VAL_SINGLE_POINT**, the default value is **NIDCPOWER_VAL_ON_DEMAND**. This value supports only the [niDCPower_Measure](group____root__nidcpower__functions__measure_1ga93106c3c3af7f1e3a3848865ce201d6e.html) function and [niDCPower_MeasureMultiple](group____root__nidcpower__functions__measure_1ga69c289b5b8f82eff74f3fafab676bb16.html) function. If the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute is set to **NIDCPOWER_VAL_SEQUENCE**, the default value is **NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE**. This value supports only the [niDCPower_FetchMultiple](group____root__nidcpower__functions__measure_1ga7d8ca519f7a28c8684041b125927560f.html) function.

**Related Topics:**

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__measure__advanced_1ga1afab21052ddefaa1504ec409e045721.html language=enus -->
## TOPIC 00015: NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__measure__advanced_1ga1afab21052ddefaa1504ec409e045721.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__measure__advanced_1ga1afab21052ddefaa1504ec409e045721.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME attribute. SyntaxNIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITSNumeric ValueData TypeAccessApplies To1150248ViInt32Read/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Supported Attributes by

### NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS

Specifies the units of the [NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME](group____root__nidcpower__attributes__measure__advanced_1ga132abd7256b59ad6462d64df5b6c69a0.html) attribute.

#### Syntax

NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150248 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_SECONDS | 1028 (0x404) | Specifies aperture time in seconds. |
| NIDCPOWER_VAL_POWER_LINE_CYCLES | 1029 (0x405) | Specifies aperture time in power line cycles (PLCs). |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__measure__advanced_1gaef3ae6bee6afdb433940af66812ca4c5.html language=enus -->
## TOPIC 00016: NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__measure__advanced_1gaef3ae6bee6afdb433940af66812ca4c5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__measure__advanced_1gaef3ae6bee6afdb433940af66812ca4c5.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the algorithm the hardware uses for measurement autoranging. SyntaxNIDCPOWER_ATTR_AUTORANGE_BEHAVIORNumeric ValueData TypeAccessApplies To1150245ViInt32Read/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Supported Attributes by Device for information about sup

### NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR

Specifies the algorithm the hardware uses for measurement autoranging.

#### Syntax

NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150245 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN | 1107 (0x453) | Range up to maximum, then down-Go to limit range then range down as needed until measured value is within thresholds. |
| NIDCPOWER_VAL_RANGE_UP | 1108 (0x454) | Range up-Go up one range when the upper threshold is reached. |
| NIDCPOWER_VAL_RANGE_UP_AND_DOWN | 1109 (0x455) | Range up and down-Go up or down one range when the upper/lower threshold is reached. |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__measure__advanced_1gaf97b9b7f9861660f4a6bec13d56dd58c.html language=enus -->
## TOPIC 00017: NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__measure__advanced_1gaf97b9b7f9861660f4a6bec13d56dd58c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__measure__advanced_1gaf97b9b7f9861660f4a6bec13d56dd58c.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement returned from any measurement call starts with a new measurement call (VI_TRUE) or returns a measurement that has already begun or completed(VI_FALSE). SyntaxNIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENTNumeric ValueData TypeAccessApplies To1150006ViBooleanRead/Wr

### NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT

Specifies whether the measurement returned from any measurement call starts with a new measurement call (VI_TRUE) or returns a measurement that has already begun or completed(VI_FALSE).

#### Syntax

NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150006 | ViBoolean | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

When you set the [NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE](group____root__nidcpower__attributes__measure_1ga8450583ec06c5209fe9dc3dca5c2388b.html) attribute in the [Running state](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates), the channel measurements might move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a session, you can force a synchronization in the running state before you run the [niDCPower_MeasureMultiple](group____root__nidcpower__functions__measure_1ga69c289b5b8f82eff74f3fafab676bb16.html) function. To force a synchronization in the running state, set this attribute to VI_TRUE, and then run the [niDCPower_MeasureMultiple](group____root__nidcpower__functions__measure_1ga69c289b5b8f82eff74f3fafab676bb16.html) function, specifying all channels in the channel name parameter. You can set the [NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT](group____root__nidcpower__attributes__measure__advanced_1gaf97b9b7f9861660f4a6bec13d56dd58c.html) attribute to VI_FALSE after the [niDCPower_MeasureMultiple](group____root__nidcpower__functions__measure_1ga69c289b5b8f82eff74f3fafab676bb16.html) function completes.

**Defined Values:**

|  |  |
| --- | --- |
| VI_FALSE (0) | Do not reset the average before measurement. |
| VI_TRUE (1) | Reset the average before measurement. |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

**Related Topics:**

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source.html language=enus -->
## TOPIC 00018: Source

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedAdvanced SequencingConstant PowerConstant ResistanceCustom Transient ResponseDC CurrentDC VoltageOutput CutoffPulse CurrentPulse VoltageGroup membersNameDescriptionNIDCPOWER_ATTR_OUTPUT_CONNECTEDSpecifies whether the output relay is connected (closed) or disconnected (open). The NIDCPO

### Source

#### Groups

- Advanced
- Advanced Sequencing
- Constant Power
- Constant Resistance
- Custom Transient Response
- DC Current
- DC Voltage
- Output Cutoff
- Pulse Current
- Pulse Voltage

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | Specifies whether the output relay is connected (closed) or disconnected (open). The NIDCPOWER_ATTR_OUTPUT_ENABLED attribute does not change based on this attribute; they are independent of each other. |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | Specifies whether the output is enabled (VI_TRUE) or disabled (VI_FALSE). |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | Configures the function to generate on the specified channel(s). |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | Specifies the output resistance that the device attempts to generate for the specified channel(s). |
| NIDCPOWER_ATTR_SOURCE_MODE | Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes. |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | Specifies the transient response. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source_1ga719ca19612c56a40b2bc2575c2d7cecf.html language=enus -->
## TOPIC 00019: NIDCPOWER_ATTR_OUTPUT_CONNECTED

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source_1ga719ca19612c56a40b2bc2575c2d7cecf.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source_1ga719ca19612c56a40b2bc2575c2d7cecf.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the output relay is connected (closed) or disconnected (open). The NIDCPOWER_ATTR_OUTPUT_ENABLED attribute does not change based on this attribute; they are independent of each other. SyntaxNIDCPOWER_ATTR_OUTPUT_CONNECTEDNumeric ValueData TypeAccessApplies To1150060ViBooleanRead/Wr

### NIDCPOWER_ATTR_OUTPUT_CONNECTED

Specifies whether the output relay is connected (closed) or disconnected (open). The [NIDCPOWER_ATTR_OUTPUT_ENABLED](group____root__nidcpower__attributes__source_1ga131827bee1cb8985b2f7e8e52d35a810.html) attribute does not change based on this attribute; they are independent of each other.

#### Syntax

NIDCPOWER_ATTR_OUTPUT_CONNECTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150060 | ViBoolean | Read/Write | Channels |

#### Remarks

Set this attribute to VI_FALSE to disconnect the output terminal from the output.

Note

Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the output can cause premature wear on electromechanical relays, such as those used by the PXIe-4147, PXI-4132, or PXIe-4138/39.

Note

The PXIe-4051 does not have an output relay. For the PXIe-4051, this attribute specifies whether the input MOSFETs are connected (ON) or disconnected (OFF).

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Defined Values:**

|  |  |
| --- | --- |
| VI_FALSE (0) | The output relay is disconnected (open). |
| VI_TRUE (1) | The output relay is connected (closed). |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

**Related Topics:**

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html language=enus -->
## TOPIC 00020: NIDCPOWER_ATTR_SOURCE_MODE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes. SyntaxNIDCPOWER_ATTR_SOURCE_MODENumeric ValueData TypeAccessApplies To1150054ViInt32R

### NIDCPOWER_ATTR_SOURCE_MODE

Specifies whether to run a single output point or a sequence. Refer to the [Single Point Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_singlept) and [Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing) topics in the *NI DC Power Supplies and SMUs Help* for more information about source modes.

#### Syntax

NIDCPOWER_ATTR_SOURCE_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150054 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_SINGLE_POINT | 1020 (0x3fc) | Applies a single source configuration. |
| NIDCPOWER_VAL_SEQUENCE | 1021 (0x3fd) | Applies a list of voltage or current configurations sequentially. |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

**Related Topics:**

**High-Level Functions**:

- [niDCPower_ConfigureSourceModeWithChannels](group____root__nidcpower__functions__source_1ga02d871da1672fd2856f792a674f8255d.html)

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced.html language=enus -->
## TOPIC 00021: Advanced

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsConduction VoltageGroup membersNameDescriptionNIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATIONReturns the power, in watts, the device is sourcing on the active channels if the NIDCPOWER_ATTR_POWER_ALLOCATION_MODE attribute is set to NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC or NIDCPOWER_VAL_POWER_AL

### Advanced

#### Groups

- Conduction Voltage

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | Returns the power, in watts, the device is sourcing on the active channels if the NIDCPOWER_ATTR_POWER_ALLOCATION_MODE attribute is set to NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC or NIDCPOWER_VAL_POWER_ALLOCATION_MODE_MANUAL. |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | Specifies whether current generation limits and voltage generation limits for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A. |
| NIDCPOWER_ATTR_MERGED_CHANNELS | Specifies the merge channel(s) to combine with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument. |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | Specifies whether to use a low or high capacitance on the output for the specified channel(s). |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | Specifies whether the input of the instrument simulates a short circuit. |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | Specifies whether NI-DCPower allows setting the voltage level (NIDCPOWER_ATTR_VOLTAGE_LEVEL), current level (NIDCPOWER_ATTR_CURRENT_LEVEL), voltage limit (NIDCPOWER_ATTR_VOLTAGE_LIMIT) and current limit (NIDCPOWER_ATTR_CURRENT_LIMIT) outside the device specification limits. VI_TRUE means that overranging is enabled. |
| NIDCPOWER_ATTR_OVP_ENABLED | Enables (VI_TRUE) or disables (VI_FALSE) overvoltage protection (OVP). |
| NIDCPOWER_ATTR_OVP_LIMIT | Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages. The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. For example, setting the OVP Limit to 65 will configure the OVP feature to trigger an OVP error if the output exceeds +-65 V. |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | Determines whether the device sources the power its output configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device. |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | Determines when, in seconds, the device generates the Pulse Complete event after generating the "off" level of a pulse. |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | Determines the length, in seconds, of the off phase of a pulse. |
| NIDCPOWER_ATTR_PULSE_ON_TIME | Determines the length, in seconds, of the on phase of a pulse. |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | Specifies the power, in watts, to request the device to source from each active channel. |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | Specifies the number of times a sequence is run after initiation. |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | Specifies whether a sequence should repeat indefinitely. |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | Specifies the amount of time, in seconds, between the start of two consecutive steps in a sequence. |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | Specifies whether the NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME attribute is enabled (VI_TRUE) or disabled (VI_FALSE). |
| NIDCPOWER_ATTR_SOURCE_DELAY | Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the NIDCPOWER_ATTR_MEASURE_WHEN attribute is set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE. |

#### Attachments

None

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1ga0567a99d63c00271128a661e371a8e04.html language=enus -->
## TOPIC 00022: NIDCPOWER_ATTR_POWER_ALLOCATION_MODE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1ga0567a99d63c00271128a661e371a8e04.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1ga0567a99d63c00271128a661e371a8e04.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the device sources the power its output configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device. SyntaxNIDCPOWER_ATTR_POWER_ALLOCA

### NIDCPOWER_ATTR_POWER_ALLOCATION_MODE

Determines whether the device sources the power its output configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device.

#### Syntax

NIDCPOWER_ATTR_POWER_ALLOCATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150207 | ViInt32 | Read/Write | Channels |

#### Remarks

When this attribute configures NI-DCPower to perform a sourcing power check, a device is not permitted to source power in excess of its maximum per-channel or overall sourcing power. If the check determines an output configuration or power request would require the device to do so, NI-DCPower returns an error.

When this attribute does not configure NI-DCPower to perform a sourcing power check, a device complies with requests to source power in excess of its maximum per-channel or overall sourcing power and may shut down to prevent damage.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices. Devices that do not support this attribute behave as if this attribute were set to **NIDCPOWER_VAL_POWER_ALLOCATION_MODE_DISABLED**.

**Defined Values**:

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_POWER_ALLOCATION_MODE_DISABLED | 1058 (0x422) | The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower does not perform a sourcing power check. If the required power is greater than the maximum sourcing power, the device attempts to source the required amount and may shut down to prevent damage. |
| NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC | 1059 (0x423) | The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower performs a sourcing power check. If the required power is greater than the maximum sourcing power, the device does not exceed the maximum power, and NI-DCPower returns an error. |
| NIDCPOWER_VAL_POWER_ALLOCATION_MODE_MANUAL | 1060 (0x424) | The device attempts to source, on each active channel, the power you request with the NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION attribute; NI-DCPower performs a sourcing power check. If the requested power is either less than the required power for the present source configuration or greater than the maximum sourcing power, the device does not exceed the requested or allowed power, respectively, and NI-DCPower returns an error. |

**Default Value**: Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1ga0b5a8402f8fd0c3dcc8c47acc3eaab0a.html language=enus -->
## TOPIC 00023: NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1ga0b5a8402f8fd0c3dcc8c47acc3eaab0a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1ga0b5a8402f8fd0c3dcc8c47acc3eaab0a.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time, in seconds, between the start of two consecutive steps in a sequence. SyntaxNIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIMENumeric ValueData TypeAccessApplies To1150198ViReal64Read/WriteChannelsRemarks You can specify this attribute as one of the attributeIDs when calling the n

### NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME

Specifies the amount of time, in seconds, between the start of two consecutive steps in a sequence.

#### Syntax

NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150198 | ViReal64 | Read/Write | Channels |

#### Remarks

You can specify this attribute as one of the **attributeIDs** when calling the [niDCPower_CreateAdvancedSequenceWithChannels](group____root__nidcpower__functions__source__advanced__sequencing_1gae609a6f88ba2ead80256f058d98d5286.html) function. In this case, this attribute specifies the amount of time between the start of the active step and the start of the next step.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

This attribute is applicable only if the [NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED](group____root__nidcpower__attributes__source__advanced_1gaa81997533e8952a35a9529bf06caed54.html) attribute is set to VI_TRUE. This attribute does not apply to the last step of the last iteration of a sequence.

Note

You can set values for the [NIDCPOWER_ATTR_SOURCE_DELAY](group____root__nidcpower__attributes__source__advanced_1ga49d08c176742348422e7020853a12bbc.html) and Measure attributes in conjunction with this attribute. Values for [NIDCPOWER_ATTR_SOURCE_DELAY](group____root__nidcpower__attributes__source__advanced_1ga49d08c176742348422e7020853a12bbc.html) may conflict with the value of this attribute; Measure attributes may conflict with the value of this attribute only if the [NIDCPOWER_ATTR_MEASURE_WHEN](group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html) attribute is set to **NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE**.

NI recommends that you configure other attributes in the Commit step when configuring [NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME](group____root__nidcpower__attributes__source__advanced_1ga0b5a8402f8fd0c3dcc8c47acc3eaab0a.html) using the [niDCPower_CreateAdvancedSequenceCommitStepWithChannels](group____root__nidcpower__functions__source__advanced__sequencing_1ga5d5bc52c3dab58860ccc27aa592d25f2.html) function to reduce the setup time in the first step of sequence.

Note

Alternatively, you can configure other attributes in first session, then close the session and proceed to start a second session with [NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME](group____root__nidcpower__attributes__source__advanced_1ga0b5a8402f8fd0c3dcc8c47acc3eaab0a.html). The channel retains the previous settings in the first session. As a result, the setup time is reduced in the first step. For more information, refer to [Sequence Step Delta Time Timing Issues](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencestepdeltatimetimingissues).

**Valid Values**

| Device | Values |
| --- | --- |
| PXIe-4135, PXIe-4136/4137, PXIe-4138/4139 | [12.5 us, 60 s] |
| PXIe-4140/4141, PXIe-4142/4143, PXIe-4144/4145 | [10 us, 60 s] |
| PXIe-4147 | [10 us, 26.512 s] |

**Default Value:** Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

Note

NI-DCPower coerces the value you specify for this attribute to the nearest multiple of a device-specific resolution. You can read back the value of this attribute to determine the coerced value. See the table below.

| Device | Selected Value | Resolution |
| --- | --- | --- |
| PXIe-4135, PXIe-4136/4137, PXIe-4138/4139 | [12.5 us, 21.4748 s] | 10 ns |
|  | (21.4748 s, 60 s] | 10 us |
| PXIe-4140/4141, PXIe-4142/4143, PXIe-4144/4145 | [10 us, 233.0169 ms] | 27.7778 ns |
|  | (233.0169 ms, 60 s] | 10 us |
| PXIe-4147 | [10 us, 26.512 s] | 6.17 ns |

**Related Topics:**

[Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)

[Advanced Sequencing](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1ga8caf33409cfda1995ea7873fbc33c2eb.html language=enus -->
## TOPIC 00024: NIDCPOWER_ATTR_MERGED_CHANNELS

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1ga8caf33409cfda1995ea7873fbc33c2eb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1ga8caf33409cfda1995ea7873fbc33c2eb.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the merge channel(s) to combine with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument. SyntaxNIDCPOWER_ATTR_MERGED_CHANNELSNumeric ValueData TypeAccessApplies To1150249ViStringRead/WriteChannelsRemarks Pass the primar

### NIDCPOWER_ATTR_MERGED_CHANNELS

Specifies the merge channel(s) to combine with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument.

#### Syntax

NIDCPOWER_ATTR_MERGED_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150249 | ViString | Read/Write | Channels |

#### Remarks

Pass the primary channel as the **channelName** parameter when setting this attribute, and pass the merge channels as the value of this attribute.

Refer to the Merged Channels topic in your instrument user manual for more information about using merged channels.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices. Devices that do not support this attribute behave as if no channels were merged.

**Default Value**: Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

**Related Topics**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1ga9b94e4b4edb503ecf83fc1b2eb7a17f5.html language=enus -->
## TOPIC 00025: NIDCPOWER_ATTR_OVP_ENABLED

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1ga9b94e4b4edb503ecf83fc1b2eb7a17f5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1ga9b94e4b4edb503ecf83fc1b2eb7a17f5.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables (VI_TRUE) or disables (VI_FALSE) overvoltage protection (OVP). SyntaxNIDCPOWER_ATTR_OVP_ENABLEDNumeric ValueData TypeAccessApplies To1250002ViBooleanRead/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supporte

### NIDCPOWER_ATTR_OVP_ENABLED

Enables (VI_TRUE) or disables (VI_FALSE) overvoltage protection (OVP).

#### Syntax

NIDCPOWER_ATTR_OVP_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1250002 | ViBoolean | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Defined Values:**

|  |  |
| --- | --- |
| VI_FALSE (0) | Overvoltage protection is disabled. |
| VI_TRUE (1) | Overvoltage protection is enabled. |

**Default Value:**

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1gaa81997533e8952a35a9529bf06caed54.html language=enus -->
## TOPIC 00026: NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1gaa81997533e8952a35a9529bf06caed54.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1gaa81997533e8952a35a9529bf06caed54.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME attribute is enabled (VI_TRUE) or disabled (VI_FALSE). SyntaxNIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLEDNumeric ValueData TypeAccessApplies To1150199ViBooleanRead/WriteChannelsRemarks When this attribute is set to VI_TRUE, you can set

### NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED

Specifies whether the [NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME](group____root__nidcpower__attributes__source__advanced_1ga0b5a8402f8fd0c3dcc8c47acc3eaab0a.html) attribute is enabled (VI_TRUE) or disabled (VI_FALSE).

#### Syntax

NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150199 | ViBoolean | Read/Write | Channels |

#### Remarks

When this attribute is set to VI_TRUE, you can set the [NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME](group____root__nidcpower__attributes__source__advanced_1ga0b5a8402f8fd0c3dcc8c47acc3eaab0a.html) attribute to control the time between consecutive steps in the sequence.

Note

This attribute is notsupported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

This attribute is applicable only if the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute is set to **NIDCPOWER_VAL_SEQUENCE** and may be set to VI_TRUE only if:

- The [NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE](group____root__nidcpower__attributes__triggers__source__trigger_1ga3595ca4bb92a50ed9fbe1d3530b58e87.html) attribute is set to **NIDCPOWER_VAL_NONE**;
- The [NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE](group____root__nidcpower__attributes__triggers__sequence__advance__trigger_1gad678b76dfb60f201f84a7d47136117bc.html) attribute is set to **NIDCPOWER_VAL_NONE**; and
- The [NIDCPOWER_ATTR_OUTPUT_FUNCTION](group____root__nidcpower__attributes__source_1gadedf2f87f0061a2af5d7a099ca9b9aa0.html) attribute is set to **NIDCPOWER_VAL_DC_VOLTAGE** or **NIDCPOWER_VAL_DC_CURRENT**.

**Default Value:** Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for the default value by device.

**Related Topics:**

[Sequence Source Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_sequencing)

[Advanced Sequencing](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1gade916962baf68c79a887aaddb6e25c33.html language=enus -->
## TOPIC 00027: NIDCPOWER_ATTR_PULSE_OFF_TIME

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1gade916962baf68c79a887aaddb6e25c33.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1gade916962baf68c79a887aaddb6e25c33.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the length, in seconds, of the off phase of a pulse. SyntaxNIDCPOWER_ATTR_PULSE_OFF_TIMENumeric ValueData TypeAccessApplies To1150094ViReal64Read/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported dev

### NIDCPOWER_ATTR_PULSE_OFF_TIME

Determines the length, in seconds, of the off phase of a pulse.

#### Syntax

NIDCPOWER_ATTR_PULSE_OFF_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150094 | ViReal64 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Valid Values**: 50 microseconds to 167 seconds

**Default Value**: 34 milliseconds

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1gaf4fbe1b1f32e757ea901aa8791609cb6.html language=enus -->
## TOPIC 00028: NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1gaf4fbe1b1f32e757ea901aa8791609cb6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1gaf4fbe1b1f32e757ea901aa8791609cb6.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether current generation limits and voltage generation limits for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A. SyntaxNIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRYNumeric ValueData TypeAccessApplies To1150184ViInt32Read/WriteChannelsRema

### NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY

Specifies whether current generation limits and voltage generation limits for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A.

#### Syntax

NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150184 | ViInt32 | Read/Write | Channels |

#### Remarks

When set to **NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC**, voltage limits and current limits are set using a single attribute with a positive value. The resulting range is bounded by this positive value and its opposite.

When set to **NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_ASYMMETRIC**, you must separately set a limit high and a limit low using distinct attributes.

For asymmetric limits, the range bounded by the limit high and limit low must include zero.

Note

Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC | 0 (0x0) | Compliance limits are specified symmetrically about 0. |
| NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_ASYMMETRIC | 1 (0x1) | Compliance limits can be specified asymmetrically with respect to 0. |

**Default Value:****NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC**

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced_1gafd6421ba6e7b16e3851dbad1c3640c19.html language=enus -->
## TOPIC 00029: NIDCPOWER_ATTR_OVERRANGING_ENABLED

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced_1gafd6421ba6e7b16e3851dbad1c3640c19.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced_1gafd6421ba6e7b16e3851dbad1c3640c19.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-DCPower allows setting the voltage level (NIDCPOWER_ATTR_VOLTAGE_LEVEL), current level (NIDCPOWER_ATTR_CURRENT_LEVEL), voltage limit (NIDCPOWER_ATTR_VOLTAGE_LIMIT) and current limit (NIDCPOWER_ATTR_CURRENT_LIMIT) outside the device specification limits. VI_TRUE means that overra

### NIDCPOWER_ATTR_OVERRANGING_ENABLED

Specifies whether NI-DCPower allows setting the voltage level ([NIDCPOWER_ATTR_VOLTAGE_LEVEL](group____root__nidcpower__attributes__source__dc__voltage_1gaa55419170244e58560200ac3ffef437d.html)), current level ([NIDCPOWER_ATTR_CURRENT_LEVEL](group____root__nidcpower__attributes__source__dc__current_1ga1fcc0a9895703a07fd4a29ae72ed6f7c.html)), voltage limit ([NIDCPOWER_ATTR_VOLTAGE_LIMIT](group____root__nidcpower__attributes__source__dc__current_1gab3a1202d6cf1d234ab7f81bbb4537843.html)) and current limit ([NIDCPOWER_ATTR_CURRENT_LIMIT](group____root__nidcpower__attributes__source__dc__voltage_1ga4b5b6844b049bcb866ad14d4d6be8af9.html)) outside the device specification limits. VI_TRUE means that overranging is enabled.

#### Syntax

NIDCPOWER_ATTR_OVERRANGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150007 | ViBoolean | Read/Write | Channels |

#### Remarks

**Defined Values:**

|  |  |
| --- | --- |
| VI_TRUE (1) | Overranging is enabled. |
| VI_FALSE (0) | Overranging is disabled. |

**Default Value:** VI_FALSE

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__advanced__sequencing_1gafe610433ad5e74ae3dfe854a4f41680e.html language=enus -->
## TOPIC 00030: NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__advanced__sequencing_1gafe610433ad5e74ae3dfe854a4f41680e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__advanced__sequencing_1gafe610433ad5e74ae3dfe854a4f41680e.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the advanced sequence to configure or generate. SyntaxNIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCENumeric ValueData TypeAccessApplies To1150074ViStringRead/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported

### NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE

Specifies the advanced sequence to configure or generate.

#### Syntax

NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150074 | ViString | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Parent topic:

Advanced Sequencing

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__source__constant__power.html language=enus -->
## TOPIC 00031: Constant Power

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__source__constant__power.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__source__constant__power.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMITSpecifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s). The device will operate in Constant Current mode if the current exceeds the specif

### Constant Power

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | Specifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s). The device will operate in Constant Current mode if the current exceeds the specified limit. |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | Specifies the power level, in watts, that the device attempts to generate on the specified channel(s). This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_CONSTANT_POWER. |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | Specifies the power level range, in watts, for the specified channel(s). The range defines the valid values to which you can set the power level. This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_CONSTANT_POWER. For valid ranges, refer to the specifications for your instrument. |

#### Attachments

None

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__pulse__trigger__digital__edge_1gae6226d5052458de0fc488d2ae885a682.html language=enus -->
## TOPIC 00032: NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__pulse__trigger__digital__edge_1gae6226d5052458de0fc488d2ae885a682.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__pulse__trigger__digital__edge_1gae6226d5052458de0fc488d2ae885a682.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Pulse trigger to assert on the rising or falling edge. SyntaxNIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGENumeric ValueData TypeAccessApplies To1150096ViInt32Read/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Supported Attributes by

### NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE

Specifies whether to configure the Pulse trigger to assert on the rising or falling edge.

#### Syntax

NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150096 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_RISING | 1016 (0x3f8) | Asserts the trigger on the rising edge of the digital signal. |
| NIDCPOWER_VAL_FALLING | 1017 (0x3f9) | Asserts the trigger on the falling edge of the digital signal. |

**Default Value**: **NIDCPOWER_VAL_RISING**

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__pulse__trigger_1gaf3abc67d0289c24a0ea6febf80ba176f.html)

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__sequence__advance__trigger_1gad678b76dfb60f201f84a7d47136117bc.html language=enus -->
## TOPIC 00033: NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__sequence__advance__trigger_1gad678b76dfb60f201f84a7d47136117bc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__sequence__advance__trigger_1gad678b76dfb60f201f84a7d47136117bc.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Sequence Advance trigger. SyntaxNIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPENumeric ValueData TypeAccessApplies To1150026ViInt32Read/WriteChannelsRemarks Refer to theConfigure Triggers and Events topic in your instrument user manual for more information about triggers a

### NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE

Specifies the behavior of the Sequence Advance trigger.

#### Syntax

NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150026 | ViInt32 | Read/Write | Channels |

#### Remarks

Refer to the

Configure Triggers and Events topic in your instrument user manual for more information about triggers and events.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_NONE | 1012 (0x3f4) | No trigger is configured. |
| NIDCPOWER_VAL_DIGITAL_EDGE | 1014 (0x3f6) | The data operation starts when a digital edge is detected. |
| NIDCPOWER_VAL_SOFTWARE_EDGE | 1015 (0x3f7) | The data operation starts when a software trigger occurs. |

**Default Value:****NIDCPOWER_VAL_NONE**

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__sequence__advance__trigger_1ga2dc64f13f3b6e58120d517718dc4f4a1.html)
- [niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__sequence__advance__trigger_1ga74a010a264aaa48dfc8b18b0906a459c.html)
- [niDCPower_DisableSequenceAdvanceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__sequence__advance__trigger_1ga450853b8b5166cd3d6575a25697bf9f8.html)

Parent topic:

Sequence Advance Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__sequence__advance__trigger__digital__edge.html language=enus -->
## TOPIC 00034: Digital Edge

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__sequence__advance__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__sequence__advance__trigger__digital__edge.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGESpecifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge. NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINALSpecifies the input terminal for the

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | Specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge. |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | Specifies the input terminal for the Sequence Advance trigger. Use this attribute only when the NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE. |

#### Attachments

None

Parent topic:

Sequence Advance Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__sequence__advance__trigger__digital__edge_1ga0561b19a64f0c46b66f7f182016202b6.html language=enus -->
## TOPIC 00035: NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__sequence__advance__trigger__digital__edge_1ga0561b19a64f0c46b66f7f182016202b6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__sequence__advance__trigger__digital__edge_1ga0561b19a64f0c46b66f7f182016202b6.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge. SyntaxNIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGENumeric ValueData TypeAccessApplies To1150027ViInt32Read/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Su

### NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE

Specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge.

#### Syntax

NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150027 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_RISING | 1016 (0x3f8) | Asserts the trigger on the rising edge of the digital signal. |
| NIDCPOWER_VAL_FALLING | 1017 (0x3f9) | Asserts the trigger on the falling edge of the digital signal. |

**Default Value:****NIDCPOWER_VAL_RISING**

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__sequence__advance__trigger_1ga2dc64f13f3b6e58120d517718dc4f4a1.html)

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__shutdown__trigger__digital__edge.html language=enus -->
## TOPIC 00036: Digital Edge

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__shutdown__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__shutdown__trigger__digital__edge.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGESpecifies whether to configure the Pulse trigger to assert on the rising or falling edge. NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINALSpecifies the input terminal for the Pulse trigger. This attribu

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | Specifies whether to configure the Pulse trigger to assert on the rising or falling edge. |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | Specifies the input terminal for the Pulse trigger. This attribute is used only when the NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE attribute is set to digital edge. |

#### Attachments

None

Parent topic:

Shutdown Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__shutdown__trigger__digital__edge_1ga669529cb6e52a1b55e136d489daa079b.html language=enus -->
## TOPIC 00037: NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__shutdown__trigger__digital__edge_1ga669529cb6e52a1b55e136d489daa079b.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__shutdown__trigger__digital__edge_1ga669529cb6e52a1b55e136d489daa079b.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Pulse trigger. This attribute is used only when the NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE attribute is set to digital edge. SyntaxNIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINALNumeric ValueData TypeAccessApplies To1150277ViStringRead/WriteChannelsRema

### NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL

Specifies the input terminal for the Pulse trigger. This attribute is used only when the [NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE](group____root__nidcpower__attributes__triggers__shutdown__trigger_1gaa0b6a920e8da3c5c32572a6aac0027a6.html) attribute is set to digital edge.

#### Syntax

NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150277 | ViString | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0.

Note

You must specify the input terminal for a PXI-4138/4139 using the form /Dev1/PXI_Trig0, where Dev1 is a PXI-4138/4139 and PXI_Trig0 is the terminal.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgeShutdownTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__shutdown__trigger_1ga007b2caffa9f172e9f39b76cf382f265.html)

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__source__trigger_1ga20bd494f3b8c7b73c9a4eed5a29e3907.html language=enus -->
## TOPIC 00038: NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__source__trigger_1ga20bd494f3b8c7b73c9a4eed5a29e3907.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__source__trigger_1ga20bd494f3b8c7b73c9a4eed5a29e3907.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Source trigger. SyntaxNIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To1150033ViStringRead/WriteChannelsRemarks Refer to the Device Routes tab in MAX for a list of the terminals available on your device. For t

### NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL

Specifies the output terminal for exporting the Source trigger.

#### Syntax

NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150033 | ViString | Read/Write | Channels |

#### Remarks

Refer to the **Device Routes** tab in MAX for a list of the terminals available on your device. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**High-Level Functions**:

- [niDCPower_ExportSignalWithChannels](group____root__nidcpower__functions__triggers__and__events_1gad51bd44ef73428bd7eef439c7403b32b.html)

Parent topic:

Source Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__source__trigger_1ga3595ca4bb92a50ed9fbe1d3530b58e87.html language=enus -->
## TOPIC 00039: NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__source__trigger_1ga3595ca4bb92a50ed9fbe1d3530b58e87.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__source__trigger_1ga3595ca4bb92a50ed9fbe1d3530b58e87.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Source trigger. SyntaxNIDCPOWER_ATTR_SOURCE_TRIGGER_TYPENumeric ValueData TypeAccessApplies To1150030ViInt32Read/WriteChannelsRemarksNI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and

### NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE

Specifies the behavior of the Source trigger.

#### Syntax

NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150030 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_NONE | 1012 (0x3f4) | No trigger is configured. |
| NIDCPOWER_VAL_DIGITAL_EDGE | 1014 (0x3f6) | The data operation starts when a digital edge is detected. |
| NIDCPOWER_VAL_SOFTWARE_EDGE | 1015 (0x3f7) | The data operation starts when a software trigger occurs. |

**Default Value:****NIDCPOWER_VAL_NONE**

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__source__trigger_1gacc0bc87e5df269c68e049ebc52e41a91.html)
- [niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__source__trigger_1gae31b49e58056132fb4b31720a9b05868.html)
- [niDCPower_DisableSourceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__source__trigger_1ga1316132301d2197826fcc1feb92116e4.html)

Parent topic:

Source Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__source__trigger__digital__edge.html language=enus -->
## TOPIC 00040: Digital Edge

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__source__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__source__trigger__digital__edge.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGESpecifies whether to configure the Source trigger to assert on the rising or falling edge. NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINALSpecifies the input terminal for the Source trigger. Use this attri

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | Specifies whether to configure the Source trigger to assert on the rising or falling edge. |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | Specifies the input terminal for the Source trigger. Use this attribute only when the NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE. |

#### Attachments

None

Parent topic:

Source Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__source__trigger__digital__edge_1gaecff3209e42a1522e9e64877f5938a6e.html language=enus -->
## TOPIC 00041: NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__source__trigger__digital__edge_1gaecff3209e42a1522e9e64877f5938a6e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__source__trigger__digital__edge_1gaecff3209e42a1522e9e64877f5938a6e.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Source trigger to assert on the rising or falling edge. SyntaxNIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGENumeric ValueData TypeAccessApplies To1150031ViInt32Read/WriteChannelsRemarksNI-DCPower uses the terms "source" and "output". However, while sinking with el

### NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE

Specifies whether to configure the Source trigger to assert on the rising or falling edge.

#### Syntax

NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150031 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_RISING | 1016 (0x3f8) | Asserts the trigger on the rising edge of the digital signal. |
| NIDCPOWER_VAL_FALLING | 1017 (0x3f9) | Asserts the trigger on the falling edge of the digital signal. |

**Default Value:****NIDCPOWER_VAL_RISING**

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__source__trigger_1gacc0bc87e5df269c68e049ebc52e41a91.html)

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__start__trigger__digital__edge.html language=enus -->
## TOPIC 00042: Digital Edge

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__start__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__start__trigger__digital__edge.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGESpecifies whether to configure the Start trigger to assert on the rising or falling edge. NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINALSpecifies the input terminal for the Start trigger. Use this attribute

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | Specifies whether to configure the Start trigger to assert on the rising or falling edge. |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | Specifies the input terminal for the Start trigger. Use this attribute only when the NIDCPOWER_ATTR_START_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE. |

#### Attachments

None

Parent topic:

Start Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__start__trigger__digital__edge_1ga26096c24c035478cdc01c4248cf5994d.html language=enus -->
## TOPIC 00043: NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__start__trigger__digital__edge_1ga26096c24c035478cdc01c4248cf5994d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__start__trigger__digital__edge_1ga26096c24c035478cdc01c4248cf5994d.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Start trigger to assert on the rising or falling edge. SyntaxNIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGENumeric ValueData TypeAccessApplies To1150022ViInt32Read/WriteChannelsRemarksThis attribute is not supported by all devices. Refer to Supported Attributes by

### NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE

Specifies whether to configure the Start trigger to assert on the rising or falling edge.

#### Syntax

NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150022 | ViInt32 | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDCPOWER_VAL_RISING | 1016 (0x3f8) | Asserts the trigger on the rising edge of the digital signal. |
| NIDCPOWER_VAL_FALLING | 1017 (0x3f9) | Asserts the trigger on the falling edge of the digital signal. |

**Default Value:****NIDCPOWER_VAL_RISING**

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga058b5793d8612abdd57067cc2e9582d6.html)

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__attributes__triggers__start__trigger__digital__edge_1gaf67921d331de5f7d21e5f9711140a849.html language=enus -->
## TOPIC 00044: NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__attributes__triggers__start__trigger__digital__edge_1gaf67921d331de5f7d21e5f9711140a849.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__attributes__triggers__start__trigger__digital__edge_1gaf67921d331de5f7d21e5f9711140a849.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Start trigger. Use this attribute only when the NIDCPOWER_ATTR_START_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE. SyntaxNIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINALNumeric ValueData TypeAccessApplies To1150023ViStringRead/WriteChannels

### NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL

Specifies the input terminal for the Start trigger. Use this attribute only when the [NIDCPOWER_ATTR_START_TRIGGER_TYPE](group____root__nidcpower__attributes__triggers__start__trigger_1gacf2be7fbdcf99a0934eebb204f450862.html) attribute is set to **NIDCPOWER_VAL_DIGITAL_EDGE**.

#### Syntax

NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150023 | ViString | Read/Write | Channels |

#### Remarks

Note

This attribute is not supported by all devices. Refer to [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device) for information about supported devices.

You can specify any valid terminal for this attribute, and the driver will create a route between it and the Start trigger terminal at Commit. Valid terminals are listed in Measurement & Automation Explorer under the **Device Routes** tab. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the output terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0.

Note

You must specify the input terminal for a PXI-4132 using the form /Dev1/PXI_Trig0, where Dev1 is a PXI-4132 and PXI_Trig0 is the terminal.

Note

To specify a channel name when accessing this attribute, you must first initialize the session using the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

**High-Level Functions**:

- [niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga058b5793d8612abdd57067cc2e9582d6.html)

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__calibration__utility_1ga20135ecba6975bca05c78dee8ffdc70a.html language=enus -->
## TOPIC 00045: niDCPower_GetSelfCalLastTemp

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__calibration__utility_1ga20135ecba6975bca05c78dee8ffdc70a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__calibration__utility_1ga20135ecba6975bca05c78dee8ffdc70a.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the onboard temperature of the device, in degrees Celsius, during the oldest successful self-calibration from among the channels in the session. SyntaxViStatus _VI_FUNC niDCPower_GetSelfCalLastTemp(ViSession vi, ViReal64 *temperature)RemarksFor example, if you have a session using channels 1

### niDCPower_GetSelfCalLastTemp

Returns the onboard temperature of the device, in degrees Celsius, during the oldest successful self-calibration from among the channels in the session.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetSelfCalLastTemp(ViSession vi, ViReal64 *temperature)

#### Remarks

For example, if you have a session using channels 1 and 2, and you perform a self-calibration on channel 1 with a device temperature of 25 degrees Celsius at 2:00, and a self-calibration was performed on channel 2 at 27 degrees Celsius at 3:00 on the same day, this function returns 25 for the **temperature** parameter.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

Note

This function can only be used in a session initialized to a single instrument.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithIndependentChannels function. |
| temperature | [out] | ViReal64 * | Returns the onboard temperature of the device, in degrees Celsius, during the oldest successful calibration. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__calibration__utility_1ga5e162776449161b01b9bd2b827ce3337.html language=enus -->
## TOPIC 00046: niDCPower_SetCalUserDefinedInfo

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__calibration__utility_1ga5e162776449161b01b9bd2b827ce3337.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__calibration__utility_1ga5e162776449161b01b9bd2b827ce3337.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores a user-defined string of characters in the device onboard EEPROM. If the string is longer than the maximum allowable size, it is truncated. This function overwrites any existing user-defined information. SyntaxViStatus _VI_FUNC niDCPower_SetCalUserDefinedInfo(ViSession vi, ViConstString info)

### niDCPower_SetCalUserDefinedInfo

Stores a user-defined string of characters in the device onboard EEPROM. If the string is longer than the maximum allowable size, it is truncated. This function overwrites any existing user-defined information.

#### Syntax

ViStatus _VI_FUNC niDCPower_SetCalUserDefinedInfo(ViSession vi, ViConstString info)

#### Remarks

If you call this function in a regular session, **info** is immediately changed. If you call this function in an external calibration session, **info** is changed only after you close the session using the [niDCPower_CloseExtCal](group____root__nidcpower__functions__calibration__external__calibration_1gad7e060526266f048f27d272e06e8bc1a.html) function with **action** set to **NIDCPOWER_VAL_COMMIT**.

Note

This function can only be used in a session initialized to a single instrument.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithIndependentChannels function. |
| info | [in] | ViConstString | Specifies the string to store in the device onboard EEPROM. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__calibration__utility_1ga8b1c34fba5a12b3112a9c38f4fad0fb3.html language=enus -->
## TOPIC 00047: niDCPower_GetCalUserDefinedInfoMaxSize

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__calibration__utility_1ga8b1c34fba5a12b3112a9c38f4fad0fb3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__calibration__utility_1ga8b1c34fba5a12b3112a9c38f4fad0fb3.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of characters that can be used to store user-defined information in the device onboard EEPROM. SyntaxViStatus _VI_FUNC niDCPower_GetCalUserDefinedInfoMaxSize(ViSession vi, ViInt32 *infoSize)RemarksThis function can only be used in a session initialized to a single instrume

### niDCPower_GetCalUserDefinedInfoMaxSize

Returns the maximum number of characters that can be used to store user-defined information in the device onboard EEPROM.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetCalUserDefinedInfoMaxSize(ViSession vi, ViInt32 *infoSize)

#### Remarks

Note

This function can only be used in a session initialized to a single instrument.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithIndependentChannels function. |
| infoSize | [out] | ViInt32 * | Returns the number of characters that can be stored in the device onboard EEPROM. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__calibration__utility_1gab4e1fd8dcae834a678ef36a235956e9e.html language=enus -->
## TOPIC 00048: niDCPower_GetExtCalRecommendedInterval

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__calibration__utility_1gab4e1fd8dcae834a678ef36a235956e9e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__calibration__utility_1gab4e1fd8dcae834a678ef36a235956e9e.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended maximum interval, in months, between external calibrations. SyntaxViStatus _VI_FUNC niDCPower_GetExtCalRecommendedInterval(ViSession vi, ViInt32 *months)RemarksThis function can only be used in a session initialized to a single instrument.ParametersNameDirectionTypeDescriptio

### niDCPower_GetExtCalRecommendedInterval

Returns the recommended maximum interval, in **months**, between external calibrations.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetExtCalRecommendedInterval(ViSession vi, ViInt32 *months)

#### Remarks

Note

This function can only be used in a session initialized to a single instrument.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithIndependentChannels function. |
| months | [out] | ViInt32 * | Specifies the recommended maximum interval, in months, between external calibrations. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__calibration__utility_1gabc27927e3acb79c1950c381e037df9c0.html language=enus -->
## TOPIC 00049: niDCPower_GetCalUserDefinedInfo

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__calibration__utility_1gabc27927e3acb79c1950c381e037df9c0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__calibration__utility_1gabc27927e3acb79c1950c381e037df9c0.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the user-defined information in the device onboard EEPROM. SyntaxViStatus _VI_FUNC niDCPower_GetCalUserDefinedInfo(ViSession vi, ViString info)RemarksThis function can only be used in a session initialized to a single instrument.ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies

### niDCPower_GetCalUserDefinedInfo

Returns the user-defined information in the device onboard EEPROM.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetCalUserDefinedInfo(ViSession vi, ViString info)

#### Remarks

Note

This function can only be used in a session initialized to a single instrument.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithIndependentChannels function. |
| info | [out] | ViString | Returns the user-defined information stored in the device onboard EEPROM. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__calibration__utility_1gacbbeca07a46f190af70dad82b798acc4.html language=enus -->
## TOPIC 00050: niDCPower_GetExtCalLastDateAndTime

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__calibration__utility_1gacbbeca07a46f190af70dad82b798acc4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__calibration__utility_1gacbbeca07a46f190af70dad82b798acc4.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this function returns 14 for hours and 30 for minutes. SyntaxViStatus _VI_FUNC niDCPower_GetExtCalLastDateAndTime(ViSession vi, ViIn

### niDCPower_GetExtCalLastDateAndTime

Returns the date and time of the last successful calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this function returns 14 for **hours** and 30 for **minutes**.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetExtCalLastDateAndTime(ViSession vi, ViInt32 *year, ViInt32 *month, ViInt32 *day, ViInt32 *hour, ViInt32 *minute)

#### Remarks

Note

This function can only be used in a session initialized to a single instrument.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithIndependentChannels function. |
| year | [out] | ViInt32 * | Returns the year the device was last calibrated. |
| month | [out] | ViInt32 * | Returns the month in which the device was last calibrated. |
| day | [out] | ViInt32 * | Returns the day on which the device was last calibrated. |
| hour | [out] | ViInt32 * | Returns the hour (in 24-hour time) in which the device was last calibrated. |
| minute | [out] | ViInt32 * | Returns the minute in which the device was last calibrated. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration.html language=enus -->
## TOPIC 00051: External Calibration

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDCPower_CalAdjustACFlatnessAdjusts the AC voltage flatness calibration based on the frequency and voltage stimulus values generated by niDCPower_CalConfigACFlatness and the voltage measured by an external oscilloscope. niDCPower_CalAdjustCurrentLimitCalculates

### External Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDCPower_CalAdjustACFlatness | Adjusts the AC voltage flatness calibration based on the frequency and voltage stimulus values generated by niDCPower_CalConfigACFlatness and the voltage measured by an external oscilloscope. |
| niDCPower_CalAdjustCurrentLimit | Calculates the calibration constants for the current limit for the specified channel and range. This function compares the array in requestedOutputs to the array in measuredOutputs and calculates the calibration constants for the current limit returned by the device. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session. |
| niDCPower_CalAdjustCurrentMeasurement | Calibrates the current measurements returned by the niDCPower_Measure function for the specified channel. This function calculates new calibration coefficients for the specified current measurement range based on the reportedOutputs and measuredOutputs. Refer to the calibration procedure for the device you are calibrating for detailed instructions about the appropriate use of this function. This function can only be called in an external calibration session. |
| niDCPower_CalAdjustInternalReference | Programs the adjusted reference value to the device. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session. |
| niDCPower_CalAdjustOutputResistance | Compares the array in requestedOutputs to the array in measuredOutputs and calculates the calibration constants for the output resistance of the specified channel. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session. |
| niDCPower_CalAdjustResidualCurrentOffset | Calculates the calibration constants for the residual current offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal switching. |
| niDCPower_CalAdjustResidualVoltageOffset | Calculates the calibration constants for the residual voltage offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal switching. |
| niDCPower_CalAdjustVoltageLevel | Calculates the calibration constants for the voltage level for the specified channel. This function compares the array in requestedOutputs to the array in measuredOutputs and calculates the calibration constants for the voltage level of the channel. Refer to the calibration procedure of the device you are calibrating for detailed instructions on the appropriate use of this function. This function can be called only in an external calibration session. |
| niDCPower_CalAdjustVoltageMeasurement | Calculates the calibration constants for the voltage measurements returned by the niDCPower_Measure function for the specified channel. This function compares the array in reportedOutputs to the array in measuredOutputs and calculates the calibration constants for the voltage measurements returned by the niDCPower_Measure function. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called in an external calibration session. |
| niDCPower_CalBeginACFlatness | Prepares the driver and device state for AC voltage flatness calibration and returns the number of steps in the calibration procedure. |
| niDCPower_CalConfigACFlatness | Configures the device to output a voltage stimulus for AC voltage flatness calibration. |
| niDCPower_CalEndACFlatness | Ends the AC voltage flatness calibration. |
| niDCPower_CloseExtCal | Closes the session specified in vi and deallocates the resources that NI-DCPower reserved for calibration. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. |
| niDCPower_ConnectInternalReference | Connects the Internal Reference to the Calibration Pin / Measurement Channel in preparation for adjustment. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session. |
| niDCPower_InitExtCal | If password is valid, this function creates a new IVI instrument driver session to the device specified in resourceName and returns an instrument handle you use to identify the device in all subsequent NI-DCPower function calls. This function also sends initialization commands to set the device to the state necessary for the operation of NI-DCPower. |

#### Attachments

None

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1ga07463730ab80a9d7725e1c77f7f451b3.html language=enus -->
## TOPIC 00052: niDCPower_CalAdjustVoltageLevel

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1ga07463730ab80a9d7725e1c77f7f451b3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1ga07463730ab80a9d7725e1c77f7f451b3.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the voltage level for the specified channel. This function compares the array in requestedOutputs to the array in measuredOutputs and calculates the calibration constants for the voltage level of the channel. Refer to the calibration procedure of the device y

### niDCPower_CalAdjustVoltageLevel

Calculates the calibration constants for the voltage level for the specified channel. This function compares the array in **requestedOutputs** to the array in **measuredOutputs** and calculates the calibration constants for the voltage level of the channel. Refer to the calibration procedure of the device you are calibrating for detailed instructions on the appropriate use of this function. This function can be called only in an external calibration session.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustVoltageLevel(ViSession vi, ViConstString channelName, ViReal64 range, ViUInt32 numberOfMeasurements, const ViReal64 requestedOutputs[], const ViReal64 measuredOutputs[])

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument calibration session. vi is obtained from the niDCPower_InitExtCal function. |
| channelName | [in] | ViConstString | Specifies the channel to which these calibration settings apply. |
| range | [in] | ViReal64 | Specifies the range to calibrate with these settings. Only one channel at a time may be calibrated. |
| numberOfMeasurements | [in] | ViUInt32 | Specifies the number of elements in requestedOutputs and measuredOutputs. |
| requestedOutputs | [in] | const ViReal64[] | Specifies an array of the output values requested in the niDCPower_ConfigureVoltageLevel function. |
| measuredOutputs | [in] | const ViReal64[] | Specifies an array of the output values measured by an external precision digital multimeter. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1ga2b64ddfa3526a8a3f707d2864fad76e8.html language=enus -->
## TOPIC 00053: niDCPower_CalAdjustOutputResistance

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1ga2b64ddfa3526a8a3f707d2864fad76e8.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1ga2b64ddfa3526a8a3f707d2864fad76e8.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares the array in requestedOutputs to the array in measuredOutputs and calculates the calibration constants for the output resistance of the specified channel. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function.

### niDCPower_CalAdjustOutputResistance

Compares the array in **requestedOutputs** to the array in **measuredOutputs** and calculates the calibration constants for the output resistance of the specified channel. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustOutputResistance(ViSession vi, ViConstString channelName, ViUInt32 numberOfMeasurements, const ViReal64 requestedOutputs[], const ViReal64 measuredOutputs[])

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument calibration session. vi is obtained from the niDCPower_InitExtCal function. |
| channelName | [in] | ViConstString | Specifies the channel name to which these calibration settings apply. Only one channel at a time can be calibrated. |
| numberOfMeasurements | [in] | ViUInt32 | Specifies the number of elements in requestedOutputs and measuredOutputs. |
| requestedOutputs | [in] | const ViReal64[] | Specifies an array of the output values that were requested in the niDCPower_ConfigureOutputResistance function. |
| measuredOutputs | [in] | const ViReal64[] | Specifies an array of the output values measured by an external precision digital multimeter. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1ga73132eb06a209b1a881b3e2f576fb60b.html language=enus -->
## TOPIC 00054: niDCPower_CalAdjustCurrentMeasurement

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1ga73132eb06a209b1a881b3e2f576fb60b.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1ga73132eb06a209b1a881b3e2f576fb60b.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibrates the current measurements returned by the niDCPower_Measure function for the specified channel. This function calculates new calibration coefficients for the specified current measurement range based on the reportedOutputs and measuredOutputs. Refer to the calibration procedure for the dev

### niDCPower_CalAdjustCurrentMeasurement

Calibrates the current measurements returned by the [niDCPower_Measure](group____root__nidcpower__functions__measure_1ga93106c3c3af7f1e3a3848865ce201d6e.html) function for the specified channel. This function calculates new calibration coefficients for the specified current measurement range based on the **reportedOutputs** and **measuredOutputs**. Refer to the calibration procedure for the device you are calibrating for detailed instructions about the appropriate use of this function. This function can only be called in an external calibration session.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustCurrentMeasurement(ViSession vi, ViConstString channelName, ViReal64 range, ViUInt32 numberOfMeasurements, const ViReal64 reportedOutputs[], const ViReal64 measuredOutputs[])

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument calibration session. vi is obtained from the niDCPower_InitExtCal function. |
| channelName | [in] | ViConstString | Specifies the channel name to which these calibration settings apply. |
| range | [in] | ViReal64 | Specifies the range to calibrate with these settings. Only one channel at a time may be calibrated. |
| numberOfMeasurements | [in] | ViUInt32 | Specifies the number of elements in reportedOutputs and measuredOutputs. |
| reportedOutputs | [in] | const ViReal64[] | Specifies an array of the output values that were returned by the niDCPower_Measure function. |
| measuredOutputs | [in] | const ViReal64[] | Specifies an array of the output values measured by an external precision digital multimeter. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1ga9dee94f4c32526c5670bda9b42b9660a.html language=enus -->
## TOPIC 00055: niDCPower_CalAdjustInternalReference

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1ga9dee94f4c32526c5670bda9b42b9660a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1ga9dee94f4c32526c5670bda9b42b9660a.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Programs the adjusted reference value to the device. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session. SyntaxViStatus _VI_FUNC niDCPower_CalAd

### niDCPower_CalAdjustInternalReference

Programs the adjusted reference value to the device. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustInternalReference(ViSession vi, ViInt32 internalReference, ViReal64 adjustedInternalReference)

#### Remarks

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| internalReference | [in] | ViInt32 | Specifies the internal reference to be adjusted.Defined Values:NameValueDescriptionNIDCPOWER_VAL_INTERNAL_REFERENCE_5V1054 (0x41e)5 V internal reference.NIDCPOWER_VAL_INTERNAL_REFERENCE_100KOHM1055 (0x41f)100 kohms internal reference.NIDCPOWER_VAL_INTERNAL_REFERENCE_GROUND1056 (0x420)Ground reference.NIDCPOWER_VAL_INTERNAL_REFERENCE_NONE1057 (0x421)No internal reference.NIDCPOWER_VAL_INTERNAL_REFERENCE_7V1119 (0x45f)7 V internal reference.NIDCPOWER_VAL_INTERNAL_REFERENCE_1KOHM1120 (0x460)1 kohms internal reference. |
| Name | Value | Description |  |
| NIDCPOWER_VAL_INTERNAL_REFERENCE_5V | 1054 (0x41e) | 5 V internal reference. |  |
| NIDCPOWER_VAL_INTERNAL_REFERENCE_100KOHM | 1055 (0x41f) | 100 kohms internal reference. |  |
| NIDCPOWER_VAL_INTERNAL_REFERENCE_GROUND | 1056 (0x420) | Ground reference. |  |
| NIDCPOWER_VAL_INTERNAL_REFERENCE_NONE | 1057 (0x421) | No internal reference. |  |
| NIDCPOWER_VAL_INTERNAL_REFERENCE_7V | 1119 (0x45f) | 7 V internal reference. |  |
| NIDCPOWER_VAL_INTERNAL_REFERENCE_1KOHM | 1120 (0x460) | 1 kohms internal reference. |  |
| adjustedInternalReference | [in] | ViReal64 | Specifies the updated value of the internal reference that will be programmed to the device. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1ga9e3060581a85dc20d60bb89261994d04.html language=enus -->
## TOPIC 00056: niDCPower_CalAdjustResidualVoltageOffset

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1ga9e3060581a85dc20d60bb89261994d04.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1ga9e3060581a85dc20d60bb89261994d04.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the residual voltage offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal s

### niDCPower_CalAdjustResidualVoltageOffset

Calculates the calibration constants for the residual voltage offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal switching.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustResidualVoltageOffset(ViSession vi, ViConstString channelName)

#### Remarks

This function requires that the output be shorted prior to it being invoked.

Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can be called only in an external calibration session.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1gab7aef18606a59dbcf669959e67909ab0.html language=enus -->
## TOPIC 00057: niDCPower_CalAdjustACFlatness

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1gab7aef18606a59dbcf669959e67909ab0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1gab7aef18606a59dbcf669959e67909ab0.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the AC voltage flatness calibration based on the frequency and voltage stimulus values generated by niDCPower_CalConfigACFlatness and the voltage measured by an external oscilloscope. SyntaxViStatus _VI_FUNC niDCPower_CalAdjustACFlatness(ViSession vi, ViConstString channelName, ViReal64 gene

### niDCPower_CalAdjustACFlatness

Adjusts the AC voltage flatness calibration based on the frequency and voltage stimulus values generated by [niDCPower_CalConfigACFlatness](group____root__nidcpower__functions__calibration__external__calibration_1gadbf86771191c00af8eaed32ae27e07dd.html) and the voltage measured by an external oscilloscope.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustACFlatness(ViSession vi, ViConstString channelName, ViReal64 generatedFrequency, ViReal64 generatedVoltageRMS, ViReal64 measuredVoltageRMS, ViUInt32 *numberOfStepsRemaining)

#### Remarks

This function returns the number of steps remaining in the calibration procedure.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument calibration session. vi is obtained from the niDCPower_InitExtCal function. |
| channelName | [in] | ViConstString | Specifies the channel to which these calibration settings apply. Only one channel at a time can be calibrated. |
| generatedFrequency | [in] | ViReal64 | Specifies the generated frequency, in Hz, utilized by the oscilloscope for the present AC flatness calibration step. |
| generatedVoltageRMS | [in] | ViReal64 | Specifies the RMS voltage, in volts, utilitized by the oscilloscope for the present AC flatness calibration step. |
| measuredVoltageRMS | [in] | ViReal64 | Specifies the RMS voltage, in volts, measured by the oscilloscope for the present AC flatness calibration step. |
| numberOfStepsRemaining | [out] | ViUInt32 * | Returns the remaining number of steps to complete the AC flatness calibration. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1gabdacab2e82a6f880b719027b9a4d02ea.html language=enus -->
## TOPIC 00058: niDCPower_CalAdjustCurrentLimit

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1gabdacab2e82a6f880b719027b9a4d02ea.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1gabdacab2e82a6f880b719027b9a4d02ea.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the current limit for the specified channel and range. This function compares the array in requestedOutputs to the array in measuredOutputs and calculates the calibration constants for the current limit returned by the device. Refer to the calibration procedu

### niDCPower_CalAdjustCurrentLimit

Calculates the calibration constants for the current limit for the specified channel and range. This function compares the array in **requestedOutputs** to the array in **measuredOutputs** and calculates the calibration constants for the current limit returned by the device. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can only be called from an external calibration session.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustCurrentLimit(ViSession vi, ViConstString channelName, ViReal64 range, ViUInt32 numberOfMeasurements, const ViReal64 requestedOutputs[], const ViReal64 measuredOutputs[])

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument calibration session. vi is obtained from the niDCPower_InitExtCal function. |
| channelName | [in] | ViConstString | Specifies the channel name to which these calibration settings apply. |
| range | [in] | ViReal64 | Specifies the range to calibrate with these settings. Only one channel at a time may be calibrated. |
| numberOfMeasurements | [in] | ViUInt32 | Specifies the number of elements in requestedOutputs and measuredOutputs. |
| requestedOutputs | [in] | const ViReal64[] | Specifies an array of the output values that were requested in the niDCPower_ConfigureCurrentLimit function. |
| measuredOutputs | [in] | const ViReal64[] | Specifies an array of the output values measured by an external precision digital multimeter. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1gadbf86771191c00af8eaed32ae27e07dd.html language=enus -->
## TOPIC 00059: niDCPower_CalConfigACFlatness

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1gadbf86771191c00af8eaed32ae27e07dd.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1gadbf86771191c00af8eaed32ae27e07dd.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to output a voltage stimulus for AC voltage flatness calibration. SyntaxViStatus _VI_FUNC niDCPower_CalConfigACFlatness(ViSession vi, ViConstString channelName, ViReal64 *generatedFrequency, ViReal64 *generatedVoltageRMS)RemarksThis function returns the generated frequency and

### niDCPower_CalConfigACFlatness

Configures the device to output a voltage stimulus for AC voltage flatness calibration.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalConfigACFlatness(ViSession vi, ViConstString channelName, ViReal64 *generatedFrequency, ViReal64 *generatedVoltageRMS)

#### Remarks

This function returns the generated frequency and voltage stimulus value.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument calibration session. vi is obtained from the niDCPower_InitExtCal function. |
| channelName | [in] | ViConstString | Specifies the channel to which these calibration settings apply. Only one channel at a time can be calibrated. |
| generatedFrequency | [out] | ViReal64 * | Returns the generated frequency for the present AC flatness calibration step. |
| generatedVoltageRMS | [out] | ViReal64 * | Returns the generated nominal RMS voltage, in volts, for the present AC flatness calibration step. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__external__calibration_1gadddff4a734cf374089d7b79af99adfea.html language=enus -->
## TOPIC 00060: niDCPower_CalAdjustResidualCurrentOffset

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__external__calibration_1gadddff4a734cf374089d7b79af99adfea.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__external__calibration_1gadddff4a734cf374089d7b79af99adfea.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the residual current offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal s

### niDCPower_CalAdjustResidualCurrentOffset

Calculates the calibration constants for the residual current offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal switching.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustResidualCurrentOffset(ViSession vi, ViConstString channelName)

#### Remarks

This function requires that the output be open prior to it being invoked.

Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this function. This function can be called only in an external calibration session.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__lcr__compensation_1ga84f15819403db31fbc82e7cb0dd1bba6.html language=enus -->
## TOPIC 00061: niDCPower_ConfigureLCRCompensation

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__lcr__compensation_1ga84f15819403db31fbc82e7cb0dd1bba6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__lcr__compensation_1ga84f15819403db31fbc82e7cb0dd1bba6.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies previously generated open, short, load, as well as open and short custom cable compensation data to LCR measurements. SyntaxViStatus _VI_FUNC niDCPower_ConfigureLCRCompensation(ViSession vi, ViConstString channelName, ViInt32 compensationDataSize, ViAddr compensationData)RemarksThis function

### niDCPower_ConfigureLCRCompensation

Applies previously generated open, short, load, as well as open and short custom cable compensation data to LCR measurements.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureLCRCompensation(ViSession vi, ViConstString channelName, ViInt32 compensationDataSize, ViAddr compensationData)

#### Remarks

This function applies open, short and load compensation data when you have set [NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE](group____root__nidcpower__attributes__lcr__compensation_1ga543647054da614f336abf22f1938bd51.html) to **NIDCPOWER_VAL_AS_CONFIGURED**, and it also applies custom cable compensation data when you have set [NIDCPOWER_ATTR_CABLE_LENGTH](group____root__nidcpower__attributes__device__specific__lcr_1gab854b2ef8812ccb9cf98b2725f92410c.html) to **NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED**

Call this function after you have obtained LCR compensation data. If [NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED](group____root__nidcpower__attributes__lcr__compensation_1ga3037309c86c1fca4678d86a5eec85b25.html) is set to true, you must generate data with both [niDCPower_PerformLCROpenCustomCableCompensation](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga8271e1c061151198faf4210d92a6c8c2.html) and [niDCPower_PerformLCRShortCustomCableCompensation](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga0a626105e3ffa7f72d3299bd3c9d66ae.html); if false, you must only use [niDCPower_PerformLCROpenCustomCableCompensation](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga8271e1c061151198faf4210d92a6c8c2.html), and NI-DCPower uses default short data.

Call [niDCPower_GetLCRCompensationData](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga69ad9d2d281c7c38d2f2912721d395b0.html) and pass the **compensation data** to this function.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| compensationDataSize | [in] | ViInt32 | Specifies the size, in bytes, of compensationData to apply. |
| compensationData | [in] | ViAddr | The open, short and load compensation data to apply. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__lcr__compensation_1gaf1342f0433cb09cd27aece9f001b1ccf.html language=enus -->
## TOPIC 00062: niDCPower_GetLCRCompensationLastDateAndTime

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__lcr__compensation_1gaf1342f0433cb09cd27aece9f001b1ccf.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__lcr__compensation_1gaf1342f0433cb09cd27aece9f001b1ccf.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time the specified type of compensation data for LCR measurements was most recently generated. SyntaxViStatus _VI_FUNC niDCPower_GetLCRCompensationLastDateAndTime(ViSession vi, ViConstString channelName, ViInt32 compensationType, ViInt32 *year, ViInt32 *month, ViInt32 *day, ViIn

### niDCPower_GetLCRCompensationLastDateAndTime

Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetLCRCompensationLastDateAndTime(ViSession vi, ViConstString channelName, ViInt32 compensationType, ViInt32 *year, ViInt32 *month, ViInt32 *day, ViInt32 *hour, ViInt32 *minute)

#### Remarks

The time returned is 24-hour (military) local time; for example, if the selected type of compensation data was generated at 2:30 PM, this VI returns 14 for **hours** and 30 for **minutes**.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| compensationType | [in] | ViInt32 | Specifies the type of compensation for LCR measurements.Defined Values:NameValueDescriptionNIDCPOWER_VAL_OPEN_COMPENSATION1130 (0x46a)Returns the date and time that open LCR compensation data was most recently generated.NIDCPOWER_VAL_SHORT_COMPENSATION1131 (0x46b)Returns the date and time that short LCR compensation data was most recently generated.NIDCPOWER_VAL_LOAD_COMPENSATION1132 (0x46c)Returns the date and time that load LCR compensation data was most recently generated.NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION1133 (0x46d)Returns the date and time that open custom cable compensation data was most recently generated.NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION1134 (0x46e)Returns the date and time that short custom cable compensation data was most recently generated. |
| Name | Value | Description |  |
| NIDCPOWER_VAL_OPEN_COMPENSATION | 1130 (0x46a) | Returns the date and time that open LCR compensation data was most recently generated. |  |
| NIDCPOWER_VAL_SHORT_COMPENSATION | 1131 (0x46b) | Returns the date and time that short LCR compensation data was most recently generated. |  |
| NIDCPOWER_VAL_LOAD_COMPENSATION | 1132 (0x46c) | Returns the date and time that load LCR compensation data was most recently generated. |  |
| NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION | 1133 (0x46d) | Returns the date and time that open custom cable compensation data was most recently generated. |  |
| NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION | 1134 (0x46e) | Returns the date and time that short custom cable compensation data was most recently generated. |  |
| year | [out] | ViInt32 * | Returns the year the specific LCR compensationType was performed on the device. |
| month | [out] | ViInt32 * | Returns the month the specific LCR compensationType was performed on the device. |
| day | [out] | ViInt32 * | Returns the day the specific LCR compensationType was performed on the device. |
| hour | [out] | ViInt32 * | Returns the hour the specific LCR compensationType was performed on the device. |
| minute | [out] | ViInt32 * | Returns the minute the specific LCR compensationType was performed on the device. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation.html language=enus -->
## TOPIC 00063: LCR Custom Cable Compensation

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDCPower_GetLCRCompensationDataCollects previously generated open, short, load compensation data as well as open and short custom cable compensation data so you can then apply it to LCR measurements with niDCPower_ConfigureLCRCompensation. niDCPower_PerformLCRO

### LCR Custom Cable Compensation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDCPower_GetLCRCompensationData | Collects previously generated open, short, load compensation data as well as open and short custom cable compensation data so you can then apply it to LCR measurements with niDCPower_ConfigureLCRCompensation. |
| niDCPower_PerformLCROpenCustomCableCompensation | Generates open custom cable compensation data for LCR measurements. |
| niDCPower_PerformLCRShortCustomCableCompensation | Generates short custom cable compensation data for LCR measurements. |

#### Attachments

None

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__control_1ga1f65932d785595695b117e36a76877a0.html language=enus -->
## TOPIC 00064: niDCPower_AbortWithChannels

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__control_1ga1f65932d785595695b117e36a76877a0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__control_1ga1f65932d785595695b117e36a76877a0.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transitions the specified channel(s) from the Running state to the Uncommitted state. If a sequence is running, it is stopped. SyntaxViStatus _VI_FUNC niDCPower_AbortWithChannels(ViSession vi, ViConstString channelName)RemarksAny configuration functions called after this function are not applied unt

### niDCPower_AbortWithChannels

Transitions the specified channel(s) from the Running state to the Uncommitted state. If a sequence is running, it is stopped.

#### Syntax

ViStatus _VI_FUNC niDCPower_AbortWithChannels(ViSession vi, ViConstString channelName)

#### Remarks

Any configuration functions called after this function are not applied until the [niDCPower_InitiateWithChannels](group____root__nidcpower__functions__control_1ga76b7224de94b21cceebe43bb4e6a867c.html) function is called. If power output is enabled when you call this function, the channel(s) remain in their current state and continue providing power.

Use the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function or the [niDCPower_ResetWithChannels](group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html) function to disable power output on a per-channel basis.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

**Related Topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Control

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__control_1ga21679973682c594d89918cc3d6bb40f2.html language=enus -->
## TOPIC 00065: niDCPower_CommitWithChannels

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__control_1ga21679973682c594d89918cc3d6bb40f2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__control_1ga21679973682c594d89918cc3d6bb40f2.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies previously configured settings to the specified channel(s). Calling this function moves the channel(s) from the Uncommitted state into the Committed state. After calling this function, modifying any attribute reverts the channel(s) to the Uncommitted state. Use the niDCPower_InitiateWithChan

### niDCPower_CommitWithChannels

Applies previously configured settings to the specified channel(s). Calling this function moves the channel(s) from the Uncommitted state into the Committed state. After calling this function, modifying any attribute reverts the channel(s) to the Uncommitted state. Use the [niDCPower_InitiateWithChannels](group____root__nidcpower__functions__control_1ga76b7224de94b21cceebe43bb4e6a867c.html) function to transition to the Running state.

#### Syntax

ViStatus _VI_FUNC niDCPower_CommitWithChannels(ViSession vi, ViConstString channelName)

#### Remarks

**Related Topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Control

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__control_1gaa2343cefc7fed5b98999cd067e73df67.html language=enus -->
## TOPIC 00066: niDCPower_Commit

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__control_1gaa2343cefc7fed5b98999cd067e73df67.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__control_1gaa2343cefc7fed5b98999cd067e73df67.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_CommitWithChannels instead. SyntaxViStatus _VI_FUNC niDCPower_Commit(ViSession vi)RemarksApplies previously configured settings to the device. Calling this function moves the NI-DCPower session from the Uncommitted state into the Committed state. After call

### niDCPower_Commit

This function is deprecated. Use [niDCPower_CommitWithChannels](group____root__nidcpower__functions__control_1ga21679973682c594d89918cc3d6bb40f2.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_Commit(ViSession vi)

#### Remarks

Applies previously configured settings to the device. Calling this function moves the NI-DCPower session from the Uncommitted state into the Committed state. After calling this function, modifying any attribute reverts the NI-DCPower session to the Uncommitted state. Use the [niDCPower_Initiate](group____root__nidcpower__functions__control_1gae9bf18cbfd1cacb74348612e260e5fb5.html) function to transition to the Running state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for details about the specific NI-DCPower software states.

**Related Topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Control

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__measure_1ga70b46ae3239cd049179c751d42ebfc84.html language=enus -->
## TOPIC 00067: niDCPower_ConfigureSense

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__measure_1ga70b46ae3239cd049179c751d42ebfc84.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__measure_1ga70b46ae3239cd049179c751d42ebfc84.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use local or remote sensing of the output voltage on the specified channel(s). Refer to the Devices topic specific to your device in the NI DC Power Supplies and SMUs Help for more information about sensing voltage on supported channels. SyntaxViStatus _VI_FUNC niDCPower_Configu

### niDCPower_ConfigureSense

Specifies whether to use local or remote sensing of the output voltage on the specified channel(s). Refer to the *Devices* topic specific to your device in the *NI DC Power Supplies and SMUs* Help for more information about sensing voltage on supported channels.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureSense(ViSession vi, ViConstString channelName, ViInt32 sense)

#### Remarks

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| sense | [in] | ViInt32 | Specifies local or remote sensing on the specified channel(s).Defined Values:NameValueDescriptionNIDCPOWER_VAL_LOCAL1008 (0x3f0)Local sensingNIDCPOWER_VAL_REMOTE1009 (0x3f1)Remote sensing |
| Name | Value | Description |  |
| NIDCPOWER_VAL_LOCAL | 1008 (0x3f0) | Local sensing |  |
| NIDCPOWER_VAL_REMOTE | 1009 (0x3f1) | Remote sensing |  |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__measure_1gaedecb08bb43fb20bccb8951abb9b2e57.html language=enus -->
## TOPIC 00068: niDCPower_FetchMultipleLCR

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__measure_1gaedecb08bb43fb20bccb8951abb9b2e57.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__measure_1gaedecb08bb43fb20bccb8951abb9b2e57.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of previously measured LCR data on the specified channel that have been taken and stored in a buffer. SyntaxViStatus _VI_FUNC niDCPower_FetchMultipleLCR(ViSession vi, ViConstString channelName, ViReal64 timeout, ViInt32 count, NILCRMeasurement measurements[], ViInt32 *actualCount)Re

### niDCPower_FetchMultipleLCR

Returns an array of previously measured LCR data on the specified channel that have been taken and stored in a buffer.

#### Syntax

ViStatus _VI_FUNC niDCPower_FetchMultipleLCR(ViSession vi, ViConstString channelName, ViReal64 timeout, ViInt32 count, NILCRMeasurement measurements[], ViInt32 *actualCount)

#### Remarks

To use this function:

- Set [NIDCPOWER_ATTR_MEASURE_WHEN](group____root__nidcpower__attributes__measure__advanced_1ga0b6f83a01a306308618acafec479ac43.html) to **NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE** or **NIDCPOWER_VAL_ON_MEASURE_TRIGGER**; and
- Put the channel(s) in the Running state (call [niDCPower_Initiate](group____root__nidcpower__functions__control_1gae9bf18cbfd1cacb74348612e260e5fb5.html)).

Note

When setting the timeout interval with **timeout**, ensure you take into account any triggers so that the timeout interval is long enough for your application.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| timeout | [in] | ViReal64 | Specifies the maximum time allowed for this function to complete, in seconds. If the function does not complete within this time interval, NI-DCPower returns an error. |
| count | [in] | ViInt32 | Specifies the number of measurements to fetch. |
| measurements | [out] | NILCRMeasurement[] | Returns an array of LCR measurement data.NILCRMeasurement:NameTypeDescriptionVdcViReal64The measured DC voltage, in volts.IdcViReal64The measured DC current, in amps.stimulusFrequencyViReal64The frequency of the LCR test signal, in Hz.ACVoltageNIComplexNumberThe measured AC voltage, in volts RMS.ACCurrentNIComplexNumberThe measured AC current, in amps RMS.ZNIComplexNumberThe complex impedance.ZMagnitudeViReal64The magnitude of the complex impedance, in ohms.ZPhaseViReal64The impedance phase angle, in degrees.YNIComplexNumberThe complex admittance.YMagnitudeViReal64The magnitude of the complex admittance, in siemens.YPhaseViReal64The admittance phase angle, in degrees.LsViReal64The inductance, in henrys, as measured using a series circuit model.CsViReal64The capacitance, in farads, as measured using a series circuit model.RsViReal64The resistance, in ohms, as measured using a series circuit model.LpViReal64The inductance, in henrys, as measured using a parallel circuit model.CpViReal64The capacitance, in farads, as measured using a parallel circuit model.RpViReal64The resistance, in ohms, as measured using a parallel circuit model.DViReal64The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor.QViReal64The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.measurementModeViUInt16Returns the measurement mode.dcInComplianceViBooleanIndicates whether the output was in DC compliance at the time the measurement was taken.acInComplianceViBooleanIndicates whether the output was in AC compliance at the time the measurement was taken.unbalancedViBooleanIndicates whether the bridge was unbalanced at the time the measurement was taken.measurementMode Defined Values:NameValueDescriptionNIDCPOWER_VAL_SMU_PS1061 (0x425)The channel(s) are operating as a power supply/SMU.NIDCPOWER_VAL_LCR1062 (0x426)The channel(s) are operating as an LCR meter. |
| Name | Type | Description |  |
| Vdc | ViReal64 | The measured DC voltage, in volts. |  |
| Idc | ViReal64 | The measured DC current, in amps. |  |
| stimulusFrequency | ViReal64 | The frequency of the LCR test signal, in Hz. |  |
| ACVoltage | NIComplexNumber | The measured AC voltage, in volts RMS. |  |
| ACCurrent | NIComplexNumber | The measured AC current, in amps RMS. |  |
| Z | NIComplexNumber | The complex impedance. |  |
| ZMagnitude | ViReal64 | The magnitude of the complex impedance, in ohms. |  |
| ZPhase | ViReal64 | The impedance phase angle, in degrees. |  |
| Y | NIComplexNumber | The complex admittance. |  |
| YMagnitude | ViReal64 | The magnitude of the complex admittance, in siemens. |  |
| YPhase | ViReal64 | The admittance phase angle, in degrees. |  |
| Ls | ViReal64 | The inductance, in henrys, as measured using a series circuit model. |  |
| Cs | ViReal64 | The capacitance, in farads, as measured using a series circuit model. |  |
| Rs | ViReal64 | The resistance, in ohms, as measured using a series circuit model. |  |
| Lp | ViReal64 | The inductance, in henrys, as measured using a parallel circuit model. |  |
| Cp | ViReal64 | The capacitance, in farads, as measured using a parallel circuit model. |  |
| Rp | ViReal64 | The resistance, in ohms, as measured using a parallel circuit model. |  |
| D | ViReal64 | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |  |
| Q | ViReal64 | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor. |  |
| measurementMode | ViUInt16 | Returns the measurement mode. |  |
| dcInCompliance | ViBoolean | Indicates whether the output was in DC compliance at the time the measurement was taken. |  |
| acInCompliance | ViBoolean | Indicates whether the output was in AC compliance at the time the measurement was taken. |  |
| unbalanced | ViBoolean | Indicates whether the bridge was unbalanced at the time the measurement was taken. |  |
| Name | Value | Description |  |
| NIDCPOWER_VAL_SMU_PS | 1061 (0x425) | The channel(s) are operating as a power supply/SMU. |  |
| NIDCPOWER_VAL_LCR | 1062 (0x426) | The channel(s) are operating as an LCR meter. |  |
| actualCount | [out] | ViInt32 * | Indicates the number of measured values actually retrieved from the specified channel. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__setget__attribute__set__attribute_1ga9b74e79e1ff158a421d793e79a62711a.html language=enus -->
## TOPIC 00069: niDCPower_SetAttributeViInt64

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__setget__attribute__set__attribute_1ga9b74e79e1ff158a421d793e79a62711a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__setget__attribute__set__attribute_1ga9b74e79e1ff158a421d793e79a62711a.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViInt64 attribute. SyntaxViStatus _VI_FUNC niDCPower_SetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 attributeValue)RemarksThis is a low-level function that you can use to set the values of device-specific attributes and inherent IVI attri

### niDCPower_SetAttributeViInt64

Sets the value of a ViInt64 attribute.

#### Syntax

ViStatus _VI_FUNC niDCPower_SetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt64 attributeValue)

#### Remarks

This is a low-level function that you can use to set the values of device-specific attributes and inherent IVI attributes.

Note

Some of the values might not be valid depending upon the current settings of the device session.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| attributeId | [in] | ViAttr | Specifies the ID of an attribute. |
| attributeValue | [in] | ViInt64 | Specifies the value to which you want to set the attribute. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__setget__attribute__set__attribute_1gaa22576967ae6763acabcc3714f35d491.html language=enus -->
## TOPIC 00070: niDCPower_SetAttributeViInt32

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__setget__attribute__set__attribute_1gaa22576967ae6763acabcc3714f35d491.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__setget__attribute__set__attribute_1gaa22576967ae6763acabcc3714f35d491.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViInt32 attribute. SyntaxViStatus _VI_FUNC niDCPower_SetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 attributeValue)RemarksThis is a low-level function that you can use to set the values of device-specific attributes and inherent IVI attri

### niDCPower_SetAttributeViInt32

Sets the value of a ViInt32 attribute.

#### Syntax

ViStatus _VI_FUNC niDCPower_SetAttributeViInt32(ViSession vi, ViConstString channelName, ViAttr attributeId, ViInt32 attributeValue)

#### Remarks

This is a low-level function that you can use to set the values of device-specific attributes and inherent IVI attributes.

Note

Some of the values might not be valid depending upon the current settings of the device session.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| attributeId | [in] | ViAttr | Specifies the ID of an attribute. |
| attributeValue | [in] | ViInt32 | Specifies the value to which you want to set the attribute. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attribute

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__advanced__sequencing_1ga2bac8e95b9c1d049d87889a0f6f841cc.html language=enus -->
## TOPIC 00071: niDCPower_DeleteAdvancedSequence

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__advanced__sequencing_1ga2bac8e95b9c1d049d87889a0f6f841cc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__advanced__sequencing_1ga2bac8e95b9c1d049d87889a0f6f841cc.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_DeleteAdvancedSequenceWithChannels instead. SyntaxViStatus _VI_FUNC niDCPower_DeleteAdvancedSequence(ViSession vi, ViConstString sequenceName)RemarksDeletes a previously created advanced sequence and all the advanced sequence steps in the advanced sequence.

### niDCPower_DeleteAdvancedSequence

This function is deprecated. Use [niDCPower_DeleteAdvancedSequenceWithChannels](group____root__nidcpower__functions__source__advanced__sequencing_1ga9e35ac4cadaddb847b4bdc9b2734e56e.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_DeleteAdvancedSequence(ViSession vi, ViConstString sequenceName)

#### Remarks

Deletes a previously created advanced sequence and all the advanced sequence steps in the advanced sequence.

**Support for this Function**

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

You must set the source mode to Sequence to use this function.

Using the [niDCPower_SetSequence](group____root__nidcpower__functions__source_1ga8df5d6bbbe1e3c0ebd0ef10175b080f4.html) function with Advanced Sequence functions is unsupported.

**Related Topics**:

[Advanced Sequencing](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| sequenceName | [in] | ViConstString | specifies the name of the sequence to delete. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced Sequencing

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__advanced__sequencing_1ga9e35ac4cadaddb847b4bdc9b2734e56e.html language=enus -->
## TOPIC 00072: niDCPower_DeleteAdvancedSequenceWithChannels

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__advanced__sequencing_1ga9e35ac4cadaddb847b4bdc9b2734e56e.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__advanced__sequencing_1ga9e35ac4cadaddb847b4bdc9b2734e56e.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a previously created advanced sequence and all the advanced sequence steps in the advanced sequence. SyntaxViStatus _VI_FUNC niDCPower_DeleteAdvancedSequenceWithChannels(ViSession vi, ViConstString channelName, ViConstString sequenceName)RemarksSupport for this FunctionThis function is not s

### niDCPower_DeleteAdvancedSequenceWithChannels

Deletes a previously created advanced sequence and all the advanced sequence steps in the advanced sequence.

#### Syntax

ViStatus _VI_FUNC niDCPower_DeleteAdvancedSequenceWithChannels(ViSession vi, ViConstString channelName, ViConstString sequenceName)

#### Remarks

**Support for this Function**

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

You must set the source mode to Sequence to use this function.

Using the [niDCPower_SetSequence](group____root__nidcpower__functions__source_1ga8df5d6bbbe1e3c0ebd0ef10175b080f4.html) function with Advanced Sequence functions for the same channel in the same session is unsupported.

**Related Topics**:

[Advanced Sequencing](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| sequenceName | [in] | ViConstString | specifies the name of the sequence to delete. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced Sequencing

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__dc__current_1ga80a35e9e40486359f0964dce15c89e91.html language=enus -->
## TOPIC 00073: niDCPower_ConfigureVoltageLimit

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__dc__current_1ga80a35e9e40486359f0964dce15c89e91.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__dc__current_1ga80a35e9e40486359f0964dce15c89e91.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage limit for the specified channel(s). The channel must be enabled for the specified voltage limit to take effect. Refer to the niDCPower_ConfigureOutputEnabled function for more information about enabling the channel. SyntaxViStatus _VI_FUNC niDCPower_ConfigureVoltageLimit(ViSes

### niDCPower_ConfigureVoltageLimit

Configures the voltage limit for the specified channel(s). The channel must be enabled for the specified voltage limit to take effect. Refer to the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function for more information about enabling the channel.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureVoltageLimit(ViSession vi, ViConstString channelName, ViReal64 limit)

#### Remarks

The voltage limit is the voltage that the output should not exceed when generating the desired current level ([niDCPower_ConfigureCurrentLevel](group____root__nidcpower__functions__source__dc__current_1ga6744316a35dbd33f4e7bada0af72c58e.html)). The voltage limit setting is applicable only if the output function of the channel is set to **NIDCPOWER_VAL_DC_CURRENT**. Use [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) to set the output function.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| limit | [in] | ViReal64 | Specifies the voltage limit, in volts, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.Valid Values: The valid values for this parameter are defined by the voltage limit range that is configured using the niDCPower_ConfigureVoltageLimitRange function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__dc__voltage_1gaf8e647a5c250a22507b8d9a9b68ffe6b.html language=enus -->
## TOPIC 00074: niDCPower_ConfigureCurrentLimitRange

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__dc__voltage_1gaf8e647a5c250a22507b8d9a9b68ffe6b.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__dc__voltage_1gaf8e647a5c250a22507b8d9a9b68ffe6b.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the current limit range for the specified channel(s).The configured range defines the valid values the current limit can be set to using the niDCPower_ConfigureCurrentLimit function. The current limit range setting is applicable only if the output function of the channel is set to NIDCPOW

### niDCPower_ConfigureCurrentLimitRange

Configures the current limit range for the specified channel(s).The configured range defines the valid values the current limit can be set to using the [niDCPower_ConfigureCurrentLimit](group____root__nidcpower__functions__source__dc__voltage_1gac7cf3668bb028dee399d4f04f29c25ab.html) function. The current limit range setting is applicable only if the output function of the channel is set to **NIDCPOWER_VAL_DC_VOLTAGE**. Use [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) to set the output function.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureCurrentLimitRange(ViSession vi, ViConstString channelName, ViReal64 range)

#### Remarks

Use the [NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE](group____root__nidcpower__attributes__source__dc__voltage_1ga3cd50bb501f89bae822c1bb6b854e93a.html) attribute to enable automatic selection of the current limit range.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| range | [in] | ViReal64 | Specifies the current limit range, in amps, for the specified channel(s).For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__pulse__current_1ga6f8271416d5bb4781b33f2b1b58432ce.html language=enus -->
## TOPIC 00075: niDCPower_ConfigurePulseCurrentLevel

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__pulse__current_1ga6f8271416d5bb4781b33f2b1b58432ce.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__pulse__current_1ga6f8271416d5bb4781b33f2b1b58432ce.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse current level that the specified channel(s) attempt to generate during the on phase of a pulse. A channel must be enabled for the specified current level to take effect. SyntaxViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLevel(ViSession vi, ViConstString channelName, ViReal6

### niDCPower_ConfigurePulseCurrentLevel

Configures the pulse current level that the specified channel(s) attempt to generate during the on phase of a pulse. A channel must be enabled for the specified current level to take effect.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLevel(ViSession vi, ViConstString channelName, ViReal64 level)

#### Remarks

Refer to the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function for more information about enabling the channel. The pulse current level setting is applicable only if the channel is set to the **NIDCPOWER_VAL_PULSE_CURRENT** output function using the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function.

Channels actively regulate the current at the specified level unless doing so causes a voltage drop greater than the pulse voltage limit ([NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT](group____root__nidcpower__attributes__source__pulse__current_1gab4b54ded02a028cef279a6f90d956341.html)) across the channels' output terminals.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| level | [in] | ViReal64 | Specifies the pulse current level, in amps, on the specified channel(s).Valid Values: The valid values for this parameter are defined by the pulse current level range that is configured using the niDCPower_ConfigurePulseCurrentLevelRange function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Pulse Current

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__pulse__current_1gacc48de7481d181335ee8a70b6c2c0c7c.html language=enus -->
## TOPIC 00076: niDCPower_ConfigurePulseVoltageLimit

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__pulse__current_1gacc48de7481d181335ee8a70b6c2c0c7c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__pulse__current_1gacc48de7481d181335ee8a70b6c2c0c7c.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse voltage limit for the specified channel(s). A channel must be enabled for the specified voltage limit to take effect. SyntaxViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLimit(ViSession vi, ViConstString channelName, ViReal64 limit)RemarksRefer to the niDCPower_ConfigureOutpu

### niDCPower_ConfigurePulseVoltageLimit

Configures the pulse voltage limit for the specified channel(s). A channel must be enabled for the specified voltage limit to take effect.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLimit(ViSession vi, ViConstString channelName, ViReal64 limit)

#### Remarks

Refer to the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function for more information about enabling the channel. The pulse voltage limit is the voltage that the output must not exceed when generating the desired pulse current level ([NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL](group____root__nidcpower__attributes__source__pulse__current_1gabc7d96dd2052a9cfd4b890612cb62a9c.html)). The pulse voltage limit setting is only applicable if the channel is set to the **NIDCPOWER_VAL_PULSE_CURRENT** output function using the [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) function.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| limit | [in] | ViReal64 | Specifies the pulse voltage limit, in volts, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.Valid Values: The valid values for this parameter are defined by the pulse voltage limit range that is configured using the niDCPower_ConfigurePulseVoltageLimitRange function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Pulse Current

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__pulse__current_1gad073fb22bd9a43c1bba3014b9c863c4d.html language=enus -->
## TOPIC 00077: niDCPower_ConfigurePulseBiasVoltageLimit

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__pulse__current_1gad073fb22bd9a43c1bba3014b9c863c4d.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__pulse__current_1gad073fb22bd9a43c1bba3014b9c863c4d.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse bias voltage limit for the specified channel(s). A channel must be enabled for the specified voltage limit to take effect. SyntaxViStatus _VI_FUNC niDCPower_ConfigurePulseBiasVoltageLimit(ViSession vi, ViConstString channelName, ViReal64 limit)RemarksRefer to the niDCPower_Confi

### niDCPower_ConfigurePulseBiasVoltageLimit

Configures the pulse bias voltage limit for the specified channel(s). A channel must be enabled for the specified voltage limit to take effect.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigurePulseBiasVoltageLimit(ViSession vi, ViConstString channelName, ViReal64 limit)

#### Remarks

Refer to the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function for more information about enabling the channel. The pulse bias voltage limit is the voltage that the output must not exceed when generating the desired pulse bias current level ([NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL](group____root__nidcpower__attributes__source__pulse__current_1ga1bca5d2788134bd7f75cf643a7bdf8f4.html)). The pulse bias voltage limit setting is only applicable if the channel is set to the **NIDCPOWER_VAL_PULSE_CURRENT** output function using the [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) function.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| limit | [in] | ViReal64 | Specifies the pulse bias voltage limit, in volts, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.Valid Values: The valid values for this parameter are defined by the pulse voltage limit range that is configured using the niDCPower_ConfigurePulseVoltageLimitRange function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Pulse Current

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__pulse__voltage_1ga1dae020d7f7b9ab684694c891124a3ac.html language=enus -->
## TOPIC 00078: niDCPower_ConfigurePulseVoltageLevel

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__pulse__voltage_1ga1dae020d7f7b9ab684694c891124a3ac.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__pulse__voltage_1ga1dae020d7f7b9ab684694c891124a3ac.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse voltage level that specified channel(s) attempt to generate during the on phase of a pulse. A channel must be enabled for the specified voltage level to take effect. SyntaxViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLevel(ViSession vi, ViConstString channelName, ViReal64 le

### niDCPower_ConfigurePulseVoltageLevel

Configures the pulse voltage level that specified channel(s) attempt to generate during the on phase of a pulse. A channel must be enabled for the specified voltage level to take effect.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLevel(ViSession vi, ViConstString channelName, ViReal64 level)

#### Remarks

Refer to the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function for more information about enabling the channel. The pulse voltage level setting is applicable only if the channel is set to the **NIDCPOWER_VAL_PULSE_VOLTAGE** output function using the [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) function.

Channels actively regulate the voltage at the specified level unless doing so causes a current greater than the pulse current limit ([NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT](group____root__nidcpower__attributes__source__pulse__voltage_1ga438453c31865f947120bdcee3b3e634f.html)) through the channels' output terminals.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| level | [in] | ViReal64 | Specifies the pulse voltage level, in volts, for the channel(s) generation.Valid Values: The valid values for this parameter are defined by the voltage level range that is selected using the niDCPower_ConfigurePulseVoltageLevelRange function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__pulse__voltage_1ga3f49d98df628d6f04513412d67152247.html language=enus -->
## TOPIC 00079: niDCPower_ConfigurePulseVoltageLevelRange

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__pulse__voltage_1ga3f49d98df628d6f04513412d67152247.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__pulse__voltage_1ga3f49d98df628d6f04513412d67152247.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse voltage level range for the specified channel(s). SyntaxViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLevelRange(ViSession vi, ViConstString channelName, ViReal64 range)RemarksThe configured range defines the valid values to which you can set the pulse voltage level and pulse

### niDCPower_ConfigurePulseVoltageLevelRange

Configures the pulse voltage level range for the specified channel(s).

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigurePulseVoltageLevelRange(ViSession vi, ViConstString channelName, ViReal64 range)

#### Remarks

The configured range defines the valid values to which you can set the pulse voltage level and pulse bias voltage level using the [niDCPower_ConfigurePulseVoltageLevel](group____root__nidcpower__functions__source__pulse__voltage_1ga1dae020d7f7b9ab684694c891124a3ac.html) and [niDCPower_ConfigurePulseBiasVoltageLevel](group____root__nidcpower__functions__source__pulse__voltage_1ga83723c9c6c77c7046b600e6284e72460.html) functions. The pulse voltage level range setting is applicable only if the channel is set to the **NIDCPOWER_VAL_PULSE_VOLTAGE** output function using the [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) function.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| range | [in] | ViReal64 | Specifies the pulse voltage level range, in volts, on the specified channel(s).For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__pulse__voltage_1ga5d1e4ae253391a872b88e2976a04ed9a.html language=enus -->
## TOPIC 00080: niDCPower_ConfigurePulseBiasCurrentLimit

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__pulse__voltage_1ga5d1e4ae253391a872b88e2976a04ed9a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__pulse__voltage_1ga5d1e4ae253391a872b88e2976a04ed9a.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse bias current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect. SyntaxViStatus _VI_FUNC niDCPower_ConfigurePulseBiasCurrentLimit(ViSession vi, ViConstString channelName, ViReal64 limit)RemarksRefer to the niDCPower_Confi

### niDCPower_ConfigurePulseBiasCurrentLimit

Configures the pulse bias current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigurePulseBiasCurrentLimit(ViSession vi, ViConstString channelName, ViReal64 limit)

#### Remarks

Refer to the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function for more information about enabling the channel. The pulse bias current limit is the current that the output must not exceed when generating the desired pulse bias voltage level ([NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL](group____root__nidcpower__attributes__source__pulse__voltage_1ga4da5413aa246be9248e744331a603f42.html)). The pulse bias current limit setting is only applicable if the channel is set to the **NIDCPOWER_VAL_PULSE_VOLTAGE** output function using the [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) function.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| limit | [in] | ViReal64 | Specifies the pulse bias current limit, in amps, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.Valid Values: The valid values for this parameter are defined by the pulse current limit range that is configured using the niDCPower_ConfigurePulseCurrentLimitRange function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__source__pulse__voltage_1ga9b6e2ec9dff9bc3f7707ff4245e391e5.html language=enus -->
## TOPIC 00081: niDCPower_ConfigurePulseCurrentLimit

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__source__pulse__voltage_1ga9b6e2ec9dff9bc3f7707ff4245e391e5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__source__pulse__voltage_1ga9b6e2ec9dff9bc3f7707ff4245e391e5.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect. SyntaxViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLimit(ViSession vi, ViConstString channelName, ViReal64 limit)RemarksRefer to the niDCPower_ConfigureOutpu

### niDCPower_ConfigurePulseCurrentLimit

Configures the pulse current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigurePulseCurrentLimit(ViSession vi, ViConstString channelName, ViReal64 limit)

#### Remarks

Refer to the [niDCPower_ConfigureOutputEnabled](group____root__nidcpower__functions__source_1ga85a7942a088e4a6ae4c286dd729f1dda.html) function for more information about enabling the channel. The pulse current limit is the current that the output must not exceed when generating the desired pulse voltage level ([NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL](group____root__nidcpower__attributes__source__pulse__voltage_1gaf679052e013d11b3484e1d029d1656c6.html)). The pulse current limit setting is only applicable if the channel is set to the **NIDCPOWER_VAL_PULSE_VOLTAGE** output function using the [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) function.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| limit | [in] | ViReal64 | Specifies the pulse current limit, in amps, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.Valid Values: The valid values for this parameter are defined by the pulse current limit range that is configured using the niDCPower_ConfigurePulseCurrentLimitRange function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__triggers__and__events_1gabbddd472907eb8e914874e0a42b8dc5c.html language=enus -->
## TOPIC 00082: niDCPower_ExportSignal

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__triggers__and__events_1gabbddd472907eb8e914874e0a42b8dc5c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__triggers__and__events_1gabbddd472907eb8e914874e0a42b8dc5c.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_ExportSignalWithChannels instead. SyntaxViStatus _VI_FUNC niDCPower_ExportSignal(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViConstString outputTerminal)RemarksRoutes signals (triggers and events) to the output terminal you specify. The r

### niDCPower_ExportSignal

This function is deprecated. Use [niDCPower_ExportSignalWithChannels](group____root__nidcpower__functions__triggers__and__events_1gad51bd44ef73428bd7eef439c7403b32b.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_ExportSignal(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViConstString outputTerminal)

#### Remarks

Routes signals (triggers and events) to the output terminal you specify. The route is created when the session is committed ([niDCPower_CommitWithChannels](group____root__nidcpower__functions__control_1ga21679973682c594d89918cc3d6bb40f2.html)).

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| signal | [in] | ViInt32 | Specifies which trigger or event to export.Defined Values:NameValueDescriptionNIDCPOWER_VAL_SOURCE_COMPLETE_EVENT1030 (0x406)The Source Complete event.NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT1031 (0x407)The Measure Complete event.NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT1032 (0x408)The Sequence Iteration Complete event.NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT1033 (0x409)The Sequence Engine Done event.NIDCPOWER_VAL_PULSE_COMPLETE_EVENT1051 (0x41b)The Pulse Complete event.NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT1052 (0x41c)The Ready Pulse Trigger event.NIDCPOWER_VAL_START_TRIGGER1034 (0x40a)The Start trigger.NIDCPOWER_VAL_SOURCE_TRIGGER1035 (0x40b)The Source trigger.NIDCPOWER_VAL_MEASURE_TRIGGER1036 (0x40c)The Measure trigger.NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER1037 (0x40d)The Sequence Advance trigger.NIDCPOWER_VAL_PULSE_TRIGGER1053 (0x41d)The Pulse trigger.NIDCPOWER_VAL_SHUTDOWN_TRIGGER1118 (0x45e)The Shutdown trigger. |
| Name | Value | Description |  |
| NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT | 1030 (0x406) | The Source Complete event. |  |
| NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT | 1031 (0x407) | The Measure Complete event. |  |
| NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT | 1032 (0x408) | The Sequence Iteration Complete event. |  |
| NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT | 1033 (0x409) | The Sequence Engine Done event. |  |
| NIDCPOWER_VAL_PULSE_COMPLETE_EVENT | 1051 (0x41b) | The Pulse Complete event. |  |
| NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT | 1052 (0x41c) | The Ready Pulse Trigger event. |  |
| NIDCPOWER_VAL_START_TRIGGER | 1034 (0x40a) | The Start trigger. |  |
| NIDCPOWER_VAL_SOURCE_TRIGGER | 1035 (0x40b) | The Source trigger. |  |
| NIDCPOWER_VAL_MEASURE_TRIGGER | 1036 (0x40c) | The Measure trigger. |  |
| NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER | 1037 (0x40d) | The Sequence Advance trigger. |  |
| NIDCPOWER_VAL_PULSE_TRIGGER | 1053 (0x41d) | The Pulse trigger. |  |
| NIDCPOWER_VAL_SHUTDOWN_TRIGGER | 1118 (0x45e) | The Shutdown trigger. |  |
| signalIdentifier | [in] | ViConstString | Reserved for future use. Pass in an empty string for this parameter. |
| outputTerminal | [in] | ViConstString | Specifies where to export the selected signal.Relative Terminals:""Do not export signal"PXI_Trig0"PXI trigger line 0"PXI_Trig1"PXI trigger line 1"PXI_Trig2"PXI trigger line 2"PXI_Trig3"PXI trigger line 3"PXI_Trig4"PXI trigger line 4"PXI_Trig5"PXI trigger line 5"PXI_Trig6"PXI trigger line 6"PXI_Trig7"PXI trigger line 7 |
|  |  |  |  |
| "" | Do not export signal |  |  |
| "PXI_Trig0" | PXI trigger line 0 |  |  |
| "PXI_Trig1" | PXI trigger line 1 |  |  |
| "PXI_Trig2" | PXI trigger line 2 |  |  |
| "PXI_Trig3" | PXI trigger line 3 |  |  |
| "PXI_Trig4" | PXI trigger line 4 |  |  |
| "PXI_Trig5" | PXI trigger line 5 |  |  |
| "PXI_Trig6" | PXI trigger line 6 |  |  |
| "PXI_Trig7" | PXI trigger line 7 |  |  |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Triggers and Events

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga058b5793d8612abdd57067cc2e9582d6.html language=enus -->
## TOPIC 00083: niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga058b5793d8612abdd57067cc2e9582d6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga058b5793d8612abdd57067cc2e9582d6.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for digital edge triggering. SyntaxViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels(ViSession vi, ViConstString channelName, ViConstString inputTerminal, ViInt32 edge)RemarksThis function is not supported on all devices. Refer to Supported Functio

### niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels

Configures the Start trigger for digital edge triggering.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels(ViSession vi, ViConstString channelName, ViConstString inputTerminal, ViInt32 edge)

#### Remarks

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| inputTerminal | [in] | ViConstString | Specifies the input terminal for the digital edge Start trigger.You can specify any valid input terminal for this function. Valid terminals are listed in MAX under the Device Routes tab. For the PXIe-4147 and PXIe-4162/4163, refer to the Signal Routing topic for the device to determine which routes are available. This information is not available on a Device Routes tab in MAX.Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0. |
| edge | [in] | ViInt32 | Specifies whether to configure the Start trigger to assert on the rising or falling edge.Defined Values:NameValueDescriptionNIDCPOWER_VAL_RISING1016 (0x3f8)Asserts the trigger on the rising edge of the digital signal.NIDCPOWER_VAL_FALLING1017 (0x3f9)Asserts the trigger on the falling edge of the digital signal. |
| Name | Value | Description |  |
| NIDCPOWER_VAL_RISING | 1016 (0x3f8) | Asserts the trigger on the rising edge of the digital signal. |  |
| NIDCPOWER_VAL_FALLING | 1017 (0x3f9) | Asserts the trigger on the falling edge of the digital signal. |  |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Start Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga1b718b6d06145f9ff2ad77aee98e7a93.html language=enus -->
## TOPIC 00084: niDCPower_DisableStartTrigger

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga1b718b6d06145f9ff2ad77aee98e7a93.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga1b718b6d06145f9ff2ad77aee98e7a93.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_DisableStartTriggerWithChannels instead. SyntaxViStatus _VI_FUNC niDCPower_DisableStartTrigger(ViSession vi)RemarksDisables the Start trigger. The device does not wait for a Start trigger when starting generation or acquisition.This function is not supporte

### niDCPower_DisableStartTrigger

This function is deprecated. Use [niDCPower_DisableStartTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga68fa4069dd3fcbb9dff83649954e0f99.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_DisableStartTrigger(ViSession vi)

#### Remarks

Disables the Start trigger. The device does not wait for a Start trigger when starting generation or acquisition.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Start Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga30117ffc531b1ebd5a87b7f96ff86958.html language=enus -->
## TOPIC 00085: niDCPower_ConfigureDigitalEdgeStartTrigger

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga30117ffc531b1ebd5a87b7f96ff86958.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga30117ffc531b1ebd5a87b7f96ff86958.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels instead. SyntaxViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeStartTrigger(ViSession vi, ViConstString inputTerminal, ViInt32 edge)RemarksConfigures the Start trigger for digital edge triggering.This function is

### niDCPower_ConfigureDigitalEdgeStartTrigger

This function is deprecated. Use [niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels](group____root__nidcpower__functions__triggers__and__events__start__trigger_1ga058b5793d8612abdd57067cc2e9582d6.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureDigitalEdgeStartTrigger(ViSession vi, ViConstString inputTerminal, ViInt32 edge)

#### Remarks

Configures the Start trigger for digital edge triggering.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| inputTerminal | [in] | ViConstString | Specifies the input terminal for the digital edge Start trigger.You can specify any valid input terminal for this function. Valid terminals are listed in MAX under the Device Routes tab. For the PXIe-4147 and PXIe-4162/4163, refer to the Signal Routing topic for the device to determine which routes are available. This information is not available on a Device Routes tab in MAX.Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent. |
| edge | [in] | ViInt32 | Specifies whether to configure the Start trigger to assert on the rising or falling edge.Defined Values:NameValueDescriptionNIDCPOWER_VAL_RISING1016 (0x3f8)Asserts the trigger on the rising edge of the digital signal.NIDCPOWER_VAL_FALLING1017 (0x3f9)Asserts the trigger on the falling edge of the digital signal. |
| Name | Value | Description |  |
| NIDCPOWER_VAL_RISING | 1016 (0x3f8) | Asserts the trigger on the rising edge of the digital signal. |  |
| NIDCPOWER_VAL_FALLING | 1017 (0x3f9) | Asserts the trigger on the falling edge of the digital signal. |  |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Start Trigger

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html language=enus -->
## TOPIC 00086: niDCPower_ResetWithChannels

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the specified channel(s) to a known state. This function disables power generation, resets channel attributes to their default values, commits the channel attributes, and leaves the channel(s) in the Uncommitted state. SyntaxViStatus _VI_FUNC niDCPower_ResetWithChannels(ViSession vi, ViConstS

### niDCPower_ResetWithChannels

Resets the specified channel(s) to a known state. This function disables power generation, resets channel attributes to their default values, commits the channel attributes, and leaves the channel(s) in the Uncommitted state.

#### Syntax

ViStatus _VI_FUNC niDCPower_ResetWithChannels(ViSession vi, ViConstString channelName)

#### Remarks

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility_1ga080148572da25eda05ff1b8b5d4ba2c8.html language=enus -->
## TOPIC 00087: niDCPower_self_test

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility_1ga080148572da25eda05ff1b8b5d4ba2c8.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility_1ga080148572da25eda05ff1b8b5d4ba2c8.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the device self-test routine and returns the test result(s). Calling this function implicitly calls the niDCPower_ResetWithChannels function. SyntaxViStatus _VI_FUNC niDCPower_self_test(ViSession vi, ViInt16 *selfTestResult, ViChar selfTestMessage[IVI_MAX_MESSAGE_BUF_SIZE])RemarksWhen calli

### niDCPower_self_test

Performs the device self-test routine and returns the test result(s). Calling this function implicitly calls the [niDCPower_ResetWithChannels](group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html) function.

#### Syntax

ViStatus _VI_FUNC niDCPower_self_test(ViSession vi, ViInt16 *selfTestResult, ViChar selfTestMessage[IVI_MAX_MESSAGE_BUF_SIZE])

#### Remarks

When calling this function with the PXIe-4162/4163, specify all channels of your PXIe-4162/4163 with the **resourceName** input of the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function. You cannot self test a subset of PXIe-4162/4163 channels.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| selfTestResult | [out] | ViInt16 * | Returns the value result from the device self-test.Self-Test CodeDescription0Self test passed.1Self test failed. |
| Self-Test Code | Description |  |  |
| 0 | Self test passed. |  |  |
| 1 | Self test failed. |  |  |
| selfTestMessage | [out] | ViChar[IVI_MAX_MESSAGE_BUF_SIZE] | Returns the self-test result message. The size of this array must be at least 256 bytes. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility_1ga68f797ce1239f36c5f47e108e1cbe305.html language=enus -->
## TOPIC 00088: niDCPower_Disable

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility_1ga68f797ce1239f36c5f47e108e1cbe305.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility_1ga68f797ce1239f36c5f47e108e1cbe305.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function performs the same actions as the niDCPower_ResetWithChannels function, except that this function also immediately sets the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute to VI_FALSE. SyntaxViStatus _VI_FUNC niDCPower_Disable(ViSession vi)RemarksThis function opens the output relay on instrume

### niDCPower_Disable

This function performs the same actions as the [niDCPower_ResetWithChannels](group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html) function, except that this function also immediately sets the [NIDCPOWER_ATTR_OUTPUT_ENABLED](group____root__nidcpower__attributes__source_1ga131827bee1cb8985b2f7e8e52d35a810.html) attribute to VI_FALSE.

#### Syntax

ViStatus _VI_FUNC niDCPower_Disable(ViSession vi)

#### Remarks

This function opens the output relay on instruments that have an output relay.

This function applies to all channels and instruments in the session.

Note

NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility_1ga9bc5fab751a72d72667b9716b4c3c7bd.html language=enus -->
## TOPIC 00089: niDCPower_reset

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility_1ga9bc5fab751a72d72667b9716b4c3c7bd.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility_1ga9bc5fab751a72d72667b9716b4c3c7bd.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_ResetWithChannels instead. SyntaxViStatus _VI_FUNC niDCPower_reset(ViSession vi)RemarksResets the device to a known state. This function disables power generation, resets session attributes to their default values, commits the session attributes, and leaves

### niDCPower_reset

This function is deprecated. Use [niDCPower_ResetWithChannels](group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_reset(ViSession vi)

#### Remarks

Resets the device to a known state. This function disables power generation, resets session attributes to their default values, commits the session attributes, and leaves the session in the Uncommitted state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic for more information about NI-DCPower software states.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga6fce6fcb730854b3e516a64274d8d1ac.html language=enus -->
## TOPIC 00090: niDCPower_ImportAttributeConfigurationBuffer

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga6fce6fcb730854b3e516a64274d8d1ac.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga6fce6fcb730854b3e516a64274d8d1ac.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from the specified buffer. SyntaxViStatus _VI_FUNC niDCPower_ImportAttributeConfigurationBuffer(ViSession vi, ViInt32 size, ViAddr configuration)RemarksYou can export and import supported configurations only between NI-DCPower devices with identical model numbe

### niDCPower_ImportAttributeConfigurationBuffer

Imports a configuration to the session from the specified buffer.

#### Syntax

ViStatus _VI_FUNC niDCPower_ImportAttributeConfigurationBuffer(ViSession vi, ViInt32 size, ViAddr configuration)

#### Remarks

You can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same number of configured channels.

Note

You cannot call this function while any channel is in the [Running](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) state.

**Supported Configurations**

You can export and import the following configurations between NI-DCPower sessions:

- Attribute configurations
- Advanced sequences

**Support for this Function**

You must set the source mode to **NIDCPOWER_VAL_SEQUENCE** in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function cannot be imported into sessions created with deprecated initialize functions.

Note

Exporting and importing simple sequences in Sequence source mode is unsupported.

**Channel Mapping Behavior**

When importing and exporting session attribute configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resourceName** input to the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

**Related Topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[Using Properties and Attributes](/csh?context=nidcpower_ni_dc_power_supplies_help_using_properties_and_attributes)

[Setting Properties and Attributes Before Reading Them](/csh?context=nidcpower_ni_dc_power_supplies_help_setting_before_reading_attributes)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| size | [in] | ViInt32 | Specifies the size, in bytes, of the byte array to import. If you enter 0, this function returns the needed size. |
| configuration | [in] | ViAddr | Specifies the byte array buffer that contains the attribute configuration to import. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Import/Export Attribute Configuration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga78ed0fe8739587fa2ddc9dae62c249aa.html language=enus -->
## TOPIC 00091: niDCPower_ExportAttributeConfigurationFile

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga78ed0fe8739587fa2ddc9dae62c249aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga78ed0fe8739587fa2ddc9dae62c249aa.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to the specified file. SyntaxViStatus _VI_FUNC niDCPower_ExportAttributeConfigurationFile(ViSession vi, ViConstString filePath)RemarksYou can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same number of

### niDCPower_ExportAttributeConfigurationFile

Exports a session configuration to the specified file.

#### Syntax

ViStatus _VI_FUNC niDCPower_ExportAttributeConfigurationFile(ViSession vi, ViConstString filePath)

#### Remarks

You can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same number of configured channels.

This function verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI-DCPower returns an error.

**Supported Configurations**

You can export and import the following configurations between NI-DCPower sessions:

- Attribute configurations
- Advanced sequences

**Support for this Function**

You must set the source mode to **NIDCPOWER_VAL_SEQUENCE** in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function cannot be imported into sessions created with deprecated initialize functions.

Note

Exporting and importing simple sequences in Sequence source mode is unsupported.

**Channel Mapping Behavior**

When importing and exporting session attribute configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resourceName** input to the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

**Related Topics:**

[Using Properties and Attributes](/csh?context=nidcpower_ni_dc_power_supplies_help_using_properties_and_attributes)

[Setting Properties and Attributes Before Reading Them](/csh?context=nidcpower_ni_dc_power_supplies_help_setting_before_reading_attributes)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| filePath | [in] | ViConstString | The absolute path to a placeholder file you must create to contain the configuration you want to export. If you specify an empty or relative path, this function returns an error.Default file extension: .nidcpowerconfig |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Import/Export Attribute Configuration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga93666c3600572c0d480fe38b0932f622.html language=enus -->
## TOPIC 00092: niDCPower_ImportAttributeConfigurationFile

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga93666c3600572c0d480fe38b0932f622.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__importexport__attribute__configuration_1ga93666c3600572c0d480fe38b0932f622.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from the specified file. SyntaxViStatus _VI_FUNC niDCPower_ImportAttributeConfigurationFile(ViSession vi, ViConstString filePath)RemarksYou can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same

### niDCPower_ImportAttributeConfigurationFile

Imports a configuration to the session from the specified file.

#### Syntax

ViStatus _VI_FUNC niDCPower_ImportAttributeConfigurationFile(ViSession vi, ViConstString filePath)

#### Remarks

You can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same number of configured channels.

Note

You cannot call this function while any channel is in the [Running](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) state.

**Supported Configurations**

You can export and import the following configurations between NI-DCPower sessions:

- Attribute configurations
- Advanced sequences

**Support for this Function**

You must set the session source mode to **NIDCPOWER_VAL_SEQUENCE** in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function cannot be imported into sessions created with deprecated initialize functions.

Note

Exporting and importing simple sequences in Sequence source mode is unsupported.

**Channel Mapping Behavior**

When importing and exporting session attribute configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resourceName** input to the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

**Related Topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[Using Properties and Attributes](/csh?context=nidcpower_ni_dc_power_supplies_help_using_properties_and_attributes)

[Setting Properties and Attributes Before Reading Them](/csh?context=nidcpower_ni_dc_power_supplies_help_setting_before_reading_attributes)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| filePath | [in] | ViConstString | The absolute path to the file that contains the configuration to import. If you specify an empty or relative path, this function returns an error.Default File Extension: .nidcpowerconfig |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Import/Export Attribute Configuration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__importexport__attribute__configuration_1gab1f3d2c9e748d73ef8ab3a7887b7d3c4.html language=enus -->
## TOPIC 00093: niDCPower_ExportAttributeConfigurationBuffer

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__importexport__attribute__configuration_1gab1f3d2c9e748d73ef8ab3a7887b7d3c4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__importexport__attribute__configuration_1gab1f3d2c9e748d73ef8ab3a7887b7d3c4.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to a buffer. SyntaxViStatus _VI_FUNC niDCPower_ExportAttributeConfigurationBuffer(ViSession vi, ViInt32 size, ViAddr configuration)RemarksYou can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same numbe

### niDCPower_ExportAttributeConfigurationBuffer

Exports a session configuration to a buffer.

#### Syntax

ViStatus _VI_FUNC niDCPower_ExportAttributeConfigurationBuffer(ViSession vi, ViInt32 size, ViAddr configuration)

#### Remarks

You can export and import supported configurations only between NI-DCPower devices with identical model numbers and the same number of configured channels.

This function verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI-DCPower returns an error.

**Supported Configurations**

You can export and import the following configurations between NI-DCPower sessions:

- Attribute configurations
- Advanced sequences

**Support for this Function**

You must set the source mode to **NIDCPOWER_VAL_SEQUENCE** in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function cannot be imported into sessions created with deprecated initialize functions.

Note

Exporting and importing simple sequences in Sequence source mode is unsupported.

**Channel Mapping Behavior**

When importing and exporting session attribute configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resourceName** input to the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

**Related Topics:**

[Using Properties and Attributes](/csh?context=nidcpower_ni_dc_power_supplies_help_using_properties_and_attributes)

[Setting Properties and Attributes Before Reading Them](/csh?context=nidcpower_ni_dc_power_supplies_help_setting_before_reading_attributes)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| size | [in] | ViInt32 | Specifies the size, in bytes, of the byte array to export. If you enter 0, this function returns the needed size. |
| configuration | [out] | ViAddr | Specifies the byte array buffer to be populated with the exported attribute configuration. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Import/Export Attribute Configuration

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__ivi__functions.html language=enus -->
## TOPIC 00094: IVI Functions

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__ivi__functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__ivi__functions.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDCPower_ClearInterchangeWarningsClears the list of current interchange warnings. niDCPower_ConfigureOVPThis function configures the power supply's overvoltage protection. You specify the overvoltage limit and the behavior of the power supply when the output vo

### IVI Functions

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDCPower_ClearInterchangeWarnings | Clears the list of current interchange warnings. |
| niDCPower_ConfigureOVP | This function configures the power supply's overvoltage protection. You specify the overvoltage limit and the behavior of the power supply when the output voltage is greater than or equal to that value. |
| niDCPower_GetChannelName | Returns channel name(s) from a one-based index. Use the NIDCPOWER_ATTR_CHANNEL_COUNT attribute to determine the upper bound of valid values for index. |
| niDCPower_GetChannelNameFromString | Returns a comma-separated list of channel names from a string index list. |
| niDCPower_GetNextCoercionRecord | Returns the coercion information associated with the IVI session and clears the earliest instance in which NI-DCPower coerced a value you specified. |
| niDCPower_GetNextInterchangeWarning | This function returns the interchangeability warning associated with the IVI session. It retrieves and clears the earliest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different device may cause a different behavior. |
| niDCPower_InvalidateAllAttributes | Invalidates the cached values of all attributes for the session. |
| niDCPower_ResetInterchangeCheck | When developing a complex test system that consists of multiple test modules, it is generally a good idea to design the test modules so that they can run in any order. To do so requires ensuring that each test module completely configures the state of each instrument it uses. If a particular test module does not completely configure the state of an instrument, the state of the instrument depends on the configuration from a previously executed test module. If you execute the test modules in a different order, the behavior of the instrument and therefore the entire test module is likely to change. This change in behavior is generally instrument specific and represents an interchangeability problem. |
| niDCPower_ResetWithDefaults | Resets all channels in the session to a known state. This function disables power generation, resets session attributes to their default values, commits the session attributes, and leaves the session in the Running state. In addition to exhibiting the behavior of the niDCPower_ResetWithChannels function, this function can assign user-defined default values for configurable attributes from the IVI configuration. |
| niDCPower_revision_query | Returns the revision information of NI-DCPower and the device firmware. |

#### Attachments

None

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__ivi__functions_1ga0abf54af886f3c02ff8e9292af6f1176.html language=enus -->
## TOPIC 00095: niDCPower_ResetWithDefaults

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__ivi__functions_1ga0abf54af886f3c02ff8e9292af6f1176.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__ivi__functions_1ga0abf54af886f3c02ff8e9292af6f1176.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all channels in the session to a known state. This function disables power generation, resets session attributes to their default values, commits the session attributes, and leaves the session in the Running state. In addition to exhibiting the behavior of the niDCPower_ResetWithChannels func

### niDCPower_ResetWithDefaults

Resets all channels in the session to a known state. This function disables power generation, resets session attributes to their default values, commits the session attributes, and leaves the session in the [Running](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) state. In addition to exhibiting the behavior of the [niDCPower_ResetWithChannels](group____root__nidcpower__functions__utility_1ga0388a6f4d53eb41f89753be0fa929c42.html) function, this function can assign user-defined default values for configurable attributes from the IVI configuration.

#### Syntax

ViStatus _VI_FUNC niDCPower_ResetWithDefaults(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IVI Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__ivi__functions_1ga2d7dde812101210fbeb59239ca98357a.html language=enus -->
## TOPIC 00096: niDCPower_GetChannelNameFromString

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__ivi__functions_1ga2d7dde812101210fbeb59239ca98357a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__ivi__functions_1ga2d7dde812101210fbeb59239ca98357a.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-separated list of channel names from a string index list. SyntaxViStatus _VI_FUNC niDCPower_GetChannelNameFromString(ViSession vi, ViConstString index, ViInt32 bufferSize, ViChar channelName[])RemarksUse this function to identify the fully qualified names of channels. Fully qualified

### niDCPower_GetChannelNameFromString

Returns a comma-separated list of channel names from a string index list.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetChannelNameFromString(ViSession vi, ViConstString index, ViInt32 bufferSize, ViChar channelName[])

#### Remarks

Use this function to identify the fully qualified names of channels. Fully qualified channel names are required to access channels in multi-instrument sessions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| index | [in] | ViConstString | Specifies an index list for the channels in the session.Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:A comma-separated list - for example, "0,2,3,1"A range using a hyphen - for example, "0-3"A range using a colon - for example, "0:3"You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing. |
| bufferSize | [in] | ViInt32 | Specifies the number of bytes in the ViChar array you specify for channelName. If the channelName, including the terminating NUL byte, contains more bytes than you indicate in this attribute, the function copies (buffer size - 1) bytes into the buffer, places an ASCII NUL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is 123456 and the buffer size is 4, the function places 123 into the buffer and returns 7.If you pass 0, you can pass VI_NULL for channelName. |
| channelName | [out] | ViChar[] | Returns a string of the channel name(s). |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IVI Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__ivi__functions_1ga4aca7ede82dabe07017db59573dc95d9.html language=enus -->
## TOPIC 00097: niDCPower_ClearInterchangeWarnings

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__ivi__functions_1ga4aca7ede82dabe07017db59573dc95d9.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__ivi__functions_1ga4aca7ede82dabe07017db59573dc95d9.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of current interchange warnings. SyntaxViStatus _VI_FUNC niDCPower_ClearInterchangeWarnings(ViSession vi)ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. Retu

### niDCPower_ClearInterchangeWarnings

Clears the list of current interchange warnings.

#### Syntax

ViStatus _VI_FUNC niDCPower_ClearInterchangeWarnings(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IVI Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__ivi__functions_1gac9147be9a38235f87e2aacc7e7db0214.html language=enus -->
## TOPIC 00098: niDCPower_ConfigureOVP

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__ivi__functions_1gac9147be9a38235f87e2aacc7e7db0214.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__ivi__functions_1gac9147be9a38235f87e2aacc7e7db0214.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function configures the power supply's overvoltage protection. You specify the overvoltage limit and the behavior of the power supply when the output voltage is greater than or equal to that value. SyntaxViStatus _VI_FUNC niDCPower_ConfigureOVP(ViSession vi, ViConstString channelName, ViBoolean

### niDCPower_ConfigureOVP

This function configures the power supply's overvoltage protection. You specify the overvoltage limit and the behavior of the power supply when the output voltage is greater than or equal to that value.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureOVP(ViSession vi, ViConstString channelName, ViBoolean enabled, ViReal64 limit)

#### Remarks

When the **enabled** parameter is FALSE, the **limit** parameter does not affect the instrument's behavior, and the driver ignores the **limit** parameter.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| enabled | [in] | ViBoolean | Pass whether you want to enable or disable the OVP limit. The driver uses this value to set the NIDCPOWER_ATTR_OVP_ENABLED attribute. Refer to the attribute documentation for more information. |
| limit | [in] | ViReal64 | Pass the overvoltage protection limit you want to use. The driver uses this value to set the NIDCPOWER_ATTR_OVP_LIMIT attribute. Refer to the attribute documentation for more information. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IVI Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__ivi__functions_1gad76f3be730867da879dc6da129640038.html language=enus -->
## TOPIC 00099: niDCPower_GetNextCoercionRecord

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__ivi__functions_1gad76f3be730867da879dc6da129640038.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__ivi__functions_1gad76f3be730867da879dc6da129640038.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the coercion information associated with the IVI session and clears the earliest instance in which NI-DCPower coerced a value you specified. SyntaxViStatus _VI_FUNC niDCPower_GetNextCoercionRecord(ViSession vi, ViInt32 bufferSize, ViChar coercionRecord[])ParametersNameDirectionTypeDescriptio

### niDCPower_GetNextCoercionRecord

Returns the coercion information associated with the IVI session and clears the earliest instance in which NI-DCPower coerced a value you specified.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetNextCoercionRecord(ViSession vi, ViInt32 bufferSize, ViChar coercionRecord[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| bufferSize | [in] | ViInt32 | Specifies the number of bytes in the ViChar array you specify for coercionRecord. If the next coercion record string, including the terminating NUL byte, contains more bytes than you indicate in this attribute, the function copies (buffer size - 1) bytes into the buffer, places an ASCII NUL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is 123456 and the buffer size is 4, the function places 123 into the buffer and returns 7.If you pass 0, you can pass VI_NULL for coercionRecord. |
| coercionRecord | [out] | ViChar[] | Returns the next coercionRecord for the IVI session. If there are no coercionRecords, the function returns an empty string. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

IVI Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__locking.html language=enus -->
## TOPIC 00100: Locking

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__locking.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__locking.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDCPower_LockSessionObtains a multithread lock on the device session. Before doing so, the software waits until all other execution threads release their locks on the device session. niDCPower_UnlockSessionReleases a lock that you acquired on an device session

### Locking

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDCPower_LockSession | Obtains a multithread lock on the device session. Before doing so, the software waits until all other execution threads release their locks on the device session. |
| niDCPower_UnlockSession | Releases a lock that you acquired on an device session using niDCPower_LockSession. Refer to niDCPower_LockSession for additional information on session locks. |

#### Attachments

None

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html language=enus -->
## TOPIC 00101: niDCPower_UnlockSession

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases a lock that you acquired on an device session using niDCPower_LockSession. Refer to niDCPower_LockSession for additional information on session locks. SyntaxViStatus _VI_FUNC niDCPower_UnlockSession(ViSession vi, ViBoolean *callerHasLock)ParametersNameDirectionTypeDescriptionvi[in]ViSession

### niDCPower_UnlockSession

Releases a lock that you acquired on an device session using [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html). Refer to [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) for additional information on session locks.

#### Syntax

ViStatus _VI_FUNC niDCPower_UnlockSession(ViSession vi, ViBoolean *callerHasLock)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| callerHasLock | [out] | ViBoolean * | This attribute is optional. If you do not want to use this attribute, pass VI_NULL.Use this attribute in complex functions to keep track of whether you obtain a lock and therefore need to unlock the session.Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to niDCPower_LockSession or niDCPower_UnlockSession in the same function.The parameter is an input/output parameter. niDCPower_LockSession and niDCPower_UnlockSession each inspect the current value and take the following actions.If the value is VI_TRUE, niDCPower_LockSession does not lock the session again.If the value is VI_FALSE, niDCPower_LockSession obtains the lock and sets the value of the parameter to VI_TRUE.If the value is VI_FALSE, niDCPower_UnlockSession does not attempt to unlock the session.If the value is VI_TRUE, niDCPower_UnlockSession releases the lock and sets the value of the parameter to VI_FALSE.Thus, you can, call niDCPower_UnlockSession at the end of your function without worrying about whether you actually have the lock, as the following example shows.ViStatus TestFunc (ViSession vi, ViInt32 flags){ ViStatus error = VI_SUCCESS; ViBoolean haveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr( niDCPower_LockSession(vi, &haveLock)); viCheckErr( TakeAction1(vi)); if (flags & BIT_2) { viCheckErr( niDCPower_UnlockSession(vi, &haveLock)); viCheckErr( TakeAction2(vi)); viCheckErr( niDCPower_LockSession(vi, &haveLock); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); } Error: /*At this point, you cannot really be sure that you have the lock. Fortunately, the haveLock variable takes care of that for you.*/ niDCPower_UnlockSession(vi, &haveLock); return error;} |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Locking

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html language=enus -->
## TOPIC 00102: niDCPower_LockSession

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a multithread lock on the device session. Before doing so, the software waits until all other execution threads release their locks on the device session. SyntaxViStatus _VI_FUNC niDCPower_LockSession(ViSession vi, ViBoolean *callerHasLock)RemarksOther threads may have obtained a lock on thi

### niDCPower_LockSession

Obtains a multithread lock on the device session. Before doing so, the software waits until all other execution threads release their locks on the device session.

#### Syntax

ViStatus _VI_FUNC niDCPower_LockSession(ViSession vi, ViBoolean *callerHasLock)

#### Remarks

Other threads may have obtained a lock on this session for the following reasons:

- The application called the [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) function.
- A call to NI-DCPower locked the session.
- A call to the IVI engine locked the session.
- After a call to the [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) function returns successfully, no other threads can access the device session until you call the [niDCPower_UnlockSession](group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html) function.
- Use the [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) function and the [niDCPower_UnlockSession](group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html) function around a sequence of calls to instrument driver functions if you require that the device retain its settings through the end of the sequence.

You can safely make nested calls to the [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) function within the same thread. To completely unlock the session, you must balance each call to the [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) function with a call to the [niDCPower_UnlockSession](group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html) function. If, however, you use **Caller_Has_Lock** in all calls to the [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) and [niDCPower_UnlockSession](group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html) function within a function, the IVI Library locks the session only once within the function regardless of the number of calls you make to the [niDCPower_LockSession](group____root__nidcpower__functions__utility__locking_1ga8a012e0aeaec1feb01d4d2038188fb81.html) function. This behavior allows you to call the [niDCPower_UnlockSession](group____root__nidcpower__functions__utility__locking_1ga273af81d8e9e4a334245dcc674ddbe49.html) function just once at the end of the function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| callerHasLock | [out] | ViBoolean * | This parameter is optional. If you do not want to use this parameter, pass VI_NULL.Use this parameter in complex functions to keep track of whether you obtain a lock and therefore need to unlock the session. Pass the address of a local ViBoolean variable. In the declaration of the local variable, initialize it to VI_FALSE. Pass the address of the same local variable to any other calls you make to the niDCPower_LockSession function or the niDCPower_UnlockSession function in the same function.The parameter is an input/output parameter. The niDCPower_LockSession and niDCPower_UnlockSession functions each inspect the current value and take the following actions.If the value is VI_TRUE, the niDCPower_LockSession function does not lock the session again.If the value is VI_FALSE, the niDCPower_LockSession function obtains the lock and sets the value of the parameter to VI_TRUE.If the value is VI_FALSE, the niDCPower_UnlockSession function does not attempt to unlock the session.If the value is VI_TRUE, the niDCPower_UnlockSession function releases the lock and sets the value of the parameter to VI_FALSE.Thus, you can, call the niDCPower_UnlockSession function at the end of your function without worrying about whether you actually have the lock, as shown in the following example.ViStatus TestFunc (ViSession vi, ViInt32 flags){ ViStatus error = VI_SUCCESS; ViBoolean haveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr( niDCPower_LockSession(vi, &haveLock)); viCheckErr( TakeAction1(vi)); if (flags & BIT_2) { viCheckErr( niDCPower_UnlockSession(vi, &haveLock)); viCheckErr( TakeAction2(vi)); viCheckErr( niDCPower_LockSession(vi, &haveLock); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); } Error: /*At this point, you cannot really be sure that you have the lock. Fortunately, the haveLock variable takes care of that for you.*/ niDCPower_UnlockSession(vi, &haveLock); return error;} |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Locking

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device.html language=enus -->
## TOPIC 00103: Supported Attributes by Device

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following topics for information about attribute support and default values.Attributes Supported by the PXIe-4051Attributes Supported by the PXI-4110Attributes Supported by the PXIe-4112/4113Attributes Supported by the PXI-4130Attributes Supported by the PXI-4132Attributes Supported by

### Supported Attributes by Device

Refer to the following topics for information about attribute support and default values.

- [Attributes Supported by the PXIe-4051](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4051)
- [Attributes Supported by the PXI-4110](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4110)
- [Attributes Supported by the PXIe-4112/4113](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4112_4113)
- [Attributes Supported by the PXI-4130](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4130)
- [Attributes Supported by the PXI-4132](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4132)
- [Attributes Supported by the PXIe-4135](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4135)
- [Attributes Supported by the PXIe-4136/4137](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4136_4137)
- [Attributes Supported by the PXIe-4138/4139](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4138_4139)
- [Attributes Supported by the PXIe-4140/4141](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4140_4141)
- [Attributes Supported by the PXIe-4142/4143](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4142_4143)
- [Attributes Supported by the PXIe-4144/4145](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4144_4145)
- [Attributes Supported by the PXIe-4147](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4147)
- [Attributes Supported by the PXIe-4150/4151](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4150_4151)
- [Attributes Supported by the PXIe-4154](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4154)
- [Attributes Supported by the PXIe-4162/4163](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4162_4163)
- [Attributes Supported by the PXIe-4190](/csh?context=nidcpower_nidcpowercref_pages_supported_attributes_4190)

#### Groups

None

#### Group members

None

#### Attachments

| Name | Description |
| --- | --- |
| Attributes Supported by the PXI-4110 |  |
| Attributes Supported by the PXI-4130 |  |
| Attributes Supported by the PXI-4132 |  |
| Attributes Supported by the PXIe-4051 |  |
| Attributes Supported by the PXIe-4112/4113 |  |
| Attributes Supported by the PXIe-4135 |  |
| Attributes Supported by the PXIe-4136/4137 |  |
| Attributes Supported by the PXIe-4138/4139 |  |
| Attributes Supported by the PXIe-4140/4141 |  |
| Attributes Supported by the PXIe-4142/4143 |  |
| Attributes Supported by the PXIe-4144/4145 |  |
| Attributes Supported by the PXIe-4147 |  |
| Attributes Supported by the PXIe-4150/4151 |  |
| Attributes Supported by the PXIe-4154 |  |
| Attributes Supported by the PXIe-4162/4163 |  |
| Attributes Supported by the PXIe-4190 |  |

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4051.html language=enus -->
## TOPIC 00104: Attributes Supported by the PXIe-4051

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4051.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4051.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4051

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4051 |
| --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | NIDCPOWER_VAL_OFF2 |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF2 |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | X |
| NIDCPOWER_ATTR_CABLE_LENGTH | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC2 |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | NIDCPOWER_VAL_CONDUCTION_VOLTAGE_MODE_AUTOMATIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | 0.05 V |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | 0.15 V |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | 0.8 A |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | 0.0 W |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | 300.0 W4 |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | 0.8 A |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | 1000.0 ohms |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | 1000.0 ohms |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.0 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | 24.0 A/us |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 40 A |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | 24.0 A/us |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.8 A |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 40 A |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_E_LOAD2 |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 1800130 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 s |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns2 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""2 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_CURRENT |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | 0.02 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | VI_FALSE |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | VI_FALSE2 |
| NIDCPOWER_ATTR_OVP_LIMIT | 0.02 |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hz |
| NIDCPOWER_ATTR_POWER_SOURCE | X |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_WRITE_TO_EEPROM |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns2 |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | X |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | VI_FALSE2 |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns2 |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 60.0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 60 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | INFINITY2 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF2 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 60 V |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

<sup>4</sup> Default depends on the max DC sinking power of the instrument. Refer to the specifications for your instrument for more information.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4112_4113.html language=enus -->
## TOPIC 00105: Attributes Supported by the PXIe-4112/4113

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4112_4113.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4112_4113.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4112/4113

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4112 | PXIe-4113 |
| --- | --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | X | X |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | X | X |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.01 | 0.02 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 1 | 6 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.1 | -0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 1 | 6 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 10500 | 10500 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""2 | ""2 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hertz | 60 Hertz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_AUXILIARY4 | NIDCPOWER_VAL_AUXILIARY4 |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | X | X |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_REMOTE5 | NIDCPOWER_VAL_REMOTE5 |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | X | X |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | X | X |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.08 s | 0.08 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | X | X |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0.1 | 0.03 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 60 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 10 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 10 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -10 | -10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 60 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | X | X |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

<sup>4</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

<sup>5</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4132.html language=enus -->
## TOPIC 00106: Attributes Supported by the PXI-4132

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4132.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4132.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXI-4132

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXI-4132 |
| --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | X |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | X |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_ON |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.002 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.02 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.02 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.02 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 0.1 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 64000 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 150 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""2 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | NIDCPOWER_VAL_HIGH |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | 0.0 |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | X |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hertz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_WRITE_TO_EEPROM |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 150 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 150 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | X |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | X |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 150 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | X |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 10 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | X |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4135.html language=enus -->
## TOPIC 00107: Attributes Supported by the PXIe-4135

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4135.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4135.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4135

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4135 |
| --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | NIDCPOWER_VAL_APERTURE_TIME_AUTO_MODE_OFF |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | NIDCPOWER_VAL_APERTURE_TIME_AUTO |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | 0.5 s |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | 0 |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | NORMAL |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | Determined by the value of the Normal setting of the Transient Response property. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | Determined by the value of the Normal setting of the Transient Response property. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.0 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 3 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 0.1 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | Determined by the value of the Normal setting of the Transient Response property. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | N/A |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 1800000 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""2 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | 0.0 |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | Yes |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | Yes |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | 0.0 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_OVP_LIMIT | 210 V |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hertz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | 0 A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | 100 mA |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | 100 mA |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | -100 mA |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | 16.67 mS |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | 0 V |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | 6 V |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | 6 V |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | -6 V |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | 0 A |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | 10 A |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | 100 mA |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | 100 mA |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | -100 mA |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | 100 mA |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | 34 ms |
| NIDCPOWER_ATTR_PULSE_ON_TIME | 34 ms |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | 0 V |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | 6 V |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | 6 V |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | 6 V |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | -6 V |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | 6 V |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_WRITE_TO_EEPROM4 |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | 50 ms |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | Determined by the value of the Normal setting of the Transient Response property. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | Determined by the value of the Normal setting of the Transient Response property. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 6 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | Determined by the value of the Normal setting of the Transient Response property. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

<sup>4</sup> NIDCPOWER_VAL_WRITE_TO_EEPROM is the only valid value.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4140_4141.html language=enus -->
## TOPIC 00108: Attributes Supported by the PXIe-4140/4141

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4140_4141.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4140_4141.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4140/4141

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4140 | PXIe-4141 |
| --- | --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.1 | -0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL1 | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | "" | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 600000 | 600000 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND2 | NIDCPOWER_VAL_ON_DEMAND2 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""3 | ""3 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | NIDCPOWER_VAL_HIGH | NIDCPOWER_VAL_HIGH |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE4 | VI_TRUE4 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | X | 0 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hertz | 60 Hertz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_KEEP_IN_MEMORY | NIDCPOWER_VAL_KEEP_IN_MEMORY |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | 50 ms | 50 ms |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 10 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 10 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 10 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -10 | -10 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 10 | 10 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | X | Determined by the value of the Normal setting of the Transient Response attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> NIDCPOWER_VAL_NORMAL is the only valid value.

<sup>2</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>3</sup> Only valid value.

<sup>4</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4142_4143.html language=enus -->
## TOPIC 00109: Attributes Supported by the PXIe-4142/4143

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4142_4143.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4142_4143.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4142/4143

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4142 | PXIe-4143 |
| --- | --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.15 | 0.15 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 0.15 | 0.15 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.15 | 0.15 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.15 | 0.15 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.15 | -0.15 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 0.15 | 0.15 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL1 | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 600000 | 600000 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND2 | NIDCPOWER_VAL_ON_DEMAND2 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""3 | ""3 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE4 | VI_TRUE4 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | X | 0 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hertz | 60 Hertz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_KEEP_IN_MEMORY | NIDCPOWER_VAL_KEEP_IN_MEMORY |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | 50 ms | 50 ms |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 24 | 24 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 24 | 24 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 24 | 24 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -24 | -24 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 24 | 24 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | X | Determined by the value of the Normal setting of the Transient Response attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> NIDCPOWER_VAL_NORMAL is the only valid value.

<sup>2</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>3</sup> Only valid value.

<sup>4</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4144_4145.html language=enus -->
## TOPIC 00110: Attributes Supported by the PXIe-4144/4145

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4144_4145.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4144_4145.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4144/4145

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4144 | PXIe-4145 |
| --- | --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0 | 0 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 0.5 | 0.5 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.1 | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.1 | -0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 0.5 | 0.5 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL1 | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 600000 | 600000 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND2 | NIDCPOWER_VAL_ON_DEMAND2 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""3 | ""3 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE4 | VI_TRUE4 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | X | 0 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hertz | 60 Hertz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_KEEP_IN_MEMORY | NIDCPOWER_VAL_KEEP_IN_MEMORY |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | 50 ms | 50 ms |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | X | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 6 | 6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 6 | 6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 6 | 6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -6 | -6 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 6 | 6 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | X | Determined by the value of the Normal setting of the Transient Response attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> NIDCPOWER_VAL_NORMAL is the only valid value.

<sup>2</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>3</sup> Only valid value.

<sup>4</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4147.html language=enus -->
## TOPIC 00111: Attributes Supported by the PXIe-4147

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4147.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4147.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4147

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4147 |
| --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | 0 |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | NIDCPOWER_VAL_APERTURE_TIME_AUTO |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | 0.5 s |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | 0 |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | NIDCPOWER_VAL_THRESHOLD_MODE_NORMAL |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.0 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 3 A |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.001 A |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.001 A |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.001 A |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 3 A |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 100096 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 s |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | None |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | "" |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE2 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | 0.0 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | 0 W |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_WRITE_TO_EEPROM |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | 50 ms |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 8 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 8 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 8 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -8 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 8 V |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4150_4151.html language=enus -->
## TOPIC 00112: Attributes Supported by the PXIe-4150/4151

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4150_4151.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4150_4151.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4150/4151

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4150 | PXIe-4151 |
| --- | --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | N/A | N/A |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | NIDCPOWER_VAL_OFF2 | NIDCPOWER_VAL_OFF2 |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF2 | NIDCPOWER_VAL_OFF2 |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | X | X |
| NIDCPOWER_ATTR_CABLE_LENGTH | X | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.0 | 0.0 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 1 A | 1 A |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.1 A | 0.1 A |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.1 A | 0.1 A |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.1 A | -0.1 A |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 1 A | 1 A |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING2 | NIDCPOWER_VAL_RISING2 |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS2 | NIDCPOWER_VAL_SMU_PS2 |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 1800130 | 1800130 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 s | 0 s |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns2 | 250 ns2 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""2 | ""2 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | 0.02 | 0.02 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | VI_FALSE2 | VI_FALSE2 |
| NIDCPOWER_ATTR_OVP_LIMIT | 0.02 | 0.02 |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC | NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hz | 60 Hz |
| NIDCPOWER_ATTR_POWER_SOURCE | X | X |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | N/A | N/A |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_WRITE_TO_EEPROM | NIDCPOWER_VAL_WRITE_TO_EEPROM |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns2 | 250 ns2 |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns2 | 250 ns2 |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | X | X |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | VI_FALSE2 | VI_FALSE2 |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH2 | NIDCPOWER_VAL_ACTIVE_HIGH2 |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns2 | 250 ns2 |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW2 |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0.01 V | 0.01 V |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 6 V | 6 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 6 V | 6 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | 6 V | 6 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -6 V | -6 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 6 V | 6 V |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4154.html language=enus -->
## TOPIC 00113: Attributes Supported by the PXIe-4154

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4154.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4154.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4154

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4154 |
| --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | X |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | X |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_APERTURE_TIME | X |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | X |
| NIDCPOWER_ATTR_AUTORANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | X |
| NIDCPOWER_ATTR_CACHE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | Channel 1: 3 Channel 2: 1.5 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -0.1 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | Channel 1: 3 Channel 2: 1.5 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | X |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 200000 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""2 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | NIDCPOWER_VAL_HIGH |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | 04 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | VI_TRUE |
| NIDCPOWER_ATTR_OVP_LIMIT | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | X |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 500 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | X |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | X |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | X |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL4 |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | Channel 0: 6 Channel 1: 8 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | Channel 0: 6 Channel 1: 8 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | Channel 0: 6 Channel 1: 8 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | Channel 0: -6 Channel 1: -8 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | Channel 0: 6 Channel 1: 8 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | X |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

<sup>4</sup> Channel 0.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4162_4163.html language=enus -->
## TOPIC 00114: Attributes Supported by the PXIe-4162/4163

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4162_4163.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4162_4163.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4162/4163

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4162 | PXIe-4163 |
| --- | --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | X | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | X | NIDCPOWER_VAL_APERTURE_TIME_AUTO |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | X | NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | X | 0.1 s |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | X | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | X | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | X | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | X | 0 |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | X | NIDCPOWER_VAL_THRESHOLD_MODE_NORMAL |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_CACHE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | Determined by the value of the Normal setting of the Transient Response attribute. | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | Determined by the value of the Normal setting of the Transient Response attribute. | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.0 | 0.0 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 0.001 | 0.001 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 0.001 | 0.001 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 0.001 | 0.001 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | Determined by the value of the Normal setting of the Transient Response attribute. | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | N/A | N/A |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | X | X |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_FREQUENCY | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | X | X |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | X | X |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | X | X |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | X | X |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | X | X |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | X | X |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 100096 | 100096 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 | 0 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | NIDCPOWER_VAL_DIGITAL_EDGE | NIDCPOWER_VAL_DIGITAL_EDGE |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | "" | "" |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | X | X |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hertz | 60 Hertz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_INTERNAL | NIDCPOWER_VAL_INTERNAL |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_WRITE_TO_EEPROM | NIDCPOWER_VAL_WRITE_TO_EEPROM |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_LOCAL | NIDCPOWER_VAL_LOCAL |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | X | X |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | X | X |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | X | X |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | X | X |
| NIDCPOWER_ATTR_SOURCE_DELAY | 0.01666666 s | 0.01666666 s |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | Determined by the value of the Normal setting of the Transient Response attribute. | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | Determined by the value of the Normal setting of the Transient Response attribute. | Determined by the value of the Normal setting of the Transient Response attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 24 | 24 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 24 | 24 |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | X | X |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | X | X |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 24 | 24 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | Determined by the value of the Normal setting of the Transient Response attribute. | Determined by the value of the Normal setting of the Transient Response attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__attributes__by__device_supported_attributes_4190.html language=enus -->
## TOPIC 00115: Attributes Supported by the PXIe-4190

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__attributes__by__device_supported_attributes_4190.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__attributes__by__device_supported_attributes_4190.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists the default values for each attribute you can configure for your device. An X in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-

### Attributes Supported by the PXIe-4190

The following table lists the default values for each attribute you can configure for your device. An **X** in a table cell indicates that the listed attribute is not supported for that device. N/A in a table cell indicates that there is not a default value for the listed attribute because it is a read-only attribute.

| Attribute | PXIe-4190 |
| --- | --- |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE | "" |
| NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP | 0 |
| NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_APERTURE_TIME | 16.66e-3 |
| NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE | X |
| NIDCPOWER_ATTR_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE | NIDCPOWER_VAL_APERTURE_TIME_AUTO |
| NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR | NIDCPOWER_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN |
| NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE | 5.0 s |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS | NIDCPOWER_VAL_SECONDS |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE | 0 |
| NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE | 0 |
| NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE | NIDCPOWER_VAL_THRESHOLD_MODE_NORMAL |
| NIDCPOWER_ATTR_AUTO_ZERO | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE | N/A |
| NIDCPOWER_ATTR_CABLE_LENGTH | NIDCPOWER_VAL_NI_STANDARD_1M |
| NIDCPOWER_ATTR_CACHE | VI_TRUE |
| NIDCPOWER_ATTR_CHANNEL_COUNT | N/A |
| NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY | NIDCPOWER_VAL_COMPLIANCE_LIMIT_SYMMETRY_SYMMETRIC |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_MODE | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_OFF_THRESHOLD | X |
| NIDCPOWER_ATTR_CONDUCTION_VOLTAGE_ON_THRESHOLD | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_POWER_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_GAIN_BANDWIDTH | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_CONSTANT_RESISTANCE_POLE_ZERO_RATIO | X |
| NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_CURRENT_LEVEL | 0.0 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LEVEL_FALLING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE | 1.0e-3 |
| NIDCPOWER_ATTR_CURRENT_LEVEL_RISING_SLEW_RATE | X |
| NIDCPOWER_ATTR_CURRENT_LIMIT | 1.0e-3 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH | 1.e0-3 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_LOW | -1.0e-3 |
| NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE | 1.0e-3 |
| NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_DC_NOISE_REJECTION | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL | X |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE | NIDCPOWER_VAL_RISING |
| NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_DRIVER_SETUP | N/A |
| NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_FETCH_BACKLOG | N/A |
| NIDCPOWER_ATTR_GROUP_CAPABILITIES | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER | N/A |
| NIDCPOWER_ATTR_INSTRUMENT_MODE | NIDCPOWER_VAL_SMU_PS |
| NIDCPOWER_ATTR_INSTRUMENT_MODEL | N/A |
| NIDCPOWER_ATTR_INTERCHANGE_CHECK | VI_FALSE |
| NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN | X |
| NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR | N/A |
| NIDCPOWER_ATTR_ISOLATION_STATE | Isolated |
| NIDCPOWER_ATTR_LCR_AC_DITHER_ENABLED | VI_TRUE |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY | Determined by the value of the NIDCPOWER_ATTR_CABLE_LENGTH attribute. |
| NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL | NIDCPOWER_VAL_ON |
| NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE | 7.08e-9 A |
| NIDCPOWER_ATTR_LCR_CURRENT_RANGE | 700.0e-6 A |
| NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME | 0.01 s |
| NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL | NIDCPOWER_VAL_ON |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL | 0.0 |
| NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_RANGE | 1.0e-3 A |
| NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE | NIDCPOWER_VAL_DC_BIAS_OFF |
| NIDCPOWER_ATTR_LCR_DC_BIAS_TRANSIENT_RESPONSE | NIDCPOWER_VAL_LCR_DC_BIAS_TRANSIENT_RESPONSE_NORMAL |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL | 0.0 |
| NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_RANGE | 10 V |
| NIDCPOWER_ATTR_LCR_FREQUENCY | 1000 |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_AUTO_RANGE | NIDCPOWER_VAL_AUTO_RANGE_OFF |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE | 100.0 |
| NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE | NIDCPOWER_VAL_LCR_IMPEDANCE_RANGE |
| NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME | NIDCPOWER_VAL_LCR_MEDIUM |
| NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE | NIDCPOWER_VAL_ONBOARD_STORAGE |
| NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED | VI_TRUE |
| NIDCPOWER_ATTR_LCR_SHORT_REACTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE | 0.0 |
| NIDCPOWER_ATTR_LCR_SOURCE_APERTURE_TIME | 50.0e-6 s |
| NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE | NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC |
| NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION | NIDCPOWER_VAL_AC_VOLTAGE |
| NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE | 7.08e-3 |
| NIDCPOWER_ATTR_LCR_VOLTAGE_RANGE | 7 V |
| NIDCPOWER_ATTR_LOGICAL_NAME | N/A |
| NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE | 60078 |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY | 0 s |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW |
| NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME | N/A |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH | 1 |
| NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE | VI_TRUE |
| NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE | None |
| NIDCPOWER_ATTR_MEASURE_WHEN | NIDCPOWER_VAL_ON_DEMAND1 |
| NIDCPOWER_ATTR_MERGED_CHANNELS | ""2 |
| NIDCPOWER_ATTR_OUTPUT_CAPACITANCE | X |
| NIDCPOWER_ATTR_OUTPUT_CONNECTED | VI_TRUE |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_OUTPUT_ENABLED | VI_TRUE3 |
| NIDCPOWER_ATTR_OUTPUT_FUNCTION | NIDCPOWER_VAL_DC_VOLTAGE |
| NIDCPOWER_ATTR_OUTPUT_RESISTANCE | 0.0 |
| NIDCPOWER_ATTR_OUTPUT_SHORTED | X |
| NIDCPOWER_ATTR_OVERRANGING_ENABLED | VI_FALSE |
| NIDCPOWER_ATTR_OVP_ENABLED | X |
| NIDCPOWER_ATTR_OVP_LIMIT | X |
| NIDCPOWER_ATTR_POWER_ALLOCATION_MODE | X |
| NIDCPOWER_ATTR_POWER_LINE_FREQUENCY | 60 Hz |
| NIDCPOWER_ATTR_POWER_SOURCE | NIDCPOWER_VAL_AUTOMATIC |
| NIDCPOWER_ATTR_POWER_SOURCE_IN_USE | N/A |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_BIAS_DELAY | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_PULSE_OFF_TIME | X |
| NIDCPOWER_ATTR_PULSE_ON_TIME | X |
| NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW | X |
| NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE | X |
| NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS | VI_TRUE |
| NIDCPOWER_ATTR_RANGE_CHECK | VI_TRUE |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY | X |
| NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH | X |
| NIDCPOWER_ATTR_RECORD_COERCIONS | VI_FALSE |
| NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION | X |
| NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT | X |
| NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE | 1 |
| NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE | NIDCPOWER_VAL_WRITE_TO_EEPROM |
| NIDCPOWER_ATTR_SENSE | NIDCPOWER_VAL_REMOTE |
| NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT | 1 |
| NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE | NIDCPOWER_VAL_TRUE |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME | X |
| NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED | X |
| NIDCPOWER_ATTR_SERIAL_NUMBER | N/A |
| NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE | X |
| NIDCPOWER_ATTR_SIMULATE | VI_FALSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_BEHAVIOR | NIDCPOWER_VAL_EVENT_OUTPUT_BEHAVIOR_PULSE |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL | "" |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY | NIDCPOWER_VAL_ACTIVE_HIGH |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH | 250 ns |
| NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_TOGGLE_INITIAL_STATE | NIDCPOWER_VAL_EVENT_TOGGLE_INITIAL_STATE_LOW |
| NIDCPOWER_ATTR_SOURCE_DELAY | 16.66e-3 s4 |
| NIDCPOWER_ATTR_SOURCE_MODE | NIDCPOWER_VAL_SINGLE_POINT |
| NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION | N/A |
| NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR | N/A |
| NIDCPOWER_ATTR_START_TRIGGER_TYPE | NIDCPOWER_VAL_NONE |
| NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS | N/A |
| NIDCPOWER_ATTR_TRANSIENT_RESPONSE | NIDCPOWER_VAL_NORMAL |
| NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL | 0 |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE | 10.0 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT | 10.0 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE | NIDCPOWER_VAL_OFF |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH | -10 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW | -10 V |
| NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE | 10.0 |
| NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO | Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute. |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>2</sup> Only valid value.

<sup>3</sup> The default value is VI_TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) or [niDCPower_InitializeWithChannels](group____root__nidcpower__functions__initializeclose_1gaf569a1bca9ef6711f07e75b53d799d3f.html) function to open the session, otherwise the default value is VI_FALSE.

<sup>4</sup> Software timed.

**Related Topics:**

- [Supported Attributes by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_attributes_by_device)

Parent topic:

Supported Attributes by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device.html language=enus -->
## TOPIC 00116: Supported Functions by Device

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following topics for information about function support.Functions Supported by the PXIe-4051Functions Supported by the PXI-4110Functions Supported by the PXIe-4112/4113Functions Supported by the PXI-4130Functions Supported by the PXI-4132Functions Supported by the PXIe-4135Functions Sup

### Supported Functions by Device

Refer to the following topics for information about function support.

- [Functions Supported by the PXIe-4051](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4051)
- [Functions Supported by the PXI-4110](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4110)
- [Functions Supported by the PXIe-4112/4113](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4112_4113)
- [Functions Supported by the PXI-4130](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4130)
- [Functions Supported by the PXI-4132](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4132)
- [Functions Supported by the PXIe-4135](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4135)
- [Functions Supported by the PXIe-4136/4137](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4136_4137)
- [Functions Supported by the PXIe-4138/4139](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4138_4139)
- [Functions Supported by the PXIe-4140/4141/4142/4143/4144/4145](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_414x)
- [Functions Supported by the PXIe-4147](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4147)
- [Functions Supported by the PXIe-4150/4151](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4150_4151)
- [Functions Supported by the PXIe-4154](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4154)
- [Functions Supported by the PXIe-4162/4163](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4162_4163)
- [Functions Supported by the PXIe-4190](/csh?context=nidcpower_nidcpowercref_pages_supported_functions_4190)

#### Groups

None

#### Group members

None

#### Attachments

| Name | Description |
| --- | --- |
| Functions Supported by the PXI-4110 |  |
| Functions Supported by the PXI-4130 |  |
| Functions Supported by the PXI-4132 |  |
| Functions Supported by the PXIe-4051 |  |
| Functions Supported by the PXIe-4112/4113 |  |
| Functions Supported by the PXIe-4135 |  |
| Functions Supported by the PXIe-4136/4137 |  |
| Functions Supported by the PXIe-4138/4139 |  |
| Functions Supported by the PXIe-4140/4141/4142/4143/4144/4145 |  |
| Functions Supported by the PXIe-4147 |  |
| Functions Supported by the PXIe-4150/4151 |  |
| Functions Supported by the PXIe-4154 |  |
| Functions Supported by the PXIe-4162/4163 |  |
| Functions Supported by the PXIe-4190 |  |

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4051.html language=enus -->
## TOPIC 00117: Functions Supported by the PXIe-4051

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4051.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4051.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4051niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceYesniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetXniDCPower_CalAdjustResidualVoltageOffsetXniDCPower_CalAdjustVolta

### Functions Supported by the PXIe-4051

| Function | PXIe-4051 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | Yes |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | X |
| niDCPower_CalAdjustResidualVoltageOffset | X |
| niDCPower_CalAdjustVoltageLevel | X |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | Yes |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | Yes |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4110.html language=enus -->
## TOPIC 00118: Functions Supported by the PXI-4110

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4110.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4110.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXI-4110niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementYesniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetXniDCPower_CalAdjustResidualVoltageOffsetXniDCPower_CalAdjustVoltag

### Functions Supported by the PXI-4110

| Function | PXI-4110 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | Yes |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | X |
| niDCPower_CalAdjustResidualVoltageOffset | X |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | Yes |
| niDCPower_CalSelfCalibrate | X |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | X |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | X |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | X |
| niDCPower_ConfigurePowerLineFrequency | X |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | X |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | X |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | X |
| niDCPower_CreateAdvancedSequenceStepWithChannels | X |
| niDCPower_DeleteAdvancedSequenceWithChannels | X |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | X |
| niDCPower_DisableSourceTriggerWithChannels | X |
| niDCPower_DisableStartTriggerWithChannels | X |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | X |
| niDCPower_FetchMultiple | X |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | X |
| niDCPower_GetSelfCalLastTemp | X |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | X |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | X |
| niDCPower_WaitForEventWithChannels | Yes3 |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4112_4113.html language=enus -->
## TOPIC 00119: Functions Supported by the PXIe-4112/4113

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4112_4113.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4112_4113.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4112PXIe-4113niDCPower_AbortWithChannelsYesYesniDCPower_CalAdjustCurrentLimitYesYesniDCPower_CalAdjustCurrentMeasurementYesYesniDCPower_CalAdjustInternalReferenceXXniDCPower_CalAdjustOutputResistanceXXniDCPower_CalAdjustResidualCurrentOffsetXXniDCPower_CalAdjustResidualVoltageOffsetXXni

### Functions Supported by the PXIe-4112/4113

| Function | PXIe-4112 | PXIe-4113 |
| --- | --- | --- |
| niDCPower_AbortWithChannels | Yes | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes | Yes |
| niDCPower_CalAdjustCurrentMeasurement | Yes | Yes |
| niDCPower_CalAdjustInternalReference | X | X |
| niDCPower_CalAdjustOutputResistance | X | X |
| niDCPower_CalAdjustResidualCurrentOffset | X | X |
| niDCPower_CalAdjustResidualVoltageOffset | X | X |
| niDCPower_CalAdjustVoltageLevel | Yes | Yes |
| niDCPower_CalAdjustVoltageMeasurement | Yes | Yes |
| niDCPower_CalSelfCalibrate | X | X |
| niDCPower_ChangeExtCalPassword | Yes | Yes |
| niDCPower_ClearInterchangeWarnings | Yes | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X | X |
| niDCPower_close | Yes | Yes |
| niDCPower_CloseExtCal | Yes | Yes |
| niDCPower_CommitWithChannels | Yes | Yes |
| niDCPower_ConfigureApertureTime | Yes | Yes |
| niDCPower_ConfigureAutoZero | X | X |
| niDCPower_ConfigureCurrentLevel | Yes | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes | Yes |
| niDCPower_ConfigureCurrentLimit | Yes | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureLCRCompensation | X |  |
| niDCPower_ConfigureLCRCustomCableCompensation | X |  |
| niDCPower_ConfigureOutputEnabled | Yes | Yes |
| niDCPower_ConfigureOutputFunction | Yes | Yes |
| niDCPower_ConfigureOutputResistance | X | X |
| niDCPower_ConfigurePowerLineFrequency | Yes | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X | X |
| niDCPower_ConfigurePulseCurrentLevel | X | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X | X |
| niDCPower_ConfigurePulseCurrentLimit | X | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X | X |
| niDCPower_ConfigurePulseVoltageLevel | X | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X | X |
| niDCPower_ConfigurePulseVoltageLimit | X | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X | X |
| niDCPower_ConfigureSense | Yes | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes | Yes |
| niDCPower_ConfigureVoltageLevel | Yes | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes | Yes |
| niDCPower_ConfigureVoltageLimit | Yes | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes | Yes |
| niDCPower_ConnectInternalReference | X | X |
| niDCPower_CreateAdvancedSequenceWithChannels | X | X |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | X | X |
| niDCPower_CreateAdvancedSequenceStepWithChannels | X | X |
| niDCPower_DeleteAdvancedSequenceWithChannels | X | X |
| niDCPower_Disable | Yes | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes | Yes |
| niDCPower_ExportSignalWithChannels | Yes | Yes |
| niDCPower_FetchMultiple | Yes | Yes |
| niDCPower_FetchMultipleLCR | X | X |
| niDCPower_GetAttributeViBoolean | Yes | Yes |
| niDCPower_GetAttributeViInt32 | Yes | Yes |
| niDCPower_GetAttributeViReal64 | Yes | Yes |
| niDCPower_GetAttributeViSession | Yes | Yes |
| niDCPower_GetAttributeViString | Yes | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes | Yes |
| niDCPower_GetChannelName | Yes | Yes |
| niDCPower_GetChannelNameFromString | Yes | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes | Yes |
| niDCPower_GetExtCalLastTemp | Yes | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |  |
| niDCPower_GetLCRCompensationData | X |  |
| niDCPower_GetLCRCustomCableCompensationData | X |  |
| niDCPower_GetNextCoercionRecord | Yes | Yes |
| niDCPower_GetNextInterchangeWarning | Yes | Yes |
| niDCPower_GetSelfCalLastDateAndTime | X | X |
| niDCPower_GetSelfCalLastTemp | X | X |
| niDCPower_ImportAttributeConfigurationBuffer | Yes | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes | Yes |
| niDCPower_InitExtCal | Yes | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes | Yes |
| niDCPower_InitWithOptions | Yes | Yes |
| niDCPower_Measure | Yes | Yes |
| niDCPower_MeasureMultiple | Yes | Yes |
| niDCPower_MeasureMultipleLCR | X | X |
| niDCPower_PerformLCRLoadCompensation | X | X |
| niDCPower_PerformLCROpenCompensation | X | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X | X |
| niDCPower_PerformLCRShortCompensation | X | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X | X |
| niDCPower_QueryInCompliance | Yes | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X | X |
| niDCPower_QueryMaxCurrentLimit | Yes | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes | Yes |
| niDCPower_QueryMinCurrentLimit | Yes | Yes |
| niDCPower_QueryOutputState | Yes | Yes |
| niDCPower_ReadCurrentTemperature | Yes | Yes |
| niDCPower_ResetWithChannels | Yes | Yes |
| niDCPower_ResetDevice | Yes | Yes |
| niDCPower_ResetInterchangeCheck | Yes | Yes |
| niDCPower_ResetWithDefaults | Yes | Yes |
| niDCPower_revision_query | Yes | Yes |
| niDCPower_self_test | Yes | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes | Yes |
| niDCPower_SetAttributeViBoolean | Yes | Yes |
| niDCPower_SetAttributeViInt32 | Yes | Yes |
| niDCPower_SetAttributeViReal64 | Yes | Yes |
| niDCPower_SetAttributeViSession | Yes | Yes |
| niDCPower_SetAttributeViString | Yes | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes | Yes |
| niDCPower_SetSequence | Yes | Yes |
| niDCPower_WaitForEventWithChannels | Yes | Yes |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4130.html language=enus -->
## TOPIC 00120: Functions Supported by the PXI-4130

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4130.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4130.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXI-4130niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementYesniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetXniDCPower_CalAdjustResidualVoltageOffsetXniDCPower_CalAdjustVoltag

### Functions Supported by the PXI-4130

| Function | PXI-4130 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | Yes |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | X |
| niDCPower_CalAdjustResidualVoltageOffset | X |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | Yes |
| niDCPower_CalSelfCalibrate | X |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | X |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | X |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | X |
| niDCPower_ConfigurePowerLineFrequency | X |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | X |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | X |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | X |
| niDCPower_CreateAdvancedSequenceStepWithChannels | X |
| niDCPower_DeleteAdvancedSequenceWithChannels | X |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | X |
| niDCPower_DisableSourceTriggerWithChannels | X |
| niDCPower_DisableStartTriggerWithChannels | X |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | X |
| niDCPower_FetchMultiple | X |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | X |
| niDCPower_GetSelfCalLastTemp | X |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | X |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | X |
| niDCPower_WaitForEventWithChannels | Yes3 |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4132.html language=enus -->
## TOPIC 00121: Functions Supported by the PXI-4132

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4132.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4132.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXI-4132niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementYesniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetXniDCPower_CalAdjustResidualVoltageOffsetXniDCPower_CalAdjustVoltag

### Functions Supported by the PXI-4132

| Function | PXI-4132 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | Yes |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | X |
| niDCPower_CalAdjustResidualVoltageOffset | X |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | Yes |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | Yes |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | X |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | X |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | X |
| niDCPower_CreateAdvancedSequenceStepWithChannels | X |
| niDCPower_DeleteAdvancedSequenceWithChannels | X |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4135.html language=enus -->
## TOPIC 00122: Functions Supported by the PXIe-4135

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4135.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4135.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4135niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetYesniDCPower_CalAdjustResidualVoltageOffsetYesniDCPower_CalAdjustVol

### Functions Supported by the PXIe-4135

| Function | PXIe-4135 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | Yes |
| niDCPower_CalAdjustResidualVoltageOffset | Yes |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | Yes |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes1 |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | Yes |
| niDCPower_ConfigurePulseBiasCurrentLimit | Yes |
| niDCPower_ConfigurePulseBiasVoltageLevel | Yes |
| niDCPower_ConfigurePulseBiasVoltageLimit | Yes |
| niDCPower_ConfigurePulseCurrentLevel | Yes |
| niDCPower_ConfigurePulseCurrentLevelRange | Yes |
| niDCPower_ConfigurePulseCurrentLimit | Yes |
| niDCPower_ConfigurePulseCurrentLimitRange | Yes |
| niDCPower_ConfigurePulseVoltageLevel | Yes |
| niDCPower_ConfigurePulseVoltageLevelRange | Yes |
| niDCPower_ConfigurePulseVoltageLimit | Yes |
| niDCPower_ConfigurePulseVoltageLimitRange | Yes |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | Yes |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | Yes |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4136_4137.html language=enus -->
## TOPIC 00123: Functions Supported by the PXIe-4136/4137

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4136_4137.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4136_4137.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4136/4137niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetYesniDCPower_CalAdjustResidualVoltageOffsetYesniDCPower_CalAdju

### Functions Supported by the PXIe-4136/4137

| Function | PXIe-4136/4137 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | Yes |
| niDCPower_CalAdjustResidualVoltageOffset | Yes |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | Yes |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes1 |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | Yes |
| niDCPower_ConfigurePulseBiasCurrentLimit | Yes |
| niDCPower_ConfigurePulseBiasVoltageLevel | Yes |
| niDCPower_ConfigurePulseBiasVoltageLimit | Yes |
| niDCPower_ConfigurePulseCurrentLevel | Yes |
| niDCPower_ConfigurePulseCurrentLevelRange | Yes |
| niDCPower_ConfigurePulseCurrentLimit | Yes |
| niDCPower_ConfigurePulseCurrentLimitRange | Yes |
| niDCPower_ConfigurePulseVoltageLevel | Yes |
| niDCPower_ConfigurePulseVoltageLevelRange | Yes |
| niDCPower_ConfigurePulseVoltageLimit | Yes |
| niDCPower_ConfigurePulseVoltageLimitRange | Yes |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | Yes |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | Yes |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4138_4139.html language=enus -->
## TOPIC 00124: Functions Supported by the PXIe-4138/4139

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4138_4139.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4138_4139.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4138/4139niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetYesniDCPower_CalAdjustResidualVoltageOffsetYesniDCPower_CalAdju

### Functions Supported by the PXIe-4138/4139

| Function | PXIe-4138/4139 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | Yes |
| niDCPower_CalAdjustResidualVoltageOffset | Yes |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | Yes |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeShutdownTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes1 |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | Yes |
| niDCPower_ConfigurePulseBiasCurrentLimit | Yes |
| niDCPower_ConfigurePulseBiasVoltageLevel | Yes |
| niDCPower_ConfigurePulseBiasVoltageLimit | Yes |
| niDCPower_ConfigurePulseCurrentLevel | Yes |
| niDCPower_ConfigurePulseCurrentLevelRange | Yes |
| niDCPower_ConfigurePulseCurrentLimit | Yes |
| niDCPower_ConfigurePulseCurrentLimitRange | Yes |
| niDCPower_ConfigurePulseVoltageLevel | Yes |
| niDCPower_ConfigurePulseVoltageLevelRange | Yes |
| niDCPower_ConfigurePulseVoltageLimit | Yes |
| niDCPower_ConfigurePulseVoltageLimitRange | Yes |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeShutdownTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | Yes |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableShutdownTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | Yes |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4147.html language=enus -->
## TOPIC 00125: Functions Supported by the PXIe-4147

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4147.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4147.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4147niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetYesniDCPower_CalAdjustResidualVoltageOffsetYesniDCPower_CalAdjustVol

### Functions Supported by the PXIe-4147

| Function | PXIe-4147 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | Yes |
| niDCPower_CalAdjustResidualVoltageOffset | Yes |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | Yes |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_414x.html language=enus -->
## TOPIC 00126: Functions Supported by the PXIe-4140/4141/4142/4143/4144/4145

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_414x.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_414x.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4140/4141/4142/4143/4144/4145niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitXniDCPower_CalAdjustCurrentMeasurementYesniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetYesniDCPower_CalAdjustResidualVoltageOffset

### Functions Supported by the PXIe-4140/4141/4142/4143/4144/4145

| Function | PXIe-4140/4141/4142/4143/4144/4145 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | X |
| niDCPower_CalAdjustCurrentMeasurement | Yes |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | Yes |
| niDCPower_CalAdjustResidualVoltageOffset | Yes |
| niDCPower_CalAdjustVoltageLevel | X |
| niDCPower_CalAdjustVoltageMeasurement | Yes |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes1 |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes9 |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes9 |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes9 |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes9 |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

<sup>9</sup> NI-DCPower 15.1 and later support this function.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4150_4151.html language=enus -->
## TOPIC 00127: Functions Supported by the PXIe-4150/4151

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4150_4151.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4150_4151.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4150/4151niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetXniDCPower_CalAdjustResidualVoltageOffsetXniDCPower_CalAdjustVo

### Functions Supported by the PXIe-4150/4151

| Function | PXIe-4150/4151 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | X |
| niDCPower_CalAdjustResidualVoltageOffset | X |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | Yes |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4154.html language=enus -->
## TOPIC 00128: Functions Supported by the PXIe-4154

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4154.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4154.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4154niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementYesniDCPower_CalAdjustInternalReferenceXniDCPower_CalAdjustOutputResistanceYesniDCPower_CalAdjustResidualCurrentOffsetXniDCPower_CalAdjustResidualVoltageOffsetXniDCPower_CalAdjustVol

### Functions Supported by the PXIe-4154

| Function | PXIe-4154 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | Yes |
| niDCPower_CalAdjustInternalReference | X |
| niDCPower_CalAdjustOutputResistance | Yes |
| niDCPower_CalAdjustResidualCurrentOffset | X |
| niDCPower_CalAdjustResidualVoltageOffset | X |
| niDCPower_CalAdjustVoltageLevel | Yes |
| niDCPower_CalAdjustVoltageMeasurement | Yes |
| niDCPower_CalSelfCalibrate | X |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | X |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | Yes2 |
| niDCPower_ConfigurePowerLineFrequency | X |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | X |
| niDCPower_CreateAdvancedSequenceWithChannels | X |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | X |
| niDCPower_CreateAdvancedSequenceStepWithChannels | X |
| niDCPower_DeleteAdvancedSequenceWithChannels | X |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | X |
| niDCPower_GetSelfCalLastTemp | X |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4162_4163.html language=enus -->
## TOPIC 00129: Functions Supported by the PXIe-4162/4163

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4162_4163.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4162_4163.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4162/4163niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitYesniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceYesniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetYesniDCPower_CalAdjustResidualVoltageOffsetYesniDCPower_CalAd

### Functions Supported by the PXIe-4162/4163

| Function | PXIe-4162/4163 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | Yes |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | Yes |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | Yes |
| niDCPower_CalAdjustResidualVoltageOffset | Yes |
| niDCPower_CalAdjustVoltageLevel | X |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | X |
| niDCPower_ConfigureLCRCustomCableCompensation | X |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | X |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevel | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | Yes |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | X |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | X |
| niDCPower_GetLCRCompensationData | X |
| niDCPower_GetLCRCustomCableCompensationData | X |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | X |
| niDCPower_PerformLCRLoadCompensation | X |
| niDCPower_PerformLCROpenCompensation | X |
| niDCPower_PerformLCROpenCustomCableCompensation | X |
| niDCPower_PerformLCRShortCompensation | X |
| niDCPower_PerformLCRShortCustomCableCompensation | X |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes |
| niDCPower_WaitForEventWithChannels | Yes |

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower__supported__functions__by__device_supported_functions_4190.html language=enus -->
## TOPIC 00130: Functions Supported by the PXIe-4190

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower__supported__functions__by__device_supported_functions_4190.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower__supported__functions__by__device_supported_functions_4190.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FunctionPXIe-4190niDCPower_AbortWithChannelsYesniDCPower_CalAdjustCurrentLimitXniDCPower_CalAdjustCurrentMeasurementXniDCPower_CalAdjustInternalReferenceYesniDCPower_CalAdjustOutputResistanceXniDCPower_CalAdjustResidualCurrentOffsetYesniDCPower_CalAdjustResidualVoltageOffsetYesniDCPower_CalAdjustVol

### Functions Supported by the PXIe-4190

| Function | PXIe-4190 |
| --- | --- |
| niDCPower_AbortWithChannels | Yes |
| niDCPower_CalAdjustCurrentLimit | X |
| niDCPower_CalAdjustCurrentMeasurement | X |
| niDCPower_CalAdjustInternalReference | Yes |
| niDCPower_CalAdjustOutputResistance | X |
| niDCPower_CalAdjustResidualCurrentOffset | Yes |
| niDCPower_CalAdjustResidualVoltageOffset | Yes |
| niDCPower_CalAdjustVoltageLevel | X |
| niDCPower_CalAdjustVoltageMeasurement | X |
| niDCPower_CalSelfCalibrate | Yes |
| niDCPower_ChangeExtCalPassword | Yes |
| niDCPower_ClearInterchangeWarnings | Yes |
| niDCPower_ClearLatchedOutputCutoffState | X |
| niDCPower_close | Yes |
| niDCPower_CloseExtCal | Yes |
| niDCPower_CommitWithChannels | Yes |
| niDCPower_ConfigureApertureTime | Yes |
| niDCPower_ConfigureAutoZero | X |
| niDCPower_ConfigureCurrentLevel | Yes |
| niDCPower_ConfigureCurrentLevelRange | Yes |
| niDCPower_ConfigureCurrentLimit | Yes |
| niDCPower_ConfigureCurrentLimitRange | Yes |
| niDCPower_ConfigureDigitalEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureDigitalEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureLCRCompensation | Yes |
| niDCPower_ConfigureLCRCustomCableCompensation | Yes |
| niDCPower_ConfigureOutputEnabled | Yes |
| niDCPower_ConfigureOutputFunction | Yes |
| niDCPower_ConfigureOutputResistance | X |
| niDCPower_ConfigurePowerLineFrequency | Yes |
| niDCPower_ConfigurePulseBiasCurrentLevel | X |
| niDCPower_ConfigurePulseBiasCurrentLimit | X |
| niDCPower_ConfigurePulseBiasVoltageLevel | X |
| niDCPower_ConfigurePulseBiasVoltageLimit | X |
| niDCPower_ConfigurePulseCurrentLevel | X |
| niDCPower_ConfigurePulseCurrentLevelRange | X |
| niDCPower_ConfigurePulseCurrentLimit | X |
| niDCPower_ConfigurePulseCurrentLimitRange | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLevelRange | X |
| niDCPower_ConfigurePulseVoltageLimit | X |
| niDCPower_ConfigurePulseVoltageLimitRange | X |
| niDCPower_ConfigureSense | Yes |
| niDCPower_ConfigureSoftwareEdgeMeasureTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgePulseTriggerWithChannels | X |
| niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeSourceTriggerWithChannels | Yes |
| niDCPower_ConfigureSoftwareEdgeStartTriggerWithChannels | Yes |
| niDCPower_ConfigureSourceModeWithChannels | Yes |
| niDCPower_ConfigureVoltageLevel | Yes |
| niDCPower_ConfigureVoltageLevelRange | Yes |
| niDCPower_ConfigureVoltageLimit | Yes |
| niDCPower_ConfigureVoltageLimitRange | Yes |
| niDCPower_ConnectInternalReference | Yes |
| niDCPower_CreateAdvancedSequenceWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceCommitStepWithChannels | Yes |
| niDCPower_CreateAdvancedSequenceStepWithChannels | Yes |
| niDCPower_DeleteAdvancedSequenceWithChannels | Yes |
| niDCPower_Disable | Yes |
| niDCPower_DisablePulseTriggerWithChannels | X |
| niDCPower_DisableSequenceAdvanceTriggerWithChannels | Yes |
| niDCPower_DisableSourceTriggerWithChannels | Yes |
| niDCPower_DisableStartTriggerWithChannels | Yes |
| niDCPower_ExportAttributeConfigurationBuffer | Yes |
| niDCPower_ExportAttributeConfigurationFile | Yes |
| niDCPower_ExportSignalWithChannels | Yes |
| niDCPower_FetchMultiple | Yes |
| niDCPower_FetchMultipleLCR | Yes |
| niDCPower_GetAttributeViBoolean | Yes |
| niDCPower_GetAttributeViInt32 | Yes |
| niDCPower_GetAttributeViReal64 | Yes |
| niDCPower_GetAttributeViSession | Yes |
| niDCPower_GetAttributeViString | Yes |
| niDCPower_GetCalUserDefinedInfo | Yes |
| niDCPower_GetCalUserDefinedInfoMaxSize | Yes |
| niDCPower_GetChannelName | Yes |
| niDCPower_GetChannelNameFromString | Yes |
| niDCPower_GetExtCalLastDateAndTime | Yes |
| niDCPower_GetExtCalLastTemp | Yes |
| niDCPower_GetExtCalRecommendedInterval | Yes |
| niDCPower_GetLCRCompensationLastDateAndTime | Yes |
| niDCPower_GetLCRCompensationData | Yes |
| niDCPower_GetLCRCustomCableCompensationData | Yes |
| niDCPower_GetNextCoercionRecord | Yes |
| niDCPower_GetNextInterchangeWarning | Yes |
| niDCPower_GetSelfCalLastDateAndTime | Yes |
| niDCPower_GetSelfCalLastTemp | Yes |
| niDCPower_ImportAttributeConfigurationBuffer | Yes |
| niDCPower_ImportAttributeConfigurationFile | Yes |
| niDCPower_InitExtCal | Yes |
| niDCPower_InitializeWithIndependentChannels | Yes |
| niDCPower_InitiateWithChannels | Yes |
| niDCPower_Measure | Yes |
| niDCPower_MeasureMultiple | Yes |
| niDCPower_MeasureMultipleLCR | Yes |
| niDCPower_PerformLCRLoadCompensation | Yes |
| niDCPower_PerformLCROpenCompensation | Yes |
| niDCPower_PerformLCROpenCustomCableCompensation | Yes |
| niDCPower_PerformLCRShortCompensation | Yes |
| niDCPower_PerformLCRShortCustomCableCompensation | Yes |
| niDCPower_QueryInCompliance | Yes |
| niDCPower_QueryLatchedOutputCutoffState | X |
| niDCPower_QueryMaxCurrentLimit | Yes |
| niDCPower_QueryMaxVoltageLevel | Yes |
| niDCPower_QueryMinCurrentLimit | Yes |
| niDCPower_QueryOutputState | Yes |
| niDCPower_ReadCurrentTemperature | Yes |
| niDCPower_ResetWithChannels | Yes |
| niDCPower_ResetDevice | Yes |
| niDCPower_ResetInterchangeCheck | Yes |
| niDCPower_ResetWithDefaults | Yes |
| niDCPower_revision_query | Yes |
| niDCPower_self_test | Yes |
| niDCPower_SendSoftwareEdgeTriggerWithChannels | Yes |
| niDCPower_SetAttributeViBoolean | Yes |
| niDCPower_SetAttributeViInt32 | Yes |
| niDCPower_SetAttributeViReal64 | Yes |
| niDCPower_SetAttributeViSession | Yes |
| niDCPower_SetAttributeViString | Yes |
| niDCPower_SetCalUserDefinedInfo | Yes |
| niDCPower_SetSequence | Yes9 |
| niDCPower_WaitForEventWithChannels | Yes3 |

Note

Not all footnotes apply; refer only to those footnotes for which a number appears in the table

<sup>1</sup> The default value is TRUE if you use the [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) function to open the session, otherwise the default value is FALSE.

<sup>2</sup> Channel 0.

<sup>3</sup> NIDCPOWER_VAL_REMOTE is the only valid value.

<sup>4</sup> Channel 1.

<sup>5</sup> Software timed.

<sup>6</sup> The default value for channel 1 is NIDCPOWER_VAL_LOW.

<sup>7</sup> Default depends on the setting of the [NIDCPOWER_ATTR_SOURCE_MODE](group____root__nidcpower__attributes__source_1gab03ff2e7c99610450628a8eb953fb2dd.html) attribute. The default is NIDCPOWER_VAL_ON_DEMAND if the source mode is set to single point, or the default is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE if the source mode is set to sequence.

<sup>8</sup> NIDCPOWER_VAL_AUXILIARY is the only valid value.

<sup>9</sup> This function is supported only if [NIDCPOWER_ATTR_INSTRUMENT_MODE](group____root__nidcpower__attributes__lcr_1ga17947a3a27fe77395d64a095bf87e59b.html) attribute is set to NIDCPOWER_VAL_SMU_PS.

Parent topic:

Supported Functions by Device

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions.html language=enus -->
## TOPIC 00131: Functions

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsObsoleted FunctionsUnsupported FunctionsGroup membersNoneAttachmentsNone

### Functions

#### Groups

- Obsoleted Functions
- Unsupported Functions

#### Group members

None

#### Attachments

None

Parent topic:

nidcpowerObsolete.h

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__obsoleted__functions.html language=enus -->
## TOPIC 00132: Obsoleted Functions

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__obsoleted__functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__obsoleted__functions.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDCPower_ConfigureLCRCustomCableCompensationThis function is deprecated, use niDCPower_ConfigureLCRCompensation instead. niDCPower_ConfigureOutputRangeConfigures either the voltage level range or the current limit range. If range type is Voltage, the voltage le

### Obsoleted Functions

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDCPower_ConfigureLCRCustomCableCompensation | This function is deprecated, use niDCPower_ConfigureLCRCompensation instead. |
| niDCPower_ConfigureOutputRange | Configures either the voltage level range or the current limit range. If range type is Voltage, the voltage level range is configured. If range type is Current, the current limit range is configured. |
| niDCPower_GetLCRCustomCableCompensationData | This function is deprecated, use niDCPower_GetLCRCompensationData instead. |
| niDCPower_InitWithOptions | This function is deprecated. Use niDCPower_InitializeWithIndependentChannels instead. |
| niDCPower_init | This function is deprecated. Use niDCPower_InitializeWithIndependentChannels instead. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga449936eac91f6cb9bf844754dcf7e7c7.html language=enus -->
## TOPIC 00133: niDCPower_init

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga449936eac91f6cb9bf844754dcf7e7c7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga449936eac91f6cb9bf844754dcf7e7c7.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_InitializeWithIndependentChannels instead. SyntaxViStatus _VI_FUNC niDCPower_init(ViRsrc resourceName, ViBoolean idQuery, ViBoolean resetDevice, ViSession *vi)RemarksCreates a new IVI instrument driver session to the device specified in resourceName and ret

### niDCPower_init

This function is deprecated. Use [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_init(ViRsrc resourceName, ViBoolean idQuery, ViBoolean resetDevice, ViSession *vi)

#### Remarks

Creates a new IVI instrument driver session to the device specified in **resourceName** and returns a session handle you use to identify the device in all subsequent NI-DCPower function calls. This function also sends initialization commands to set the device to the state necessary for the operation of NI-DCPower.

To place the device in a known start-up state when creating a new session, set **resetDevice** to VI_TRUE. This action is equivalent to using the [niDCPower_reset](group____root__nidcpower__functions__utility_1ga9bc5fab751a72d72667b9716b4c3c7bd.html) function.

To open a session and leave the device in its existing configuration without passing through a transitional output state, set **resetDevice** to VI_FALSE, and immediately call the [niDCPower_Abort](group____root__nidcpower__functions__control_1gaab94ff0b35999f35ec28b51a97e5c156.html) function. Then configure the device as in the previous session, changing only the desired settings, and then call the [niDCPower_Initiate](group____root__nidcpower__functions__control_1gae9bf18cbfd1cacb74348612e260e5fb5.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| resourceName | [in] | ViRsrc | Specifies the resourceName assigned by Measurement & Automation Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an instrument's resourceName. resourceName can also be a logical IVI name. |
| idQuery | [in] | ViBoolean | Specifies whether the device is queried to determine if the device is a valid instrument for NI-DCPower.Defined Values:VI_TRUE (1)Perform ID query.VI_FALSE (0)Do not perform ID query. |
|  |  |  |  |
| VI_TRUE (1) | Perform ID query. |  |  |
| VI_FALSE (0) | Do not perform ID query. |  |  |
| resetDevice | [in] | ViBoolean | Specifies whether to reset the device during the initialization procedure.Defined Values:VI_TRUE (1)Reset the device.VI_FALSE (0)Do not reset the device. |
|  |  |  |  |
| VI_TRUE (1) | Reset the device. |  |  |
| VI_FALSE (0) | Do not reset the device. |  |  |
| vi | [out] | ViSession * | Returns a session handle that you use to identify the session in all subsequent NI-DCPower function calls. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsoleted Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga63bcd4e0349cf1d0d74c04876cbd9533.html language=enus -->
## TOPIC 00134: niDCPower_ConfigureOutputRange

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga63bcd4e0349cf1d0d74c04876cbd9533.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga63bcd4e0349cf1d0d74c04876cbd9533.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures either the voltage level range or the current limit range. If range type is Voltage, the voltage level range is configured. If range type is Current, the current limit range is configured. SyntaxViStatus _VI_FUNC niDCPower_ConfigureOutputRange(ViSession vi, ViConstString channelName, ViIn

### niDCPower_ConfigureOutputRange

Configures either the voltage level range or the current limit range. If **range type** is Voltage, the voltage level range is configured. If **range type** is Current, the current limit range is configured.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureOutputRange(ViSession vi, ViConstString channelName, ViInt32 rangeType, ViReal64 range)

#### Remarks

This function does not configure any of the DC Current output function settings. Refer to the [niDCPower_ConfigureOutputFunction](group____root__nidcpower__functions__source_1ga43b3e28d30812580498d1c4a2c1f5c60.html) function for more information.

This is a deprecated function. You must use the following functions instead of theniDCPower_ConfigureOutputRange function:

- [niDCPower_ConfigureVoltageLevel](group____root__nidcpower__functions__source__dc__voltage_1ga7ffb491b416b3b63baf987ebcfd8bc93.html)
- [niDCPower_ConfigureVoltageLimit](group____root__nidcpower__functions__source__dc__current_1ga80a35e9e40486359f0964dce15c89e91.html)
- [niDCPower_ConfigureCurrentLevel](group____root__nidcpower__functions__source__dc__current_1ga6744316a35dbd33f4e7bada0af72c58e.html)
- [niDCPower_ConfigureCurrentLimit](group____root__nidcpower__functions__source__dc__voltage_1gac7cf3668bb028dee399d4f04f29c25ab.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| rangeType | [in] | ViInt32 | Specifies the type of the range: voltage or current.Defined Values:NameValueDescriptionNIDCPOWER_VAL_RANGE_CURRENT0 (0x0)NI-DCPower configures the current range.NIDCPOWER_VAL_RANGE_VOLTAGE1 (0x1)NI-DCPower configures the voltage range. |
| Name | Value | Description |  |
| NIDCPOWER_VAL_RANGE_CURRENT | 0 (0x0) | NI-DCPower configures the current range. |  |
| NIDCPOWER_VAL_RANGE_VOLTAGE | 1 (0x1) | NI-DCPower configures the voltage range. |  |
| range | [in] | ViReal64 | Specifies the range to calibrate with these settings. Only one channel at a time may be calibrated. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsoleted Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga9458db72da6d196ff74c7415df1a9987.html language=enus -->
## TOPIC 00135: niDCPower_GetLCRCustomCableCompensationData

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga9458db72da6d196ff74c7415df1a9987.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga9458db72da6d196ff74c7415df1a9987.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated, use niDCPower_GetLCRCompensationData instead. SyntaxViStatus _VI_FUNC niDCPower_GetLCRCustomCableCompensationData(ViSession vi, ViConstString channelName, ViInt32 customCableCompensationDataSize, ViAddr customCableCompensationData)RemarksCollects previously generated ope

### niDCPower_GetLCRCustomCableCompensationData

This function is deprecated, use [niDCPower_GetLCRCompensationData](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga69ad9d2d281c7c38d2f2912721d395b0.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_GetLCRCustomCableCompensationData(ViSession vi, ViConstString channelName, ViInt32 customCableCompensationDataSize, ViAddr customCableCompensationData)

#### Remarks

Collects previously generated open and short custom cable compensation data so you can then apply it to LCR measurements with [niDCPower_ConfigureLCRCustomCableCompensation](group____root__nidcpower_obsolete__functions__obsoleted__functions_1gab26e6d4e41e91661f184dca3c713a825.html).

Call this function after you have obtained open and short custom cable compensation data. Pass the **custom cable compensation data** to [niDCPower_ConfigureLCRCustomCableCompensation](group____root__nidcpower_obsolete__functions__obsoleted__functions_1gab26e6d4e41e91661f184dca3c713a825.html).

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| customCableCompensationDataSize | [in] | ViInt32 | Specifies the size, in bytes, of customCableCompensationData to retrieve. If you enter 0, this function returns the needed size. |
| customCableCompensationData | [out] | ViAddr | The open and short custom cable compensation data to retrieve. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsoleted Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__obsoleted__functions_1gab26e6d4e41e91661f184dca3c713a825.html language=enus -->
## TOPIC 00136: niDCPower_ConfigureLCRCustomCableCompensation

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__obsoleted__functions_1gab26e6d4e41e91661f184dca3c713a825.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__obsoleted__functions_1gab26e6d4e41e91661f184dca3c713a825.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated, use niDCPower_ConfigureLCRCompensation instead. SyntaxViStatus _VI_FUNC niDCPower_ConfigureLCRCustomCableCompensation(ViSession vi, ViConstString channelName, ViInt32 customCableCompensationDataSize, ViAddr customCableCompensationData)RemarksApplies previously generated

### niDCPower_ConfigureLCRCustomCableCompensation

This function is deprecated, use [niDCPower_ConfigureLCRCompensation](group____root__nidcpower__functions__calibration__lcr__compensation_1ga84f15819403db31fbc82e7cb0dd1bba6.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_ConfigureLCRCustomCableCompensation(ViSession vi, ViConstString channelName, ViInt32 customCableCompensationDataSize, ViAddr customCableCompensationData)

#### Remarks

Applies previously generated open and short custom cable compensation data to LCR measurements.

This function applies custom cable compensation data when you have set [NIDCPOWER_ATTR_CABLE_LENGTH](group____root__nidcpower__attributes__device__specific__lcr_1gab854b2ef8812ccb9cf98b2725f92410c.html) to **NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED**.

Call this function after you have obtained custom cable compensation data. If [NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED](group____root__nidcpower__attributes__lcr__compensation_1ga3037309c86c1fca4678d86a5eec85b25.html) is set to true, you must generate data with both [niDCPower_PerformLCROpenCustomCableCompensation](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga8271e1c061151198faf4210d92a6c8c2.html) and [niDCPower_PerformLCRShortCustomCableCompensation](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga0a626105e3ffa7f72d3299bd3c9d66ae.html); if false, you must only use [niDCPower_PerformLCROpenCustomCableCompensation](group____root__nidcpower__functions__calibration__lcr__compensation__lcr__custom__cable__compensation_1ga8271e1c061151198faf4210d92a6c8c2.html), and NI-DCPower uses default short data.

Call [niDCPower_GetLCRCustomCableCompensationData](group____root__nidcpower_obsolete__functions__obsoleted__functions_1ga9458db72da6d196ff74c7415df1a9987.html) and pass the **custom cable compensation data** to this function.

Note

This function is not supported on all devices. Refer to [Supported Functions by Device](/csh?context=nidcpower_nidcpowercref_groups_supported_functions_by_device) for more information about supported devices.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |
| customCableCompensationDataSize | [in] | ViInt32 | Specifies the size, in bytes, of customCableCompensationData to apply. |
| customCableCompensationData | [in] | ViAddr | The open and short custom cable compensation data to apply. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsoleted Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__obsoleted__functions_1gad980955d10bbc713b9acd58bb06bab1c.html language=enus -->
## TOPIC 00137: niDCPower_InitWithOptions

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__obsoleted__functions_1gad980955d10bbc713b9acd58bb06bab1c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__obsoleted__functions_1gad980955d10bbc713b9acd58bb06bab1c.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Use niDCPower_InitializeWithIndependentChannels instead. SyntaxViStatus _VI_FUNC niDCPower_InitWithOptions(ViRsrc resourceName, ViBoolean idQuery, ViBoolean resetDevice, ViConstString optionString, ViSession *vi)RemarksCreates a new IVI instrument driver session to the d

### niDCPower_InitWithOptions

This function is deprecated. Use [niDCPower_InitializeWithIndependentChannels](group____root__nidcpower__functions__initializeclose_1gae218d41f401f3eef9841e5fb7279d9ee.html) instead.

#### Syntax

ViStatus _VI_FUNC niDCPower_InitWithOptions(ViRsrc resourceName, ViBoolean idQuery, ViBoolean resetDevice, ViConstString optionString, ViSession *vi)

#### Remarks

Creates a new IVI instrument driver session to the device specified in **resourceName** and returns a session handle you use to identify the device in all subsequent NI-DCPower function calls. With this function, you can optionally set the initial state of the following session attributes:

- [NIDCPOWER_ATTR_SIMULATE](group____root__nidcpower__attributes__inherent__ivi__attributes__user__options_1gaba7f65e1f3698427f21462caedc7ff6a.html)
- [NIDCPOWER_ATTR_DRIVER_SETUP](group____root__nidcpower__attributes__inherent__ivi__attributes__advanced__session__information_1gae335f5a897c736c25156389b70ca15d5.html)
- [NIDCPOWER_ATTR_RANGE_CHECK](group____root__nidcpower__attributes__inherent__ivi__attributes__user__options_1ga107a3ee116ba9c37eb8830e6e8010fa8.html)
- [NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS](group____root__nidcpower__attributes__inherent__ivi__attributes__user__options_1ga51d42097ae144af71fbcdbe7898f5299.html)
- [NIDCPOWER_ATTR_CACHE](group____root__nidcpower__attributes__inherent__ivi__attributes__user__options_1ga021af282d59a75636f95b092e4b3c8e7.html)
- [NIDCPOWER_ATTR_RECORD_COERCIONS](group____root__nidcpower__attributes__inherent__ivi__attributes__user__options_1ga408209a9aed784d4a51808ce9a4399b6.html)

This function also sends initialization commands to set the device to the state necessary for NI-DCPower to operate.

To place the device in a known start-up state when creating a new session, set **resetDevice** to VI_TRUE. This action is equivalent to using the [niDCPower_reset](group____root__nidcpower__functions__utility_1ga9bc5fab751a72d72667b9716b4c3c7bd.html) function.

To open a session and leave the device in its existing configuration without passing through a transitional output state, set **resetDevice** to VI_FALSE, and immediately call the [niDCPower_Abort](group____root__nidcpower__functions__control_1gaab94ff0b35999f35ec28b51a97e5c156.html) function. Then configure the device as in the previous session changing only the desired settings, and then call the [niDCPower_Initiate](group____root__nidcpower__functions__control_1gae9bf18cbfd1cacb74348612e260e5fb5.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| resourceName | [in] | ViRsrc | Specifies the resourceName assigned by Measurement & Automation Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an instrument's resourceName. resourceName can also be a logical IVI name. |
| idQuery | [in] | ViBoolean | Specifies whether the device is queried to determine if the device is a valid instrument for NI-DCPower. |
| resetDevice | [in] | ViBoolean | Specifies whether to reset the device during the initialization procedure. |
| optionString | [in] | ViConstString | Specifies the initial value of certain attributes for the session. The syntax for optionString is a list of attributes with an assigned value where 1 is VI_TRUE and 0 is VI_FALSE. Each attribute/value combination is delimited with a comma, as shown in the following example:"Simulate=0,RangeCheck=1,QueryInstrStatus=0,Cache=1"If you do not wire this input or pass an empty string, the session assigns the default values, shown in the example, for these attributes. You do not have to specify a value for all the attributes. If you do not specify a value for an attribute, the default value is used.For more information about simulating a device, refer to Simulating an Instrument. |
| vi | [out] | ViSession * | Returns a handle that you use to identify the device in all subsequent NI-DCPower function calls. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsoleted Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__unsupported__functions.html language=enus -->
## TOPIC 00138: Unsupported Functions

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__unsupported__functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__unsupported__functions.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDCPower_CalAdjustACImpedanceReferenceThis function is deprecated. Do not use this function. niDCPower_ResetOutputProtectionClears all output-protection conditions on the power supply. AttachmentsNone

### Unsupported Functions

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDCPower_CalAdjustACImpedanceReference | This function is deprecated. Do not use this function. |
| niDCPower_ResetOutputProtection | Clears all output-protection conditions on the power supply. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__unsupported__functions_1gaa78a439d94bf873b7f06bcf2b81862d8.html language=enus -->
## TOPIC 00139: niDCPower_CalAdjustACImpedanceReference

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__unsupported__functions_1gaa78a439d94bf873b7f06bcf2b81862d8.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__unsupported__functions_1gaa78a439d94bf873b7f06bcf2b81862d8.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This function is deprecated. Do not use this function. SyntaxViStatus _VI_FUNC niDCPower_CalAdjustACImpedanceReference(ViSession vi, ViConstString channelName, ViReal64 actualResistance, ViInt32 cableLength)ParametersNameDirectionTypeDescriptionvi[in]ViSessionDeprecated. channelName[in]ViConstString

### niDCPower_CalAdjustACImpedanceReference

This function is deprecated. Do not use this function.

#### Syntax

ViStatus _VI_FUNC niDCPower_CalAdjustACImpedanceReference(ViSession vi, ViConstString channelName, ViReal64 actualResistance, ViInt32 cableLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Deprecated. |
| channelName | [in] | ViConstString | Deprecated. |
| actualResistance | [in] | ViReal64 | Deprecated. |
| cableLength | [in] | ViInt32 | Deprecated. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Unsupported Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group____root__nidcpower_obsolete__functions__unsupported__functions_1gaff31fb743126d2c81eff6c15a99af152.html language=enus -->
## TOPIC 00140: niDCPower_ResetOutputProtection

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group____root__nidcpower_obsolete__functions__unsupported__functions_1gaff31fb743126d2c81eff6c15a99af152.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group____root__nidcpower_obsolete__functions__unsupported__functions_1gaff31fb743126d2c81eff6c15a99af152.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all output-protection conditions on the power supply. SyntaxViStatus _VI_FUNC niDCPower_ResetOutputProtection(ViSession vi, ViConstString channelName)ParametersNameDirectionTypeDescriptionvi[in]ViSessionIdentifies a particular instrument session. vi is obtained from the niDCPower_InitializeWi

### niDCPower_ResetOutputProtection

Clears all output-protection conditions on the power supply.

#### Syntax

ViStatus _VI_FUNC niDCPower_ResetOutputProtection(ViSession vi, ViConstString channelName)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | Identifies a particular instrument session. vi is obtained from the niDCPower_InitializeWithIndependentChannels function. |
| channelName | [in] | ViConstString | Specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels.If you pass "" for this control, all channels in the session are used. |

#### Returns

Reports the status of this operation. To obtain a text description of the status code, call [niDCPower_error_message](group____root__nidcpower__functions__utility__error__info_1ga43890f42cc20fed2bb8167bb2153519d.html). To obtain additional information concerning the error condition, call [niDCPower_GetError](group____root__nidcpower__functions__utility__error__info_1ga2212c88e92a73522b4583110225360a4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Unsupported Functions

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group__root__nidcpower.html language=enus -->
## TOPIC 00141: nidcpower.h

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group__root__nidcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group__root__nidcpower.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### nidcpower.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None

<!--NI_TOPIC bundle=ni-dcpower-c-api-ref path=group__root__nidcpower_obsolete.html language=enus -->
## TOPIC 00142: nidcpowerObsolete.h

- bundle_id: `ni-dcpower-c-api-ref`
- source_path: `group__root__nidcpower_obsolete.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-c-api-ref/raw/resource/enus/group__root__nidcpower_obsolete.html
- document_id: `ni-dcpower-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsFunctionsGroup membersNoneAttachmentsNone

### nidcpowerObsolete.h

#### Groups

- Functions

#### Group members

None

#### Attachments

None
