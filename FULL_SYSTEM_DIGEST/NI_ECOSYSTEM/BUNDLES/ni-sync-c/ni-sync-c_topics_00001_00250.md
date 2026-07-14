# NI DOCUMENT BUNDLE: ni-sync-c

<!--NI_BUNDLE_CHUNK bundle=ni-sync-c start=1 end=250 -->
<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/attributes.html language=enus -->
## TOPIC 00001: Attributes

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/attributes.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### Attributes

The topics in this section describe the NI-Sync attributes you can use in the LabWindows/CVI (C/C++) programming environment.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_avail_timestamps.html language=enus -->
## TOPIC 00002: NISYNC_ATTR_1588_AVAIL_TIMESTAMPS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_avail_timestamps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_avail_timestamps.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_AVAIL_TIMESTAMPS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the number of timestamps available to read for the specified terminal.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_bmca_mode.html language=enus -->
## TOPIC 00003: NISYNC_ATTR_1588_BMCA_MODE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_bmca_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_bmca_mode.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_BMCA_MODE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns which mode of the Best Master Clock algorithm (BMCA) to use for the time reference specified in the **activeItem** parameter.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem attribute when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_clk_resolution.html language=enus -->
## TOPIC 00004: NISYNC_ATTR_1588_CLK_RESOLUTION

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_clk_resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_clk_resolution.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_CLK_RESOLUTION

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the resolution, in nanoseconds, of the device's clock. The clock resolution represents the duration of a single tick of the clock.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_clock_accuracy.html language=enus -->
## TOPIC 00005: NISYNC_ATTR_1588_CLOCK_ACCURACY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_clock_accuracy.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_CLOCK_ACCURACY

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViEnum | RO | N/A | None | None |

#### Description

Returns the accuracy of the device's 1588 clock in comparison to the currently selected time reference.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

#### Defined Values

| Unknown | 0 |
| --- | --- |
| Within25nsec | 1 |
| Within100nsec | 2 |
| Within250nsec | 3 |
| Within1usec | 4 |
| Within2500nsec | 5 |
| Within10usec | 6 |
| Within25usec | 7 |
| Within100usec | 8 |
| Within250usec | 9 |
| Within1msec | 10 |
| Within2500usec | 11 |
| Within10msec | 12 |
| Within25msec | 13 |
| Within100msec | 14 |
| Within250msec | 15 |
| Within1sec | 16 |
| Within10sec | 17 |
| GreaterThan10sec | 18 |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_clock_class.html language=enus -->
## TOPIC 00006: NISYNC_ATTR_1588_CLOCK_CLASS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_clock_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_clock_class.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_CLOCK_CLASS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the traceability of the time or frequency distributed by the 1588 clock on the specified time reference.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_clock_id.html language=enus -->
## TOPIC 00007: NISYNC_ATTR_1588_CLOCK_ID

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_clock_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_clock_id.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_CLOCK_ID

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns a string that represents the 64-bit Global Identifier (EUI-64) for the 1588 clock on the time reference specified in the **activeItem** parameter.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_clock_state.html language=enus -->
## TOPIC 00008: NISYNC_ATTR_1588_CLOCK_STATE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_clock_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_clock_state.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_CLOCK_STATE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the state of the 1588 clock. You can query this attribute to determine if this clock has reached a steady state before the application continues with other operations dependent on this clock, or to determine if an error occurred during synchronization.

|  | Note For Linux RT devices, you must specify the time reference by passing the activeItem parameter when querying this attribute.This property is supported only on certain targets; refer to Target Support for Timing Properties and Functions for more information. |
| --- | --- |

#### Defined Values

| Value | Integer | Final? | Description |
| --- | --- | --- | --- |
| NISYNC_VAL_1588_CLK_STATE_NOT_DEFINED | -1 | N/A | The state of 1588 clock associated with this session is not defined. |
| NISYNC_VAL_1588_CLK_STATE_INIT | 0 | No | The 1588 clock associated with this session is in the Initializing state. |
| NISYNC_VAL_1588_CLK_STATE_FAULT | 1 | Yes | The 1588 clock associated with this session is in the Faulty state, which indicates that this clock is not participating in PTP due to a problem. |
| NISYNC_VAL_1588_CLK_STATE_DISABLE | 2 | Yes | The 1588 clock associated with this session is in the Disabled state, which indicates that this clock is not participating in PTP since it has been disabled. |
| NISYNC_VAL_1588_CLK_STATE_LISTENING | 3 | No | The 1588 clock associated with this session is in the Listening state, which indicates it is waiting to receive timestamps from the Master clock. |
| NISYNC_VAL_1588_CLK_STATE_PREMASTER | 4 | No | The 1588 clock associated with this session is in the Pre-Master state. |
| NISYNC_VAL_1588_CLK_STATE_MASTER | 5 | Yes | The 1588 clock associated with this session is in the Master state, which indicates that this clock has been selected as the master clock for its subdomain. |
| NISYNC_VAL_1588_CLK_STATE_PASSIVE | 6 | Yes | The 1588 clock associated with this session is in the Passive state, which indicates that this clock will not generate any PTP-related communications. |
| NISYNC_VAL_1588_CLK_STATE_UNCALIBRATED | 7 | No | The 1588 clock associated with this session is in the Uncalibrated state. |
| NISYNC_VAL_1588_CLK_STATE_SLAVE | 8 | Yes | The 1588 clock associated with this session is in the Slave state, which indicates that this clock has been selected as a slave clock within its subdomain. |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_frequency_traceable.html language=enus -->
## TOPIC 00009: NISYNC_ATTR_1588_FREQUENCY_TRACEABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_frequency_traceable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_frequency_traceable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_FREQUENCY_TRACEABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

A Boolean indicating whether the clock frequency can be traced.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_accuracy.html language=enus -->
## TOPIC 00010: NISYNC_ATTR_1588_GRANDMASTER_CLOCK_ACCURACY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_accuracy.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_GRANDMASTER_CLOCK_ACCURACY

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViEnum | RO | N/A | None | None |

#### Description

Returns the accuracy of the 1588 grandmaster clock.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

#### Defined Values

| Unknown | 0 |
| --- | --- |
| Within25nsec | 1 |
| Within100nsec | 2 |
| Within250nsec | 3 |
| Within1usec | 4 |
| Within2500nsec | 5 |
| Within10usec | 6 |
| Within25usec | 7 |
| Within100usec | 8 |
| Within250usec | 9 |
| Within1msec | 10 |
| Within2500usec | 11 |
| Within10msec | 12 |
| Within25msec | 13 |
| Within100msec | 14 |
| Within250msec | 15 |
| Within1sec | 16 |
| Within10sec | 17 |
| GreaterThan10sec | 18 |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_class.html language=enus -->
## TOPIC 00011: NISYNC_ATTR_1588_GRANDMASTER_CLOCK_CLASS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_class.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_GRANDMASTER_CLOCK_CLASS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the traceability of the time or frequency distributed by the 1588 grandmaster clock associated with this session.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_id.html language=enus -->
## TOPIC 00012: NISYNC_ATTR_1588_GRANDMASTER_CLOCK_ID

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_grandmaster_clock_id.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_GRANDMASTER_CLOCK_ID

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns a string that represents the 64-bit Global Identifier (EUI-64) for the 1588 grandmaster clock.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_grandmaster_ip_address.html language=enus -->
## TOPIC 00013: NISYNC_ATTR_1588_GRANDMASTER_IP_ADDRESS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_grandmaster_ip_address.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_grandmaster_ip_address.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_GRANDMASTER_IP_ADDRESS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns the IP address of the 1588 grandmaster clock used by the time reference specified by the **activeItem** parameter.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_grandmaster_priority1.html language=enus -->
## TOPIC 00014: NISYNC_ATTR_1588_GRANDMASTER_PRIORITY1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_grandmaster_priority1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_grandmaster_priority1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_GRANDMASTER_PRIORITY1

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the 1st order priority assigned to the 1588 grandmaster clock. This attribute can range from 0 to 255. A lower value indicates a higher priority.

|  | Note For Linux RT devices, you must specify the time reference the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_grandmaster_priority2.html language=enus -->
## TOPIC 00015: NISYNC_ATTR_1588_GRANDMASTER_PRIORITY2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_grandmaster_priority2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_grandmaster_priority2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_GRANDMASTER_PRIORITY2

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the 2nd order priority assigned to the 1588 grandmaster clock. This attribute is used in the execution of the Best Master Clock algorithm (BMCA). This attribute can range from 0 to 255. A lower value increases the priority.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_interface_name.html language=enus -->
## TOPIC 00016: NISYNC_ATTR_1588_INTERFACE_NAME

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_interface_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_interface_name.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_INTERFACE_NAME

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns the name of the network interface used by the time reference specified in **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_ip_address.html language=enus -->
## TOPIC 00017: NISYNC_ATTR_1588_IP_ADDRESS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_ip_address.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_ip_address.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_IP_ADDRESS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns the IP address assigned to the 1588 device associated with this session.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_leap59.html language=enus -->
## TOPIC 00018: NISYNC_ATTR_1588_LEAP59

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_leap59.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_leap59.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_LEAP59

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

A Boolean indicating whether the last minute of the current UTC day contains 59 seconds.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_leap61.html language=enus -->
## TOPIC 00019: NISYNC_ATTR_1588_LEAP61

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_leap61.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_leap61.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_LEAP61

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

A Boolean indicating whether the last minute of the current UTC day contains 61 seconds.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_log_sync_interval.html language=enus -->
## TOPIC 00020: NISYNC_ATTR_1588_LOG_SYNC_INTERVAL

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_log_sync_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_log_sync_interval.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_LOG_SYNC_INTERVAL

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViEnum | R/W | N/A | None | None |

#### Description

Specifies or returns the mean sync interval used by the 1588 clock. Use a smaller sync interval to make clocks respond more quickly to changes in the time reference. Use a larger sync interval to send packets less frequently and decrease network load.

The sync interval of the grandmaster clock becomes the sync interval for the entire PTP subdomain. Therefore, when setting this value, remember that it will be used only if the Best Master Clock algorithm (BMCA) chooses the local clock to be the grandmaster.

The default is 0. Note that this value is the logarithm to the base 2.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute.This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Defined Values

| 500 Milliseconds | -1 |
| --- | --- |
| 1 Second | 0 |
| 2 Seconds | 1 |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_mean_path_delay.html language=enus -->
## TOPIC 00021: NISYNC_ATTR_1588_MEAN_PATH_DELAY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_mean_path_delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_mean_path_delay.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_MEAN_PATH_DELAY

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | RO | N/A | None | None |

#### Description

Returns the mean propagation delay, in seconds, between the 1588 clock associated with this session and the 1588 master clock. The mean propagation delay is the average amount of time it takes for a packet to reach a slave device from the 1588 master.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_offset_scaled_log_variance.html language=enus -->
## TOPIC 00022: NISYNC_ATTR_1588_OFFSET_SCALED_LOG_VARIANCE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_offset_scaled_log_variance.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_offset_scaled_log_variance.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_OFFSET_SCALED_LOG_VARIANCE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the log-scaled value representing the clock's precision.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_priority1.html language=enus -->
## TOPIC 00023: NISYNC_ATTR_1588_PRIORITY1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_priority1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_priority1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_PRIORITY1

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the 1st order priority assigned to the 1588 clock. This attribute can range from 0 to 255. A lower value indicates a higher priority.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_priority2.html language=enus -->
## TOPIC 00024: NISYNC_ATTR_1588_PRIORITY2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_priority2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_priority2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_PRIORITY2

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the second order priority assigned to the 1588 clock. This attribute can range from 0 to 255. A lower value indicates a higher priority.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_steps_to_grandmaster.html language=enus -->
## TOPIC 00025: NISYNC_ATTR_1588_STEPS_TO_GRANDMASTER

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_steps_to_grandmaster.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_steps_to_grandmaster.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_STEPS_TO_GRANDMASTER

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the number of steps that the 1588 clock is away from the grandmaster.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_time_source.html language=enus -->
## TOPIC 00026: NISYNC_ATTR_1588_TIME_SOURCE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_time_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_time_source.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_TIME_SOURCE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViEnum | RO | N/A | None | None |

#### Description

An integer enumeration indicating the clock's time source, as obtained from the leader clock.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

#### Defined Values

| Name | # |
| --- | --- |
| Unknown | 0 |
| AtomicClock | 1 |
| Gps | 2 |
| TerrestrialRadio | 3 |
| Ptp | 4 |
| Ntp | 5 |
| HandSet | 6 |
| Other | 7 |
| InternalOscillator | 8 |
| AlternatePTP* | 9 |
| Reserved* | 10 |

* Only available on Linux.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_time_traceable.html language=enus -->
## TOPIC 00027: NISYNC_ATTR_1588_TIME_TRACEABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_time_traceable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_time_traceable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_TIME_TRACEABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

A Boolean indicating whether time can be traced.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_1588_timestamp_buf_size.html language=enus -->
## TOPIC 00028: NISYNC_ATTR_1588_TIMESTAMP_BUF_SIZE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_1588_timestamp_buf_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_1588_timestamp_buf_size.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_1588_TIMESTAMP_BUF_SIZE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the software buffer size, in number of timestamps, for the specified terminal. The default is 1000.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_as_capable.html language=enus -->
## TOPIC 00029: NISYNC_ATTR_8021AS_AS_CAPABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_as_capable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_as_capable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_AS_CAPABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns whether the time reference specified by **activeItem** is capable of participating in the IEEE 802.1AS protocol. This value is TRUE only if this time-aware system and the time-aware system it is linked to can inter-operate with each other via the 802.1AS protocol.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_clock_accuracy.html language=enus -->
## TOPIC 00030: NISYNC_ATTR_8021AS_CLOCK_ACCURACY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_clock_accuracy.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_CLOCK_ACCURACY

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the accuracy of the 802.1AS clock used by the time reference specified by **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

| Value | Description |
| --- | --- |
| 32 | Within25nsec |
| 33 | Within100nsec |
| 34 | Within250nsec |
| 35 | Within1usec |
| 36 | Within2500nsec |
| 37 | Within10usec |
| 38 | Within25usec |
| 39 | Within100usec |
| 40 | Within250usec |
| 41 | Within1msec |
| 42 | Within2500usec |
| 43 | Within10msec |
| 44 | Within25msec |
| 45 | Within100msec |
| 46 | Within250msec |
| 47 | Within1sec |
| 48 | Within10sec |
| 49 | GreaterThan10sec |
| 254 | Unknown |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_clock_class.html language=enus -->
## TOPIC 00031: NISYNC_ATTR_8021AS_CLOCK_CLASS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_clock_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_clock_class.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_CLOCK_CLASS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the traceability of the time or frequency distributed by the 802.1AS clock used by the time reference specified by **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

| Integer | Clock Class Specification |
| --- | --- |
| 0 | Reserved to enable compatibility with future versions. |
| 1&em;5 | Reserved |
| 6 | The clock is synchronized to a primary time reference. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 7 | The clock has previously been designated as Clock Class 6, but has lost the ability to synchronize to a primary time reference. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 8 | Reserved |
| 9&em;10 | Reserved to enable compatibility with future versions. |
| 11&em;12 | Reserved |
| 13 | The clock is synchronized to an application-specific time source. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 14 | The clock has previously been designated as Clock Class 13, but has lost the ability to synchronize to an application-specific time source. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 15&em;51 | Reserved |
| 52 | The clock is degradation alternative A for a Clock Class 7 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 53&em;57 | Reserved |
| 58 | The clock is degredation alternative A for a Clock Class 14 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 59&em;67 | Reserved |
| 68&em;122 | The clock uses an alternate PTP profile. |
| 123&em;127 | Reserved |
| 128&em;132 | Reserved |
| 133&em;170 | The clock uses an alternate PTP profile. |
| 171&em;186 | Reserved |
| 187 | The clock is degredation alternative B for a Clock Class 7 clock that is not within holdover specification. A clock in this class can be a slave to another clock in the domain. |
| 188&em;192 | Reserved |
| 193 | The clock is degredation alternative B for a Clock Class 14 clock that is not within holdover specification. A clock of this class can be a slave to another clock in the domain. |
| 194&em;215 | Reserved |
| 216&em;232 | The clock uses an alternate PTP profile. |
| 233&em;247 | Reserved |
| 248 | The default Clock Class. This class is used if none of the other class definitions apply. |
| 249&em;250 | Reserved |
| 251 | Reserved for version 1 compatibility. |
| 252&em;254 | Reserved |
| 255 | The clock is a slave-only clock. |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_clock_id.html language=enus -->
## TOPIC 00032: NISYNC_ATTR_8021AS_CLOCK_ID

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_clock_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_clock_id.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_CLOCK_ID

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns a string that represents the 64-bit Global Identifier (EUI-64) of the 802.1AS clock used by the time reference specified by **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_accuracy.html language=enus -->
## TOPIC 00033: NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_ACCURACY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_accuracy.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_ACCURACY

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the accuracy of the 802.1AS grandmaster clock used by the time reference specified by **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

| Value | Description |
| --- | --- |
| 0 | Unknown |
| 1 | Within25nsec |
| 2 | Within100nsec |
| 3 | Within250nsec |
| 4 | Within1usec |
| 5 | Within2500nsec |
| 6 | Within10usec |
| 7 | Within25usec |
| 8 | Within100usec |
| 9 | Within250usec |
| 10 | Within1msec |
| 11 | Within2500usec |
| 12 | Within10msec |
| 13 | Within25msec |
| 14 | Within100msec |
| 15 | Within250msec |
| 16 | Within1sec |
| 17 | Within10sec |
| 18 | GreaterThan10sec |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_class.html language=enus -->
## TOPIC 00034: NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_CLASS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_class.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_CLASS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the traceability of the time or frequency distributed by the 802.1AS grandmaster clock used by the time reference specified by **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

| Integer | Clock Class Specification |
| --- | --- |
| 0 | Reserved to enable compatibility with future versions. |
| 1—5 | Reserved |
| 6 | The clock is synchronized to a primary time reference. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 7 | The clock has previously been designated as Clock Class 6, but has lost the ability to synchronize to a primary time reference. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 8 | Reserved |
| 9—10 | Reserved to enable compatibility with future versions. |
| 11—12 | Reserved |
| 13 | The clock is synchronized to an application-specific time source. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 14 | The clock has previously been designated as Clock Class 13, but has lost the ability to synchronize to an application-specific time source. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 15—51 | Reserved |
| 52 | The clock is degradation alternative A for a Clock Class 7 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 53—57 | Reserved |
| 58 | The clock is degredation alternative A for a Clock Class 14 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 59—67 | Reserved |
| 68—122 | The clock uses an alternate PTP profile. |
| 123—127 | Reserved |
| 128—132 | Reserved |
| 133—170 | The clock uses an alternate PTP profile. |
| 171—186 | Reserved |
| 187 | The clock is degredation alternative B for a Clock Class 7 clock that is not within holdover specification. A clock in this class can be a slave to another clock in the domain. |
| 188—192 | Reserved |
| 193 | The clock is degredation alternative B for a Clock Class 14 clock that is not within holdover specification. A clock of this class can be a slave to another clock in the domain. |
| 194—215 | Reserved |
| 216—232 | The clock uses an alternate PTP profile. |
| 233—247 | Reserved |
| 248 | The default Clock Class. This class is used if none of the other class definitions apply. |
| 249—250 | Reserved |
| 251 | Reserved for version 1 compatibility. |
| 252—254 | Reserved |
| 255 | The clock is a slave-only clock. |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_id.html language=enus -->
## TOPIC 00035: NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_ID

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_grandmaster_clock_id.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_GRANDMASTER_CLOCK_ID

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns a string that represents the 64-bit Global Identifier (EUI-64) for the 802.1AS grandmaster clock used by the time reference specified by **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_grandmaster_priority1.html language=enus -->
## TOPIC 00036: NISYNC_ATTR_8021AS_GRANDMASTER_PRIORITY1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_grandmaster_priority1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_grandmaster_priority1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_GRANDMASTER_PRIORITY1

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the 1st order priority assigned to the 802.1AS grandmaster clock used by the time reference specified by **activeItem**. This attribute is used in the execution of the Best Master Clock algorithm (BMCA) and cannot be modified. This attribute can range from 0 to 255. A lower value denotes a higher priority.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_grandmaster_priority2.html language=enus -->
## TOPIC 00037: NISYNC_ATTR_8021AS_GRANDMASTER_PRIORITY2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_grandmaster_priority2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_grandmaster_priority2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_GRANDMASTER_PRIORITY2

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the 2nd order priority assigned to the 802.1AS grandmaster clock used by the time reference specified by **activeItem**. This attribute is used in the execution of the Best Master Clock algorithm (BMCA) and cannot be modified. This attribute can range from 0 to 255. A lower value denotes a higher priority.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_interface_name.html language=enus -->
## TOPIC 00038: NISYNC_ATTR_8021AS_INTERFACE_NAME

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_interface_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_interface_name.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_INTERFACE_NAME

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns the network interface used by the 802.1AS clock in the time reference specified by **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_log_announce_interval.html language=enus -->
## TOPIC 00039: NISYNC_ATTR_8021AS_LOG_ANNOUNCE_INTERVAL

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_log_announce_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_log_announce_interval.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_LOG_ANNOUNCE_INTERVAL

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the mean time interval between the sending of successive announce messages. Announce messages allow time-aware systems to exchange information used by the Best Master Clock algorithm (BMCA). This value is the logarithm to the base 2.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

