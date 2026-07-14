# NI DOCUMENT BUNDLE: ni-switch-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-switch-c-api-ref start=1 end=106 -->
<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_abortscan.html language=enus -->
## TOPIC 00001: niSwitch_AbortScan

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_abortscan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_abortscan.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_AbortScan

#### IviSwtchScanner Capability Group

#### C Function Prototype

ViStatus niSwitch_AbortScan (ViSession vi);

#### Purpose

Aborts the scan in progress. The switch module returns to the state it was in before the scan was initiated. 
 
Initiate a scan with [niSwitch_InitiateScan](c_nisw_initiatescan.html). 
 
If the switch module is not scanning, the NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- niSwitch Properties
- Scanning
- Writing a Software Trigger Scanning Program

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_analogbussharingenable.html language=enus -->
## TOPIC 00002: NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_analogbussharingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_analogbussharingenable.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150018 | ViBoolean | RW | N/A | None | None |

#### Description

Enables or disables sharing of an analog bus line so that multiple NI SwitchBlock devices may connect to it simultaneously. To enable multiple NI SwitchBlock devices to share an analog bus line, set this attribute to VI_TRUE for each device on the channel that corresponds with the shared analog bus line. The default value for all devices is VI_FALSE, which disables sharing of the analog bus.

Refer to [Using the Analog Bus on an NI SwitchBlock Carrier](/csh?topicname=switch/switchblock_analog_bus_reservation.html) for more information about sharing the analog bus.

#### Related Information

- Using the Analog Bus on an NI SwitchBlock Carrier
- Analog Bus Sharing Enable Property
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_bandwidth.html language=enus -->
## TOPIC 00003: NISWITCH_ATTR_BANDWIDTH

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_bandwidth.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_BANDWIDTH

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250005 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the bandwidth for the channel. 
 The units are hertz.

#### Related Information

- Bandwidth and Insertion Loss
- niSwitch Properties
- RF Switching Considerations

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_cablmodtrigbus.html language=enus -->
## TOPIC 00004: NISWITCH_ATTR_CABLED_MODULE_TRIGGER_BUS

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_cablmodtrigbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_cablmodtrigbus.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_CABLED_MODULE_TRIGGER_BUS

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150008 | ViInt32 | R/W | N/A | None | None |

#### Description

This attribute has been deprecated and may be removed from a future release of NI-SWITCH. Use the [niSwitch_RouteTriggerInput](c_nisw_routetriggerinput.html) function instead.

#### Defined Values:

[NISWITCH_VAL_NONE](c_nisw_val_none.html)

[NISWITCH_VAL_TTL0](c_nisw_val_ttl0.html)

[NISWITCH_VAL_TTL1](c_nisw_val_ttl1.html)

[NISWITCH_VAL_TTL2](c_nisw_val_ttl2.html)

[NISWITCH_VAL_TTL3](c_nisw_val_ttl3.html)

[NISWITCH_VAL_TTL4](c_nisw_val_ttl4.html)

[NISWITCH_VAL_TTL5](c_nisw_val_ttl5.html)

[NISWITCH_VAL_TTL6](c_nisw_val_ttl6.html)

[NISWITCH_VAL_TTL7](c_nisw_val_ttl7.html)

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_cache.html language=enus -->
## TOPIC 00005: NISWITCH_ATTR_CACHE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_cache.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_CACHE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050004 | ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether to cache the value of attributes. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. 
 The instrument driver can choose always to cache or never to cache particular attributes regardless of the setting of this attribute. 
 The default value is [VI_TRUE](c_vi_true.html). Use the [niSwitch_InitWithOptions](c_nisw_initwithoptions.html) function to override this value.

#### Defined Values:

[VI_TRUE](c_vi_true.html)

[VI_FALSE](c_vi_false.html)

#### Related Information

- niSwitch_InitWithOptions
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_digital_filter_enable.html language=enus -->
## TOPIC 00006: NISWITCH_ATTR_DIGITAL_FILTER_ENABLE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_digital_filter_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_digital_filter_enable.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_DIGITAL_FILTER_ENABLE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150016 | ViBoolean | RO | N/A | None | None |

#### Description

This attribute specifies whether to apply the pulse width filter to the Trigger Input. Set the property to TRUE to prevent the switch module from being triggered by pulses that are less than 150 ns on PXI trigger lines 0-7.

#### Defined Values:

[VI_TRUE](c_vi_true.html)

[VI_FALSE](c_vi_false.html)

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_group_capabil.html language=enus -->
## TOPIC 00007: NISWITCH_ATTR_GROUP_CAPABILITIES

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_group_capabil.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_group_capabil.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_GROUP_CAPABILITIES

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050401 | ViString | RO | N/A | None | None |

#### Description

A string that contains a comma-separated list of class-extension groups that this driver implements.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_instr_firm_rev.html language=enus -->
## TOPIC 00008: NISWITCH_ATTR_INSTRUMENT_FIRMWARE_REVISION

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_instr_firm_rev.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_instr_firm_rev.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_INSTRUMENT_FIRMWARE_REVISION

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050510 | ViString | RO | N/A | None | None |

#### Description

A string that contains the firmware revision information for the instrument you are currently using.

#### Related Information

- niSwitch Properties
- niSwitch_revision_query

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_instr_manuf.html language=enus -->
## TOPIC 00009: NISWITCH_ATTR_INSTRUMENT_MANUFACTURER

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_instr_manuf.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_instr_manuf.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_INSTRUMENT_MANUFACTURER

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050511 | ViString | RO | N/A | None | None |

#### Description

A string that contains the name of the instrument manufacturer you are currently using.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_instr_model.html language=enus -->
## TOPIC 00010: NISWITCH_ATTR_INSTRUMENT_MODEL

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_instr_model.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_instr_model.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_INSTRUMENT_MODEL

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050512 | ViString | RO | N/A | None | None |

#### Description

A string that contains the model number or name of the instrument that you are currently using.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_interchg_check.html language=enus -->
## TOPIC 00011: NISWITCH_ATTR_INTERCHANGE_CHECK

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_interchg_check.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_interchg_check.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_INTERCHANGE_CHECK

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050021 | ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether to perform interchangeability checking and retrieve interchangeability warnings when you call [niSwitch_Connect](c_nisw_connect.html), [niSwitch_SetPath](c_nisw_setpath.html) and [niSwitch_InitiateScan](c_nisw_initiatescan.html) functions. 
 
The default value is [VI_FALSE](c_vi_false.html). 
 
Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. call [niSwitch_GetNextInterchangeWarning](c_nisw_getnextinterchgwarn.html) to extract interchange warnings. Call the [niSwitch_ClearInterchangeWarnings](c_nisw_clearinterchgwarn.html) function to clear the list of interchangeability warnings without reading them. 
 
Interchangeability checking examines the attributes in a capability group only if you specify a value for at least one attribute within that group. Interchangeability warnings can occur when an attribute affects the behavior of the instrument and you have not set that attribute, or the attribute has been invalidated since you set it.

#### Defined Values:

[VI_TRUE](c_vi_true.html)

[VI_FALSE](c_vi_false.html)

#### Related Information

- niSwitch_GetNextInterchangeWarning
- niSwitch Properties
- niSwitch_ResetInterchangeCheck

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_io_resrc_desc.html language=enus -->
## TOPIC 00012: NISWITCH_ATTR_IO_RESOURCE_DESCRIPTOR

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_io_resrc_desc.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_io_resrc_desc.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_IO_RESOURCE_DESCRIPTOR

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050304 | ViString | RO | N/A | None | None |

#### Description

Indicates the resource descriptor the driver uses to identify the physical device. 
 If you initialize the driver with a logical name, this attribute contains the resource descriptor that corresponds to the entry in the IVI Configuration utility. 
 If you initialize the instrument driver with the resource descriptor, this attribute contains that value.

#### Related Information

- Initialization
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_max_ac_voltage.html language=enus -->
## TOPIC 00013: NISWITCH_ATTR_MAX_AC_VOLTAGE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_max_ac_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_max_ac_voltage.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_AC_VOLTAGE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250007 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum AC voltage the channel can switch. 
 The units are volts RMS.

#### Related Information

- General Switching Considerations
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_max_dc_voltage.html language=enus -->
## TOPIC 00014: NISWITCH_ATTR_MAX_DC_VOLTAGE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_max_dc_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_max_dc_voltage.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_DC_VOLTAGE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250006 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum DC voltage the channel can switch. 
 The units are volts.

#### Related Information

- General Switching Considerations
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_max_sw_ac_curr.html language=enus -->
## TOPIC 00015: NISWITCH_ATTR_MAX_SWITCHING_AC_CURRENT

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_max_sw_ac_curr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_max_sw_ac_curr.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_SWITCHING_AC_CURRENT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250009 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum AC current the channel can switch. 
 The units are amperes RMS.

#### Related Information

- niSwitch Properties
- Switching Current

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_max_sw_ac_pwr.html language=enus -->
## TOPIC 00016: NISWITCH_ATTR_MAX_SWITCHING_AC_POWER

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_max_sw_ac_pwr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_max_sw_ac_pwr.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_SWITCHING_AC_POWER

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250013 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum AC power the channel can switch. 
 The units are volt-amperes.

#### Related Information

- niSwitch Properties
- Switching Power

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_max_sw_dc_curr.html language=enus -->
## TOPIC 00017: NISWITCH_ATTR_MAX_SWITCHING_DC_CURRENT

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_max_sw_dc_curr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_max_sw_dc_curr.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_SWITCHING_DC_CURRENT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250008 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum DC current the channel can switch. 
 The units are amperes.

#### Related Information

- niSwitch Properties
- Switching Current

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_max_sw_dc_pwr.html language=enus -->
## TOPIC 00018: NISWITCH_ATTR_MAX_SWITCHING_DC_POWER

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_max_sw_dc_pwr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_max_sw_dc_pwr.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_SWITCHING_DC_POWER

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250012 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum DC power the channel can switch. 
 The units are watts.

#### Related Information

- niSwitch Properties
- Switching Power

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_mx_cary_ac_pwr.html language=enus -->
## TOPIC 00019: NISWITCH_ATTR_MAX_CARRY_AC_POWER

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_mx_cary_ac_pwr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_mx_cary_ac_pwr.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_CARRY_AC_POWER

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250015 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum AC power the channel can carry. 
 The units are volt-amperes.

#### Related Information

- General Switching Considerations
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_mxcarryac_curr.html language=enus -->
## TOPIC 00020: NISWITCH_ATTR_MAX_CARRY_AC_CURRENT

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_mxcarryac_curr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_mxcarryac_curr.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MAX_CARRY_AC_CURRENT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250011 | ViReal64 | RO | N/A | None | None |

#### Description

This channel-based attribute returns the maximum AC current the channel can carry. 
 The units are amperes RMS.

#### Related Information

- General Switching Considerations
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_num_of_relays.html language=enus -->
## TOPIC 00021: NISWITCH_ATTR_NUMBER_OF_RELAYS

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_num_of_relays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_num_of_relays.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_NUMBER_OF_RELAYS

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150014 | ViInt32 | RO | N/A | None | None |

#### Description

This attribute returns the number of relays.

#### Related Information

- niSwitch Get Relay Name
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_scan_list.html language=enus -->
## TOPIC 00022: NISWITCH_ATTR_SCAN_LIST

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_scan_list.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_scan_list.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SCAN_LIST

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250020 | ViString | R/W | N/A | None | None |

#### Description

