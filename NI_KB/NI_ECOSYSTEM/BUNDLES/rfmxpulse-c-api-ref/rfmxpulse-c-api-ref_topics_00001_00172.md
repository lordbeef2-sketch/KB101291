# NI DOCUMENT BUNDLE: rfmxpulse-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxpulse-c-api-ref start=1 end=172 -->
<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes_1ga0ec113161ac1eae8f58b3894591e3e72.html language=enus -->
## TOPIC 00001: RFMXPULSE_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes_1ga0ec113161ac1eae8f58b3894591e3e72.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes_1ga0ec113161ac1eae8f58b3894591e3e72.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the wait time before results are available in the RFmxPulse Attribute. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_RESULT_FETCH_TIMEOUTNumeric ValueData TypeAccessApplies To12632064float64Read/WriteN/ARemarks Set this value to a time longer than expected for fetching the measu

### RFMXPULSE_ATTR_RESULT_FETCH_TIMEOUT

Specifies the wait time before results are available in the RFmxPulse Attribute. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_RESULT_FETCH_TIMEOUT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12632064 | float64 | Read/Write | N/A |

#### Remarks

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxPulse Attribute waits until the measurement is complete.

You do not need to use a [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes_1ga34b969140e655d46967f8a34035329d2.html language=enus -->
## TOPIC 00002: RFMXPULSE_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes_1ga34b969140e655d46967f8a34035329d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes_1ga34b969140e655d46967f8a34035329d2.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin RFmx adds to the RFMXPULSE_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxRFMXPULSE_ATTR_REFERENCE_LEVEL_HEADROOMNumeric ValueData TypeAccessApplies To12587004float64Read/WriteN/A

### RFMXPULSE_ATTR_REFERENCE_LEVEL_HEADROOM

Specifies the margin RFmx adds to the [RFMXPULSE_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_pulse__attributes_1ga61f9c2c3dbacccd33963a6d6c3a8088b.html) attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

RFMXPULSE_ATTR_REFERENCE_LEVEL_HEADROOM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587004 | float64 | Read/Write | N/A |

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

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes_1ga5d5c7dcd6f7d13f22eeba1ef4c333413.html language=enus -->
## TOPIC 00003: RFMXPULSE_ATTR_SELECTED_PORTS

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes_1ga5d5c7dcd6f7d13f22eeba1ef4c333413.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes_1ga5d5c7dcd6f7d13f22eeba1ef4c333413.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. SyntaxRFMXPULSE_ATTR_SELECTED_PORTSNumeric ValueData TypeAccessApplies To12587005char[]Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXPULSE_ATTR_SELECTED_PORTS

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr_GetAvailablePorts](/csh?context=rfmxinstr_rfmxinstrcref_function_get_available_ports) function to get the valid port names.

#### Syntax

RFMXPULSE_ATTR_SELECTED_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587005 | char[] | Read/Write | N/A |

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

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes_1ga9df2405e6f385c1ad4147faa4ad45f8b.html language=enus -->
## TOPIC 00004: RFMXPULSE_ATTR_MEASUREMENT_FILTER_TYPE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes_1ga9df2405e6f385c1ad4147faa4ad45f8b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes_1ga9df2405e6f385c1ad4147faa4ad45f8b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the demodulation filter type to be used in the measurements. SyntaxRFMXPULSE_ATTR_MEASUREMENT_FILTER_TYPENumeric ValueData TypeAccessApplies To12582936int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Ref

### RFMXPULSE_ATTR_MEASUREMENT_FILTER_TYPE

Specifies the demodulation filter type to be used in the measurements.

#### Syntax

RFMXPULSE_ATTR_MEASUREMENT_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12582936 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_MEASUREMENT_FILTER_TYPE_RECTANGULAR | 0 (0x0) | The Rectangular filter is applied. |
| RFMXPULSE_VAL_MEASUREMENT_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The Gaussian filter is applied. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse_1ga4e33880b850ca2cb37c0957ac2b05722.html language=enus -->
## TOPIC 00005: RFMXPULSE_ATTR_PULSE_MEASUREMENT_ENABLED

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse_1ga4e33880b850ca2cb37c0957ac2b05722.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse_1ga4e33880b850ca2cb37c0957ac2b05722.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether pulse measurements are enabled. SyntaxRFMXPULSE_ATTR_PULSE_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To12587008int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXPULSE_ATTR_PULSE_MEASUREMENT_ENABLED

Specifies whether pulse measurements are enabled.

#### Syntax

RFMXPULSE_ATTR_PULSE_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587008 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **FALSE**.

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse_1ga5a91e8262c667bee0d1150eb431888b9.html language=enus -->
## TOPIC 00006: RFMXPULSE_ATTR_PULSE_AMPLITUDE_TRACE_UNIT

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse_1ga5a91e8262c667bee0d1150eb431888b9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse_1ga5a91e8262c667bee0d1150eb431888b9.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit of the amplitude level. This attribute is applicable only for the amplitude and acquired amplitude trace. SyntaxRFMXPULSE_ATTR_PULSE_AMPLITUDE_TRACE_UNITNumeric ValueData TypeAccessApplies To12587228int32Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXPULSE_ATTR_PULSE_AMPLITUDE_TRACE_UNIT

Specifies the unit of the amplitude level. This attribute is applicable only for the amplitude and acquired amplitude trace.

#### Syntax

RFMXPULSE_ATTR_PULSE_AMPLITUDE_TRACE_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587228 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dBm**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_PULSE_AMPLITUDE_TRACE_UNIT_DBM | 0 (0x0) | Amplitude trace is expressed in dBm. |
| RFMXPULSE_VAL_PULSE_AMPLITUDE_TRACE_UNIT_VOLTS | 1 (0x1) | Amplitude trace is expressed in Volts. |
| RFMXPULSE_VAL_PULSE_AMPLITUDE_TRACE_UNIT_WATTS | 2 (0x2) | Amplitude trace is expressed in Watts. |

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace.html language=enus -->
## TOPIC 00007: Acquisition Trace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECTSpecifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to RFMXPULSE_ATTR_MAXIMUM_PULSE_COUNT_ENABLED attribute if set to True. RFMXPULSE_ATTR_PULSE_AC

### Acquisition Trace

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT | Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to RFMXPULSE_ATTR_MAXIMUM_PULSE_COUNT_ENABLED attribute if set to True. |
| RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_LENGTH | Specifies the total number of pulses starting from offset to be used for display acquisition trace. You must configure this attribute when you set the RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT attribute to Subset. |
| RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_OFFSET | Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this attribute when you set the RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT attribute to Subset. |

#### Attachments

None

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga33dae866996a1dbda5cfab3383e3a3e3.html language=enus -->
## TOPIC 00008: RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga33dae866996a1dbda5cfab3383e3a3e3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga33dae866996a1dbda5cfab3383e3a3e3.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to RFMXPULSE_ATTR_MAXIMUM_PULSE_COUNT_ENABLED attribute if set to True. SyntaxRFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECTNumeric ValueData TypeAccessApplies To12587278int32Read

### RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT

Specifies the mode to select all pulses or the subset of acquired pulses available for display acquisition trace, limited to [RFMXPULSE_ATTR_MAXIMUM_PULSE_COUNT_ENABLED](group____root__ni_r_fmx_pulse__attributes__maximum__pulse__count_1ga4f10900065a47571c3996b482c9b31c0.html) attribute if set to **True**.

#### Syntax

RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587278 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Subset**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_PULSE_ACQUISITION_TRACE_SELECT_ALL_PULSES | 0 (0x0) | Selects all the acquired pulses. |
| RFMXPULSE_VAL_PULSE_ACQUISITION_TRACE_SELECT_SUBSET | 1 (0x1) |  |

Parent topic:

Acquisition Trace

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga84a630f975688d335611869a70b9f5d8.html language=enus -->
## TOPIC 00009: RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_OFFSET

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga84a630f975688d335611869a70b9f5d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga84a630f975688d335611869a70b9f5d8.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this attribute when you set the RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT attribute to Subset. SyntaxRFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_OFFSETNumeric ValueData TypeAccessApplies To125

### RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_OFFSET

Specifies the offset in number of pulses to be used for display acquisition trace. You must configure this attribute when you set the [RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT](group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga33dae866996a1dbda5cfab3383e3a3e3.html) attribute to **Subset**.

#### Syntax

RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SUBSET_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587279 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0. Valid values are 0 to 9999, inclusive.

Parent topic:

Acquisition Trace

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__detection_1ga301f374491aebec1535444e86c69d73b.html language=enus -->
## TOPIC 00010: RFMXPULSE_ATTR_PULSE_DETECTION_THRESHOLD

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__detection_1ga301f374491aebec1535444e86c69d73b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__detection_1ga301f374491aebec1535444e86c69d73b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the RFMXPULSE_ATTR_PULSE_DETECTION_REFERENCE attribute. SyntaxRFMXPULSE_ATTR_PULSE_DETECTION_THRESHOLDNumeric ValueData TypeAccessApplies To12587011float64Read/WriteN/ARemarks You do not need to use

### RFMXPULSE_ATTR_PULSE_DETECTION_THRESHOLD

Specifies the threshold used for pulse detection. The unit dB or dBm is based on the value you set to the [RFMXPULSE_ATTR_PULSE_DETECTION_REFERENCE](group____root__ni_r_fmx_pulse__attributes__pulse__detection_1gafbf4cdc7b765416a7782b2516a4857ed.html) attribute.

#### Syntax

RFMXPULSE_ATTR_PULSE_DETECTION_THRESHOLD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587011 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -20. Valid values are -100 to 100, inclusive.

Parent topic:

Detection

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__detection_1ga64dbcd2b93a6e1e2e74c658f993adaf7.html language=enus -->
## TOPIC 00011: RFMXPULSE_ATTR_PULSE_DETECTION_MINIMUM_OFF_DURATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__detection_1ga64dbcd2b93a6e1e2e74c658f993adaf7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__detection_1ga64dbcd2b93a6e1e2e74c658f993adaf7.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_DETECTION_MINIMUM_OFF_DURATIONNumeric ValueData TypeAccessApplies To12587013float64Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXPULSE_ATTR_PULSE_DETECTION_MINIMUM_OFF_DURATION

Specifies the minimum pulse off duration to be ignored by the pulse detection. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_DETECTION_MINIMUM_OFF_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587013 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.00000005. Valid values are 0 to 0.001, inclusive.

Parent topic:

Detection

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__detection_1gadd7b169d67aa0b9d960b4042197fe6b0.html language=enus -->
## TOPIC 00012: RFMXPULSE_ATTR_PULSE_DETECTION_HYSTERESIS

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__detection_1gadd7b169d67aa0b9d960b4042197fe6b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__detection_1gadd7b169d67aa0b9d960b4042197fe6b0.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the hysteresis for pulse detection in dB for the defined threshold. SyntaxRFMXPULSE_ATTR_PULSE_DETECTION_HYSTERESISNumeric ValueData TypeAccessApplies To12587012float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal i

### RFMXPULSE_ATTR_PULSE_DETECTION_HYSTERESIS

Specifies the hysteresis for pulse detection in dB for the defined threshold.

#### Syntax

RFMXPULSE_ATTR_PULSE_DETECTION_HYSTERESIS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587012 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1. Valid values are 0 to 50, inclusive.

Parent topic:

Detection

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase.html language=enus -->
## TOPIC 00013: Frequency and Phase

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDeviation RangeDeviation RangeGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSETSpecifies to manually enter the CW frequency offset. This attribute is valid only when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE attribute to CW. RFM

### Frequency and Phase

#### Groups

- Deviation Range
- Deviation Range

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET | Specifies to manually enter the CW frequency offset. This attribute is valid only when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE attribute to CW. |
| RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET_AUTO | Specifies whether the CW frequency offset computation of every detected pulse is automatic or manual. This attribute is valid only when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE attribute to CW. |
| RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE | Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. |

#### Attachments

None

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase_1ga24db13e4244e76716ecc87893bd69b2a.html language=enus -->
## TOPIC 00014: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase_1ga24db13e4244e76716ecc87893bd69b2a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase_1ga24db13e4244e76716ecc87893bd69b2a.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to manually enter the CW frequency offset. This attribute is valid only when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE attribute to CW. SyntaxRFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSETNumeric ValueData TypeAccessApplies To12587165float64Read/Wri

### RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET

Specifies to manually enter the CW frequency offset. This attribute is valid only when you set the [RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE](group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase_1gaad3bca7ba3801e786d2b5c4ad7ee93b9.html) attribute to **CW**.

#### Syntax

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587165 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase_1gaad3bca7ba3801e786d2b5c4ad7ee93b9.html language=enus -->
## TOPIC 00015: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase_1gaad3bca7ba3801e786d2b5c4ad7ee93b9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase_1gaad3bca7ba3801e786d2b5c4ad7ee93b9.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement. SyntaxRFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPENumeric ValueData TypeAccessApplies To12587163int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read t

### RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE

Specifies the pulse modulation type used for the phase and frequency error, and pulsed FM Measurement.