| Value | Description |
| --- | --- |
| -1 | 500 milliseconds |
| 0 | 1 second |
| 1 | 2 seconds |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_log_sync_interval.html language=enus -->
## TOPIC 00040: NISYNC_ATTR_8021AS_LOG_SYNC_INTERVAL

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_log_sync_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_log_sync_interval.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_LOG_SYNC_INTERVAL

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the mean sync interval used by the 802.1AS clock in the time reference specified by **activeItem**. This value will be used only if the Best Master Clock algorithm (BMCA) chooses the local clock to be the grandmaster. The default is 0. This value is the logarithm to the base 2.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

| Value | Description |
| --- | --- |
| -3 | 125 milliseconds |
| -2 | 250 milliseconds |
| -1 | 500 milliseconds |
| 0 | 1 second |
| 1 | 2 seconds |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_neighbor_prop_delay_thresh.html language=enus -->
## TOPIC 00041: NISYNC_ATTR_8021AS_NEIGHBOR_PROP_DELAY_THRESH

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_neighbor_prop_delay_thresh.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_neighbor_prop_delay_thresh.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_NEIGHBOR_PROP_DELAY_THRESH

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the propagation time threshold, in nanoseconds, of the time reference specified by **activeItem**. When a port's propagation delay time exceeds this threshold, the port is not considered capable of participating in the IEEE 802.1AS protocol, and the [NISYNC_ATTR_8021AS_AS_CAPABLE](nisync_attr_8021as_as_capable.html) attribute is set to FALSE.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_port_state.html language=enus -->
## TOPIC 00042: NISYNC_ATTR_8021AS_PORT_STATE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_port_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_port_state.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_PORT_STATE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the state of the 802.1AS clock used by the time reference specified in **activeItem**. This attribute can be queried to determine if this clock has reached a steady state before the application continues with other operations dependent on this clock. You can also use this attribute to determine if this clock has entered the Disabled state, in which case the clock is no longer synchronized with other 802.1AS devices.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

| Integer | State |
| --- | --- |
| 3 | Disabled |
| 6 | Master |
| 7 | Passive |
| 9 | Slave |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_priority1.html language=enus -->
## TOPIC 00043: NISYNC_ATTR_8021AS_PRIORITY1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_priority1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_priority1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_PRIORITY1

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the 1st order priority assigned to the 802.1AS clock used by the time reference specified by **activeItem**. This attribute is used in the execution of the Best Master Clock algorithm (BMCA). This attribute can range from 0 to 255. A lower value increases the priority. The default value is 246.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_8021as_priority2.html language=enus -->
## TOPIC 00044: NISYNC_ATTR_8021AS_PRIORITY2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_8021as_priority2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_8021as_priority2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_8021AS_PRIORITY2

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the 2nd order priority assigned to the 802.1AS clock used by the time reference specified by **activeItem**. This attribute is used in the execution of the Best Master Clock algorithm (BMCA). This attribute can range from 0 to 255. A lower value increases the priority. The default value is 247.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_clk10_phase_adjust.html language=enus -->
## TOPIC 00045: NISYNC_ATTR_CLK10_PHASE_ADJUST

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_clk10_phase_adjust.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_clk10_phase_adjust.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_CLK10_PHASE_ADJUST

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the phase voltage between an external clock and PXI_Clk10 when you are using the PLL circuit to lock PXI_CLK10 to an external reference clock. You can minimize the time between rising edges of PXI_CLK10 and the external reference clock using this parameter.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_clkin_attenuation_disable.html language=enus -->
## TOPIC 00046: NISYNC_ATTR_CLKIN_ATTENUATION_DISABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_clkin_attenuation_disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_clkin_attenuation_disable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_CLKIN_ATTENUATION_DISABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Use this attribute to specify whether or not to attenuate the signal at ClkIn. Setting this attribute to TRUE disables the ClkIn attenuation.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_clkin_pll_freq.html language=enus -->
## TOPIC 00047: NISYNC_ATTR_CLKIN_PLL_FREQ

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_clkin_pll_freq.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_clkin_pll_freq.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_CLKIN_PLL_FREQ

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the frequency of the clock the PLL circuit should lock to. Refer to your hardware manual to determine the specific frequency range the device's PLL circuit can lock to.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_clkin_pll_locked.html language=enus -->
## TOPIC 00048: NISYNC_ATTR_CLKIN_PLL_LOCKED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_clkin_pll_locked.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_clkin_pll_locked.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_CLKIN_PLL_LOCKED

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns whether or not the PLL circuit is locked to the external reference clock. This attribute returns TRUE when the PLL is locked.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_clkin_use_pll.html language=enus -->
## TOPIC 00049: NISYNC_ATTR_CLKIN_USE_PLL

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_clkin_use_pll.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_clkin_use_pll.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_CLKIN_USE_PLL

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies or returns whether or not the connection between ClkIn and PXI_Clk10 should use the PLL circuit. If this attribute is set to TRUE, the PLL circuit will be used to lock to the frequency of the external clock at ClkIn when connecting to PXI_CLK10. You must set this attribute before connecting an external clock to PXI_Clk10_In.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_clkout_gain_enable.html language=enus -->
## TOPIC 00050: NISYNC_ATTR_CLKOUT_GAIN_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_clkout_gain_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_clkout_gain_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_CLKOUT_GAIN_ENABLE

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Set this attribute to TRUE to increase the amplitude of the ClkOut terminal from 1 peak-to-peak volt to 2.5 peak-to-peak volts. Enable this attribute if you are distributing a clock between chassis to give the clock enough gain to reach its destination. Set the attribute to FALSE to return the amplitude to 1 peak-to-peak volt.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_dds_freq.html language=enus -->
## TOPIC 00051: NISYNC_ATTR_DDS_FREQ

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_dds_freq.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_dds_freq.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_DDS_FREQ

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the frequency, in Hz, of the DDS signal generated by the associated device. Use this parameter to generate a DDS clock signal at a specific frequency or to read the current DDS frequency.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_dds_initial_delay.html language=enus -->
## TOPIC 00052: NISYNC_ATTR_DDS_INITIAL_DELAY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_dds_initial_delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_dds_initial_delay.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_DDS_INITIAL_DELAY

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the initial delay, in seconds, that the associated device should wait before it begins generating a DDS signal. You must set this attribute prior to setting the DDS frequency, and you must set it using the same NI-Sync instrument driver session that you use to set the DDS frequency.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_dds_phase_adjust.html language=enus -->
## TOPIC 00053: NISYNC_ATTR_DDS_PHASE_ADJUST

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_dds_phase_adjust.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_dds_phase_adjust.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_DDS_PHASE_ADJUST

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | None |

#### Description

Specifies or returns the DDS Phase Adjust voltage.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_dds_update_source.html language=enus -->
## TOPIC 00054: NISYNC_ATTR_DDS_UPDATE_SOURCE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_dds_update_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_dds_update_source.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_DDS_UPDATE_SOURCE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | None |

#### Description

Specifies or returns the source terminal of the signal that triggers DDS generation. By default, the DDS signal generates as soon as you set the frequency. Using this attribute, you can generate or update the DDS frequency with an update pulse that arrives on a specified PXI_Trig terminal.

#### Defined Values

[NISYNC_VAL_DDS_UPDATE_IMMEDIATE](nisync_val_dds_update_immediate.html)

[NISYNC_VAL_PXITRIG0](nisync_val_pxitrig0.html)

[NISYNC_VAL_PXITRIG1](nisync_val_pxitrig1.html)

[NISYNC_VAL_PXITRIG2](nisync_val_pxitrig2.html)

[NISYNC_VAL_PXITRIG3](nisync_val_pxitrig3.html)

[NISYNC_VAL_PXITRIG4](nisync_val_pxitrig4.html)

[NISYNC_VAL_PXITRIG5](nisync_val_pxitrig5.html)

[NISYNC_VAL_PXITRIG6](nisync_val_pxitrig6.html)