This attribute contains a [scan list](/csh?topicname=switch/scan_list.html)—a string that specifies channel connections and trigger conditions. The [niSwitch_InitiateScan](c_nisw_initiatescan.html) function makes or breaks connections and waits for triggers according to the instructions in the scan list. A scan list is comprised of channel names that you separate with special characters. These special characters determine the operations the scanner performs on the channels when it executes this scan list.

- To create a path between two channels, use the following character between the two channel names: -> (a dash followed by a '>' sign) Example: \CH1->CH2\ tells the switch to make a path from channel CH1 to channel CH2.
- To break or clear a path, use the following character as a prefix before the path: ~ (tilde) Example: \~CH1->CH2\ tells the switch to break the path from channel CH1 to channel CH2.
- To tell the switch to wait for a trigger event, use the following character as a separator between paths: ; (semicolon) Example: \CH1->CH2;CH3->CH4\ tells the switch to make the path from channel CH1 to channel CH2, wait for a trigger, and then make the path from CH3 to CH4.
- To tell the switch module to create multiple paths as quickly as possible, use the & (ampersand) or && (double ampersand) as a separator between the paths. The & in 'CH0->CH1;CH2->CH3&CH4->CH5' instructs the scanner to make the path between channels CH0 and CH1, wait for a trigger, and then make the paths between channels CH2 and CH3 and between channels CH4 and CH5 in no particular order without waiting for settling or waiting for a trigger. If wait for settling is desired, replace & with &&. The && in 'CH0->CH1;CH2->CH3&&CH4->CH5' instructs the scanner to make the path between channels CH0 and CH1, wait for a trigger, and then make the path between channels CH2 and CH3, wait for settling, then make the path between channels CH4 and CH5.

Refer to [Scan Lists](/csh?topicname=switch/scan_list.html) for additional information.

#### Related Information

- niSwitch Properties
- Scan Lists
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_scan_mode.html language=enus -->
## TOPIC 00023: NISWITCH_ATTR_SCAN_MODE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_scan_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_scan_mode.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SCAN_MODE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250021 | ViInt32 | R/W | N/A | None | None |

#### Description

This attribute specifies what happens to existing connections that conflict with the connections you make in a scan list. For example, if CH1 is already connected to CH2 and the scan list instructs the switch to connect CH1 to CH3, this attribute specifies what happens to the connection between CH1 and CH2. 
 If the value of this attribute is NISWITCH_VAL_NONE, the switch takes no action on existing paths. If the value is NISWITCH_VAL_BREAK_BEFORE_MAKE, the switch breaks conflicting paths before making new ones. If the value is NISWITCH_VAL_BREAK_AFTER_MAKE, the switch breaks conflicting paths after making new ones. 
 Most switches support only one of the possible values. In such cases, this attribute serves as an indicator of the device's behavior.

#### Defined Values:

[NISWITCH_VAL_NONE](c_nisw_val_none.html)

[NISWITCH_VAL_BREAK_BEFORE_MAKE](c_nisw_val_break_before_mk.html)

[NISWITCH_VAL_BREAK_AFTER_MAKE](c_nisw_val_break_aftr_make.html)

#### Related Information

- niSwitch Properties
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_scn_adv_output.html language=enus -->
## TOPIC 00024: NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_scn_adv_output.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_scn_adv_output.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250023 | ViInt32 | R/W | N/A | None | None |

#### Description

This attribute specifies the method you want to use to notify another instrument that all signals going through the switch have settled following the processing of one entry in the scan list.

#### Defined Values:

[NISWITCH_VAL_NONE](c_nisw_val_none.html)

[NISWITCH_VAL_EXTERNAL](c_nisw_val_external.html)

[NISWITCH_VAL_TTL0](c_nisw_val_ttl0.html)

[NISWITCH_VAL_TTL1](c_nisw_val_ttl1.html)

[NISWITCH_VAL_TTL2](c_nisw_val_ttl2.html)

[NISWITCH_VAL_TTL3](c_nisw_val_ttl3.html)

[NISWITCH_VAL_TTL4](c_nisw_val_ttl4.html)

[NISWITCH_VAL_TTL5](c_nisw_val_ttl5.html)

[NISWITCH_VAL_TTL6](c_nisw_val_ttl6.html)

[NISWITCH_VAL_TTL7](c_nisw_val_ttl7.html)

[NISWITCH_VAL_PXI_STAR](c_nisw_val_pxistar.html)

[NISWITCH_VAL_REARCONNECTOR](c_nisw_val_rearconn.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE1](c_nisw_val_rearconn_mod1.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE2](c_nisw_val_rearconn_mod2.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE3](c_nisw_val_rearconn_mod3.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE4](c_nisw_val_rearconn_mod4.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE5](c_nisw_val_rearconn_mod5.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE6](c_nisw_val_rearconn_mod6.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE7](c_nisw_val_rearconn_mod7.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE8](c_nisw_val_rearconn_mod8.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE9](c_nisw_val_rearconn_mod9.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE10](c_nisw_val_rearconn_mod10.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE11](c_nisw_val_rearconn_mod11.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE12](c_nisw_val_rearconn_mod12.html)

[NISWITCH_VAL_FRONTCONNECTOR](c_nisw_val_frontconn.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE1](c_nisw_val_frontconn_mod1.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE2](c_nisw_val_frontconn_mod2.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE3](c_nisw_val_frontconn_mod3.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE4](c_nisw_val_frontconn_mod4.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE5](c_nisw_val_frontconn_mod5.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE6](c_nisw_val_frontconn_mod6.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE7](c_nisw_val_frontconn_mod7.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE8](c_nisw_val_frontconn_mod8.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE9](c_nisw_val_frontconn_mod9.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE10](c_nisw_val_frontconn_mod10.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE11](c_nisw_val_frontconn_mod11.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE12](c_nisw_val_frontconn_mod12.html)

|  | Notes (0) NISWITCH_VAL_NONE The switch does not produce a Scan Advanced Output trigger. (2) NISWITCH_VAL_EXTERNAL External Trigger. The switch produces the Scan Advanced Output trigger on the "trigger out" connector. (111) NISWITCH_VAL_TTL0 The switch produces the Scan Advanced Output on the SCXI or PXI_TRIG0 line. (112) NISWITCH_VAL_TTL1 The switch produces the Scan Advanced Output on the PXI_TRIG1 line. (113) NISWITCH_VAL_TTL2 The switch produces the Scan Advanced Output on the SCXI or PXI_TRIG2 line. (114) NISWITCH_VAL_TTL3 The switch produces the Scan Advanced Output on the PXI_TRIG3 line. (115) NISWITCH_VAL_TTL4 The switch produces the Scan Advanced Output on the PXI_TRIG4 line. (116) NISWITCH_VAL_TTL5 The switch produces the Scan Advanced Output on the PXI_TRIG5 line. (117) NISWITCH_VAL_TTL6 The switch produces the Scan Advanced Output on the PXI_TRIG6 line. (118) NISWITCH_VAL_TTL7 The switch produces the Scan Advanced Output on the PXI_TRIG7 line. (125) NISWITCH_VAL_PXI_STAR The switch produces the Scan Advanced Output on the PXI STAR trigger bus. (1001) NISWITCH_VAL_FRONTCONNECTOR This indicates that the switch will send its SCANNER ADVANCED output to the front connector. When using SCXI switches as scanners, all the devices that are part of the scanner will send their SCANNER ADVANCED output to their respective front connectors. |
| --- | --- |

#### Related Information

- niSwitch Properties
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_serial_number.html language=enus -->
## TOPIC 00025: NISWITCH_ATTR_SERIAL_NUMBER

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_serial_number.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_serial_number.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SERIAL_NUMBER

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150015 | ViString | RO | N/A | None | None |

#### Description

This read-only attribute returns the serial number for the switch controlled by NI-SWITCH. If the device does not return a serial number, NI-SWITCH returns the Invalid Attribute error.

#### Related Information

- Characteristic Impedance
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_settling_time.html language=enus -->
## TOPIC 00026: NISWITCH_ATTR_SETTLING_TIME

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_settling_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_settling_time.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SETTLING_TIME

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250004 | ViReal64 | R/W | N/A | None | None |

#### Description

This channel-based attribute returns the maximum length of time from after you make a connection until the signal flowing through the channel [settles](/csh?topicname=switch/settling_time.html). The units are seconds.

|  | Note PXI-2501/2503/2565/2590/2591 Users—the actual delay will always be the greater value of the settling time and the value you specify as the scan delay. |
| --- | --- |

#### Related Information

- niSwitch Properties
- Settling Time

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_simulate.html language=enus -->
## TOPIC 00027: NISWITCH_ATTR_SIMULATE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_simulate.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SIMULATE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050005 | ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not to simulate instrument driver I/O operations. If simulation is enabled, instrument driver functions perform range checking and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not perform instrument I/O. For output parameters that represent instrument data, the instrument driver functions return calculated values. 
 The default value is [VI_FALSE](c_vi_false.html). Use the [niSwitch_InitWithOptions](c_nisw_initwithoptions.html) function to override this value.

#### Defined Values:

[VI_TRUE](c_vi_true.html)

[VI_FALSE](c_vi_false.html)

#### Related Information

- niSwitch_InitWithOptions
- niSwitch Properties
- Simulating a Switch

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_spcdrvrspcmajv.html language=enus -->
## TOPIC 00028: NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_spcdrvrspcmajv.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_spcdrvrspcmajv.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050515 | ViInt32 | RO | N/A | None | None |

#### Description

The major version number of the IviSwtch class specification.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_spcdrvrspcminv.html language=enus -->
## TOPIC 00029: NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_spcdrvrspcminv.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_spcdrvrspcminv.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050516 | ViInt32 | RO | N/A | None | None |

#### Description

The minor version number of the class specification with which this driver is compliant.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_spec_drvr_desc.html language=enus -->
## TOPIC 00030: NISWITCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_spec_drvr_desc.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_spec_drvr_desc.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050514 | ViString | RO | N/A | None | None |

#### Description

A string that contains a brief description of the specific driver.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_spec_drvr_prfx.html language=enus -->
## TOPIC 00031: NISWITCH_ATTR_SPECIFIC_DRIVER_PREFIX

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_spec_drvr_prfx.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_spec_drvr_prfx.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SPECIFIC_DRIVER_PREFIX

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050302 | ViString | RO | N/A | None | None |

#### Description

A string that contains the prefix for the instrument driver. The name of each user-callable function in this driver starts with this prefix.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_spec_drvr_rev.html language=enus -->
## TOPIC 00032: NISWITCH_ATTR_SPECIFIC_DRIVER_REVISION

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_spec_drvr_rev.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_spec_drvr_rev.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SPECIFIC_DRIVER_REVISION

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050551 | ViString | RO | N/A | None | None |

#### Description

A string that contains additional version information about this instrument driver.

#### Related Information

- niSwitch Properties
- niSwitch_revision_query

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_spec_drvr_vndr.html language=enus -->
## TOPIC 00033: NISWITCH_ATTR_SPECIFIC_DRIVER_VENDOR

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_spec_drvr_vndr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_spec_drvr_vndr.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SPECIFIC_DRIVER_VENDOR

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050513 | ViString | RO | N/A | None | None |

#### Description

A string that contains the name of the vendor that supplies this driver.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_supp_instr_mdl.html language=enus -->
## TOPIC 00034: NISWITCH_ATTR_SUPPORTED_INSTRUMENT_MODELS

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_supp_instr_mdl.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_supp_instr_mdl.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_SUPPORTED_INSTRUMENT_MODELS

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1050327 | ViString | RO | N/A | None | None |

#### Description