#### Syntax

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587163 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **CW**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_PULSE_MODULATION_TYPE_CW | 0 (0x0) | Continous wave where the frequency remains constant over pulse ON duration. |
| RFMXPULSE_VAL_PULSE_MODULATION_TYPE_LINEAR_FM | 1 (0x1) | Frequency varies linearly within pulse ON duration. |
| RFMXPULSE_VAL_PULSE_MODULATION_TYPE_TRIANGULAR_FM | 2 (0x2) | Frequency varies with two lienar FM chirps with opposite slopes within pulse ON duration. |

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase__deviation__range.html language=enus -->
## TOPIC 00016: Deviation Range

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase__deviation__range.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase__deviation__range.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STARTSpecifies the start of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute t

### Deviation Range

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_START | Specifies the start of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute to Edge. |
| RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOP | Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute to Edge. |
| RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH | Specifies the length of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute to Center. |

#### Attachments

None

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase__deviation__range_1ga3bf5a0e3322db34d8fd0ab2bcbd4bc99.html language=enus -->
## TOPIC 00017: RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOP

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase__deviation__range_1ga3bf5a0e3322db34d8fd0ab2bcbd4bc99.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase__deviation__range_1ga3bf5a0e3322db34d8fd0ab2bcbd4bc99.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE attribute to Edge. SyntaxRFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOPNumeric ValueData TypeAcce

### RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOP

Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the [RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE](group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase____deviation__range_1ga0c87f1741aea9b011233d160e2228772.html) attribute to **Edge**.

#### Syntax

RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587152 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Deviation Range

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__level_1gacc3bd577a3366e5ffd4f9f4baf9aea29.html language=enus -->
## TOPIC 00018: RFMXPULSE_ATTR_PULSE_LOWER_THRESHOLD_LEVEL

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__level_1gacc3bd577a3366e5ffd4f9f4baf9aea29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__level_1gacc3bd577a3366e5ffd4f9f4baf9aea29.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge. SyntaxRFMXPULSE_ATTR_PULSE_LOWER_THRESHOLD_LEVELNumeric ValueData TypeAccessApplies To12587020float64Read/WriteN/ARemarks You do not need to use a selector strin

### RFMXPULSE_ATTR_PULSE_LOWER_THRESHOLD_LEVEL

Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.

#### Syntax

RFMXPULSE_ATTR_PULSE_LOWER_THRESHOLD_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587020 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10. Valid values are 0 to 100, inclusive.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__level_1gadd038f20a1fbee8dd85f9ca183424be9.html language=enus -->
## TOPIC 00019: RFMXPULSE_ATTR_PULSE_LEVEL_COMPUTATION_METHOD

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__level_1gadd038f20a1fbee8dd85f9ca183424be9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__level_1gadd038f20a1fbee8dd85f9ca183424be9.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in IEEE Std 181-2011. SyntaxRFMXPULSE_ATTR_PULSE_LEVEL_COMPUTATION_METHODNumeric ValueData TypeAccessApplies To12587016int32Read/WriteN/ARemarks You do not need to us

### RFMXPULSE_ATTR_PULSE_LEVEL_COMPUTATION_METHOD

Specifies the algorithm used to detect the pulse levels. The algorithm is based on the histogram method of level detection as defined in *IEEE Std 181-2011*.

#### Syntax

RFMXPULSE_ATTR_PULSE_LEVEL_COMPUTATION_METHOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587016 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Median**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_PULSE_LEVEL_COMPUTATION_METHOD_MEAN | 0 (0x0) | The levels derived as the pulse sub-histogram mean levels. |
| RFMXPULSE_VAL_PULSE_LEVEL_COMPUTATION_METHOD_MEDIAN | 1 (0x1) | The levels derived as the pulse sub-histogram median levels. |
| RFMXPULSE_VAL_PULSE_LEVEL_COMPUTATION_METHOD_MODE | 2 (0x2) | The levels derived as the pulse sub-histogram mode levels. |

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point.html language=enus -->
## TOPIC 00020: Measurement Point

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_AVERAGING_DURATIONSpecifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_OFFSETSpecifies the time offset of the measu

### Measurement Point

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_AVERAGING_DURATION | Specifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. |
| RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_OFFSET | Specifies the time offset of the measurement point within the pulse for phase, frequency, and stability measurements. |
| RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_REFERENCE | Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. |

#### Attachments

None

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point_1ga633ae5b53dea7f955697b6ebc79844e0.html language=enus -->
## TOPIC 00021: RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_AVERAGING_DURATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point_1ga633ae5b53dea7f955697b6ebc79844e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point_1ga633ae5b53dea7f955697b6ebc79844e0.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally. SyntaxRFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_AVERAGING_DURATIONNumeric ValueData TypeAccessApplies To12587148float64Read/WriteN/ARemarks You do not need to use a selector string

### RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_AVERAGING_DURATION

Specifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally.

#### Syntax

RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_AVERAGING_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587148 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Measurement Point

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point_1ga7249a28fbf82a2b3f80afbbd394c1b6b.html language=enus -->
## TOPIC 00022: RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_REFERENCE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point_1ga7249a28fbf82a2b3f80afbbd394c1b6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__measurement__point_1ga7249a28fbf82a2b3f80afbbd394c1b6b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset. SyntaxRFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_REFERENCENumeric ValueData TypeAccessApplies To12587146int32Read/WriteN/ARe

### RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_REFERENCE

Specifies the reference used for the measurement point calculation, in phase, frequency, and stability measurements. You can set measurement point based on a reference and offset.

#### Syntax

RFMXPULSE_ATTR_PULSE_MEASUREMENT_POINT_REFERENCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587146 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Center**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_PULSE_MEASUREMENT_POINT_REFERENCE_RISE | 0 (0x0) | The measurement point is defined in reference to the rising edge. |
| RFMXPULSE_VAL_PULSE_MEASUREMENT_POINT_REFERENCE_CENTER | 1 (0x1) | The measurement point is defined in reference to the center of the pulse. |
| RFMXPULSE_VAL_PULSE_MEASUREMENT_POINT_REFERENCE_FALL | 2 (0x2) | The measurement point is defined in reference to the falling edge. |

Parent topic:

Measurement Point

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__metrics_1gacaba2e44e2164ebd778a2f5f2de86690.html language=enus -->
## TOPIC 00023: RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__metrics_1gacaba2e44e2164ebd778a2f5f2de86690.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__metrics_1gacaba2e44e2164ebd778a2f5f2de86690.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit for amplitude deviation results. This attribute is applicable only for droop, ripple and overshoot results. SyntaxRFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNITNumeric ValueData TypeAccessApplies To12587229int32Read/WriteN/ARemarks You do not need to use a selector string t

### RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT

Specifies the unit for amplitude deviation results. This attribute is applicable only for droop, ripple and overshoot results.

#### Syntax

RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587229 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Percentage**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT_PERCENTAGE | 0 (0x0) | Amplitude deviation results are returned as a percentage. |
| RFMXPULSE_VAL_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT_DB | 1 (0x1) | Amplitude deviation results are returned in dB. |

Parent topic:

Metrics

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__multiburst.html language=enus -->
## TOPIC 00024: Multiburst

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__multiburst.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__multiburst.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_MULTIBURST_ENABLEDSpecifies whether to enable pulse measurements on the multiple burst transmission. RFMXPULSE_ATTR_PULSE_MULTIBURST_LENGTHSpecifies the number of pulses assigned to a single burst. AttachmentsNone

### Multiburst

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_MULTIBURST_ENABLED | Specifies whether to enable pulse measurements on the multiple burst transmission. |
| RFMXPULSE_ATTR_PULSE_MULTIBURST_LENGTH | Specifies the number of pulses assigned to a single burst. |

#### Attachments

None

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__multiple__measurement__points__window_1gaa0c8f92a4f5dabe5e0ac1bd318b4c505.html language=enus -->
## TOPIC 00025: RFMXPULSE_ATTR_PULSE_MULTIPLE_MEASUREMENT_POINTS_WINDOW_STOP

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__multiple__measurement__points__window_1gaa0c8f92a4f5dabe5e0ac1bd318b4c505.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__multiple__measurement__points__window_1gaa0c8f92a4f5dabe5e0ac1bd318b4c505.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop of the measurement window used for multiple measurement points selection over pulse ON duration. SyntaxRFMXPULSE_ATTR_PULSE_MULTIPLE_MEASUREMENT_POINTS_WINDOW_STOPNumeric ValueData TypeAccessApplies To12587237float64Read/WriteN/ARemarks You do not need to use a selector string to

### RFMXPULSE_ATTR_PULSE_MULTIPLE_MEASUREMENT_POINTS_WINDOW_STOP

Specifies the stop of the measurement window used for multiple measurement points selection over pulse ON duration.

#### Syntax

RFMXPULSE_ATTR_PULSE_MULTIPLE_MEASUREMENT_POINTS_WINDOW_STOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587237 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 80. Valid values are 0 to 100, inclusive.

Parent topic:

Window

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results.html language=enus -->
## TOPIC 00026: Results

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsFM ChirpFrequency and PhaseLevelStabilityTimeTime SidelobeGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_RESULTS_BURST_INDEXReturns the burst indices of all the measured pulses. RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_COUNTReturns the measured pulse count. RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_POSIT

### Results

#### Groups

- FM Chirp
- Frequency and Phase
- Level
- Stability
- Time
- Time Sidelobe

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_RESULTS_BURST_INDEX | Returns the burst indices of all the measured pulses. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_COUNT | Returns the measured pulse count. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_POSITION_INDEX | Returns the position indices of all the measured pulses within a burst. |

#### Attachments

None

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results_1gadfab320ddea4317df3f6d7d7b7b5d3ac.html language=enus -->
## TOPIC 00027: RFMXPULSE_ATTR_PULSE_RESULTS_BURST_INDEX

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results_1gadfab320ddea4317df3f6d7d7b7b5d3ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results_1gadfab320ddea4317df3f6d7d7b7b5d3ac.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst indices of all the measured pulses. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_BURST_INDEXNumeric ValueData TypeAccessApplies To12587233Aint32Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strin

### RFMXPULSE_ATTR_PULSE_RESULTS_BURST_INDEX

Returns the burst indices of all the measured pulses.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_BURST_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587233 | Aint32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp.html language=enus -->
## TOPIC 00028: FM Chirp

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATEReturns the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENG

### FM Chirp

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE | Returns the frequency slope rate of a best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for each pulse. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2 | Returns the frequency slope rate of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_MAXIMUM | Returns the maximum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_MEAN | Returns the mean of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_MINIMUM | Returns the minimum FM chirp rate2 value across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE2_STANDARD_DEVIATION | Returns the standard deviation of the FM chirp rate2 values across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MAXIMUM | Returns the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MEAN | Returns the mean of the FM chirp rates across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MINIMUM | Returns the minimum FM chirp rate across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_STANDARD_DEVIATION | Returns the standard deviation of the FM chirp rates across the measured pulses. This value is expressed in Hz/us. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY | Returns the start frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2 | Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MAXIMUM | Returns the maximum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MEAN | Returns the mean of the FM chirp start frequency2 across the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MINIMUM | Returns the minimum FM chirp start frequency2 among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_STANDARD_DEVIATION | Returns the FM chirp start frequency2 standard deviation across the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MAXIMUM | Returns the maximum FM chirp start frequency among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MEAN | Returns the mean of the FM chirp start frequency across the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MINIMUM | Returns the minimum FM chirp start frequency among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_STANDARD_DEVIATION | Returns the FM chirp start frequency standard deviation across the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY | Returns the stop frequencies of the best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2 | Returns the stop frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MAXIMUM | Returns the maximum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MEAN | Returns the mean of the FM chirp stop frequency2 across the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MINIMUM | Returns the minimum FM chirp stop frequency2 among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_STANDARD_DEVIATION | Returns the FM chirp stop frequency2 standard deviation across the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MAXIMUM | Returns the maximum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEAN | Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MINIMUM | Returns the minimum FM chirp stop frequency among the measured pulses. This value is expressed in Hz. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_STANDARD_DEVIATION | Returns the FM chirp stop frequency standard deviation across the measured pulses. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1ga2d73b0ba6e2fd8dbf7672cb1c16975bf.html language=enus -->
## TOPIC 00029: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1ga2d73b0ba6e2fd8dbf7672cb1c16975bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1ga2d73b0ba6e2fd8dbf7672cb1c16975bf.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MAXIMUMNumeric ValueData TypeAccessApplies To12587190float64Read-OnlyN/ARemarks This result is valid for linear FM and triangular FM modulation.You do not

### RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MAXIMUM

Returns the maximum FM chirp rate across the measured pulses. This value is expressed in Hz/us.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_RATE_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587190 | float64 | Read-Only | N/A |

#### Remarks

This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

FM Chirp

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1gaafd53b38b4b75dd4af390945d51913fd.html language=enus -->
## TOPIC 00030: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1gaafd53b38b4b75dd4af390945d51913fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1gaafd53b38b4b75dd4af390945d51913fd.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH attribute for the measured pulses. This value is expressed in Hz. SyntaxRFMX

### RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2

Returns the start frequency of the 2nd best-fit linear least square regression line measured over user specified sample analysis time interval as determined by [RFMXPULSE_ATTR_PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH](group____root__ni_r_fmx_pulse__attributes__pulse__frequency__and__phase__deviation__range_1gacc09490c4bc5570959cca9418a8da0ba.html) attribute for the measured pulses. This value is expressed in Hz.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587218 | Adouble | Read-Only | N/A |