[NISYNC_VAL_PXITRIG7](nisync_val_pxitrig7.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_dds_vcxo_voltage.html language=enus -->
## TOPIC 00055: NISYNC_ATTR_DDS_VCXO_VOLTAGE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_dds_vcxo_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_dds_vcxo_voltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_DDS_VCXO_VOLTAGE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | None |

#### Description

Specifies or returns the DDS VCXO voltage.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_front_sync_clk_src.html language=enus -->
## TOPIC 00056: NISYNC_ATTR_FRONT_SYNC_CLK_SRC

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_front_sync_clk_src.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_front_sync_clk_src.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_FRONT_SYNC_CLK_SRC

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | None |

#### Description

Specifies or returns the synchronization clock source for the front zone (PFI and PFI_LVDS) terminals.

#### Defined Values

[NISYNC_VAL_PFI0](nisync_val_pfi0.html)

[NISYNC_VAL_CLK10](nisync_val_clk10.html)

[NISYNC_VAL_DDS](nisync_val_dds.html)

[NISYNC_VAL_CLK100](nisync_val_clk100.html)

[NISYNC_VAL_CLKIN](nisync_val_clkin.html)

[NISYNC_VAL_OSCILLATOR](nisync_val_oscillator.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_gps_antenna_connected.html language=enus -->
## TOPIC 00057: NISYNC_ATTR_GPS_ANTENNA_CONNECTED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_gps_antenna_connected.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_gps_antenna_connected.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_GPS_ANTENNA_CONNECTED

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns whether or not the GPS antenna is properly connected. This attribute returns TRUE if a GPS antenna is connected.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_gps_mobile_mode.html language=enus -->
## TOPIC 00058: NISYNC_ATTR_GPS_MOBILE_MODE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_gps_mobile_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_gps_mobile_mode.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_GPS_MOBILE_MODE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies or returns whether or not the GPS uses mobile mode. If you enable mobile mode by setting the attribute to TRUE, you can move the GPS antenna and continuously calculate the current position and velocity. If you disable mobile mode by setting the parameter to FALSE, the antenna must remain in a fixed position while the computer is on. Timing accuracy is significantly improved with mobile mode disabled.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_gps_recalculate_position.html language=enus -->
## TOPIC 00059: NISYNC_ATTR_GPS_RECALCULATE_POSITION

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_gps_recalculate_position.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_gps_recalculate_position.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_GPS_RECALCULATE_POSITION

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies or returns whether or not the GPS receiver of the device should attempt to recalculate the current position every time the system reboots. If you set this value to FALSE, the GPS permanently stores the current location. GPS never performs a self survey until you set this attribute.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_gps_satellites_available.html language=enus -->
## TOPIC 00060: NISYNC_ATTR_GPS_SATELLITES_AVAILABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_gps_satellites_available.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_gps_satellites_available.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_GPS_SATELLITES_AVAILABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the number of GPS satellites currently being tracked. A minimum of four satellites must be visible for the onboard GPS receiver to perform a self survey. If you have selected GPS as the time reference, four or more satellites must be visible throughout timing measurements for the most accurate results.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_gps_self_survey.html language=enus -->
## TOPIC 00061: NISYNC_ATTR_GPS_SELF_SURVEY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_gps_self_survey.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_gps_self_survey.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_GPS_SELF_SURVEY

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the percentage of the GPS self survey that is complete. During a self-survey, the onboard GPS receiver performs position fixes, then the individual position fixes are accumulated and averaged. Therefore, the GPS time reference and location information are most accurate after the self survey has completed and least accurate at the beginning of a self survey. If you have set GPS as the selected time reference, wait until the self survey is complete prior to beginning timing measurements for the most accurate results.

The onboard GPS receiver requires at least four visible satellites to perform a self survey.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_gps_status.html language=enus -->
## TOPIC 00062: NISYNC_ATTR_GPS_STATUS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_gps_status.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_gps_status.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_GPS_STATUS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the status of GPS on the associated device. Query this attribute to determine if GPS is in a valid state before the application continues with other operations dependent on GPS. You can also use this attribute to troubleshoot various GPS errors.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Defined Values

[NISYNC_VAL_GPS_UNINITIALIZED](nisync_val_gps_uninitialized.html)

[NISYNC_VAL_GPS_ANTENNA_ERROR](nisync_val_gps_antenna_error.html)

[NISYNC_VAL_GPS_NO_USEABLE_SATELLITE](nisync_val_gps_no_useable_satellite.html)

[NISYNC_VAL_GPS_ONE_USEABLE_SATELLITE](nisync_val_gps_one_useable_satellite.html)

[NISYNC_VAL_GPS_TWO_USEABLE_SATELLITES](nisync_val_gps_two_useable_satellites.html)

[NISYNC_VAL_GPS_THREE_USEABLE_SATELLITES](nisync_val_gps_three_useable_satellites.html)

[NISYNC_VAL_GPS_NO_GPS_TIME](nisync_val_gps_no_gps_time.html)

[NISYNC_VAL_GPS_PDOP_TOO_HIGH](nisync_val_gps_pdop_too_high.html)

[NISYNC_VAL_GPS_UNUSABLE_SATELLITE](nisync_val_gps_unuseable_satellite.html)

[NISYNC_VAL_GPS_FIX_REJECTED](nisync_val_gps_fix_rejected.html)

[NISYNC_VAL_GPS_SELF_SURVEY_COMPLETE](nisync_val_gps_self_survey_complete.html)

[NISYNC_VAL_GPS_SELF_SURVEY_NOT_COMPLETE](nisync_val_gps_self_survey_not_complete.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_intf_num.html language=enus -->
## TOPIC 00063: NISYNC_ATTR_INTF_NUM

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_intf_num.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_intf_num.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_INTF_NUM

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the board/interface number of the connected NI-Sync device. If there are multiple instances of the NI-Sync device, each will have a unique interface number.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_oscillator_voltage.html language=enus -->
## TOPIC 00064: NISYNC_ATTR_OSCILLATOR_VOLTAGE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_oscillator_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_oscillator_voltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_OSCILLATOR_VOLTAGE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the tuning voltage for the selected device's oscillator. You can vary the oscillator frequency over a small range (between 0 and 3 volts). The tuning voltage adjusts the output frequency.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi0_10kohm_enable.html language=enus -->
## TOPIC 00065: NISYNC_ATTR_PFI0_10KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi0_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi0_10kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI0_10KOHM_ENABLE

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI0 terminal should be terminated with 10 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi0_1kohm_enable.html language=enus -->
## TOPIC 00066: NISYNC_ATTR_PFI0_1KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi0_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi0_1kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI0_1KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI0 terminal should be terminated with 1 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi0_threshold.html language=enus -->
## TOPIC 00067: NISYNC_ATTR_PFI0_THRESHOLD

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi0_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi0_threshold.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI0_THRESHOLD

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, for the PFI0 terminal of the associated device.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi1_10kohm_enable.html language=enus -->
## TOPIC 00068: NISYNC_ATTR_PFI1_10KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi1_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi1_10kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI1_10KOHM_ENABLE

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI1 terminal should be terminated with 10 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi1_1kohm_enable.html language=enus -->
## TOPIC 00069: NISYNC_ATTR_PFI1_1KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi1_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi1_1kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI1_1KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI1 terminal should be terminated with 1 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi1_threshold.html language=enus -->
## TOPIC 00070: NISYNC_ATTR_PFI1_THRESHOLD

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi1_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi1_threshold.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI1_THRESHOLD

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, of the PFI1 terminal of the associated device.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi2_10kohm_enable.html language=enus -->
## TOPIC 00071: NISYNC_ATTR_PFI2_10KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi2_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi2_10kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI2_10KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI2 terminal should be terminated with 10 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi2_1kohm_enable.html language=enus -->
## TOPIC 00072: NISYNC_ATTR_PFI2_1KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi2_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi2_1kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI2_1KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI2 terminal should be terminated with 1 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi2_threshold.html language=enus -->
## TOPIC 00073: NISYNC_ATTR_PFI2_THRESHOLD

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi2_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi2_threshold.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI2_THRESHOLD

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, of the PFI2 terminal of the associated device.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi3_10kohm_enable.html language=enus -->
## TOPIC 00074: NISYNC_ATTR_PFI3_10KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi3_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi3_10kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI3_10KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI3 terminal should be terminated with 10 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi3_1kohm_enable.html language=enus -->
## TOPIC 00075: NISYNC_ATTR_PFI3_1KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi3_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi3_1kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI3_1KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI3 terminal should be terminated with 1 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi3_threshold.html language=enus -->
## TOPIC 00076: NISYNC_ATTR_PFI3_THRESHOLD

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi3_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi3_threshold.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI3_THRESHOLD

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, of the PFI3 terminal of the associated device.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi4_10kohm_enable.html language=enus -->
## TOPIC 00077: NISYNC_ATTR_PFI4_10KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi4_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi4_10kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI4_10KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI4 terminal should be terminated with 10 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi4_1kohm_enable.html language=enus -->
## TOPIC 00078: NISYNC_ATTR_PFI4_1KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi4_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi4_1kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI4_1KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI4 terminal should be terminated with 1 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi4_threshold.html language=enus -->
## TOPIC 00079: NISYNC_ATTR_PFI4_THRESHOLD

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi4_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi4_threshold.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI4_THRESHOLD

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, of the PFI4 terminal of the associated device.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi5_10kohm_enable.html language=enus -->
## TOPIC 00080: NISYNC_ATTR_PFI5_10KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi5_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi5_10kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI5_10KOHM_ENABLE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI5 terminal should be terminated with 10 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi5_1kohm_enable.html language=enus -->
## TOPIC 00081: NISYNC_ATTR_PFI5_1KOHM_ENABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi5_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi5_1kohm_enable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI5_1KOHM_ENABLE

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI5 terminal should be terminated with 1 k[IMAGE alt='image' src='omega2.gif'] impedance.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pfi5_threshold.html language=enus -->
## TOPIC 00082: NISYNC_ATTR_PFI5_THRESHOLD

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pfi5_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pfi5_threshold.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PFI5_THRESHOLD

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, of the PFI5 terminal of the associated device.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_pxiclk10_present.html language=enus -->
## TOPIC 00083: NISYNC_ATTR_PXICLK10_PRESENT

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_pxiclk10_present.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_pxiclk10_present.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_PXICLK10_PRESENT

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns whether or not the PXI_Clk10 signal is present on the backplane. This attribute returns TRUE when the PXI_Clk10 signal is present.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_rear_sync_clk_src.html language=enus -->
## TOPIC 00084: NISYNC_ATTR_REAR_SYNC_CLK_SRC

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_rear_sync_clk_src.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_rear_sync_clk_src.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_REAR_SYNC_CLK_SRC

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | None |

#### Description

Specifies or returns the synchronization clock source for the rear zone (PXI_Trig, PXI_Star, and PXIe_DStarB) terminals.

#### Defined Values

[NISYNC_VAL_PFI0](nisync_val_pfi0.html)

[NISYNC_VAL_CLK10](nisync_val_clk10.html)

[NISYNC_VAL_DDS](nisync_val_dds.html)

[NISYNC_VAL_CLK100](nisync_val_clk100.html)

[NISYNC_VAL_CLKIN](nisync_val_clkin.html)

[NISYNC_VAL_OSCILLATOR](nisync_val_oscillator.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_serial_num.html language=enus -->
## TOPIC 00085: NISYNC_ATTR_SERIAL_NUM

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_serial_num.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_serial_num.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SERIAL_NUM

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the serial number of the connected NI-Sync device.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_sync_clk_div1.html language=enus -->
## TOPIC 00086: NISYNC_ATTR_SYNC_CLK_DIV1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_sync_clk_div1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_sync_clk_div1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SYNC_CLK_DIV1

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the value of the first clock divisor. Use this number to divide the full-speed synchronization clock and produce Divided Clock 1. The value must be a power of two between 2 and 512.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_sync_clk_div2.html language=enus -->
## TOPIC 00087: NISYNC_ATTR_SYNC_CLK_DIV2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_sync_clk_div2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_sync_clk_div2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SYNC_CLK_DIV2

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the value of the second clock divisor. Use this number to divide the full-speed synchronization clock and produce Divided Clock 2. The value must be a power of two between 2 and 512.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_sync_clk_pfi0_freq.html language=enus -->
## TOPIC 00088: NISYNC_ATTR_SYNC_CLK_PFI0_FREQ

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_sync_clk_pfi0_freq.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_sync_clk_pfi0_freq.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SYNC_CLK_PFI0_FREQ

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies or returns the frequency reference, in MHz, for the PFI0 terminal. You must have an external reference clock connected to PFI0 to call this attribute.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_sync_clk_rst_clk10_cntr_on_pxitrig.html language=enus -->
## TOPIC 00089: NISYNC_ATTR_SYNC_CLK_RST_CLK10_CNTR_ON_PXITRIG

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_sync_clk_rst_clk10_cntr_on_pxitrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_sync_clk_rst_clk10_cntr_on_pxitrig.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SYNC_CLK_RST_CLK10_CNTR_ON_PXITRIG

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies or returns whether or not PXI_Clk10 clock dividers should reset when the device receives an update pulse on a PXI_Trig line. You can specify which PXI_Trig line contains the update pulse using the [NISYNC_ATTR_SYNC_CLK_RST_PXITRIG_NUM](nisync_attr_sync_clk_rst_pxitrig_num.html) attribute. If TRUE, the PXI_Clk10 dividers reset on the rising edge of the update pulse.

|  | Note This attribute is supported only on signal-based devices. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_sync_clk_rst_dds_cntr_on_pxitrig.html language=enus -->
## TOPIC 00090: NISYNC_ATTR_SYNC_CLK_RST_DDS_CNTR_ON_PXITRIG

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_sync_clk_rst_dds_cntr_on_pxitrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_sync_clk_rst_dds_cntr_on_pxitrig.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SYNC_CLK_RST_DDS_CNTR_ON_PXITRIG

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies whether or not the DDS clock dividers should reset when the device receives an update pulse on the PXI_Trig line specified in the [NISYNC_ATTR_SYNC_CLK_RST_PXITRIG_NUM](nisync_attr_sync_clk_rst_pxitrig_num.html) attribute. If TRUE, the DDS clock dividers reset on the rising edge of the update pulse.

|  | Note This attribute is supported only on signal-based devices. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_sync_clk_rst_pfi0_cntr_on_pxitrig.html language=enus -->
## TOPIC 00091: NISYNC_ATTR_SYNC_CLK_RST_PFI0_CNTR_ON_PXITRIG

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_sync_clk_rst_pfi0_cntr_on_pxitrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_sync_clk_rst_pfi0_cntr_on_pxitrig.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SYNC_CLK_RST_PFI0_CNTR_ON_PXITRIG

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies or returns whether or not the PFI0 clock dividers should reset when the device receives an update pulse on a PXI_Trig line. You can specify which PXI_Trig line contains the update pulse using the [NISYNC_ATTR_SYNC_CLK_RST_PXITRIG_NUM](nisync_attr_sync_clk_rst_pxitrig_num.html) attribute. If TRUE, the PFI0 dividers reset on the rising edge of the update pulse.

|  | Note This attribute is supported only on signal-based devices. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_sync_clk_rst_pxitrig_num.html language=enus -->
## TOPIC 00092: NISYNC_ATTR_SYNC_CLK_RST_PXITRIG_NUM

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_sync_clk_rst_pxitrig_num.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_sync_clk_rst_pxitrig_num.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_SYNC_CLK_RST_PXITRIG_NUM

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | None |

#### Description

Specifies or returns which PXI_Trig terminal contains the update pulse used to reset the synchronization clock dividers. The default is none. You must set this value before you can reset synchronization clock dividers using an update pulse on a PXI_Trig line.

|  | Note This attribute is supported only on signal-based devices. |
| --- | --- |

#### Defined Values

[NISYNC_VAL_PXITRIG0](nisync_val_pxitrig0.html)

[NISYNC_VAL_PXITRIG1](nisync_val_pxitrig1.html)

[NISYNC_VAL_PXITRIG2](nisync_val_pxitrig2.html)

[NISYNC_VAL_PXITRIG3](nisync_val_pxitrig3.html)

[NISYNC_VAL_PXITRIG4](nisync_val_pxitrig4.html)

[NISYNC_VAL_PXITRIG5](nisync_val_pxitrig5.html)

[NISYNC_VAL_PXITRIG6](nisync_val_pxitrig6.html)

[NISYNC_VAL_PXITRIG7](nisync_val_pxitrig7.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_terminal_state_pfi.html language=enus -->
## TOPIC 00093: NISYNC_ATTR_TERMINAL_STATE_PFI

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_terminal_state_pfi.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_terminal_state_pfi.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TERMINAL_STATE_PFI

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PFI terminals by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PFI0, bit 1 corresponds to PFI1, etc. Bits 6 and above are not defined.

|  | Note Terminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_terminal_state_pfi_lvds.html language=enus -->
## TOPIC 00094: NISYNC_ATTR_TERMINAL_STATE_PFI_LVDS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_terminal_state_pfi_lvds.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_terminal_state_pfi_lvds.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TERMINAL_STATE_PFI_LVDS

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PFI_LVDS terminals by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PFI_LVDS0, bit 1 corresponds to PFI_LVDS1, etc.

|  | Note Terminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_terminal_state_pxiedstarbperipheral.html language=enus -->
## TOPIC 00095: NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARBPERIPHERAL

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_terminal_state_pxiedstarbperipheral.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_terminal_state_pxiedstarbperipheral.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARBPERIPHERAL

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns TRUE when there is a peripheral device connected to the PXIe_DStarB peripheral terminal.

|  | Note Terminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_terminal_state_pxiedstarc.html language=enus -->
## TOPIC 00096: NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARC

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_terminal_state_pxiedstarc.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_terminal_state_pxiedstarc.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARC

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PXIe_DStarC lines by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PXIe_DStarC0, bit 1 corresponds to PXIe_DStarC1, and so on.

|  | NoteTerminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. PXIe_DStarC lines default to the logic high state. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_terminal_state_pxistar.html language=enus -->
## TOPIC 00097: NISYNC_ATTR_TERMINAL_STATE_PXISTAR

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_terminal_state_pxistar.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_terminal_state_pxistar.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TERMINAL_STATE_PXISTAR

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PXI_Star lines by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PXI_Star0, bit 1 corresponds to PXI_Star1, and so on.

|  | NoteTerminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. PXI_Star lines default to the logic high state. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_terminal_state_pxistarperipheral.html language=enus -->
## TOPIC 00098: NISYNC_ATTR_TERMINAL_STATE_PXISTARPERIPHERAL

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_terminal_state_pxistarperipheral.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_terminal_state_pxistarperipheral.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TERMINAL_STATE_PXISTARPERIPHERAL

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns the logical state of the PXI_Star peripheral terminal. This value is only valid when the board is in a peripheral slot.

|  | Note Terminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_terminal_state_pxitrig.html language=enus -->
## TOPIC 00099: NISYNC_ATTR_TERMINAL_STATE_PXITRIG

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_terminal_state_pxitrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_terminal_state_pxitrig.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TERMINAL_STATE_PXITRIG

#### Specific Attribute

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PXI_Trig lines by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PXI_Trig0, bit 1 corresponds to PXI_Trig1, and so on.

|  | NoteTerminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. PXI_Trig lines default to the logic high state. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_correction.html language=enus -->
## TOPIC 00100: NISYNC_ATTR_TIMEREF_CORRECTION

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_correction.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_CORRECTION

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | RO | N/A | None | None |

#### Description

Specifies or returns a manual correction, in seconds, to apply to the specified module's board time. Use this attribute to calibrate the board time manually to achieve better synchronization with a selected time reference.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_enabled.html language=enus -->
## TOPIC 00101: NISYNC_ATTR_TIMEREF_ENABLED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_enabled.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_ENABLED

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies or returns whether the time reference connected to **activeItem** is enabled.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference by passing the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_is_selected.html language=enus -->
## TOPIC 00102: NISYNC_ATTR_TIMEREF_IS_SELECTED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_is_selected.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_is_selected.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_IS_SELECTED

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns whether the time reference specified by the **activeItem** parameter is the selected time reference for the device.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference by passing the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_last_sync_id.html language=enus -->
## TOPIC 00103: NISYNC_ATTR_TIMEREF_LAST_SYNC_ID

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_last_sync_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_last_sync_id.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_LAST_SYNC_ID

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Increments when a synchronization message is received from the current time reference.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.Synchronization messages are not received if the time reference is set to Free Running, or if the time reference is set to 1588 and the 1588 clock is a master. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_offset.html language=enus -->
## TOPIC 00104: NISYNC_ATTR_TIMEREF_OFFSET

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_offset.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_OFFSET

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | RO | N/A | None | None |

#### Description

Returns the calculated offset, in seconds, between the specified module's board clock and its selected time reference. Use this attribute to determine when the local clock is sufficiently synchronized with the selected time reference to continue operations.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_offset_ns.html language=enus -->
## TOPIC 00105: NISYNC_ATTR_TIMEREF_OFFSET_NS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_offset_ns.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_offset_ns.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_OFFSET_NS

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Returns the calculated offset, in nanoseconds, between the specified device's clock and its selected time reference. Use this attribute to determine when the local clock is sufficiently synchronized with the selected time reference to continue operations.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_present.html language=enus -->
## TOPIC 00106: NISYNC_ATTR_TIMEREF_PRESENT

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_present.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_present.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_PRESENT

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | RO | N/A | None | None |

#### Description

Returns TRUE if the selected time reference is currently providing a valid time signal. You must set an external time reference for this parameter to function.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_selected_name.html language=enus -->
## TOPIC 00107: NISYNC_ATTR_TIMEREF_SELECTED_NAME

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_selected_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_selected_name.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_SELECTED_NAME

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViConstString | RO | N/A | None | None |

#### Description

Returns the name of the selected time reference.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_selected_type.html language=enus -->
## TOPIC 00108: NISYNC_ATTR_TIMEREF_SELECTED_TYPE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_selected_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_selected_type.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_SELECTED_TYPE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Returns the time synchronization protocol (1588, EtherCAT, GPS, etc.) being used by the selected time reference of the specified device.

|  | Note For Linux RT devices, you must specify the time reference using the activeItem parameter when querying this attribute. |
| --- | --- |

#### Defined Values

| Description | Value |
| --- | --- |
| IEEE 1588-2008 | A network-based time synchronization protocol (also referred to as PTP) that synchronizes devices to a single grandmaster clock. Each IEEE 1588-2008 time reference instance is associated with a single network interface on the device and can either be a slave to the network's grandmaster, or the grandmaster to a network of devices. |
| IEEE 1588-2008 BC | Similar to the IEEE 1588-2008 protocol, except each instance of the IEEE 1588-2008 BC (boundary clock) time reference is associated with multiple ports, typically on a device that acts as a network switch. |
| IEEE 802.1AS-2011 | A network-based time synchronization protocol similar to IEEE 1588-2008, but optimized for time-sensitive applications. IEEE 802.1AS-2011 also provides fewer configuration options and requires IEEE 802.1AS-compatible network infrastructure. Each IEEE 802.1AS-2011 time reference instance is associated with a single network interface on the device and can either be a slave to the network's grandmaster or the grandmaster to a network of devices. |
| IEEE 802.1AS-2011 TAB | Similar to the IEEE 802.1AS-2011 protocol, except each IEEE 802.1AS-2011 TAB (time-aware bridge) time reference instance is associated with multiple ports, typically on a device that acts as a network switch. |
| IRIG-B | An encoded TTL signal that carries the absolute time, including the day, year, and straight binary seconds. IRIG-B is similar to a pulse per second (PPS) signal, but instead of outputting a single uniform pulse every second, IRIG-B sends coded bits that make up a one-second long data frame, and it repeats or re-synchronizes every second. |

|  | Note The values defined above are not a complete list of time reference types. Other time reference types can be installed by other NI software. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_type.html language=enus -->
## TOPIC 00109: NISYNC_ATTR_TIMEREF_TYPE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_type.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_TYPE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | N/A | None | None |

#### Description

Specifies or returns the synchronization protocol being used by the time reference connected to **activeItem**.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target.You must specify the time reference by passing the activeItem parameter when querying this attribute. |
| --- | --- |

#### Defined Values

| Description | Value |
| --- | --- |
| IEEE 1588-2008 | A network-based time synchronization protocol (also referred to as PTP) that synchronizes devices to a single grandmaster clock. Each IEEE 1588-2008 time reference instance is associated with a single network interface on the device and can either be a slave to the network's grandmaster, or the grandmaster to a network of devices. |
| IEEE 1588-2008 BC | Similar to the IEEE 1588-2008 protocol, except each instance of the IEEE 1588-2008 BC (boundary clock) time reference is associated with multiple ports, typically on a device that acts as a network switch. |
| IEEE 802.1AS-2011 | A network-based time synchronization protocol similar to IEEE 1588-2008, but optimized for time-sensitive applications. IEEE 802.1AS-2011 also provides fewer configuration options and requires IEEE 802.1AS-compatible network infrastructure. Each IEEE 802.1AS-2011 time reference instance is associated with a single network interface on the device and can either be a slave to the network's grandmaster or the grandmaster to a network of devices. |
| IEEE 802.1AS-2011 TAB | Similar to the IEEE 802.1AS-2011 protocol, except each IEEE 802.1AS-2011 TAB (time-aware bridge) time reference instance is associated with multiple ports, typically on a device that acts as a network switch. |
| IRIG-B | An encoded TTL signal that carries the absolute time, including the day, year, and straight binary seconds. IRIG-B is similar to a pulse per second (PPS) signal, but instead of outputting a single uniform pulse every second, IRIG-B sends coded bits that make up a one-second long data frame, and it repeats or re-synchronizes every second. |

|  | Note The values defined above are not a complete list of time reference types. Other time reference types can be installed by other NI software. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_utc_offset.html language=enus -->
## TOPIC 00110: NISYNC_ATTR_TIMEREF_UTC_OFFSET

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_utc_offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_utc_offset.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_TIMEREF_UTC_OFFSET

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies or returns the offset, in seconds, of the UTC timescale from the currently selected time reference.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_timeref_utc_offset_valid.html language=enus -->
## TOPIC 00111: NISYNC_ATTR_UTC_OFFSET_VALID

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_timeref_utc_offset_valid.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_timeref_utc_offset_valid.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_UTC_OFFSET_VALID

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Specifies or returns whether the UTC offset of the selected time reference is valid.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_attr_user_led_state.html language=enus -->
## TOPIC 00112: NISYNC_ATTR_USER_LED_STATE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_attr_user_led_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_attr_user_led_state.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_ATTR_USER_LED_STATE

| DataType | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Returns the state of the User LED. The LED lights when this attribute is set. When queried, this attribute returns TRUE when the LED is lit.

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_caladjustclk10phasevoltage.html language=enus -->
## TOPIC 00113: niSync_CalAdjustClk10PhaseVoltage

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_caladjustclk10phasevoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_caladjustclk10phasevoltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CalAdjustClk10PhaseVoltage

#### C Function Prototype

ViStatus niSync_CalAdjustClk10PhaseVoltage (ViSession vi, ViReal64 newVoltage, ViReal64* oldVoltage);

#### Purpose

Sets the Clk10 phase voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The value you enter for **newVoltage** is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant only if you set the action parameter of [niSync_CloseExtCal](nisync_closeextcal.html) to NISYNC_VAL_EXT_CAL_COMMIT.

|  | Notes This operation will succeed only during a session created with niSync_InitExtCal. Use the niSync_CalGetClk10PhaseVoltage function to return the Clk10 phase voltage value currently stored in the device's non-volatile onboard memory. This function does not immediately change the Clk10 phase voltage. Use the NISYNC_ATTR_CLK10_PHASE_ADJUST attribute to immediately adjust the Clk10 phase voltage. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_InitExtCal. The handle identifies the device to calibrateDefault Value: None |
| newVoltage | ViReal64 | Specifies the new Clk10 phase voltage value, in volts, to write to the non-volatile onboard memory of the instrument you are calibrating. |
| oldVoltage | ViReal64 | Returns the Clk10 phase voltage value, in volts, that was last written to the specified device's non-volatile onboard memory. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_caladjustddsstartpulsephasevoltage.html language=enus -->
## TOPIC 00114: niSync_CalAdjustDDSStartPulsePhaseVoltage

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_caladjustddsstartpulsephasevoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_caladjustddsstartpulsephasevoltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CalAdjustDDSStartPulsePhaseVoltage

#### C Function Prototype

ViStatus niSync_CalAdjustDDSStartPulsePhaseVoltage (ViSession vi, ViReal64 newVoltage, ViReal64* oldVoltage);

#### Purpose

Sets the DDS start pulse phase voltage to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The value you enter for **newVoltage** is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant only if you set the action parameter of [niSync_CloseExtCal](nisync_closeextcal.html) to NISYNC_VAL_EXT_CAL_COMMIT.

|  | Notes This operation will succeed only during a session created with niSync_InitExtCal. Use the niSync_CalGetDDSStartPulsePhaseVoltage function to return the DDS start pulse phase voltage value currently stored in the device's non-volatile onboard memory. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_InitExtCal. The handle identifies the device to calibrate.Default Value: None |
| newVoltage | ViReal64 | Specifies the new DDS start pulse phase voltage value, in volts, to write to the non-volatile onboard memory of the instrument you are calibrating. |
| oldVoltage | ViReal64 | Returns the DDS start pulse phase voltage, in volts, last written to the device's non-volatile onboard memory. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_caladjustoscillatorvoltage.html language=enus -->
## TOPIC 00115: niSync_CalAdjustOscillatorVoltage

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_caladjustoscillatorvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_caladjustoscillatorvoltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CalAdjustOscillatorVoltage

#### C Function Prototype

ViStatus niSync_CalAdjustOscillatorVoltage (ViSession vi, ViReal64 newVoltage, ViReal64* oldVoltage);

#### Purpose

Sets the oscillator voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference. The oscillator voltage controls the frequency of the specified device's oscillator.

The value you enter for **newVoltage** is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant only if you set the action parameter of [niSync_CloseExtCal](nisync_closeextcal.html) to NISYNC_VAL_EXT_CAL_COMMIT.

|  | Notes This operation will succeed only during a session created with niSync_InitExtCal. Use niSync_CalGetOscillatorVoltage to return the oscillator voltage value currently stored in the device's non-volatile onboard memory. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_InitExtCal. The handle identifies the device to calibrate. |
| newVoltage | ViReal64 | Specifies the value of the new oscillator voltage, in volts, to write to the device's non-volatile onboard memory. |
| oldVoltage | ViReal64 | Returns the value of the oscillator voltage, in volts, last written to the device's non-volatile onboard memory. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_calgetclk10phasevoltage.html language=enus -->
## TOPIC 00116: niSync_CalGetClk10PhaseVoltage

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_calgetclk10phasevoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_calgetclk10phasevoltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CalGetClk10PhaseVoltage

#### C Function Prototype

ViStatus niSync_CalGetClk10PhaseVoltage (ViSession vi, ViReal64* voltage);

#### Purpose

Reads the Clk10 phase voltage value, in volts, currently stored on the specified device's non-volatile onboard memory.

You can adjust this value using [niSync_CalAdjustClk10PhaseVoltage](nisync_caladjustclk10phasevoltage.html). Use this function in conjunction with the other NI-Sync external calibration functions to determine if the device needs an external calibration session.

|  | Note You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either niSync_init or niSync_InitExtCal. If you adjust the Clk10 phase voltage using niSync_CalAdjustClk10PhaseVoltage as part of an open session, this function returns the new Clk10 phase voltage value you set using niSync_CalAdjustClk10PhaseVoltage. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session. |
| voltage | ViReal64 | Returns the current Clk10 phase voltage, in volts, stored on the device's non-volatile onboard memory. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_calgetddsstartpulsephasevoltage.html language=enus -->
## TOPIC 00117: niSync_CalGetDDSStartPulsePhaseVoltage

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_calgetddsstartpulsephasevoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_calgetddsstartpulsephasevoltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CalGetDDSStartPulsePhaseVoltage

#### C Function Prototype

ViStatus niSync_CalGetDDSStartPulsePhaseVoltage (ViSession vi, ViReal64* voltage);

#### Purpose

Reads the phase voltage of the DDS start pulse currently stored on the specified device's non-volatile onboard memory.

You can adjust this value using [niSync_CalAdjustDDSStartPulsePhaseVoltage](nisync_caladjustddsstartpulsephasevoltage.html). Use this function to determine if your device needs to be externally calibrated.

|  | Note You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either niSync_init or niSync_InitExtCal. If you adjust the DDS start pulse phase voltage using niSync_CalAdjustDDSStartPulsePhaseVoltage as part of an open session, this function returns the new DDS start pulse phase voltage value you set using niSync_CalAdjustDDSStartPulsePhaseVoltage. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session. |
| voltage | ViReal64 | Returns the current DDS start pulse phase voltage, in volts, stored in the device's non-volatile onboard memory. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_calgetoscillatorvoltage.html language=enus -->
## TOPIC 00118: niSync_CalGetOscillatorVoltage

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_calgetoscillatorvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_calgetoscillatorvoltage.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CalGetOscillatorVoltage

#### C Function Prototype

ViStatus niSync_CalGetOscillatorVoltage (ViSession vi, ViReal64* voltage);

#### Purpose

Reads the voltage that controls the oscillator frequency currently stored on the specified device's non-volatile onboard memory.

You can adjust the oscillator voltage using [niSync_CalAdjustOscillatorVoltage](nisync_caladjustoscillatorvoltage.html) during an external calibration session. Use this function in conjunction with other NI-Sync external calibration functions to determine if your device needs an external calibration session.

|  | Note You do not need a calibration password to use this function. It can be invoked with an instrument handle created with either niSync_init or niSync_InitExtCal. If you adjust the oscillator voltage using niSync_CalAdjustOscillatorVoltage as part of an open session, this function returns the new oscillator voltage value you set using niSync_CalAdjustOscillatorVoltage. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session. |
| voltage | ViReal64 | Returns the oscillator voltage, in volts, currently stored in the device's non-volatile onboard memory. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_changeextcalpassword.html language=enus -->
## TOPIC 00119: niSync_ChangeExtCalPassword

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_changeextcalpassword.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_changeextcalpassword.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ChangeExtCalPassword

#### C Function Prototype

ViStatus niSync_ChangeExtCalPassword (ViSession vi, ViConstString oldPassword, ViConstString newPassword);

#### Purpose

Sets the password required to begin a new external calibration session on the specified device.

|  | Note You must supply the existing calibration password using the oldPassword parameter for this operation to succeed. If this is the first time you have set the device's calibration password, refer to the device's calibration procedure manual to find the default calibration password. In order to successfully change the calibration password, you must call niSync_CloseExtCal and set the action parameter to NISYNC_VAL_EXT_CAL_COMMIT. You can invoke this function with an instrument handle created with either niSync_init or niSync_InitExtCal. |
| --- | --- |

#### Parameters

| Name | Type | Description |  |  |  |
| --- | --- | --- | --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session. |  |  |  |
| oldPassword | ViConstString | Specifies the old external calibration password for the device. oldPassword must exactly match the value, including case, in the device's non-volatile onboard memory for this operation to succeed. | newPassword | ViConstString | Specifies the new external calibration password for the module. The new password is case-sensitive and must be entered exactly to begin a new calibration session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_clearclock.html language=enus -->
## TOPIC 00120: niSync_ClearClock

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_clearclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_clearclock.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ClearClock

#### C Function Prototype

ViStatus _VI_FUNC niSync_ClearClock (ViSession vi, ViConstString terminal);

#### Purpose

Frees a resource that contains a clock generated by [niSync_CreateClock](nisync_createclock.html). Once you clear the clock, you can use the associated terminal for other operations.

|  | Note This function is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the line that contains the generated clock to clear. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_clearfuturetimeevents.html language=enus -->
## TOPIC 00121: niSync_ClearFutureTimeEvents

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_clearfuturetimeevents.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_clearfuturetimeevents.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ClearFutureTimeEvents

#### C Function Prototype

ViStatus _VI_FUNC niSync_ClearFutureTimeEvents (ViSession vi, ViConstString terminal);

#### Purpose

Frees the specified terminal of any future time events previously created by the [niSync_CreateFutureTimeEvent](nisync_createfuturetimeevent.html) function that have not yet occurred.

Once you invoke this function, you can use the associated terminal for other operations. The specified line is tri-stated and the resource is freed.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the terminal that from which to clear future time events. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_close.html language=enus -->
## TOPIC 00122: niSync_close

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_close.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_close.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_close

#### C Function Prototype

ViStatus niSync_close (ViSession vi);

#### Purpose

Ends an NI-Sync instrument driver session and frees the device for other operations.

You must use this function any time you begin a session using [niSync_init](nisync_init.html). This function clears or disables any generated clocks, future time events, and timestamp triggers on the associated device.

|  | Note If the session is locked, you must unlock the session before calling niSync_close. After calling niSync_close, you cannot use the instrument driver again until you call niSync_init. If any clocks have been created with niSync_CreateClock in the context of this session and have not been cleared, this function clears them. If any future time events have been created with niSync_CreateFutureTimeEvent in the context of this session and have not occurred or been cleared, this function clears them. If any timestamp triggers have been enabled with niSync_EnableTimeStampTrigger in the context of this session and have not been disabled, this function clears them. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_closeextcal.html language=enus -->
## TOPIC 00123: niSync_CloseExtCal

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_closeextcal.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_closeextcal.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CloseExtCal

#### C Function Prototype

ViStatus niSync_CloseExtCal (ViSession vi, ViInt32 action);

#### Purpose

Ends an external calibration session you began using [niSync_InitExtCal.](nisync_initextcal.html)

When you set new calibration constants using an external calibration function such as [niSync_CalAdjustClk10PhaseVoltage](nisync_caladjustclk10phasevoltage.html), [niSync_CalAdjustDDSStartPulsePhaseVoltage](nisync_caladjustddsstartpulsephasevoltage.html), or [niSync_CalAdjustOscillatorVoltage](nisync_caladjustoscillatorvoltage.html), you must set the **action** parameter to Commit to write the new calibration constants to the device's EEPROM. If you do not set **action** to Commit, changes made using external calibration functions will not be applied.

|  | Note If the session is locked, you must unlock the session before calling niSync_CloseExtCal. After invoking niSync_CloseExtCal, you cannot use the the NI-Sync session handle again until you invoke niSync_init or niSync_InitExtCal. If you invoke this function with action set to Commit, the function updates the external calibration date stored in the device's non-volatile onboard memory, even if no calibration constants were changed. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | Specifies the instrument handle that you obtain from niSync_init or niSync_InitExtCal. |
| action | ViInt32 | Specifies whether or not to write the external calibration constants set using an external calibration function to the device's non-volatile onboard memory. Valid Values: NISYNC_VAL_EXT_CAL_ABORT (Default Value) NISYNC_VAL_EXT_CAL_COMMIT |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_configurefpga.html language=enus -->
## TOPIC 00124: niSync_ConfigureFPGA

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_configurefpga.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_configurefpga.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ConfigureFPGA

#### C Function Prototype

ViStatus niSync_ConfigureFPGA (ViSession vi, ViConstString fpgaProgramPath);

#### Purpose

Reprograms the FPGA circuits on the specified device using an alternate bitstream file.

|  | Caution Use this function carefully: it is an advanced operation that requires in-depth knowledge of your hardware. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| fpgaProgramPath | ViConstString | Specifies the absolute path to an FPGA bitstream file on disk. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_connectclkterminals.html language=enus -->
## TOPIC 00125: niSync_ConnectClkTerminals

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_connectclkterminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_connectclkterminals.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ConnectClkTerminals

#### C Function Prototype

ViStatus niSync_ConnectClkTerminals (ViSession vi, ViConstString sourceTerminal, ViConstString destinationTerminal);

#### Purpose

Connects a source clock terminal to a destination clock terminal. A clock terminal connection is characterized by its source terminal and destination terminal.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | Specifies the source terminal of the clock you would like to connect. Valid Values: NISYNC_VAL_CLKIN (Default Value) NISYNC_VAL_CLK10 NISYNC_VAL_OSCILLATOR NISYNC_VAL_DDS NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16 Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |
| destinationTerminal | ViConstString | Specifies where to route the clock signal specified in the sourceTerminal. Valid Values: NISYNC_VAL_CLK10_IN (Default Value) NISYNC_VAL_CLKOUT NISYNC_VAL_BOARD_CLK NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARA0 NISYNC_VAL_PXIEDSTARA1 NISYNC_VAL_PXIEDSTARA2 NISYNC_VAL_PXIEDSTARA3 NISYNC_VAL_PXIEDSTARA4 NISYNC_VAL_PXIEDSTARA5 NISYNC_VAL_PXIEDSTARA6 NISYNC_VAL_PXIEDSTARA7 NISYNC_VAL_PXIEDSTARA8 NISYNC_VAL_PXIEDSTARA9 NISYNC_VAL_PXIEDSTARA10 NISYNC_VAL_PXIEDSTARA11 NISYNC_VAL_PXIEDSTARA12 NISYNC_VAL_PXIEDSTARA13 NISYNC_VAL_PXIEDSTARA14 NISYNC_VAL_PXIEDSTARA15 NISYNC_VAL_PXIEDSTARA16 Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_connectswtrigtoterminal.html language=enus -->
## TOPIC 00126: niSync_ConnectSWTrigToTerminal

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_connectswtrigtoterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_connectswtrigtoterminal.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ConnectSWTrigToTerminal

#### C Function Prototype

ViStatus niSync_ConnectSWTrigToTerminal (ViSession vi, ViConstString sourceTerminal, ViConstString destinationTerminal, ViConstString synchronizationClock, ViInt32 invert, ViInt32 updateEdge, ViReal64 delay);

#### Purpose

Connects the global software trigger terminal to a destination trigger terminal.

Once you connect the global software trigger, you can fire the trigger using [niSync_SendSoftwareTrigger](nisync_sendsoftwaretrigger.html).

|  | Note The destination terminal you specify in this function determines the full-speed synchronization clock used by the global software trigger. PFI and PFI_LVDS lines are in the front trigger zone, and PXI_Trig, PXI_Star, and PXIe_DStarB lines are in the rear trigger zone. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | Specifies the source software trigger terminal to connect to the destination terminal. Valid Values: NISYNC_VAL_SWTRIG_GLOBAL (Default Value) |
| destinationTerminal | ViConstString | Specifies the destination trigger terminal that the global software trigger terminal will connect to. Valid Values: NISYNC_VAL_PXITRIG0 (Default Value) NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16 Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |
| synchronizationClock | ViConstString | Specifies whether to use the full-speed or a divided synchronization clock to control when the global software trigger fires. The global software trigger will be synchronized with the rising or falling edge of the clock you select in this terminal. Note Asynchronous connections are not valid for software trigger terminal connections.The source of the synchronization clock for software trigger connections is determined by the destination terminal trigger "zone" ("front" for the PFI and PFI_LVDS lines, and "rear" for the PXI_Trig, PXI_Star, and PXIe_DStarB terminals). The source of the synchronization clock for a given trigger zone can be selected using the NISYNC_ATTR_FRONT_SYNC_CLK_SRC (PFI zone) and NISYNC_ATTR_REAR_SYNC_CLK_SRC (PXI backplane zone) attributes. Valid Values:NISYNC_VAL_SYNC_CLK_FULLSPEED (Default Value)NISYNC_VAL_SYNC_CLK_DIV1NISYNC_VAL_SYNC_CLK_DIV2 |
|  | Note Asynchronous connections are not valid for software trigger terminal connections.The source of the synchronization clock for software trigger connections is determined by the destination terminal trigger "zone" ("front" for the PFI and PFI_LVDS lines, and "rear" for the PXI_Trig, PXI_Star, and PXIe_DStarB terminals). The source of the synchronization clock for a given trigger zone can be selected using the NISYNC_ATTR_FRONT_SYNC_CLK_SRC (PFI zone) and NISYNC_ATTR_REAR_SYNC_CLK_SRC (PXI backplane zone) attributes. |  |
| invert | ViInt32 | Specifies whether or not to invert the digital signal of the Global Software Trigger when it reaches the destination terminal. Valid Values: NISYNC_VAL_DONT_INVERT NISYNC_VAL_INVERT |
| updateEdge | ViInt32 | Specifies the synchronization clock update edge that the global software trigger should be propagated on. Valid Values: NISYNC_VAL_UPDATE_EDGE_RISING (Default Value) NISYNC_VAL_UPDATE_EDGE_FALLING |
| delay | ViReal64 | Specifies the number of seconds to delay the global software trigger pulse. The delay must be a multiple of the synchronization clock period. The global software trigger can be delayed up to 15 clock cycles for each route. Default Value: 0.00 seconds Note This input is not supported on the PXIe-6674. |
|  | Note This input is not supported on the PXIe-6674. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_connecttrigterminals.html language=enus -->
## TOPIC 00127: niSync_ConnectTrigTerminals

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_connecttrigterminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_connecttrigterminals.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ConnectTrigTerminals

#### C Function Prototype

ViStatus niSync_ConnectTrigTerminals (ViSession vi, ViConstString sourceTerminal, ViConstString destinationTerminal, ViConstString synchronizationClock, ViInt32 invert, ViInt32 updateEdge);

#### Purpose

Routes triggers through the PXI backplane, between devices, or between multiple chassis.

Once a terminal route is connected, you can invert the trigger signal at the destination terminal, synchronize the trigger to the rising or falling edge of a synchronization clock, fire the trigger asynchronously, or route the trigger to other trigger terminals.

You can also route clocks along some trigger lines by setting a full speed or divided synchronization clock as the **source terminal**.

|  | Note The destination terminal determines the source of the trigger's synchronization clock. PFI and PFI_LVDS lines are in the front trigger zone, and PXI_Trig, PXI_Star, and PXIe_DStar lines are in the rear trigger zone. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | Specifies the source of the trigger you want to connect to the destination terminal. Note The source of the synchronization clock for trigger connections is determined by the destination terminal (either the PFI sync clock zone or the backplane sync clock zone). Also, the two divided versions of the synchronization clock are shared between the PFI sync clock zone and the backplane sync clock zone. Valid Values: NISYNC_VAL_PXITRIG0 (Default Value) NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_GND NISYNC_VAL_SYNC_CLK_FULLSPEED NISYNC_VAL_SYNC_CLK_DIV1 NISYNC_VAL_SYNC_CLK_DIV2 NISYNC_VAL_CLKIN NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16 Note Each PXI_Star and PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note The source of the synchronization clock for trigger connections is determined by the destination terminal (either the PFI sync clock zone or the backplane sync clock zone). Also, the two divided versions of the synchronization clock are shared between the PFI sync clock zone and the backplane sync clock zone. |  |
|  | Note Each PXI_Star and PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |
| destinationTerminal | ViConstString | Specifies the destination trigger terminal that the source terminal will connect to.. Valid Values: NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 (Default Value) NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16 Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |
| synchronizationClock | ViConstString | Specifies whether to use the full-speed or a divided synchronization clock to control when the trigger fires. The trigger will be synchronized with the rising or falling edge of the clock you select in this terminal. Note The source of the synchronization clock for software trigger connections is determined by the destination terminal trigger "zone" ("front" for the PFI and PFI_LVDS lines, and "rear" for the PXI_Trig, PXI_Star, and PXIe_DStarB terminals). The source of the synchronization clock for a given trigger zone can be selected using the NISYNC_ATTR_FRONT_SYNC_CLK_SRC (PFI zone) and NISYNC_ATTR_REAR_SYNC_CLK_SRC (PXI backplane zone) attributes. Valid Values:NISYNC_VAL_SYNC_CLK_ASYNC (Default)NISYNC_VAL_SYNC_CLK_FULLSPEEDNISYNC_VAL_SYNC_CLK_DIV1NISYNC_VAL_SYNC_CLK_DIV2 |
|  | Note The source of the synchronization clock for software trigger connections is determined by the destination terminal trigger "zone" ("front" for the PFI and PFI_LVDS lines, and "rear" for the PXI_Trig, PXI_Star, and PXIe_DStarB terminals). The source of the synchronization clock for a given trigger zone can be selected using the NISYNC_ATTR_FRONT_SYNC_CLK_SRC (PFI zone) and NISYNC_ATTR_REAR_SYNC_CLK_SRC (PXI backplane zone) attributes. |  |
| invert | ViInt32 | Specifies whether or not to invert the source terminal signal at the destination terminal. Note The source and destination must be connected synchronously for the signal to be inverted. Valid Values: NISYNC_VAL_DONT_INVERT (Default Value) NISYNC_VAL_INVERT |
|  | Note The source and destination must be connected synchronously for the signal to be inverted. |  |
| updateEdge | ViInt32 | Specifies on which update edge of the synchronization clock to propagate the trigger. Note You must connect the source and destination terminals synchronously for this parameter to apply. Valid Values: NISYNC_VAL_UPDATE_EDGE_RISING (Default Value) NISYNC_VAL_UPDATE_EDGE_FALLING |
|  | Note You must connect the source and destination terminals synchronously for this parameter to apply. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_createclock.html language=enus -->
## TOPIC 00128: niSync_CreateClock

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_createclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_createclock.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_CreateClock

#### C Function Prototype

ViStatus _VI_FUNC niSync_CreateClock (ViSession vi, ViConstString terminal, ViUInt32 highTicks, ViUInt32 lowTicks, ViUInt32 startTimeSeconds, ViUInt32 startTimeNanoseconds, ViUInt16 startTimeFractionalNanoseconds, ViUInt32 stopTimeSeconds, ViUInt32 stopTimeNanoseconds, ViUInt16 stopTimeFractionalNanoseconds);

#### Purpose

Generates a clock that is synchronized to the board time associated with the specified session handle. The terminal associated with this clock cannot be used for other operations until the clock is cleared with the [niSync_ClearClock](nisync_clearclock.html) function or the session is closed with the [niSync_close](nisync_close.html) function. When this function is invoked, the digital signal on the specified terminal is driven low until the clock starts.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the line you would like to generate the clock on. You cannot use this terminal for other operations until you clear the generated clock using niSync_ClearClock or you close the session with niSync_close. |
| highTicks | ViUInt32 | Specifies the number of ticks the generated clock should spend in the high logic state. The clock resolution, which can be queried using the NISYNC_ATTR_1588_CLK_RESOLUTION attribute, determines the length of a tick. |
| lowTicks | ViUInt32 | Specifies the number of ticks the generated clock should spend in the low logic state. The clock resolution, which can be queried using the NISYNC_ATTR_1588_CLK_RESOLUTION attribute, determines the length of a tick. |
| startTimeSeconds | ViUInt32 | Specifies, in seconds, when to start the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is 0, which generates the clock as soon as the function is invoked. |
| startTimeNanoseconds | ViUInt32 | Specifies, in nanoseconds, when to start the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is 0, which generates the clock as soon as the function is invoked. |
| startTimeFractionalNanoseconds | ViUInt16 | Specifies, in fractional nanoseconds, when to start the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is 0, which generates the clock as soon as the function is invoked. |
| stopTimeSeconds | ViUInt32 | Specifies, in seconds, when to stop the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is 0, which never stops the clock. |
| stopTimeNanoseconds | ViUInt32 | Specifies, in nanoseconds, when to stop the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is 0, which never stops the clock. |
| stopTimeFractionalNanoseconds | ViUInt16 | Specifies, in fractional nanoseconds, when to stop the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is 0, which never stops the clock. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_createfuturetimeevent.html language=enus -->
## TOPIC 00129: niSync_CreateFutureTimeEvent

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_createfuturetimeevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_createfuturetimeevent.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_CreateFutureTimeEvent

### niSync_CreateFutureTimeEvent

#### C Function Prototype

ViStatus _VI_FUNC niSync_CreateFutureTimeEvent (ViSession vi, ViConstString terminal, ViInt32 outputLevel, ViUInt32 timeSeconds, ViUInt32 timeNanoseconds, ViUInt16 timeFractionalNanoseconds);

#### Purpose

Schedules a future time event. A future time event changes the digital signal at the terminal you specify—either from low to high or high to low—when the board time of the specified module reaches the time you specify with **time**. The future time event you create with this function is synchronized with the board time of the module you specify with **instrument handle**.

To create multiple future time events, invoke this function multiple times. Once you generate a future time event on a terminal, that terminal cannot be used for operations other than generating future time events until you clear all future time events with [niSync_ClearFutureTimeEvents](nisync_clearfuturetimeevents.html) or you close the session with [niSync_close](nisync_close.html). When you invoke this function, the digital signal on the specified terminal is driven low until the first future time event occurs.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the terminal whose digital signal will be changed by the future time event. |
| outputLevel | ViInt32 | Specifies the level to set the digital signal to when the future time event occurs.Valid Values:NISYNC_VAL_LEVEL_LOWNISYNC_VAL_LEVEL_HIGH |
| timeSeconds | ViUInt32 | Specifies, in seconds, the board time when the future time event occurs. When the board time of the module you specify in the vi attribute reaches this time, the digital signal of the terminal input changes to the value you specify in the outputLevel attribute. The default value of this input is 0, which triggers the future time event as soon as the function is invoked. Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, the specified number of seconds is assumed to be within the supported time range. |
|  | Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, the specified number of seconds is assumed to be within the supported time range. |  |
| timeNanoseconds | ViUInt32 | Specifies, in nanoseconds, the board time when the future time event occurs. When the board time of the module you specify in the vi attribute reaches this time, the digital signal of the terminal input changes to the value you specify in the outputLevel attribute. The default value of this input is 0, which triggers the future time event as soon as the function is invoked. Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, the specified number of seconds is assumed to be within the supported time range. |
|  | Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, the specified number of seconds is assumed to be within the supported time range. |  |
| timeFractionalNanoseconds | ViUInt16 | Specifies, in fractional nanoseconds, the board time when the future time event occurs. When the board time of the module you specify in the vi attribute reaches this time, the digital signal of the terminal input changes to the value you specify in the outputLevel attribute. The default value of this input is 0, which triggers the future time event as soon as the function is invoked. Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, the specified number of seconds is assumed to be within the supported time range. |
|  | Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, the specified number of seconds is assumed to be within the supported time range. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_disablegpstimestamping.html language=enus -->
## TOPIC 00130: niSync_DisableGPSTimestamping

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_disablegpstimestamping.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_disablegpstimestamping.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_DisableGPSTimestamping

#### C Function Prototype

ViStatus _VI_FUNC niSync_DisableGPSTimestamping (ViSession vi);

#### Purpose

Disables timestamping of the GPS pulse per second enabled by [niSync_EnableGPSTimestamping](nisync_enablegpstimestamping.html).

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_disableirigtimestamping.html language=enus -->
## TOPIC 00131: niSync_DisableIRIGTimestamping

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_disableirigtimestamping.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_disableirigtimestamping.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_DisableIRIGTimestamping

#### C Function Prototype

ViStatus _VI_FUNC niSync_DisableIRIGTimestamping (ViSession vi, ViConstString terminalName);

#### Purpose

Disables timestamping of IRIG-B AM or IRIG-B DC decods enabled by [niSync_EnableIRIGTimestamping](nisync_enableirigtimestamping.html). The associated terminal may be used for other operations once timestamping has been disabled.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | viConstString | Specifies the terminal on which to disable IRIG decoding. You can then use this terminal for other operations. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_disabletimestamptrigger.html language=enus -->
## TOPIC 00132: niSync_DisableTimeStampTrigger

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_disabletimestamptrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_disabletimestamptrigger.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_DisableTimeStampTrigger

#### C Function Prototype

ViStatus _VI_FUNC niSync_DisableTimeStampTrigger (ViSession vi, ViConstString terminal);

#### Purpose

Disables a timestamp trigger enabled by the [niSync_EnableTimeStampTrigger](nisync_enabletimestamptrigger.html) function. Once the time stamp trigger is disabled, you can use the associated terminal for other operations.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the terminal that you would like to stop timestamping on. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_disconnectclkterminals.html language=enus -->
## TOPIC 00133: niSync_DisconnectClkTerminals

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_disconnectclkterminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_disconnectclkterminals.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_DisconnectClkTerminals

#### C Function Prototype

ViStatus niSync_DisconnectClkTerminals (ViSession vi, ViConstString sourceTerminal, ViConstString destinationTerminal);

#### Purpose

Closes a route between a source clock terminal and a destination clock terminal. You must use this function any time you connect clock terminals using [niSync_ConnectClkTerminals](nisync_connectclkterminals.html). Once you invoke this function, the specified terminal will be free to perform other operations.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | Specifies the source clock terminal you want to disconnect from the destination terminal. The source and destination terminals must be connected for this operation to succeed. Valid Values: NISYNC_VAL_CLKIN NISYNC_VAL_CLK10 NISYNC_VAL_OSCILLATOR NISYNC_VAL_DDS NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_ALL_CONNECTED (Default Value) Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |
| destinationTerminal | ViConstString | Specifies the destination clock terminal you would like to disconnect from the source terminal. The source and destination terminals must be connected for this operation to succeed. Valid Values: NISYNC_VAL_CLKIN NISYNC_VAL_CLK10_IN NISYNC_VAL_CLKOUT NISYNC_VAL_BOARD_CLK NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARA0 NISYNC_VAL_PXIEDSTARA1 NISYNC_VAL_PXIEDSTARA2 NISYNC_VAL_PXIEDSTARA3 NISYNC_VAL_PXIEDSTARA4 NISYNC_VAL_PXIEDSTARA5 NISYNC_VAL_PXIEDSTARA6 NISYNC_VAL_PXIEDSTARA7 NISYNC_VAL_PXIEDSTARA8 NISYNC_VAL_PXIEDSTARA9 NISYNC_VAL_PXIEDSTARA10 NISYNC_VAL_PXIEDSTARA11 NISYNC_VAL_PXIEDSTARA12 NISYNC_VAL_PXIEDSTARA13 NISYNC_VAL_PXIEDSTARA14 NISYNC_VAL_PXIEDSTARA15 NISYNC_VAL_PXIEDSTARA16 NISYNC_VAL_ALL_CONNECTED (Default Value) Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_disconnectswtrigfromterminal.html language=enus -->
## TOPIC 00134: niSync_DisconnectSWTrigFromTerminal

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_disconnectswtrigfromterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_disconnectswtrigfromterminal.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_DisconnectSWTrigFromTerminal

#### C Function Prototype

ViStatus niSync_DisconnectSWTrigFromTerminal (ViSession vi, ViConstString sourceTerminal, ViConstString destinationTerminal);

#### Purpose

Closes a route between the global software trigger and a destination trigger terminal. You must use this function every time you connect a software trigger using [niSync_ConnectSWTrigToTerminal](nisync_connectswtrigtoterminal.html). Once you invoke this function, you can use the associated terminal for other operations.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | Specifies the source software trigger terminal you want to disconnect from the destination terminal. The global software trigger must be connected to the destination terminal for this operation to succeed. The only acceptable value is Global Software Trigger. Valid Values: NISYNC_VAL_SWTRIG_GLOBAL (Default Value) |
| destinationTerminal | ViConstString | Specifies the destination trigger terminal to disconnect the global software trigger terminal from. The global software trigger must be connected to the destination terminal for this operation to succeed. Valid Values: NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16 NISYNC_VAL_ALL_CONNECTED (Default Value) Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_disconnecttrigterminals.html language=enus -->
## TOPIC 00135: niSync_DisconnectTrigTerminals

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_disconnecttrigterminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_disconnecttrigterminals.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_DisconnectTrigTerminals

#### C Function Prototype

ViStatus niSync_DisconnectTrigTerminals (ViSession vi, ViConstString sourceTerminal, ViConstString destinationTerminal);

#### Purpose

This function disconnects a source trigger terminal from a destination trigger terminal.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | This input specifies the source trigger terminal to disconnect from the destination terminal. The source and destination terminals must be connected for this operation to succeed. Valid Values: NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_GND NISYNC_VAL_SYNC_CLK_FULLSPEED NISYNC_VAL_SYNC_CLK_DIV1 NISYNC_VAL_SYNC_CLK_DIV2 NISYNC_VAL_CLKIN NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_ALL_CONNECTED (Default Value) Note Each PXI_Star and PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXI_Star and PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |
| destinationTerminal | ViConstString | This input specifies the destination trigger terminal that the source terminal disconnect from. The source and destination terminals must be connected for this operation to succeed. Valid Values: NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16 NISYNC_VAL_ALL_CONNECTED (Default Value) Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |
|  | Note Each PXI_Star and PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Your chassis documentation may describe this mapping in addition to the chassis.ini and pxisys.ini system description files the PXI Specification requires. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_enablegpstimestamping.html language=enus -->
## TOPIC 00136: niSync_EnableGPSTimestamping

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_enablegpstimestamping.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_enablegpstimestamping.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_EnableGPSTimestamping

#### C Function Prototype

ViStatus _VI_FUNC niSync_EnableGPSTimestamping (ViSession vi);

#### Purpose

Enables timestamping of the GPS pulse per second signal. You must select GPS as the time reference for the module specified in the **ViSession** attribute for this instance to function.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_enableirigtimestamping.html language=enus -->
## TOPIC 00137: niSync_EnableIRIGTimestamping

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_enableirigtimestamping.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_enableirigtimestamping.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_EnableIRIGTimestamping

#### C Function Prototype

ViStatus _VI_FUNC niSync_EnableIRIGTimestamping (ViSession vi, ViInt32 irigType, ViConstString terminalName);

#### Purpose

Enables timestamping of IRIG decodes synchronized to the board time associated with the specified instrument handle. The terminal associated with this timestamp cannot be used for other operations until timestamping is disabled with [niSync_DisableIRIGTimestamping](nisync_disableirigtimestamping.html) or the session is closed with [niSync_close](nisync_close.html).

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| irigType | ViInt32 | This attribute specifies the type of IRIG output generated by the external IRIG source. Valid Values: NISYNC_VAL_IRIG_TYPE_IRIGB_DC NISYNC_VAL_IRIG_TYPE_IRIGB_AM |
| activeItem | viConstString | This attribute specifies the terminal that contains the external IRIG source you would like to timestamp. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_enabletimestamptrigger.html language=enus -->
## TOPIC 00138: niSync_EnableTimeStampTrigger

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_enabletimestamptrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_enabletimestamptrigger.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_EnableTimeStampTrigger

#### C Function Prototype

ViStatus _VI_FUNC niSync_EnableTimeStampTrigger (ViSession vi, ViConstString terminal, ViInt32 activeEdge);

#### Purpose

Creates a timestamp every time the signal of the specified trigger or clock changes. You can then read a single timestamp or multiple timestamps at a later point in the data flow.

You cannot use the input terminal specified in this function for other operations until you disable the timestamp trigger using [niSync_DisableTimeStampTrigger](nisync_disabletimestamptrigger.html) or close the session with [niSync_close](nisync_close.html). You can create timestamps for triggers, future time events, clocks created using [niSync_CreateClock, and external devices.](nisync_createclock.html)

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the terminal that contains the trigger signal you would like to timestamp. |
| activeEdge | ViInt32 | Specifies at what point in the trigger signal to record a timestamp in the software buffer.Valid Values:NISYNC_VAL_EDGE_RISINGNISYNC_VAL_EDGE_FALLINGNISYNC_VAL_EDGE_ANY |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_enabletimestamptriggerwithdecimation.html language=enus -->
## TOPIC 00139: niSync_EnableTimeStampTriggerWithDecimation

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_enabletimestamptriggerwithdecimation.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_enabletimestamptriggerwithdecimation.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_EnableTimeStampTriggerWithDecimation

#### C Function Prototype

ViStatus _VI_FUNC niSync_EnableTimeStampTriggerWithDecimation (ViSession vi, ViConstString terminal, ViInt32 activeEdge, ViUInt32 decimationCount);

#### Purpose

Creates a timestamp every time the signal of the specified trigger or clock changes. You can then read a single timestamp or multiple timestamps at a later point in the data flow. With this function, incoming trigger events are decimated by a value of one or more.

The terminal associated with this time stamp trigger cannot be used for other operations until the time stamp trigger is disabled with the [niSync_DisableTimeStampTrigger](nisync_disabletimestamptrigger.html) function or the session is closed with the [niSync_close](nisync_close.html) function.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the terminal that contains the trigger signal you would like to timestamp. |
| activeEdge | ViInt32 | Specifies at what point in the trigger signal to record a timestamp in the software buffer.Valid Values:NISYNC_VAL_EDGE_RISINGNISYNC_VAL_EDGE_FALLINGNISYNC_VAL_EDGE_ANY |
| decimationCount | ViUint32 | Specifies by how much to decimate incoming trigger events. Use this parameter to adjust the number of timestamps that should elapse before the next timestamp is recorded. For example, if you set the decimationCount to 10, the function will record every tenth timestamp. The value must be greater than or equal to one, and the default value is one. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_error_message.html language=enus -->
## TOPIC 00140: niSync_error_message

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_error_message.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_error_message.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_error_message

#### C Function Prototype

ViStatus niSync_error_message (ViSession vi, ViStatus errorCode, ViChar[] errorMessage);

#### Purpose

Converts an error or warning code returned by an NI-Sync driver function into a user-readable string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session.You can pass VI_NULL for this parameter. This is useful when one of the initialize functions fail. |
| errorCode | ViStatus | The error code to be explained in a user-readable string. Pass the Status parameter that is returned from any of the instrument driver functions to use this parameter. Default Value: 0 (VI_SUCCESS) |
| errorMessage | ViChar[] | Returns a user-readable message string. This string explains the error code specified in errorCode. You must pass a ViChar array at least 256 bytes in size. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getattributeviboolean.html language=enus -->
## TOPIC 00141: niSync_GetAttributeViBoolean

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getattributeviboolean.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getattributeviboolean.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetAttributeViBoolean

#### C Function Prototype

ViStatus niSync_GetAttributeViBoolean (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViBoolean* attributeValue);

#### Purpose

Queries the value of a ViBoolean attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | Ignored for most attributes. For those attributes that are specific to a given terminal, you must specify the terminal name, for example, NISYNC_VAL_PFI0. |
| attributeID | ViAttr | Specifies the ID of the attribute you want to get. |
| attributeValue | ViBoolean | Specifies the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current settings of the instrument session. Default Value: none |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getattributeviint32.html language=enus -->
## TOPIC 00142: niSync_GetAttributeViInt32

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getattributeviint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getattributeviint32.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetAttributeViInt32

#### C Function Prototype

ViStatus niSync_GetAttributeViInt32 (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViInt32* attributeValue);

#### Purpose

Queries the value of a ViInt32 attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | Ignored for most attributes. For those attributes that are specific to a given terminal, you must specify the terminal name, for example, NISYNC_VAL_PFI0. |
| attributeID | ViAttr | Specifies the ID of the attribute you want to get. |
| attributeValue | ViInt32 | Returns the current value of the attribute. Pass the address of a ViInt32 variable. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getattributevireal64.html language=enus -->
## TOPIC 00143: niSync_GetAttributeViReal64

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getattributevireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getattributevireal64.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetAttributeViReal64

#### C Function Prototype

ViStatus niSync_GetAttributeViReal64 (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViReal64* attributeValue);

#### Purpose

Queries the value of a ViReal64 attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | Ignored for most attributes. For those attributes that are specific to a given terminal, you must specify the terminal name, for example, NISYNC_VAL_PFI0. |
| attributeID | ViAttr | Specifies the ID of the attribute you want to get. |
| attributeValue | ViReal64 | Returns the current value of the attribute. Pass the address of a ViReal64 variable. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getattributevistring.html language=enus -->
## TOPIC 00144: niSync_GetAttributeViString

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getattributevistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getattributevistring.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetAttributeViString

#### C Function Prototype

ViStatus niSync_GetAttributeViString (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViInt32 bufferSize, ViChar[] attributeValue);

#### Purpose

Queries the value of a ViString attribute.

You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufferSize** parameter. If the current value of the attribute, including the terminating NUL byte, is larger than the size you indicate in the **bufferSize** parameter, the function copies buffer size – 1 bytes into the buffer, places an ASCII NUL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.
 

 
If you want to call this function just to get the required buffer size, you can pass 0 for **bufferSize** and VI_NULL for the **attributeValue** parameter.
 

 
If you want the function to fill in the buffer regardless of the number of bytes in the value, pass a negative number for the **bufferSize** parameter.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | Ignored for most attributes. For those attributes that are specific to a given terminal, you must specify the terminal name (for example, NISYNC_VAL_PFI0). |
| attributeID | ViAttr | Specifies the ID of the attribute you want to get. |
| bufferSize | ViInt32 | Specifies the number of bytes in the ViChar array you specify for attributeValue. If the current value of the attribute, including the terminating NUL byte, contains more bytes than you indicate in this parameter, the function copies buffer size – 1 bytes into the buffer, places an ASCII NUL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you pass a negative number, the function copies the value to the buffer regardless of the number of bytes in the value. If you pass 0, you can pass VI_NULL for the attributeValue buffer parameter. Default Value: 256 |
| attributeValue | ViChar[] | Returns the current value of the attribute. This buffer must be of type ViChar and have at least as many bytes as indicated in bufferSize. If the current value of the attribute, including the terminating NUL byte, contains more bytes than you indicate in this parameter, the function copies buffer size – 1 bytes into the buffer, places an ASCII NUL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you specify 0 for the bufferSize parameter, you can pass VI_NULL for this parameter. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getextcallastdateandtime.html language=enus -->
## TOPIC 00145: niSync_GetExtCalLastDateAndTime

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getextcallastdateandtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getextcallastdateandtime.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetExtCalLastDateAndTime

#### C Function Prototype

ViStatus niSync_GetExtCalLastDateAndTime (ViSession vi, ViInt32* year, ViInt32* month, ViInt32* day, ViInt32* hour, ViInt32* minute);

#### Purpose

Returns the date and time, in Greenwich Mean Time (GMT), of the specified device's last external calibration session. Use this function to determine if your device needs external calibration or plan ahead for a future external calibration session.

|  | Note You do not need to enter a calibration password to use this function. You can invoke this function with an instrument handle created with either niSync_init or niSync_InitExtCal.The date and time returned by this function updates every time you invoke niSync_CloseExtCal with the action parameter set to Commit, even if no calibration constants were changed. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | This parameter specifies the session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session.Default Value: None |
| year | ViInt32 | The year of the module's last external calibration session. |
| month | ViInt32 | The month of the module's last external calibration session. Valid Values: ValueMonth 1 January 2 February 3 March 4 April 5 May 6 June 7 July 8 August 9 September 10 October 11 November 12 December |
| Value | Month |  |
| 1 | January |  |
| 2 | February |  |
| 3 | March |  |
| 4 | April |  |
| 5 | May |  |
| 6 | June |  |
| 7 | July |  |
| 8 | August |  |
| 9 | September |  |
| 10 | October |  |
| 11 | November |  |
| 12 | December |  |
| day | ViInt32 | The day of the month when the module was last externally calibrated. |
| hour | ViInt32 | The hour, in GMT, of the module's last external calibration session. Valid Values: ValueHour (GMT) 0Midnight 11:00 a.m. 22:00 a.m. 33:00 a.m. 44:00 a.m. 55:00 a.m. 66:00 a.m. 77:00 a.m. 88:00 a.m. 99:00 a.m. 1010:00 a.m. 1111:00 a.m. 12Noon 131:00 p.m. 142:00 p.m. 153:00 p.m. 164:00 p.m. 175:00 p.m. 186:00 p.m. 197:00 p.m. 208:00 p.m. 219:00 p.m. 2210:00 p.m. 2311:00 p.m. |
| Value | Hour (GMT) |  |
| 0 | Midnight |  |
| 1 | 1:00 a.m. |  |
| 2 | 2:00 a.m. |  |
| 3 | 3:00 a.m. |  |
| 4 | 4:00 a.m. |  |
| 5 | 5:00 a.m. |  |
| 6 | 6:00 a.m. |  |
| 7 | 7:00 a.m. |  |
| 8 | 8:00 a.m. |  |
| 9 | 9:00 a.m. |  |
| 10 | 10:00 a.m. |  |
| 11 | 11:00 a.m. |  |
| 12 | Noon |  |
| 13 | 1:00 p.m. |  |
| 14 | 2:00 p.m. |  |
| 15 | 3:00 p.m. |  |
| 16 | 4:00 p.m. |  |
| 17 | 5:00 p.m. |  |
| 18 | 6:00 p.m. |  |
| 19 | 7:00 p.m. |  |
| 20 | 8:00 p.m. |  |
| 21 | 9:00 p.m. |  |
| 22 | 10:00 p.m. |  |
| 23 | 11:00 p.m. |  |
| minute | ViInt32 | The minute, in GMT, of the module's last external calibration session. Valid Values: 0-59 |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getextcallasttemp.html language=enus -->
## TOPIC 00146: niSync_GetExtCalLastTemp

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getextcallasttemp.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getextcallasttemp.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetExtCalLastTemp

#### C Function Prototype

ViStatus niSync_GetExtCalLastTemp (ViSession vi, ViReal64* temperature);

#### Purpose

Returns the temperature, in degrees Celsius, of the specified module's circuitry during its last external calibration session.

Use this function in conjunction with [niSync_ReadCurrentTemperature](nisync_readcurrenttemperature.html) to determine if the device is running at a temperature comparable to when it was last calibrated.

|  | Note You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either niSync_init or niSync_InitExtCal. This function does not return the ambient temperature of the module. The temperature of the circuitry is generally higher than the ambient temperature. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | This parameter specifies the session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session.Default Value: None |
| temperature | ViReal64 | The temperature, in degrees Celsius, of the device's circuitry during its last external calibration session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getextcalrecommendedinterval.html language=enus -->
## TOPIC 00147: niSync_GetExtCalRecommendedInterval

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getextcalrecommendedinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getextcalrecommendedinterval.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetExtCalRecommendedInterval

#### C Function Prototype

ViStatus niSync_GetExtCalRecommendedInterval (ViSession vi, ViInt32* months);

#### Purpose

Returns the number of months recommended between external calibration sessions for the device.

You can use this function in conjunction with other external calibration functions to determine the next time to run the device through an external calibration session.

|  | Note You do not need a calibration password to use this function. It can be invoked with an instrument handle created with either niSync_init or niSync_InitExtCal. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session.Default Value: None |
| months | ViInt32 | The recommended external calibration interval, in months, for the specified module. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getlocation.html language=enus -->
## TOPIC 00148: niSync_GetLocation

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getlocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getlocation.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetLocation

#### C Function Prototype

ViStatus _VI_FUNC niSync_GetLocation (ViSession vi, ViReal64 * latitude, ViReal64 * longitude, ViReal64 * altitude);

#### Purpose

Returns the last calculated latitude, longitude, and altitude of the device's onboard GPS receiver.

|  | Note You must connect an external GPS antenna to the device and set the device's external time reference to GPS in order to receive valid data from this function. For best results, allow the GPS receiver to compete a self survey before reading the location.This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| latitude | ViReal64 * | The current latitude, in degrees, of the connected device's GPS receiver. Negative values represent southern latitude. Positive values represent northern latitude. This parameter is an input double pointer; the caller of this function must allocate a ViReal64 and pass the pointer in this argument. |
| longitude | ViReal64 * | The current longitude, in degrees, of the connected device's GPS receiver. Negative values represent western longitude. Positive values represent eastern longitude. This parameter is an input double pointer; the caller of this function must allocate a ViReal64 and pass the pointer in this argument. |
| altitude | ViReal64 * | The current altitude, in meters, of the connected device's GPS receiver using the WGS-84 earth ellipsoid standard. This parameter is an input double pointer; the caller of this function must allocate a ViReal64 and pass the pointer in this argument. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_gettime.html language=enus -->
## TOPIC 00149: niSync_GetTime

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_gettime.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_gettime.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_GetTime

### niSync_GetTime

#### C Function Prototype

ViStatus _VI_FUNC niSync_GetTime (ViSession vi, ViUInt32* timeSeconds, ViUInt32* timeNanoseconds, ViUInt16* timeFractionalNanoseconds);

#### Purpose

Returns the current board time of the specified device.

|  | Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, if the supported time range has ended, an error is returned. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| timeSeconds | ViUInt32* | The seconds portion of the board time. |
| timeNanoseconds | ViUInt32* | The nanoseconds portion of the board time. |
| timeFractionalNanoseconds | ViUInt16* | The fractional nanoseconds portion of the board time. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_gettimereferencenames.html language=enus -->
## TOPIC 00150: niSync_GetTimeReferenceNames

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_gettimereferencenames.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_gettimereferencenames.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetTimeReferenceNames

#### Purpose

Returns an array of installed time references

This function returns both enabled and disabled time references for the device. Use the [NISYNC_ATTR_TIMEREF_ENABLED](nisync_attr_timeref_enabled.html) attribute to return whether or not a time reference is enabled.

|  | Note This function is supported only on Linux RT targets. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| bufferSize | ViUInt32 | Specifies the size of the buffer. |
| timeReferenceNames | ViChar | Returns a list of installed time references. |

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_getvelocity.html language=enus -->
## TOPIC 00151: niSync_GetVelocity

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_getvelocity.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_getvelocity.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_GetVelocity

#### C Function Prototype

ViStatus _VI_FUNC niSync_GetVelocity (ViSession vi, ViReal64 * eastVelocity, ViReal64 * northVelocity, ViReal64 * upVelocity);

#### Purpose

Returns the last calculated velocity of the onboard GPS receiver. The function returns east velocity, north velocity, and up velocity in meters per second.

|  | Note You must connect an external GPS antenna to your device to receive valid data from this function, and you must enable Mobile Mode on the device to receive non-zero velocity values. You can enable Mobile Mode using Measurement & Automation Explorer (MAX) or by calling the NISYNC_ATTR_GPS_MOBILE_MODE attribute.This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| eastVelocity | ViReal64 * | An input double pointer. The caller of this function must allocate a ViReal64 and pass the pointer in this argument. This parameter returns current east velocity, in meters per second, of the device. Negative values represent how fast the device is traveling west. Positive values represent how fast the device is traveling east. |
| northVelocity | ViReal64 * | An input double pointer. The caller of this function must allocate a ViReal64 and pass the pointer in this argument. The parameter returns the current north velocity, in meters per second, of the device. Negative values represent how fast the device is traveling south. Positive values represent how fast the device is traveling north. |
| upVelocity | ViReal64 * | An input double pointer. The caller of this function must allocate a ViReal64 and pass the pointer in this argument. This parameter returns the current up velocity, in meters per second, of your device. Negative values represent how fast your device is traveling down. Positive values represent how fast your device is traveling up. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_init.html language=enus -->
## TOPIC 00152: niSync_init

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_init.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_init.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_init

#### C Function Prototype

ViStatus niSync_init (ViRsrc resourceName, ViBoolean idQuery, ViBoolean resetDevice, ViSession* vi);

#### Purpose

Creates a new NI-Sync instrument driver session.

You must call this function any time you want to use NI-Sync functions, and you must open a separate section for each device. You can use the instrument handle returned from this function to identify the device to other NI-Sync functions, including NI-Sync external calibration functions.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | ViConstString | The resource name of the module to initialize. You can assign the resource name of a device in Measurement & Automation Explorer (MAX). PXI and DAQ Syntax PXI[bus number]::device number NI-DAQmx name Optional fields are shown in square brackets ([]). Note VISA aliases are also valid for the resource name. Example resource names: Resource Name Description Dev1 DAQmx name pxi1slot5 DAQmx name PXI0::15::INSTR PXI bus 0, device number 15 PXI::15::INSTR PXI bus 0, device number 15 PXI4::9::INSTR PXI bus 4, device number 9 |
|  | Note VISA aliases are also valid for the resource name. |  |
| Resource Name | Description |  |
| Dev1 | DAQmx name |  |
| pxi1slot5 | DAQmx name |  |
| PXI0::15::INSTR | PXI bus 0, device number 15 |  |
| PXI::15::INSTR | PXI bus 0, device number 15 |  |
| PXI4::9::INSTR | PXI bus 4, device number 9 |  |
| idQuery | ViBoolean | This parameter is ignored. Because NI-Sync supports multiple NI-Sync modules, it always queries the device to determine which device is installed. Valid Values: TRUE—Query the device (Default Value) FALSE—Do not query the device |
| resetDevice | ViBoolean | Resets the NI-Sync module during the initialization procedure. Valid Range: TRUE (1)—Reset Device FALSE (0)—Don't Reset (Default Value) |
| vi | ViSession | Returns a ViSession handle that you use to identify the instrument in all subsequent instrument driver function calls. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_initextcal.html language=enus -->
## TOPIC 00153: niSync_InitExtCal

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_initextcal.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_initextcal.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_InitExtCal

#### C Function Prototype

ViStatus niSync_InitExtCal (ViRsrc resourceName, ViConstString password, ViSession* calibrationInstrumentHandle);

#### Purpose

Begins an external calibration session for the specified device. The function returns an instrument driver session handle that can be used to adjust calibration constants for the module or read current calibration constants stored in the device's non-volatile memory.

You must close the external calibration session using [niSync_CloseExtCal](nisync_closeextcal.html).

|  | Note You must supply the external calibration password for the module for the operation to succeed. Refer to your device's calibration documentation for the default external calibration password. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | ViRsrc | Resource name of the module to initialize. The resource name is assigned in Measurement & Automation Explorer (MAX). Syntax: PXI[bus number]::device number NI-DAQmx name Optional fields are shown in square brackets ([]). Note VISA aliases are also valid for the resource name. Example resource names: Resource Name Description Dev1 DAQmx name PXI1Slot5 DAQmx name PXI0::15::INSTR PXI bus 0, device number 15 PXI::15::INSTR PXI bus 0, device number 15 PXI4::9::INSTR PXI bus 4, device number 9 |
|  | Note VISA aliases are also valid for the resource name. |  |
| Resource Name | Description |  |
| Dev1 | DAQmx name |  |
| PXI1Slot5 | DAQmx name |  |
| PXI0::15::INSTR | PXI bus 0, device number 15 |  |
| PXI::15::INSTR | PXI bus 0, device number 15 |  |
| PXI4::9::INSTR | PXI bus 4, device number 9 |  |
| password | ViConstString | Specifies the external calibration password for the module.You must enter the correct case-sensitive password exactly as it is stored in the device's EEPROM to begin an external calibration session. Note You can change the external calibration password using niSync_ChangeExtCalPassword. Default Value: "" |
|  | Note You can change the external calibration password using niSync_ChangeExtCalPassword. |  |
| calibrationInstrumentHandle | ViSession | Returns an instrument handle that you use to identify the instrument in all subsequent instrument driver function calls. Note Although you can create more than one NI-Sync session for the same resource, it is best not to do so. A better approach is to use the same NI-Sync session in multiple execution threads. You can use VISA functions viLock and viUnlock to protect sections of code that require exclusive access to the resource. |
|  | Note Although you can create more than one NI-Sync session for the same resource, it is best not to do so. A better approach is to use the same NI-Sync session in multiple execution threads. You can use VISA functions viLock and viUnlock to protect sections of code that require exclusive access to the resource. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_measurefrequency.html language=enus -->
## TOPIC 00154: niSync_MeasureFrequency

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_measurefrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_measurefrequency.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_MeasureFrequency

#### C Function Prototype

ViStatus niSync_MeasureFrequency (ViSession vi, ViConstString sourceTerminal, ViReal64 duration, ViReal64* actualDuration, ViReal64* measuredFrequency, ViReal64* error);

#### Purpose

Measures the frequency of the signal at the specified terminal for a specified duration. The terminal you specify with **sourceTerminal** must contain a digital signal for the function to operate.

#### niSync_MeasureFrequency Details

##### Using niSync_MeasureFrequency with Time-Based Devices

The following time-based timing and synchronization devices are compatible with Measure Frequency:

- PXI-6683
- PXI-6683H
- PXI-6682
- PXI-6682H

When using niSync_MeasureFrequency with a PXI-6683(H) or other time-based device, timestamping is used to measure the frequency. The function will measure timestamps until you have acquired timestamps that have an **actualDuration** greater than or equal to the specified **duration**. If timestamps are not detected or not enough timestamps are detected due to a slow signal or a **decimationCount** that is too high, the function may encounter an error. Generally, you should have a timestamp within every second to avoid this error.

|  | Note The maximum signal you can measure using this function is 22.7 MHz. |
| --- | --- |

The **decimationCount** parameter is only necessary on PXI-6683(H) and other time-based devices. In order to set the **decimationCount** accurately, you should have a general idea of what range (Hz, kHz, MHz) the signal to be measured occupies.

Only PFI and PXI_Trig lines can be used as the **sourceTerminal** on time-based devices.

For the most accurate measurement, the board clock for the time-based device you are trying to measure should be set to free running. If you are synchronizing to GPS, IRIG, or a PTP protocol like 1588, the function may encounter an error or the result may be unreliable.

##### Troubleshooting the Software Buffer Overflow Error

When you are measuring frequency with this function using a time-based device, you may encounter a software buffer overflow error. This means that there is not enough memory to store the recorded timestamps when measuring frequency. You can take one or more of the following actions to resolve a software buffer overflow error:

- Set a higher value in the decimationCount parameter.
- Increase the timestamp buffer size using the NISYNC_ATTR_1588_TIMESTAMP_BUF_SIZE attribute.

##### Using Measure Frequency with Signal-Based Devices

The following signal-based timing and synchronization devices are compatible with Measure Frequency:

- PXI-6652 (PFI0 only)
- PXI-6653 (PFI0 only)
- PXIe-6672 (PFI0 only)
- PXIe-6674T

Using a signal-based device and niSync_MeasureFrequency, you can measure the frequency of the device's oscillator, an external clock connected to a front panel input, or a full speed or divided synchronization clock.

When measuring the frequency on a signal-based device, you must set the **duration** in multiples of 100 nanoseconds, i.e. a multiple of the PXI_Clk10 period. If the **duration** is not a multiple of the PXI_Clk10 period, it will be coerced to the closest multiple and returned in the **actualDuration** parameter.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | This input specifies the source terminal of the signal to measure. Valid Values: NISYNC_VAL_PFI0 (Default Value) NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_OSCILLATOR NISYNC_VAL_CLKIN |
| duration | ViReal64 | Specifies the length of time, in seconds, to measure the frequency. Set a longer duration to return a more accurate frequency measurement.The duration should be a multiple of the PXI_Clk10 signal period. That is, it should be specified in multiples of 100 ns. If the duration is not a multiple of the PXI_Clk10 period, it will be coerced to the closest multiple. Default Value: 0.00000100 seconds |
| actualDuration | ViReal64 | Returns the actual duration, in seconds, that the function measured the frequency of the signal at the specified terminal.If the value you enter in duration is not a multiple of the PXI_CLK10 period, the actualDuration will be the closest multiple of 100 ns. |
| measuredFrequency | ViReal64 | Returns the frequency, in Hz, measured at the specified terminal. THe measurable frequency range is dependent on the hardware; refer to the hardware's documentation to determine the frequency range of any given terminal. |
| error | ViReal64 | Returns the margin of error calculated for the frequency measurement. The formula used to calculate the error is: error = [ (10M / base_freq) ] / [actual_duration] where base_freq refers to the base frequency and actual_duration refers to the output of the actualDuration parameter. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_persistconfig.html language=enus -->
## TOPIC 00155: niSync_PersistConfig

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_persistconfig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_persistconfig.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_PersistConfig

#### Purpose

Retains modified settings even after the controller is rebooted.

By default, modified NI-Sync settings are reverted to the last saved (persisted) configuration after the controller reboots. Call this function after you have changed settings to keep those settings.

|  | Note This function is supported only on Linux RT targets. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_readcurrenttemperature.html language=enus -->
## TOPIC 00156: niSync_ReadCurrentTemperature

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_readcurrenttemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_readcurrenttemperature.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ReadCurrentTemperature

#### C Function Prototype

ViStatus niSync_ReadCurrentTemperature (ViSession vi, ViReal64* temperature);

#### Purpose

Reads the current temperature, in degrees Celsius, of the specified device's circuitry.

Use this function to determine if the device is in a properly cooled location or if it needs external calibration.

|  | Note You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either niSync_init or niSync_InitExtCal. This function does not return the ambient temperature of the device. The temperature of the circuitry is generally higher than the ambient temperature. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | Specifies the session handle that you obtain from niSync_init or niSync_InitExtCal. The handle identifies a particular instrument session.Default Value: None |
| temperature | ViReal64 | Returns the temperature, in degrees Celsius, of the specified device's circuitry. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_readlastgpstimestamp.html language=enus -->
## TOPIC 00157: niSync_ReadLastGPSTimestamp

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_readlastgpstimestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_readlastgpstimestamp.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_ReadLastGPSTimestamp

### niSync_ReadLastGPSTimestamp

#### C Function Prototype

ViStatus _VI_FUNC niSync_ReadLastGPSTimestamp (ViSession vi, ViUInt32 * timestampSeconds, ViUInt32 * timestampNanoseconds, ViUInt16 * timestampFractionalNanoseconds, ViUInt32 * gpsSeconds, ViUInt32 * gpsNanoseconds, ViUInt16 * gpsFractionalNanoseconds);

#### Purpose

Returns two timestamps: one with the module's board time when the module received the GPS pulse per second signal, and the other with the time of the onboard GPS receiver. Use these two values to determine the delay between GPS and your module.

The read operation is a single-timestamp, nonblocking read. That is, the newest timestamp is returned. If no valid timestamp has ever been received, a value of zero is returned for the timestamp and the decoded time. A single timestamp can be read multiple times; only the reception of a subsequent timestamp updates the values returned. The function does not block waiting for a new timestamp to become available.

Prior to calling niSync_ReadLastGPSTimestamp, you must enable GPS timestamping by calling [niSync_EnableGPSTimestamping](nisync_enablegpstimestamping.html).

|  | Note You can combine the values returned in timestampSeconds, timestampNanoseconds, and timestampFractionalNanoseconds to get the board time the GPS pulse per second was received. You can combine the values returned in gpsSeconds, gpsNanoseconds, and gpsFractionalNanoseconds to get the time reported by the onboard GPS receiver. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| timestampSeconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the seconds field of when the timestamp occurred. |
| timestampNanoseconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the nanoseconds field of when the timestamp occurred. |
| timestampFractionalNanoseconds | ViUInt16 * | An input integer pointer. The caller of this function must allocate a ViUInt16 and pass the pointer in this argument. The function sets the ViUInt16 value to the fractional nanoseconds field of when the timestamp occurred. |
| gpsSeconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the seconds field of time reported by the onboard GPS receiver. |
| gpsNanoseconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the nanoseconds field of the time reported by the onboard GPS receiver. |
| gpsFractionalNanoseconds | ViUInt16 * | An input integer pointer. The caller of this function must allocate a ViUInt16 and pass the pointer in this argument. The function sets the ViUInt16 value to the fractional nanoseconds field of the time reported by the onboard GPS receiver. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_readlastirigtimestamp.html language=enus -->
## TOPIC 00158: niSync_ReadLastIRIGTimestamp

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_readlastirigtimestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_readlastirigtimestamp.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_ReadLastIRIGTimestamp

### niSync_ReadLastIRIGTimestamp

#### C Function Prototype

ViStatus _VI_FUNC niSync_ReadLastIRIGTimestamp (ViSession vi, ViConstString terminal, ViUInt32 * timestampSeconds, ViUInt32 * timestampNanoseconds, ViUInt16 * timestampFractionalNanoseconds, ViUInt32 * irigbSeconds, ViUInt32 * irigbNanoseconds, ViUInt16 * irigbFractionalNanoseconds);

#### Purpose

Returns two timestamps: one with the board time when the module received the IRIG message, and one with the time encoded in the IRIG message. Use these two values to determine the delay between the external IRIG source and your module, or to test the stability of an external IRIG source against an external time reference.

The read operation is a single-timestamp, nonblocking read. That is, the newest timestamp is returned. If no valid timestamp has ever been received, a value of zero is returned for the timestamp and the decoded time. A single timestamp can be read multiple times; only the reception of a subsequent timestamp will update the values returned. The function does not block waiting for a new timestamp to become available.

Prior to calling niSync_ReadLastIRIGTimestamp, you must enable IRIG timestamping by calling [niSync_EnableIRIGTimestamping](nisync_enableirigtimestamping.html).

|  | Note You can combine the values returned in timestampSeconds, timestampNanoseconds, and timestampFractionalNanoseconds to get the board time the IRIG message was received. You can combine the values returned in irigbSeconds, irigbNanoseconds, and irigbFractionalNanoseconds to get the time reported in the IRIG message. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | viConstString | Specifies the terminal to which the IRIG input is connected. |
| timestampSeconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the seconds field of when the timestamp occurred. |
| timestampNanoseconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the nanoseconds field of when the timestamp occurred. |
| timestampFractionalNanoseconds | ViUInt16 * | An input integer pointer. The caller of this function must allocate a ViUInt16 and pass the pointer in this argument. The function sets the ViUInt16 value to the fractional nanoseconds field of when the timestamp occurred. |
| irigbSeconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the seconds field of time reported in the IRIG message. |
| irigbNanoseconds | ViUInt32 * | An input integer pointer. The caller of this function must allocate a ViUInt32 and pass the pointer in this argument. The function sets the ViUInt32 value to the nanoseconds field of the time reported in the IRIG message. |
| irigbFractionalNanoseconds | ViUInt16 * | An input integer pointer. The caller of this function must allocate a ViUInt16 and pass the pointer in this argument. The function sets the ViUInt16 value to the fractional nanoseconds field of the time reported in the IRIG message. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_readmultipletriggertimestamp.html language=enus -->
## TOPIC 00159: niSync_ReadMultipleTriggertimestamp

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_readmultipletriggertimestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_readmultipletriggertimestamp.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ReadMultipleTriggertimestamp

#### C Function Prototype

ViStatus _VI_FUNC niSync_ReadMultipleTriggertimestamp (ViSession vi, ViConstString terminal, ViUInt32 timestampsToRead, ViReal64 timeout, ViUInt32 * timeSecondsBuffer, ViUInt32 * timeNanosecondsBuffer, ViUInt16 * timeFractionalNanosecondsBuffer, ViInt32 * detectedEdgeBuffer, ViUInt32 * timestampsRead);

#### Purpose

Reads trigger timestamps from the internal software buffer for the specified terminal. The read operation is a destructive, blocking read. That is, the oldest unread timestamp associated with the specified terminal is returned. When a timestamp is read, it is removed from the buffer. The function does not return until the timestamps requested are available to be read, or the specified timeout elapses.

#### Troubleshooting a Full Buffer

If the internal software buffer associated with the specified terminal is full, timestamp operations for that terminal are suspended and an error specifying that the internal software buffer has overflowed is returned.

If the hardware timestamp buffer is full, all trigger timestamp operations are suspended and an error specifying that the hardware timestamp buffer has overflowed is returned. niSync_ReadMultipleTriggertimestamp continues to return previously generated timestamps, despite the overflow condition, until no timestamps are available.

To clear this error condition, you must invoke [niSync_DisabletimestampTrigger](nisync_disabletimestamptrigger.html) or expand the size of the timestamp buffer using the [NISYNC_ATTR_1588_TIMESTAMP_BUF_SIZE](nisync_attr_1588_timestamp_buf_size.html) attribute.

|  | Note If timestampsToRead is not equal to timestampsRead, the data held in the output arrays from index timestampsRead to the end of the arrays is uninitialized, and should be considered invalid. NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, if the supported time range ends before a timestamp is captured, an error is returned. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | viConstString | Specifies the terminal that contains the the trigger signal you would like to read timestamps from. |
| timestampsToRead | ViUInt32 | Specifies the number of timestamps to read. If the number of timestamps is not available before the timeout elapses, the number read before the timeout occurred is returned. |
| timeout | ViReal64 | Specifies the time to wait, in seconds, for a timestamp to be generated. If the function can't find any timestamps to read on the specified terminal, it returns a timeout error and stops the program. The default value is 10 seconds. |
| timeSecondsBuffer | ViUInt32 * | An input pointer to an array of ViUInt32 values. The caller of this function must allocate an array of ViUInt32s of size timestampsToRead and pass the pointer to the array in this argument. The function sets the values of the ViUInt32s to the seconds field of when the timestamp occurred. After the function returns, index 0 holds the earliest occurring seconds value, and the value returned in timestampsRead, minus one, is the index in which the latest occurring seconds value is stored. |
| timeNanosecondsBuffer | ViUInt32 * | An input pointer to an array of ViUInt32 values. The caller of this function must allocate an array of ViUInt32s of size timestampsToRead and pass the pointer to the array in this argument. The function sets the values of the ViUInt32s to the nanoseconds field of when the time stamp occurred. After the function returns, index 0 holds the earliest occurring nanoseconds value, and the value returned in timestampsRead, minus one, is the index in which the latest occurring nanoseconds value is stored. |
| timeFractionalNanosecondsBuffer | ViUInt16 * | An input pointer to an array of ViUInt16 values. The caller of this function must allocate an array of ViUInt16s of size timestampsToRead and pass the pointer to the array in this argument. The function sets the values of the ViUInt16s to the fractional nanoseconds field of when the time stamp occurred. After the function returns, index 0 holds the earliest occurring fractional nanoseconds value, and the value returned in timestampsRead, minus one, is the index in which the latest occurring fractional nanoseconds value is stored. |
| detectedEdgeBuffer | ViInt32 * | An input pointer to an array of ViInt32s. The caller of this function must allocate an array of ViUInt32s of size timestampsToRead and pass the pointer to the array in this argument. After the function returns, index 0 holds the earliest occurring detectedEdge value, and the value returned in timestampsRead, minus one, is the index in which the latest occurring detectedEdge value is stored. Each detectedEdge is an integer enumeration that specifies the detected trigger condition. Valid Values: NISYNC_VAL_EDGE_RISING NISYNC_VAL_EDGE_FALLING |
| timestampsRead | ViUInt32 * | An input pointer to a ViUInt32. The caller of this function must allocate a ViUInt32 and pass the pointer to the array in this argument. When the function returns, the value at this pointer is set to the number of actual time stamps read. This value may be different than timestampsToRead if a timeout or other error occurs while reading time stamps. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_readtriggertimestamp.html language=enus -->
## TOPIC 00160: niSync_ReadTriggerTimeStamp

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_readtriggertimestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_readtriggertimestamp.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_ReadTriggerTimeStamp

### niSync_ReadTriggerTimeStamp

#### C Function Prototype

ViStatus _VI_FUNC niSync_ReadTriggerTimeStamp (ViSession vi, ViConstString terminal, ViReal64 timeout, ViUInt32* timeSeconds, ViUInt32* timeNanoseconds, ViUInt16* timeFractionalNanoseconds, ViInt32* detectedEdge);

#### Purpose

Reads a timestamp recorded on the internal software buffer for a specific terminal.

The read operation is a single-time-stamp, destructive, blocking read. That is, the oldest unread time stamp associated with the specified terminal is returned. When a time stamp is read, it is removed from the buffer. The function does not return until a time stamp is available to be read or the specified timeout elapses.

|  | Note NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, if the supported time range ends before a time stamp is captured, an error is returned. |
| --- | --- |

#### Details

If the internal software buffer associated with the specified terminal is full, timestamp operations for that terminal are suspended and an error, specifying that the internal software buffer overflowed, is returned when the niSync_ReadTriggerTimeStamp function is invoked. If the hardware timestamp buffer is full, all trigger timestamp operations are suspended and an error, specifying that the hardware timestamp buffer overflowed, is returned when the niSync_ReadTriggerTimeStamp function is invoked. That is, the niSync_ReadTriggerTimeStamp function continues to return previously generated timestamps, despite the overflow condition, until no time stamps are available. To clear this error condition, you must invoke the [niSync_DisableTimeStampTrigger](nisync_disabletimestamptrigger.html) function .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminal | ViConstString | Specifies the terminal that contains the digital signal you want to read timestamps from. |
| timeout | ViReal64 | An input floating-point number that specifies the number of seconds to wait for a timestamp to be generated before returning a timeout error.Default Value: 10 seconds |
| timeSeconds | ViUInt32* | An output integer that returns a portion of the board time when the trigger associated with the specified terminal was detected. |
| timeNanoseconds | ViUInt32* | An output integer that returns a portion of the board time when the trigger associated with the specified terminal was detected. |
| timeFractionalNanoseconds | ViUInt16* | An output integer that returns a portion of the board time when the trigger associated with the specified terminal was detected. |
| detectedEdge | ViInt32* | An output integer enumeration that returns the detected trigger condition of the timestamp.Valid Values:NISYNC_VAL_EDGE_RISINGNISYNC_VAL_EDGE_FALLING |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_reset.html language=enus -->
## TOPIC 00161: niSync_reset

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_reset.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_reset

#### C Function Prototype

ViStatus niSync_reset (ViSession vi);

#### Purpose

Resets the specified device to the state specified below. You can also reset a device before the program starts by using the **resetDevice** parameter of [niSync_init](nisync_init.html).

When you invoke niSync_reset, it executes the following actions:

- Disconnects all terminal connections
- Sets the DDS frequency to 0 Hz.
- Sets all PFI front panel terminals to 50 ohm input impedance.
- Sets the front and rear zone synchronization clock sources to PXI_Clk10.

For time-based timing and synchronization modules, calling this function also executes the following actions:

- Stops PTP participation.
- Resets the 1588 clock to the current system time.
- Clears all clocks.
- Clears all hardware and software triggers.
- Clears all future time events.
- Disables timestamp triggers.
- Sets the selected time reference to the default.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_resetfrequency.html language=enus -->
## TOPIC 00162: niSync_ResetFrequency

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_resetfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_resetfrequency.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_ResetFrequency

#### C Function Prototype

ViStatus _VI_FUNC niSync_ResetFrequency (ViSession vi);

#### Purpose

Resets the internal frequency at which the board time increments to the default value.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_revision_query.html language=enus -->
## TOPIC 00163: niSync_revision_query

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_revision_query.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_revision_query.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_revision_query

#### C Function Prototype

ViStatus niSync_revision_query (ViSession vi, ViChar[] instrumentDriverRevision, ViChar[] firmwareRevision);

#### Purpose

Returns the revision numbers of the NI-Sync driver and specified device's firmware. You can use this function to confirm that your hardware and software is up to date or compatible with a specific feature.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| instrumentDriverRevision | ViChar[] | Returns the NI-Sync software revision numbers in the form of a string. Note You must pass a ViChar array at least 256 bytes in size. |
|  | Note You must pass a ViChar array at least 256 bytes in size. |  |
| firmwareRevision | ViChar[] | Returns the NI-Sync module firmware revision numbers in the form of a string. Note You must pass a ViChar array at least 256 bytes in size. |
|  | Note You must pass a ViChar array at least 256 bytes in size. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_self_test.html language=enus -->
## TOPIC 00164: niSync_self_test

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_self_test.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_self_test.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_self_test

#### C Function Prototype

ViStatus niSync_self_test (ViSession vi, ViInt16* selfTestResult, ViChar[] selfTestMessage);

#### Purpose

Runs the NI-Sync module's self test routine and returns the test result(s).

|  | Note Currently, this operation does nothing. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| selfTestResult | ViInt16 | This control contains the value returned from the instrument self test: Self-Test Code Description 0 Self-test passed 1 Self-test failed |
| Self-Test Code | Description |  |
| 0 | Self-test passed |  |
| 1 | Self-test failed |  |
| selfTestMessage | ViChar[] | Returns the self-test response string from the instrument. See the device's operation manual for an explanation of the string's contents. Note You must pass a ViChar array at least 256 bytes in size. |
|  | Note You must pass a ViChar array at least 256 bytes in size. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_sendsoftwaretrigger.html language=enus -->
## TOPIC 00165: niSync_SendSoftwareTrigger

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_sendsoftwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_sendsoftwaretrigger.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_SendSoftwareTrigger

#### C Function Prototype

ViStatus niSync_SendSoftwareTrigger (ViSession vi, ViConstString sourceTerminal);

#### Purpose

Sends a pulse on the global software trigger terminal. You must first route the global software trigger to at least one destination terminal using [niSync_ConnectSWTrigToTerminal](nisync_connectswtrigtoterminal.html) for this operation to have any effect.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| sourceTerminal | ViConstString | Specifies the source to send the software trigger from. Valid Values: NISYNC_VAL_SWTRIG_GLOBAL (Default Value) |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_setattributeviboolean.html language=enus -->
## TOPIC 00166: niSync_SetAttributeViBoolean

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_setattributeviboolean.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_setattributeviboolean.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_SetAttributeViBoolean

#### C Function Prototype

ViStatus niSync_SetAttributeViBoolean (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViBoolean attributeValue);

#### Purpose

This function sets the value of a ViBoolean attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | This parameter is ignored for most attributes. For those attributes that are specific to a given item or terminal, the item or terminal's name, for example, NISYNC_VAL_PFI0, must be specified. Default Value: "" |
| attributeID | ViAttr | This parameter specifies the ID of the attribute you want to set. |
| attributeValue | ViBoolean | Pass the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current settings of the instrument session. Default Value: none |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_setattributeviint32.html language=enus -->
## TOPIC 00167: niSync_SetAttributeViInt32

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_setattributeviint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_setattributeviint32.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_SetAttributeViInt32

#### C Function Prototype

ViStatus niSync_SetAttributeViInt32 (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViInt32 attributeValue);

#### Purpose

This function sets the value of a ViInt32 attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | This parameter is ignored for most attributes. For those attributes that are specific to a given item or terminal, the item or terminal's name, for example, NISYNC_VAL_PFI0, must be specified. Default Value: "" |
| attributeID | ViAttr | This parameter specifies the ID of the attribute you want to set. |
| attributeValue | ViInt32 | Pass the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current settings of the instrument session. Default Value: none |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_setattributevireal64.html language=enus -->
## TOPIC 00168: niSync_SetAttributeViReal64

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_setattributevireal64.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_setattributevireal64.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_SetAttributeViReal64

#### C Function Prototype

ViStatus niSync_SetAttributeViReal64 (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViReal64 attributeValue);

#### Purpose

This function sets the value of a ViReal64 attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | This parameter is ignored for most attributes. For those attributes that are specific to a given item or terminal, the item or terminal's name, for example, NISYNC_VAL_PFI0, must be specified. Default Value: "" |
| attributeID | ViAttr | This parameter specifies the ID of the attribute you want to set. |
| attributeValue | ViReal64 | Pass the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current settings of the instrument session. Default Value: none |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_setattributevistring.html language=enus -->
## TOPIC 00169: niSync_SetAttributeViString

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_setattributevistring.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_setattributevistring.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_SetAttributeViString

#### C Function Prototype

ViStatus niSync_SetAttributeViString (ViSession vi, ViConstString terminalName, ViAttr attributeID, ViConstString attributeValue);

#### Purpose

This function sets the value of a ViString attribute.

This instrument driver contains high-level functions that set most of the instrument attributes. It is best to use the high-level driver functions as much as possible. They handle order dependencies and multithread locking for you. In addition, they perform status checking only after setting all of the attributes. In contrast, when you set multiple attributes using the SetAttribute functions, the functions check the instrument status after each call.
 

 
Also, when state caching is enabled, the high-level functions that configure multiple attributes perform instrument I/O only for the attributes whose value you change. Thus, you can safely call the high-level functions without the penalty of redundant instrument I/O.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| activeItem | ViConstString | This parameter is ignored for most attributes. For those attributes that are specific to a given item or terminal, the item or terminal's name, for example, NISYNC_VAL_PFI0, must be specified. Default Value: "" |
| attributeID | ViAttr | This parameter specifies the ID of the attribute you want to set. |
| attributeValue | ViConstString | Pass the value to which you want to set the attribute. Note Some of the values might not be valid depending on the current settings of the instrument session. Default Value: none |
|  | Note Some of the values might not be valid depending on the current settings of the instrument session. |  |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_settime.html language=enus -->
## TOPIC 00170: niSync_SetTime

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_settime.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_settime.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_SetTime

### niSync_SetTime

#### C Function Prototype

ViStatus _VI_FUNC niSync_SetTime (ViSession vi, ViInt32 timeSource, ViUInt32 timeSeconds, ViUInt32 timeNanoseconds, ViUInt16 timeFractionalNanoseconds);

#### Purpose

Sets the absolute board time of the specified device to a certain time. You can set the device to a specific time or to the system time of your OS. This function does not change the frequency at which the board time increments; use [niSync_ResetFrequency](nisync_resetfrequency.html) to reset the board time increment frequency.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| timeSource | ViInt32 | Specifies the time source for the board time. Valid Values: NISYNC_VAL_INIT_TIME_SRC_SYSTEM_CLK NISYNC_VAL_INIT_TIME_SRC_MANUAL |
| timeSeconds | ViUInt32 | Specifies the seconds portion of the time to which the board time will be set. Note that NI-Sync supports setting the initial time between 0 hours on 1 January 1970 and 0 hours on 1 January 2100. This parameter is ignored unless the timeSource parameter is set to NISYNC_VAL_INIT_TIME_SRC_MANUAL. |
| timeNanoseconds | ViUInt32 | Specifies the nanoseconds portion of the time to which the board time will be set. Note that NI-Sync supports setting the initial time between 0 hours on 1 January 1970 and 0 hours on 1 January 2100. This parameter is ignored unless the timeSource parameter is set to NISYNC_VAL_INIT_TIME_SRC_MANUAL. |
| timeFractionalNanoseconds | ViUInt16 | Specifies the fractional nanoseconds portion of the time to which the board time will be set. Note that NI-Sync supports setting the initial time between 0 hours on 1 January 1970 and 0 hours on 1 January 2100. This parameter is ignored unless the timeSource parameter is set to NISYNC_VAL_INIT_TIME_SRC_MANUAL. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_settimereference1588ordinaryclock.html language=enus -->
## TOPIC 00171: niSync_SetTimeReference1588OrdinaryClock

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_settimereference1588ordinaryclock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_settimereference1588ordinaryclock.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_SetTimeReference1588OrdinaryClock

### niSync_SetTimeReference1588OrdinaryClock

#### C Function Prototype

ViStatus _VI_FUNC niSync_SetTimeReference1588OrdinaryClock (ViSession vi);

#### Purpose

Sets the selected time reference of the specified device to IEEE 1588. If the device is not a 1588 slave and you set 1588 as the selected time reference, the board time enters free running mode.

This function is a nonblocking call that returns immediately regardless of the state of the time reference selected. Selecting the time reference is a system-wide (per device) configuration that persists after the session exits. The time reference is not reservable; the last call to select the time reference takes precedence.

If the selected time reference is not providing valid time information, the board time goes into free running mode, starting at the last known time and running at the last frequency that was applied.

|  | Note The servo may apply a macro phase adjustment when your device's board time and the selected time reference varies by more than 1 ms. A macro phase adjustment adjusts the selected time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the selected time reference is set forward, future time events and clock transitions that were missed occur immediately. If the selected time reference is set backward, future time events and clock transitions are delayed. An alternative to calling this function is to configure the default selected time reference through Measurement & Automation Explorer. The selected state is then reapplied at every restart. Closing the session that calls this function does not alter the value of the selected time reference. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_settimereference8021as.html language=enus -->
## TOPIC 00172: niSync_SetTimeReference8021AS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_settimereference8021as.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_settimereference8021as.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_SetTimeReference8021AS

### niSync_SetTimeReference8021AS

#### C Function Prototype

ViStatus _VI_FUNC niSync_SetTimeReference8021ASOrdinaryClock (ViSession vi);

#### Purpose

Sets the selected time reference of the specified device to IEEE 802.1AS. If the device is not a 802.1AS slave and you set 802.1AS as the selected time reference, the board time enters free running mode.

This function is a nonblocking call that returns immediately regardless of the state of the time reference selected. Selecting the time reference is a system-wide (per device) configuration that persists after the session exits. The time reference is not reservable; the last call to select the time reference takes precedence.

If the selected time reference is not providing valid time information, the board time goes into free running mode, starting at the last known time and running at the last frequency that was applied.

|  | Note The servo may apply a macro phase adjustment when your device's board time and the selected time reference varies by more than 1 ms. A macro phase adjustment adjusts the selected time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the selected time reference is set forward, future time events and clock transitions that were missed occur immediately. If the selected time reference is set backward, future time events and clock transitions are delayed. Closing the session that calls this function does not alter the value of the selected time reference. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_settimereferencefreerunning.html language=enus -->
## TOPIC 00173: niSync_SetTimeReferenceFreeRunning

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_settimereferencefreerunning.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_settimereferencefreerunning.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_SetTimeReferenceFreeRunning

### niSync_SetTimeReferenceFreeRunning

#### C Function Prototype

ViStatus _VI_FUNC niSync_SetTimeReferenceFreeRunning (ViSession vi);

#### Purpose

Sets the selected time reference of the specified device to Free Running, where its start time and frequency are not tied to any time reference. The board time atomically increments at the last applied frequency. Use this instance if you do not have a strong connection to a network or a time reference. Your device will automatically enter free running mode if the selected time reference does not provide valid time information.

This function is a nonblocking call that returns immediately regardless of the state of the time reference selected. Selecting the time reference is a system-wide (per device) configuration that persists after the session exits. The time reference is not reservable; the last call to select the time reference takes precedence.

If the selected time reference is not providing valid time information, the board time goes into free running mode, starting at the last known time and running at the last frequency that was applied.

|  | Note The servo may apply a macro phase adjustment when your device's board time and the selected time reference varies by more than 1 ms. A macro phase adjustment adjusts the selected time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the selected time reference is set forward, future time events and clock transitions that were missed occur immediately. If the selected time reference is set backward, future time events and clock transitions are delayed. An alternative to calling this function is to configure the default selected time reference through Measurement & Automation Explorer. The selected state is then reapplied at every restart. Closing the session that calls this function does not alter the value of the selected time reference. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_settimereferencegps.html language=enus -->
## TOPIC 00174: niSync_SetTimeReferenceGPS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_settimereferencegps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_settimereferencegps.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_SetTimeReferenceGPS

### niSync_SetTimeReferenceGPS

#### C Function Prototype

ViStatus _VI_FUNC niSync_SetTimeReferenceGPS (ViSession vi);

#### Purpose

Sets the selected time reference of the specified device to GPS. This function is a nonblocking call that returns immediately regardless of the state of the time reference selected. Selecting the time reference is a system-wide (per device) configuration that persists after the session exits. The time reference is not reservable; the last call to select the time reference takes precedence.

If the selected time reference is not providing valid time information, the board time goes into free running mode, starting at the last known time and running at the last frequency that was applied.

|  | Note The servo may apply a macro phase adjustment when your device's board time and the selected time reference varies by more than 1 ms. A macro phase adjustment adjusts the selected time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the selected time reference is set forward, future time events and clock transitions that were missed occur immediately. If the selected time reference is set backward, future time events and clock transitions are delayed. An alternative to calling this function is to configure the default selected time reference through Measurement & Automation Explorer. The selected state is then reapplied at every restart. Closing the session that calls this function does not alter the value of the selected time reference. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_settimereferenceirig.html language=enus -->
## TOPIC 00175: niSync_SetTimeReferenceIRIG

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_settimereferenceirig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_settimereferenceirig.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_SetTimeReferenceIRIG

### niSync_SetTimeReferenceIRIG

#### C Function Prototype

ViStatus _VI_FUNC niSync_SetTimeReferenceIRIG (ViSession vi, ViInt32 irigType, ViConstString terminalName);

#### Purpose

Sets the selected time reference of the specified device to IRIG. You must have an external IRIG source connected to the specified terminal for this function to operate.

This function is a nonblocking call that returns immediately regardless of the state of the time reference selected. Selecting the time reference is a system-wide (per device) configuration that persists after the session exits. The time reference is not reservable; the last call to select the time reference takes precedence.

If the selected time reference is not providing valid time information, the board time goes into free running mode, starting at the last known time and running at the last frequency that was applied.

|  | Note The servo may apply a macro phase adjustment when your device's board time and the selected time reference varies by more than 1 ms. A macro phase adjustment adjusts the selected time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the selected time reference is set forward, future time events and clock transitions that were missed occur immediately. If the selected time reference is set backward, future time events and clock transitions are delayed. An alternative to calling this function is to configure the default selected time reference through Measurement & Automation Explorer. The selected state is then reapplied at every restart. Closing the session that calls this function does not alter the value of the selected time reference. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| irigType | ViInt32 | Specifies the type of IRIG output generated by the external IRIG source. Valid Values: NISYNC_VAL_IRIG_TYPE_IRIGB_DC NISYNC_VAL_IRIG_TYPE_IRIGB_AM |
| terminalName | viConstString | An input string that specifies the terminal to which the IRIG input is connected. Refer to your hardware documentation to determine which terminals on your device support IRIG. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_settimereferencepps.html language=enus -->
## TOPIC 00176: niSync_SetTimeReferencePPS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_settimereferencepps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_settimereferencepps.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

niSync_SetTimeReferencePPS

### niSync_SetTimeReferencePPS

#### C Function Prototype

ViStatus _VI_FUNC niSync_SetTimeReferencePPS (ViSession vi, ViConstString terminalName, ViBoolean useManualTime, ViUInt32 initialTimeSeconds, ViUInt32 initialTimeNanoseconds, ViUInt16 initialTimeFractionalNanoseconds);

#### Purpose

Sets the selected time reference of the device to PPS (pulse per second).

This function is a nonblocking call that returns immediately regardless of the state of the time reference selected. Selecting the time reference is a system-wide (per device) configuration that persists after the session exits. The time reference is not reservable; the last call to select the time reference takes precedence.

|  | Note The servo may apply a macro phase adjustment when your device's board time and the selected time reference varies by more than 1 ms. A macro phase adjustment adjusts the selected time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the selected time reference is set forward, future time events and clock transitions that were missed occur immediately. If the selected time reference is set backward, future time events and clock transitions are delayed. An alternative to calling this function is to configure the default selected time reference through Measurement & Automation Explorer. The selected state is then reapplied at every restart. Closing the session that calls this function does not alter the value of the selected time reference. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |
| terminalName | ViConstString | Specifies the terminal that contains the PPS signal. |
| useManualTime | ViBoolean | Specifies whether to use a user-supplied time or the OS system time to set the board time when the module receives the first pulse. After the first pulse sets the board time, every subsequent pulse is interpreted to be received one second later, and the function adjusts the board time accordingly. |
| initialTimeSeconds | ViUInt32 | Specifies the seconds field of the time to set the board time to when the module receives the first pulse. Only use this parameter if you set useManualTime to TRUE. |
| initialTimeNanoseconds | ViUInt32 | Specifies the nanoseconds field of the time to set the board time to when the module receives the first pulse. Only use this parameter if you set useManualTime to TRUE. |
| initialTimeFractionalNanoseconds | ViUInt16 | Specifies the fractional nanoseconds field of the time to set the board time to when the module receives the first pulse. Only use this parameter if you set useManualTime to TRUE. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_start1588.html language=enus -->
## TOPIC 00177: niSync_Start1588

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_start1588.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_start1588.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_Start1588

#### C Function Prototype

ViStatus _VI_FUNC niSync_Start1588 (ViSession vi);

#### Purpose

Begins participation in the IEEE 1588-2008 time synchronization protocol.

To synchronize clocks, future time events, and triggered timestamps to 1588 time, use this function in conjunction with [niSync_SetTimeReference1588OrdinaryClock](nisync_settimereference1588ordinaryclock.html). Use [niSync_Stop1588](nisync_stop1588.html) to stop participation in a 1588 session. Alternately, you can start and stop 1588 participation in the Test Panels window of Measurement & Automation Explorer (MAX).

|  | Note This function returns as soon as participation begins and does not wait until the 1588 clock has reached a steady state. You do not need to invoke this function in the same session as these other operations. You can invoke it in a separate session associated with the same device. If the clock participating in 1588 enters the faulty state, and 1588 is the selected time reference, then future time events, clocks, and timestamps are no longer synchronized with other 1588 devices participating in PTP. This should not occur on a well designed and stable network. You can check for this condition by monitoring the NISYNC_ATTR_1588_CLOCK_STATE attribute. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_start8021as.html language=enus -->
## TOPIC 00178: niSync_Start8021AS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_start8021as.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_start8021as.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_Start8021AS

#### C Function Prototype

ViStatus _VI_FUNC niSync_Start8021AS (ViSession vi);

#### Purpose

Begins participation in the IEEE 802.1AS time synchronization protocol.

To synchronize clocks, future time events, and triggered timestamps to 802.1AS time, use this function in conjunction with [niSync_SetTimeReference8021AS](nisync_settimereference8021as.html). Use [niSync_Stop8021AS](nisync_stop8021as.html) to stop participation in an 802.1AS session.

|  | Note This function returns as soon as participation begins and does not wait until the 802.1AS clock has reached a steady state. You do not need to invoke this function in the same session as these other operations. You can invoke it in a separate session associated with the same device. This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_stop1588.html language=enus -->
## TOPIC 00179: niSync_Stop1588

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_stop1588.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_stop1588.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_Stop1588

#### C Function Prototype

ViStatus _VI_FUNC niSync_Stop1588 (ViSession vi);

#### Purpose

Ends participation in the IEEE 1588-2008 time synchronization protocol. You must be participating in 1588 in order for this function to operate. Use [niSync_Start1588](nisync_start1588.html) to begin participation in the 1588 protocol.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_stop8021as.html language=enus -->
## TOPIC 00180: niSync_Stop8021AS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_stop8021as.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_stop8021as.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### niSync_Stop8021AS

#### C Function Prototype

ViStatus _VI_FUNC niSync_Stop8021AS (ViSession vi);

#### Purpose

Ends participation in the IEEE 802.1AS time synchronization protocol. You must be participating in 802.1AS in order for this function to operate. Use [niSync_Start8021AS](nisync_start8021as.html) to begin participation in the 802.1AS protocol.

|  | Note This attribute is supported only on certain targets. Refer to Target Support for Timing Attributes and Functions to determine whether or not this attribute is supported on your target. |
| --- | --- |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vi | ViSession | The session handle that you obtain from niSync_init. The handle identifies a particular instrument session. |

[Return Values](status_codes.html)

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_disable.html language=enus -->
## TOPIC 00181: NISYNC_VAL_1588_CLK_STATE_DISABLE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_disable.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_DISABLE

#### Description

Specifies that the 1588 clock associated with this session is in the disabled state in terms of its participation in PTP. This is a "final" state that indicates that this clock is not participating in PTP since it has been disabled.

#### Defined Value

2

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_fault.html language=enus -->
## TOPIC 00182: NISYNC_VAL_1588_CLK_STATE_FAULT

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_fault.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_fault.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_FAULT

#### Description

Specifies that the 1588 clock associated with this session is in the faulty state in terms of its participation in PTP. This is a "final" state that indicates that this clock is not participating in PTP due to a problem. Address the problem such that the clock can participate in PTP.

#### Defined Value

1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_init.html language=enus -->
## TOPIC 00183: NISYNC_VAL_1588_CLK_STATE_INIT

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_init.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_init.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_INIT

#### Description

Specifies that the 1588 clock associated with this session is in the initializing state in terms of its participation in PTP. This is not a "final" state.

#### Defined Value

0

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_listening.html language=enus -->
## TOPIC 00184: NISYNC_VAL_1588_CLK_STATE_LISTENING

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_listening.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_listening.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_LISTENING

#### Description

Specifies that the 1588 clock associated with this session is in the listening state in terms of its participation in PTP. This is not a "final" state. The clock has begun participation in PTP and is waiting for communication that will determine its final state.

#### Defined Value

3

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_master.html language=enus -->
## TOPIC 00185: NISYNC_VAL_1588_CLK_STATE_MASTER

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_master.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_master.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_MASTER

#### Description

Specifies that the 1588 clock associated with this session is in the master state in terms of its participation in PTP. This is a "final" state that specifies that this clock has been selected as the master clock for its subdomain.

#### Defined Value

5

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_not_defined.html language=enus -->
## TOPIC 00186: NISYNC_VAL_1588_CLK_STATE_NOT_DEFINED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_not_defined.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_not_defined.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_NOT_DEFINED

#### Description

Specifies that the state of 1588 clock associated with this session is not defined.

#### Defined Value

–1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_passive.html language=enus -->
## TOPIC 00187: NISYNC_VAL_1588_CLK_STATE_PASSIVE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_passive.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_passive.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_PASSIVE

#### Description

Specifies that the 1588 clock associated with this session is in the passive state in terms of its participation in PTP. This is a "final" state that specifies that this clock will not generate any PTP-related communications.

#### Defined Value

6

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_premaster.html language=enus -->
## TOPIC 00188: NISYNC_VAL_1588_CLK_STATE_PREMASTER

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_premaster.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_premaster.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_PREMASTER

#### Description

Specifies that the 1588 clock associated with this session is in the pre-master state in terms of its participation in PTP. This is not a "final" state.

#### Defined Value

4

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_slave.html language=enus -->
## TOPIC 00189: NISYNC_VAL_1588_CLK_STATE_SLAVE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_slave.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_slave.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_SLAVE

#### Description

Specifies that the 1588 clock associated with this session is in the slave state in terms of its participation in PTP. This is a "final" state that specifies that this clock has been selected as a slave clock within its subdomain.

#### Defined Value

8

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_1588_clk_state_uncalibrated.html language=enus -->
## TOPIC 00190: NISYNC_VAL_1588_CLK_STATE_UNCALIBRATED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_1588_clk_state_uncalibrated.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_1588_clk_state_uncalibrated.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_1588_CLK_STATE_UNCALIBRATED

#### Description

Specifies that the 1588 clock associated with this session is in the uncalibrated state in terms of its participation in PTP. This is not a "final" state.

#### Defined Value

7

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_all_connected.html language=enus -->
## TOPIC 00191: NISYNC_VAL_ALL_CONNECTED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_all_connected.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_all_connected.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_ALL_CONNECTED

#### Description

Indicates that a source or destination should disconnect from all connected terminals. If this value is specified for the source parameter, all terminals connected to the destination terminal will be disconnected from the destination terminal. If this value is specified for the destination parameter, all terminals connected to the source terminal will be disconnected. If this value is specified to both the source and destination, all connections will be disconnected.

#### Defined Value

"AllConnected"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_board_clk.html language=enus -->
## TOPIC 00192: NISYNC_VAL_BOARD_CLK

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_board_clk.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_board_clk.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_BOARD_CLK

#### Description

The niSync device's local board clock.

#### Defined Value

"BoardClk"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_clk10.html language=enus -->
## TOPIC 00193: NISYNC_VAL_CLK10

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_clk10.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_clk10.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_CLK10

#### Description

The PXI_Clk10 terminal. When used as a source parameter, this value indicates the 10 MHz PXI Reference Clock (PXI_CLK10). When used as a destination parameter, this value indicates the 10 MHz PXI frequency input line (PXI_CLK10_IN).

#### Defined Value

"PXI_Clk10"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_clk100.html language=enus -->
## TOPIC 00194: NISYNC_VAL_CLK100

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_clk100.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_clk100.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_CLK100

#### Description

The PXIe_Clk100 terminal. When used as a source parameter, this value indicates the 100 MHz PXI Reference Clock (PXIE_CLK100).

#### Defined Value

"PXIe_Clk100"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_clk10_in.html language=enus -->
## TOPIC 00195: NISYNC_VAL_CLK10_IN

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_clk10_in.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_clk10_in.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_CLK10_IN

#### Description

The PXI_Clk10_In terminal. This value is the destination used to overdrive PXI_Clk10.

#### Defined Value

"PXI_Clk10_In"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_clkin.html language=enus -->
## TOPIC 00196: NISYNC_VAL_CLKIN

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_clkin.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_clkin.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_CLKIN

#### Description

The ClkIn front panel terminal.

#### Defined Value

"ClkIn"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_clkout.html language=enus -->
## TOPIC 00197: NISYNC_VAL_CLKOUT

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_clkout.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_clkout.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_CLKOUT

#### Description

The ClkOut front panel terminal.

#### Defined Value

"ClkOut"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_dds.html language=enus -->
## TOPIC 00198: NISYNC_VAL_DDS

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_dds.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_dds.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_DDS

#### Description

The DDS Clock terminal. When specified as a synchronization clock sources, this value indicates that the DDS should be used to synchronize terminal connections for the specified synchronization clock zone (PFI or PXI_Trig/PXI_Star). When specified as a source parameter, this value indicates that the DDS should be connected to the ClkOut front panel terminal.

#### Defined Value

"DDS"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_dds_update_immediate.html language=enus -->
## TOPIC 00199: NISYNC_VAL_DDS_UPDATE_IMMEDIATE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_dds_update_immediate.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_dds_update_immediate.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_DDS_UPDATE_IMMEDIATE

#### Description

Indicates that the DDS should be updated immediately. That is, the DDS update pulse is issued immediately after the frequency is changed.

#### Defined Value

"DDS_UpdateImmediate"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_edge_any.html language=enus -->
## TOPIC 00200: NISYNC_VAL_EDGE_ANY

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_edge_any.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_edge_any.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_EDGE_ANY

#### Description

Specifies that the trigger is associated with any edge of a digital signal, rising or falling. That is, when the digital signal level transitions from either a logic low to a logic high or from a logic high to a logic low.

#### Defined Value

2

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_edge_falling.html language=enus -->
## TOPIC 00201: NISYNC_VAL_EDGE_FALLING

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_edge_falling.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_edge_falling.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_EDGE_FALLING

#### Description

Specifies that the trigger is associated with a falling edge of a digital signal. That is, when the digital signal level transitions from a logic high to a logic low.

#### Defined Value

1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_antenna_error.html language=enus -->
## TOPIC 00202: NISYNC_VAL_GPS_ANTENNA_ERROR

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_antenna_error.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_antenna_error.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_ANTENNA_ERROR

#### Description

Specifies the onboard GPS receiver does not have an antenna correctly connected.

#### Defined Value

1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_no_gps_time.html language=enus -->
## TOPIC 00203: NISYNC_VAL_GPS_NO_GPS_TIME

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_no_gps_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_no_gps_time.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_NO_GPS_TIME

#### Description

Specifies the onboard GPS receiver is not locked to GPS time.

#### Defined Value

6

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_no_useable_satellite.html language=enus -->
## TOPIC 00204: NISYNC_VAL_GPS_NO_USEABLE_SATELLITE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_no_useable_satellite.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_no_useable_satellite.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_NO_USEABLE_SATELLITE

#### Description

Specifies the onboard GPS receiver is unable to locate any visible satellites.

#### Defined Value

2

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_one_useable_satellite.html language=enus -->
## TOPIC 00205: NISYNC_VAL_GPS_ONE_USEABLE_SATELLITE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_one_useable_satellite.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_one_useable_satellite.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_ONE_USEABLE_SATELLITE

#### Description

Specifies the onboard GPS receiver can locate only one visible satellite.

#### Defined Value

3

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_pdop_too_high.html language=enus -->
## TOPIC 00206: NISYNC_VAL_GPS_PDOP_TOO_HIGH

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_pdop_too_high.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_pdop_too_high.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_PDOP_TOO_HIGH

#### Description

Specifies the onboard GPS receiver is reporting a PDOP (Position Dilution of Position) error.

#### Defined Value

7

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_self_survey_complete.html language=enus -->
## TOPIC 00207: NISYNC_VAL_GPS_SELF_SURVEY_COMPLETE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_self_survey_complete.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_self_survey_complete.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_SELF_SURVEY_COMPLETE

#### Description

Specifies the onboard GPS receiver has completed a self survey.

#### Defined Value

10

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_self_survey_not_complete.html language=enus -->
## TOPIC 00208: NISYNC_VAL_GPS_SELF_SURVEY_NOT_COMPLETE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_self_survey_not_complete.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_self_survey_not_complete.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_SELF_SURVEY_NOT_COMPLETE

#### Description

Specifies the onboard GPS receiver has not completed a self survey.

#### Defined Value

11

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_three_useable_satellites.html language=enus -->
## TOPIC 00209: NISYNC_VAL_GPS_THREE_USEABLE_SATELLITES

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_three_useable_satellites.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_three_useable_satellites.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_THREE_USEABLE_SATELLITES

#### Description

Specifies the onboard GPS receiver can locate only three visible satellites.

#### Defined Value

5

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_two_useable_satellites.html language=enus -->
## TOPIC 00210: NISYNC_VAL_GPS_TWO_USEABLE_SATELLITES

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_two_useable_satellites.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_two_useable_satellites.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_TWO_USEABLE_SATELLITES

#### Description

Specifies the onboard GPS receiver can locate only two visible satellites.

#### Defined Value

4

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_uninitialized.html language=enus -->
## TOPIC 00211: NISYNC_VAL_GPS_UNINITIALIZED

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_uninitialized.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_uninitialized.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_UNINITIALIZED

#### Description

Specifies the onboard GPS receiver cannot be initialized to a known state.

#### Defined Value

0

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_gps_unuseable_satellite.html language=enus -->
## TOPIC 00212: NISYNC_VAL_GPS_UNUSABLE_SATELLITE

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_gps_unuseable_satellite.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_gps_unuseable_satellite.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_GPS_UNUSABLE_SATELLITE

#### Description

Specifies the onboard GPS receiver is locked to an unusable satellite.

#### Defined Value

8

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_init_time_src_manual.html language=enus -->
## TOPIC 00213: NISYNC_VAL_INIT_TIME_SRC_MANUAL

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_init_time_src_manual.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_init_time_src_manual.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_INIT_TIME_SRC_MANUAL

#### Description

Specifies that the time of the 1588 clock associated with this session will be initialized to the manually specified time.

#### Defined Value

1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_init_time_src_system_clk.html language=enus -->
## TOPIC 00214: NISYNC_VAL_INIT_TIME_SRC_SYSTEM_CLK

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_init_time_src_system_clk.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_init_time_src_system_clk.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_INIT_TIME_SRC_SYSTEM_CLK

#### Description

Specifies that the time of the 1588 clock associated with this session will be initialized to the time specified by the system clock.

#### Defined Value

0

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_invert.html language=enus -->
## TOPIC 00215: NISYNC_VAL_INVERT

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_invert.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_invert.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_INVERT

#### Description

Indicates that the routed signal should be inverted.

#### Defined Value

1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_irig_type_irigb_am.html language=enus -->
## TOPIC 00216: NISYNC_VAL_IRIG_TYPE_IRIGB_AM

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_irig_type_irigb_am.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_irig_type_irigb_am.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_IRIG_TYPE_IRIGB_AM

#### Description

Specifies the IRIG protocol IRIGB-AM (amplitude modulated).

#### Defined Value

1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_irig_type_irigb_dc.html language=enus -->
## TOPIC 00217: NISYNC_VAL_IRIG_TYPE_IRIGB_DC

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_irig_type_irigb_dc.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_irig_type_irigb_dc.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_IRIG_TYPE_IRIGB_DC

#### Description

Specifies the IRIG protocol IRIGB-DC (DC level shift).

#### Defined Value

0

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_level_high.html language=enus -->
## TOPIC 00218: NISYNC_VAL_LEVEL_HIGH

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_level_high.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_level_high.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_LEVEL_HIGH

#### Description

Specifies that the digital signal level is a logic high.

#### Defined Value

1

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_level_low.html language=enus -->
## TOPIC 00219: NISYNC_VAL_LEVEL_LOW

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_level_low.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_level_low.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_LEVEL_LOW

#### Description

Specifies that the digital signal level is a logic low.

#### Defined Value

0

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_oscillator.html language=enus -->
## TOPIC 00220: NISYNC_VAL_OSCILLATOR

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_oscillator.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_oscillator.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_OSCILLATOR

#### Description

The onboard oscillator (OCXO).

#### Defined Value

"Oscillator"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfi0.html language=enus -->
## TOPIC 00221: NISYNC_VAL_PFI0

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfi0.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFI0

#### Description

The PFI0 front panel terminal.

#### Defined Value

"PFI0"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfi1.html language=enus -->
## TOPIC 00222: NISYNC_VAL_PFI1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfi1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfi1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFI1

#### Description

The PFI1 front panel terminal.

#### Defined Value

"PFI1"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfi2.html language=enus -->
## TOPIC 00223: NISYNC_VAL_PFI2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfi2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfi2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFI2

#### Description

The PFI2 front panel terminal.

#### Defined Value

"PFI2"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfi3.html language=enus -->
## TOPIC 00224: NISYNC_VAL_PFI3

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfi3.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfi3.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFI3

#### Description

The PFI3 front panel terminal.

#### Defined Value

"PFI3"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfi4.html language=enus -->
## TOPIC 00225: NISYNC_VAL_PFI4

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfi4.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfi4.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFI4

#### Description

The PFI4 front panel terminal.

#### Defined Value

"PFI4"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfi5.html language=enus -->
## TOPIC 00226: NISYNC_VAL_PFI5

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfi5.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfi5.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFI5

#### Description

The PFI5 front panel terminal.

#### Defined Value

"PFI5"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfilvds0.html language=enus -->
## TOPIC 00227: NISYNC_VAL_PFILVDS0

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfilvds0.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfilvds0.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFILVDS0

#### Description

The PFILVDS0 front panel terminal.

#### Defined Value

"PFI_LVDS0"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfilvds1.html language=enus -->
## TOPIC 00228: NISYNC_VAL_PFILVDS1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfilvds1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfilvds1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFILVDS1

#### Description

The PFILVDS1 front panel terminal.

#### Defined Value

"PFI_LVDS1"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pfilvds2.html language=enus -->
## TOPIC 00229: NISYNC_VAL_PFILVDS2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pfilvds2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pfilvds2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PFILVDS2

#### Description

The PFILVDS2 front panel terminal.

#### Defined Value

"PFI_LVDS2"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara.html language=enus -->
## TOPIC 00230: NISYNC_VAL_PXIEDSTARA

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA

#### Description

The PXIEDSTARA backplane terminal.

#### Defined Value

"PXIe_DStarA"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara0.html language=enus -->
## TOPIC 00231: NISYNC_VAL_PXIEDSTARA0

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara0.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara0.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA0

#### Description

The PXIEDSTARA0 backplane terminal.

#### Defined Value

"PXIe_DStarA0"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara1.html language=enus -->
## TOPIC 00232: NISYNC_VAL_PXIEDSTARA1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA1

#### Description

The PXIEDSTARA1 backplane terminal.

#### Defined Value

"PXIe_DStarA1"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara10.html language=enus -->
## TOPIC 00233: NISYNC_VAL_PXIEDSTARA10

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara10.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara10.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA10

#### Description

The PXIEDSTARA10 backplane terminal.

#### Defined Value

"PXIe_DStarA10"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara11.html language=enus -->
## TOPIC 00234: NISYNC_VAL_PXIEDSTARA11

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara11.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara11.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA11

#### Description

The PXIEDSTARA11 backplane terminal.

#### Defined Value

"PXIe_DStarA11"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara12.html language=enus -->
## TOPIC 00235: NISYNC_VAL_PXIEDSTARA12

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara12.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara12.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA12

#### Description

The PXIEDSTARA12 backplane terminal.

#### Defined Value

"PXIe_DStarA12"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara13.html language=enus -->
## TOPIC 00236: NISYNC_VAL_PXIEDSTARA13

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara13.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara13.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA13

#### Description

The PXIEDSTARA13 backplane terminal.

#### Defined Value

"PXIe_DStarA13"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara14.html language=enus -->
## TOPIC 00237: NISYNC_VAL_PXIEDSTARA14

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara14.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara14.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA14

#### Description

The PXIEDSTARA14 backplane terminal.

#### Defined Value

"PXIe_DStarA14"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara15.html language=enus -->
## TOPIC 00238: NISYNC_VAL_PXIEDSTARA15

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara15.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara15.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA15

#### Description

The PXIEDSTARA15 backplane terminal.

#### Defined Value

"PXIe_DStarA15"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara16.html language=enus -->
## TOPIC 00239: NISYNC_VAL_PXIEDSTARA16

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara16.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara16.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA16

#### Description

The PXIEDSTARA16 backplane terminal.

#### Defined Value

"PXIe_DStarA16"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara2.html language=enus -->
## TOPIC 00240: NISYNC_VAL_PXIEDSTARA2

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara2.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA2

#### Description

The PXIEDSTARA2 backplane terminal.

#### Defined Value

"PXIe_DStarA2"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara3.html language=enus -->
## TOPIC 00241: NISYNC_VAL_PXIEDSTARA3

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara3.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara3.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA3

#### Description

The PXIEDSTARA3 backplane terminal.

#### Defined Value

"PXIe_DStarA3"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara4.html language=enus -->
## TOPIC 00242: NISYNC_VAL_PXIEDSTARA4

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara4.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara4.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA4

#### Description

The PXIEDSTARA4 backplane terminal.

#### Defined Value

"PXIe_DStarA4"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara5.html language=enus -->
## TOPIC 00243: NISYNC_VAL_PXIEDSTARA5

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara5.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara5.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA5

#### Description

The PXIEDSTARA5 backplane terminal.

#### Defined Value

"PXIe_DStarA5"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara6.html language=enus -->
## TOPIC 00244: NISYNC_VAL_PXIEDSTARA6

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara6.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara6.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA6

#### Description

The PXIEDSTARA6 backplane terminal.

#### Defined Value

"PXIe_DStarA6"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara7.html language=enus -->
## TOPIC 00245: NISYNC_VAL_PXIEDSTARA7

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara7.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara7.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA7

#### Description

The PXIEDSTARA7 backplane terminal.

#### Defined Value

"PXIe_DStarA7"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara8.html language=enus -->
## TOPIC 00246: NISYNC_VAL_PXIEDSTARA8

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara8.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara8.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA8

#### Description

The PXIEDSTARA8 backplane terminal.

#### Defined Value

"PXIe_DStarA8"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstara9.html language=enus -->
## TOPIC 00247: NISYNC_VAL_PXIEDSTARA9

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstara9.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstara9.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARA9

#### Description

The PXIEDSTARA9 backplane terminal.

#### Defined Value

"PXIe_DStarA9"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstarb.html language=enus -->
## TOPIC 00248: NISYNC_VAL_PXIEDSTARB

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstarb.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstarb.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARB

#### Description

The PXIEDSTARB backplane terminal.

#### Defined Value

"PXIe_DStarB"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstarb0.html language=enus -->
## TOPIC 00249: NISYNC_VAL_PXIEDSTARB0

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstarb0.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstarb0.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARB0

#### Description

The PXIEDSTARB0 backplane terminal.

#### Defined Value

"PXIe_DStarB0"

<!--NI_TOPIC bundle=ni-sync-c path=nisyncapi/cvi/nisync_val_pxiedstarb1.html language=enus -->
## TOPIC 00250: NISYNC_VAL_PXIEDSTARB1

- bundle_id: `ni-sync-c`
- source_path: `nisyncapi/cvi/nisync_val_pxiedstarb1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-c/raw/resource/enus/nisyncapi/cvi/nisync_val_pxiedstarb1.html
- document_id: `ni-sync-c`
- page_type: `leaf`
- content_type: ``

### NISYNC_VAL_PXIEDSTARB1

#### Description

The PXIEDSTARB1 backplane terminal.

#### Defined Value

"PXIe_DStarB1"