Contains a comma-separated list of supported instrument models.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_temperature.html language=enus -->
## TOPIC 00035: NISWITCH_ATTR_TEMPERATURE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_temperature.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_TEMPERATURE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150019 | ViReal64 | RO | N/A | None | None |

#### Description

This attribute returns the temperature for the switch module. 
 The units are degrees Celsius.

#### Related Information

- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_trig_in_pol.html language=enus -->
## TOPIC 00036: NISWITCH_ATTR_TRIGGER_INPUT_POLARITY

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_trig_in_pol.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_trig_in_pol.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_TRIGGER_INPUT_POLARITY

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150010 | ViInt32 | R/W | N/A | None | None |

#### Description

Determines the behavior of the trigger input.

#### Defined Values:

[NISWITCH_VAL_RISING_EDGE](c_nisw_val_rising_edge.html)

[NISWITCH_VAL_FALLING_EDGE](c_nisw_val_falling_edge.html)

#### Related Information

- niSwitch Properties
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_trigger_input.html language=enus -->
## TOPIC 00037: NISWITCH_ATTR_TRIGGER_INPUT

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_trigger_input.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_trigger_input.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_TRIGGER_INPUT

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250022 | ViInt32 | R/W | N/A | None | None |

#### Description

This attribute specifies the source of the trigger for which the switch can wait when processing a scan list. The switch waits for a trigger when it encounters a semicolon in a scan list. When the trigger occurs, the switch advances to the next entry in the scan list.

#### Defined Values:

[NISWITCH_VAL_IMMEDIATE](c_nisw_val_immediate.html)

[NISWITCH_VAL_EXTERNAL](c_nisw_val_external.html)

[NISWITCH_VAL_SOFTWARE_TRIG](c_nisw_val_sw_trig_func.html)

[NISWITCH_VAL_TTL0](c_nisw_val_ttl0.html)

[NISWITCH_VAL_TTL1](c_nisw_val_ttl1.html)

[NISWITCH_VAL_TTL2](c_nisw_val_ttl2.html)

[NISWITCH_VAL_TTL3](c_nisw_val_ttl3.html)

[NISWITCH_VAL_TTL4](c_nisw_val_ttl4.html)

[NISWITCH_VAL_TTL5](c_nisw_val_ttl5.html)

[NISWITCH_VAL_TTL6](c_nisw_val_ttl6.html)

[NISWITCH_VAL_TTL7](c_nisw_val_ttl7.html)

[NISWITCH_VAL_PXI_STAR](c_nisw_val_pxi_star.html)

[NISWITCH_VAL_REARCONNECTOR](c_nisw_val_rearconn.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE1](c_nisw_val_rearconn_mod1.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE2](c_nisw_val_rearconn_mod2.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE3](c_nisw_val_rearconn_mod3.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE4](c_nisw_val_rearconn_mod4.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE5](c_nisw_val_rearconn_mod5.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE6](c_nisw_val_rearconn_mod6.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE7](c_nisw_val_rearconn_mod7.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE8](c_nisw_val_rearconn_mod8.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE9](c_nisw_val_rearconn_mod9.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE10](c_nisw_val_rearconn_mod10.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE11](c_nisw_val_rearconn_mod11.html)

[NISWITCH_VAL_REARCONNECTOR_MODULE12](c_nisw_val_rearconn_mod12.html)

[NISWITCH_VAL_FRONTCONNECTOR](c_nisw_val_frontconn.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE1](c_nisw_val_frontconn_mod1.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE2](c_nisw_val_frontconn_mod2.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE3](c_nisw_val_frontconn_mod3.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE4](c_nisw_val_frontconn_mod4.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE5](c_nisw_val_frontconn_mod5.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE6](c_nisw_val_frontconn_mod6.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE7](c_nisw_val_frontconn_mod7.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE8](c_nisw_val_frontconn_mod8.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE9](c_nisw_val_frontconn_mod9.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE10](c_nisw_val_frontconn_mod10.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE11](c_nisw_val_frontconn_mod11.html)

[NISWITCH_VAL_FRONTCONNECTOR_MODULE12](c_nisw_val_frontconn_mod12.html)

|  | Notes (1) NISWITCH_VAL_IMMEDIATE Immediate Trigger. The switch does not wait for a trigger before processing the next entry in the scan list. (2) NISWITCH_VAL_EXTERNAL External Trigger. The switch waits until it receives a trigger from an external source through the "trigger in" connector. (3) NISWITCH_VAL_SOFTWARE_TRIG The switch waits until you call the niSwitch_SendSWTrigger function. (111) NISWITCH_VAL_TTL0 The switch waits until it receives a trigger on the SCXI or PXI_TRIG0 line before processing the next entry in the scan list. (112) NISWITCH_VAL_TTL1 The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. (113) NISWITCH_VAL_TTL2 The switch waits until it receives a trigger on the SCXI or PXI_TRIG2 line before processing the next entry in the scan list. (114) NISWITCH_VAL_TTL3 The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. (115) NISWITCH_VAL_TTL4 The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. (116) NISWITCH_VAL_TTL5 The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. (117) NISWITCH_VAL_TTL6 The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. (118) NISWITCH_VAL_TTL7 The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list. (125) NISWITCH_VAL_PXI_STAR The switch waits until it receives a trigger on the PXI STAR trigger bus before processing the next entry in the scan list. (1000) NISWITCH_VAL_REARCONNECTOR The switch waits until it receives a trigger on the Rear connector before processing the next entry in the scan list. This value is valid for SCXI scanners that consist of a single device. If more than one device is used, you must use niSwitch_RouteTriggerInput or niSwitch_RouteScanAdvancedOutput functions to route a trigger from the connector on another module to one of the TTL lines instead. (1001) NISWITCH_VAL_FRONTCONNECTOR The switch waits until it receives a trigger on the front connector before processing the next entry in the scan list. When using SCXI scanners, this variable is valid for scanners that consist of a single device. If more than one device is used, you must use the niSwitch_RouteTriggerInput or niSwitch_RouteScanAdvancedOutput functions to route a trigger from the connector on another module to one of the TTL lines instead. |
| --- | --- |

#### Related Information

- niSwitch_ConfigureScanList
- niSwitch Properties
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_trigger_mode.html language=enus -->
## TOPIC 00038: NISWITCH_ATTR_TRIGGER_MODE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_trigger_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_trigger_mode.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_TRIGGER_MODE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150005 | ViInt32 | R/W | N/A | None | None |

#### Description

This attribute has been deprecated and may be removed from a future release of NI-SWITCH. Use the [niSwitch_RouteTriggerInput](c_nisw_routetriggerinput.html) and/or [niSwitch_RouteScanAdvancedOutput](c_nisw_routescanadvoutput.html) functions instead.

#### Defined Values:

[NISWITCH_VAL_SINGLE](c_nisw_val_single.html)

[NISWITCH_VAL_MASTER](c_nisw_val_master.html)

[NISWITCH_VAL_SLAVE](c_nisw_val_slave.html)

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_waiting_trig.html language=enus -->
## TOPIC 00039: NISWITCH_ATTR_IS_WAITING_FOR_TRIG

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_waiting_trig.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_waiting_trig.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_IS_WAITING_FOR_TRIG

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150004 | ViBoolean | RO | N/A | None | None |

#### Description

In a scan list, a semicolon (;) is used to indicate that at that point in the scan list, the scan engine should pause until a trigger is received from the trigger input. If that trigger is user generated through either a hardware pulse or the Send SW Trigger operation, it is necessary for the user to know when the scan engine has reached such a state.

#### Defined Values:

[VI_TRUE](c_vi_true.html)

[VI_FALSE](c_vi_false.html)

#### Related Information

- niSwitch_ConfigureScanList
- niSwitch Properties
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attr_wire_mode.html language=enus -->
## TOPIC 00040: NISWITCH_ATTR_WIRE_MODE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attr_wire_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attr_wire_mode.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_WIRE_MODE

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1250017 | ViInt32 | RO | N/A | None | None |

#### Description

This attribute returns the wire mode of the switch. 
 This attribute affects the values of the [NISWITCH_ATTR_NUM_OF_ROWS](c_nisw_attr_num_of_rows.html) and [NISWITCH_ATTR_NUM_OF_COLUMNS](c_nisw_attr_num_of_columns.html) attributes. The actual number of input and output lines on the switch is fixed, but the number of channels depends on how many lines constitute each channel.

#### Related Information

- N-Wire Switching Modes
- niSwitch Properties

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attrmstrslvscnadvb.html language=enus -->
## TOPIC 00041: NISWITCH_ATTR_MASTER_SLAVE_SCAN_ADVANCED_BUS

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attrmstrslvscnadvb.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attrmstrslvscnadvb.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_ATTR_MASTER_SLAVE_SCAN_ADVANCED_BUS

#### Specific Attribute

| Numeric Value | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| 1150007 | ViInt32 | R/W | N/A | None | None |

#### Description

This attribute has been deprecated and may be removed from a future release of NI-SWITCH. Use the [niSwitch_RouteScanAdvancedOutput](c_nisw_routescanadvoutput.html) function instead.

#### Defined Values:

[NISWITCH_VAL_NONE](c_nisw_val_none.html)

[NISWITCH_VAL_TTL0](c_nisw_val_ttl0.html)

[NISWITCH_VAL_TTL1](c_nisw_val_ttl1.html)

[NISWITCH_VAL_TTL2](c_nisw_val_ttl2.html)

[NISWITCH_VAL_TTL3](c_nisw_val_ttl3.html)

[NISWITCH_VAL_TTL4](c_nisw_val_ttl4.html)

[NISWITCH_VAL_TTL5](c_nisw_val_ttl5.html)

[NISWITCH_VAL_TTL6](c_nisw_val_ttl6.html)

[NISWITCH_VAL_TTL7](c_nisw_val_ttl7.html)

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_attrs.html language=enus -->
## TOPIC 00042: NI-SWITCH Attributes

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_attrs.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_attrs.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-SWITCH Attributes

| Group/Attribute Name | Attribute Label |
| --- | --- |
| Is Source Channel | NISWITCH_ATTR_IS_SOURCE_CHANNEL |
| Is Configuration Channel | NISWITCH_ATTR_IS_CONFIGURATION_CHANNEL |
| Analog Bus Sharing Enable | NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE |
| Module Characteristics |  |
| Serial Number | NISWITCH_ATTR_SERIAL_NUMBER |
| Is Debounced | NISWITCH_ATTR_IS_DEBOUNCED |
| Settling Time | NISWITCH_ATTR_SETTLING_TIME |
| Bandwidth | NISWITCH_ATTR_BANDWIDTH |
| Maximum DC Voltage | NISWITCH_ATTR_MAX_DC_VOLTAGE |
| Maximum AC Voltage | NISWITCH_ATTR_MAX_AC_VOLTAGE |
| Maximum Switching DC Current | NISWITCH_ATTR_MAX_SWITCHING_DC_CURRENT |
| Maximum Switching AC Current | NISWITCH_ATTR_MAX_SWITCHING_AC_CURRENT |
| Maximum Carry DC Current | NISWITCH_ATTR_MAX_CARRY_DC_CURRENT |
| Maximum Carry AC Current | NISWITCH_ATTR_MAX_CARRY_AC_CURRENT |
| Maximum Switching DC Power | NISWITCH_ATTR_MAX_SWITCHING_DC_POWER |
| Maximum Switching AC Power | NISWITCH_ATTR_MAX_SWITCHING_AC_POWER |
| Maximum Carry DC Power | NISWITCH_ATTR_MAX_CARRY_DC_POWER |
| Maximum Carry AC Power | NISWITCH_ATTR_MAX_CARRY_AC_POWER |
| Characteristic Impedance | NISWITCH_ATTR_CHARACTERISTIC_IMPEDANCE |
| Wire mode | NISWITCH_ATTR_WIRE_MODE |
| Temperature | NISWITCH_ATTR_TEMPERATURE |
| Number of Relays | NISWITCH_ATTR_NUMBER_OF_RELAYS |
| Scanning Configuration |  |
| Scan List | NISWITCH_ATTR_SCAN_LIST |
| Scan Mode | NISWITCH_ATTR_SCAN_MODE |
| Continuous Scan | NISWITCH_ATTR_CONTINUOUS_SCAN |
| Trigger Input | NISWITCH_ATTR_TRIGGER_INPUT |
| Scan Advanced Output | NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT |
| Is Scanning | NISWITCH_ATTR_IS_SCANNING |
| Is Waiting for Trigger? | NISWITCH_ATTR_IS_WAITING_FOR_TRIG |
| Scan Delay | NISWITCH_ATTR_SCAN_DELAY |
| Trigger Input Polarity | NISWITCH_ATTR_TRIGGER_INPUT_POLARITY |
| Scan Advanced Polarity | NISWITCH_ATTR_SCAN_ADVANCED_POLARITY |
| Handshaking Initiation | NISWITCH_ATTR_HANDSHAKING_INITIATION |
| Matrix Configuration |  |
| Number of Rows | NISWITCH_ATTR_NUM_OF_ROWS |
| Number of Columns | NISWITCH_ATTR_NUM_OF_COLUMNS |
| Obsolete Attributes |  |
| Cabled Module Scan Advanced Bus | NISWITCH_ATTR_CABLED_MODULE_SCAN_ADVANCED_BUS |
| Cabled Module Trigger Bus | NISWITCH_ATTR_CABLED_MODULE_TRIGGER_BUS |
| Master Slave Scan Advanced Bus | NISWITCH_ATTR_MASTER_SLAVE_SCAN_ADVANCED_BUS |
| Master Slave Trigger Bus | NISWITCH_ATTR_MASTER_SLAVE_TRIGGER_BUS |
| Parsed Scan List | NISWITCH_ATTR_PARSED_SCAN_LIST |
| Trigger Mode | NISWITCH_ATTR_TRIGGER_MODE |

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_canconnect.html language=enus -->
## TOPIC 00043: niSwitch_CanConnect

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_canconnect.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_canconnect.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_CanConnect

#### IviSwtchBase Capability Group

#### C Function Prototype

ViStatus niSwitch_CanConnect (ViSession vi, ViConstString channel1, ViConstString channel2, ViInt32* pathCapability);

#### Purpose

Verifies that a path between **channel1** and **channel2** can be created.

If a path is possible in the switch module, the availability of that path is returned given the existing connections. If the path is possible but in use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is returned.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channel1 | ViConstString | Input one of the channel names of the desired path. Pass the other channel name as the channel2. Refer to Devices for valid channel names for the switch module. Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp The default value is an empty string. |
| channel2 | ViConstString | Input one of the channel names of the desired path. Pass the other channel name as channel1. Refer to Devices for valid channel names for the switch module. Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp The default value is an empty string. |
| pathCapability | ViInt32 | Indicates whether a path is valid. Possible values include: Value Description NISWITCH_VAL_PATH_AVAILABLE Indicates that NI-SWITCH can create the path at this time. NISWITCH_VAL_PATH_EXISTS Indicates that the path already exists. NISWITCH_VAL_PATH_UNSUPPORTED Indicates that the instrument is not capable of creating a path between the channels you specify. NISWITCH_VAL_RSRC_IN_USE Indicates that although the path is valid, NI-SWITCH cannot create the path at this moment because the switch is currently using one or more of the required channels to create another path. You must destroy the other path before creating this one. NISWITCH_VAL_SOURCE_CONFLICT Indicates that the instrument cannot create a path because both channels are connected to different source channels. NISWITCH_VAL_CHANNEL_NOT_AVAILABLE Indicates that NI-SWITCH cannot create a path between the two channels because one of the channels is a configuration channel and unavailable for external connections. |
| Value | Description |  |
| NISWITCH_VAL_PATH_AVAILABLE | Indicates that NI-SWITCH can create the path at this time. |  |
| NISWITCH_VAL_PATH_EXISTS | Indicates that the path already exists. |  |
| NISWITCH_VAL_PATH_UNSUPPORTED | Indicates that the instrument is not capable of creating a path between the channels you specify. |  |
| NISWITCH_VAL_RSRC_IN_USE | Indicates that although the path is valid, NI-SWITCH cannot create the path at this moment because the switch is currently using one or more of the required channels to create another path. You must destroy the other path before creating this one. |  |
| NISWITCH_VAL_SOURCE_CONFLICT | Indicates that the instrument cannot create a path because both channels are connected to different source channels. |  |
| NISWITCH_VAL_CHANNEL_NOT_AVAILABLE | Indicates that NI-SWITCH cannot create a path between the two channels because one of the channels is a configuration channel and unavailable for external connections. |  |

#### Related Information

- niSwitch_GetPath

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_checkattrviboolean.html language=enus -->
## TOPIC 00044: niSwitch_CheckAttributeViBoolean

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_checkattrviboolean.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_checkattrviboolean.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_CheckAttributeViBoolean

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_CheckAttributeViBoolean (ViSession vi, ViConstString channelName, ViAttr attributeID, ViBoolean attributeValue);

#### Purpose

Checks the validity of a value you specify for a ViBoolean attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. Read-only attributes appear dim in the list box. If you select a read-only attribute, an error message appears. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViBoolean type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViBoolean | Pass the value which you want to verify as a valid value for the attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. Note Some of the values might not be valid depending on the current settings of the instrument session. |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_checkattrviint32.html language=enus -->
## TOPIC 00045: niSwitch_CheckAttributeViInt32

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_checkattrviint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_checkattrviint32.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_CheckAttributeViInt32

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_CheckAttributeViInt32 (ViSession vi, ViConstString channelName, ViAttr attributeID, ViInt32 attributeValue);

#### Purpose

Checks the validity of a value you specify for a ViInt32 attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. Read-only attributes appear dim in the list box. If you select a read-only attribute, an error message appears. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViInt32 type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViInt32 | Pass the value which you want to verify as a valid value for the attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. Note Some of the values might not be valid depending on the current settings of the instrument session. |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_checkattrvireal64.html language=enus -->
## TOPIC 00046: niSwitch_CheckAttributeViReal64

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_checkattrvireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_checkattrvireal64.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_CheckAttributeViReal64

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_CheckAttributeViReal64 (ViSession vi, ViConstString channelName, ViAttr attributeID, ViReal64 attributeValue);

#### Purpose

Checks the validity of a value you specify for a ViReal64 attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. Read-only attributes appear dim in the list box. If you select a read-only attribute, an error message appears. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViReal64 type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViReal64 | Pass the value which you want to verify as a valid value for the attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. Note Some of the values might not be valid depending on the current settings of the instrument session. |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_checkattrvisession.html language=enus -->
## TOPIC 00047: niSwitch_CheckAttributeViSession

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_checkattrvisession.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_checkattrvisession.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_CheckAttributeViSession

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_CheckAttributeViSession (ViSession vi, ViConstString channelName, ViAttr attributeID, ViSession attributeValue);

#### Purpose

Checks the validity of a value you specify for a ViSession attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. Read-only attributes appear dim in the list box. If you select a read-only attribute, an error message appears. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViSession type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViSession | Pass the value which you want to verify as a valid value for the attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. Note Some of the values might not be valid depending on the current settings of the instrument session. |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_checkattrvistring.html language=enus -->
## TOPIC 00048: niSwitch_CheckAttributeViString

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_checkattrvistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_checkattrvistring.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_CheckAttributeViString

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_CheckAttributeViString (ViSession vi, ViConstString channelName, ViAttr attributeID, ViConstString attributeValue);

#### Purpose

Checks the validity of a value you specify for a ViString attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. Read-only attributes appear dim in the list box. If you select a read-only attribute, an error message appears. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViString type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViConstString | Pass the value which you want to verify as a valid value for the attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. Note Some of the values might not be valid depending on the current settings of the instrument session. |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_clearerror.html language=enus -->
## TOPIC 00049: niSwitch_ClearError

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_clearerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_clearerror.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_ClearError

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_ClearError (ViSession vi);

#### Purpose

This function clears the error code and error description for the IVI session. 
If you specify a valid IVI session for the **vi** parameter, this function clears the error information for the session. 
 
If the user passes VI_NULL for the **vi** parameter, this function clears the error information for the current execution thread. 
If **vi** is an invalid session, the function does nothing and returns an error. The function clears the error code by setting it to VI_SUCCESS, 
 
If the error description string is non-NULL, the function deallocates the error description string and sets the address to VI_NULL. 
 
Maintaining the error information separately for each thread is useful if the user does not have a session handle to pass to the [niSwitch_GetError](c_nisw_geterror.html) function, which occurs when a call to [niSwitch_init](c_nisw_init.html) or [niSwitch_InitWithOptions](c_nisw_initwithoptions.html) fails.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- Error and Status Codes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_clearinterchgwarn.html language=enus -->
## TOPIC 00050: niSwitch_ClearInterchangeWarnings

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_clearinterchgwarn.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_clearinterchgwarn.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_ClearInterchangeWarnings

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_ClearInterchangeWarnings (ViSession vi);

#### Purpose

This function clears the list of current interchange warnings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- niSwitch_GetNextInterchangeWarning
- niSwitch_ResetInterchangeCheck

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_close.html language=enus -->
## TOPIC 00051: niSwitch_close

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_close.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_close.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_close

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_close (ViSession vi);

#### Purpose

Terminates the NI-SWITCH session and all of its attributes and deallocates any memory resources the driver uses.

|  | Note You must unlock the session before calling niSwitch_close. After calling niSwitch_close, you cannot use the NI-SWITCH again until you call niSwitch_init or niSwitch_InitWithOptions. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- Close

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_commit.html language=enus -->
## TOPIC 00052: niSwitch_Commit

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_commit.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_Commit

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_Commit (ViSession vi);

#### Purpose

Downloads the configured scan list and trigger settings to hardware. 
 
Calling [niSwitch_Commit](c_nisw_commit.html) is optional as it is implicitly called during [niSwitch_InitiateScan](c_nisw_initiatescan.html). Use [niSwitch_Commit](c_nisw_commit.html) to arm triggers in a given order or to control when expensive hardware operations are performed.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- niSwitch_InitiateScan
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_configscanlist.html language=enus -->
## TOPIC 00053: niSwitch_ConfigureScanList

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_configscanlist.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_configscanlist.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_ConfigureScanList

#### IviSwtchScanner Capability Group

#### C Function Prototype

ViStatus niSwitch_ConfigureScanList (ViSession vi, ViConstString scanlist, ViInt32 scanMode);

#### Purpose

Configures the scan list and scan mode used for scanning. 
 
Refer to [Devices](/csh?topicname=switch/devices.html) to determine if the switch module supports scanning. 
 
The scan list is comprised of a list of channel connections separated by semicolons. For example, the following scan list will scan the first three channels of a multiplexer: 
 
com0->ch0; com0->ch1; com0->ch2; 
 
Refer to [Scan Lists](/csh?topicname=switch/scan_list.html) for more information on scan list syntax. 
 
To see the status of the scan, call either [niSwitch_IsScanning](c_nisw_isscanning.html) or [niSwitch_WaitForScanComplete](c_nisw_waitforscancomplete.html). Use the [niSwitch_ConfigureScanTrigger](c_nisw_configscantrigger.html) function to configure the scan trigger. Use the [niSwitch_InitiateScan](c_nisw_initiatescan.html) function to start the scan.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| scanlist | ViConstString | The scan list to use. NI-SWITCH uses this value to set the NISWITCH_ATTR_SCAN_LIST attribute. |
| scanMode | ViInt32 | Specifies how the switch module breaks existing connections when scanning. The driver uses this value to set the NISWITCH_ATTR_SCAN_MODE attribute. Refer to scan modes for more information. The default value is NISWITCH_VAL_BREAK_BEFORE_MAKE. |

#### Related Information

- Scan Lists
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_configscantrigger.html language=enus -->
## TOPIC 00054: niSwitch_ConfigureScanTrigger

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_configscantrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_configscantrigger.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_ConfigureScanTrigger

#### IviSwtchScanner Capability Group

#### C Function Prototype

ViStatus niSwitch_ConfigureScanTrigger (ViSession vi, ViReal64 scanDelay, ViInt32 triggerInput, ViInt32 scanAdvancedOutput);

#### Purpose

Configures the scan triggers for the scan list established with [niSwitch_ConfigureScanList](c_nisw_configscanlist.html). 
 
Refer to [Devices](/csh?topicname=switch/devices.html) to determine if the switch module supports scanning. 
 
[niSwitch_ConfigureScanTrigger](c_nisw_configscantrigger.html) sets the location that the switch expects to receive an input trigger to advance through the scan list. This function also sets the location where it outputs a scan advanced signal after it completes an entry in the scan list.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| scanDelay | ViReal64 | The minimum length of time you want the switch to wait after it creates a path until it asserts a trigger on the scan advanced output line. The driver uses this value to set the NISWITCH_ATTR_SCAN_DELAY attribute. The scan delay is in addition to the settling time. The driver uses this value to set the NISWITCH_ATTR_SCAN_DELAY attribute.Express this value in seconds. The default value is 0.0 s. |
| triggerInput | ViInt32 | Trigger source you want the switch module to use during scanning. The driver uses this value to set the NISWITCH_ATTR_TRIGGER_INPUT attribute. The switch waits for the trigger you specify when it encounters a semicolon in the scan list. When the trigger occurs, the switch advances to the next entry in the scan list. Refer to NISWITCH_ATTR_TRIGGER_INPUT for a list of valid values. |
| scanAdvancedOutput | ViInt32 | Output destination of the scan advanced trigger signal. NI-SWITCH uses this value to set the NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT attribute. After the switch processes each entry in the scan list, it waits the length of time you specify in the scanDelay parameter and then asserts a trigger on the line you specify with this parameter. Refer to NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT for a list of valid values. |

#### Related Information

- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_connect.html language=enus -->
## TOPIC 00055: niSwitch_Connect

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_connect.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_connect.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_Connect

#### IviSwtchBase Capability Group

#### C Function Prototype

ViStatus niSwitch_Connect (ViSession vi, ViConstString channel1, ViConstString channel2);

#### Purpose

Creates a path between **channel1** and **channel2**. NI-SWITCH calculates and uses the shortest path between the two channels. Refer to [Immediate Operations](/csh?topicname=switch/immediate.html) for information about channel usage types.

If a path is not available, the function returns one of the following errors:

- NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are already connected by calling either the niSwitch_Connect or niSwitch_SetPath function.
- NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a configuration channel. Error elaboration contains information about which of the two channels is a configuration channel.
- NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are connected to a different source. Error elaboration contains information about sources channel1 and channel2 connect to.
- NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channel1 and channel2 are one and the same channel.
- NISWITCH_ERROR_PATH_NOT_FOUND, if the driver cannot find a path between the two channels.

|  | Note Paths are bidirectional. For example, if a path exists between channels CH1 and CH2, then the path also exists between channels CH2 and CH1. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channel1 | ViConstString | Input one of the channel names of the desired path. Pass the other channel name as channel2. Refer to Devices for valid channel names for the switch module.Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp |
| channel2 | ViConstString | Input one of the channel names of the desired path. Pass the other channel name as channel1. Refer to Devices for valid channel names for the switch module. Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp |

#### Related Information

- Immediate Operations
- niSwitch_ConnectMultiple
- niSwitch_CanConnect
- niSwitch_SetPath

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_connect_multiple.html language=enus -->
## TOPIC 00056: niSwitch_ConnectMultiple

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_connect_multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_connect_multiple.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_ConnectMultiple

#### C Function Prototype

ViStatus niSwitch_ConnectMultiple (ViSession vi, ViConstString connectionList);

#### Purpose

Creates the connections between channels specified in **connection list**. Specify connections with two endpoints only or the explicit path between two endpoints. NI-SWITCH calculates and uses the shortest path between the channels. Refer to [Setting Source and Configuration Channels](/csh?topicname=switch/configchannels.html) for information about channel usage types. In the event of an error, connecting stops at the point in the list where the error occurred.

If a path is not available, the function returns one of the following errors:

- NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are already connected.
- NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a configuration channel. Error elaboration contains information about which of the two channels is a configuration channel.
- NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if the connection between two channels is connected to different source channels. Error elaboration contains information about the connection channel with errors.
- NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if two channels in a single connection are the same channel.
- NISWITCH_ERROR_PATH_NOT_FOUND, if the driver cannot find a path between two channels.

|  | Note Paths are bidirectional. For example, if a path exists between channels ch1 and ch2, then the path also exists between channels ch2 and ch1. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| connectionList | ViConstString | Connection list specifies a list of connections between channels to make. NI-SWITCH validates the connection list, and aborts execution of the list if errors are returned. Refer to Connection and Disconnection List Syntax for valid connection list syntax and examples. Refer to Devices for valid channel names for the switch module. |

#### Related Information

- Immediate Operations
- niSwitch_Connect

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_disable.html language=enus -->
## TOPIC 00057: niSwitch_Disable

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_disable.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_Disable

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_Disable (ViSession vi);

#### Purpose

Places the switch module in a quiescent state, where it has minimal or no impact on the system to which it is connected. All channels are disconnected and any scan in progress is aborted.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- niSwitch_close
- niSwitch_DisconnectAll

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_disconnect.html language=enus -->
## TOPIC 00058: niSwitch_Disconnect

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_disconnect.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_disconnect.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_Disconnect

#### IviSwtchBase Capability Group

#### C Function Prototype

ViStatus niSwitch_Disconnect (ViSession vi, ViConstString channel1, ViConstString channel2);

#### Purpose

Destroys the path between two channels that you create with the [niSwitch_Connect](c_nisw_connect.html) or [niSwitch_SetPath](c_nisw_setpath.html) function.

If a path is not available, the function returns one of the following errors:

- NISWITCH_ERROR_NO_SUCH_PATH, if a path does not exist between two channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channel1 | ViConstString | Input one of the channel names of the path to break. Pass the other channel name as channel2. Refer to Devices for valid channel names for the switch module.Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp |
| channel2 | ViConstString | Input one of the channel names of the path to break. Pass the other channel name as channel1. Refer to Devices for valid channel names for the switch module.Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp |

#### Related Information

- Immediate Operations
- niSwitch_DisconnectMultiple

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_disconnect_multiple.html language=enus -->
## TOPIC 00059: niSwitch_DisconnectMultiple

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_disconnect_multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_disconnect_multiple.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_DisconnectMultiple

#### C Function Prototype

ViStatus niSwitch_DisconnectMultiple (ViSession vi, ViConstString disconnectionList);

#### Purpose

Breaks the connections between channels specified in **disconnection list**. If no connections exist between channels, NI-SWITCH returns an error. In the event of an error, the VI stops at the point in the list where the error occurred.

If a path is not available, the function returns the following error:

- NISWITCH_ERROR_NO_SUCH_PATH, if a path does not exist between two channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| disconnectionList | ViConstString | Disconnection list specifies a list of connections between channels to break. NI-SWITCH validates the disconnection list, and aborts execution of the list if errors are returned. Refer to Connection and Disconnection list Syntax for valid connection list syntax and examples. Refer to Devices for valid channel names for the switch module. |

#### Related Information

- Immediate Operations
- niSwitch_Disconnect

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_disconnectall.html language=enus -->
## TOPIC 00060: niSwitch_DisconnectAll

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_disconnectall.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_disconnectall.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_DisconnectAll

#### IviSwtchBase Capability Group

#### C Function Prototype

ViStatus niSwitch_DisconnectAll (ViSession vi);

#### Purpose

Breaks all existing paths.

If the switch module cannot break all paths, the NISWITCH_WARN_PATH_REMAINS warning is returned.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- Immediate Operations
- niSwitch_Disconnect

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_error_message.html language=enus -->
## TOPIC 00061: niSwitch_error_message

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_error_message.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_error_message.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_error_message

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_error_message (ViSession vi, ViStatus errorCode, ViChar[] errorMessage);

#### Purpose

Converts an error code returned by NI-SWITCH into a user-readable string. Generally this information is supplied in error out of any NI-SWITCH VI. Use [niSwitch_error_message](c_nisw_error_message.html) for a static lookup of an error code description.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| errorCode | ViStatus | Status code returned by any NI-SWITCH function. The default value is 0 (VI_SUCCESS). |
| errorMessage | ViChar[] | The error information formatted into a string. You must pass a ViChar array with at least 256 bytes. |

#### Related Information

- Error and Status Codes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_error_query.html language=enus -->
## TOPIC 00062: niSwitch_error_query

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_error_query.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_error_query.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_error_query

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_error_query (ViSession vi, ViInt32* errorCode, ViChar[] errorMessage);

#### Purpose

This function reads an error code and a message from the instrument error queue. 
NI-SWITCH does not have an error queue, so this function never returns any errors.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| errorCode | ViInt32 | Returns the error code read from the instrument error queue.NI-SWITCH does not have an error queue, so this function never returns any errors. |
| errorMessage | ViChar[] | Returns the error message string read from the instrument's error message queue. You must pass a ViChar array with at least 256 bytes.NI-SWITCH does not have an error queue, so this function only returns No error. |

#### Related Information

- Error and Status Codes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getattrviboolean.html language=enus -->
## TOPIC 00063: niSwitch_GetAttributeViBoolean

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getattrviboolean.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getattrviboolean.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetAttributeViBoolean

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetAttributeViBoolean (ViSession vi, ViConstString channelName, ViAttr attributeID, ViBoolean* attributeValue);

#### Purpose

Queries the value of a ViBoolean attribute. You can use this function to get the values of instrument specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViInt32 type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViBoolean | Returns the current value of the attribute. Pass the address of a ViBoolean variable. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getattrviint32.html language=enus -->
## TOPIC 00064: niSwitch_GetAttributeViInt32

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getattrviint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getattrviint32.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetAttributeViInt32

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetAttributeViInt32 (ViSession vi, ViConstString channelName, ViAttr attributeID, ViInt32* attributeValue);

#### Purpose

Queries the value of a ViInt32 attribute. You can use this function to get the values of instrument specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViInt32 type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViInt32 | Returns the current value of the attribute. Pass the address of a ViInt32 variable. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getattrvireal64.html language=enus -->
## TOPIC 00065: niSwitch_GetAttributeViReal64

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getattrvireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getattrvireal64.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetAttributeViReal64

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetAttributeViReal64 (ViSession vi, ViConstString channelName, ViAttr attributeID, ViReal64* attributeValue);

#### Purpose

Queries the value of a ViReal64 attribute. You can use this function to get the values of instrument specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViInt32 type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViReal64 | Returns the current value of the attribute. Pass the address of a ViReal64 variable. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getattrvisession.html language=enus -->
## TOPIC 00066: niSwitch_GetAttributeViSession

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getattrvisession.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getattrvisession.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetAttributeViSession

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetAttributeViSession (ViSession vi, ViConstString channelName, ViAttr attributeID, ViSession* attributeValue);

#### Purpose

Queries the value of a ViSession attribute. You can use this function to get the values of instrument specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViInt32 type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| attributeValue | ViSession | Returns the current value of the attribute. Pass the address of a ViSession variable. From the function panel window in LabWindows/CVI, you can use this control as follows. If the attribute currently showing in the Attribute ID ring control has constants as valid values, you can view a list of the constants by pressing <ENTER> on this control. Select a value by double-clicking on it or by selecting it and then pressing <ENTER>. |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getattrvistring.html language=enus -->
## TOPIC 00067: niSwitch_GetAttributeViString

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getattrvistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getattrvistring.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetAttributeViString

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetAttributeViString (ViSession vi, ViConstString channelName, ViAttr attributeID, ViInt32 arraySize, ViChar[] attributeValue);

#### Purpose

Queries the value of a ViString attribute. You can use this function to get the values of instrument specific attributes and inherent IVI attributes. If the attribute represents an instrument state, this function performs instrument I/O in the following cases:

- State caching is disabled for the entire session or for the particular attribute.
- State caching is enabled and the currently cached value is invalid.

You must provide a ViChar array to serve as a buffer for the value. Pass the number of bytes in the buffer as **arraySize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in **arraySize**, the function copies **arraySize**-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the array size you must pass to get the entire value. For example, if the value is "123456" and **arraySize** is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required array size, you can pass 0 for **arraySize** and VI_NULL for the **attributeValue** buffer. If you want the function to fill in the buffer regardless of the number of bytes in the value, pass a negative number for **arraySize**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channelName | ViConstString | Some attributes are unique for each channel. For these, pass the name of the channel. Other attributes are unique for each switch. Pass VI_NULL or an empty string for this parameter. The default value is an empty string. |
| attributeID | ViAttr | Pass the ID of an attribute. From the function panel window in LabWindows/CVI, you can use this control as follows. Click on the control or press <ENTER>, <spacebar>, or <ctrl-down arrow>, to display a dialog box containing a hierarchical list of the available attributes. Attributes whose value cannot be set are dim. Help text is shown for each attribute. Select an attribute by double-clicking on it or by selecting it and then pressing <ENTER>. A ring control at the top of the dialog box allows you to see all IVI attributes or only the attributes of the ViInt32 type. If you choose to see all IVI attributes, the data types appear to the right of the attribute names in the list box. The data types that are not consistent with this function are dim. If you select an attribute data type that is dim, LabWindows/CVI transfers you to the function panel for the corresponding function that is consistent with the data type. If you want to enter a variable name, press <CTRL-T> to change this ring control to a manual input box. If the attribute in this ring control has constants as valid values, you can view the constants by moving to the Attribute Value control and pressing <ENTER>. |
| arraySize | ViInt32 | Pass the number of bytes in the ViChar array you specify for the Attribute Value parameter. If the current value of the attribute, including the terminating NUL byte, contains more bytes that you indicate in this parameter, the function copies Array Size-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the array size you must pass to get the entire value. For example, if the value is "123456" and the Array Size is 4, the function places 123 into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value. If you pass 0, you can pass VI_NULL for the Attribute Value buffer parameter. The default value is 512. |
| attributeValue | ViChar[] | Buffer in which the function returns the current value of the attribute. The buffer must be of type ViChar and have at least as many bytes as indicated in the arraySize parameter. If the current value of the attribute, including the terminating NULL byte, contains more bytes that you indicate in this parameter, the function copies arraySize-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the array size you must pass to get the entire value. |

#### Related Information

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getchannelname.html language=enus -->
## TOPIC 00068: niSwitch_GetChannelName

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getchannelname.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getchannelname.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetChannelName

#### IviSwtchBase Capability Group

#### C Function Prototype

ViStatus niSwitch_GetChannelName (ViSession vi, ViInt32 index, ViInt32 bufferSize, ViChar[] channelNameBuffer);

#### Purpose

Returns the channel string that is in the channel table at the specified index. 
 
Use [niSwitch_GetChannelName](c_nisw_getchannelname.html) in a For Loop to get a complete list of valid channel names for the switch. Use the NISWITCH_ATTR_CHANNEL_COUNT attribute to determine the number of channels.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| index | ViInt32 | A 1-based index into the channel table. The default value is 1. The maximum value is Value of Channel Count attribute. |
| bufferSize | ViInt32 | Pass the number of bytes in the ViChar array you specify for the Channel Name Buffer parameter. If the channel name string, including the terminating NUL byte, contains more bytes than you indicate in this parameter, the function copies Buffer Size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and bufferSize is 4, the function places "123" into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value. If you pass 0, you can pass VI_NULL for the Coercion Record buffer parameter. |
| channelNameBuffer | ViChar[] | Returns the channel name that is in the channel table at the index you specify. |

#### Related Information

- niSwitch_GetRelayName

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_geterror.html language=enus -->
## TOPIC 00069: niSwitch_GetError

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_geterror.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_geterror.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetError

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetError (ViSession vi, ViStatus* code, ViInt32 buffersize, ViChar[] description);

#### Purpose

This function retrieves and then clears the IVI error information for the session or the current execution thread. 
 
One exception exists: If the **bufferSize** parameter is 0, the function does not clear the error information. By passing 0 for the buffer size, the caller can ascertain the buffer size required to get the entire error description string and then call the function again with a sufficiently large buffer. If you specify a valid IVI session for the **vi** parameter, this function retrieves and then clears the error information for the session. If the user passes VI_NULL for the **vi** parameter, this function retrieves and then clears the error information for the current execution thread. If the **vi** parameter is an invalid session, the function does nothing and returns an error. Normally, the error information describes the first error that occurred since the user last called [niSwitch_GetError](c_nisw_geterror.html) or [niSwitch_ClearError](c_nisw_clearerror.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| code | ViStatus | Returns the error code for the session or execution thread. If you pass 0 for bufferSize, you can pass VI_NULL for this parameter. |
| buffersize | ViInt32 | Pass the number of bytes in the ViChar array you specify for the Description parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies bufferSize–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and bufferSize is 4, the function places "123" into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value. If you pass 0, you can pass VI_NULL for the description buffer parameter. |
| description | ViChar[] | Returns the error description for the IVI session or execution thread. If there is no description, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the bufferSize parameter. If the error description, including the terminating NULL byte, contains more bytes than you indicate with the bufferSize, the function copies bufferSize–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and bufferSize is 4, the function places "123" into the buffer and returns 7. If you pass 0 for the Buffer Size, you can pass VI_NULL for this parameter. |

#### Related Information

- Error and Status Codes

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getnextcoercionrec.html language=enus -->
## TOPIC 00070: niSwitch_GetNextCoercionRecord

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getnextcoercionrec.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getnextcoercionrec.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetNextCoercionRecord

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetNextCoercionRecord (ViSession vi, ViInt32 bufferSize, ViChar[] coercionRecord);

#### Purpose

This function returns the coercion information associated with the IVI session. This function retrieves and clears the oldest instance in which NI-SWITCH coerced a value you specified to another value. 
 
If you set the [NISWITCH_ATTR_RECORD_COERCIONS](c_nisw_attr_rec_coercions.html) attribute to [VI_TRUE](c_vi_true.html), NI-SWITCH keeps a list of all coercions it makes on ViInt32 or ViReal64 values you pass to NI-SWITCH functions. You use this function to retrieve information from that list. If the next coercion record string, including the terminating NUL byte, contains more bytes than you indicate in this parameter, the function copies **bufferSize**–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the **bufferSize** is 4, the function places "123" into the buffer and returns 7. If you pass 0, you can pass VI_NULL for the Coercion Record buffer parameter. The function returns an empty string in the Coercion Record parameter if no coercion records remain for the session.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| bufferSize | ViInt32 | Pass the number of bytes in the ViChar array you specify for the Coercion Record parameter. If the next coercion record string, including the terminating NUL byte, contains more bytes than you indicate in this parameter, the function copies bufferSize–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the bufferSize is 4, the function places "123" into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value. If you pass 0, you can pass VI_NULL for the Coercion Record buffer parameter. |
| coercionRecord | ViChar[] | Returns the next coercion record for the IVI session. If there are no coercion records, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the bufferSize parameter. If the next coercion record string, including the terminating NUL byte, contains more bytes than you indicate with the bufferSize parameter, the function copies bufferSize–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and bufferSize is 4, the function places "123" into the buffer and returns 7. This parameter returns an empty string if no coercion records remain for the session. |

#### Related Information

- Record Value Coercions

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getnextinterchgwarn.html language=enus -->
## TOPIC 00071: niSwitch_GetNextInterchangeWarning

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getnextinterchgwarn.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getnextinterchgwarn.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetNextInterchangeWarning

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetNextInterchangeWarning (ViSession vi, ViInt32 bufferSize, ViChar[] interchangeWarning);

#### Purpose

This function returns the interchangeability warnings associated with the IVI session. It retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. You use this function to retrieve interchangeability warnings. The driver performs interchangeability checking when the [NISWITCH_ATTR_INTERCHANGE_CHECK](c_nisw_attr_interchg_check.html) attribute is set to [VI_TRUE](c_vi_true.html). The function returns an empty string in the **interchangeWarning** parameter if no interchangeability warnings remain for the session. In general, the instrument driver generates interchangeability warnings when an attribute that affects the behavior of the instrument is in a state that you did not specify.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| bufferSize | ViInt32 | Pass the number of bytes in the ViChar array you specify for the interchangeWarning parameter. If the next interchangeability warning string, including the terminating NUL byte, contains more bytes than you indicate in this parameter, the function copies bufferSize–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the bufferSize is 4, the function places "123" into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value. If you pass 0, you can pass VI_NULL for the Interchange Warning buffer parameter. |
| interchangeWarning | ViChar[] | Returns the next interchange warning for the IVI session. If there are no interchange warnings, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the bufferSize parameter. If the next interchangeability warning string, including the terminating NUL byte, contains more bytes than you indicate with the bufferSize parameter, the function copies bufferSize–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and bufferSize is 4, the function places "123" into the buffer and returns 7. This parameter returns an empty string if no interchangeability warnings remain for the session. |

#### Related Information

- niSwitch_ClearInterchangeWarnings
- niSwitch_ResetInterchangeCheck

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getpath.html language=enus -->
## TOPIC 00072: niSwitch_GetPath

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getpath.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getpath.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetPath

#### IviSwtchBase Capability Group

#### C Function Prototype

ViStatus niSwitch_GetPath (ViSession vi, ViConstString channel1, ViConstString channel2, ViInt32 bufferSize, ViChar[] path);

#### Purpose

Returns a string that identifies the explicit path created with [niSwitch_Connect](c_nisw_connect.html). Pass this string to [niSwitch_SetPath](c_nisw_setpath.html) to establish the exact same path in future connections.

In some cases, multiple paths are available between two channels. When you call [niSwitch_Connect](c_nisw_connect.html), NI-SWITCH selects an available path; however, the driver may not always select the same path through the switch module.

[niSwitch_GetPath](c_nisw_getpath.html) only returns those paths explicitly created by [niSwitch_Connect](c_nisw_connect.html) or [niSwitch_SetPath](c_nisw_setpath.html). For example, if you connect channels CH1 and CH3, and then channels CH2 and CH3, an explicit path between channels CH1 and CH2 does not exist and an error is returned.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| channel1 | ViConstString | Input one of the channel names of the desired path. Pass the other channel name as channel2. Refer to Devices for valid channel names for the switch module. Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp The default value is an empty string. |
| channel2 | ViConstString | Input one of the channel names of the desired path. Pass the other channel name as channel1. Refer to Devices for valid channel names for the switch module. Examples of valid channel names: ch0, com0, ab0, r1, c2, cjtemp The default value is an empty string. |
| bufferSize | ViInt32 | Pass the number of bytes in the ViChar array you specify for the Path parameter. If the current value of the attribute, including the terminating NULL byte, contains more bytes that you indicate in this parameter, the function copies bufferSize–1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "R1->C1" and bufferSize is 4, the function places "R1-" into the buffer and returns 7. If you pass 0, you can pass VI_NULL for path. This enables you to find out the path size and to allocate the buffer of the appropriate size before calling this function again. |
| path | ViChar[] | A string composed of comma-separated paths between channel1 and channel2. The first and last names in the path are the endpoints of the path. All other channels in the path are configuration channels.Examples of returned paths:ch0->com0, com0->ab0 |

#### Related Information

- niSwitch_SetPath

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getrelaycount.html language=enus -->
## TOPIC 00073: niSwitch_GetRelayCount

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getrelaycount.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getrelaycount.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetRelayCount

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetRelayCount (ViSession vi, ViConstString relayName, ViInt32* relayCount);

#### Purpose

Returns the number of times the relay has changed from closed to open. Relay count is useful for tracking relay lifetime and usage. Call [niSwitch_WaitForDebounce](c_nisw_waitfordebounce.html) before niSwitch_GetRelayCount to ensure an accurate count.

Refer to [Relay Count](/csh?topicname=switch/relay_count.html) to determine if the switch module supports relay counting.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| relayName | ViConstString | Name of the relay. Refer to Devices for a list of valid relay names for the switch module.Examples of valid relay names:ch0, ab0, 1wire, hlselect |
| relayCount | ViInt32 | The number of relay cycles. |

#### Related Information

- niSwitch_GetRelayName

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getrelayname.html language=enus -->
## TOPIC 00074: niSwitch_GetRelayName

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getrelayname.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getrelayname.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetRelayName

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetRelayName (ViSession vi, ViInt32 index, ViInt32 relayNameBufferSize, ViChar[] relayNameBuffer);

#### Purpose

Returns the relay name string that is in the relay list at the specified index. 
 
Use [niSwitch_GetRelayName](c_nisw_getrelayname.html) in a For Loop to get a complete list of valid relay names for the switch. Use the NISWITCH_ATTR_NUMBER_OF_RELAYS attribute to determine the number of relays.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| index | ViInt32 | A 1-based index into the channel table. The default value is 1. The maximum value is the value of the NISWITCH_ATTR_CHANNEL_COUNT attribute. |
| relayNameBufferSize | ViInt32 | Pass the number of bytes in the ViChar array you specify for the relayNameBuffer parameter. If the relay name string, including the terminating NUL byte, contains more bytes than you indicate in this parameter, the function copies Buffer Size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and relayBufferSize is 4, the function places "123" into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value. If you pass 0, you can pass VI_NULL for the Coercion Record buffer parameter. |
| relayNameBuffer | ViChar[] | Returns the relay name for the index you specify. |

#### Related Information

- niSwitch_GetChannelName
- niSwitch_GetRelayCount

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_getrelayposition.html language=enus -->
## TOPIC 00075: niSwitch_GetRelayPosition

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_getrelayposition.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_getrelayposition.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_GetRelayPosition

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_GetRelayPosition (ViSession vi, ViConstString relayName, ViInt32* relayPosition);

#### Purpose

Returns the relay position for the relay specified in the **relayName** parameter.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| relayName | ViConstString | Name of the relay. Refer to Devices for a list of valid relay names for the switch module.Examples of valid relay names:ch0, ab0, 1wire, hlselect |
| relayPosition | ViInt32 | Indicates whether the relay is open or closed. Valid Values:NISWITCH_VAL_OPEN (10)NISWITCH_VAL_CLOSED (11) |

#### Related Information

- niSwitch_RelayControl
- Relay Forms

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_init.html language=enus -->
## TOPIC 00076: niSwitch_init

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_init.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_init.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_init

#### Specific Function

#### C Function Prototype

ViStatus niSwitch_init (ViRsrc resourceName, ViBoolean idQuery, ViBoolean resetDevice, ViSession* vi);

#### Purpose

Returns a session handle used to identify the switch module in all subsequent instrument driver calls. 
 
[niSwitch_init](c_nisw_init.html) creates a new IVI instrument driver session for the switch module specified in the **resourceName** parameter. If multiple [topologies](/csh?topicname=switch/topology.html) are valid for that device, NI-SWITCH uses the default topology specified in MAX. 
 
By default, the switch module is reset to a known state. 
 
An error is returned if a session to the specified resource exists in another process. The same session is returned if [niSwitch_init](c_nisw_init.html) is called twice in the same process for the same resource with the same topology.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | ViRsrc | Resource name of the switch module to initialize. Syntax: Configured in MAX Under Valid Syntax Devices and Interfaces DeviceName PXI System PXI[bus number]::device number Optional fields are shown in square brackets ([]). The default values for optional fields are as follows: chassis ID = 1bus number = 0 Tip IVI logical names are also valid for the resource name. Example resource names: Name Description SC1Mod3 NI-DAQmx module in chassis "SC1" Slot 3 MySwitch NI-DAQmx module renamed to "MySwitch" PXI0::16 PXI bus 0, device number 16 PXI::16 PXI bus 0, device number 16 |
| Configured in MAX Under | Valid Syntax |  |
| Devices and Interfaces | DeviceName |  |
| PXI System | PXI[bus number]::device number |  |
|  | Tip IVI logical names are also valid for the resource name. |  |
| Name | Description |  |
| SC1Mod3 | NI-DAQmx module in chassis "SC1" Slot 3 |  |
| MySwitch | NI-DAQmx module renamed to "MySwitch" |  |
| PXI0::16 | PXI bus 0, device number 16 |  |
| PXI::16 | PXI bus 0, device number 16 |  |
| idQuery | ViBoolean | This parameter is ignored. Because NI-SWITCH supports multiple switch modules, it always queries the switch to determine which device is installed. For this reason, this VI may return NISWITCH_ERROR_FAIL_ID_QUERY even if this parameter is set to VI_FALSE. Value Description VI_TRUE (default) Queries the switch to determine which device is installed. VI_FALSE Currently unsupported. |
| Value | Description |  |
| VI_TRUE (default) | Queries the switch to determine which device is installed. |  |
| VI_FALSE | Currently unsupported. |  |
| resetDevice | ViBoolean | Specifies whether to reset the switch module during the initialization process. Value Description VI_TRUE (default) Resets the device. VI_FALSE Currently unsupported. The device will not reset. |
| Value | Description |  |
| VI_TRUE (default) | Resets the device. |  |
| VI_FALSE | Currently unsupported. The device will not reset. |  |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- Initialization
- Programming Flow

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_initiatescan.html language=enus -->
## TOPIC 00077: niSwitch_InitiateScan

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_initiatescan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_initiatescan.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_InitiateScan

#### IviSwtchScanner Capability Group

#### C Function Prototype

ViStatus niSwitch_InitiateScan (ViSession vi);

#### Purpose

Commits the configured scan list and trigger settings to hardware and initiates the scan. If [niSwitch_Commit](c_nisw_commit.html) was called earlier, [niSwitch_InitiateScan](c_nisw_initiatescan.html) only initiates the scan and returns immediately. 
 
Once the scanning operation begins, you cannot perform any other operation other than GetAttribute, [niSwitch_AbortScan](c_nisw_abortscan.html), or [niSwitch_SendSoftwareTrigger](c_nisw_sendsoftwaretrigger.html). All other functions return the NISWITCH_ERROR_SCAN_IN_PROGRESS error. To stop the scanning operation, 
 
To stop the scanning operation, call [niSwitch_AbortScan](c_nisw_abortscan.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |

#### Related Information

- niSwitch_Commit
- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_external.html language=enus -->
## TOPIC 00078: NISWITCH_VAL_EXTERNAL

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_external.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_external.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_EXTERNAL

#### Description

External Trigger. The switch waits until it receives a trigger from an external source through the external trigger input before processing the next entry in the scan list.

#### Defined Value

2

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_falling_edge.html language=enus -->
## TOPIC 00079: NISWITCH_VAL_FALLING_EDGE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_falling_edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_falling_edge.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_FALLING_EDGE

#### Description

The trigger occurs on the falling edge of the signal.

#### Defined Value

1

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_frontconn.html language=enus -->
## TOPIC 00080: NISWITCH_VAL_FRONTCONNECTOR

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_frontconn.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_frontconn.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_FRONTCONNECTOR

#### Description

This value represents the front connector. The front connector can send or receive triggers for scan list operations.

#### Defined Value

1001

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_frontconn_mod1.html language=enus -->
## TOPIC 00081: NISWITCH_VAL_FRONTCONNECTOR_MODULE1

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_frontconn_mod1.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_frontconn_mod1.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_FRONTCONNECTOR_MODULE1

#### Description

This value represents the front connector module 1. The front connector module 1 can send or receive triggers for scan list operations.

#### Defined Value

1041

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_frontconn_mod10.html language=enus -->
## TOPIC 00082: NISWITCH_VAL_FRONTCONNECTOR_MODULE10

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_frontconn_mod10.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_frontconn_mod10.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_FRONTCONNECTOR_MODULE10

#### Description

This value represents the front connector module 10. The front connector module 10 can send or receive triggers for scan list operations.

#### Defined Value

1050

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_frontconn_mod11.html language=enus -->
## TOPIC 00083: NISWITCH_VAL_FRONTCONNECTOR_MODULE11

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_frontconn_mod11.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_frontconn_mod11.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_FRONTCONNECTOR_MODULE11

#### Description

This value represents the front connector module 11. The front connector module 11 can send or receive triggers for scan list operations.

#### Defined Value

1051

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_frontconn_mod2.html language=enus -->
## TOPIC 00084: NISWITCH_VAL_FRONTCONNECTOR_MODULE2

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_frontconn_mod2.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_frontconn_mod2.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_FRONTCONNECTOR_MODULE2

#### Description

This value represents the front connector module 2. The front connector module 2 can send or receive triggers for scan list operations.

#### Defined Value

1042

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_frontconn_mod4.html language=enus -->
## TOPIC 00085: NISWITCH_VAL_FRONTCONNECTOR_MODULE4

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_frontconn_mod4.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_frontconn_mod4.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_FRONTCONNECTOR_MODULE4

#### Description

This value represents the front connector module 4. The front connector module 4 can send or receive triggers for scan list operations.

#### Defined Value

1044

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_none.html language=enus -->
## TOPIC 00086: NISWITCH_VAL_NONE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_none.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_none.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_NONE

#### Description

No implicit action on connections when scanning.

#### Defined Value

0

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_pxi_star.html language=enus -->
## TOPIC 00087: NISWITCH_VAL_PXI_STAR

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_pxi_star.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_pxi_star.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_PXI_STAR

#### Description

This value represents the PXI_STAR trigger bus. The PXI_STAR trigger bus can send or receive triggers for scan list operations.

#### Defined Value

125

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_rearconn.html language=enus -->
## TOPIC 00088: NISWITCH_VAL_REARCONNECTOR

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_rearconn.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_rearconn.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_REARCONNECTOR

#### Description

This value represents the rear connector. The rear connector can send or receive triggers for scan list operations.

#### Defined Value

1000

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_rearconn_mod1.html language=enus -->
## TOPIC 00089: NISWITCH_VAL_REARCONNECTOR_MODULE1

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_rearconn_mod1.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_rearconn_mod1.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_REARCONNECTOR_MODULE1

#### Description

This value represents the rear connector module 1. The rear connector module 1 can send or receive triggers for scan list operations.

#### Defined Value

1021

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_rearconn_mod10.html language=enus -->
## TOPIC 00090: NISWITCH_VAL_REARCONNECTOR_MODULE10

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_rearconn_mod10.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_rearconn_mod10.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_REARCONNECTOR_MODULE10

#### Description

This value represents the rear connector module 10. The rear connector module 10 can send or receive triggers for scan list operations.

#### Defined Value

1030

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_rearconn_mod11.html language=enus -->
## TOPIC 00091: NISWITCH_VAL_REARCONNECTOR_MODULE11

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_rearconn_mod11.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_rearconn_mod11.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_REARCONNECTOR_MODULE11

#### Description

This value represents the rear connector module 11. The rear connector module 11 can send or receive triggers for scan list operations.

#### Defined Value

1031

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_rearconn_mod12.html language=enus -->
## TOPIC 00092: NISWITCH_VAL_REARCONNECTOR_MODULE12

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_rearconn_mod12.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_rearconn_mod12.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_REARCONNECTOR_MODULE12

#### Description

This value represents the rear connector module 12. The rear connector module 12 can send or receive triggers for scan list operations.

#### Defined Value

1032

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_rearconn_mod2.html language=enus -->
## TOPIC 00093: NISWITCH_VAL_REARCONNECTOR_MODULE2

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_rearconn_mod2.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_rearconn_mod2.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_REARCONNECTOR_MODULE2

#### Description

This value represents the rear connector module 2. The rear connector module 2 can send or receive triggers for scan list operations.

#### Defined Value

1022

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_single.html language=enus -->
## TOPIC 00094: NISWITCH_VAL_SINGLE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_single.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_single.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_SINGLE

#### Description

When scanning, the switch does not share trigger lines with other switches. You must set NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT and NISWITCH_ATTR_TRIGGER_INPUT for this device.

#### Defined Value

0

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_sw_trig_func.html language=enus -->
## TOPIC 00095: NISWITCH_VAL_SW_TRIG_FUNC

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_sw_trig_func.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_sw_trig_func.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_SW_TRIG_FUNC

#### Description

The switch waits until you call the [niSwitch_SendSoftwareTrigger](c_nisw_sendsoftwaretrigger.html) function before processing the next entry in the scan list.

#### Defined Value

3

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_ttl1.html language=enus -->
## TOPIC 00096: NISWITCH_VAL_TTL1

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_ttl1.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_ttl1.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_TTL1

#### Description

This value represents the PXI_TRIG1 line. The PXI_TRIG1 line can send or receive triggers for scan list operations.

#### Defined Value

112

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_ttl2.html language=enus -->
## TOPIC 00097: NISWITCH_VAL_TTL2

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_ttl2.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_ttl2.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_TTL2

#### Description

This value represents the PXI_TRIG2 line. The PXI_TRIG2 line can send or receive triggers for scan list operations.

#### Defined Value

113

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_ttl3.html language=enus -->
## TOPIC 00098: NISWITCH_VAL_TTL3

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_ttl3.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_ttl3.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_TTL3

#### Description

This value represents the PXI_TRIG3 line. The PXI_TRIG3 line can send or receive triggers for scan list operations.

#### Defined Value

114

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_ttl5.html language=enus -->
## TOPIC 00099: NISWITCH_VAL_TTL5

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_ttl5.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_ttl5.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_TTL5

#### Description

This value represents the PXI_TRIG5 line. The PXI_TRIG5 line can send or receive triggers for scan list operations. .

#### Defined Value

116

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_ttl6.html language=enus -->
## TOPIC 00100: NISWITCH_VAL_TTL6

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_ttl6.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_ttl6.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_TTL6

#### Description

This value represents the PXI_TRIG6 line. The PXI_TRIG6 line can send or receive triggers for scan list operations.

#### Defined Value

117

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_val_ttl7.html language=enus -->
## TOPIC 00101: NISWITCH_VAL_TTL7

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_val_ttl7.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_val_ttl7.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NISWITCH_VAL_TTL7

#### Description

This value represents the PXI_TRIG7 line. The PXI_TRIG7 line can send or receive triggers for scan list operations.

#### Defined Value

118

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_waitfordebounce.html language=enus -->
## TOPIC 00102: niSwitch_WaitForDebounce

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_waitfordebounce.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_waitfordebounce.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_WaitForDebounce

#### IviSwtchBase Capability Group

#### C Function Prototype

ViStatus niSwitch_WaitForDebounce (ViSession vi, ViInt32 maximumTime_ms);

#### Purpose

Pauses until all created paths have settled.

If the time you specify with the **maximumTime_ms** parameter elapses before the switch paths settle, this function returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| maximumTime_ms | ViInt32 | Specifies the maximum length of time to wait for all relays in the switch module to activate or deactivate. If the specified time elapses before all relays activate or deactivate, a timeout error is returned. The default value is5000 ms. |

#### Related Information

- niSwitch_IsDebounced
- Electromechanical Relays

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_nisw_waitforscancomplete.html language=enus -->
## TOPIC 00103: niSwitch_WaitForScanComplete

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_nisw_waitforscancomplete.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_nisw_waitforscancomplete.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niSwitch_WaitForScanComplete

#### IviSwtchScanner Capability Group

#### C Function Prototype

ViStatus niSwitch_WaitForScanComplete (ViSession vi, ViInt32 maximumTime_ms);

#### Purpose

Pauses until the switch stops scanning or until the maximum time has elapsed, when NI-SWITCH returns a timeout error. 
 
If the time you specify with the **maximumTime_ms** parameter elapsed before the scanning operation has finished, this function returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls. |
| maximumTime_ms | ViInt32 | Specifies the maximum length of time to wait for the switch module to stop scanning. If the specified time elapses before the scan ends, the NISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. The default value is 5000 ms. |

#### Related Information

- Scanning

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_reference.html language=enus -->
## TOPIC 00104: NI-SWITCH Functions

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_reference.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-SWITCH Functions

| Class/Panel Name | Function Name |
| --- | --- |
| Initialize | niSwitch_init |
| Initialize With Options | niSwitch_InitWithOptions |
| Initialize With Topology | niSwitch_InitWithTopology |
| Configuration Functions |  |
| Set/Get/Check Attribute |  |
| Set Attribute |  |
| Set Attribute ViInt32 | niSwitch_SetAttributeViInt32 |
| Set Attribute ViReal64 | niSwitch_SetAttributeViReal64 |
| Set Attribute ViString | niSwitch_SetAttributeViString |
| Set Attribute ViBoolean | niSwitch_SetAttributeViBoolean |
| Set Attribute ViSession | niSwitch_SetAttributeViSession |
| Get Attribute |  |
| Get Attribute ViInt32 | niSwitch_GetAttributeViInt32 |
| Get Attribute ViReal64 | niSwitch_GetAttributeViReal64 |
| Get Attribute ViString | niSwitch_GetAttributeViString |
| Get Attribute ViBoolean | niSwitch_GetAttributeViBoolean |
| Get Attribute ViSession | niSwitch_GetAttributeViSession |
| Check Attribute |  |
| Check Attribute ViInt32 | niSwitch_CheckAttributeViInt32 |
| Check Attribute ViReal64 | niSwitch_CheckAttributeViReal64 |
| Check Attribute ViString | niSwitch_CheckAttributeViString |
| Check Attribute ViBoolean | niSwitch_CheckAttributeViBoolean |
| Check Attribute ViSession | niSwitch_CheckAttributeViSession |
| Route Functions |  |
| Connect Channels | niSwitch_Connect |
| Connect Multiple Channels | niSwitch_ConnectMultiple |
| Disconnect Channels | niSwitch_Disconnect |
| Disconnect Multiple Channels | niSwitch_DisconnectMultiple |
| Disconnect All Channels | niSwitch_DisconnectAll |
| Switch Is Debounced? | niSwitch_IsDebounced |
| Wait For Debounce | niSwitch_WaitForDebounce |
| Can Connect Channels? | niSwitch_CanConnect |
| Paths |  |
| Set Path | niSwitch_SetPath |
| Get Path | niSwitch_GetPath |
| Scan Functions |  |
| Scan | niSwitch_Scan |
| Initiate Scan | niSwitch_InitiateScan |
| Abort Scan | niSwitch_AbortScan |
| Send Software Trigger | niSwitch_SendSoftwareTrigger |
| Switch Is Scanning? | niSwitch_IsScanning |
| Wait For Scan To Complete | niSwitch_WaitForScanComplete |
| Set Continuous Scan | niSwitch_SetContinuousScan |
| Configure Scanlist | niSwitch_ConfigureScanList |
| Configure Scan Trigger | niSwitch_ConfigureScanTrigger |
| Route Trigger Input | niSwitch_RouteTriggerInput |
| Route Scan Advanced Output | niSwitch_RouteScanAdvancedOutput |
| Relay Operations |  |
| Get Relay Name | niSwitch_GetRelayName |
| Get Relay Count | niSwitch_GetRelayCount |
| Get Relay Position | niSwitch_GetRelayPosition |
| Relay Control | niSwitch_RelayControl |
| Utility Functions |  |
| Commit | niSwitch_Commit |
| Get Channel Name | niSwitch_GetChannelName |
| Reset | niSwitch_reset |
| Reset With Defaults | niSwitch_ResetWithDefaults |
| Disable | niSwitch_Disable |
| Self-Test | niSwitch_self_test |
| Revision Query | niSwitch_revision_query |
| Error-Query | niSwitch_error_query |
| Error Message | niSwitch_error_message |
| Coercion Info |  |
| Get Next Coercion Record | niSwitch_GetNextCoercionRecord |
| Interchangeability Info |  |
| Get Next Interchange Warning | niSwitch_GetNextInterchangeWarning |
| Clear Interchange Warnings | niSwitch_ClearInterchangeWarnings |
| Reset Interchange Check | niSwitch_ResetInterchangeCheck |
| Error Info |  |
| Get Error | niSwitch_GetError |
| Clear Error | niSwitch_ClearError |
| Locking |  |
| Lock Session | niSwitch_LockSession |
| Unlock Session | niSwitch_UnlockSession |
| Close | niSwitch_close |

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/c_vi_false.html language=enus -->
## TOPIC 00105: VI_FALSE

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/c_vi_false.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/c_vi_false.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### VI_FALSE

#### Description

False.

#### Defined Value

0

<!--NI_TOPIC bundle=ni-switch-c-api-ref path=switchcref/cref_title.html language=enus -->
## TOPIC 00106: NI-SWITCH Function Reference

- bundle_id: `ni-switch-c-api-ref`
- source_path: `switchcref/cref_title.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-c-api-ref/raw/resource/enus/switchcref/cref_title.html
- document_id: `ni-switch-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-SWITCH Function Reference

February 2019

Use the NI-SWITCH functions to create an application using LabWindows™/CVI™, Microsoft Visual C++, or Microsoft Visual Basic.

To comment on National Instruments documentation, refer to the National Instruments Web site.

© 2007–2019 National Instruments. All rights reserved.