#### Remarks

This result is valid only for triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

FM Chirp

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1gac176290ee6d31438965e7cf3f6c76262.html language=enus -->
## TOPIC 00031: RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1gac176290ee6d31438965e7cf3f6c76262.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__fm__chirp_1gac176290ee6d31438965e7cf3f6c76262.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEANNumeric ValueData TypeAccessApplies To12587199float64Read-OnlyN/ARemarks This result is valid for linear FM and triangular FM modu

### RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEAN

Returns the mean of the FM chirp stop frequency across the measured pulses. This value is expressed in Hz.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587199 | float64 | Read-Only | N/A |

#### Remarks

This result is valid for linear FM and triangular FM modulation.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

FM Chirp

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga019437d78ae63af774a6b40d5030c2ce.html language=enus -->
## TOPIC 00032: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga019437d78ae63af774a6b40d5030c2ce.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga019437d78ae63af774a6b40d5030c2ce.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MEANNumeric ValueData TypeAccessApplies To12587105float64Read-OnlyN/ARemarks You do not need to use a selector st

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MEAN

Returns the mean of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587105 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga025b11f6bfb06cdb7a335a0221edebaf.html language=enus -->
## TOPIC 00033: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga025b11f6bfb06cdb7a335a0221edebaf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga025b11f6bfb06cdb7a335a0221edebaf.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCENumeric ValueData TypeAccessApplies To12587119AdoubleRead-OnlyN/ARemarks You do not need to use a sele

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE

Returns the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587119 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga3a56e82b076290c2cd6ef44a5bbb30e7.html language=enus -->
## TOPIC 00034: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_FREQUENCY_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga3a56e82b076290c2cd6ef44a5bbb30e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga3a56e82b076290c2cd6ef44a5bbb30e7.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_FREQUENCY_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587118float64Read-OnlyN/ARemarks You do not need to use a selector string

### RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_FREQUENCY_STANDARD_DEVIATION

Returns the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_FREQUENCY_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587118 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga53e9bff92052f9e301bdf34be6c6a79b.html language=enus -->
## TOPIC 00035: RFMXPULSE_ATTR_PULSE_RESULTS_FREQUENCY_DEVIATION_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga53e9bff92052f9e301bdf34be6c6a79b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga53e9bff92052f9e301bdf34be6c6a79b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_FREQUENCY_DEVIATION_MEANNumeric ValueData TypeAccessApplies To12587125float64Read-OnlyN/ARemarks You do not need to use a selector string to read this re

### RFMXPULSE_ATTR_PULSE_RESULTS_FREQUENCY_DEVIATION_MEAN

Returns the mean of the peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_FREQUENCY_DEVIATION_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587125 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga70f1c216a02494c2614268399379659c.html language=enus -->
## TOPIC 00036: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga70f1c216a02494c2614268399379659c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1ga70f1c216a02494c2614268399379659c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum RMS phase error across the measured pulses. This value is expressed in degrees. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MAXIMUMNumeric ValueData TypeAccessApplies To12587168float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for defa

### RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MAXIMUM

Returns the maximum RMS phase error across the measured pulses. This value is expressed in degrees.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_ERROR_RMS_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587168 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1gaa5df306388213a4242dbe0a6f945094a.html language=enus -->
## TOPIC 00037: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1gaa5df306388213a4242dbe0a6f945094a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1gaa5df306388213a4242dbe0a6f945094a.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MAXIMUMNumeric ValueData TypeAccessApplies To12587106float64Read-OnlyN/ARemarks You do not need to use a selector str

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MAXIMUM

Returns the maximum pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587106 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1gaf74f139cf5538a09a6ee892b5ff77d5f.html language=enus -->
## TOPIC 00038: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1gaf74f139cf5538a09a6ee892b5ff77d5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__frequency__and__phase_1gaf74f139cf5538a09a6ee892b5ff77d5f.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587108float64Read-OnlyN/ARemarks You do n

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_STANDARD_DEVIATION

Returns the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587108 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Frequency and Phase

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga413418a491ab51729c6d3e046c00fb29.html language=enus -->
## TOPIC 00039: RFMXPULSE_ATTR_PULSE_RESULTS_PEAK_LEVEL_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga413418a491ab51729c6d3e046c00fb29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga413418a491ab51729c6d3e046c00fb29.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PEAK_LEVEL_MEANNumeric ValueData TypeAccessApplies To12587040float64Read-OnlyN/ARemarks You do not need to use a selector string to read th

### RFMXPULSE_ATTR_PULSE_RESULTS_PEAK_LEVEL_MEAN

Returns the mean of the peak power levels during the pulse period across the measured pulses. This value is expressed in dBm.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PEAK_LEVEL_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587040 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga4ca8bf841e49fd2c6022a39612b38f18.html language=enus -->
## TOPIC 00040: RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MINIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga4ca8bf841e49fd2c6022a39612b38f18.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga4ca8bf841e49fd2c6022a39612b38f18.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum top level across the measured pulses. This value is expressed in dBm. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MINIMUMNumeric ValueData TypeAccessApplies To12587027float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and r

### RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MINIMUM

Returns the minimum top level across the measured pulses. This value is expressed in dBm.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587027 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga5a0619ca03d910937cea117c27a3e217.html language=enus -->
## TOPIC 00041: RFMXPULSE_ATTR_PULSE_RESULTS_OVERSHOOT_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga5a0619ca03d910937cea117c27a3e217.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga5a0619ca03d910937cea117c27a3e217.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT attribute. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_OVERSHOOT_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies T

### RFMXPULSE_ATTR_PULSE_RESULTS_OVERSHOOT_STANDARD_DEVIATION

Returns the standard deviation of the overshoot values computed for all measured pulses. This value is expressed in units specified by [RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT](group____root__ni_r_fmx_pulse__attributes__pulse__metrics_1gacaba2e44e2164ebd778a2f5f2de86690.html) attribute.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_OVERSHOOT_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587053 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga62cce515795c59d7303532b8d387c7bf.html language=enus -->
## TOPIC 00042: RFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVEL_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga62cce515795c59d7303532b8d387c7bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga62cce515795c59d7303532b8d387c7bf.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum base level across the measured pulses. This value is expressed in dBm. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVEL_MAXIMUMNumeric ValueData TypeAccessApplies To12587031float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and

### RFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVEL_MAXIMUM

Returns the maximum base level across the measured pulses. This value is expressed in dBm.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVEL_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587031 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga6794e942ec4241875f3b4a062dded102.html language=enus -->
## TOPIC 00043: RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga6794e942ec4241875f3b4a062dded102.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga6794e942ec4241875f3b4a062dded102.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum top level across the measured pulses. This value is expressed in dBm. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MAXIMUMNumeric ValueData TypeAccessApplies To12587026float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and r

### RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MAXIMUM

Returns the maximum top level across the measured pulses. This value is expressed in dBm.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TOP_LEVEL_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587026 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga821a2140bb1c396784630551d2316e31.html language=enus -->
## TOPIC 00044: RFMXPULSE_ATTR_PULSE_RESULTS_RIPPLE_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga821a2140bb1c396784630551d2316e31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga821a2140bb1c396784630551d2316e31.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT attribute. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_RIPPLE_MEANNumeric ValueData TypeAccessApplies To12587060float64Read-OnlyN/ARemark

### RFMXPULSE_ATTR_PULSE_RESULTS_RIPPLE_MEAN

Returns the mean of the ripple values computed for all measured pulses. This value is expressed in units specified by [RFMXPULSE_ATTR_PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT](group____root__ni_r_fmx_pulse__attributes__pulse__metrics_1gacaba2e44e2164ebd778a2f5f2de86690.html) attribute.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_RIPPLE_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587060 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga88d673c8fd7b7430f59ed9757dcc02b8.html language=enus -->
## TOPIC 00045: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga88d673c8fd7b7430f59ed9757dcc02b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1ga88d673c8fd7b7430f59ed9757dcc02b8.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power levels during the pulse period for all measured pulses. The values are expressed in dBm. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVELNumeric ValueData TypeAccessApplies To12587044AdoubleRead-OnlyN/ARemarks You do not need to use a selector string to read this result for

### RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL

Returns the average power levels during the pulse period for all measured pulses. The values are expressed in dBm.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587044 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1gad8d2578aad4094ee09512bd2db6e2d11.html language=enus -->
## TOPIC 00046: RFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVEL

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1gad8d2578aad4094ee09512bd2db6e2d11.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__level_1gad8d2578aad4094ee09512bd2db6e2d11.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the base levels for all measured pulses. The values are expressed in dBm. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVELNumeric ValueData TypeAccessApplies To12587029AdoubleRead-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result instance.

### RFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVEL

Returns the base levels for all measured pulses. The values are expressed in dBm.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_BASE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587029 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Level

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga148d6e5c00817e121657eeb3decc8cf4.html language=enus -->
## TOPIC 00047: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga148d6e5c00817e121657eeb3decc8cf4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga148d6e5c00817e121657eeb3decc8cf4.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the phase stability standard deviation across the measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587138float64Read-OnlyN/ARemarks You do not need to use a selector string to read thi

### RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_STANDARD_DEVIATION

Returns the phase stability standard deviation across the measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587138 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Stability

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga611c2365a8cbca23ea8fca2a6bcc223a.html language=enus -->
## TOPIC 00048: RFMXPULSE_ATTR_PULSE_RESULTS_TOTAL_STABILITY_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga611c2365a8cbca23ea8fca2a6bcc223a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga611c2365a8cbca23ea8fca2a6bcc223a.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum total stability across the measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TOTAL_STABILITY_MAXIMUMNumeric ValueData TypeAccessApplies To12587141float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default s

### RFMXPULSE_ATTR_PULSE_RESULTS_TOTAL_STABILITY_MAXIMUM

Returns the maximum total stability across the measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TOTAL_STABILITY_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587141 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Stability

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga6ff5824b8ab1612f98d358ad046117e2.html language=enus -->
## TOPIC 00049: RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga6ff5824b8ab1612f98d358ad046117e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1ga6ff5824b8ab1612f98d358ad046117e2.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the phase stability values across the measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_MEANNumeric ValueData TypeAccessApplies To12587135float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for d

### RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_MEAN

Returns the mean of the phase stability values across the measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PHASE_STABILITY_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587135 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Stability

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gaba86e5cd9643286763912e8fcffa9f81.html language=enus -->
## TOPIC 00050: RFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gaba86e5cd9643286763912e8fcffa9f81.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gaba86e5cd9643286763912e8fcffa9f81.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum amplitude stability across the measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_MAXIMUMNumeric ValueData TypeAccessApplies To12587131float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for d

### RFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_MAXIMUM

Returns the maximum amplitude stability across the measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587131 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Stability

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gad1cee34bc1087f45c0ef35c89d654ed5.html language=enus -->
## TOPIC 00051: RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_TOTAL_STABILITY

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gad1cee34bc1087f45c0ef35c89d654ed5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gad1cee34bc1087f45c0ef35c89d654ed5.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average total stability over measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_TOTAL_STABILITYNumeric ValueData TypeAccessApplies To12587159float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal

### RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_TOTAL_STABILITY

Returns the average total stability over measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_AVERAGE_TOTAL_STABILITY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587159 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Stability

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gaef8b818c25ed7fb4528b69a95e61bd23.html language=enus -->
## TOPIC 00052: RFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gaef8b818c25ed7fb4528b69a95e61bd23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__stability_1gaef8b818c25ed7fb4528b69a95e61bd23.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the amplitude stability standard deviation across the measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587133float64Read-OnlyN/ARemarks You do not need to use a selector string to

### RFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_STANDARD_DEVIATION

Returns the amplitude stability standard deviation across the measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_AMPLITUDE_STABILITY_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587133 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Stability

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time.html language=enus -->
## TOPIC 00053: Time

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLEReturns the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MAXIMUMReturns the ma

### Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE | Returns the duty cycle values for all measured pulses. Duty cycle is the ratio of pulse ON duration to the pulse period. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MAXIMUM | Returns the maximum duty cycle across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MEAN | Returns the mean of duty cycle values across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_MINIMUM | Returns the minimum duty cycle across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_DUTY_CYCLE_STANDARD_DEVIATION | Returns the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FALL_EDGE | Returns the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME | Returns the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MAXIMUM | Returns the maximum fall time across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MEAN | Returns the mean of the fall time values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MINIMUM | Returns the minimum fall time across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_STANDARD_DEVIATION | Returns the standard deviation of the fall time values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION | Returns the OFF duration values for all measured pulses. OFF duration value is the duration of the pulse for the first falling-edge and the subsequent rising-edge transition at width threshold. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_MAXIMUM | Returns the maximum OFF duration across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_MEAN | Returns the mean of the OFF duration values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_MINIMUM | Returns the minimum OFF duration across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATION | Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL | Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MAXIMUM | Returns the maximum pulse period across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MEAN | Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MINIMUM | Returns the minimum pulse period across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_STANDARD_DEVIATION | Returns the standard deviation of pulse period values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH | Returns the ON duration for all measured pulses. ON duration value is the duration of the pulse for the first rising-edge and the subsequent falling-edge transition at width threshold. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_MAXIMUM | Returns the maximum ON duration across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_MEAN | Returns the mean of the ON duration values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_MINIMUM | Returns the minimum ON duration across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_WIDTH_STANDARD_DEVIATION | Returns the standard deviation of ON duration values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_RISE_EDGE | Returns the rise edge for all measured pulses. Rise edge is the absolute time instant when the pulse exceeds the rising edge lower threshold. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME | Returns the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MAXIMUM | Returns the maximum rise time across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MEAN | Returns the mean of the rise time values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MINIMUM | Returns the minimum rise time across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATION | Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga05568ef12602a4551cb4a6b162dcbed7.html language=enus -->
## TOPIC 00054: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MINIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga05568ef12602a4551cb4a6b162dcbed7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga05568ef12602a4551cb4a6b162dcbed7.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum rise time across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MINIMUMNumeric ValueData TypeAccessApplies To12587067float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal a

### RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MINIMUM

Returns the minimum rise time across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587067 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga21e7c0bac8210c384f417337d67c0f90.html language=enus -->
## TOPIC 00055: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga21e7c0bac8210c384f417337d67c0f90.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga21e7c0bac8210c384f417337d67c0f90.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MEANNumeric ValueData TypeAccessApplies To12587090float64Read-OnlyN/ARemarks You do not need to use a selector string to read this resu

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MEAN

Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587090 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga32379b4fdd3870988b9da9f84eff98e6.html language=enus -->
## TOPIC 00056: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga32379b4fdd3870988b9da9f84eff98e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga32379b4fdd3870988b9da9f84eff98e6.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587068float64Read-OnlyN/ARemarks You do not need to use a selector string to r

### RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATION

Returns the standard deviation of the rise time values across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587068 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga7bfb71c4d6196f70c6035a52f998ca1e.html language=enus -->
## TOPIC 00057: RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga7bfb71c4d6196f70c6035a52f998ca1e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga7bfb71c4d6196f70c6035a52f998ca1e.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIMENumeric ValueData TypeAccessApplies To12587069AdoubleRead-OnlyN/ARema

### RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME

Returns the fall time for all measured pulses. Fall time is the difference between the time when the pulse drops below the upper and lower thresholds. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587069 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga9c80ab5acae429215052a4a3e1d02ddc.html language=enus -->
## TOPIC 00058: RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga9c80ab5acae429215052a4a3e1d02ddc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1ga9c80ab5acae429215052a4a3e1d02ddc.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum fall time across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MAXIMUMNumeric ValueData TypeAccessApplies To12587071float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal a

### RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MAXIMUM

Returns the maximum fall time across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_FALL_TIME_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587071 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaa7fd01e16648dba79df6e977848fb1a4.html language=enus -->
## TOPIC 00059: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaa7fd01e16648dba79df6e977848fb1a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaa7fd01e16648dba79df6e977848fb1a4.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_I

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL

Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587089 | Adouble | Read-Only | N/A |

#### Remarks

This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gab4187946b6b2e240770cb2c4c9839dda.html language=enus -->
## TOPIC 00060: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gab4187946b6b2e240770cb2c4c9839dda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gab4187946b6b2e240770cb2c4c9839dda.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIMENumeric ValueData TypeAccessApplies To12587064AdoubleRead-OnlyN/ARemarks

### RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME

Returns the rise time for all measured pulses. Rise time is the difference between the time when the pulse exceeds the lower and upper thresholds. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587064 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gacdfa3b2a01b3c8b2c59acb461c76350e.html language=enus -->
## TOPIC 00061: RFMXPULSE_ATTR_PULSE_RESULTS_FALL_EDGE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gacdfa3b2a01b3c8b2c59acb461c76350e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gacdfa3b2a01b3c8b2c59acb461c76350e.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_FALL_EDGENumeric ValueData TypeAccessApplies To12587277AdoubleRead-OnlyN/ARemarks You

### RFMXPULSE_ATTR_PULSE_RESULTS_FALL_EDGE

Returns the fall edge for all measured pulses. Fall edge is the absolute time instant when the pulse exceeds the falling edge width threshold. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_FALL_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587277 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gacf0ce926304a466639a309f49d8a69d0.html language=enus -->
## TOPIC 00062: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MINIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gacf0ce926304a466639a309f49d8a69d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gacf0ce926304a466639a309f49d8a69d0.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum pulse period across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MINIMUMNumeric ValueData TypeAccessApplies To12587092float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result f

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MINIMUM

Returns the minimum pulse period across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587092 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gae2c85929dc464aae1abad8c403f1059c.html language=enus -->
## TOPIC 00063: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gae2c85929dc464aae1abad8c403f1059c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gae2c85929dc464aae1abad8c403f1059c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587083float64Read-OnlyN/ARemarks You do not need to use a selector str

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATION

Returns the standard deviation of OFF duration values across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587083 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaeae90136bca13f2866aecad796b354ee.html language=enus -->
## TOPIC 00064: RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_MINIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaeae90136bca13f2866aecad796b354ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaeae90136bca13f2866aecad796b354ee.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum OFF duration across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_MINIMUMNumeric ValueData TypeAccessApplies To12587082float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for defa

### RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_MINIMUM

Returns the minimum OFF duration across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_PULSE_OFF_DURATION_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587082 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaecb5736c66b0ea3418870a9f56d8ac71.html language=enus -->
## TOPIC 00065: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MEAN

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaecb5736c66b0ea3418870a9f56d8ac71.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaecb5736c66b0ea3418870a9f56d8ac71.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the rise time values across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MEANNumeric ValueData TypeAccessApplies To12587065float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default

### RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MEAN

Returns the mean of the rise time values across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587065 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaf269534b2f7fbf98ea99e0f69ba7d01c.html language=enus -->
## TOPIC 00066: RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaf269534b2f7fbf98ea99e0f69ba7d01c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time_1gaf269534b2f7fbf98ea99e0f69ba7d01c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum rise time across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MAXIMUMNumeric ValueData TypeAccessApplies To12587066float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal a

### RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MAXIMUM

Returns the maximum rise time across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_RISE_TIME_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587066 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe.html language=enus -->
## TOPIC 00067: Time Sidelobe

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIOReturns the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. RFMXPULSE_ATTR_PULSE_RESULTS_TIME

### Time Sidelobe

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO | Returns the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MAXIMUM | Returns the maximum compression ratio across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MEAN | Returns the mean of the compression ratio values across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MINIMUM | Returns the minimum compression ratio across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_STANDARD_DEVIATION | Returns the standard deviation of the compression ratio values across the measured pulses. This value is expressed as a percentage. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY | Returns the sidelobe delay for all measured pulses. Sidelobe delay is the time elapsed between the highest sidelobe peak and mainlobe peak level. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MAXIMUM | Returns the maximum sidelobe delay across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MEAN | Returns the mean of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_MINIMUM | Returns the minimum sidelobe delay across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATION | Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH | Returns the mainlobe width for all measured pulses. Mainlobe width is the width at 3dB below from its peak level. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUM | Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MEAN | Returns the mean of the mainlobe width values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUM | Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATION | Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION | Returns the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MAXIMUM | Returns the maximum peak correlation across the measured pulses. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MEAN | Returns the mean of the peak correlation values across the measured pulses. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUM | Returns the minimum peak correlation across the measured pulses. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_STANDARD_DEVIATION | Returns the standard deviation of the peak correlation values across the measured pulses. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL | Returns the peak sidelobe level for all measured pulses. Peak sidelobe level is the ratio of the highest sidelobe peak to the mainlobe peak level. This value is expressed in dB. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MAXIMUM | Returns the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MEAN | Returns the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUM | Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. |
| RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATION | Returns the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga16ab3d74a3c32b006a0b432f6235e9c9.html language=enus -->
## TOPIC 00068: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga16ab3d74a3c32b006a0b432f6235e9c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga16ab3d74a3c32b006a0b432f6235e9c9.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUMNumeric ValueData TypeAccessApplies To12587247float64Read-OnlyN/ARemarks You do not need to use a selector string to read this res

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUM

Returns the minimum mainlobe width across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587247 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga3acb052defbc3955e305bb0f46632290.html language=enus -->
## TOPIC 00069: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga3acb052defbc3955e305bb0f46632290.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga3acb052defbc3955e305bb0f46632290.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587248float64Read-OnlyN/ARemarks You do not need to us

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATION

Returns the standard deviation of the mainlobe width values across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587248 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga3f28c97d93e01ce65cd3e58e5a1d1c67.html language=enus -->
## TOPIC 00070: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga3f28c97d93e01ce65cd3e58e5a1d1c67.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga3f28c97d93e01ce65cd3e58e5a1d1c67.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum peak correlation across the measured pulses. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUMNumeric ValueData TypeAccessApplies To12587267float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and resul

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUM

Returns the minimum peak correlation across the measured pulses.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587267 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga69d25c15ecf80d41caf17cc9bcef8676.html language=enus -->
## TOPIC 00071: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga69d25c15ecf80d41caf17cc9bcef8676.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga69d25c15ecf80d41caf17cc9bcef8676.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUMNumeric ValueData TypeAccessApplies To12587246float64Read-OnlyN/ARemarks You do not need to use a selector string to read this res

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUM

Returns the maximum mainlobe width across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587246 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga70c198e26d149734b6c575210f58acb0.html language=enus -->
## TOPIC 00072: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga70c198e26d149734b6c575210f58acb0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga70c198e26d149734b6c575210f58acb0.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587253float64Read-OnlyN/ARemarks You do not need to use a selec

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATION

Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587253 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga88f4a10c4a1ae944592cdb8b8a9fa202.html language=enus -->
## TOPIC 00073: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga88f4a10c4a1ae944592cdb8b8a9fa202.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga88f4a10c4a1ae944592cdb8b8a9fa202.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIONumeric ValueData TypeAccessApplies To12587259AdoubleRead-OnlyN/A

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO

Returns the compression ratio for all measured pulses. Compression ratio is the ratio of the mainlobe width to the pulse width. This value is expressed as a percentage.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587259 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga9b0436060d86d9b3178974743f9b5f32.html language=enus -->
## TOPIC 00074: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUM

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga9b0436060d86d9b3178974743f9b5f32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1ga9b0436060d86d9b3178974743f9b5f32.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUMNumeric ValueData TypeAccessApplies To12587257float64Read-OnlyN/ARemarks You do not need to use a selector string to read thi

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUM

Returns the minimum peak sidelobe level across the measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587257 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1gadb741b675af0c213728452bc4156b376.html language=enus -->
## TOPIC 00075: RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1gadb741b675af0c213728452bc4156b376.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__results__time__sidelobe_1gadb741b675af0c213728452bc4156b376.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB. SyntaxRFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To12587258float64Read-OnlyN/ARemarks You do not need

### RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATION

Returns the standard deviation of the peak sidelobe level values across the measured pulses. This value is expressed in dB.

#### Syntax

RFMXPULSE_ATTR_PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587258 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Time Sidelobe

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__pulse__stability_1ga8dd29c13025663c02a585b942e870595.html language=enus -->
## TOPIC 00076: RFMXPULSE_ATTR_PULSE_STABILITY_FREQUENCY_ERROR_COMPENSATION

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__pulse__stability_1ga8dd29c13025663c02a585b942e870595.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__pulse__stability_1ga8dd29c13025663c02a585b942e870595.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this attribute to Off to avoid incorrect results. SyntaxRFMXPULSE_ATTR_PULSE_STABILITY_FREQUENCY_ERROR_COMPENSATIONNum

### RFMXPULSE_ATTR_PULSE_STABILITY_FREQUENCY_ERROR_COMPENSATION

Specifies whether to compute and correct the frequency offset for stability results computation. This is an optional setting and in negligible frequency error condition you must set this attribute to Off to avoid incorrect results.

#### Syntax

RFMXPULSE_ATTR_PULSE_STABILITY_FREQUENCY_ERROR_COMPENSATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587145 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **On**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_PULSE_STABILITY_FREQUENCY_ERROR_COMPENSATION_OFF | 0 (0x0) | Frequency error compensation is disabled. |
| RFMXPULSE_VAL_PULSE_STABILITY_FREQUENCY_ERROR_COMPENSATION_ON | 1 (0x1) | Frequency error compensation is enabled. |

Parent topic:

Stability

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__segmented__acquisition_1ga2c44e9db254a33910122308016399ee0.html language=enus -->
## TOPIC 00077: RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__segmented__acquisition_1ga2c44e9db254a33910122308016399ee0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__segmented__acquisition_1ga2c44e9db254a33910122308016399ee0.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced. SyntaxRFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLEDNumeric ValueData TypeAccessApplies To12582932int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED

Specifies whether to enable Segmented Acquisition. This mode is best applied when the pulses are sparsely spaced.

#### Syntax

RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12582932 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_FALSE | 0 (0x0) | Segmented acquisition is disabled. |
| RFMXPULSE_VAL_SEGMENTED_ACQUISITION_ENABLED_TRUE | 1 (0x1) | Segmented acquisition is enabled. |

Parent topic:

Segmented Acquisition

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__trigger.html language=enus -->
## TOPIC 00078: Trigger

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__trigger.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXPULSE_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. RFMXPULSE_ATTR_TRIGGER_TYPESpecifies the trigger type. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. |
| RFMXPULSE_ATTR_TRIGGER_TYPE | Specifies the trigger type. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__trigger_1ga7c61ea0ff1bf9f352b1089517a4c006a.html language=enus -->
## TOPIC 00079: RFMXPULSE_ATTR_TRIGGER_TYPE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__trigger_1ga7c61ea0ff1bf9f352b1089517a4c006a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__trigger_1ga7c61ea0ff1bf9f352b1089517a4c006a.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxRFMXPULSE_ATTR_TRIGGER_TYPENumeric ValueData TypeAccessApplies To12582916int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information about

### RFMXPULSE_ATTR_TRIGGER_TYPE

Specifies the trigger type.

#### Syntax

RFMXPULSE_ATTR_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12582916 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **None**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_TRIGGER_TYPE_NONE | 0 (0x0) | No Reference Trigger is configured. |
| RFMXPULSE_VAL_TRIGGER_TYPE_DIGITAL_EDGE | 1 (0x1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the RFMXPULSE_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE attribute. |
| RFMXPULSE_VAL_TRIGGER_TYPE_IQ_POWER_EDGE | 2 (0x2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE attribute. |
| RFMXPULSE_VAL_TRIGGER_TYPE_SOFTWARE | 3 (0x3) | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga5dac381a45800b99536113e3b9fff16c.html language=enus -->
## TOPIC 00080: RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga5dac381a45800b99536113e3b9fff16c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga5dac381a45800b99536113e3b9fff16c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXPULSE_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPENumeric ValueData TypeAccessApplies

### RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

Specifies the reference for the [RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga7ce098933aaccb63614dd93c46969acf.html) attribute. The IQ Power Edge Level Type attribute is used only when you set the [RFMXPULSE_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_pulse__attributes__trigger_1ga7c61ea0ff1bf9f352b1089517a4c006a.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12587007 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Absolute**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The value of the IQ Power Edge Level attribute is relative to the value of the RFMXPULSE_ATTR_REFERENCE_LEVEL attribute. |
| RFMXPULSE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga7ce098933aaccb63614dd93c46969acf.html language=enus -->
## TOPIC 00081: RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga7ce098933aaccb63614dd93c46969acf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga7ce098933aaccb63614dd93c46969acf.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level Type attribute to Absolute. The device asserts the trigger when the signal exce

### RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE](group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga5dac381a45800b99536113e3b9fff16c.html) attribute to **Relative** and in dBm when you set the IQ Power Edge Level Type attribute to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the [RFMXPULSE_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_pulse__attributes__trigger_1ga7c61ea0ff1bf9f352b1089517a4c006a.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12582920 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1gae48c32d723150eafa8ea9d79e562ab24.html language=enus -->
## TOPIC 00082: RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1gae48c32d723150eafa8ea9d79e562ab24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1gae48c32d723150eafa8ea9d79e562ab24.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute with the slope you specify. This attribute is us

### RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the [RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_pulse__attributes__trigger__iq__power__edge_1ga7ce098933aaccb63614dd93c46969acf.html) attribute with the slope you specify. This attribute is used only when you set the [RFMXPULSE_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_pulse__attributes__trigger_1ga7c61ea0ff1bf9f352b1089517a4c006a.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXPULSE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12582921 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXPULSE_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |
| RFMXPULSE_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00083: Minimum Quiet Time

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODESpecifi

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions.html language=enus -->
## TOPIC 00084: Functions

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedBuild StringConfigurationFetchSet and Get AttributesUtilityGroup membersNameDescriptionRFmxPulse_CloseCloses the session to the device. RFmxPulse_GetErrorRetrieves and then clears the error information for the session or the current execution thread. You must provide a char array to se

### Functions

#### Groups

- Advanced
- Build String
- Configuration
- Fetch
- Set and Get Attributes
- Utility

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_Close | Closes the session to the device. |
| RFmxPulse_GetError | Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxPulse_GetErrorString | Converts a status code returned by an RFmxPulse function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. |
| RFmxPulse_Initialize | Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. |
| RFmxPulse_Initiate | Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the RFmxPulse_WaitForMeasurementComplete function or RFmxPulse_CheckMeasurementStatus function. |
| RFmxPulse_SelectMeasurements | Enables the measurement that you specify in the Measurement parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

niRFmxPulse.h

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions_1ga42b13082fa429e93c1adc254bb9f113b.html language=enus -->
## TOPIC 00085: RFmxPulse_Initialize

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions_1ga42b13082fa429e93c1adc254bb9f113b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions_1ga42b13082fa429e93c1adc254bb9f113b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxPulse_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewS

### RFmxPulse_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxPulse_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

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
| isNewSession | [out] | int32 * | Returns RFMXPULSE_VAL_TRUE if the function created a new session, or RFMXPULSE_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions_1ga6a82c9cf3ca77714a7b24da3d77a8efa.html language=enus -->
## TOPIC 00086: RFmxPulse_GetErrorString

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions_1ga6a82c9cf3ca77714a7b24da3d77a8efa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions_1ga6a82c9cf3ca77714a7b24da3d77a8efa.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxPulse function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxPulse_GetErrorString(niRFmxInstrHandle

### RFmxPulse_GetErrorString

Converts a status code returned by an RFmxPulse function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxPulse function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions_1gaa0881ac2467ea1f8d8859b00d4d22a85.html language=enus -->
## TOPIC 00087: RFmxPulse_Initiate

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions_1gaa0881ac2467ea1f8d8859b00d4d22a85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions_1gaa0881ac2467ea1f8d8859b00d4d22a85.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in

### RFmxPulse_Initiate

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, use the [RFmxPulse_WaitForMeasurementComplete](group____root__ni_r_fmx_pulse__functions__utility_1gaef873e30375ac7a98d0a43d77d6a1a77.html) function or [RFmxPulse_CheckMeasurementStatus](group____root__ni_r_fmx_pulse__functions__utility_1ga97d29a92da47b2f60f3e546cc126ad43.html) function.

#### Syntax

int32 __stdcall RFmxPulse_Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance.Example:"""result::r1""r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced.html language=enus -->
## TOPIC 00088: Advanced

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxPulse_AbortMeasurementsStops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxPulse_Initiate function or measurement read functions. Calling this functi

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_AbortMeasurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxPulse_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error. |
| RFmxPulse_AnalyzeIQ1Waveform | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxPulse_AnalyzeIQ1WaveformSplit | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE attribute value is either IQ or IQ or Spectral. |
| RFmxPulse_ClearAllNamedResults | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxPulse_ClearNamedResult | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxPulse_CloneSignalConfiguration | Creates a new instance of a signal by copying all the attribute values from an existing signal instance. |
| RFmxPulse_CreateSignalConfiguration | Creates a new instance of a signal. |
| RFmxPulse_DeleteSignalConfiguration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxPulse_GetAllNamedResultNames | Returns all the named result names of the signal that you specify in the Selector String parameter. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1ga036bb0e4d2813b8ae320cbba420e4b57.html language=enus -->
## TOPIC 00089: RFmxPulse_AnalyzeIQ1WaveformSplit

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1ga036bb0e4d2813b8ae320cbba420e4b57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1ga036bb0e4d2813b8ae320cbba420e4b57.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxPulse_AnalyzeIQ1WaveformSplit

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxPulse_AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqI[], float32 iqQ[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxPulse_Commit](group____root__ni_r_fmx_pulse__functions__utility_1ga0a4089fa8d887fcfbd9220808c1db671.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iqI | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqQ | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1ga2e1cb9db583f368fee32ae5aecc65b21.html language=enus -->
## TOPIC 00090: RFmxPulse_CloneSignalConfiguration

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1ga2e1cb9db583f368fee32ae5aecc65b21.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1ga2e1cb9db583f368fee32ae5aecc65b21.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the attribute values from an existing signal instance. Syntaxint32 __stdcall RFmxPulse_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]n

### RFmxPulse_CloneSignalConfiguration

Creates a new instance of a signal by copying all the attribute values from an existing signal instance.

#### Syntax

int32 __stdcall RFmxPulse_CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| oldSignalName | [in] | char[] | This parameter specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::OldSigName""OldSigName" |
| newSignalName | [in] | char[] | This parameter specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::NewSigName""NewSigName" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1ga3d13c3076f7607c3471bc2fb3c87696b.html language=enus -->
## TOPIC 00091: RFmxPulse_DeleteSignalConfiguration

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1ga3d13c3076f7607c3471bc2fb3c87696b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1ga3d13c3076f7607c3471bc2fb3c87696b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. Syntaxint32 __stdcall RFmxPulse_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx

### RFmxPulse_DeleteSignalConfiguration

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

#### Syntax

int32 __stdcall RFmxPulse_DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::s1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1ga607b81989c34b09cc250b08b77642831.html language=enus -->
## TOPIC 00092: RFmxPulse_GetAllNamedResultNames

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1ga607b81989c34b09cc250b08b77642831.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1ga607b81989c34b09cc250b08b77642831.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxPulse_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *

### RFmxPulse_GetAllNamedResultNames

Returns all the named result names of the signal that you specify in the Selector String parameter.

#### Syntax

int32 __stdcall RFmxPulse_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1ga689d5681b4d59284344e7de4a0b77217.html language=enus -->
## TOPIC 00093: RFmxPulse_ClearAllNamedResults

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1ga689d5681b4d59284344e7de4a0b77217.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1ga689d5681b4d59284344e7de4a0b77217.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxPulse_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxPulse_ClearAllNamedResults

Clears all results for the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxPulse_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1ga6c012edf70783926d3570be54aaf693d.html language=enus -->
## TOPIC 00094: RFmxPulse_AbortMeasurements

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1ga6c012edf70783926d3570be54aaf693d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1ga6c012edf70783926d3570be54aaf693d.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxPulse_Initiate function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it i

### RFmxPulse_AbortMeasurements

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxPulse_Initiate](group____root__ni_r_fmx_pulse__functions_1gaa0881ac2467ea1f8d8859b00d4d22a85.html) function or measurement read functions. Calling this function is optional, unless you want to stop a measurement before it is complete. This function executes even if there is an incoming error.

#### Syntax

int32 __stdcall RFmxPulse_AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1ga700f5c3f7659fd62b5a7abdb4a0ecf1e.html language=enus -->
## TOPIC 00095: RFmxPulse_ClearNamedResult

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1ga700f5c3f7659fd62b5a7abdb4a0ecf1e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1ga700f5c3f7659fd62b5a7abdb4a0ecf1e.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. Syntaxint32 __stdcall RFmxPulse_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the R

### RFmxPulse_ClearNamedResult

Clears a result instance specified by the result name in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxPulse_ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1gad130d4fc4e91a1931a9bb78a01b84731.html language=enus -->
## TOPIC 00096: RFmxPulse_AnalyzeIQ1Waveform

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1gad130d4fc4e91a1931a9bb78a01b84731.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1gad130d4fc4e91a1931a9bb78a01b84731.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxPulse_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxPulse_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxPulse_Commit](group____root__ni_r_fmx_pulse__functions__utility_1ga0a4089fa8d887fcfbd9220808c1db671.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with the option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__advanced_1gae70fa475d1d4afe2cd465afa49878096.html language=enus -->
## TOPIC 00097: RFmxPulse_CreateSignalConfiguration

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__advanced_1gae70fa475d1d4afe2cd465afa49878096.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__advanced_1gae70fa475d1d4afe2cd465afa49878096.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxPulse_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obt

### RFmxPulse_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxPulse_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::s1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__build__string.html language=enus -->
## TOPIC 00098: Build String

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__build__string.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxPulse_BuildSignalStringAttachmentsNone

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_BuildSignalString |  |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__build__string_1ga5e5e3c3110e6e272faf6e73bd5eebc2c.html language=enus -->
## TOPIC 00099: RFmxPulse_BuildSignalString

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__build__string_1ga5e5e3c3110e6e272faf6e73bd5eebc2c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__build__string_1ga5e5e3c3110e6e272faf6e73bd5eebc2c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __stdcall RFmxPulse_BuildSignalString(int32 selectorStringLength)ParametersNameDirectionTypeDescriptionselectorStringLength[in]int32ReturnsReturns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status co

### RFmxPulse_BuildSignalString

#### Syntax

int32 __stdcall RFmxPulse_BuildSignalString(int32 selectorStringLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorStringLength | [in] | int32 |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration.html language=enus -->
## TOPIC 00100: Configuration

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTriggerGroup membersNameDescriptionRFmxPulse_AutoLevelExamines the input signal to calculate the peak power level and sets it as the value of the RFMXPULSE_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. RFmxPulse_Cfg1Referenc

### Configuration

#### Groups

- Trigger

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_AutoLevel | Examines the input signal to calculate the peak power level and sets it as the value of the RFMXPULSE_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. |
| RFmxPulse_Cfg1ReferenceWaveform | Configures the reference pulse waveform used for time sidelobe measurements. |
| RFmxPulse_Cfg1ReferenceWaveformSplit | Configures the reference pulse waveform used for time sidelobe measurements. |
| RFmxPulse_CfgExternalAttenuation | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
| RFmxPulse_CfgFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxPulse_CfgFrequencyReference | Configures the Reference Clock and the frequency reference source. |
| RFmxPulse_CfgMechanicalAttenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxPulse_CfgRF | Configures the RF attributes of the signal specified by the selector string. |
| RFmxPulse_CfgRFAttenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxPulse_CfgReferenceLevel | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| RFmxPulse_SendSoftwareEdgeTrigger | Sends a trigger to the device when you use the RFmxPulse Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1ga057b1c3a97587b13f182cdf23cc4ff84.html language=enus -->
## TOPIC 00101: RFmxPulse_CfgFrequencyReference

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1ga057b1c3a97587b13f182cdf23cc4ff84.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1ga057b1c3a97587b13f182cdf23cc4ff84.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxPulse_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Instru

### RFmxPulse_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxPulse_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXPULSE_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXPULSE_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXPULSE_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXPULSE_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXPULSE_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXPULSE_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXPULSE_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXPULSE_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXPULSE_VAL_CLK_IN_STR or RFMXPULSE_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1ga0ca7a2c2f977cbfb14938c9c381aa82f.html language=enus -->
## TOPIC 00102: RFmxPulse_CfgFrequency

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1ga0ca7a2c2f977cbfb14938c9c381aa82f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1ga0ca7a2c2f977cbfb14938c9c381aa82f.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxPulse_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[i

### RFmxPulse_CfgFrequency

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxPulse_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| centerFrequency | [in] | float64 | This parameter specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this attribute is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1ga447c4597ce6017562a8b3b9c0bdc2a6b.html language=enus -->
## TOPIC 00103: RFmxPulse_SendSoftwareEdgeTrigger

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1ga447c4597ce6017562a8b3b9c0bdc2a6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1ga447c4597ce6017562a8b3b9c0bdc2a6b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxPulse Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. Syntaxint32 __stdcall RFmxPulse_SendSoftwareEdgeTrigger(n

### RFmxPulse_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use the RFmxPulse Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger.

#### Syntax

int32 __stdcall RFmxPulse_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [RFmxPulse_Initiate](group____root__ni_r_fmx_pulse__functions_1gaa0881ac2467ea1f8d8859b00d4d22a85.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1ga5e22bd98830729362caf1c310e1cd206.html language=enus -->
## TOPIC 00104: RFmxPulse_Cfg1ReferenceWaveform

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1ga5e22bd98830729362caf1c310e1cd206.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1ga5e22bd98830729362caf1c310e1cd206.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference pulse waveform used for time sidelobe measurements. Syntaxint32 __stdcall RFmxPulse_Cfg1ReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize)ParametersNameDirectionTypeDescri

### RFmxPulse_Cfg1ReferenceWaveform

Configures the reference pulse waveform used for time sidelobe measurements.

#### Syntax

int32 __stdcall RFmxPulse_Cfg1ReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| x0 | [in] | float64 | This parameter specifies the starting time of the reference waveform. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
| referenceWaveform | [in] | NIComplexSingle[] | This parameter specifies an array of waveform samples of the reference waveform. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1ga8797fb82db9fdb70d4068638d0c42155.html language=enus -->
## TOPIC 00105: RFmxPulse_CfgMechanicalAttenuation

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1ga8797fb82db9fdb70d4068638d0c42155.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1ga8797fb82db9fdb70d4068638d0c42155.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxPulse_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wrap

### RFmxPulse_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxPulse_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXPULSE_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXPULSE_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXPULSE_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXPULSE_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXPULSE_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1gab3652f7c8bcc4ce8db8eb19c13f82a69.html language=enus -->
## TOPIC 00106: RFmxPulse_AutoLevel

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1gab3652f7c8bcc4ce8db8eb19c13f82a69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1gab3652f7c8bcc4ce8db8eb19c13f82a69.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the RFMXPULSE_ATTR_REFERENCE_LEVEL attribute. Use this function to help calculate an approximate setting for the reference level. Syntaxint32 __stdcall RFmxPulse_AutoLevel(niRFmxInstrHandle instrumentHandle, char

### RFmxPulse_AutoLevel

Examines the input signal to calculate the peak power level and sets it as the value of the [RFMXPULSE_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_pulse__attributes_1ga61f9c2c3dbacccd33963a6d6c3a8088b.html) attribute. Use this function to help calculate an approximate setting for the reference level.

#### Syntax

int32 __stdcall RFmxPulse_AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 bandwidth, float64 measurementInterval, float64 *referenceLevel)

#### Remarks

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the [RFMXPULSE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL](group____root__ni_r_fmx_pulse__attributes__advanced_1gaf270f0bbfbb9e6717fbfbb3bb7d6455d.html) attribute.

When using PXIe-5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmx Pulse Auto Level function. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function, thus reducing wear and tear, and maximizing the life time of the attenuator.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| bandwidth | [in] | float64 | This parameter specifies the bandwidth, in Hz, of the signal to be analyzed. The default value is 80 MHz. |
| measurementInterval | [in] | float64 | This parameter specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms.Auto Level function does not use any trigger for acquisition. It ignores the user-configured trigger attributes. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
| referenceLevel | [out] | float64 * | This parameter returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1gad6240af37214b13f00d79d115d2d8413.html language=enus -->
## TOPIC 00107: RFmxPulse_CfgReferenceLevel

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1gad6240af37214b13f00d79d115d2d8413.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1gad6240af37214b13f00d79d115d2d8413.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level, which represents the maximum expected power of an RF input signal. Syntaxint32 __stdcall RFmxPulse_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstr

### RFmxPulse_CfgReferenceLevel

Configures the reference level, which represents the maximum expected power of an RF input signal.

#### Syntax

int32 __stdcall RFmxPulse_CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| referenceLevel | [in] | float64 | This parameter specifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this attribute is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1gaf5729f55d2d50994c5125588a30702d2.html language=enus -->
## TOPIC 00108: RFmxPulse_CfgExternalAttenuation

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1gaf5729f55d2d50994c5125588a30702d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1gaf5729f55d2d50994c5125588a30702d2.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. Syntaxint32 __stdcall RFmxPulse_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)ParametersNameDirectionTypeDescriptioninstrumentHand

### RFmxPulse_CfgExternalAttenuation

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

#### Syntax

int32 __stdcall RFmxPulse_CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration_1gafa55697244943e3a6ae9beb828a06237.html language=enus -->
## TOPIC 00109: RFmxPulse_Cfg1ReferenceWaveformSplit

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration_1gafa55697244943e3a6ae9beb828a06237.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration_1gafa55697244943e3a6ae9beb828a06237.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference pulse waveform used for time sidelobe measurements. Syntaxint32 __stdcall RFmxPulse_Cfg1ReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize)Param

### RFmxPulse_Cfg1ReferenceWaveformSplit

Configures the reference pulse waveform used for time sidelobe measurements.

#### Syntax

int32 __stdcall RFmxPulse_Cfg1ReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| x0 | [in] | float64 | This parameter specifies the starting time of the reference waveform. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
| referenceWaveformI | [in] | float32[] | This parameter specifies an array of waveform samples of the reference waveform. |
| referenceWaveformQ | [in] | float32[] | This parameter specifies an array of waveform samples of the reference waveform. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration__trigger.html language=enus -->
## TOPIC 00110: Trigger

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration__trigger.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxPulse_CfgDigitalEdgeTriggerConfigures the device to wait for a digital edge trigger and then marks a reference point within the record. RFmxPulse_CfgIQPowerEdgeTriggerConfigures the device to wait for the complex power of the I/Q data to cross the specified

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_CfgDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| RFmxPulse_CfgIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst. |
| RFmxPulse_CfgSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| RFmxPulse_DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga2cbe84e9bd536a519baa826611db65d7.html language=enus -->
## TOPIC 00111: RFmxPulse_CfgDigitalEdgeTrigger

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga2cbe84e9bd536a519baa826611db65d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga2cbe84e9bd536a519baa826611db65d7.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxPulse_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enabl

### RFmxPulse_CfgDigitalEdgeTrigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxPulse_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
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
| digitalEdge | [in] | int32 | This parameter specifies the trigger edge to detect. The default value is Rising Edge.NameValueDescriptionRFMXPULSE_VAL_DIGITAL_EDGE_RISING_EDGE0 (0x0)The trigger asserts on the rising edge of the signal.RFMXPULSE_VAL_DIGITAL_EDGE_FALLING_EDGE1 (0x1)The trigger asserts on the falling edge of the signal. |
| Name | Value | Description |  |
| RFMXPULSE_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |  |
| RFMXPULSE_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga92574ae749806746da4aa5027d53f366.html language=enus -->
## TOPIC 00112: RFmxPulse_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga92574ae749806746da4aa5027d53f366.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga92574ae749806746da4aa5027d53f366.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxPulse_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptioni

### RFmxPulse_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxPulse_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga96ff1e5f715ca872cc8ac26b639f1568.html language=enus -->
## TOPIC 00113: RFmxPulse_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga96ff1e5f715ca872cc8ac26b639f1568.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration__trigger_1ga96ff1e5f715ca872cc8ac26b639f1568.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The qu

### RFmxPulse_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

#### Syntax

int32 __stdcall RFmxPulse_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 iqPowerEdgeLevelType, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. The default of this attribute is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope.NameValueDescriptionRFMXPULSE_VAL_IQ_POWER_EDGE_RISING_SLOPE0 (0x0)The trigger asserts when the signal power is rising.RFMXPULSE_VAL_IQ_POWER_EDGE_FALLING_SLOPE1 (0x1)The trigger asserts when the signal power is falling. |
| Name | Value | Description |  |
| RFMXPULSE_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |  |
| RFMXPULSE_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |  |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this attribute is hardware dependent. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. The default value is 0. |
| triggerMinQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual.NameValueDescriptionRFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL0 (0x0)The minimum quiet time for triggering is the value of the RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute.RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO1 (0x1)The measurement computes the minimum quiet time used for triggering. |
| Name | Value | Description |  |
| RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXPULSE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |  |
| RFMXPULSE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |  |
| triggerMinQuietTimeDuration | [in] | float64 | This parameter specifies the duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q Power Edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this attribute is hardware dependent. |
| iqPowerEdgeLevelType | [in] | int32 | This parameter specifies the reference for the IQ Power Edge Level parameter. The default value is Absolute.NameValueDescriptionRFMXPULSE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE0 (0x0)The value of the IQ Power Edge Level attribute is relative to the value of the RFMXPULSE_ATTR_REFERENCE_LEVEL attribute.RFMXPULSE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE1 (0x1)The IQ Power Edge Level attribute specifies the absolute power. |
| Name | Value | Description |  |
| RFMXPULSE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The value of the IQ Power Edge Level attribute is relative to the value of the RFMXPULSE_ATTR_REFERENCE_LEVEL attribute. |  |
| RFMXPULSE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |  |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__configuration__trigger_1gaa3c8c63fdcc1b40046d9595932380403.html language=enus -->
## TOPIC 00114: RFmxPulse_DisableTrigger

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__configuration__trigger_1gaa3c8c63fdcc1b40046d9595932380403.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__configuration__trigger_1gaa3c8c63fdcc1b40046d9595932380403.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxPulse_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrume

### RFmxPulse_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxPulse_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch.html language=enus -->
## TOPIC 00115: Fetch

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxPulse_FetchAcquiredAmplitudeTraceFetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT attribute to select all pulses or the subset of a

### Fetch

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_FetchAcquiredAmplitudeTrace | Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT attribute to select all pulses or the subset of acquired pulses. When you set the RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED attribute to False, returns a single element in the Start Indices and Start Time Stamp array. |
| RFmxPulse_FetchAmplitudeTrace | Fetches the amplitude trace of the selected pulse. |
| RFmxPulse_FetchBurstIntrapulseStabilityTrace | Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points. |
| RFmxPulse_FetchBurstSelectedPositionStabilityTrace | Fetches the burst stability trace of the selected position. |
| RFmxPulse_FetchFrequencyTrace | Fetches the frequency trace of the selected pulse. |
| RFmxPulse_FetchIQTrace | Fetches the IQ trace of the selected pulse. |
| RFmxPulse_FetchIQTraceSplit | Fetches the IQ trace of the selected pulse. |
| RFmxPulse_FetchIntrapulseStabilityTrace | Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position. |
| RFmxPulse_FetchMultipleMeasurementPointsStabilityTrace | Fetches the multiple measurement points stability trace. |
| RFmxPulse_FetchPhaseWrappedTrace | Fetches the wrapped phase trace of the selected pulse. |
| RFmxPulse_FetchPulseToPulseStabilityTrace | Fetches the pulse to pulse stability trace. |
| RFmxPulse_FetchStabilityTrace | Fetches the stability trace of the selected pulse. |
| RFmxPulse_FetchTimeSidelobeTrace | Fetches the time sidelobe trace for the selected pulse. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga0bda8babd2797991829c2004723429b8.html language=enus -->
## TOPIC 00116: RFmxPulse_FetchFrequencyTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga0bda8babd2797991829c2004723429b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga0bda8babd2797991829c2004723429b8.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency trace of the selected pulse. Syntaxint32 __stdcall RFmxPulse_FetchFrequencyTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 frequency[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescrip

### RFmxPulse_FetchFrequencyTrace

Fetches the frequency trace of the selected pulse.

#### Syntax

int32 __stdcall RFmxPulse_FetchFrequencyTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 frequency[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| frequency | [out] | float32[] | This parameter returns the frequency, in Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga23c550efbac1c7bb2c9085afef0bed38.html language=enus -->
## TOPIC 00117: RFmxPulse_FetchAmplitudeTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga23c550efbac1c7bb2c9085afef0bed38.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga23c550efbac1c7bb2c9085afef0bed38.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the amplitude trace of the selected pulse. Syntaxint32 __stdcall RFmxPulse_FetchAmplitudeTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 amplitude[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescrip

### RFmxPulse_FetchAmplitudeTrace

Fetches the amplitude trace of the selected pulse.

#### Syntax

int32 __stdcall RFmxPulse_FetchAmplitudeTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 amplitude[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| amplitude | [out] | float32[] | This parameter returns the amplitude, in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga33e31eeced08ed585179cc2fe3516437.html language=enus -->
## TOPIC 00118: RFmxPulse_FetchPhaseWrappedTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga33e31eeced08ed585179cc2fe3516437.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga33e31eeced08ed585179cc2fe3516437.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the wrapped phase trace of the selected pulse. Syntaxint32 __stdcall RFmxPulse_FetchPhaseWrappedTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 wrappedPhase[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionT

### RFmxPulse_FetchPhaseWrappedTrace

Fetches the wrapped phase trace of the selected pulse.

#### Syntax

int32 __stdcall RFmxPulse_FetchPhaseWrappedTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 wrappedPhase[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| wrappedPhase | [out] | float32[] | This parameter returns the wrapped phase, in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga3d68d4f286764a09c2154b901efc71a4.html language=enus -->
## TOPIC 00119: RFmxPulse_FetchBurstSelectedPositionStabilityTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga3d68d4f286764a09c2154b901efc71a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga3d68d4f286764a09c2154b901efc71a4.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the burst stability trace of the selected position. Syntaxint32 __stdcall RFmxPulse_FetchBurstSelectedPositionStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pulseAmplitudeStability[], float32 pulsePhaseStability[],

### RFmxPulse_FetchBurstSelectedPositionStabilityTrace

Fetches the burst stability trace of the selected position.

#### Syntax

int32 __stdcall RFmxPulse_FetchBurstSelectedPositionStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pulseAmplitudeStability[], float32 pulsePhaseStability[], float32 pulseTotalStability[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| pulseAmplitudeStability | [out] | float32[] | This parameter returns the amplitude stability, in dB. |
| pulsePhaseStability | [out] | float32[] | This parameter returns the amplitude stability, in dB. |
| pulseTotalStability | [out] | float32[] | This parameter returns the amplitude stability, in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga3efa022b46d6ea6a65c26cf1b7fe6d33.html language=enus -->
## TOPIC 00120: RFmxPulse_FetchTimeSidelobeTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga3efa022b46d6ea6a65c26cf1b7fe6d33.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga3efa022b46d6ea6a65c26cf1b7fe6d33.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the time sidelobe trace for the selected pulse. Syntaxint32 __stdcall RFmxPulse_FetchTimeSidelobeTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 timeSidelobe[], int32 arraySize, int32 *actualArraySize)ParametersNameDirection

### RFmxPulse_FetchTimeSidelobeTrace

Fetches the time sidelobe trace for the selected pulse.

#### Syntax

int32 __stdcall RFmxPulse_FetchTimeSidelobeTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 timeSidelobe[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| timeSidelobe | [out] | float32[] | This parameter returns the correlated magnitude, in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga64e7cf5479b58fa8804ab7eff1210107.html language=enus -->
## TOPIC 00121: RFmxPulse_FetchStabilityTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga64e7cf5479b58fa8804ab7eff1210107.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga64e7cf5479b58fa8804ab7eff1210107.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stability trace of the selected pulse. Syntaxint32 __stdcall RFmxPulse_FetchStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pulseAmplitudeStability[], float32 pulsePhaseStability[], float32 pulseTotalStability[]

### RFmxPulse_FetchStabilityTrace

Fetches the stability trace of the selected pulse.

#### Syntax

int32 __stdcall RFmxPulse_FetchStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pulseAmplitudeStability[], float32 pulsePhaseStability[], float32 pulseTotalStability[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| pulseAmplitudeStability | [out] | float32[] | This parameter returns the amplitude stability, in dB. |
| pulsePhaseStability | [out] | float32[] | This parameter returns the amplitude stability, in dB. |
| pulseTotalStability | [out] | float32[] | This parameter returns the amplitude stability, in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga663fe75fa146def3a48e30c76fc2a220.html language=enus -->
## TOPIC 00122: RFmxPulse_FetchIntrapulseStabilityTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga663fe75fa146def3a48e30c76fc2a220.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga663fe75fa146def3a48e30c76fc2a220.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position. Syntaxint32 __stdcall RFmxPulse_FetchIntrapulseStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 intrapulseAmplitude

### RFmxPulse_FetchIntrapulseStabilityTrace

Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position.

#### Syntax

int32 __stdcall RFmxPulse_FetchIntrapulseStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 intrapulseAmplitudeStability[], float32 intrapulsePhaseStability[], float32 intrapulseTotalStability[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of measurement window, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration of measurement window, in seconds. |
| intrapulseAmplitudeStability | [out] | float32[] | This parameter returns the intrapulse amplitude stability of multiple measurement points, in dB. |
| intrapulsePhaseStability | [out] | float32[] | This parameter returns the intrapulse amplitude stability of multiple measurement points, in dB. |
| intrapulseTotalStability | [out] | float32[] | This parameter returns the intrapulse amplitude stability of multiple measurement points, in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga68b29ec4c271d9259e41c6eb78a9358c.html language=enus -->
## TOPIC 00123: RFmxPulse_FetchAcquiredAmplitudeTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga68b29ec4c271d9259e41c6eb78a9358c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga68b29ec4c271d9259e41c6eb78a9358c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT attribute to select all pulses or the subset of acquired pulses. When you set the RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABL

### RFmxPulse_FetchAcquiredAmplitudeTrace

Fetches the acquired amplitude trace in the measurement, where the Amplitude array forms the y-axis of the trace. You can use the [RFMXPULSE_ATTR_PULSE_ACQUISITION_TRACE_SELECT](group____root__ni_r_fmx_pulse__attributes__pulse__acquisition__trace_1ga33dae866996a1dbda5cfab3383e3a3e3.html) attribute to select all pulses or the subset of acquired pulses. When you set the [RFMXPULSE_ATTR_SEGMENTED_ACQUISITION_ENABLED](group____root__ni_r_fmx_pulse__attributes__segmented__acquisition_1ga2c44e9db254a33910122308016399ee0.html) attribute to **False**, returns a single element in the Start Indices and Start Time Stamp array.

#### Syntax

int32 __stdcall RFmxPulse_FetchAcquiredAmplitudeTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *sampleDuration, float32 amplitude[], int32 amplitudeArraySize, int32 *amplitudeActualArraySize, int32 startIndex[], float64 startTimeStamp[], int32 startArraysSize, int32 *startActualArraysSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| sampleDuration | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| amplitude | [out] | float32[] | This parameter returns the trace of amplitude measured in units specified by RFMXPULSE_ATTR_PULSE_AMPLITUDE_TRACE_UNIT attribute. |
| amplitudeArraySize | [in] | int32 | Specifies the size of amplitude array. Set the amplitudeArraySize parameter to 0 to get the size of amplitude array in the amplitudeActualArraySize parameter. |
| amplitudeActualArraySize | [out] | int32 * | Returns the actual size of the amplitude array, if you pass NULL to amplitude output array parameters, and set the amplitudeArraySize parameter to 0. |
| startIndex | [out] | int32[] | This parameter returns the array of sample indices for the start of each segment. |
| startTimeStamp | [out] | float64[] | This parameter returns the array of timestamps of each segment start, in seconds. |
| startArraysSize | [in] | int32 | Specifies the size of start index and start time stamp array. Set the startArraysSize parameter to 0 to get the size of start index and start time stamp arrays in the startActualArraysSize parameter. |
| startActualArraysSize | [out] | int32 * | Returns the actual size of the start index and start time stamp array, if you pass NULL to start index and start time stamp output array parameters, and set the startArraysSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1ga69499a866326470a39f56dec32ee94a9.html language=enus -->
## TOPIC 00124: RFmxPulse_FetchBurstIntrapulseStabilityTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1ga69499a866326470a39f56dec32ee94a9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1ga69499a866326470a39f56dec32ee94a9.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points. Syntaxint32 __stdcall RFmxPulse_FetchBurstIntrapulseStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, fl

### RFmxPulse_FetchBurstIntrapulseStabilityTrace

Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points.

#### Syntax

int32 __stdcall RFmxPulse_FetchBurstIntrapulseStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 intrapulseAverageAmplitudeStability[], float32 intrapulseAveragePhaseStability[], float32 intrapulseAverageTotalStability[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of measurement window, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration of measurement window, in seconds. |
| intrapulseAverageAmplitudeStability | [out] | float32[] | This parameter returns the intrapulse average amplitude stability of multiple measurement points, in dB. |
| intrapulseAveragePhaseStability | [out] | float32[] | This parameter returns the intrapulse average amplitude stability of multiple measurement points, in dB. |
| intrapulseAverageTotalStability | [out] | float32[] | This parameter returns the intrapulse average amplitude stability of multiple measurement points, in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1gab0c3aae21fe0f8fe77b945f7aedb5acd.html language=enus -->
## TOPIC 00125: RFmxPulse_FetchMultipleMeasurementPointsStabilityTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1gab0c3aae21fe0f8fe77b945f7aedb5acd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1gab0c3aae21fe0f8fe77b945f7aedb5acd.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the multiple measurement points stability trace. Syntaxint32 __stdcall RFmxPulse_FetchMultipleMeasurementPointsStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pulseAverageAmplitudeStability[], float32 pulseAveragePh

### RFmxPulse_FetchMultipleMeasurementPointsStabilityTrace

Fetches the multiple measurement points stability trace.

#### Syntax

int32 __stdcall RFmxPulse_FetchMultipleMeasurementPointsStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 pulseAverageAmplitudeStability[], float32 pulseAveragePhaseStability[], float32 pulseAverageTotalStability[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time of measurement window, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration of measurement window, in seconds. |
| pulseAverageAmplitudeStability | [out] | float32[] | This parameter returns the average amplitude stability of multiple measurement points, in dB. |
| pulseAveragePhaseStability | [out] | float32[] | This parameter returns the average amplitude stability of multiple measurement points, in dB. |
| pulseAverageTotalStability | [out] | float32[] | This parameter returns the average amplitude stability of multiple measurement points, in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1gacda718f34a6177d04feb589d4fe12bc8.html language=enus -->
## TOPIC 00126: RFmxPulse_FetchPulseToPulseStabilityTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1gacda718f34a6177d04feb589d4fe12bc8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1gacda718f34a6177d04feb589d4fe12bc8.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the pulse to pulse stability trace. Syntaxint32 __stdcall RFmxPulse_FetchPulseToPulseStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 pulseIndex[], float64 pulseToPulseAmplitudeStability[], float64 pulseToPulsePhaseStability[], float64 pulseToP

### RFmxPulse_FetchPulseToPulseStabilityTrace

Fetches the pulse to pulse stability trace.

#### Syntax

int32 __stdcall RFmxPulse_FetchPulseToPulseStabilityTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 pulseIndex[], float64 pulseToPulseAmplitudeStability[], float64 pulseToPulsePhaseStability[], float64 pulseToPulseTotalStability[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| pulseIndex | [out] | int32[] | This parameter returns the pulse index. |
| pulseToPulseAmplitudeStability | [out] | float64[] | This parameter returns the trace of pulse to pulse amplitude stability, in dB. |
| pulseToPulsePhaseStability | [out] | float64[] | This parameter returns the trace of pulse to pulse phase stability, in dB. |
| pulseToPulseTotalStability | [out] | float64[] | This parameter returns the trace of pulse to pulse total stability, in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1gad0821e9cbd728ab82a9183cf060eaa32.html language=enus -->
## TOPIC 00127: RFmxPulse_FetchIQTraceSplit

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1gad0821e9cbd728ab82a9183cf060eaa32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1gad0821e9cbd728ab82a9183cf060eaa32.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the IQ trace of the selected pulse. Syntaxint32 __stdcall RFmxPulse_FetchIQTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 iqDataI[], float32 iqDataQ[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTyp

### RFmxPulse_FetchIQTraceSplit

Fetches the IQ trace of the selected pulse.

#### Syntax

int32 __stdcall RFmxPulse_FetchIQTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 iqDataI[], float32 iqDataQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| iqDataI | [out] | float32[] | This parameter Returns the real part of in-phase and quadrature-phase values, in Volts. |
| iqDataQ | [out] | float32[] | This parameter Returns the imaginary part of in-phase and quadrature-phase values, in Volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__fetch_1gafbac4c414f22922a08c2f86452d6f338.html language=enus -->
## TOPIC 00128: RFmxPulse_FetchIQTrace

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__fetch_1gafbac4c414f22922a08c2f86452d6f338.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__fetch_1gafbac4c414f22922a08c2f86452d6f338.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the IQ trace of the selected pulse. Syntaxint32 __stdcall RFmxPulse_FetchIQTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle iqData[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstr

### RFmxPulse_FetchIQTrace

Fetches the IQ trace of the selected pulse.

#### Syntax

int32 __stdcall RFmxPulse_FetchIQTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle iqData[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1" |
| timeout | [in] | float64 | This parameter specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| iqData | [out] | NIComplexSingle[] | This parameter returns the in-phase and quadrature-phase values, in Volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00129: Set and Get Attributes

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes.html
- document_id: `rfmxpulse-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00130: Get Attributes

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxPulse_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxPulse_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffe

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxPulse_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxPulse_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxPulse_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxPulse_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxPulse_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxPulse_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxPulse_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxPulse_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxPulse_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxPulse_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga0f6d60a1851824c5c87ffbf5f0333ab0.html language=enus -->
## TOPIC 00131: RFmxPulse_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga0f6d60a1851824c5c87ffbf5f0333ab0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga0f6d60a1851824c5c87ffbf5f0333ab0.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxPulse_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga18e2ba1efea6071c70f9677dbd934b6b.html language=enus -->
## TOPIC 00132: RFmxPulse_GetAttributeI16

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga18e2ba1efea6071c70f9677dbd934b6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga18e2ba1efea6071c70f9677dbd934b6b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxPulse_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga1ec69045481d0f81f6bc8b78e7b47265.html language=enus -->
## TOPIC 00133: RFmxPulse_GetAttributeU8Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga1ec69045481d0f81f6bc8b78e7b47265.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga1ec69045481d0f81f6bc8b78e7b47265.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxPulse_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga3b33a887aebc82efdc3a01de975c6c3c.html language=enus -->
## TOPIC 00134: RFmxPulse_GetAttributeU32Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga3b33a887aebc82efdc3a01de975c6c3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga3b33a887aebc82efdc3a01de975c6c3c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxPulse_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga6487e8b6d95d5e592a11ac04c814ebd3.html language=enus -->
## TOPIC 00135: RFmxPulse_GetAttributeF64

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga6487e8b6d95d5e592a11ac04c814ebd3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga6487e8b6d95d5e592a11ac04c814ebd3.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxPulse_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga64a32d96151067b513720e33e60298eb.html language=enus -->
## TOPIC 00136: RFmxPulse_GetAttributeString

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga64a32d96151067b513720e33e60298eb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga64a32d96151067b513720e33e60298eb.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxPulse_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga66c76dcb941b255a956ea8f2dee304b4.html language=enus -->
## TOPIC 00137: RFmxPulse_GetAttributeI32Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga66c76dcb941b255a956ea8f2dee304b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga66c76dcb941b255a956ea8f2dee304b4.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxPulse_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga8ac50c46a20befdb969e0ccafed350f5.html language=enus -->
## TOPIC 00138: RFmxPulse_GetAttributeI64

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga8ac50c46a20befdb969e0ccafed350f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga8ac50c46a20befdb969e0ccafed350f5.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxPulse_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga956603009ee911f306bb8eccf0d00b50.html language=enus -->
## TOPIC 00139: RFmxPulse_GetAttributeF32Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga956603009ee911f306bb8eccf0d00b50.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1ga956603009ee911f306bb8eccf0d00b50.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxPulse_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaa5b421774216914d4029a7a9e17cb578.html language=enus -->
## TOPIC 00140: RFmxPulse_GetAttributeI8

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaa5b421774216914d4029a7a9e17cb578.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaa5b421774216914d4029a7a9e17cb578.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxPulse_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaabc4a2b0e64a4b2a75d96735ca627f80.html language=enus -->
## TOPIC 00141: RFmxPulse_GetAttributeU64Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaabc4a2b0e64a4b2a75d96735ca627f80.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaabc4a2b0e64a4b2a75d96735ca627f80.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxPulse_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaaf903ab27702c72db73e03cc46618002.html language=enus -->
## TOPIC 00142: RFmxPulse_GetAttributeF32

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaaf903ab27702c72db73e03cc46618002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaaf903ab27702c72db73e03cc46618002.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxPulse_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gabd0514ba723071d41669733742ae01c6.html language=enus -->
## TOPIC 00143: RFmxPulse_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gabd0514ba723071d41669733742ae01c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gabd0514ba723071d41669733742ae01c6.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxPulse_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gac1c11317785614361c48a7b8507fa95d.html language=enus -->
## TOPIC 00144: RFmxPulse_GetAttributeI8Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gac1c11317785614361c48a7b8507fa95d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gac1c11317785614361c48a7b8507fa95d.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxPulse_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gac59d8e378095d77e76b52d211fe5107b.html language=enus -->
## TOPIC 00145: RFmxPulse_GetAttributeU8

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gac59d8e378095d77e76b52d211fe5107b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gac59d8e378095d77e76b52d211fe5107b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxPulse_GetAttributeU8

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gad946eb12569f1fa007c9102441890fcc.html language=enus -->
## TOPIC 00146: RFmxPulse_GetAttributeI32

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gad946eb12569f1fa007c9102441890fcc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gad946eb12569f1fa007c9102441890fcc.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxPulse_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaee8d5f824ba1e70cbaf4054edcd1eef6.html language=enus -->
## TOPIC 00147: RFmxPulse_GetAttributeU16

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaee8d5f824ba1e70cbaf4054edcd1eef6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaee8d5f824ba1e70cbaf4054edcd1eef6.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxPulse_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf16f716991c39e76002f40a984333634.html language=enus -->
## TOPIC 00148: RFmxPulse_GetAttributeU32

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf16f716991c39e76002f40a984333634.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf16f716991c39e76002f40a984333634.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxPulse_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxPulse_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf5c098f669464f3bf9033eca297cc949.html language=enus -->
## TOPIC 00149: RFmxPulse_GetAttributeF64Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf5c098f669464f3bf9033eca297cc949.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf5c098f669464f3bf9033eca297cc949.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxPulse_GetAttributeF64Array

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf71ab3a1f7d4740cae9b3a36452bdb83.html language=enus -->
## TOPIC 00150: RFmxPulse_GetAttributeI64Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf71ab3a1f7d4740cae9b3a36452bdb83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__get__attributes_1gaf71ab3a1f7d4740cae9b3a36452bdb83.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxPulse_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxPulse_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00151: Set Attributes

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxPulse_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxPulse_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxPulse_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxPulse_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxPulse_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxPulse_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxPulse_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxPulse_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxPulse_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxPulse_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxPulse_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxPulse_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxPulse_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga027027faaed2d3db5201e532f0b00d89.html language=enus -->
## TOPIC 00152: RFmxPulse_SetAttributeF64Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga027027faaed2d3db5201e532f0b00d89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga027027faaed2d3db5201e532f0b00d89.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, ch

### RFmxPulse_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga17fbbdb7579ef413cf1310e0bf7c0fc2.html language=enus -->
## TOPIC 00153: RFmxPulse_SetAttributeU32

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga17fbbdb7579ef413cf1310e0bf7c0fc2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga17fbbdb7579ef413cf1310e0bf7c0fc2.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxPulse_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3444902336ef7ef0f14c717233e2d3c9.html language=enus -->
## TOPIC 00154: RFmxPulse_SetAttributeF64

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3444902336ef7ef0f14c717233e2d3c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3444902336ef7ef0f14c717233e2d3c9.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentif

### RFmxPulse_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3e44afbf3836e36f59ca3c5a9213fa18.html language=enus -->
## TOPIC 00155: RFmxPulse_SetAttributeI8Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3e44afbf3836e36f59ca3c5a9213fa18.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3e44afbf3836e36f59ca3c5a9213fa18.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[]

### RFmxPulse_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3f653128a8a15a0e1fba9768a2120686.html language=enus -->
## TOPIC 00156: RFmxPulse_SetAttributeI64

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3f653128a8a15a0e1fba9768a2120686.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga3f653128a8a15a0e1fba9768a2120686.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxPulse_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga49990ff0bab037e2cb343ae85827afe2.html language=enus -->
## TOPIC 00157: RFmxPulse_SetAttributeI32

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga49990ff0bab037e2cb343ae85827afe2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga49990ff0bab037e2cb343ae85827afe2.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxPulse_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga5391cf1d114af52da8e7235ce64e7b3b.html language=enus -->
## TOPIC 00158: RFmxPulse_SetAttributeString

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga5391cf1d114af52da8e7235ce64e7b3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga5391cf1d114af52da8e7235ce64e7b3b.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can

### RFmxPulse_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga5c4def2b01daac896fc8be2a8b92d41a.html language=enus -->
## TOPIC 00159: RFmxPulse_SetAttributeU32Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga5c4def2b01daac896fc8be2a8b92d41a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga5c4def2b01daac896fc8be2a8b92d41a.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxPulse_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga7c2303ab41b4c95299a9708bb5a35e10.html language=enus -->
## TOPIC 00160: RFmxPulse_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga7c2303ab41b4c95299a9708bb5a35e10.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga7c2303ab41b4c95299a9708bb5a35e10.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxPulse_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga82b1e886e31b4f25df2590eae7f1dda3.html language=enus -->
## TOPIC 00161: RFmxPulse_SetAttributeI32Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga82b1e886e31b4f25df2590eae7f1dda3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga82b1e886e31b4f25df2590eae7f1dda3.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxPulse_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga89d3f6f85d263e5bc7082a3d2f5ce002.html language=enus -->
## TOPIC 00162: RFmxPulse_SetAttributeI8

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga89d3f6f85d263e5bc7082a3d2f5ce002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga89d3f6f85d263e5bc7082a3d2f5ce002.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxPulse_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga916b78ec1cdfdee048ec8c803473a6ca.html language=enus -->
## TOPIC 00163: RFmxPulse_SetAttributeU16

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga916b78ec1cdfdee048ec8c803473a6ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1ga916b78ec1cdfdee048ec8c803473a6ca.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxPulse_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaa0713b157f1346b75e867d86ac0318c9.html language=enus -->
## TOPIC 00164: RFmxPulse_SetAttributeI64Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaa0713b157f1346b75e867d86ac0318c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaa0713b157f1346b75e867d86ac0318c9.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxPulse_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaa223e97473f79868840107165d90be3c.html language=enus -->
## TOPIC 00165: RFmxPulse_SetAttributeI16

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaa223e97473f79868840107165d90be3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaa223e97473f79868840107165d90be3c.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxPulse_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaaed92ef93ad2dc48677b5e503c231c35.html language=enus -->
## TOPIC 00166: RFmxPulse_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaaed92ef93ad2dc48677b5e503c231c35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaaed92ef93ad2dc48677b5e503c231c35.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxPulse_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab0569f75cb26aacc373cb93487d3f92e.html language=enus -->
## TOPIC 00167: RFmxPulse_SetAttributeU64Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab0569f75cb26aacc373cb93487d3f92e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab0569f75cb26aacc373cb93487d3f92e.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxPulse_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab5c02a98fd3cd67a5881c30c7a1ddeab.html language=enus -->
## TOPIC 00168: RFmxPulse_SetAttributeF32

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab5c02a98fd3cd67a5881c30c7a1ddeab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab5c02a98fd3cd67a5881c30c7a1ddeab.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentif

### RFmxPulse_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab6ebf09b135319aa0026d93df18b01c2.html language=enus -->
## TOPIC 00169: RFmxPulse_SetAttributeU8

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab6ebf09b135319aa0026d93df18b01c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gab6ebf09b135319aa0026d93df18b01c2.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxPulse_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFm

### RFmxPulse_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaec5af6b805ec4fb3f5f23514366716a5.html language=enus -->
## TOPIC 00170: RFmxPulse_SetAttributeF32Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaec5af6b805ec4fb3f5f23514366716a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaec5af6b805ec4fb3f5f23514366716a5.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, ch

### RFmxPulse_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaf3cacb341237f5a8b15a6bf49e6b0de8.html language=enus -->
## TOPIC 00171: RFmxPulse_SetAttributeU8Array

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaf3cacb341237f5a8b15a6bf49e6b0de8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__set__and__get__attributes__set__attributes_1gaf3cacb341237f5a8b15a6bf49e6b0de8.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxPulse_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char select

### RFmxPulse_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxPulse_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxPulse_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxPulse_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxPulse_GetError](group____root__ni_r_fmx_pulse__functions_1ga8970ac51bb5f317ddfb31d25f94737e0.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxpulse-c-api-ref path=group____root__ni_r_fmx_pulse__functions__utility.html language=enus -->
## TOPIC 00172: Utility

- bundle_id: `rfmxpulse-c-api-ref`
- source_path: `group____root__ni_r_fmx_pulse__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxpulse-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_pulse__functions__utility.html
- document_id: `rfmxpulse-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxPulse_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxPulse_CommitCommits settings to the h

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxPulse_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxPulse_Commit | Commits settings to the hardware. Calling this function is optional. RFmxPulse commits settings to the hardware when you call the RFmxPulse_Initiate function or any of the measurement Read functions. |
| RFmxPulse_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxPulse_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxPulse_ResetToDefault | Resets a signal to the default values. |
| RFmxPulse_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxPulse_WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions
