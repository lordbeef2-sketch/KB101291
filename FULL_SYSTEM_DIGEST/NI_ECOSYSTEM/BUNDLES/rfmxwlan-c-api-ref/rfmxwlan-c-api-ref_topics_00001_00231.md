# NI DOCUMENT BUNDLE: rfmxwlan-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwlan-c-api-ref start=1 end=231 -->
<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga6ed45741745e3f092294eee0191daf44.html language=enus -->
## TOPIC 00001: RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga6ed45741745e3f092294eee0191daf44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga6ed45741745e3f092294eee0191daf44.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips. SyntaxRFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To10498062int32Read/WriteN/ARemarks If you set this attribute to -1, all chips in the si

### RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH

Specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498062 | int32 | Read/Write | N/A |

#### Remarks

If you set this attribute to -1, all chips in the signal are used for measurement.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1000.

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga8853fa2c84e39aff91ce617c75b79c2d.html language=enus -->
## TOPIC 00002: RFMXWLAN_ATTR_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga8853fa2c84e39aff91ce617c75b79c2d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga8853fa2c84e39aff91ce617c75b79c2d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable frequency error correction. SyntaxRFMXWLAN_ATTR_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLEDNumeric ValueData TypeAccessApplies To10498092int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instanc

### RFMXWLAN_ATTR_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED

Specifies whether to enable frequency error correction.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498092 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED_FALSE | 0 (0x0) | Disables frequency error correction. |
| RFMXWLAN_VAL_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED_TRUE | 1 (0x1) | Enables frequency error correction. |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga9a4b4460d826a79bb9b7a7c4a7b8b378.html language=enus -->
## TOPIC 00003: RFMXWLAN_ATTR_DSSSMODACC_DATA_DECODING_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga9a4b4460d826a79bb9b7a7c4a7b8b378.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga9a4b4460d826a79bb9b7a7c4a7b8b378.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). SyntaxRFMXWLAN_ATTR_DSSSMODACC_DATA_DECODING_ENABLEDNumeric ValueData TypeAccessApplies To10498172int32Read/WriteN/ARemarksSet the RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH attribute to -

### RFMXWLAN_ATTR_DSSSMODACC_DATA_DECODING_ENABLED

Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_DATA_DECODING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498172 | int32 | Read/Write | N/A |

#### Remarks

Note

Set the [RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc_1ga6ed45741745e3f092294eee0191daf44.html) attribute to -1 to decode all chips. Data decoding is not supported if the data rate is 33 Mbps.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_DSSSMODACC_DATA_DECODING_ENABLED_FALSE | 0 (0x0) | Disables data decoding. |
| RFMXWLAN_VAL_DSSSMODACC_DATA_DECODING_ENABLED_TRUE | 1 (0x1) | Enables data decoding. |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__power_1gae9b385a29fad096739ad134100de52e4.html language=enus -->
## TOPIC 00004: RFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_START_TIME

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__power_1gae9b385a29fad096739ad134100de52e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__power_1gae9b385a29fad096739ad134100de52e4.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start time of the custom power gate. This value is expressed in seconds. SyntaxRFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_START_TIMENumeric ValueData TypeAccessApplies To10498069float64Read/WriteGateRemarks Use "gate<k>" as the Selector String to configure or read this attribute.A valu

### RFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_START_TIME

Specifies the start time of the custom power gate. This value is expressed in seconds.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_START_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498069 | float64 | Read/Write | Gate |

#### Remarks

Use "gate<k>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

A value of 0 indicates that the start time is the start of the PPDU. The default value is 0 seconds.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gacfa192666c5e798652e10827be5edcdc.html language=enus -->
## TOPIC 00005: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CHIP_CLOCK_ERROR_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gacfa192666c5e798652e10827be5edcdc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gacfa192666c5e798652e10827be5edcdc.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip clock error of the transmitter. This value is expressed in parts per million (ppm). SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_CHIP_CLOCK_ERROR_MEANNumeric ValueData TypeAccessApplies To10498130float64Read-OnlyN/ARemarks When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attrib

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CHIP_CLOCK_ERROR_MEAN

Returns the chip clock error of the transmitter. This value is expressed in parts per million (ppm).

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CHIP_CLOCK_ERROR_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498130 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__averaging_1ga3982601abeacbe78e61ff7a92eb29ac0.html) attribute to **True**, this result returns the mean of the chip clock error computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gada729d6611ce80e8b9f947eff545cb56.html language=enus -->
## TOPIC 00006: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_IQ_ORIGIN_OFFSET_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gada729d6611ce80e8b9f947eff545cb56.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gada729d6611ce80e8b9f947eff545cb56.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset. This value is expressed in dB. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_IQ_ORIGIN_OFFSET_MEANNumeric ValueData TypeAccessApplies To10498139float64Read-OnlyN/ARemarks I/Q origin offset is the ratio of the mean value of the signal to the RMS value of the signal. When you s

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_IQ_ORIGIN_OFFSET_MEAN

Returns the I/Q origin offset. This value is expressed in dB.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_IQ_ORIGIN_OFFSET_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498139 | float64 | Read-Only | N/A |

#### Remarks

I/Q origin offset is the ratio of the mean value of the signal to the RMS value of the signal. When you set this [RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__averaging_1ga3982601abeacbe78e61ff7a92eb29ac0.html) attribute to **True**, this result returns the mean of the I/Q origin offset computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gafe346807d8b6c859d39bd5c6a8778e5a.html language=enus -->
## TOPIC 00007: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gafe346807d8b6c859d39bd5c6a8778e5a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results_1gafe346807d8b6c859d39bd5c6a8778e5a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of chips used for the DSSSModAcc measurement. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USEDNumeric ValueData TypeAccessApplies To10498125int32Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result instance. Refe

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USED

Returns the number of chips used for the DSSSModAcc measurement.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498125 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__peak__evm_1gaea0207ec16aa77acf1df3338b7493957.html language=enus -->
## TOPIC 00008: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__peak__evm_1gaea0207ec16aa77acf1df3338b7493957.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__peak__evm_1gaea0207ec16aa77acf1df3338b7493957.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak EVM of the burst. This value is expressed as percentage or in dB. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUMNumeric ValueData TypeAccessApplies To10498100float64Read-OnlyN/ARemarks This measurement is performed in accordance with section 18.4.7.8 of IEEE Sta

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUM

Returns the peak EVM of the burst. This value is expressed as percentage or in dB.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498100 | float64 | Read-Only | N/A |

#### Remarks

This measurement is performed in accordance with section 18.4.7.8 of *IEEE Standard 802.11b-1999*. When you set the [RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__averaging_1ga3982601abeacbe78e61ff7a92eb29ac0.html) attribute to **True**, this result returns the maximum of the peak EVM computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Peak EVM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__peak__evm_1gaf8073da17b33c233b6dc161ec1e7124e.html language=enus -->
## TOPIC 00009: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__peak__evm_1gaf8073da17b33c233b6dc161ec1e7124e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__peak__evm_1gaf8073da17b33c233b6dc161ec1e7124e.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak EVM of the burst. This value is expressed as a percentage or in dB. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MEANNumeric ValueData TypeAccessApplies To10498108float64Read-OnlyN/ARemarks This measurement is performed in accordance with section 16.3.7.9 of IEEE Stan

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MEAN

Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498108 | float64 | Read-Only | N/A |

#### Remarks

This measurement is performed in accordance with section 16.3.7.9 of *IEEE Standard 802.11-2016*. When you set the [RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__averaging_1ga3982601abeacbe78e61ff7a92eb29ac0.html) attribute to **True**, this result returns the mean of the peak EVM computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Peak EVM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power.html language=enus -->
## TOPIC 00010: Power

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_DSSSMODACC_RESULTS_CUSTOM_GATE_AVERAGE_POWER_MEANReturns the average power of the custom gate. This value is expressed in dBm. RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CUSTOM_GATE_PEAK_POWER_MAXIMUMReturns the peak power of the custom gate. This value is e

### Power

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CUSTOM_GATE_AVERAGE_POWER_MEAN | Returns the average power of the custom gate. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CUSTOM_GATE_PEAK_POWER_MAXIMUM | Returns the peak power of the custom gate. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_DATA_AVERAGE_POWER_MEAN | Returns the average power of the data field of the PPDU. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_DATA_PEAK_POWER_MAXIMUM | Returns the peak power of the data field of the PPDU. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_AVERAGE_POWER_MEAN | Returns the average power of the header field of the PPDU. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_PEAK_POWER_MAXIMUM | Returns the peak power of the header field of the PPDU. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_AVERAGE_POWER_MEAN | Returns the average power of the PPDU. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_PEAK_POWER_MAXIMUM | Returns the peak power of the PPDU. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_AVERAGE_POWER_MEAN | Returns the average power of the preamble field of the PPDU. This value is expressed in dBm. |
| RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_PEAK_POWER_MAXIMUM | Returns the peak power of the preamble field of the PPDU. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power_1ga01019731b0a7204cbebe42885df565b1.html language=enus -->
## TOPIC 00011: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power_1ga01019731b0a7204cbebe42885df565b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power_1ga01019731b0a7204cbebe42885df565b1.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the PPDU. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10498168float64Read-OnlyN/ARemarks When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this result ret

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_AVERAGE_POWER_MEAN

Returns the average power of the PPDU. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498168 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__averaging_1ga3982601abeacbe78e61ff7a92eb29ac0.html) attribute to **True**, this result returns the mean of the average PPDU power computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power_1ga6086e69d4d11660548d2cf34464fd283.html language=enus -->
## TOPIC 00012: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power_1ga6086e69d4d11660548d2cf34464fd283.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__power_1ga6086e69d4d11660548d2cf34464fd283.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the PPDU. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10498169float64Read-OnlyN/ARemarks When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this result return

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_PEAK_POWER_MAXIMUM

Returns the peak power of the PPDU. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498169 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__averaging_1ga3982601abeacbe78e61ff7a92eb29ac0.html) attribute to **True**, this result returns the maximum value of the peak PPDU power computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__ppdu__info_1ga1391c7c856bdb078e97565e928fa2da4.html language=enus -->
## TOPIC 00013: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PAYLOAD_LENGTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__ppdu__info_1ga1391c7c856bdb078e97565e928fa2da4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__ppdu__info_1ga1391c7c856bdb078e97565e928fa2da4.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the payload length of the acquired burst. This value is expressed in bytes. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_PAYLOAD_LENGTHNumeric ValueData TypeAccessApplies To10498153int32Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result i

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PAYLOAD_LENGTH

Returns the payload length of the acquired burst. This value is expressed in bytes.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PAYLOAD_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498153 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__ppdu__info_1ga5168c68fb578b9e52a9bcb414318a8fe.html language=enus -->
## TOPIC 00014: RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__ppdu__info_1ga5168c68fb578b9e52a9bcb414318a8fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__results__ppdu__info_1ga5168c68fb578b9e52a9bcb414318a8fe.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of IEEE Standard 802.11 2016. SyntaxRFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUSNumeric ValueData TypeAccessApplies To10498157int32Read-OnlyN/ARemarks You do not need to use a select

### RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUS

Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of *IEEE Standard 802.11 2016*.

#### Syntax

RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10498157 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_FAIL | 0 (0x0) | Returns that the header CRC failed. |
| RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_PASS | 1 (0x1) | Returns that the header CRC passed. |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm_1ga0f4544b00eab5e74933b0a5bef3f637a.html language=enus -->
## TOPIC 00015: RFMXWLAN_ATTR_NUMBER_OF_FREQUENCY_SEGMENTS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm_1ga0f4544b00eab5e74933b0a5bef3f637a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm_1ga0f4544b00eab5e74933b0a5bef3f637a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of frequency segments for 802.11ac and 802.11ax signals. SyntaxRFMXWLAN_ATTR_NUMBER_OF_FREQUENCY_SEGMENTSNumeric ValueData TypeAccessApplies To10485775int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal in

### RFMXWLAN_ATTR_NUMBER_OF_FREQUENCY_SEGMENTS

Specifies the number of frequency segments for 802.11ac and 802.11ax signals.

#### Syntax

RFMXWLAN_ATTR_NUMBER_OF_FREQUENCY_SEGMENTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485775 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Valid values are 1 and 2.

Parent topic:

OFDM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm_1ga80f16fab4c5804d0178ea9b494c7e452.html language=enus -->
## TOPIC 00016: RFMXWLAN_ATTR_NUMBER_OF_RECEIVE_CHAINS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm_1ga80f16fab4c5804d0178ea9b494c7e452.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm_1ga80f16fab4c5804d0178ea9b494c7e452.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of receive chains for OFDM standards. SyntaxRFMXWLAN_ATTR_NUMBER_OF_RECEIVE_CHAINSNumeric ValueData TypeAccessApplies To10485776int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Se

### RFMXWLAN_ATTR_NUMBER_OF_RECEIVE_CHAINS

Specifies the number of receive chains for OFDM standards.

#### Syntax

RFMXWLAN_ATTR_NUMBER_OF_RECEIVE_CHAINS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485776 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

The valid values are as follows.

| Standard | Number of Receive Chains |
| --- | --- |
| 802.11a/g, 802.11j, 802.11p | 1 |
| 802.11n | 1–4 |
| 802.11ac, 802.11ax, 802.11be | 1–8 |

Parent topic:

OFDM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced.html language=enus -->
## TOPIC 00017: Advanced

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPhase RotationPreamble PuncturingUnequal ModulationGroup membersNameDescriptionRFMXWLAN_ATTR_OFDM_2XLDPC_ENABLEDSpecifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. RFMXWLAN_ATTR_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLEDSpecifies whether to enable auto detection of

### Advanced

#### Groups

- Phase Rotation
- Preamble Puncturing
- Unequal Modulation

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_OFDM_2XLDPC_ENABLED | Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. |
| RFMXWLAN_ATTR_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED | Specifies whether to enable auto detection of the PPDU type when performing the OFDMModAcc measurement. |
| RFMXWLAN_ATTR_OFDM_DCM_ENABLED | Specifies whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals. |
| RFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTH | Specifies the bandwidth across which RU subcarriers are distributed, when you set RFMXWLAN_ATTR_OFDM_RU_TYPE attribute to dRU. |
| RFMXWLAN_ATTR_OFDM_FEC_CODING_TYPE | Specifies the type of forward error correction (FEC) coding used. |
| RFMXWLAN_ATTR_OFDM_GUARD_INTERVAL_TYPE | Specifies the size of the guard interval of OFDM symbols. |
| RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED | Specifies whether to enable the decoding of the header fields in the PPDU. |
| RFMXWLAN_ATTR_OFDM_IM_PILOTS_ENABLED | Specifies whether inteference mitigating pilots are present in 802.11bn MU PPDU signals. |
| RFMXWLAN_ATTR_OFDM_LDPC_EXTRA_SYMBOL_SEGMENT | Specifies the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU, 802.11be TB PPDU, and 802.11bn TB PPDU. |
| RFMXWLAN_ATTR_OFDM_LTF_SIZE | Specifies the LTF symbol size. This attribute is applicable only for 802.11ax, 802.11be, and 802.11bn signals. |
| RFMXWLAN_ATTR_OFDM_MCS_INDEX | Specifies the modulation and coding scheme (MCS) index or the data rate when you set the RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED attribute to False. |
| RFMXWLAN_ATTR_OFDM_MU_MIMO_LTF_MODE_ENABLED | Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code. |
| RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS | Specifies the number of HE-SIG-B symbols. |
| RFMXWLAN_ATTR_OFDM_NUMBER_OF_LTF_SYMBOLS | Specifies the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively. |
| RFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLS | Specifies the number of SIG symbols. This attribute is applicable for 802.11be and 802.11bn MU PPDU signals. |
| RFMXWLAN_ATTR_OFDM_NUMBER_OF_SPACE_TIME_STREAMS | Specifies the number of space time streams. |
| RFMXWLAN_ATTR_OFDM_NUMBER_OF_USERS | Specifies the number of users in a multi-user (MU) PPDU. |
| RFMXWLAN_ATTR_OFDM_PE_DISAMBIGUITY | Specifies the packet extension disambiguity information. |
| RFMXWLAN_ATTR_OFDM_PPDU_TYPE | Specifies the PPDU type when you set the RFMXWLAN_ATTR_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED. |
| RFMXWLAN_ATTR_OFDM_PRE_FEC_PADDING_FACTOR | Specifies the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits. |
| RFMXWLAN_ATTR_OFDM_RU_OFFSET_MRU_INDEX | Specifies the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of. |
| RFMXWLAN_ATTR_OFDM_RU_SIZE | Specifies the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax, 802.11be, and 802.11bn signals. |
| RFMXWLAN_ATTR_OFDM_RU_TYPE | Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU). |
| RFMXWLAN_ATTR_OFDM_SCRAMBLER_SEED | Specifies the scrambler seed for combined signal demodulation. This is applicable only if RFMXWLAN_ATTR_OFDMMODACC_COMBINED_SIGNAL_DEMODULATION_ENABLED is set to True. |
| RFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLED | Specifies whether to enable SIG compression. This attribute is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals. |
| RFMXWLAN_ATTR_OFDM_SPACE_TIME_STREAM_OFFSET | Specifies the space time stream offset. |
| RFMXWLAN_ATTR_OFDM_STBC_ENABLED | Specifies whether space-time block coding is enabled. This attribute is applicable only for 802.11ax TB PPDU. |

#### Attachments

None

Parent topic:

OFDM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0cc73b8e23f72aabb6bba00a94739c6f.html language=enus -->
## TOPIC 00018: RFMXWLAN_ATTR_OFDM_2XLDPC_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0cc73b8e23f72aabb6bba00a94739c6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0cc73b8e23f72aabb6bba00a94739c6f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. SyntaxRFMXWLAN_ATTR_OFDM_2XLDPC_ENABLEDNumeric ValueData TypeAccessApplies To10485825int32Read/WriteUserRemarks Use "user<n>" as the Selector String to configure or read this attribute.The default value is False.Na

### RFMXWLAN_ATTR_OFDM_2XLDPC_ENABLED

Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals.

#### Syntax

RFMXWLAN_ATTR_OFDM_2XLDPC_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485825 | int32 | Read/Write | User |

#### Remarks

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_2XLDPC_ENABLED_FALSE | 0 (0x0) | Specifies that 2xLDPC is disabled. |
| RFMXWLAN_VAL_OFDM_2XLDPC_ENABLED_TRUE | 1 (0x1) | Specifies that 2xLDPC is enabled. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html language=enus -->
## TOPIC 00019: RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the decoding of the header fields in the PPDU. SyntaxRFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLEDNumeric ValueData TypeAccessApplies To10485800int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal insta

### RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED

Specifies whether to enable the decoding of the header fields in the PPDU.

#### Syntax

RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485800 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_HEADER_DECODING_ENABLED_FALSE | 0 (0x0) | Header information is not read from the header fields in the PPDU. You must configure the following properties:RFMXWLAN_ATTR_OFDM_NUMBER_OF_USERSRFMXWLAN_ATTR_OFDM_MCS_INDEXRFMXWLAN_ATTR_OFDM_RU_SIZERFMXWLAN_ATTR_OFDM_RU_OFFSET_MRU_INDEXRFMXWLAN_ATTR_OFDM_GUARD_INTERVAL_TYPERFMXWLAN_ATTR_OFDM_LTF_SIZERFMXWLAN_ATTR_OFDM_SPACE_TIME_STREAM_OFFSETRFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLSRFMXWLAN_ATTR_OFDM_PE_DISAMBIGUITYRFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLEDRFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLSRFMXWLAN_ATTR_OFDM_RU_TYPERFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTHRFMXWLAN_ATTR_OFDM_IM_PILOTS_ENABLEDRFMXWLAN_ATTR_OFDM_UNEQUAL_MODULATION_ENABLEDRFMXWLAN_ATTR_OFDM_UNEQUAL_MODULATION_PATTERN_INDEX |
| RFMXWLAN_VAL_OFDM_HEADER_DECODING_ENABLED_TRUE | 1 (0x1) | Header information is obtained by decoding the header fields in the PPDU. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga1f18a230d2a5e8804190984f913d5b0b.html language=enus -->
## TOPIC 00020: RFMXWLAN_ATTR_OFDM_DCM_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga1f18a230d2a5e8804190984f913d5b0b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga1f18a230d2a5e8804190984f913d5b0b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals. SyntaxRFMXWLAN_ATTR_OFDM_DCM_ENABLEDNumeric ValueData TypeAccessApplies To10485793int32Read/WriteUserRemarks You can set this attribute to True only for MCS indices 0, 1, 3, or 4. This a

### RFMXWLAN_ATTR_OFDM_DCM_ENABLED

Specifies whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals.

#### Syntax

RFMXWLAN_ATTR_OFDM_DCM_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485793 | int32 | Read/Write | User |

#### Remarks

You can set this attribute to **True** only for MCS indices 0, 1, 3, or 4. This attribute is used to compute masks for unused tone error measurements.

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_DCM_ENABLED_FALSE | 0 (0x0) | Specifies that DCM is not applied to the data field for 802.11ax signals. |
| RFMXWLAN_VAL_OFDM_DCM_ENABLED_TRUE | 1 (0x1) | Specifies that DCM is applied to the data field for 802.11ax signals. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga2ef4a9cffba063a69f40aa9d36ab3e43.html language=enus -->
## TOPIC 00021: RFMXWLAN_ATTR_OFDM_FEC_CODING_TYPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga2ef4a9cffba063a69f40aa9d36ab3e43.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga2ef4a9cffba063a69f40aa9d36ab3e43.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of forward error correction (FEC) coding used. SyntaxRFMXWLAN_ATTR_OFDM_FEC_CODING_TYPENumeric ValueData TypeAccessApplies To10485810int32Read/WriteUserRemarks The value of this attribute is used to decode PLCP service data unit (PSDU) bits. This attribute is applicable only to 80

### RFMXWLAN_ATTR_OFDM_FEC_CODING_TYPE

Specifies the type of forward error correction (FEC) coding used.

#### Syntax

RFMXWLAN_ATTR_OFDM_FEC_CODING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485810 | int32 | Read/Write | User |

#### Remarks

The value of this attribute is used to decode PLCP service data unit (PSDU) bits. This attribute is applicable only to 802.11ax TB PPDU, 802.11be TB PPDU, and 802.11bn TB PPDU.

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute for 802.11ax TB PPDU, 802.11be TB PPDU, and 802.11bn TB PPDU.

The default value is **LDPC**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_FEC_CODING_TYPE_BCC | 0 (0x0) | The FEC coding type used is binary convolutional code (BCC). |
| RFMXWLAN_VAL_OFDM_FEC_CODING_TYPE_LDPC | 1 (0x1) | The FEC coding type used is low-density parity check (LDPC). |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga30742a7ecb61ab059b70b8c8a3a8fbc2.html language=enus -->
## TOPIC 00022: RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga30742a7ecb61ab059b70b8c8a3a8fbc2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga30742a7ecb61ab059b70b8c8a3a8fbc2.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of HE-SIG-B symbols. SyntaxRFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLSNumeric ValueData TypeAccessApplies To10485792int32Read/WriteN/ARemarks This attribute is applicable only to 802.11ax MU PPDU signals. You must configure this attribute if the RFMXWLAN_ATTR_OFDM_HEADER_DECOD

### RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS

Specifies the number of HE-SIG-B symbols.

#### Syntax

RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485792 | int32 | Read/Write | N/A |

#### Remarks

This attribute is applicable only to 802.11ax MU PPDU signals. You must configure this attribute if the [RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html) attribute is set to **False**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga4e91b1d217c51a9008caf5f71a25c437.html language=enus -->
## TOPIC 00023: RFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga4e91b1d217c51a9008caf5f71a25c437.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga4e91b1d217c51a9008caf5f71a25c437.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of SIG symbols. This attribute is applicable for 802.11be and 802.11bn MU PPDU signals. SyntaxRFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLSNumeric ValueData TypeAccessApplies To10485819int32Read/WriteN/ARemarks You must configure this attribute if the RFMXWLAN_ATTR_OFDM_HEADER_DECODI

### RFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLS

Specifies the number of SIG symbols. This attribute is applicable for 802.11be and 802.11bn MU PPDU signals.

#### Syntax

RFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485819 | int32 | Read/Write | N/A |

#### Remarks

You must configure this attribute if the [RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html) attribute is set to **False**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaae3e776235e4d74a02b804c5c378cd73.html language=enus -->
## TOPIC 00024: RFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaae3e776235e4d74a02b804c5c378cd73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaae3e776235e4d74a02b804c5c378cd73.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth across which RU subcarriers are distributed, when you set RFMXWLAN_ATTR_OFDM_RU_TYPE attribute to dRU. SyntaxRFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTHNumeric ValueData TypeAccessApplies To10485824float64Read/WriteUserRemarks This attribute is only applicable for 802.11bn TB P

### RFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTH

Specifies the bandwidth across which RU subcarriers are distributed, when you set [RFMXWLAN_ATTR_OFDM_RU_TYPE](group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaeb63b358173de04c0780b9d424eb1cb1.html) attribute to **dRU**.

#### Syntax

RFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485824 | float64 | Read/Write | User |

#### Remarks

This attribute is only applicable for 802.11bn TB PPDU signals. You must configure this attribute if [RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html) is set to **False**.

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **20M**.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gabbd74e3734a37a0dcfc3cbcf740f227a.html language=enus -->
## TOPIC 00025: RFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gabbd74e3734a37a0dcfc3cbcf740f227a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gabbd74e3734a37a0dcfc3cbcf740f227a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable SIG compression. This attribute is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals. SyntaxRFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLEDNumeric ValueData TypeAccessApplies To10485818int32Read/WriteN/ARemarks You must configure this attribute if the RFMXWLAN_

### RFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLED

Specifies whether to enable SIG compression. This attribute is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals.

#### Syntax

RFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485818 | int32 | Read/Write | N/A |

#### Remarks

You must configure this attribute if the [RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html) attribute is set to **False**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_SIG_COMPRESSION_ENABLED_FALSE | 0 (0x0) | Specifies that SIG compression is disabled. |
| RFMXWLAN_VAL_OFDM_SIG_COMPRESSION_ENABLED_TRUE | 1 (0x1) | Specifies that SIG compression is enabled. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaeb63b358173de04c0780b9d424eb1cb1.html language=enus -->
## TOPIC 00026: RFMXWLAN_ATTR_OFDM_RU_TYPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaeb63b358173de04c0780b9d424eb1cb1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaeb63b358173de04c0780b9d424eb1cb1.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU). SyntaxRFMXWLAN_ATTR_OFDM_RU_TYPENumeric ValueData TypeAccessApplies To10485823int32Read/WriteUserRemarks This attribute is only applicable for 802.11bn TB PPDU signals. Y

### RFMXWLAN_ATTR_OFDM_RU_TYPE

Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU).

#### Syntax

RFMXWLAN_ATTR_OFDM_RU_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485823 | int32 | Read/Write | User |

#### Remarks

This attribute is only applicable for 802.11bn TB PPDU signals. You must configure this attribute if [RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1ga0e0eea709f2ea0467d46e348bd2099cb.html) is set to **False**.

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **rRU**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_RU_TYPE_RRU | 0 (0x0) | Contiguous subcarriers are present in the RU. |
| RFMXWLAN_VAL_OFDM_RU_TYPE_DRU | 1 (0x1) | Non-contiguous subcarriers are present in the RU. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga0c14528d2557a830f1be2349a0b1076a.html language=enus -->
## TOPIC 00027: RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga0c14528d2557a830f1be2349a0b1076a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga0c14528d2557a830f1be2349a0b1076a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols. SyntaxRFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSETNumeric ValueData TypeAccessApplies To10502155int32Read/WriteN/ARemarks You do not need to use a selector stri

### RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET

Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502155 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga125bafd2be7bd99aad4906f9425c21f8.html language=enus -->
## TOPIC 00028: RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga125bafd2be7bd99aad4906f9425c21f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga125bafd2be7bd99aad4906f9425c21f8.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the waveform to be acquired for the OFDMModAcc measurement, when you set the RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH_MODE attribute to Manual. This value is expressed in seconds. SyntaxRFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTHNumeric ValueData TypeAccessApplies To105021

### RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH

Specifies the length of the waveform to be acquired for the OFDMModAcc measurement, when you set the [RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH_MODE](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1gae3c211e7dcc8e5332965988a68ec08ee.html) attribute to **Manual**. This value is expressed in seconds.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502154 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga37fa40dd4141501b3646751b373cedc9.html language=enus -->
## TOPIC 00029: RFMXWLAN_ATTR_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga37fa40dd4141501b3646751b373cedc9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga37fa40dd4141501b3646751b373cedc9.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal. SyntaxRFMXWLAN_ATTR_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHODNumeric ValueData TypeAccessApplies To10502270int32Read/WriteN/ARemarks You do not need to use a selector string to conf

### RFMXWLAN_ATTR_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD

Specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502270 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Preamble and Pilots**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_DISABLED | 0 (0x0) | Carrier frequency error is not computed and the corresponding result is returned as NaN. |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_INITIAL_PREAMBLE | 1 (0x1) | Initial short and long training fields in the PPDU are used. |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE | 2 (0x2) | Initial short and long training fields along with the SIGnal fields are used. |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS | 3 (0x3) | The initial short and long training fields, SIGnal fields, and the pilot subcarriers in the DATA field are used. |
| RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_PILOTS_AND_DATA | 4 (0x4) | The initial short and long training fields, SIGnal fields, and all the subcarriers in the DATA field are used. |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga3ed536c88e8e833b8c321405c6767387.html language=enus -->
## TOPIC 00030: RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga3ed536c88e8e833b8c321405c6767387.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga3ed536c88e8e833b8c321405c6767387.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit for EVM results. SyntaxRFMXWLAN_ATTR_OFDMMODACC_EVM_UNITNumeric ValueData TypeAccessApplies To10502152int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for info

### RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT

Specifies the unit for EVM results.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502152 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_PERCENTAGE | 0 (0x0) | The EVM results are returned as a percentage. |
| RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_DB | 1 (0x1) | The EVM results are returned in dB. |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga5600a8208d27e8f5d50b22f335d5d8b8.html language=enus -->
## TOPIC 00031: RFMXWLAN_ATTR_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga5600a8208d27e8f5d50b22f335d5d8b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga5600a8208d27e8f5d50b22f335d5d8b8.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether common pilot error is computed relative to only LTF or scaling by average CPE. SyntaxRFMXWLAN_ATTR_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCENumeric ValueData TypeAccessApplies To10502353int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXWLAN_ATTR_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE

Specifies whether common pilot error is computed relative to only LTF or scaling by average CPE.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502353 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Average CPE**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE_NONE | 0 (0x0) | Specifies that Common Pilot Error is computed relative to only LTF and no scaling is performed. |
| RFMXWLAN_VAL_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE_AVERAGE_CPE | 1 (0x1) | Specifies that Common Pilot Error is computed relative to LTF and scaling by average CPE is performed. |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga68f194e6ce78d9683b026df3fac5f5d3.html language=enus -->
## TOPIC 00032: RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_MODE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga68f194e6ce78d9683b026df3fac5f5d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1ga68f194e6ce78d9683b026df3fac5f5d3.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calibrates the noise floor of analyzer or performs the ModAcc measurement. SyntaxRFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_MODENumeric ValueData TypeAccessApplies To10502246int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attri

### RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_MODE

Specifies whether the measurement calibrates the noise floor of analyzer or performs the ModAcc measurement.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502246 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_MEASURE | 0 (0x0) | The OFDMModAcc measurement is performed on the acquired signal. |
| RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR | 1 (0x1) | The OFDMModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1gaba6ba3ac869184e995c554f2cbd549ab.html language=enus -->
## TOPIC 00033: RFMXWLAN_ATTR_OFDMMODACC_MAXIMUM_MEASUREMENT_LENGTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1gaba6ba3ac869184e995c554f2cbd549ab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1gaba6ba3ac869184e995c554f2cbd549ab.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of OFDM symbols that the measurement uses to compute EVM. This value is expressed in symbols. SyntaxRFMXWLAN_ATTR_OFDMMODACC_MAXIMUM_MEASUREMENT_LENGTHNumeric ValueData TypeAccessApplies To10502156int32Read/WriteN/ARemarks If the number of available data symbols (n) is g

### RFMXWLAN_ATTR_OFDMMODACC_MAXIMUM_MEASUREMENT_LENGTH

Specifies the maximum number of OFDM symbols that the measurement uses to compute EVM. This value is expressed in symbols.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_MAXIMUM_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502156 | int32 | Read/Write | N/A |

#### Remarks

If the number of available data symbols (n) is greater than the value that you specify (*m*), the measurement ignores (n-*m*) symbols from the end of the data field. If you set this attribute to -1, all symbols in the data field are used to compute the EVM.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 16.

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1gaf631aa0c8b0e0fdb7a84321bf8b81af8.html language=enus -->
## TOPIC 00034: RFMXWLAN_ATTR_OFDMMODACC_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1gaf631aa0c8b0e0fdb7a84321bf8b81af8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc_1gaf631aa0c8b0e0fdb7a84321bf8b81af8.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the OFDMModAcc measurement. SyntaxRFMXWLAN_ATTR_OFDMMODACC_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To10502148int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The nu

### RFMXWLAN_ATTR_OFDMMODACC_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the OFDMModAcc measurement.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502148 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging.html language=enus -->
## TOPIC 00035: Averaging

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsVector AveragingGroup membersNameDescriptionRFMXWLAN_ATTR_OFDMMODACC_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True. RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLEDSpecifies whether to enable avera

### Averaging

#### Groups

- Vector Averaging

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True. |
| RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED | Specifies whether to enable averaging for OFDMModAcc measurements. |
| RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_TYPE | Specifies the averaging type for the OFDMModAcc measurement. |

#### Attachments

None

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1gaa7a117c3f9a82e3edba4b4a3306d2b51.html language=enus -->
## TOPIC 00036: RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_TYPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1gaa7a117c3f9a82e3edba4b4a3306d2b51.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1gaa7a117c3f9a82e3edba4b4a3306d2b51.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for the OFDMModAcc measurement. SyntaxRFMXWLAN_ATTR_OFDMMODACC_AVERAGING_TYPENumeric ValueData TypeAccessApplies To10502316int32Read/WriteN/ARemarks This attribute is considered only when you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True and when y

### RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_TYPE

Specifies the averaging type for the OFDMModAcc measurement.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502316 | int32 | Read/Write | N/A |

#### Remarks

This attribute is considered only when you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True** and when you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_COUNT](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga2884c352a353d95f6285cf95f4f1adc8.html) attribute is to a value greater than 1.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_AVERAGING_TYPE_RMS | 0 (0x0) | The OFDMModAcc measurement is performed on I/Q data acquired in each averaging count. The scalar results and traces are linearly averaged over the averaging count. |
| RFMXWLAN_VAL_OFDMMODACC_AVERAGING_TYPE_VECTOR | 5 (0x5) | The acquired I/Q data is averaged across averaging count after aligning the data in time and phase using the RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED and RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED properties, respectively. The averaged I/Q data is used for the measurement. Refer to the OFDMModAcc Vector Averaging concept topic for more information.Note You must ensure that the frequency reference is locked between the generator and the analyzer. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging__vector__averaging.html language=enus -->
## TOPIC 00037: Vector Averaging

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging__vector__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging__vector__averaging.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLEDSpecifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLEDSpecifies whether to enable time

### Vector Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED | Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. |
| RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED | Specifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions. |

#### Attachments

None

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__iq__impairments_1gab170bf19e31c30a30f9c95b121533fff.html language=enus -->
## TOPIC 00038: RFMXWLAN_ATTR_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__iq__impairments_1gab170bf19e31c30a30f9c95b121533fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__iq__impairments_1gab170bf19e31c30a30f9c95b121533fff.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable I/Q quadrature error correction. SyntaxRFMXWLAN_ATTR_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLEDNumeric ValueData TypeAccessApplies To10502173int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signa

### RFMXWLAN_ATTR_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED

Specifies whether to enable I/Q quadrature error correction.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502173 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_FALSE | 0 (0x0) | I/Q quadrature error correction is disabled. |
| RFMXWLAN_VAL_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_TRUE | 1 (0x1) | I/Q quadrature error correction is enabled. |

Parent topic:

I/Q Impairments

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__optimize__dynamic__range__for__evm.html language=enus -->
## TOPIC 00039: Optimize Dynamic Range for EVM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__optimize__dynamic__range__for__evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__optimize__dynamic__range__for__evm.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLEDSpecifies whether to optimize the analyzer's dynamic range for the EVM measurement. RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGINSpecifies the margin above the reference level you sp

### Optimize Dynamic Range for EVM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED | Specifies whether to optimize the analyzer's dynamic range for the EVM measurement. |
| RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGIN | Specifies the margin above the reference level you specify when you set the RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED attribute to True. This value is expressed in dB. |

#### Attachments

None

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__optimize__dynamic__range__for__evm_1ga16d215aa7c458d5290ab457f7cd3b5e8.html language=enus -->
## TOPIC 00040: RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGIN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__optimize__dynamic__range__for__evm_1ga16d215aa7c458d5290ab457f7cd3b5e8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__optimize__dynamic__range__for__evm_1ga16d215aa7c458d5290ab457f7cd3b5e8.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin above the reference level you specify when you set the RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED attribute to True. This value is expressed in dB. SyntaxRFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGINNumeric ValueData TypeAccessApplies To1050

### RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGIN

Specifies the margin above the reference level you specify when you set the [RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__optimize__dynamic__range__for__evm_1gab2f0235bcba8590c9815ed875e36ab76.html) attribute to **True**. This value is expressed in dB.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502269 | float64 | Read/Write | N/A |

#### Remarks

When the property's value 0, the dynamic range is optimized. When you set a positive value to the attribute, the dynamic range reduces from the optimized dynamic range. You can use this attribute to avoid ADC and onboard signal processing (OSP) overflows.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Optimize Dynamic Range for EVM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__power.html language=enus -->
## TOPIC 00041: Power

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__power.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__power.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_OFDMMODACC_POWER_CUSTOM_GATE_START_TIMESpecifies the start time of the custom power gate. This value is expressed in seconds. RFMXWLAN_ATTR_OFDMMODACC_POWER_CUSTOM_GATE_STOP_TIMESpecifies the stop time of the custom power gate, and must be greater

### Power

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_OFDMMODACC_POWER_CUSTOM_GATE_START_TIME | Specifies the start time of the custom power gate. This value is expressed in seconds. |
| RFMXWLAN_ATTR_OFDMMODACC_POWER_CUSTOM_GATE_STOP_TIME | Specifies the stop time of the custom power gate, and must be greater than the corresponding RFMXWLAN_ATTR_OFDMMODACC_POWER_CUSTOM_GATE_START_TIME attribute. This value is expressed in seconds. |
| RFMXWLAN_ATTR_OFDMMODACC_POWER_MEASUREMENT_ENABLED | Specifies whether power measurements are performed. |
| RFMXWLAN_ATTR_OFDMMODACC_POWER_NUMBER_OF_CUSTOM_GATES | Specifies the number of custom gates for power measurement. |

#### Attachments

None

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga0930a90fc3a056b37f1f2bf9e6b6af24.html language=enus -->
## TOPIC 00042: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga0930a90fc3a056b37f1f2bf9e6b6af24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga0930a90fc3a056b37f1f2bf9e6b6af24.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_MAXIMUMNumeric ValueData TypeAccessApplies To10502304float64Read-OnlySegment

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_MAXIMUM

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502304 | float64 | Read-Only | Segment |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga119d505b894ad683d9dfd31ea5aba933.html language=enus -->
## TOPIC 00043: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga119d505b894ad683d9dfd31ea5aba933.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga119d505b894ad683d9dfd31ea5aba933.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. This value is expressed in dB. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MEANNumeric ValueData TypeAccessApplies To10502187float64Read-OnlyCh

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MEAN

Returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. This value is expressed in dB.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502187 | float64 | Read-Only | Chain |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the relative I/Q origin offset computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga3ff60c58f68b9603c42509de754f4c0d.html language=enus -->
## TOPIC 00044: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga3ff60c58f68b9603c42509de754f4c0d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga3ff60c58f68b9603c42509de754f4c0d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MAXIMUMNumeric ValueData TypeAccessApplies To10502298float64Read-OnlyStream

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MAXIMUM

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502298 | float64 | Read-Only | Stream |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga62da5312dcfeb887fda5da46875086c7.html language=enus -->
## TOPIC 00045: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_RMS_EVM_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga62da5312dcfeb887fda5da46875086c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga62da5312dcfeb887fda5da46875086c7.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of subcarriers in the UHR-SIG symbol. This value is expressed as a percentage or in dB. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To10502354float64Read-OnlyN/ARemarks When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_RMS_EVM_MEAN

Returns the RMS EVM of subcarriers in the UHR-SIG symbol. This value is expressed as a percentage or in dB.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502354 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga69f14cc5001ad48677fb47ce88f08249.html language=enus -->
## TOPIC 00046: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_RMS_EVM_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga69f14cc5001ad48677fb47ce88f08249.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga69f14cc5001ad48677fb47ce88f08249.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of subcarriers in the SIG symbol. This value is expressed as a percentage or in dB. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To10502332float64Read-OnlyN/ARemarks When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribut

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_RMS_EVM_MEAN

Returns the RMS EVM of subcarriers in the SIG symbol. This value is expressed as a percentage or in dB.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502332 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga6d2e34ad103ee5ad0a9ee76341586b88.html language=enus -->
## TOPIC 00047: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_EHT_SIG_RMS_EVM_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga6d2e34ad103ee5ad0a9ee76341586b88.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga6d2e34ad103ee5ad0a9ee76341586b88.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_EHT_SIG_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To10502335float64Read-OnlyN/ARemarks When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_EHT_SIG_RMS_EVM_MEAN

Returns the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_EHT_SIG_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502335 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga922430808482c425b44e02d70ee44f10.html language=enus -->
## TOPIC 00048: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_ELR_SIG_RMS_EVM_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga922430808482c425b44e02d70ee44f10.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results_1ga922430808482c425b44e02d70ee44f10.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of subcarriers in the ELR-SIG symbol. This value is expressed as a percentage or in dB. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_ELR_SIG_RMS_EVM_MEANNumeric ValueData TypeAccessApplies To10502356float64Read-OnlyN/ARemarks When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_ELR_SIG_RMS_EVM_MEAN

Returns the RMS EVM of subcarriers in the ELR-SIG symbol. This value is expressed as a percentage or in dB.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_ELR_SIG_RMS_EVM_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502356 | float64 | Read-Only | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__channel__matrix__power_1gad29b1cdb8a064978b724c6f7b242ef2e.html language=enus -->
## TOPIC 00049: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_STREAM_CROSS_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__channel__matrix__power_1gad29b1cdb8a064978b724c6f7b242ef2e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__channel__matrix__power_1gad29b1cdb8a064978b724c6f7b242ef2e.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stream cross power. The cross power for chain k stream m is the power contribution of stream m in chain k. This value is expressed in dB. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_STREAM_CROSS_POWER_MEANNumeric ValueData TypeAccessApplies To10502376float64Read-OnlyStreamRemarks When y

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_STREAM_CROSS_POWER_MEAN

Returns the stream cross power. The cross power for chain k stream *m* is the power contribution of stream *m* in chain k. This value is expressed in dB.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_STREAM_CROSS_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502376 | float64 | Read-Only | Stream |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the chain stream cross power results computed for each averaging count.

Use "segment<n>/chain<k>/stream<<i>m</i>>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Channel Matrix Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga03a7df56df6d02dbb726fbb269a0c872.html language=enus -->
## TOPIC 00050: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga03a7df56df6d02dbb726fbb269a0c872.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga03a7df56df6d02dbb726fbb269a0c872.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the VHT-SIG-B field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502217float64Read-OnlyChainRemarks This result is applicable only to 802.11ac signals. When you set the RFMX

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_PEAK_POWER_MAXIMUM

Returns the peak power of the VHT-SIG-B field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502217 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11ac signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the VHT-SIG-B field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga258af6b102a02f382a36eb1b72fd170d.html language=enus -->
## TOPIC 00051: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga258af6b102a02f382a36eb1b72fd170d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga258af6b102a02f382a36eb1b72fd170d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the VHT-SIG-B field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502216float64Read-OnlyChainRemarks This result is applicable only to 802.11ac signals. When you set the R

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_AVERAGE_POWER_MEAN

Returns the average power of the VHT-SIG-B field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502216 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11ac signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the VHT-SIG-B field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga45cd5ed6b475cd6eff4dfdf2791b7f9f.html language=enus -->
## TOPIC 00052: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_B_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga45cd5ed6b475cd6eff4dfdf2791b7f9f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga45cd5ed6b475cd6eff4dfdf2791b7f9f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the HE-SIG-B field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_B_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502219float64Read-OnlyChainRemarks This result is applicable only to 802.11ax signals. When you set the RFMXWL

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_B_PEAK_POWER_MAXIMUM

Returns the peak power of the HE-SIG-B field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_B_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502219 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11ax signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the HE-SIG-B field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga5b1215cc2601f0a9725c5f898f43419b.html language=enus -->
## TOPIC 00053: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga5b1215cc2601f0a9725c5f898f43419b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga5b1215cc2601f0a9725c5f898f43419b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the PPDU. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502240float64Read-OnlyChainRemarks When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this at

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_AVERAGE_POWER_MEAN

Returns the average power of the PPDU. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502240 | float64 | Read-Only | Chain |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the PPDU average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga713d55b75c1ba230fbd70ad199fad88b.html language=enus -->
## TOPIC 00054: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga713d55b75c1ba230fbd70ad199fad88b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga713d55b75c1ba230fbd70ad199fad88b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the custom gate. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502242float64Read-OnlyGateRemarks When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_AVERAGE_POWER_MEAN

Returns the average power of the custom gate. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502242 | float64 | Read-Only | Gate |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the custom gate average power results computed for each averaging count.

Use "gate<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga7510ab0e941db11edd8ceabe6a87b4d1.html language=enus -->
## TOPIC 00055: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_U_SIG_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga7510ab0e941db11edd8ceabe6a87b4d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga7510ab0e941db11edd8ceabe6a87b4d1.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the U-SIG field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_U_SIG_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502337float64Read-OnlyChainRemarks This result is applicable only to 802.11be signals. When you set the RFMXWLAN_ATT

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_U_SIG_PEAK_POWER_MAXIMUM

Returns the peak power of the U-SIG field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_U_SIG_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502337 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11be signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the U-SIG field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga88f0bfe6f62addefd2df063237e923fc.html language=enus -->
## TOPIC 00056: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_ELTF_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga88f0bfe6f62addefd2df063237e923fc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga88f0bfe6f62addefd2df063237e923fc.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HT-ELTF field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_ELTF_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502230float64Read-OnlyChainRemarks This result is applicable only to 802.11n signals. When you set the RFMXWL

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_ELTF_AVERAGE_POWER_MEAN

Returns the average power of the HT-ELTF field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_ELTF_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502230 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11n signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the HT-ELTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga9400bdd8e6e59e4ab03414227facb601.html language=enus -->
## TOPIC 00057: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_DLTF_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga9400bdd8e6e59e4ab03414227facb601.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1ga9400bdd8e6e59e4ab03414227facb601.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HT-DLTF. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_DLTF_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502228float64Read-OnlyChainRemarks This result is applicable only to 802.11n signals. When you set the RFMXWLAN_ATT

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_DLTF_AVERAGE_POWER_MEAN

Returns the average power of the HT-DLTF. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_DLTF_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502228 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11n signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the HT-DLTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gab676314c34e8f4338cfe5060640122a1.html language=enus -->
## TOPIC 00058: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_STF_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gab676314c34e8f4338cfe5060640122a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gab676314c34e8f4338cfe5060640122a1.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the HT-STF field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_STF_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502221float64Read-OnlyChainRemarks This result is applicable only to 802.11n signals. When you set the RFMXWLAN_AT

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_STF_PEAK_POWER_MAXIMUM

Returns the peak power of the HT-STF field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_STF_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502221 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11n signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the HT-STF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gabec6f110a875ef284b22b94cb59cd852.html language=enus -->
## TOPIC 00059: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_STF_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gabec6f110a875ef284b22b94cb59cd852.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gabec6f110a875ef284b22b94cb59cd852.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HE-STF field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_STF_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502226float64Read-OnlyChainRemarks This result is applicable only to 802.11ax signals. When you set the RFMXWLA

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_STF_AVERAGE_POWER_MEAN

Returns the average power of the HE-STF field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_STF_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502226 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11ax signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the HE-STF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac5aa2142f7dd23453db1c0a979e37264.html language=enus -->
## TOPIC 00060: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac5aa2142f7dd23453db1c0a979e37264.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac5aa2142f7dd23453db1c0a979e37264.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the PPDU. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502241float64Read-OnlyChainRemarks When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this attri

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_PEAK_POWER_MAXIMUM

Returns the peak power of the PPDU. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502241 | float64 | Read-Only | Chain |

#### Remarks

When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the PPDU peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac7c521c19c33eec0a23db3330d1c532b.html language=enus -->
## TOPIC 00061: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac7c521c19c33eec0a23db3330d1c532b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac7c521c19c33eec0a23db3330d1c532b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the ELR-MARK field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502366float64Read-OnlyChainRemarks This result is applicable only to 802.11bn signals. When you set the RFM

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_AVERAGE_POWER_MEAN

Returns the average power of the ELR-MARK field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502366 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11bn signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the ELR-MARK field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac7f62b2007d157aa36abf75fe90d4f01.html language=enus -->
## TOPIC 00062: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_A_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac7f62b2007d157aa36abf75fe90d4f01.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gac7f62b2007d157aa36abf75fe90d4f01.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the VHT-SIG-A field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_A_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502212float64Read-OnlyChainRemarks This result is applicable only to 802.11ac signals. When you set the R

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_A_AVERAGE_POWER_MEAN

Returns the average power of the VHT-SIG-A field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_A_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502212 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11ac signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the VHT-SIG-A field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gad1bf60ca0ff0bdba1d11919acc517fc3.html language=enus -->
## TOPIC 00063: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gad1bf60ca0ff0bdba1d11919acc517fc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gad1bf60ca0ff0bdba1d11919acc517fc3.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the ELR-MARK field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502367float64Read-OnlyChainRemarks This result is applicable only to 802.11bn signals. When you set the RFMXWL

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_PEAK_POWER_MAXIMUM

Returns the peak power of the ELR-MARK field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502367 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11bn signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the ELR-MARK field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gadd0052e03aebcb6dfa9f3795ab7c5c5f.html language=enus -->
## TOPIC 00064: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_STF_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gadd0052e03aebcb6dfa9f3795ab7c5c5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gadd0052e03aebcb6dfa9f3795ab7c5c5f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the UHR-STF field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_STF_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502359float64Read-OnlyChainRemarks This result is applicable only to 802.11bn signals. When you set the RFMXWLAN

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_STF_PEAK_POWER_MAXIMUM

Returns the peak power of the UHR-STF field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_STF_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502359 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11bn signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the UHR-STF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gaf3b30fbad150a32440f858766df2c41c.html language=enus -->
## TOPIC 00065: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_AVERAGE_POWER_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gaf3b30fbad150a32440f858766df2c41c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gaf3b30fbad150a32440f858766df2c41c.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the UHR-SIG field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_AVERAGE_POWER_MEANNumeric ValueData TypeAccessApplies To10502362float64Read-OnlyChainRemarks This result is applicable only to 802.11bn signals. When you set the RFMXW

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_AVERAGE_POWER_MEAN

Returns the average power of the UHR-SIG field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_AVERAGE_POWER_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502362 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11bn signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the mean of the UHR-SIG field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gaf9929f6e800bd49907f66969573ca1ce.html language=enus -->
## TOPIC 00066: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_PEAK_POWER_MAXIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gaf9929f6e800bd49907f66969573ca1ce.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__power_1gaf9929f6e800bd49907f66969573ca1ce.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the UHR-SIG field. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_PEAK_POWER_MAXIMUMNumeric ValueData TypeAccessApplies To10502363float64Read-OnlyChainRemarks This result is applicable only to 802.11bn signals. When you set the RFMXWLAN

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_PEAK_POWER_MAXIMUM

Returns the peak power of the UHR-SIG field. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_PEAK_POWER_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502363 | float64 | Read-Only | Chain |

#### Remarks

This result is applicable only to 802.11bn signals. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this attribute returns the maximum of the UHR-SIG field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Power

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga33d2231a024ffe5804296898e7915d39.html language=enus -->
## TOPIC 00067: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SPACE_TIME_STREAMS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga33d2231a024ffe5804296898e7915d39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga33d2231a024ffe5804296898e7915d39.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of space time streams. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SPACE_TIME_STREAMSNumeric ValueData TypeAccessApplies To10502201int32Read-OnlyUserRemarks The value is decoded for various standards as follows:StandardDerivation802.11nDerived from the MCS field and STBC fiel

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SPACE_TIME_STREAMS

Returns the number of space time streams.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SPACE_TIME_STREAMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502201 | int32 | Read-Only | User |

#### Remarks

The value is decoded for various standards as follows:

| Standard | Derivation |
| --- | --- |
| 802.11n | Derived from the MCS field and STBC field of the HT-SIG. |
| 802.11ac | Derived from the NSTS field of the VHT-SIG-A. |
| 802.11ax | Derived from the HE-SIG-A for HE SU PPDU and HE Extended Range PPDU. Derived from the HE-SIG-B for HE MU PPDU. |
| 802.11be | Derived from the EHT-SIG for EHT MU PPDU. |
| 802.11bn | Derived from the UHR-SIG for UHR MU PPDU. |

For all other configurations, the attribute returns the value of 1.

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga45201a559b8d596fd63cbad97c740f3e.html language=enus -->
## TOPIC 00068: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IM_PILOTS_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga45201a559b8d596fd63cbad97c740f3e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga45201a559b8d596fd63cbad97c740f3e.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether interference mitigating pilots are present. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_IM_PILOTS_ENABLEDNumeric ValueData TypeAccessApplies To10502372int32Read-OnlyN/ARemarks This result is applicable only to 802.11bn MU PPDU signals.You do not need to use a selector string to read this

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IM_PILOTS_ENABLED

Returns whether interference mitigating pilots are present.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IM_PILOTS_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502372 | int32 | Read-Only | N/A |

#### Remarks

This result is applicable only to 802.11bn MU PPDU signals.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_IM_PILOTS_ENABLED_FALSE | 0 (0x0) | Indicates that interference mitigating pilots are absent. |
| RFMXWLAN_VAL_OFDMMODACC_IM_PILOTS_ENABLED_TRUE | 1 (0x1) | Indicates that interference mitigating pilots are present. |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga4cb4fa93a88496b330eb5069ed7044ec.html language=enus -->
## TOPIC 00069: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_DISTRIBUTION_BANDWIDTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga4cb4fa93a88496b330eb5069ed7044ec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga4cb4fa93a88496b330eb5069ed7044ec.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth across which RU Subcarriers are distributed for a user. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_DISTRIBUTION_BANDWIDTHNumeric ValueData TypeAccessApplies To10502370float64Read-OnlyUserRemarks This result is applicable for 802.11bn TB PPDU signals when RU Type is dRU. For 802.11b

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_DISTRIBUTION_BANDWIDTH

Returns the bandwidth across which RU Subcarriers are distributed for a user.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_DISTRIBUTION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502370 | float64 | Read-Only | User |

#### Remarks

This result is applicable for 802.11bn TB PPDU signals when RU Type is dRU. For 802.11bn TB PPDU signals, this attribute returns the same value as the [RFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTH](group____root__ni_r_fmx_w_l_a_n__attributes__ofdm__advanced_1gaae3e776235e4d74a02b804c5c378cd73.html) attribute.

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga8325a73f279bfed8ae1dde64b21d6d75.html language=enus -->
## TOPIC 00070: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SIG_SYMBOLS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga8325a73f279bfed8ae1dde64b21d6d75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1ga8325a73f279bfed8ae1dde64b21d6d75.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SIG_SYMBOLSNumeric ValueData TypeAccessApplies To10502375int32Read-OnlyN/A

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SIG_SYMBOLS

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SIG_SYMBOLS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502375 | int32 | Read-Only | N/A |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gaa57341cd3331a5fb8939433cc4fadb8a.html language=enus -->
## TOPIC 00071: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PPDU_TYPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gaa57341cd3331a5fb8939433cc4fadb8a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gaa57341cd3331a5fb8939433cc4fadb8a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the PPDU type of the measured signal. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_PPDU_TYPENumeric ValueData TypeAccessApplies To10502193int32Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector String topic

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PPDU_TYPE

Returns the PPDU type of the measured signal.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PPDU_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502193 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_NON_HT | 0 (0x0) | Specifies an 802.11a, 802.11j, or 802.11p PPDU type, or 802.11n, 802.11ac, or 802.11ax PPDU type when operating in the Non-HT mode. |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_MIXED | 1 (0x1) | Specifies the HT-Mixed PPDU (802.11n) type. |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_GREENFIELD | 2 (0x2) | Specifies the HT-Greenfield PPDU (802.11n) type. |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_SU | 3 (0x3) | Specifies the VHT SU PPDU type if you set the RFMXWLAN_ATTR_STANDARD attribute to 802.11ac or the HE SU PPDU type if you set the Standard attribute to 802.11ax. |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_MU | 4 (0x4) | Specifies the VHT MU PPDU type if you set the Standard attribute to 802.11ac, the HE MU PPDU type if you set the Standard attribute to 802.11ax, or the EHT MU PPDU type if you set the Standard attribute to 802.11be. |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_EXTENDED_RANGE_SU | 5 (0x5) | Specifies the HE Extended Range SU PPDU (802.11ax) type. |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_TRIGGER_BASED | 6 (0x6) | Specifies the HE TB PPDU if you set the Standard attribute to 802.11ax , the EHT TB PPDU if you set the Standard attribute to 802.11be or the UHR TB PPDU if you set the Standard attribute to 802.11bn . |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_ELR | 7 (0x7) |  |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gac7b7797681c81065e5ee7cb6d1430539.html language=enus -->
## TOPIC 00072: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_LTF_SIZE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gac7b7797681c81065e5ee7cb6d1430539.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gac7b7797681c81065e5ee7cb6d1430539.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the HE-LTF size, EHT-LTF or UHR-LTF size when you set the RFMXWLAN_ATTR_STANDARD attribute to 802.11ax, 802.11be, or 802.11bn, respectively. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_LTF_SIZENumeric ValueData TypeAccessApplies To10502200int32Read-OnlyN/ARemarks This result is applicable only to

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_LTF_SIZE

Returns the HE-LTF size, EHT-LTF or UHR-LTF size when you set the [RFMXWLAN_ATTR_STANDARD](group____root__ni_r_fmx_w_l_a_n__attributes_1ga913b590b9053ced995f137a7e81dd441.html) attribute to **802.11ax**, **802.11be**, or **802.11bn**, respectively.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_LTF_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502200 | int32 | Read-Only | N/A |

#### Remarks

This result is applicable only to 802.11ax, 802.11be and 802.11bn signals. This value is decoded from the HE-SIG-A field when you set the Standard attribute to **802.11ax**, from the EHT-SIG field when you set the Standard attribute to **802.11be**, and from the UHR-SIG field when you set the Standard attribute to **802.11bn**.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_4X | 0 (0x0) | Specifies that the LTF symbol size is 4x. |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_2X | 1 (0x1) | Specifies that the LTF symbol size is 2x. |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_1X | 2 (0x2) | Specifies that the LTF symbol size is 1x. |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_NOT_APPLICABLE | -1 (-0x1) | Specifies that the LTF Size is invalid for the current waveform. |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gadbd343bfd3933e0ff81c51ee74f7bf58.html language=enus -->
## TOPIC 00073: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SCRAMBLER_SEED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gadbd343bfd3933e0ff81c51ee74f7bf58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gadbd343bfd3933e0ff81c51ee74f7bf58.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected initial state of the scrambler, which is used to scramble the data bits in the device under test (DUT). RFmx uses the same seed to descramble the received bit-sequence. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_SCRAMBLER_SEEDNumeric ValueData TypeAccessApplies To10502344int32Read-O

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SCRAMBLER_SEED

Returns the detected initial state of the scrambler, which is used to scramble the data bits in the device under test (DUT). RFmx uses the same seed to descramble the received bit-sequence.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SCRAMBLER_SEED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502344 | int32 | Read-Only | User |

#### Remarks

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for MU PPDU signals.

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gae0cf0232f1ceeb8202396358669f96a2.html language=enus -->
## TOPIC 00074: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FEC_CODING_TYPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gae0cf0232f1ceeb8202396358669f96a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gae0cf0232f1ceeb8202396358669f96a2.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FEC coding type for a specified user. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_FEC_CODING_TYPENumeric ValueData TypeAccessApplies To10502314int32Read-OnlyUserRemarks Use "user<n>" as the Selector String to read this result for MU and TB PPDU signals.NameValueDescriptionRFMXWLAN_VAL_OFDMMOD

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FEC_CODING_TYPE

Returns the FEC coding type for a specified user.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FEC_CODING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502314 | int32 | Read-Only | User |

#### Remarks

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for MU and TB PPDU signals.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_FEC_CODING_TYPE_BCC | 0 (0x0) | Indicates that the FEC coding type is BCC. |
| RFMXWLAN_VAL_OFDMMODACC_FEC_CODING_TYPE_LDPC | 1 (0x1) | Indicates that the FEC coding type is LDPC. |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gafa3780c342f4688aeb6fe65513905492.html language=enus -->
## TOPIC 00075: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_2XLDPC_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gafa3780c342f4688aeb6fe65513905492.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gafa3780c342f4688aeb6fe65513905492.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether 2xLDPC is enabled for a specified user. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_2XLDPC_ENABLEDNumeric ValueData TypeAccessApplies To10502371int32Read-OnlyUserRemarks Use "user<n>" as the Selector String to read this result for 802.11bn MU and TB PPDU signals.NameValueDescriptionRFMXWL

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_2XLDPC_ENABLED

Returns whether 2xLDPC is enabled for a specified user.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_2XLDPC_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502371 | int32 | Read-Only | User |

#### Remarks

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for 802.11bn MU and TB PPDU signals.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_2XLDPC_ENABLED_FALSE | 0 (0x0) | Indicates that 2xLDPC is disabled for the specified user. |
| RFMXWLAN_VAL_OFDMMODACC_2XLDPC_ENABLED_TRUE | 1 (0x1) | Indicates that 2xLDPC is enabled for the specified user. |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gafeea91016d8f90d149ed99caa5e00c80.html language=enus -->
## TOPIC 00076: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_CRC_STATUS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gafeea91016d8f90d149ed99caa5e00c80.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info_1gafeea91016d8f90d149ed99caa5e00c80.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the cyclic redundancy check (CRC) has passed for the UHR-SIG field of the 802.11bn waveform. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_CRC_STATUSNumeric ValueData TypeAccessApplies To10502355int32Read-OnlyN/ARemarks You do not need to use a selector string to read this result fo

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_CRC_STATUS

Returns whether the cyclic redundancy check (CRC) has passed for the UHR-SIG field of the 802.11bn waveform.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_CRC_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502355 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_UHR_SIG_CRC_STATUS_NOT_APPLICABLE | -1 (-0x1) | Returns that the UHR-SIG CRC is invalid for the current waveform. |
| RFMXWLAN_VAL_OFDMMODACC_UHR_SIG_CRC_STATUS_FAIL | 0 (0x0) | Returns that the UHR-SIG CRC failed. |
| RFMXWLAN_VAL_OFDMMODACC_UHR_SIG_CRC_STATUS_PASS | 1 (0x1) | Returns that the UHR-SIG CRC passed. |

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation.html language=enus -->
## TOPIC 00077: Unequal Modulation

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLEDReturns whether unequal modulation is enabled for a specified user. RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEXReturns unequal modulation pattern for a specified user. AttachmentsNo

### Unequal Modulation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLED | Returns whether unequal modulation is enabled for a specified user. |
| RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEX | Returns unequal modulation pattern for a specified user. |

#### Attachments

None

Parent topic:

PPDU Info

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation_1ga0b0e765bc4a269e18b3daa6e97abad75.html language=enus -->
## TOPIC 00078: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEX

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation_1ga0b0e765bc4a269e18b3daa6e97abad75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation_1ga0b0e765bc4a269e18b3daa6e97abad75.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns unequal modulation pattern for a specified user. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEXNumeric ValueData TypeAccessApplies To10502374int32Read-OnlyUserRemarks Use "user<n>" as the Selector String to read this result for 802.11bn MU PPDU signals.

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEX

Returns unequal modulation pattern for a specified user.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502374 | int32 | Read-Only | User |

#### Remarks

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for 802.11bn MU PPDU signals.

Parent topic:

Unequal Modulation

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation_1ga7dddf819207f657d7deb017dda55d81a.html language=enus -->
## TOPIC 00079: RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation_1ga7dddf819207f657d7deb017dda55d81a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__results__ppdu__info__unequal__modulation_1ga7dddf819207f657d7deb017dda55d81a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether unequal modulation is enabled for a specified user. SyntaxRFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLEDNumeric ValueData TypeAccessApplies To10502373int32Read-OnlyUserRemarks Use "user<n>" as the Selector String to read this result for 802.11bn MU PPDU signals.NameValue

### RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLED

Returns whether unequal modulation is enabled for a specified user.

#### Syntax

RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10502373 | int32 | Read-Only | User |

#### Remarks

Use "user<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result for 802.11bn MU PPDU signals.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_OFDMMODACC_UNEQUAL_MODULATION_ENABLED_FALSE | 0 (0x0) | Indicates that unequal modulation is disabled for the specified user. |
| RFMXWLAN_VAL_OFDMMODACC_UNEQUAL_MODULATION_ENABLED_TRUE | 1 (0x1) | Indicates that unequal modulation is enabled for the specified user. |

Parent topic:

Unequal Modulation

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__powerramp_1ga195a128dbdcdc2bcf770aba5b70ac0a5.html language=enus -->
## TOPIC 00080: RFMXWLAN_ATTR_POWERRAMP_ALL_TRACES_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__powerramp_1ga195a128dbdcdc2bcf770aba5b70ac0a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__powerramp_1ga195a128dbdcdc2bcf770aba5b70ac0a5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable all the traces computed by the PowerRamp measurement. SyntaxRFMXWLAN_ATTR_POWERRAMP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To10493974int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signa

### RFMXWLAN_ATTR_POWERRAMP_ALL_TRACES_ENABLED

Specifies whether to enable all the traces computed by the PowerRamp measurement.

#### Syntax

RFMXWLAN_ATTR_POWERRAMP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10493974 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__powerramp_1gaf2480e3bec522be24e1eca0c1cbfde3d.html language=enus -->
## TOPIC 00081: RFMXWLAN_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__powerramp_1gaf2480e3bec522be24e1eca0c1cbfde3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__powerramp_1gaf2480e3bec522be24e1eca0c1cbfde3d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for PowerRamp measurement. SyntaxRFMXWLAN_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To10493975int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number o

### RFMXWLAN_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for PowerRamp measurement.

#### Syntax

RFMXWLAN_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10493975 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__averaging_1ga9b81bc5b1bc963299090e49ab334ccbb.html language=enus -->
## TOPIC 00082: RFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__averaging_1ga9b81bc5b1bc963299090e49ab334ccbb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__averaging_1ga9b81bc5b1bc963299090e49ab334ccbb.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if averaging is enabled for PowerRamp measurements. SyntaxRFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To10493972int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to

### RFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLED

Specifies if averaging is enabled for PowerRamp measurements.

#### Syntax

RFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10493972 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_POWERRAMP_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXWLAN_VAL_POWERRAMP_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement uses the RFMXWLAN_ATTR_POWERRAMP_AVERAGING_COUNT attribute as the number of acquisitions using which the results are averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__results.html language=enus -->
## TOPIC 00083: Results

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__results.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEANReturns the power-ramp fall time of the burst. This value is expressed in seconds. RFMXWLAN_ATTR_POWERRAMP_RESULTS_RISE_TIME_MEANReturns the power-ramp rise time of the burst. This value is expressed in seconds. Atta

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEAN | Returns the power-ramp fall time of the burst. This value is expressed in seconds. |
| RFMXWLAN_ATTR_POWERRAMP_RESULTS_RISE_TIME_MEAN | Returns the power-ramp rise time of the burst. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__results_1ga6b9c4e22b1b7b7e5cb608b3792a4e67a.html language=enus -->
## TOPIC 00084: RFMXWLAN_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEAN

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__results_1ga6b9c4e22b1b7b7e5cb608b3792a4e67a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__results_1ga6b9c4e22b1b7b7e5cb608b3792a4e67a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power-ramp fall time of the burst. This value is expressed in seconds. SyntaxRFMXWLAN_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEANNumeric ValueData TypeAccessApplies To10493977float64Read-OnlyN/ARemarks This measurement is performed in accordance with section 16.3.7.7 of IEEE Standard 802.11-20

### RFMXWLAN_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEAN

Returns the power-ramp fall time of the burst. This value is expressed in seconds.

#### Syntax

RFMXWLAN_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10493977 | float64 | Read-Only | N/A |

#### Remarks

This measurement is performed in accordance with section 16.3.7.7 of *IEEE Standard 802.11-2016*.

When you set the [RFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__powerramp__averaging_1ga9b81bc5b1bc963299090e49ab334ccbb.html) attribute to **True**, this attribute returns the mean of the fall time results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem_1ga54a85e2fcb08a6557e7d6dfd8ad4ed1d.html language=enus -->
## TOPIC 00085: RFMXWLAN_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem_1ga54a85e2fcb08a6557e7d6dfd8ad4ed1d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem_1ga54a85e2fcb08a6557e7d6dfd8ad4ed1d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for SEM measurement. SyntaxRFMXWLAN_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To10506264int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threads yo

### RFMXWLAN_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for SEM measurement.

#### Syntax

RFMXWLAN_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506264 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__averaging_1ga5d6f507c7cebee5327c350d5ad6ba8a0.html language=enus -->
## TOPIC 00086: RFMXWLAN_ATTR_SEM_AVERAGING_TYPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__averaging_1ga5d6f507c7cebee5327c350d5ad6ba8a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__averaging_1ga5d6f507c7cebee5327c350d5ad6ba8a0.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. SyntaxRFMXWLAN_ATTR_SEM_AVERAGING_TYPENumeric ValueData TypeAccessApplies To10506261int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXWLAN_ATTR_SEM_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.

#### Syntax

RFMXWLAN_ATTR_SEM_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506261 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum is retained from one acquisition to the next at each frequency bin. |
| RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum is retained from one acquisition to the next at each frequency bin. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__carrier_1gae7d1c3e961d97785956bf93117f93f84.html language=enus -->
## TOPIC 00087: RFMXWLAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__carrier_1gae7d1c3e961d97785956bf93117f93f84.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__carrier_1gae7d1c3e961d97785956bf93117f93f84.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz. SyntaxRFMXWLAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To10506245float64Read-OnlyN/ARemarks You do not need to use a selector string to read th

### RFMXWLAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

Returns the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz.

#### Syntax

RFMXWLAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506245 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 18 M.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__offset_1ga45c66d67c461578b01f288eeb5285463.html language=enus -->
## TOPIC 00088: RFMXWLAN_ATTR_SEM_OFFSET_START_FREQUENCY

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__offset_1ga45c66d67c461578b01f288eeb5285463.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__offset_1ga45c66d67c461578b01f288eeb5285463.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz. SyntaxRFMXWLAN_ATTR_SEM_OFFSET_START_FREQUENCYNumeric ValueData TypeAccessApplies To10506247float64Read/WriteOffsetRemarks Use "offset<n>" as the Selector String to configure this at

### RFMXWLAN_ATTR_SEM_OFFSET_START_FREQUENCY

Specifies the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz.

#### Syntax

RFMXWLAN_ATTR_SEM_OFFSET_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506247 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure this attribute.

The default value is 9 MHz.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results_1ga0841f123f4ff74067161a3382196a5b5.html language=enus -->
## TOPIC 00089: RFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results_1ga0841f123f4ff74067161a3382196a5b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results_1ga0841f123f4ff74067161a3382196a5b5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. SyntaxRFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To10506267int32Read-OnlyN/ARemarks You do not need to use a selector st

### RFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments.

#### Syntax

RFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506267 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. |
| RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_PASS | 1 (0x1) | The spectrum does not exceed the SEM measurement mask limits for any offset segment. |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset.html language=enus -->
## TOPIC 00090: Lower Offset

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERReturns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm. RFMXWLAN_ATTR_SE

### Lower Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER | Returns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER | Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN | Returns the margin from the SEM measurement mask for the lower (negative) offset. This value is expressed in dB. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power level of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. This value is expressed in dBm. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY | Returns the frequency of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. This value is expressed in Hz. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power level of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. This value is expressed in dB. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS | Returns the lower offset segment measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER | Returns the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
| RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER | Returns the peak power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1ga01c2c348ceca47787a2ec03c4776f57b.html language=enus -->
## TOPIC 00091: RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1ga01c2c348ceca47787a2ec03c4776f57b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1ga01c2c348ceca47787a2ec03c4776f57b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power level of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To10506280float64Read-OnlyOffsetRe

### RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

Returns the power level of the spectrum corresponding to the result of the [RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN](group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1gadc7f7cfc968c6728e288972bd939382a.html) attribute. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506280 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1ga1772bf236eddfbd4fd66a9a0b388c69b.html language=enus -->
## TOPIC 00092: RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1ga1772bf236eddfbd4fd66a9a0b388c69b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1ga1772bf236eddfbd4fd66a9a0b388c69b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm. SyntaxRFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To10506274fl

### RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

Returns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm.

#### Syntax

RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506274 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1gaac5fa7740ed785a7dba8505228d0db67.html language=enus -->
## TOPIC 00093: RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1gaac5fa7740ed785a7dba8505228d0db67.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1gaac5fa7740ed785a7dba8505228d0db67.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz. SyntaxRFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCYNumeric ValueData TypeAccessApplies To10506278float64Read-OnlyOffsetRemarks Use "offset<n>" as the Selector String to

### RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

Returns the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz.

#### Syntax

RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506278 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1gac3b30398fcc55d8831051d84cf137d48.html language=enus -->
## TOPIC 00094: RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1gac3b30398fcc55d8831051d84cf137d48.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__lower__offset_1gac3b30398fcc55d8831051d84cf137d48.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset segment measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment. SyntaxRFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUSNumeric ValueData TypeAccessApplies To10506273int32Read-OnlyOffsetRemarks Use "offse

### RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

Returns the lower offset segment measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment.

#### Syntax

RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506273 | int32 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |
| RFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |

Parent topic:

Lower Offset

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset.html language=enus -->
## TOPIC 00095: Upper Offset

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWERReturns the average power of the offset (positive) offset channel over the bandwidth determined by the start and stop frequencies of the offset channel. This value is expressed in dBm. RFMXWLAN_ATTR

### Upper Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER | Returns the average power of the offset (positive) offset channel over the bandwidth determined by the start and stop frequencies of the offset channel. This value is expressed in dBm. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER | Returns the peak power of the offset (positive) offset segment. This value is expressed in dBm. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN | Returns the margin from the SEM measurement mask for the offset (positive). This value is expressed in dB. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER | Returns the power level of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. This value is expressed in dBm. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY | Returns the frequency of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. This value is expressed in Hz. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER | Returns the power level of the spectrum corresponding to the result of the RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. This value is expressed in dB. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS | Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY | Returns the frequency at which the peak power occurs in the offset (positive) channel. This value is expressed in Hz. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER | Returns the average power of the offset (positive) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. |
| RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER | Returns the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset_1ga400d942d835a5a49da221aad2eef6d98.html language=enus -->
## TOPIC 00096: RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset_1ga400d942d835a5a49da221aad2eef6d98.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset_1ga400d942d835a5a49da221aad2eef6d98.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the offset (positive) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. SyntaxRFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWERNumeric ValueData TypeAccessApplies To10506285float64Read-OnlyOffsetRemarks Use "o

### RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

Returns the average power of the offset (positive) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.

#### Syntax

RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506285 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset_1ga968d55fd3d483b6b541a8bef726d263b.html language=enus -->
## TOPIC 00097: RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset_1ga968d55fd3d483b6b541a8bef726d263b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__results__upper__offset_1ga968d55fd3d483b6b541a8bef726d263b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB. SyntaxRFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWERNumeric ValueData TypeAccessApplies To10506287float64Read-OnlyOffsetRemarks Use "offset<n>" as the

### RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

Returns the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB.

#### Syntax

RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506287 | float64 | Read-Only | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Upper Offset

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__sem__sweep__time_1ga85714d64bfe04da755e7c0a3a397edaf.html language=enus -->
## TOPIC 00098: RFMXWLAN_ATTR_SEM_SWEEP_TIME_INTERVAL

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__sem__sweep__time_1ga85714d64bfe04da755e7c0a3a397edaf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__sem__sweep__time_1ga85714d64bfe04da755e7c0a3a397edaf.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time for the SEM measurement. This value is expressed in seconds. SyntaxRFMXWLAN_ATTR_SEM_SWEEP_TIME_INTERVALNumeric ValueData TypeAccessApplies To10506258float64Read/WriteN/ARemarks This attribute is ignored when you set the RFMXWLAN_ATTR_SEM_SWEEP_TIME_AUTO attribute to True.Yo

### RFMXWLAN_ATTR_SEM_SWEEP_TIME_INTERVAL

Specifies the sweep time for the SEM measurement. This value is expressed in seconds.

#### Syntax

RFMXWLAN_ATTR_SEM_SWEEP_TIME_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10506258 | float64 | Read/Write | N/A |

#### Remarks

This attribute is ignored when you set the [RFMXWLAN_ATTR_SEM_SWEEP_TIME_AUTO](group____root__ni_r_fmx_w_l_a_n__attributes__sem__sweep__time_1ga8d9e38fe4617186bd48a4112dc1752e1.html) attribute to **True**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__digital__edge.html language=enus -->
## TOPIC 00099: Digital Edge

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__digital__edge.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_EDGESpecifies the active edge for the trigger. This attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to Digital Edge. RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCESpecifies the source terminal for the di

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_EDGE | Specifies the active edge for the trigger. This attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to Digital Edge. |
| RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE | Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to Digital Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__digital__edge_1ga00e5f87f064322cd2b03235f9da8c6a7.html language=enus -->
## TOPIC 00100: RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__digital__edge_1ga00e5f87f064322cd2b03235f9da8c6a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__digital__edge_1ga00e5f87f064322cd2b03235f9da8c6a7.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To10485765char[]Read/WriteN/ARemarks On a MIMO session, th

### RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

Specifies the source terminal for the digital edge trigger. This attribute is used only when you set the [RFMXWLAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_l_a_n__attributes__trigger_1ga99ffba3c9ea659ff90bc99e442aeb38d.html) attribute to **Digital Edge**.

#### Syntax

RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485765 | char[] | Read/Write | N/A |

#### Remarks

On a MIMO session, this attribute configures the digital edge trigger on the master port. By default, the [RFMXWLAN_ATTR_SELECTED_PORTS](group____root__ni_r_fmx_w_l_a_n__attributes_1ga5bc48d1191df4d4809c611342648e086.html) attribute is configured to "segment0/chain0" and is considered as the master port.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating.html language=enus -->
## TOPIC 00101: Gating

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_TRIGGER_GATE_ENABLEDEnables time-domain gating of the acquired signal for SEM measurement. RFMXWLAN_ATTR_TRIGGER_GATE_LENGTHSpecifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measur

### Gating

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED | Enables time-domain gating of the acquired signal for SEM measurement. |
| RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH | Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED attribute to True. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga1e15880a41f068795583e4adb6743d9d.html language=enus -->
## TOPIC 00102: RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga1e15880a41f068795583e4adb6743d9d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga1e15880a41f068795583e4adb6743d9d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED attribute to True. SyntaxRFMXWLAN_ATTR_TRIGGER_GATE_LENGTHNumeric ValueData TypeAccessApplies To10485803float64Rea

### RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH

Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the [RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga972c1456c2458442f7cad955323e658b.html) attribute to **True**.

#### Syntax

RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485803 | float64 | Read/Write | N/A |

#### Remarks

If the measurement interval required to perform the measurement exceeds the gate length, the measurement acquires as many additional records as necessary to honor the required measurement interval. This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

Parent topic:

Gating

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga972c1456c2458442f7cad955323e658b.html language=enus -->
## TOPIC 00103: RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga972c1456c2458442f7cad955323e658b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga972c1456c2458442f7cad955323e658b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables time-domain gating of the acquired signal for SEM measurement. SyntaxRFMXWLAN_ATTR_TRIGGER_GATE_ENABLEDNumeric ValueData TypeAccessApplies To10485802int32Read/WriteN/ARemarks If you set this attribute to True and the required measurement interval exceeds the value you set for the RFMXWLAN_AT

### RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED

Enables time-domain gating of the acquired signal for SEM measurement.

#### Syntax

RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485802 | int32 | Read/Write | N/A |

#### Remarks

If you set this attribute to **True** and the required measurement interval exceeds the value you set for the [RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH](group____root__ni_r_fmx_w_l_a_n__attributes__trigger__gating_1ga1e15880a41f068795583e4adb6743d9d.html) attribute, then the measurement restricts the acquisition duration of each record to Gate Length attribute and acquires as many additional records as necessary for the required measurement interval. If you want to ignore the idle duration between multiple PPDUs during an SEM measurement, you must set Gate Enabled to **True** and set Gate Length to a value less than or equal to the length of the PPDU under analysis. This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_FALSE | 0 (0x0) | Gate for SEM measurements is disabled. |
| RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_TRUE | 1 (0x1) | Gate for SEM measurements is enabled. |

Parent topic:

Gating

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge.html language=enus -->
## TOPIC 00104: IQ Power Edge

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVELSpecifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level T

### IQ Power Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL | Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level Type attribute to Absolute. |
| RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE | Specifies the reference for the RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |
| RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE | Specifies whether the device asserts the trigger when the signal power is rising or falling. |
| RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE | Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1ga7230a90becf537ce68cf8cd1b5bf1039.html language=enus -->
## TOPIC 00105: RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1ga7230a90becf537ce68cf8cd1b5bf1039.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1ga7230a90becf537ce68cf8cd1b5bf1039.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To10485767char[]Read/WriteN/ARemarks On a MIMO ses

### RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is used only when you set the [RFMXWLAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_l_a_n__attributes__trigger_1ga99ffba3c9ea659ff90bc99e442aeb38d.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485767 | char[] | Read/Write | N/A |

#### Remarks

On a MIMO session, this attribute configures the IQ Power edge trigger on the master port. By default, the [RFMXWLAN_ATTR_SELECTED_PORTS](group____root__ni_r_fmx_w_l_a_n__attributes_1ga5bc48d1191df4d4809c611342648e086.html) attribute is configured to "segment0/chain0" and is considered as the master port.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1ga8bc7dfa0342ed4f9757a11c699441e78.html language=enus -->
## TOPIC 00106: RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1ga8bc7dfa0342ed4f9757a11c699441e78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1ga8bc7dfa0342ed4f9757a11c699441e78.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or falling. SyntaxRFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPENumeric ValueData TypeAccessApplies To10485769int32Read/WriteN/ARemarks The device asserts the trigger when the signal power exceeds the specified level with th

### RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

Specifies whether the device asserts the trigger when the signal power is rising or falling.

#### Syntax

RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485769 | int32 | Read/Write | N/A |

#### Remarks

The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This attribute is used only when you set the [RFMXWLAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_l_a_n__attributes__trigger_1ga99ffba3c9ea659ff90bc99e442aeb38d.html) attribute to **IQ Power Edge**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |
| RFMXWLAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gaa65506ab680faa8fa21f1647feea3034.html language=enus -->
## TOPIC 00107: RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gaa65506ab680faa8fa21f1647feea3034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gaa65506ab680faa8fa21f1647feea3034.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level at which the device triggers. This value is expressed in dB when you set the RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE attribute to Relative and in dBm when you set the IQ Power Edge Level Type attribute to Absolute. SyntaxRFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVELNumer

### RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE](group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gab4bd977adb3e3f1d566c8e5b039009af.html) attribute to **Relative** and in dBm when you set the IQ Power Edge Level Type attribute to **Absolute**.

#### Syntax

RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10485768 | float64 | Read/Write | N/A |

#### Remarks

The device asserts the trigger when the signal exceeds the level specified by the value of this attribute, taking into consideration the specified slope. This attribute is used only when you set the [RFMXWLAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_l_a_n__attributes__trigger_1ga99ffba3c9ea659ff90bc99e442aeb38d.html) attribute to **IQ Power Edge**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gab4bd977adb3e3f1d566c8e5b039009af.html language=enus -->
## TOPIC 00108: RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gab4bd977adb3e3f1d566c8e5b039009af.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gab4bd977adb3e3f1d566c8e5b039009af.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL attribute. The IQ Power Edge Level Type attribute is used only when you set the RFMXWLAN_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPENumeric ValueData TypeAccessApplies To1

### RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

Specifies the reference for the [RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL](group____root__ni_r_fmx_w_l_a_n__attributes__trigger__iq__power__edge_1gaa65506ab680faa8fa21f1647feea3034.html) attribute. The IQ Power Edge Level Type attribute is used only when you set the [RFMXWLAN_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_w_l_a_n__attributes__trigger_1ga99ffba3c9ea659ff90bc99e442aeb38d.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10489855 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The IQ Power Edge Level attribute is relative to the value of the RFMXWLAN_ATTR_REFERENCE_LEVEL attribute. |
| RFMXWLAN_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__trigger__minimum__quiet__time.html language=enus -->
## TOPIC 00109: Minimum Quiet Time

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__trigger__minimum__quiet__time.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__trigger__minimum__quiet__time.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATIONSpecifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. RFMXWLAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODESpecifies

### Minimum Quiet Time

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. |
| RFMXWLAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE | Specifies whether the measurement computes the minimum quiet time used for triggering. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga21bbecfed7971d08c70810428192c11c.html language=enus -->
## TOPIC 00110: RFMXWLAN_ATTR_TXP_ALL_TRACES_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga21bbecfed7971d08c70810428192c11c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga21bbecfed7971d08c70810428192c11c.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement. SyntaxRFMXWLAN_ATTR_TXP_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To10489862int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for t

### RFMXWLAN_ATTR_TXP_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement.

#### Syntax

RFMXWLAN_ATTR_TXP_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10489862 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga243172899525a11f17e3b964de3c6100.html language=enus -->
## TOPIC 00111: RFMXWLAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga243172899525a11f17e3b964de3c6100.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga243172899525a11f17e3b964de3c6100.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for TXP measurement. SyntaxRFMXWLAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To10489863int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threads yo

### RFMXWLAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for TXP measurement.

#### Syntax

RFMXWLAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10489863 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga4205f1801568878a8f906fe97ceb0328.html language=enus -->
## TOPIC 00112: RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga4205f1801568878a8f906fe97ceb0328.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga4205f1801568878a8f906fe97ceb0328.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum measurement interval. This value is expressed in seconds. SyntaxRFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVALNumeric ValueData TypeAccessApplies To10489858float64Read/WriteN/ARemarks When you set the RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED attribute to True, the measurement

### RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL

Specifies the maximum measurement interval. This value is expressed in seconds.

#### Syntax

RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10489858 | float64 | Read/Write | N/A |

#### Remarks

When you set the [RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__txp_1gaa5f842975d87143affbc3edca9673286.html) attribute to **True**, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this attribute.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__txp_1gaa5f842975d87143affbc3edca9673286.html language=enus -->
## TOPIC 00113: RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__txp_1gaa5f842975d87143affbc3edca9673286.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__txp_1gaa5f842975d87143affbc3edca9673286.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement detects the start and the end of a WLAN packet automatically. SyntaxRFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLEDNumeric ValueData TypeAccessApplies To10489859int32Read/WriteN/ARemarks When you set this attribute to True, the measurement interval used is equal to the sm

### RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED

Specifies whether the measurement detects the start and the end of a WLAN packet automatically.

#### Syntax

RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10489859 | int32 | Read/Write | N/A |

#### Remarks

When you set this attribute to **True**, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for the [RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL](group____root__ni_r_fmx_w_l_a_n__attributes__txp_1ga4205f1801568878a8f906fe97ceb0328.html) attribute.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_FALSE | 0 (0x0) | Disables burst detection. |
| RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_TRUE | 1 (0x1) | Enables burst detection. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__txp_1gaa611361b2ff611dd45a822f47d0c344b.html language=enus -->
## TOPIC 00114: RFMXWLAN_ATTR_TXP_MEASUREMENT_ENABLED

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__txp_1gaa611361b2ff611dd45a822f47d0c344b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__txp_1gaa611361b2ff611dd45a822f47d0c344b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the transmit power (TXP) measurement. SyntaxRFMXWLAN_ATTR_TXP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To10489856int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to

### RFMXWLAN_ATTR_TXP_MEASUREMENT_ENABLED

Specifies whether to enable the transmit power (TXP) measurement.

#### Syntax

RFMXWLAN_ATTR_TXP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10489856 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__txp__averaging.html language=enus -->
## TOPIC 00115: Averaging

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__txp__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__txp__averaging.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXWLAN_ATTR_TXP_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED attribute to True. RFMXWLAN_ATTR_TXP_AVERAGING_ENABLEDSpecifies whether to enable averaging for the TXP measurement. Att

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXWLAN_ATTR_TXP_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED attribute to True. |
| RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED | Specifies whether to enable averaging for the TXP measurement. |

#### Attachments

None

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__attributes__txp__results_1gacb319bcaba0552fdfd13637c508587d0.html language=enus -->
## TOPIC 00116: RFMXWLAN_ATTR_TXP_RESULTS_PEAK_POWER_MINIMUM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__attributes__txp__results_1gacb319bcaba0552fdfd13637c508587d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__attributes__txp__results_1gacb319bcaba0552fdfd13637c508587d0.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxRFMXWLAN_ATTR_TXP_RESULTS_PEAK_POWER_MINIMUMNumeric ValueData TypeAccessApplies To10489880float64Read-OnlyChain

### RFMXWLAN_ATTR_TXP_RESULTS_PEAK_POWER_MINIMUM

#### Syntax

RFMXWLAN_ATTR_TXP_RESULTS_PEAK_POWER_MINIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10489880 | float64 | Read-Only | Chain |

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions_1ga24594f906a1d8bfe80354ed6ecf3f279.html language=enus -->
## TOPIC 00117: RFmxWLAN_OFDMModAccFetchDecodedUHRSIGBitsTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions_1ga24594f906a1d8bfe80354ed6ecf3f279.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions_1ga24594f906a1d8bfe80354ed6ecf3f279.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedUHRSIGBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedUhrsigBits[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleselectorStrin

### RFmxWLAN_OFDMModAccFetchDecodedUHRSIGBitsTrace

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedUHRSIGBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedUhrsigBits[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle |  |
| selectorString | [in] | char[] |  |
| timeout | [in] | float64 |  |
| decodedUhrsigBits | [out] | int32[] |  |
| arraySize | [in] | int32 |  |
| actualArraySize | [out] | int32 * |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions_1gabec970b9c04929769642216c6b2b2bde.html language=enus -->
## TOPIC 00118: RFmxWLAN_Initialize

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions_1gabec970b9c04929769642216c6b2b2bde.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions_1gabec970b9c04929769642216c6b2b2bde.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the device you specify through the resourceName parameter, and returns a handleOut that identifies this device in all subsequent RFmx functions. Syntaxint32 __stdcall RFmxWLAN_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSe

### RFmxWLAN_Initialize

Creates an RFmx session to the device you specify through the **resourceName** parameter, and returns a **handleOut** that identifies this device in all subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxWLAN_Initialize(char resourceName[], char optionString[], niRFmxInstrHandle *handleOut, int32 *isNewSession)

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
| isNewSession | [out] | int32 * | Returns RFMXWLAN_VAL_TRUE if the function created a new session, or RFMXWLAN_VAL_FALSE if the function returned a reference to an existing session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__advanced__analyze2_1gae45742e8ab52671f35a81a79f1b55af9.html language=enus -->
## TOPIC 00119: RFmxWLAN_AnalyzeNWaveformsIQ

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__advanced__analyze2_1gae45742e8ab52671f35a81a79f1b55af9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__advanced__analyze2_1gae45742e8ab52671f35a81a79f1b55af9.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function o

### RFmxWLAN_AnalyzeNWaveformsIQ

Performs the enabled measurements on the I/Q complex waveform(s) that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxWLAN_AnalyzeNWaveformsIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0[], float64 dx[], NIComplexSingle iq[], int32 iqSize[], int32 arraySize, int32 reset)

#### Remarks

When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxWLAN_Commit](group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga2a063d37aeaab7f7daae37826c3e75cf.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64[] | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64[] | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqSize | [in] | int32[] | Specifies the size of n waveforms |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__advanced__analyze2_1gafcb9ed3316a2908c4538badf94a6c309.html language=enus -->
## TOPIC 00120: RFmxWLAN_AnalyzeIQ1Waveform

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__advanced__analyze2_1gafcb9ed3316a2908c4538badf94a6c309.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__advanced__analyze2_1gafcb9ed3316a2908c4538badf94a6c309.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxWLAN_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is either **IQ** or **IQ or Spectral**.

#### Syntax

int32 __stdcall RFmxWLAN_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxWLAN_Commit](group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga2a063d37aeaab7f7daae37826c3e75cf.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the Selector String. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Analyze2

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__build__string_1ga0e92c133c4eb5deb6c073fafeb5f4432.html language=enus -->
## TOPIC 00121: RFmxWLAN_BuildUserString

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__build__string_1ga0e92c133c4eb5deb6c073fafeb5f4432.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__build__string_1ga0e92c133c4eb5deb6c073fafeb5f4432.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the user string to use as the selector string. Syntaxint32 __stdcall RFmxWLAN_BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector Str

### RFmxWLAN_BuildUserString

Creates the user string to use as the selector string.

#### Syntax

int32 __stdcall RFmxWLAN_BuildUserString(char selectorString[], int32 userNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| userNumber | [in] | int32 | This parameter specifies the user number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__build__string_1ga523532c109b1f4c82338075320e15334.html language=enus -->
## TOPIC 00122: RFmxWLAN_BuildChainString

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__build__string_1ga523532c109b1f4c82338075320e15334.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__build__string_1ga523532c109b1f4c82338075320e15334.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a chain string. Syntaxint32 __stdcall RFmxWLAN_BuildChainString(char selectorString[], int32 chainNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Selector String comprising of the signal

### RFmxWLAN_BuildChainString

Creates a chain string.

#### Syntax

int32 __stdcall RFmxWLAN_BuildChainString(char selectorString[], int32 chainNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. You can also pass Selector String Out from the RFmxWLAN_BuildSegmentString function as an input to this function. The default value is "segment0".Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxWLAN Build Segment String function to build the selector string. |
| chainNumber | [in] | int32 | This parameter specifies the chain number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__build__string_1gaaf9bd0c8d6cef4e8c9813e62c086589c.html language=enus -->
## TOPIC 00123: RFmxWLAN_BuildOffsetString

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__build__string_1gaaf9bd0c8d6cef4e8c9813e62c086589c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__build__string_1gaaf9bd0c8d6cef4e8c9813e62c086589c.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the offset string to use as the selector string. Syntaxint32 __stdcall RFmxWLAN_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])ParametersNameDirectionTypeDescriptionselectorString[in]char[]This parameter specifies a Select

### RFmxWLAN_BuildOffsetString

Creates the offset string to use as the selector string.

#### Syntax

int32 __stdcall RFmxWLAN_BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| offsetNumber | [in] | int32 | This parameter specifies the offset number for building the selector string. |
| selectorStringOutLength | [out] | int32 | Specifies the length of the string that is returned by the selectorStringOut parameter. To get the minimum buffer size required to build the selector string, set the selectorStringOutLength parameter to 0. |
| selectorStringOut | [out] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration_1ga6f2f25532569bf94fd41f7b354abd6cf.html language=enus -->
## TOPIC 00124: RFmxWLAN_CfgFrequencyReference

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration_1ga6f2f25532569bf94fd41f7b354abd6cf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration_1ga6f2f25532569bf94fd41f7b354abd6cf.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxWLAN_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Instrum

### RFmxWLAN_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxWLAN_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXWLAN_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXWLAN_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXWLAN_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXWLAN_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXWLAN_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXWLAN_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXWLAN_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXWLAN_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXWLAN_VAL_CLK_IN_STR or RFMXWLAN_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration_1ga9a773a4ca4593ceb5b2b4c3c9ce632b0.html language=enus -->
## TOPIC 00125: RFmxWLAN_CfgRFAttenuation

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration_1ga9a773a4ca4593ceb5b2b4c3c9ce632b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration_1ga9a773a4ca4593ceb5b2b4c3c9ce632b0.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the nominal attenuation and the RFmx driver setting. Syntaxint32 __stdcall RFmxWLAN_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the R

### RFmxWLAN_CfgRFAttenuation

Configures the nominal attenuation and the RFmx driver setting.

#### Syntax

int32 __stdcall RFmxWLAN_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgRFAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_rf_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| rfAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver computes the RF attenuation.ValueDescriptionRFMXWLAN_VAL_RF_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter.RFMXWLAN_VAL_RF_ATTENUATION_AUTO_TRUE (1)Specifies that the RFmx driver computes the RF attenuation automatically. |
| Value | Description |  |  |
| RFMXWLAN_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. |  |  |
| RFMXWLAN_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that the RFmx driver computes the RF attenuation automatically. |  |  |
| rfAttenuationValue | [in] | float64 | Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain when the rfAttenuationAuto parameter is set to RFMXWLAN_VAL_RF_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gac8af2bdceeb7bbb721476c29da0db030.html language=enus -->
## TOPIC 00126: RFmxWLAN_CfgChannelBandwidth

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gac8af2bdceeb7bbb721476c29da0db030.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gac8af2bdceeb7bbb721476c29da0db030.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the channel bandwidth. Syntaxint32 __stdcall RFmxWLAN_CfgChannelBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 channelBandwidth)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instru

### RFmxWLAN_CfgChannelBandwidth

Configures the channel bandwidth.

#### Syntax

int32 __stdcall RFmxWLAN_CfgChannelBandwidth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 channelBandwidth)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| channelBandwidth | [in] | float64 | This parameter specifies the channel spacing as defined in section 3.1 of IEEE Standard 802.11-2016 (pp. 130). This value is expressed in Hz. The default value is 20M.Name (Value)Description5M (5e6)This bandwidth corresponds to IEEE Standard 802.11p.10M (10e6)This bandwidth corresponds to IEEE Standard 802.11j and IEEE Standard 802.11p.20M (20e6)This bandwidth corresponds to IEEE Standard 802.11a/g, IEEE Standard 802.11j, IEEE Standard 802.11p, IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn.40M (40e6)This bandwidth corresponds to IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn.80M (80e6)This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn.160M (160e6)This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn.320M (320e6)This bandwidth corresponds to IEEE Standard 802.11be, and IEEE Standard 802.11bn. |
| Name (Value) | Description |  |  |
| 5M (5e6) | This bandwidth corresponds to IEEE Standard 802.11p. |  |  |
| 10M (10e6) | This bandwidth corresponds to IEEE Standard 802.11j and IEEE Standard 802.11p. |  |  |
| 20M (20e6) | This bandwidth corresponds to IEEE Standard 802.11a/g, IEEE Standard 802.11j, IEEE Standard 802.11p, IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn. |  |  |
| 40M (40e6) | This bandwidth corresponds to IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn. |  |  |
| 80M (80e6) | This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn. |  |  |
| 160M (160e6) | This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, IEEE Standard 802.11be, and IEEE Standard 802.11bn. |  |  |
| 320M (320e6) | This bandwidth corresponds to IEEE Standard 802.11be, and IEEE Standard 802.11bn. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gaeb6cce056d2d42b542ae7e5c231f6e1a.html language=enus -->
## TOPIC 00127: RFmxWLAN_CfgMechanicalAttenuation

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gaeb6cce056d2d42b542ae7e5c231f6e1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gaeb6cce056d2d42b542ae7e5c231f6e1a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxWLAN_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wrapp

### RFmxWLAN_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxWLAN_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXWLAN_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXWLAN_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXWLAN_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXWLAN_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXWLAN_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gaf79a9944ee81a9224b75496fd2f55f0e.html language=enus -->
## TOPIC 00128: RFmxWLAN_SendSoftwareEdgeTrigger

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gaf79a9944ee81a9224b75496fd2f55f0e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gaf79a9944ee81a9224b75496fd2f55f0e.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxWLAN Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger. Syntaxint32 __stdcall RFmxWLAN_SendSoftwareEdgeTrigger(niR

### RFmxWLAN_SendSoftwareEdgeTrigger

Sends a trigger to the device when you use the RFmxWLAN Configure Trigger function to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this function to override a hardware trigger.

#### Syntax

int32 __stdcall RFmxWLAN_SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)

#### Remarks

- You configure an invalid trigger.
- You have not previously called the [RFmxWLAN_Initiate](group____root__ni_r_fmx_w_l_a_n__functions_1ga5aee2296d1c63c1b33e69983d6722929.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gafa02ab725f5ed9419bcbfa462f099e77.html language=enus -->
## TOPIC 00129: RFmxWLAN_AutoDetectSignalAnalysisOnlySplit

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gafa02ab725f5ed9419bcbfa462f099e77.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration_1gafa02ab725f5ed9419bcbfa462f099e77.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically detects the standard, channel bandwidth, and burst length on the I/Q complex waveform that you specify in IQ parameter, and writes the RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_STANDARD, RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_CHANNEL_BANDWIDTH, and RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_D

### RFmxWLAN_AutoDetectSignalAnalysisOnlySplit

Automatically detects the standard, channel bandwidth, and burst length on the I/Q complex waveform that you specify in **IQ** parameter, and writes the [RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_STANDARD](group____root__ni_r_fmx_w_l_a_n__attributes__auto__detect__signal_1ga650d8567f77698a245a7cb038d900cc8.html), [RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_CHANNEL_BANDWIDTH](group____root__ni_r_fmx_w_l_a_n__attributes__auto__detect__signal_1gaad3fc97486b86ced67dc2537e1c51a3d.html), and [RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_BURST_LENGTH](group____root__ni_r_fmx_w_l_a_n__attributes__auto__detect__signal_1ga68e8d85fc8aad27f7ee564c6684fc7bd.html) attributes.

#### Syntax

int32 __stdcall RFmxWLAN_AutoDetectSignalAnalysisOnlySplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 iqI[], float32 iqQ[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| x0 | [in] | float64 | This parameter specifies the start time of the input y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iqI | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| iqQ | [in] | float32[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc.html language=enus -->
## TOPIC 00130: DSSSModAcc

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWLAN_DSSSModAccCfgAcquisitionLengthConfigures the Acquisition Length parameter and the Acquisition Length Mode parameter of the acquired waveform for the measurement. RFmxWLAN_DSSSModAccCfgAveragingConfigures averaging for the measurement. RFmxWLAN_DSSSModAc

### DSSSModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWLAN_DSSSModAccCfgAcquisitionLength | Configures the Acquisition Length parameter and the Acquisition Length Mode parameter of the acquired waveform for the measurement. |
| RFmxWLAN_DSSSModAccCfgAveraging | Configures averaging for the measurement. |
| RFmxWLAN_DSSSModAccCfgEVMUnit | Configures EVM unit for the measurement. |
| RFmxWLAN_DSSSModAccCfgMeasurementLength | Configures the measurement offset and the maximum measurement length for the DSSSModAcc measurement. |
| RFmxWLAN_DSSSModAccCfgPowerMeasurementCustomGateArray | Configures the custom gate start and stop times for power measurement. |
| RFmxWLAN_DSSSModAccCfgPowerMeasurementEnabled | Configures whether power measurement is enabled for the DSSSModAcc measurement. |
| RFmxWLAN_DSSSModAccCfgPowerMeasurementNumberOfCustomGates | Configures the number of custom gates for power measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga062736698d643bca75187bc779b6b5e5.html language=enus -->
## TOPIC 00131: RFmxWLAN_DSSSModAccCfgAveraging

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga062736698d643bca75187bc779b6b5e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga062736698d643bca75187bc779b6b5e5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the measurement. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies

### RFmxWLAN_DSSSModAccCfgAveraging

Configures averaging for the measurement.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for DSSSModAcc measurements. The default value is False.NameValueDescriptionRFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_FALSE0 (0x0)Performs measurement on a single acquisition.RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE1 (0x1)Measurement uses the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_COUNT attribute for the number of acquisitions using which the results are averaged. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_FALSE | 0 (0x0) | Performs measurement on a single acquisition. |  |
| RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE | 1 (0x1) | Measurement uses the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_COUNT attribute for the number of acquisitions using which the results are averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga1a14b33bab16a79aeb730e0f22d52def.html language=enus -->
## TOPIC 00132: RFmxWLAN_DSSSModAccCfgAcquisitionLength

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga1a14b33bab16a79aeb730e0f22d52def.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga1a14b33bab16a79aeb730e0f22d52def.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Acquisition Length parameter and the Acquisition Length Mode parameter of the acquired waveform for the measurement. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccCfgAcquisitionLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 acquisitionLengthMode, float64 acquisitio

### RFmxWLAN_DSSSModAccCfgAcquisitionLength

Configures the **Acquisition Length** parameter and the **Acquisition Length Mode** parameter of the acquired waveform for the measurement.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccCfgAcquisitionLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 acquisitionLengthMode, float64 acquisitionLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| acquisitionLengthMode | [in] | int32 | This parameter specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc attributes. The default value is Auto.NameValueDescriptionRFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_MANUAL0 (0x0)Uses the acquisition length specified by the RFMXWLAN_ATTR_DSSSMODACC_ACQUISITION_LENGTH attribute.RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_AUTO1 (0x1)Computes the acquisition length based on the RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_OFFSET attribute and the RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH attribute. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_MANUAL | 0 (0x0) | Uses the acquisition length specified by the RFMXWLAN_ATTR_DSSSMODACC_ACQUISITION_LENGTH attribute. |  |
| RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_AUTO | 1 (0x1) | Computes the acquisition length based on the RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_OFFSET attribute and the RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH attribute. |  |
| acquisitionLength | [in] | float64 | This parameter specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the Acquisition Length Mode parameter to Manual. This value is expressed in seconds. The default value is 0.001. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga1b09611bc108c0367586ee939431f3e7.html language=enus -->
## TOPIC 00133: RFmxWLAN_DSSSModAccCfgPowerMeasurementNumberOfCustomGates

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga1b09611bc108c0367586ee939431f3e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga1b09611bc108c0367586ee939431f3e7.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of custom gates for power measurement. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementNumberOfCustomGates(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCustomGates)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandl

### RFmxWLAN_DSSSModAccCfgPowerMeasurementNumberOfCustomGates

Configures the number of custom gates for power measurement.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementNumberOfCustomGates(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfCustomGates)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| numberOfCustomGates | [in] | int32 | This parameter specifies the number of custom gates used for power measurement. The default value is 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga506bd886a4444409253a1754f5572cbc.html language=enus -->
## TOPIC 00134: RFmxWLAN_DSSSModAccCfgPowerMeasurementCustomGateArray

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga506bd886a4444409253a1754f5572cbc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1ga506bd886a4444409253a1754f5572cbc.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the custom gate start and stop times for power measurement. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementCustomGateArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 startTime[], float64 stopTime[], int32 numberOfElements)ParametersNameDirectionTypeDes

### RFmxWLAN_DSSSModAccCfgPowerMeasurementCustomGateArray

Configures the custom gate start and stop times for power measurement.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementCustomGateArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 startTime[], float64 stopTime[], int32 numberOfElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| startTime | [in] | float64[] | This parameter specifies the array of start time of the custom power gates. This value is expressed in seconds. A value of 0 indicates that the start time is the start of the PPDU. The default value is an empty array. |
| stopTime | [in] | float64[] | This parameter specifies the array of stop time of the custom power gates. This value is expressed in seconds. The default value is an empty array. |
| numberOfElements | [in] | int32 | Specifies the number of elements in each array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1gaa70f6c93cddc157df285f0161f94c56f.html language=enus -->
## TOPIC 00135: RFmxWLAN_DSSSModAccCfgPowerMeasurementEnabled

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1gaa70f6c93cddc157df285f0161f94c56f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration__dsssmodacc_1gaa70f6c93cddc157df285f0161f94c56f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether power measurement is enabled for the DSSSModAcc measurement. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerMeasurementEnabled)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFm

### RFmxWLAN_DSSSModAccCfgPowerMeasurementEnabled

Configures whether power measurement is enabled for the DSSSModAcc measurement.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerMeasurementEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| powerMeasurementEnabled | [in] | int32 | This parameter specifies if power measurement is performed. This parameter computes power of various fields in the PPDU. Additionally, this measurement computes power over the custom gates that you can configure using the RFMXWLAN_ATTR_DSSSMODACC_POWER_NUMBER_OF_CUSTOM_GATES, the RFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_START_TIME and the RFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_STOP_TIME attributes. The default value is False.NameValueDescriptionRFMXWLAN_VAL_DSSSMODACC_POWER_MEASUREMENT_ENABLED_FALSE0 (0x0)Disables power measurement.RFMXWLAN_VAL_DSSSMODACC_POWER_MEASUREMENT_ENABLED_TRUE1 (0x1)Enables power measurement. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_DSSSMODACC_POWER_MEASUREMENT_ENABLED_FALSE | 0 (0x0) | Disables power measurement. |  |
| RFMXWLAN_VAL_DSSSMODACC_POWER_MEASUREMENT_ENABLED_TRUE | 1 (0x1) | Enables power measurement. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__configuration__mimo_1gac008ed0fd58f45f03b99b79e20b0d204.html language=enus -->
## TOPIC 00136: RFmxWLAN_CfgNumberOfFrequencySegmentsAndReceiveChains

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__configuration__mimo_1gac008ed0fd58f45f03b99b79e20b0d204.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__configuration__mimo_1gac008ed0fd58f45f03b99b79e20b0d204.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of frequency segments and receive chains. Syntaxint32 __stdcall RFmxWLAN_CfgNumberOfFrequencySegmentsAndReceiveChains(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfFrequencySegments, int32 numberOfReceiveChains)ParametersNameDirectionTypeDescriptionin

### RFmxWLAN_CfgNumberOfFrequencySegmentsAndReceiveChains

Configures the number of frequency segments and receive chains.

#### Syntax

int32 __stdcall RFmxWLAN_CfgNumberOfFrequencySegmentsAndReceiveChains(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfFrequencySegments, int32 numberOfReceiveChains)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| numberOfFrequencySegments | [in] | int32 | This parameter specifies the number of frequency segments. The default value is 1. |
| numberOfReceiveChains | [in] | int32 | This parameter specifies the number of receive chains. The default value is 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Mimo

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga1d83fa1fda2cad585ceb87cf2c8f50ad.html language=enus -->
## TOPIC 00137: RFmxWLAN_DSSSModAccFetchEVMPerChipMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga1d83fa1fda2cad585ceb87cf2c8f50ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga1d83fa1fda2cad585ceb87cf2c8f50ad.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM per chip in the data field. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the EVM per chip computed for each averaging count. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccFetchEVMPerChipMeanTrace(niRFmxInstrHandle instrum

### RFmxWLAN_DSSSModAccFetchEVMPerChipMeanTrace

Fetches the EVM per chip in the data field. When you set the [RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__dsssmodacc__averaging_1ga3982601abeacbe78e61ff7a92eb29ac0.html) attribute to **True**, this function returns the mean of the EVM per chip computed for each averaging count.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccFetchEVMPerChipMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evmPerChipMean[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the index of the first chip. |
| dx | [out] | float64 * | This parameter returns the trace increment interval in number of chips. This value is always equal to 1. |
| evmPerChipMean | [out] | float32[] | This parameter returns an array of EVM per chip. When you set the RFMXWLAN_ATTR_DSSSMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit attribute to dB, the measurement returns this result in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga4801e74ba939c002c175771d2dd5b60b.html language=enus -->
## TOPIC 00138: RFmxWLAN_DSSSModAccFetchConstellationTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga4801e74ba939c002c175771d2dd5b60b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga4801e74ba939c002c175771d2dd5b60b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the data field. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescrip

### RFmxWLAN_DSSSModAccFetchConstellationTrace

Fetches the constellation trace for the data field.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| constellation | [out] | NIComplexSingle[] | This parameter returns the constellation of the received symbols. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga4b3f841774d5aaa138353be914cdf18d.html language=enus -->
## TOPIC 00139: RFmxWLAN_DSSSModAccFetchPeakPowers

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga4b3f841774d5aaa138353be914cdf18d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga4b3f841774d5aaa138353be914cdf18d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of various fields in the PPDU. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccFetchPeakPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *preamblePeakPowerMaximum, float64 *headerPeakPowerMaximum, float64 *dataPeakPowerMaximum, float64 *ppduP

### RFmxWLAN_DSSSModAccFetchPeakPowers

Fetches the peak power of various fields in the PPDU.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccFetchPeakPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *preamblePeakPowerMaximum, float64 *headerPeakPowerMaximum, float64 *dataPeakPowerMaximum, float64 *ppduPeakPowerMaximum)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| preamblePeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the preamble field of the PPDU. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this result returns the maximum of the peak preamble field power results computed for each averaging count. This value is expressed in dBm. |
| headerPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the header field of the PPDU. When you set the DSSSModAcc Averaging Enabled attribute to True, this result returns the maximum of the peak header field power results computed for each averaging count. This value is expressed in dBm. |
| dataPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the data field of the PPDU. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this result returns the maximum of the peak data field power results computed for each averaging count. This value is expressed in dBm. |
| ppduPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the PPDU. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the maximum of the peak PPDU power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga6b6a25c2d6eae5f23dfc9e0d102e7ed5.html language=enus -->
## TOPIC 00140: RFmxWLAN_DSSSModAccFetchEVM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga6b6a25c2d6eae5f23dfc9e0d102e7ed5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga6b6a25c2d6eae5f23dfc9e0d102e7ed5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM results for the DSSSModAcc measurement. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsEVMMean, float64 *peakEvm802112016Maximum, float64 *peakEvm802112007Maximum, float64 *peakEvm802111999Maxi

### RFmxWLAN_DSSSModAccFetchEVM

Fetches the EVM results for the DSSSModAcc measurement.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsEVMMean, float64 *peakEvm802112016Maximum, float64 *peakEvm802112007Maximum, float64 *peakEvm802111999Maximum, float64 *frequencyErrorMean, float64 *chipClockErrorMean, int32 *numberOfChipsUsed)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| rmsEVMMean | [out] | float64 * | This parameter returns the RMS EVM results of the burst. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this result returns the mean of the RMS EVM computed for each averaging count. When you set the RFMXWLAN_ATTR_DSSSMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit attribute to dB, the measurement returns this result in dB. |
| peakEvm802112016Maximum | [out] | float64 * | This parameter returns the peak EVM results of the burst. When you set the RFMXWLAN_ATTR_DSSSMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit attribute to dB, the measurement returns this result in dB. This measurement is performed in accordance with section 16.3.7.9 of IEEE Standard 802.11-2016. When you set the DSSSModAcc Averaging Enabled attribute to True, this result returns the maximum of the peak EVM computed for each averaging count. |
| peakEvm802112007Maximum | [out] | float64 * | This parameter returns the peak EVM results of the burst. When you set the RFMXWLAN_ATTR_DSSSMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit attribute to dB, the measurement returns this result in dB. This measurement is performed in accordance with section 18.4.7.8 of IEEE Standard 802.11-2007. When you set the DSSSModAcc Averaging Enabled attribute to True, this result returns the maximum of the peak EVM computed for each averaging count. |
| peakEvm802111999Maximum | [out] | float64 * | This parameter returns the peak EVM results of the burst. When you set the RFMXWLAN_ATTR_DSSSMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit attribute to dB, the measurement returns this result in dB. This measurement is performed in accordance with section 18.4.7.8 of IEEE Standard 802.11b-1999. When you set the DSSSModAcc Averaging Enabled attribute to True, this result returns the maximum of the peak EVM computed for each averaging count. |
| frequencyErrorMean | [out] | float64 * | This parameter returns the carrier frequency error of the transmitter. This value is expressed in Hz. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this result returns the mean of the carrier frequency error results computed for each averaging count. |
| chipClockErrorMean | [out] | float64 * | This parameter returns the chip clock error result of the transmitter. This value is expressed in parts per million (ppm). When you set the DSSSModAcc Averaging Enabled attribute to True, this result returns the mean of the chip clock error computed for each averaging count. |
| numberOfChipsUsed | [out] | int32 * | This parameter returns the number of chips used for the DSSSModAcc measurement. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga79290cf575644afa7703299e2657b306.html language=enus -->
## TOPIC 00141: RFmxWLAN_DSSSModAccFetchIQImpairments

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga79290cf575644afa7703299e2657b306.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1ga79290cf575644afa7703299e2657b306.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q Impairment results for the DSSSModAcc measurement. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffsetMean, float64 *iqGainImbalanceMean, float64 *iqQuadratureErrorMean)Paramet

### RFmxWLAN_DSSSModAccFetchIQImpairments

Fetches the I/Q Impairment results for the DSSSModAcc measurement.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffsetMean, float64 *iqGainImbalanceMean, float64 *iqQuadratureErrorMean)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| iqOriginOffsetMean | [out] | float64 * | This parameter returns the I/Q origin offset. This value is expressed in dB. I/Q origin offset is the ratio of the mean value of the signal to the RMS value of the signal. When you set the RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the mean of the I/Q origin offset results computed for each averaging count. |
| iqGainImbalanceMean | [out] | float64 * | This parameter returns the I/Q gain imbalance results. This value is expressed in dB. I/Q gain imbalance is the ratio of the mean amplitude of the in-phase (I) signal to the mean amplitude of the quadrature-phase (Q) signal. When you set the DSSSModAcc Averaging Enabled attribute to True, this parameter returns the mean of the I/Q gain imbalance results computed for each averaging count. |
| iqQuadratureErrorMean | [out] | float64 * | This parameter returns the I/Q quadrature error. This value is expressed in degrees. Quadrature error is the deviation in angle from 90 degrees between the in-phase (I) and quadrature-phase (Q) signals. When the DSSSModAcc Averaging Enabled attribute is set to True, this parameter returns the mean of the I/Q quadrature error results computed for each averaging count. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1gac020db21b544a8efc128b117b184cfb5.html language=enus -->
## TOPIC 00142: RFmxWLAN_DSSSModAccFetchPPDUInformation

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1gac020db21b544a8efc128b117b184cfb5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__dsssmodacc_1gac020db21b544a8efc128b117b184cfb5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PPDU information. Syntaxint32 __stdcall RFmxWLAN_DSSSModAccFetchPPDUInformation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *dataModulationFormat, int32 *payloadLength, int32 *preambleType, int32 *lockedClocksBit, int32 *headerCrcStatus, int32 *psduc

### RFmxWLAN_DSSSModAccFetchPPDUInformation

Fetches the PPDU information.

#### Syntax

int32 __stdcall RFmxWLAN_DSSSModAccFetchPPDUInformation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *dataModulationFormat, int32 *payloadLength, int32 *preambleType, int32 *lockedClocksBit, int32 *headerCrcStatus, int32 *psducrcStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| dataModulationFormat | [out] | int32 * | This parameter returns the data modulation format results of the analyzed waveform.NameValueDescriptionRFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_DSSS1MBPS0 (0x0)Indicates that the modulation format is DSSS and the data rate is 1 Mbps.RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_DSSS2MBPS1 (0x1)Indicates that the modulation format is DSSS and the data rate is 2 Mbps.RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_CCK5_5MBPS2 (0x2)Indicates that the modulation format is CCK and the data rate is 5.5 Mbps.RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_CCK11MBPS3 (0x3)Indicates that the modulation format is CCK and the data rate is 11 Mbps.RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC5_5MBPS4 (0x4)Indicates that the modulation format is PBCC and the data rate is 5.5 Mbps.RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC11MBPS5 (0x5)Indicates that the modulation format is PBCC and the data rate is 11 Mbps.RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC22MBPS6 (0x6)Indicates that the modulation format is PBCC and the data rate is 22 Mbps.RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC33MBPS7 (0x7)Indicates that the modulation format is PBCC and the data rate is 33 Mbps. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_DSSS1MBPS | 0 (0x0) | Indicates that the modulation format is DSSS and the data rate is 1 Mbps. |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_DSSS2MBPS | 1 (0x1) | Indicates that the modulation format is DSSS and the data rate is 2 Mbps. |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_CCK5_5MBPS | 2 (0x2) | Indicates that the modulation format is CCK and the data rate is 5.5 Mbps. |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_CCK11MBPS | 3 (0x3) | Indicates that the modulation format is CCK and the data rate is 11 Mbps. |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC5_5MBPS | 4 (0x4) | Indicates that the modulation format is PBCC and the data rate is 5.5 Mbps. |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC11MBPS | 5 (0x5) | Indicates that the modulation format is PBCC and the data rate is 11 Mbps. |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC22MBPS | 6 (0x6) | Indicates that the modulation format is PBCC and the data rate is 22 Mbps. |  |
| RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC33MBPS | 7 (0x7) | Indicates that the modulation format is PBCC and the data rate is 33 Mbps. |  |
| payloadLength | [out] | int32 * | This parameter returns the payload length of the acquired burst. This value is expressed in bytes. |
| preambleType | [out] | int32 * | This parameter returns the detected preamble type.NameValueDescriptionRFMXWLAN_VAL_DSSSMODACC_PREAMBLE_TYPE_LONG0 (0x0)Indicates that the PPDU has a long PHY preamble and header.RFMXWLAN_VAL_DSSSMODACC_PREAMBLE_TYPE_SHORT1 (0x1)Indicates that the PPDU has a short PHY preamble and header. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_DSSSMODACC_PREAMBLE_TYPE_LONG | 0 (0x0) | Indicates that the PPDU has a long PHY preamble and header. |  |
| RFMXWLAN_VAL_DSSSMODACC_PREAMBLE_TYPE_SHORT | 1 (0x1) | Indicates that the PPDU has a short PHY preamble and header. |  |
| lockedClocksBit | [out] | int32 * | This parameter returns the value of the locked clocks bit in the Long PHY SERVICE field. A value of 1 indicates that the transmit frequency and the symbol clock are derived from the same oscillator. A value of 0 indicates that the transmit frequency and the symbol clock are derived from independent oscillators. |
| headerCrcStatus | [out] | int32 * | This parameter returns whether the header CRC is successfully passed, as defined under section 16.2.3.7 of IEEE Standard 802.11 2016.NameValueDescriptionRFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_FAIL0 (0x0)Returns that the header CRC failed.RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_PASS1 (0x1)Returns that the header CRC passed. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_FAIL | 0 (0x0) | Returns that the header CRC failed. |  |
| RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_PASS | 1 (0x1) | Returns that the header CRC passed. |  |
| psducrcStatus | [out] | int32 * | This parameter returns whether the PLCP service data unit (PSDU) cyclic redundancy check (CRC) has successfully passed.NameValueDescriptionRFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_FAIL0 (0x0)Indicates that the PSDU CRC failed.RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_PASS1 (0x1)Indicates that the PSDU CRC passed. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_FAIL | 0 (0x0) | Indicates that the PSDU CRC failed. |  |
| RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_PASS | 1 (0x1) | Indicates that the PSDU CRC passed. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc.html language=enus -->
## TOPIC 00143: OFDMModAcc

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWLAN_OFDMModAccFetchChainDataRMSEVMPerSymbolMeanTraceFetches the chain data-subcarriers RMS EVM per symbol trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the chain data RMS EVM per symb

### OFDMModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWLAN_OFDMModAccFetchChainDataRMSEVMPerSymbolMeanTrace | Fetches the chain data-subcarriers RMS EVM per symbol trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the chain data RMS EVM per symbol computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace | Fetches the chain pilot-subcarriers RMS EVM per symbol trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the chain pilot RMS EVM per symbol computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchChainRMSEVM | Fetches the chain RMS EVM results. |
| RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace | Fetches the chain RMS EVM per subcarrier trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the chain RMS EVM per subcarrier computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSymbolMeanTrace | Fetches the chain RMS EVM per symbol trace. When you set the When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the chain RMS EVM per symbol computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchChannelFrequencyResponseMeanTrace | Fetches the channel frequency response trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the channel frequency response trace computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchCommonPilotErrorTrace | Fetches the common pilot error magnitude and phase traces. |
| RFmxWLAN_OFDMModAccFetchCompositeRMSEVM | Fetches the composite RMS EVM results. |
| RFmxWLAN_OFDMModAccFetchCrossPower | Fetches the cross power. |
| RFmxWLAN_OFDMModAccFetchCustomGatePowersArray | Fetches the average and peak power of the custom gates. |
| RFmxWLAN_OFDMModAccFetchDataAveragePower | Fetches the average power of the data field. |
| RFmxWLAN_OFDMModAccFetchDataConstellationTrace | Fetches the constellation trace for the data-subcarriers. |
| RFmxWLAN_OFDMModAccFetchDataConstellationTraceSplit | Fetches the constellation trace for the data-subcarriers. |
| RFmxWLAN_OFDMModAccFetchDataPeakPower | Fetches the peak power of the data field. |
| RFmxWLAN_OFDMModAccFetchDecodedEHTSIGBitsTrace | Fetches the decoded EHT-SIG bits trace. |
| RFmxWLAN_OFDMModAccFetchDecodedLSIGBitsTrace | Fetches the decoded L-SIG bits trace. |
| RFmxWLAN_OFDMModAccFetchDecodedPSDUBitsTrace | Fetches the decoded PLCP service data unit (PSDU) bits. |
| RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace | Fetches the decoded SIG-B bits. |
| RFmxWLAN_OFDMModAccFetchDecodedSIGBitsTrace | Fetches the decoded SIG bits. |
| RFmxWLAN_OFDMModAccFetchDecodedServiceBitsTrace | Fetches the decoded Service bits. |
| RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace | Fetches the decoded U-SIG bits trace. |
| RFmxWLAN_OFDMModAccFetchEVMSubcarrierIndices | Fetches the array of subcarrier indices for which the EVM results are computed. |
| RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent | Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations. |
| RFmxWLAN_OFDMModAccFetchFrequencyErrorMean | Fetches the carrier frequency error of the transmitter. |
| RFmxWLAN_OFDMModAccFetchGroupDelayMeanTrace | Fetches the group delay trace. Group delay is computed from the channel frequency response. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the group delay trace computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchGuardIntervalType | Fetches the guard interval type. |
| RFmxWLAN_OFDMModAccFetchIQGainImbalancePerSubcarrierMeanTrace | Fetches the I/Q gain imbalance per subcarrier trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the I/Q gain imbalance computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchIQImpairments | Fetches the I/Q Impairment results for the OFDMModAcc measurement. |
| RFmxWLAN_OFDMModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace | Fetches the I/Q quadrature error per subcarrier trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the I/Q quadrature error computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchLSIGParityCheckStatus | Fetches the L-SIG parity check status. |
| RFmxWLAN_OFDMModAccFetchLTFSize | Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively. |
| RFmxWLAN_OFDMModAccFetchMCSIndex | Fetches the MCS index. |
| RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols | Fetches the number of HE-SIG-B symbols. |
| RFmxWLAN_OFDMModAccFetchNumberOfSpaceTimeStreams | Fetches the number of space time streams. |
| RFmxWLAN_OFDMModAccFetchNumberOfUsers | Fetches the number of users. |
| RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed | Fetches the number of OFDM symbols used for EVM measurement. |
| RFmxWLAN_OFDMModAccFetchPEAveragePower | Fetches the average power of the packet extension field. |
| RFmxWLAN_OFDMModAccFetchPEDuration | Fetches the duration of the packet extension field. |
| RFmxWLAN_OFDMModAccFetchPEPeakPower | Fetches the peak power of the packet extension field. |
| RFmxWLAN_OFDMModAccFetchPPDUAveragePower | Fetches the average power of the PPDU. |
| RFmxWLAN_OFDMModAccFetchPPDUPeakPower | Fetches the peak power of the PPDU. |
| RFmxWLAN_OFDMModAccFetchPPDUType | Fetches the PPDU type. |
| RFmxWLAN_OFDMModAccFetchPSDUCRCStatus | Fetches the PLCP service data unit (PSDU) CRC status. |
| RFmxWLAN_OFDMModAccFetchPhaseNoisePSDMeanTrace | Fetches the phase noise power spectral density (PSD) trace for signals containing an OFDM payload. |
| RFmxWLAN_OFDMModAccFetchPilotConstellationTrace | Fetches the constellation trace for the pilot-subcarriers. |
| RFmxWLAN_OFDMModAccFetchPilotConstellationTraceSplit | Fetches the constellation trace for the pilot-subcarriers. |
| RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac | Fetches the average power of the 802.11ac specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ax | Fetches the average power of the 802.11ax specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11be | Fetches the average power of the 802.11be specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n | Fetches the average power of the 802.11n specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreambleAveragePowersCommon | Fetches the average power of the preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace | Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols. |
| RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ac | Fetches the peak power of the 802.11ac specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ax | Fetches the peak power of the 802.11ax specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11be | Fetches the peak power of the 802.11be specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11n | Fetches the peak power of the 802.11n specific preamble fields. |
| RFmxWLAN_OFDMModAccFetchPreamblePeakPowersCommon | Fetches the peak power of the preamble fields. |
| RFmxWLAN_OFDMModAccFetchRUOffsetAndSize | Fetches the RU offset and the RU size of the specified user. |
| RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTrace | Fetches the reference constellation trace for the data-subcarriers. |
| RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTraceSplit | Fetches the reference constellation trace for the data-subcarriers. |
| RFmxWLAN_OFDMModAccFetchSIGBCRCStatus | Fetches the SIG-B CRC Status. |
| RFmxWLAN_OFDMModAccFetchSIGCRCStatus | Fetches the SIG CRC Status. |
| RFmxWLAN_OFDMModAccFetchSpectralFlatness | Fetches the spectral flatness margin results. |
| RFmxWLAN_OFDMModAccFetchSpectralFlatnessMeanTrace | Fetches the spectral flatness trace, and the lower and upper spectral flatness mask traces. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the spectral flatness trace computed on the mean of the channel estimates computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchStreamDataRMSEVMPerSymbolMeanTrace | Fetches the stream data subcarriers RMS EVM per symbol trace. |
| RFmxWLAN_OFDMModAccFetchStreamPilotRMSEVMPerSymbolMeanTrace | Fetches the stream pilot subcarriers RMS EVM per symbol trace. |
| RFmxWLAN_OFDMModAccFetchStreamRMSEVM | Fetches the stream RMS EVM results. |
| RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace | Fetches the stream RMS EVM per subcarrier trace. |
| RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSymbolMeanTrace | Fetches the stream RMS EVM per symbol trace. |
| RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace | Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN. |
| RFmxWLAN_OFDMModAccFetchSubcarrierStreamEVMPerSymbolTrace | Fetches the stream EVM per symbol trace for a subcarrier. |
| RFmxWLAN_OFDMModAccFetchSymbolChainEVMPerSubcarrierTrace | Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. |
| RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean | Fetches the symbol clock error of the transmitter. |
| RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace | Fetches the stream EVM per subcarrier trace for a symbol. |
| RFmxWLAN_OFDMModAccFetchUnusedToneError | Fetches the unused tone error margin results. |
| RFmxWLAN_OFDMModAccFetchUnusedToneErrorMarginPerRU | Fetches the unused tone error margin result per RU. |
| RFmxWLAN_OFDMModAccFetchUnusedToneErrorMeanTrace | Fetches the unused tone error trace and the unused tone error mask trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the unused tone error computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchUserDataConstellationTrace | Fetches the constellation trace for the data-subcarriers of each user. |
| RFmxWLAN_OFDMModAccFetchUserDataConstellationTraceSplit | Fetches the constellation trace for the data-subcarriers of each user. |
| RFmxWLAN_OFDMModAccFetchUserPilotConstellationTrace | Fetches the constellation trace for the pilot-subcarriers of each user. |
| RFmxWLAN_OFDMModAccFetchUserPilotConstellationTraceSplit | Fetches the constellation trace for the pilot-subcarriers of each user. |
| RFmxWLAN_OFDMModAccFetchUserPower | Fetches the user power. |
| RFmxWLAN_OFDMModAccFetchUserStreamDataRMSEVMPerSymbolMeanTrace | Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the user stream data RMS EVM per symbol computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchUserStreamPilotRMSEVMPerSymbolMeanTrace | Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user. |
| RFmxWLAN_OFDMModAccFetchUserStreamRMSEVM | Fetches the stream RMS EVM results for the specified user. |
| RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSubcarrierMeanTrace | Fetches the stream RMS EVM per subcarrier trace for each user. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count. |
| RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSymbolMeanTrace | Fetches the stream RMS EVM per symbol trace for each user. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the user stream RMS EVM per symbol computed for each averaging count. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga003a5083263c507a2f39d98f3b36d3f3.html language=enus -->
## TOPIC 00144: RFmxWLAN_OFDMModAccFetchLSIGParityCheckStatus

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga003a5083263c507a2f39d98f3b36d3f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga003a5083263c507a2f39d98f3b36d3f3.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the L-SIG parity check status. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchLSIGParityCheckStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *lsigParityCheckStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramete

### RFmxWLAN_OFDMModAccFetchLSIGParityCheckStatus

Fetches the L-SIG parity check status.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchLSIGParityCheckStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *lsigParityCheckStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| lsigParityCheckStatus | [out] | int32 * | This parameter returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms.NameValueDescriptionRFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_NOT_APPLICABLE-1 (-0x1)Returns that the parity check is invalid for the current waveform.RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_FAIL0 (0x0)Returns that the parity check failed.RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_PASS1 (0x1)Returns that the parity check passed. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_NOT_APPLICABLE | -1 (-0x1) | Returns that the parity check is invalid for the current waveform. |  |
| RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_FAIL | 0 (0x0) | Returns that the parity check failed. |  |
| RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_PASS | 1 (0x1) | Returns that the parity check passed. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga01fda8a8813c5dd96c77a8048b58d05b.html language=enus -->
## TOPIC 00145: RFmxWLAN_OFDMModAccFetchUserStreamPilotRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga01fda8a8813c5dd96c77a8048b58d05b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga01fda8a8813c5dd96c77a8048b58d05b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamPilotRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 userStreamPilotRMSEVMPerSym

### RFmxWLAN_OFDMModAccFetchUserStreamPilotRMSEVMPerSymbolMeanTrace

Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamPilotRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 userStreamPilotRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0".Example:"user0/stream0""signal::sig1/user0/stream0""signal::sig1/result::r1/user0/stream0""result::r1/user0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns the OFDM symbol increment value. This value is always equal to 1. |
| userStreamPilotRMSEVMPerSymbolMean | [out] | float32[] | This parameter returns the stream pilot subcarriers RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga05f929560eb0d04a99908a5e79852c2f.html language=enus -->
## TOPIC 00146: RFmxWLAN_OFDMModAccFetchPPDUPeakPower

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga05f929560eb0d04a99908a5e79852c2f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga05f929560eb0d04a99908a5e79852c2f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the PPDU. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPPDUPeakPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *ppduPeakPowerMaximum)RemarksUse "segment<n>/chain<k>" as the selector string to read results from this function.Paramet

### RFmxWLAN_OFDMModAccFetchPPDUPeakPower

Fetches the peak power of the PPDU.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPPDUPeakPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *ppduPeakPowerMaximum)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| ppduPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the PPDU. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the maximum of the PPDU peak power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0622c52c2c14ddefcb465fd8c2722524.html language=enus -->
## TOPIC 00147: RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ac

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0622c52c2c14ddefcb465fd8c2722524.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0622c52c2c14ddefcb465fd8c2722524.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the 802.11ac specific preamble fields. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ac(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *vhtsigaPeakPowerMaximum, float64 *vhtstfPeakPowerMaximum, float64 *vhtltfPeak

### RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ac

Fetches the peak power of the 802.11ac specific preamble fields.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ac(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *vhtsigaPeakPowerMaximum, float64 *vhtstfPeakPowerMaximum, float64 *vhtltfPeakPowerMaximum, float64 *vhtsigbPeakPowerMaximum)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| vhtsigaPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the VHT-SIG-A field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this attribute returns the maximum of the VHT-SIG-A field peak power results computed for each averaging count. This value is expressed in dBm. |
| vhtstfPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the VHT-STF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the VHT-STF peak power results computed for each averaging count. This value is expressed in dBm. |
| vhtltfPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the VHT-LTF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the VHT-LTF peak power results computed for each averaging count. This value is expressed in dBm. |
| vhtsigbPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the VHT-SIG-B field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the VHT-SIG-B field peak power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0cdf6ece245cc9080658ef7cff672a55.html language=enus -->
## TOPIC 00148: RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0cdf6ece245cc9080658ef7cff672a55.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0cdf6ece245cc9080658ef7cff672a55.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the 802.11n specific preamble fields. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *htsigAveragePowerMean, float64 *htstfAveragePowerMean, float64 *htdltfAve

### RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n

Fetches the average power of the 802.11n specific preamble fields.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *htsigAveragePowerMean, float64 *htstfAveragePowerMean, float64 *htdltfAveragePowerMean, float64 *hteltfAveragePowerMean)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| htsigAveragePowerMean | [out] | float64 * | This parameter returns the average power of the HT-SIG field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the mean of the HT-SIG field average power results computed for each averaging count. This value is expressed in dBm. |
| htstfAveragePowerMean | [out] | float64 * | This parameter returns the average power of the HT-STF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the mean of the HT-STF average power results computed for each averaging count. This value is expressed in dBm. |
| htdltfAveragePowerMean | [out] | float64 * | This parameter returns the average power of the HT-DLTF. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the mean of the HT-DLTF average power results computed for each averaging count. This value is expressed in dBm. |
| hteltfAveragePowerMean | [out] | float64 * | This parameter returns the average power of the HT-ELTF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the mean of the HT-ELTF average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0f7fb57f03bc93d84698d5683a940486.html language=enus -->
## TOPIC 00149: RFmxWLAN_OFDMModAccFetchDecodedPSDUBitsTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0f7fb57f03bc93d84698d5683a940486.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga0f7fb57f03bc93d84698d5683a940486.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded PLCP service data unit (PSDU) bits. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedPSDUBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedPsduBits[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescripti

### RFmxWLAN_OFDMModAccFetchDecodedPSDUBitsTrace

Fetches the decoded PLCP service data unit (PSDU) bits.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedPSDUBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedPsduBits[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0".Example:"user0""signal::sig1/user0""signal::sig1/result::r1/user0""result::r1/user0"You can use the RFmxWLAN_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| decodedPsduBits | [out] | int32[] | This parameter returns an array of PSDU bits obtained after demodulation and decoding. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga10066ebaa74436ae59e10a657ebbe713.html language=enus -->
## TOPIC 00150: RFmxWLAN_OFDMModAccFetchPilotConstellationTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga10066ebaa74436ae59e10a657ebbe713.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga10066ebaa74436ae59e10a657ebbe713.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the pilot-subcarriers. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPilotConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pilotConstellation[], int32 arraySize, int32 *actualArraySize)RemarksUse "segme

### RFmxWLAN_OFDMModAccFetchPilotConstellationTrace

Fetches the constellation trace for the pilot-subcarriers.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPilotConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle pilotConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| pilotConstellation | [out] | NIComplexSingle[] | This parameter returns the demodulated QAM symbols from all the pilot-subcarriers in all OFDM symbols. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga189866e67249ecf02a47bd7f3fd96b73.html language=enus -->
## TOPIC 00151: RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga189866e67249ecf02a47bd7f3fd96b73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga189866e67249ecf02a47bd7f3fd96b73.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded SIG-B bits. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedSigbBits[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]ni

### RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace

Fetches the decoded SIG-B bits.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedSigbBits[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| decodedSigbBits | [out] | int32[] | This parameter returns an array of bits in the VHT-SIG-B field of the 802.11ac waveform or the HE-SIG-B field of the 802.11ax waveform. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga18daafa5ec56120e6c289636369e9adc.html language=enus -->
## TOPIC 00152: RFmxWLAN_OFDMModAccFetchDataConstellationTraceSplit

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga18daafa5ec56120e6c289636369e9adc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga18daafa5ec56120e6c289636369e9adc.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the data-subcarriers. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 dataConstellationI[], float32 dataConstellationQ[], int32 arraySize, int32 *actualAr

### RFmxWLAN_OFDMModAccFetchDataConstellationTraceSplit

Fetches the constellation trace for the data-subcarriers.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 dataConstellationI[], float32 dataConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| dataConstellationI | [out] | float32[] | This parameter Returns the real part of demodulated QAM symbols from all the data-subcarriers in all the OFDM symbols. |
| dataConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of demodulated QAM symbols from all the data-subcarriers in all the OFDM symbols. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga19bfc5824a7d66118baf12731a88acd1.html language=enus -->
## TOPIC 00153: RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga19bfc5824a7d66118baf12731a88acd1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga19bfc5824a7d66118baf12731a88acd1.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream EVM per subcarrier trace for a symbol. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 symbolIndex, float64 *x0, float64 *dx, float32 symbolStreamEVMPerSubcarrier[], i

### RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace

Fetches the stream EVM per subcarrier trace for a symbol.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 symbolIndex, float64 *x0, float64 *dx, float32 symbolStreamEVMPerSubcarrier[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| symbolIndex | [in] | int32 | This parameter specifies the symbol index for which to fetch the trace. The default value is 0. |
| x0 | [out] | float64 * | This parameter returns the starting subcarrier index. |
| dx | [out] | float64 * | This parameter returns the subcarrier increment value. This value is always 1. |
| symbolStreamEVMPerSubcarrier | [out] | float32[] | This parameter returns the stream EVM for each subcarrier for the specified symbol index. This value is expressed as a percentage or in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga1dbed4a0ecbd4cc4d48a7a921a6747a2.html language=enus -->
## TOPIC 00154: RFmxWLAN_OFDMModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga1dbed4a0ecbd4cc4d48a7a921a6747a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga1dbed4a0ecbd4cc4d48a7a921a6747a2.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q quadrature error per subcarrier trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the I/Q quadrature error computed for each averaging count. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchIQQuadratureErrorPerSubcar

### RFmxWLAN_OFDMModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace

Fetches the I/Q quadrature error per subcarrier trace. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this function returns the mean of the I/Q quadrature error computed for each averaging count.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 iqQuadratureErrorPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting subcarrier index. |
| dx | [out] | float64 * | This parameter returns the subcarrier increment value. This value is always 1. |
| iqQuadratureErrorPerSubcarrierMean | [out] | float32[] | This parameter returns an array of I/Q quadrature errors for each subcarrier. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga2391eee8a3af945c73ba62d3ad5aa253.html language=enus -->
## TOPIC 00155: RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga2391eee8a3af945c73ba62d3ad5aa253.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga2391eee8a3af945c73ba62d3ad5aa253.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM per subcarrier trace. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 streamRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *act

### RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace

Fetches the stream RMS EVM per subcarrier trace.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 streamRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting subcarrier index. |
| dx | [out] | float64 * | This parameter returns the subcarrier increment value. This value is always 1. |
| streamRMSEVMPerSubcarrierMean | [out] | float32[] | This parameter returns the stream RMS EVM for each subcarrier. This value is expressed as a percentage or in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga317b5bce75796894ec4c825b87954424.html language=enus -->
## TOPIC 00156: RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga317b5bce75796894ec4c825b87954424.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga317b5bce75796894ec4c825b87954424.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *freque

### RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent

Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *frequencyErrorCcdf10Percent)

#### Remarks

Use "segment<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0".Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxWLAN_BuildSegmentString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| frequencyErrorCcdf10Percent | [out] | float64 * | This parameter returns the 10% point of the CCDF of absolute frequency error. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, the CCDF is computed over each averaging count. This value is expressed in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga3fd201ad625688511c33c362cafa1a6f.html language=enus -->
## TOPIC 00157: RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga3fd201ad625688511c33c362cafa1a6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga3fd201ad625688511c33c362cafa1a6f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM per subcarrier trace for each user. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchUser

### RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSubcarrierMeanTrace

Fetches the stream RMS EVM per subcarrier trace for each user. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this function returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 userStreamRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "user<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0".Example:"user0/stream0""signal::sig1/user0/stream0""signal::sig1/result::r1/user0/stream0""result::r1/user0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting subcarrier index. |
| dx | [out] | float64 * | This parameter returns the subcarrier increment value. This value is always 1. |
| userStreamRMSEVMPerSubcarrierMean | [out] | float32[] | This parameter returns the user stream RMS EVM for each subcarrier. This value is expressed as a percentage or in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga46857058ebbaddfc06a646b6284a46c0.html language=enus -->
## TOPIC 00158: RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga46857058ebbaddfc06a646b6284a46c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga46857058ebbaddfc06a646b6284a46c0.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 subcarrierIndex, float64 *x0,

### RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace

Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 subcarrierIndex, float64 *x0, float64 *dx, float32 subcarrierChainEVMPerSymbol[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| subcarrierIndex | [in] | int32 | This parameter specifies the subcarrier index for which the trace is fetched. The default value is 0. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns the OFDM symbol increment value. This value is always equal to 1. |
| subcarrierChainEVMPerSymbol | [out] | float32[] | This parameter returns an array of chain EVM of each OFDM symbol for the specified subcarrier index. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit attribute to dB, the measurement returns this result in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga501220d8aabee27cd1ef4456483c72da.html language=enus -->
## TOPIC 00159: RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga501220d8aabee27cd1ef4456483c72da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga501220d8aabee27cd1ef4456483c72da.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of HE-SIG-B symbols. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfHesigbSymbols)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis paramet

### RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols

Fetches the number of HE-SIG-B symbols.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfHesigbSymbols)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| numberOfHesigbSymbols | [out] | int32 * | This parameter returns the number of HE-SIG-B symbols. This result is applicable for 802.11ax MU PPDU signals, and is decoded from the HE-SIG-A field. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5624605f5695fd6e88c3a0b7619cf417.html language=enus -->
## TOPIC 00160: RFmxWLAN_OFDMModAccFetchNumberOfSpaceTimeStreams

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5624605f5695fd6e88c3a0b7619cf417.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5624605f5695fd6e88c3a0b7619cf417.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of space time streams. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfSpaceTimeStreams(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfSpaceTimeStreams)RemarksUse "user<n>" as the selector string to read results from this function.

### RFmxWLAN_OFDMModAccFetchNumberOfSpaceTimeStreams

Fetches the number of space time streams.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfSpaceTimeStreams(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfSpaceTimeStreams)

#### Remarks

Use "user<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0".Example:"user0""signal::sig1/user0""signal::sig1/result::r1/user0""result::r1/user0"You can use the RFmxWLAN_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| numberOfSpaceTimeStreams | [out] | int32 * | This parameter returns the number of space time streams. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga56b75a963137e419fcb317d826e56db8.html language=enus -->
## TOPIC 00161: RFmxWLAN_OFDMModAccFetchIQGainImbalancePerSubcarrierMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga56b75a963137e419fcb317d826e56db8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga56b75a963137e419fcb317d826e56db8.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q gain imbalance per subcarrier trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the I/Q gain imbalance computed for each averaging count. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchIQGainImbalancePerSubcarrierMe

### RFmxWLAN_OFDMModAccFetchIQGainImbalancePerSubcarrierMeanTrace

Fetches the I/Q gain imbalance per subcarrier trace. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this function returns the mean of the I/Q gain imbalance computed for each averaging count.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchIQGainImbalancePerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 iqGainImbalancePerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting subcarrier index. |
| dx | [out] | float64 * | This parameter returns the subcarrier increment value. This value is always 1. |
| iqGainImbalancePerSubcarrierMean | [out] | float32[] | This parameter returns an array of I/Q gain imbalance for each subcarrier. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga57014d965880b8ff0a95e7495cfdd936.html language=enus -->
## TOPIC 00162: RFmxWLAN_OFDMModAccFetchSIGCRCStatus

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga57014d965880b8ff0a95e7495cfdd936.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga57014d965880b8ff0a95e7495cfdd936.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SIG CRC Status. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchSIGCRCStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *sigcrcStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxWLAN_OFDMModAccFetchSIGCRCStatus

Fetches the SIG CRC Status.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchSIGCRCStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *sigcrcStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| sigcrcStatus | [out] | int32 * | This parameter returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform.NameValueDescriptionRFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE-1 (-0x1)Returns that the SIG CRC is invalid for the current waveform.RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_FAIL0 (0x0)Returns that the SIG CRC failed.RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_PASS1 (0x1)Returns that the SIG CRC passed. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE | -1 (-0x1) | Returns that the SIG CRC is invalid for the current waveform. |  |
| RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_FAIL | 0 (0x0) | Returns that the SIG CRC failed. |  |
| RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_PASS | 1 (0x1) | Returns that the SIG CRC passed. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5c17de3c63369e51bfc15dc5e76c3aab.html language=enus -->
## TOPIC 00163: RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5c17de3c63369e51bfc15dc5e76c3aab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5c17de3c63369e51bfc15dc5e76c3aab.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols. Syntaxint32 __stdcall RF

### RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace

Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 preambleFrequencyError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time in seconds. |
| dx | [out] | float64 * | This parameter returns the time increment value. This value is the reciprocal of OFDM ModAcc processing rate. |
| preambleFrequencyError | [out] | float32[] | This parameter returns the preamble frequency error at every sampling time. This value is expressed in Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5ee0a93bf494ed457061d45176f8d37a.html language=enus -->
## TOPIC 00164: RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5ee0a93bf494ed457061d45176f8d37a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga5ee0a93bf494ed457061d45176f8d37a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chain pilot-subcarriers RMS EVM per symbol trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the chain pilot RMS EVM per symbol computed for each averaging count. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchChainPilo

### RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace

Fetches the chain pilot-subcarriers RMS EVM per symbol trace. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this function returns the mean of the chain pilot RMS EVM per symbol computed for each averaging count.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chainPilotRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns the OFDM symbol increment value. This value is always equal to 1. |
| chainPilotRMSEVMPerSymbolMean | [out] | float32[] | This parameter returns an array of chain pilot-subcarriers RMS EVM of each OFDM symbol. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit attribute to dB, the measurement returns this result in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga6252c955d160c6a6d320ed356ed2d2ed.html language=enus -->
## TOPIC 00165: RFmxWLAN_OFDMModAccFetchMCSIndex

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga6252c955d160c6a6d320ed356ed2d2ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga6252c955d160c6a6d320ed356ed2d2ed.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the MCS index. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchMCSIndex(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *mcsIndex)RemarksUse "user<n>" as the selector string to read results from this function.ParametersNameDirectionTypeDescriptioninstrumentHan

### RFmxWLAN_OFDMModAccFetchMCSIndex

Fetches the MCS index.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchMCSIndex(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *mcsIndex)

#### Remarks

Use "user<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0".Example:"user0""signal::sig1/user0""signal::sig1/result::r1/user0""result::r1/user0"You can use the RFmxWLAN_BuildUserString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| mcsIndex | [out] | int32 * | This parameter returns the MCS index or the data rate. The MCS index or data rate for various standard signals are decoded as follows:StandardField802.11a, 802.11j, 802.11pThe data rate is decoded from the SIGNAL field.802.11nThe MCS index is decoded from the HT-SIG field.802.11acThe MCS index is decoded from the VHT-SIG-A field.802.11ax SU and Extended Range SU PPDUThe MCS index is decoded from the HE-SIG-A field.802.11ax MU PPDUThe MCS index is decoded from the HE-SIG-B field.802.11be MU PPDUThe MCS index is decoded from the EHT-SIG field.802.11bn MU PPDUThe MCS index is decoded from the UHR-SIG field.802.11bn ELR PPDUThe MCS index is decoded from the ELR-SIG field.For 802.11a, 802.11j, and 802.11p signals, the following MCS indices corresponds to their data rates:MCSData Rate01.5 Mbps, 3 Mbps, and 6 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively.12.25 Mbps, 4.5 Mbps, and 9 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively.23 Mbps, 6 Mbps, and 12 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively.34.5 Mbps, 9 Mbps, and 18 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively.46 Mbps, 12 Mbps, and 24 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively.59 Mbps, 18 Mbps, and 36 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively.612 Mbps, 24 Mbps, and 48 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively.713.5 Mbps, 27 Mbps, and 54 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| Standard | Field |  |  |
| 802.11a, 802.11j, 802.11p | The data rate is decoded from the SIGNAL field. |  |  |
| 802.11n | The MCS index is decoded from the HT-SIG field. |  |  |
| 802.11ac | The MCS index is decoded from the VHT-SIG-A field. |  |  |
| 802.11ax SU and Extended Range SU PPDU | The MCS index is decoded from the HE-SIG-A field. |  |  |
| 802.11ax MU PPDU | The MCS index is decoded from the HE-SIG-B field. |  |  |
| 802.11be MU PPDU | The MCS index is decoded from the EHT-SIG field. |  |  |
| 802.11bn MU PPDU | The MCS index is decoded from the UHR-SIG field. |  |  |
| 802.11bn ELR PPDU | The MCS index is decoded from the ELR-SIG field. |  |  |
| MCS | Data Rate |  |  |
| 0 | 1.5 Mbps, 3 Mbps, and 6 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |
| 1 | 2.25 Mbps, 4.5 Mbps, and 9 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |
| 2 | 3 Mbps, 6 Mbps, and 12 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |
| 3 | 4.5 Mbps, 9 Mbps, and 18 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |
| 4 | 6 Mbps, 12 Mbps, and 24 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |
| 5 | 9 Mbps, 18 Mbps, and 36 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |
| 6 | 12 Mbps, 24 Mbps, and 48 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |
| 7 | 13.5 Mbps, 27 Mbps, and 54 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga7112e71eea727dabd17ffdf128c15888.html language=enus -->
## TOPIC 00166: RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga7112e71eea727dabd17ffdf128c15888.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga7112e71eea727dabd17ffdf128c15888.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol clock error of the transmitter. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *symbolClockErrorMean)RemarksUse "segment<n>" as the selector string to read results from this fun

### RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean

Fetches the symbol clock error of the transmitter.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *symbolClockErrorMean)

#### Remarks

Use "segment<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0".Example:"segment0""signal::sig1/segment0""result::r1/segment0""signal::sig1/result::r1/segment0"You can use the RFmxWLAN_BuildSegmentString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| symbolClockErrorMean | [out] | float64 * | This parameter returns the symbol clock error of the transmitter. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the mean of the symbol clock error results computed for each averaging count. This value is expressed in parts per million (ppm). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga79f9cf7cec62128636a2ad9d280140a5.html language=enus -->
## TOPIC 00167: RFmxWLAN_OFDMModAccFetchPPDUType

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga79f9cf7cec62128636a2ad9d280140a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga79f9cf7cec62128636a2ad9d280140a5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PPDU type. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPPDUType(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *ppDUTYpe)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instr

### RFmxWLAN_OFDMModAccFetchPPDUType

Fetches the PPDU type.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPPDUType(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *ppDUTYpe)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| ppDUTYpe | [out] | int32 * | This parameter returns the PPDU type.NameValueDescriptionRFMXWLAN_VAL_OFDM_PPDU_TYPE_NON_HT0 (0x0)Specifies an 802.11a, 802.11j, or 802.11p PPDU type, or 802.11n, 802.11ac, or 802.11ax PPDU type when operating in the Non-HT mode.RFMXWLAN_VAL_OFDM_PPDU_TYPE_MIXED1 (0x1)Specifies the HT-Mixed PPDU (802.11n) type.RFMXWLAN_VAL_OFDM_PPDU_TYPE_GREENFIELD2 (0x2)Specifies the HT-Greenfield PPDU (802.11n) type.RFMXWLAN_VAL_OFDM_PPDU_TYPE_SU3 (0x3)Specifies the VHT SU PPDU type if you set the RFMXWLAN_ATTR_STANDARD attribute to 802.11ac or the HE SU PPDU type if you set the Standard attribute to 802.11ax.RFMXWLAN_VAL_OFDM_PPDU_TYPE_MU4 (0x4)Specifies the VHT MU PPDU type if you set the Standard attribute to 802.11ac, the HE MU PPDU type if you set the Standard attribute to 802.11ax, or the EHT MU PPDU type if you set the Standard attribute to 802.11be.RFMXWLAN_VAL_OFDM_PPDU_TYPE_EXTENDED_RANGE_SU5 (0x5)Specifies the HE Extended Range SU PPDU (802.11ax) type.RFMXWLAN_VAL_OFDM_PPDU_TYPE_TRIGGER_BASED6 (0x6)Specifies the HE TB PPDU if you set the Standard attribute to 802.11ax , the EHT TB PPDU if you set the Standard attribute to 802.11be or the UHR TB PPDU if you set the Standard attribute to 802.11bn .RFMXWLAN_VAL_OFDM_PPDU_TYPE_ELR7 (0x7) |
| Name | Value | Description |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_NON_HT | 0 (0x0) | Specifies an 802.11a, 802.11j, or 802.11p PPDU type, or 802.11n, 802.11ac, or 802.11ax PPDU type when operating in the Non-HT mode. |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_MIXED | 1 (0x1) | Specifies the HT-Mixed PPDU (802.11n) type. |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_GREENFIELD | 2 (0x2) | Specifies the HT-Greenfield PPDU (802.11n) type. |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_SU | 3 (0x3) | Specifies the VHT SU PPDU type if you set the RFMXWLAN_ATTR_STANDARD attribute to 802.11ac or the HE SU PPDU type if you set the Standard attribute to 802.11ax. |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_MU | 4 (0x4) | Specifies the VHT MU PPDU type if you set the Standard attribute to 802.11ac, the HE MU PPDU type if you set the Standard attribute to 802.11ax, or the EHT MU PPDU type if you set the Standard attribute to 802.11be. |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_EXTENDED_RANGE_SU | 5 (0x5) | Specifies the HE Extended Range SU PPDU (802.11ax) type. |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_TRIGGER_BASED | 6 (0x6) | Specifies the HE TB PPDU if you set the Standard attribute to 802.11ax , the EHT TB PPDU if you set the Standard attribute to 802.11be or the UHR TB PPDU if you set the Standard attribute to 802.11bn . |  |
| RFMXWLAN_VAL_OFDM_PPDU_TYPE_ELR | 7 (0x7) |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga82642e4da7d8cb38481b26838570800b.html language=enus -->
## TOPIC 00168: RFmxWLAN_OFDMModAccFetchPSDUCRCStatus

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga82642e4da7d8cb38481b26838570800b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga82642e4da7d8cb38481b26838570800b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PLCP service data unit (PSDU) CRC status. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPSDUCRCStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *psducrcStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter

### RFmxWLAN_OFDMModAccFetchPSDUCRCStatus

Fetches the PLCP service data unit (PSDU) CRC status.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPSDUCRCStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *psducrcStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| psducrcStatus | [out] | int32 * | This parameter returns the PSDU CRC status.NameValueDescriptionRFMXWLAN_VAL_OFDMMODACC_PSDU_CRC_STATUS_FAIL0 (0x0)Indicates that the PSDU CRC failed.RFMXWLAN_VAL_OFDMMODACC_PSDU_CRC_STATUS_PASS1 (0x1)Indicates that the PSDU CRC passed. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_OFDMMODACC_PSDU_CRC_STATUS_FAIL | 0 (0x0) | Indicates that the PSDU CRC failed. |  |
| RFMXWLAN_VAL_OFDMMODACC_PSDU_CRC_STATUS_PASS | 1 (0x1) | Indicates that the PSDU CRC passed. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga96b97d44b9de427d30ba259c188e9663.html language=enus -->
## TOPIC 00169: RFmxWLAN_OFDMModAccFetchDecodedSIGBitsTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga96b97d44b9de427d30ba259c188e9663.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga96b97d44b9de427d30ba259c188e9663.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded SIG bits. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedSIGBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedSigBits[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmx

### RFmxWLAN_OFDMModAccFetchDecodedSIGBitsTrace

Fetches the decoded SIG bits.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedSIGBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedSigBits[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| decodedSigBits | [out] | int32[] | This parameter returns an array of bits in the HT-SIG field of the 802.11n waveform, the VHT-SIG-A field of the 802.11ac waveform, or the HE-SIG-A field of the 802.11ax waveform. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga9986ed095c418d38d0122435f3a3ec2d.html language=enus -->
## TOPIC 00170: RFmxWLAN_OFDMModAccFetchLTFSize

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga9986ed095c418d38d0122435f3a3ec2d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga9986ed095c418d38d0122435f3a3ec2d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchLTFSize(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *ltfSize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxWLAN_OFDMModAccFetchLTFSize

Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchLTFSize(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *ltfSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| ltfSize | [out] | int32 * | This parameter returns the HE-LTF or EHT-LTF size. This result is applicable only to 802.11ax and 802.11be signals.NameValueDescriptionRFMXWLAN_VAL_OFDM_LTF_SIZE_4X0 (0x0)Specifies that the LTF symbol size is 4x.RFMXWLAN_VAL_OFDM_LTF_SIZE_2X1 (0x1)Specifies that the LTF symbol size is 2x.RFMXWLAN_VAL_OFDM_LTF_SIZE_1X2 (0x2)Specifies that the LTF symbol size is 1x.RFMXWLAN_VAL_OFDM_LTF_SIZE_NOT_APPLICABLE-1 (-0x1)Specifies that the LTF Size is invalid for the current waveform. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_4X | 0 (0x0) | Specifies that the LTF symbol size is 4x. |  |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_2X | 1 (0x1) | Specifies that the LTF symbol size is 2x. |  |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_1X | 2 (0x2) | Specifies that the LTF symbol size is 1x. |  |
| RFMXWLAN_VAL_OFDM_LTF_SIZE_NOT_APPLICABLE | -1 (-0x1) | Specifies that the LTF Size is invalid for the current waveform. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga9a74e2a944d22b0fd5f834cc22bf2866.html language=enus -->
## TOPIC 00171: RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11n

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga9a74e2a944d22b0fd5f834cc22bf2866.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1ga9a74e2a944d22b0fd5f834cc22bf2866.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the 802.11n specific preamble fields. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11n(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *htsigPeakPowerMaximum, float64 *htstfPeakPowerMaximum, float64 *htdltfPeakPower

### RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11n

Fetches the peak power of the 802.11n specific preamble fields.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11n(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *htsigPeakPowerMaximum, float64 *htstfPeakPowerMaximum, float64 *htdltfPeakPowerMaximum, float64 *hteltfPeakPowerMaximum)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| htsigPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HT-SIG field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the maximum of the HT-SIG field peak power results computed for each averaging count. This value is expressed in dBm. |
| htstfPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HT-STF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the HT-STF peak power results computed for each averaging count. This value is expressed in dBm. |
| htdltfPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HT-DLTF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the HT-DLTF peak power results computed for each averaging count. This value is expressed in dBm. |
| hteltfPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HT-ELTF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the HT-ELTF peak power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaa532e25165463cfb175f02fc95767bb6.html language=enus -->
## TOPIC 00172: RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaa532e25165463cfb175f02fc95767bb6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaa532e25165463cfb175f02fc95767bb6.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the 802.11ac specific preamble fields. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *vhtsigaAveragePowerMean, float64 *vhtstfAveragePowerMean, float64 *vhtl

### RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac

Fetches the average power of the 802.11ac specific preamble fields.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *vhtsigaAveragePowerMean, float64 *vhtstfAveragePowerMean, float64 *vhtltfAveragePowerMean, float64 *vhtsigbAveragePowerMean)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| vhtsigaAveragePowerMean | [out] | float64 * | This parameter returns the average power of the VHT-SIG-A field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the mean of the VHT-SIG-A field average power results computed for each averaging count. This value is expressed in dBm. |
| vhtstfAveragePowerMean | [out] | float64 * | This parameter returns the average power of the VHT-STF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this paramter returns the mean of the VHT-STF average power results computed for each averaging count. This value is expressed in dBm. |
| vhtltfAveragePowerMean | [out] | float64 * | This parameter returns the average power of the VHT-LTF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this paramter returns the mean of the VHT-LTF average power results computed for each averaging count. This value is expressed in dBm. |
| vhtsigbAveragePowerMean | [out] | float64 * | This parameter returns the average power of the VHT-SIG-B field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the mean of the VHT-SIG-B field average power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaafa9084938f15bb17890099c01ea976f.html language=enus -->
## TOPIC 00173: RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTraceSplit

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaafa9084938f15bb17890099c01ea976f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaafa9084938f15bb17890099c01ea976f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference constellation trace for the data-subcarriers. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 referenceDataConstellationI[], float32 referenceDataConstellation

### RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTraceSplit

Fetches the reference constellation trace for the data-subcarriers.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 referenceDataConstellationI[], float32 referenceDataConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| referenceDataConstellationI | [out] | float32[] | This parameter Returns the real part of reference QAM symbols for all the data-subcarriers in all the OFDM symbols. |
| referenceDataConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of reference QAM symbols for all the data-subcarriers in all the OFDM symbols. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gab107fa9827675703a71690d3f2b9ea12.html language=enus -->
## TOPIC 00174: RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gab107fa9827675703a71690d3f2b9ea12.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gab107fa9827675703a71690d3f2b9ea12.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference constellation trace for the data-subcarriers. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle referenceDataConstellation[], int32 arraySize, int32 *actualAr

### RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTrace

Fetches the reference constellation trace for the data-subcarriers.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle referenceDataConstellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| referenceDataConstellation | [out] | NIComplexSingle[] | This parameter returns the reference QAM symbols for all the data-subcarriers in all the OFDM symbols. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gab2df5cfc11b42a52b1bf887877732ef5.html language=enus -->
## TOPIC 00175: RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gab2df5cfc11b42a52b1bf887877732ef5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gab2df5cfc11b42a52b1bf887877732ef5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of OFDM symbols used for EVM measurement. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfSymbolsUsed)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrH

### RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed

Fetches the number of OFDM symbols used for EVM measurement.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfSymbolsUsed)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| numberOfSymbolsUsed | [out] | int32 * | This parameter returns the number of OFDM symbols used by the measurement. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gabcc73fd1c81ef27efd655fc5bce2e440.html language=enus -->
## TOPIC 00176: RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gabcc73fd1c81ef27efd655fc5bce2e440.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gabcc73fd1c81ef27efd655fc5bce2e440.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded U-SIG bits trace. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedUsigBits[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle

### RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace

Fetches the decoded U-SIG bits trace.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 decodedUsigBits[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| decodedUsigBits | [out] | int32[] | This parameter returns the array of bits in the U-SIG field of the 802.11be/802.11bn waveform for all 80 MHz subblocks. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gad65947d97b972bbcfdddd51e1318e5ba.html language=enus -->
## TOPIC 00177: RFmxWLAN_OFDMModAccFetchSpectralFlatness

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gad65947d97b972bbcfdddd51e1318e5ba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gad65947d97b972bbcfdddd51e1318e5ba.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectral flatness margin results. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchSpectralFlatness(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *spectralFlatnessMargin, int32 *spectralFlatnessMarginSubcarrierIndex)RemarksUse "segment<n>/chain<k>/strea

### RFmxWLAN_OFDMModAccFetchSpectralFlatness

Fetches the spectral flatness margin results.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchSpectralFlatness(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *spectralFlatnessMargin, int32 *spectralFlatnessMarginSubcarrierIndex)

#### Remarks

Use "segment<n>/chain<k>/stream<<i>l</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, chain number, and stream number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/stream0".Example:"segment0/chain0/stream0""signal::sig1/segment0/chain0/stream0""signal::sig1/result::r1/segment0/chain0/stream0""result::r1/segment0/chain0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| spectralFlatnessMargin | [out] | float64 * | This parameter returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. The upper spectral flatness margin is the minimum difference between the upper mask and the spectral flatness across subcarriers. The lower spectral flatness margin is the minimum difference between the spectral flatness and the lower mask across subcarriers. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, the spectral flatness is computed using the mean of the channel frequency response magnitude computed for each averaging count. This value is expressed in dB. |
| spectralFlatnessMarginSubcarrierIndex | [out] | int32 * | This parameter returns the subcarrier index corresponding to the Spectral Flatness Margin parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gadb8aadd315657c3e494a1953ef2dda1b.html language=enus -->
## TOPIC 00178: RFmxWLAN_OFDMModAccFetchUnusedToneError

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gadb8aadd315657c3e494a1953ef2dda1b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gadb8aadd315657c3e494a1953ef2dda1b.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the unused tone error margin results. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *unusedToneErrorMargin, int32 *unusedToneErrorMarginRuIndex)RemarksRefer to Unused Tone Error Mx for more in

### RFmxWLAN_OFDMModAccFetchUnusedToneError

Fetches the unused tone error margin results.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *unusedToneErrorMargin, int32 *unusedToneErrorMarginRuIndex)

#### Remarks

Refer to [Unused Tone Error Mx](https://www.ni.com/docs/en-US/bundle/rfmx-wlan/page/unused-tone-error-mx.html) for more information.

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| unusedToneErrorMargin | [out] | float64 * | This parameter returns the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB. |
| unusedToneErrorMarginRuIndex | [out] | int32 * | This parameter returns the 26-tone RU index corresponding to the Unused Tone Error Margin parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaee31cc7ccf429114d637b732e5b0cc88.html language=enus -->
## TOPIC 00179: RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaee31cc7ccf429114d637b732e5b0cc88.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaee31cc7ccf429114d637b732e5b0cc88.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chain RMS EVM per subcarrier trace. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this function returns the mean of the chain RMS EVM per subcarrier computed for each averaging count. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSubcarrierM

### RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace

Fetches the chain RMS EVM per subcarrier trace. When you set the [RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED](group____root__ni_r_fmx_w_l_a_n__attributes__ofdmmodacc__averaging_1ga9a2117a7db867d286a0784ee2d51a189.html) attribute to **True**, this function returns the mean of the chain RMS EVM per subcarrier computed for each averaging count.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chainRMSEVMPerSubcarrierMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting subcarrier index. |
| dx | [out] | float64 * | This parameter returns the subcarrier increment value. This value is always 1. |
| chainRMSEVMPerSubcarrierMean | [out] | float32[] | This parameter returns an array of chain RMS EVM of each subcarrier. When you set the RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT attribute to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit attribute to dB, the measurement returns this result in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaee5b5159cf826c895aad845de3d3b98e.html language=enus -->
## TOPIC 00180: RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ax

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaee5b5159cf826c895aad845de3d3b98e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaee5b5159cf826c895aad845de3d3b98e.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the 802.11ax specific preamble fields. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ax(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rlsigPeakPowerMaximum, float64 *hesigaPeakPowerMaximum, float64 *hesigbPeakPo

### RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ax

Fetches the peak power of the 802.11ax specific preamble fields.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ax(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rlsigPeakPowerMaximum, float64 *hesigaPeakPowerMaximum, float64 *hesigbPeakPowerMaximum, float64 *hestfPeakPowerMaximum, float64 *heltfPeakPowerMaximum)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| rlsigPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the RL-SIG field. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the maximum of the RL-SIG field peak power results computed for each averaging count. This value is expressed in dBm. |
| hesigaPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HE-SIG-A field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the HE-SIG-A field peak power results computed for each averaging count. This value is expressed in dBm. |
| hesigbPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HE-SIG-B field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the HE-SIG-B field peak power results computed for each averaging count. This value is expressed in dBm. |
| hestfPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HE-STF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the HE-STF peak power results computed for each averaging count. This value is expressed in dBm. |
| heltfPeakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the HE-LTF field. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns the maximum of the HE-LTF peak power results computed for each averaging count. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf0045551bff60f7b8e8fd7e39977fea5.html language=enus -->
## TOPIC 00181: RFmxWLAN_OFDMModAccFetchUnusedToneErrorMarginPerRU

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf0045551bff60f7b8e8fd7e39977fea5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf0045551bff60f7b8e8fd7e39977fea5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the unused tone error margin result per RU. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneErrorMarginPerRU(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 unusedToneErrorMarginPerRu[], int32 arraySize, int32 *actualArraySize)RemarksUse "segment<n

### RFmxWLAN_OFDMModAccFetchUnusedToneErrorMarginPerRU

Fetches the unused tone error margin result per RU.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneErrorMarginPerRU(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 unusedToneErrorMarginPerRu[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| unusedToneErrorMarginPerRu | [out] | float64[] | This parameter returns an array of unused tone error margin per RU, which is the difference between the unused tone error mask and the unused tone error for each RU. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf0ff4cea9a43ae66f4c3b21892bb15de.html language=enus -->
## TOPIC 00182: RFmxWLAN_OFDMModAccFetchCrossPower

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf0ff4cea9a43ae66f4c3b21892bb15de.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf0ff4cea9a43ae66f4c3b21892bb15de.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the cross power. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchCrossPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *crossPowerMean)RemarksUse "segment<n>/chain<k>" as the selector string to read results from this function.ParametersNameDirectionType

### RFmxWLAN_OFDMModAccFetchCrossPower

Fetches the cross power.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchCrossPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *crossPowerMean)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| crossPowerMean | [out] | float64 * | This parameter returns the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this parameter returns the mean of the cross power results computed for each averaging count. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf7ebccdd59bfd6cb5356e6a21928cd5f.html language=enus -->
## TOPIC 00183: RFmxWLAN_OFDMModAccFetchStreamDataRMSEVMPerSymbolMeanTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf7ebccdd59bfd6cb5356e6a21928cd5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf7ebccdd59bfd6cb5356e6a21928cd5f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream data subcarriers RMS EVM per symbol trace. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchStreamDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 streamDataRMSEVMPerSymbolMean[], int32 arraySiz

### RFmxWLAN_OFDMModAccFetchStreamDataRMSEVMPerSymbolMeanTrace

Fetches the stream data subcarriers RMS EVM per symbol trace.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamDataRMSEVMPerSymbolMeanTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 streamDataRMSEVMPerSymbolMean[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the starting OFDM symbol index corresponding to the value of RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET attribute. |
| dx | [out] | float64 * | This parameter returns the OFDM symbol increment value. This value is always equal to 1. |
| streamDataRMSEVMPerSymbolMean | [out] | float32[] | This parameter returns the stream data subcarriers RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf818644774ba4961892ebab083d554ca.html language=enus -->
## TOPIC 00184: RFmxWLAN_OFDMModAccFetchCustomGatePowersArray

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf818644774ba4961892ebab083d554ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gaf818644774ba4961892ebab083d554ca.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average and peak power of the custom gates. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchCustomGatePowersArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 averagePowerMean[], float64 peakPowerMaximum[], int32 arraySize, int32 *actualArraySize)Rema

### RFmxWLAN_OFDMModAccFetchCustomGatePowersArray

Fetches the average and peak power of the custom gates.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchCustomGatePowersArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 averagePowerMean[], float64 peakPowerMaximum[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| averagePowerMean | [out] | float64[] | This parameter returns an array of average powers of the custom gates. This value is expressed in dBm. When you set the RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED attribute to True, this parameter returns an array of the mean of the average custom gate power results computed for each averaging count. |
| peakPowerMaximum | [out] | float64[] | This parameter returns an array of peak powers of the custom gates. This value is expressed in dBm. When you set the OFDMModAcc Averaging Enabled attribute to True, this parameter returns an array of the maximum of the peak custom gate power results computed for each averaging count. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gafe3696f2f4947cc31f02577ac1be686a.html language=enus -->
## TOPIC 00185: RFmxWLAN_OFDMModAccFetchPilotConstellationTraceSplit

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gafe3696f2f4947cc31f02577ac1be686a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__ofdmmodacc_1gafe3696f2f4947cc31f02577ac1be686a.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the pilot-subcarriers. Syntaxint32 __stdcall RFmxWLAN_OFDMModAccFetchPilotConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pilotConstellationI[], float32 pilotConstellationQ[], int32 arraySize, int32 *actu

### RFmxWLAN_OFDMModAccFetchPilotConstellationTraceSplit

Fetches the constellation trace for the pilot-subcarriers.

#### Syntax

int32 __stdcall RFmxWLAN_OFDMModAccFetchPilotConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 pilotConstellationI[], float32 pilotConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/stream<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0".Example:"segment0/stream0""signal::sig1/segment0/stream0""signal::sig1/result::r1/segment0/stream0""result::r1/segment0/stream0"You can use the RFmxWLAN_BuildStreamString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| pilotConstellationI | [out] | float32[] | This parameter Returns the real part of demodulated QAM symbols from all the pilot-subcarriers in all OFDM symbols. |
| pilotConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of demodulated QAM symbols from all the pilot-subcarriers in all OFDM symbols. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp.html language=enus -->
## TOPIC 00186: PowerRamp

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWLAN_PowerRampFetchFallTraceReturns the raw, processed, thresholding and power reference waveforms at the end of a burst. RFmxWLAN_PowerRampFetchMeasurementReturns the PowerRamp rise time and fall time. RFmxWLAN_PowerRampFetchRiseTraceReturns the raw, proces

### PowerRamp

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWLAN_PowerRampFetchFallTrace | Returns the raw, processed, thresholding and power reference waveforms at the end of a burst. |
| RFmxWLAN_PowerRampFetchMeasurement | Returns the PowerRamp rise time and fall time. |
| RFmxWLAN_PowerRampFetchRiseTrace | Returns the raw, processed, threshold and power-reference traces at the beginning of a burst. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1ga49fe657d85f8c0538a30f285b7c98f83.html language=enus -->
## TOPIC 00187: RFmxWLAN_PowerRampFetchRiseTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1ga49fe657d85f8c0538a30f285b7c98f83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1ga49fe657d85f8c0538a30f285b7c98f83.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the raw, processed, threshold and power-reference traces at the beginning of a burst. Syntaxint32 __stdcall RFmxWLAN_PowerRampFetchRiseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rawWaveform[], float32 processedWaveform[

### RFmxWLAN_PowerRampFetchRiseTrace

Returns the raw, processed, threshold and power-reference traces at the beginning of a burst.

#### Syntax

int32 __stdcall RFmxWLAN_PowerRampFetchRiseTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rawWaveform[], float32 processedWaveform[], float32 threshold[], float32 powerReference[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the trace start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling interval. This value is expressed in seconds. |
| rawWaveform | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| processedWaveform | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| threshold | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| powerReference | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1ga845d6e54e7332ea1b8f2a841fe76feae.html language=enus -->
## TOPIC 00188: RFmxWLAN_PowerRampFetchFallTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1ga845d6e54e7332ea1b8f2a841fe76feae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1ga845d6e54e7332ea1b8f2a841fe76feae.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the raw, processed, thresholding and power reference waveforms at the end of a burst. Syntaxint32 __stdcall RFmxWLAN_PowerRampFetchFallTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rawWaveform[], float32 processedWaveform[

### RFmxWLAN_PowerRampFetchFallTrace

Returns the raw, processed, thresholding and power reference waveforms at the end of a burst.

#### Syntax

int32 __stdcall RFmxWLAN_PowerRampFetchFallTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 rawWaveform[], float32 processedWaveform[], float32 threshold[], float32 powerReference[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the trace start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling interval. This value is expressed in seconds. |
| rawWaveform | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| processedWaveform | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| threshold | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| powerReference | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1gaa7b87d1c26b63f755c764aa2895ac8b6.html language=enus -->
## TOPIC 00189: RFmxWLAN_PowerRampFetchMeasurement

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1gaa7b87d1c26b63f755c764aa2895ac8b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__powerramp_1gaa7b87d1c26b63f755c764aa2895ac8b6.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the PowerRamp rise time and fall time. Syntaxint32 __stdcall RFmxWLAN_PowerRampFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *riseTimeMean, float64 *fallTimeMean)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandle

### RFmxWLAN_PowerRampFetchMeasurement

Returns the PowerRamp rise time and fall time.

#### Syntax

int32 __stdcall RFmxWLAN_PowerRampFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *riseTimeMean, float64 *fallTimeMean)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| riseTimeMean | [out] | float64 * | This parameter returns the rise time of the acquired signal that is the amount of time taken for the power envelope to rise from a level of 10 percent to 90 percent. This value is expressed in seconds. When you set the RFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLED attribute to True, this parameter returns the mean of the rise time computed for each averaging count. This value is expressed in seconds. |
| fallTimeMean | [out] | float64 * | This parameter returns the fall time of the acquired signal that is the amount of time taken for the power envelope to fall from a level of 90 percent to 10 percent. This value is expressed in seconds. When you set the PowerRamp Averaging Enabled attribute to True, this parameter returns the mean of the fall time computed for each averaging count. This value is expressed in seconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem.html language=enus -->
## TOPIC 00190: SEM

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWLAN_SEMFetchCarrierMeasurementReturns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier. RFmxWLAN_SEMFetchLowerOffsetMarginReturns the measurement status, margin, margin-frequency, and abso

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWLAN_SEMFetchCarrierMeasurement | Returns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier. |
| RFmxWLAN_SEMFetchLowerOffsetMargin | Returns the measurement status, margin, margin-frequency, and absolute and relative power corresponding to the margin-frequency for lower offset segment. The relative power is relative to the peak power in the carrier. |
| RFmxWLAN_SEMFetchLowerOffsetMarginArray | Returns an array of measurement status, margins, margin-frequencies, and absolute and relative powers corresponding to the margin-frequencies for lower offset segments. The relative powers are relative to the peak power in the carrier. |
| RFmxWLAN_SEMFetchLowerOffsetPower | Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of lower offset segment. The relative power is relative to the peak power of the carrier. |
| RFmxWLAN_SEMFetchLowerOffsetPowerArray | Returns an array of total absolute and relative powers, peak absolute and relative powers and frequencies corresponding to the peak absolute powers of lower offset segments. The relative powers are relative to peak power of the carrier. |
| RFmxWLAN_SEMFetchMeasurementStatus | Fetches the overall measurement status. |
| RFmxWLAN_SEMFetchSpectrum | Fetches the spectrum and mask traces. |
| RFmxWLAN_SEMFetchUpperOffsetMargin | Returns the measurement status, margin, margin-frequency, absolute and relative power corresponding to the margin-frequency for upper offset segment. The relative power is relative to the peak power in the carrier. |
| RFmxWLAN_SEMFetchUpperOffsetMarginArray | Returns an array of measurement status, margins, margin frequencies, absolute and relative powers corresponding to the margin-frequencies for upper offset segments. The relative powers are relative to the peak power in the carrier. |
| RFmxWLAN_SEMFetchUpperOffsetPower | Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of upper offset segment. The relative power is relative to the peak power of the carrier. |
| RFmxWLAN_SEMFetchUpperOffsetPowerArray | Fetches an array of total absolute and relative powers, peak absolute and relative powers, and frequencies corresponding to the peak absolute powers of upper offset segments. The relative powers are relative to peak power of the carrier. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga3e73c8b98780c0a047881bb70595ceca.html language=enus -->
## TOPIC 00191: RFmxWLAN_SEMFetchMeasurementStatus

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga3e73c8b98780c0a047881bb70595ceca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga3e73c8b98780c0a047881bb70595ceca.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall measurement status. Syntaxint32 __stdcall RFmxWLAN_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies th

### RFmxWLAN_SEMFetchMeasurementStatus

Fetches the overall measurement status.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the overall measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments.NameValueDescriptionRFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_FAIL0 (0x0)The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments.RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_PASS1 (0x1)The spectrum does not exceed the SEM measurement mask limits for any offset segment. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. |  |
| RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_PASS | 1 (0x1) | The spectrum does not exceed the SEM measurement mask limits for any offset segment. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga4687969ba18e090f4613b0f69edd5aa6.html language=enus -->
## TOPIC 00192: RFmxWLAN_SEMFetchUpperOffsetPower

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga4687969ba18e090f4613b0f69edd5aa6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga4687969ba18e090f4613b0f69edd5aa6.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of upper offset segment. The relative power is relative to the peak power of the carrier. Syntaxint32 __stdcall RFmxWLAN_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle,

### RFmxWLAN_SEMFetchUpperOffsetPower

Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of upper offset segment. The relative power is relative to the peak power of the carrier.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAbsolutePower, float64 *totalRelativePower, float64 *peakAbsolutePower, float64 *peakFrequency, float64 *peakRelativePower)

#### Remarks

Use "segment<n>/chain<k>/offset<<i>l</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0".Example:"segment0/chain0/offset0""signal::sig1/segment0/chain0/offset0""signal::sig1/result::r1/segment0/chain0/offset0""result::r1/segment0/chain0/offset0"You can use the RFmxWLAN_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| totalAbsolutePower | [out] | float64 * | This parameter returns the average power of the upper (positive) offset over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
| totalRelativePower | [out] | float64 * | This parameter returns the average power of the upper offset relative to the peak power of the carrier channel. This value is expressed in dB. |
| peakAbsolutePower | [out] | float64 * | This parameter returns the peak power of the upper offset. This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurs in the upper offset. This value is expressed in Hz. |
| peakRelativePower | [out] | float64 * | This parameter returns the peak power of the upper offset, relative to the peak power of the carrier channel. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga475cb8259cbc97e819ffd986d0144aaf.html language=enus -->
## TOPIC 00193: RFmxWLAN_SEMFetchSpectrum

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga475cb8259cbc97e819ffd986d0144aaf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga475cb8259cbc97e819ffd986d0144aaf.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum and mask traces. Syntaxint32 __stdcall RFmxWLAN_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32 *actualArraySize)RemarksUse "segment<n>/chai

### RFmxWLAN_SEMFetchSpectrum

Fetches the spectrum and mask traces.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 compositeMask[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns an array of power measured at each frequency bin. This value is expressed in dBm. |
| compositeMask | [out] | float32[] | This parameter returns an array of power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga49a377cb9369f1b6fe0f3cf52ba14c42.html language=enus -->
## TOPIC 00194: RFmxWLAN_SEMFetchCarrierMeasurement

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga49a377cb9369f1b6fe0f3cf52ba14c42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga49a377cb9369f1b6fe0f3cf52ba14c42.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier. Syntaxint32 __stdcall RFmxWLAN_SEMFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *relati

### RFmxWLAN_SEMFetchCarrierMeasurement

Returns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *relativePower)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| absolutePower | [out] | float64 * | This parameter returns the average power of the carrier channel over the bandwidth indicated by the RFMXWLAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH attribute. This value is expressed in dBm. |
| relativePower | [out] | float64 * | This parameter returns the average power of the carrier channel, relative to the peak power of the carrier channel, over the bandwidth indicated by the SEM Carrier IBW attribute. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga5439a6e944b9ce1de8af4de2dd432e4f.html language=enus -->
## TOPIC 00195: RFmxWLAN_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga5439a6e944b9ce1de8af4de2dd432e4f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga5439a6e944b9ce1de8af4de2dd432e4f.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement status, margins, margin frequencies, absolute and relative powers corresponding to the margin-frequencies for upper offset segments. The relative powers are relative to the peak power in the carrier. Syntaxint32 __stdcall RFmxWLAN_SEMFetchUpperOffsetMarginArray(niRFmx

### RFmxWLAN_SEMFetchUpperOffsetMarginArray

Returns an array of measurement status, margins, margin frequencies, absolute and relative powers corresponding to the margin-frequencies for upper offset segments. The relative powers are relative to the peak power in the carrier.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns an array of upper offset (positive) segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the upper offset segments.NameValueDescriptionRFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)The spectrum exceeds the SEM measurement mask and limits for the upper offset segment.RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)The spectrum does not exceed the SEM measurement mask and limits for the upper offset segment. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The spectrum exceeds the SEM measurement mask and limits for the upper offset segment. |  |
| RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | The spectrum does not exceed the SEM measurement mask and limits for the upper offset segment. |  |
| margin | [out] | float64[] | This parameter returns an array of margins from the SEM measurement mask for the upper offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. |
| marginFrequency | [out] | float64[] | This parameter returns an array of frequencies corresponding to the margins for the upper offsets. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns an array of absolute powers corresponding to the margins for the upper (positive) offsets. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns an array of relative powers corresponding to the margins for the upper (positive) offsets. The relative powers are relative to the peak power of the carrier channel. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga86f9502f7b49846ef7bcba6db88cd3be.html language=enus -->
## TOPIC 00196: RFmxWLAN_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga86f9502f7b49846ef7bcba6db88cd3be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga86f9502f7b49846ef7bcba6db88cd3be.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of total absolute and relative powers, peak absolute and relative powers and frequencies corresponding to the peak absolute powers of lower offset segments. The relative powers are relative to peak power of the carrier. Syntaxint32 __stdcall RFmxWLAN_SEMFetchLowerOffsetPowerArray(ni

### RFmxWLAN_SEMFetchLowerOffsetPowerArray

Returns an array of total absolute and relative powers, peak absolute and relative powers and frequencies corresponding to the peak absolute powers of lower offset segments. The relative powers are relative to peak power of the carrier.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| totalAbsolutePower | [out] | float64[] | This parameter returns an array of average powers of the lower offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
| totalRelativePower | [out] | float64[] | This parameter returns an array of average powers of the lower offsets relative to the peak power of the carrier channel. This value is expressed in dB. |
| peakAbsolutePower | [out] | float64[] | This parameter returns an array of peak powers of the lower offsets. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns an array of frequencies at which the peak power occurs in the lower offsets. This value is expressed in Hz. |
| peakRelativePower | [out] | float64[] | This parameter returns an array of peak powers of the lower offsets, relative to the peak power of the carrier channel. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga97391f0626d12d3734f38f6ac5fce140.html language=enus -->
## TOPIC 00197: RFmxWLAN_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga97391f0626d12d3734f38f6ac5fce140.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1ga97391f0626d12d3734f38f6ac5fce140.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement status, margins, margin-frequencies, and absolute and relative powers corresponding to the margin-frequencies for lower offset segments. The relative powers are relative to the peak power in the carrier. Syntaxint32 __stdcall RFmxWLAN_SEMFetchLowerOffsetMarginArray(ni

### RFmxWLAN_SEMFetchLowerOffsetMarginArray

Returns an array of measurement status, margins, margin-frequencies, and absolute and relative powers corresponding to the margin-frequencies for lower offset segments. The relative powers are relative to the peak power in the carrier.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns an array of lower (negative) offset segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segments.NameValueDescriptionRFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL0 (0x0)Indicates that the measurement has failed.RFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS1 (0x1)Indicates that the measurement has passed. |
| Name | Value | Description |  |
| RFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL | 0 (0x0) | Indicates that the measurement has failed. |  |
| RFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS | 1 (0x1) | Indicates that the measurement has passed. |  |
| margin | [out] | float64[] | This parameter returns an array of margins from the SEM measurement mask for the lower offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. |
| marginFrequency | [out] | float64[] | This parameter returns an array of frequencies corresponding to the margins for the lower (negative) offsets. This value is expressed in dB. |
| marginAbsolutePower | [out] | float64[] | This parameter returns an array of absolute powers corresponding to the margins for the lower offsets. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns an array of relative powers corresponding to the margins for the lower offsets. The relative powers are relative to the peak power of the carrier channel. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1gaa1134ef5048e399e2503c5e07075699c.html language=enus -->
## TOPIC 00198: RFmxWLAN_SEMFetchLowerOffsetPower

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1gaa1134ef5048e399e2503c5e07075699c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1gaa1134ef5048e399e2503c5e07075699c.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of lower offset segment. The relative power is relative to the peak power of the carrier. Syntaxint32 __stdcall RFmxWLAN_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle,

### RFmxWLAN_SEMFetchLowerOffsetPower

Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of lower offset segment. The relative power is relative to the peak power of the carrier.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalAbsolutePower, float64 *totalRelativePower, float64 *peakAbsolutePower, float64 *peakFrequency, float64 *peakRelativePower)

#### Remarks

Use "segment<n>/chain<k>/offset<<i>l</i>>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0".Example:"segment0/chain0/offset0""signal::sig1/segment0/chain0/offset0""signal::sig1/result::r1/segment0/chain0/offset0""result::r1/segment0/chain0/offset0"You can use the RFmxWLAN_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| totalAbsolutePower | [out] | float64 * | This parameter returns the average power of the lower offset over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
| totalRelativePower | [out] | float64 * | This parameter returns the average power of the lower offset relative to the peak power of the carrier channel. This value is expressed in dB. |
| peakAbsolutePower | [out] | float64 * | This parameter returns the peak power of the lower offset. This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurs in the lower offset. This value is expressed in Hz. |
| peakRelativePower | [out] | float64 * | This parameter returns the peak power of the lower offset, relative to the peak power of the carrier channel. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1gae29fe75084e35b4187dccd94d8ec1f42.html language=enus -->
## TOPIC 00199: RFmxWLAN_SEMFetchUpperOffsetPowerArray

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1gae29fe75084e35b4187dccd94d8ec1f42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__sem_1gae29fe75084e35b4187dccd94d8ec1f42.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of total absolute and relative powers, peak absolute and relative powers, and frequencies corresponding to the peak absolute powers of upper offset segments. The relative powers are relative to peak power of the carrier. Syntaxint32 __stdcall RFmxWLAN_SEMFetchUpperOffsetPowerArray(n

### RFmxWLAN_SEMFetchUpperOffsetPowerArray

Fetches an array of total absolute and relative powers, peak absolute and relative powers, and frequencies corresponding to the peak absolute powers of upper offset segments. The relative powers are relative to peak power of the carrier.

#### Syntax

int32 __stdcall RFmxWLAN_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 totalAbsolutePower[], float64 totalRelativePower[], float64 peakAbsolutePower[], float64 peakFrequency[], float64 peakRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| totalAbsolutePower | [out] | float64[] | This parameter returns an array of average powers of the upper offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
| totalRelativePower | [out] | float64[] | This parameter returns an array of average powers of the upper offsets relative to the peak power of the carrier channel. This value is expressed in dB. |
| peakAbsolutePower | [out] | float64[] | This parameter returns an array of peak powers of the upper offsets. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns an array of frequencies at which the peak power occurs in the upper offsets. This value is expressed in Hz. |
| peakRelativePower | [out] | float64[] | This parameter returns an array of peak powers of the upper offsets, relative to the peak power of the carrier channel. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp.html language=enus -->
## TOPIC 00200: TXP

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWLAN_TXPFetchMeasurementReturns the average power and the peak power of the signal over which power measurements are performed. RFmxWLAN_TXPFetchPowerTraceReturns the power versus time trace. AttachmentsNone

### TXP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWLAN_TXPFetchMeasurement | Returns the average power and the peak power of the signal over which power measurements are performed. |
| RFmxWLAN_TXPFetchPowerTrace | Returns the power versus time trace. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp_1ga1f65799f028628ff4c431698f893ef85.html language=enus -->
## TOPIC 00201: RFmxWLAN_TXPFetchMeasurement

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp_1ga1f65799f028628ff4c431698f893ef85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp_1ga1f65799f028628ff4c431698f893ef85.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power and the peak power of the signal over which power measurements are performed. Syntaxint32 __stdcall RFmxWLAN_TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averagePowerMean, float64 *peakPowerMaximum)RemarksUse "segm

### RFmxWLAN_TXPFetchMeasurement

Returns the average power and the peak power of the signal over which power measurements are performed.

#### Syntax

int32 __stdcall RFmxWLAN_TXPFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averagePowerMean, float64 *peakPowerMaximum)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| averagePowerMean | [out] | float64 * | This parameter returns the average power of the acquired signal. This value is expressed in dBm. When you set the RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED attribute to True, this parameter returns the mean of the average power computed for each averaging count. |
| peakPowerMaximum | [out] | float64 * | This parameter returns the peak power of the acquired signal. This value is expressed in dBm. When you set the TXP Averaging Enabled attribute to True, this parameter returns the maximum of the peak power computed for each averaging count. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp_1gafcd6655d9c63c7eab0879876d0017cb9.html language=enus -->
## TOPIC 00202: RFmxWLAN_TXPFetchPowerTrace

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp_1gafcd6655d9c63c7eab0879876d0017cb9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__fetch__txp_1gafcd6655d9c63c7eab0879876d0017cb9.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power versus time trace. Syntaxint32 __stdcall RFmxWLAN_TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)RemarksUse "segment<n>/chain<k>" as the selector strin

### RFmxWLAN_TXPFetchPowerTrace

Returns the power versus time trace.

#### Syntax

int32 __stdcall RFmxWLAN_TXPFetchPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 power[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "segment<n>/chain<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0".Example:"segment0/chain0""signal::sig1/segment0/chain0""signal::sig1/result::r1/segment0/chain0""result::r1/segment0/chain0"You can use the RFmxWLAN_BuildChainString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the trace start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sampling interval. This value is expressed in seconds. |
| power | [out] | float32[] | This parameter returns an array of measured signal power. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__select__measurement.html language=enus -->
## TOPIC 00203: Select Measurement

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__select__measurement.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWLAN_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWLAN_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__select__measurement_1ga68c4691a7c33e96771e1c10ea5de57dc.html language=enus -->
## TOPIC 00204: RFmxWLAN_SelectMeasurements

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__select__measurement_1ga68c4691a7c33e96771e1c10ea5de57dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__select__measurement_1ga68c4691a7c33e96771e1c10ea5de57dc.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxWLAN_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescript

### RFmxWLAN_SelectMeasurements

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxWLAN_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array.Name (Value)DescriptionTXP (0)Enables TXP measurement.PowerRamp (1)Enables PowerRamp measurement.DSSSModAcc (2)Enables DSSSModAcc measurement.OFDMModAcc (3)Enables OFDMModAcc measurement.SEM (4)Enables SEM measurement. |
| Name (Value) | Description |  |  |
| TXP (0) | Enables TXP measurement. |  |  |
| PowerRamp (1) | Enables PowerRamp measurement. |  |  |
| DSSSModAcc (2) | Enables DSSSModAcc measurement. |  |  |
| OFDMModAcc (3) | Enables OFDMModAcc measurement. |  |  |
| SEM (4) | Enables SEM measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurement. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00205: Set and Get Attributes

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes.html
- document_id: `rfmxwlan-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00206: Get Attributes

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWLAN_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxWLAN_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWLAN_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxWLAN_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxWLAN_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxWLAN_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxWLAN_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxWLAN_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxWLAN_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxWLAN_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxWLAN_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWLAN_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxWLAN_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga2ef63d42fc344a2f69ad16c75282d493.html language=enus -->
## TOPIC 00207: RFmxWLAN_GetAttributeI64

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga2ef63d42fc344a2f69ad16c75282d493.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga2ef63d42fc344a2f69ad16c75282d493.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxWLAN_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx se

### RFmxWLAN_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga3e05bf7d41e11769dd03c240b70040b1.html language=enus -->
## TOPIC 00208: RFmxWLAN_GetAttributeI32Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga3e05bf7d41e11769dd03c240b70040b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga3e05bf7d41e11769dd03c240b70040b1.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxWLAN_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga4001abd4307e7de5ac2de74476b3bab6.html language=enus -->
## TOPIC 00209: RFmxWLAN_GetAttributeF32Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga4001abd4307e7de5ac2de74476b3bab6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga4001abd4307e7de5ac2de74476b3bab6.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxWLAN_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga42a0162dd947701dd09e20c124655d06.html language=enus -->
## TOPIC 00210: RFmxWLAN_GetAttributeI8

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga42a0162dd947701dd09e20c124655d06.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga42a0162dd947701dd09e20c124655d06.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxWLAN_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessio

### RFmxWLAN_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga496fa753d7cb13ec2d0fda8c136faf83.html language=enus -->
## TOPIC 00211: RFmxWLAN_GetAttributeString

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga496fa753d7cb13ec2d0fda8c136faf83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga496fa753d7cb13ec2d0fda8c136faf83.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxWLAN_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga4d2edf8d81c1fc12ff8dde5afcb87dd2.html language=enus -->
## TOPIC 00212: RFmxWLAN_GetAttributeI32

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga4d2edf8d81c1fc12ff8dde5afcb87dd2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga4d2edf8d81c1fc12ff8dde5afcb87dd2.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxWLAN_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx se

### RFmxWLAN_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga55991f70ae2eea7f4efd10a3122f53d3.html language=enus -->
## TOPIC 00213: RFmxWLAN_GetAttributeI64Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga55991f70ae2eea7f4efd10a3122f53d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga55991f70ae2eea7f4efd10a3122f53d3.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxWLAN_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga8426e359b8b520fc710da86929b111c4.html language=enus -->
## TOPIC 00214: RFmxWLAN_GetAttributeU64Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga8426e359b8b520fc710da86929b111c4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga8426e359b8b520fc710da86929b111c4.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxWLAN_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga8ea93e372740c250782b02e272de3eaa.html language=enus -->
## TOPIC 00215: RFmxWLAN_GetAttributeU8Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga8ea93e372740c250782b02e272de3eaa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1ga8ea93e372740c250782b02e272de3eaa.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxWLAN_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaa0480833552f7fc5cf30e79017261358.html language=enus -->
## TOPIC 00216: RFmxWLAN_GetAttributeF64

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaa0480833552f7fc5cf30e79017261358.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaa0480833552f7fc5cf30e79017261358.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxWLAN_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIden

### RFmxWLAN_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaa3e54f8904f09fa6c3eb028ce3446d3d.html language=enus -->
## TOPIC 00217: RFmxWLAN_GetAttributeU32Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaa3e54f8904f09fa6c3eb028ce3446d3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaa3e54f8904f09fa6c3eb028ce3446d3d.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxWLAN_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaaa5469459ec296a49880dab4e146657e.html language=enus -->
## TOPIC 00218: RFmxWLAN_GetAttributeI8Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaaa5469459ec296a49880dab4e146657e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gaaa5469459ec296a49880dab4e146657e.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxWLAN_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gab58eb2630caf89bbd216bd6d0244a332.html language=enus -->
## TOPIC 00219: RFmxWLAN_GetAttributeU16

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gab58eb2630caf89bbd216bd6d0244a332.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__get__attributes_1gab58eb2630caf89bbd216bd6d0244a332.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxWLAN_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxWLAN_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga3633d4f6853d508ad81c74bb37858253.html language=enus -->
## TOPIC 00220: RFmxWLAN_SetAttributeI8

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga3633d4f6853d508ad81c74bb37858253.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga3633d4f6853d508ad81c74bb37858253.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxWLAN_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. Y

### RFmxWLAN_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga446d7a70af8bd6fe8f18dba8b6b2c662.html language=enus -->
## TOPIC 00221: RFmxWLAN_SetAttributeU8

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga446d7a70af8bd6fe8f18dba8b6b2c662.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga446d7a70af8bd6fe8f18dba8b6b2c662.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxWLAN_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxWLAN_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga46873216cfbc610b187f433a1b75fe09.html language=enus -->
## TOPIC 00222: RFmxWLAN_SetAttributeU32

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga46873216cfbc610b187f433a1b75fe09.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga46873216cfbc610b187f433a1b75fe09.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxWLAN_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxWLAN_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga9794f818285a05352e9c106a24b960ed.html language=enus -->
## TOPIC 00223: RFmxWLAN_SetAttributeF32Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga9794f818285a05352e9c106a24b960ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1ga9794f818285a05352e9c106a24b960ed.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWLAN_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, cha

### RFmxWLAN_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gaaaec86cc1138f1f841aec823cf017ca3.html language=enus -->
## TOPIC 00224: RFmxWLAN_SetAttributeString

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gaaaec86cc1138f1f841aec823cf017ca3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gaaaec86cc1138f1f841aec823cf017ca3.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxWLAN_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can o

### RFmxWLAN_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gab640bfabfc7fbb991c68517331bd57b5.html language=enus -->
## TOPIC 00225: RFmxWLAN_SetAttributeI32Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gab640bfabfc7fbb991c68517331bd57b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gab640bfabfc7fbb991c68517331bd57b5.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWLAN_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxWLAN_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gaba10983a6d0225d1e4d85584e37d6427.html language=enus -->
## TOPIC 00226: RFmxWLAN_SetAttributeU16

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gaba10983a6d0225d1e4d85584e37d6427.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gaba10983a6d0225d1e4d85584e37d6427.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxWLAN_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxWLAN_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gacf726da0f1958a7f56b1ec31c7639a22.html language=enus -->
## TOPIC 00227: RFmxWLAN_SetAttributeU64Array

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gacf726da0f1958a7f56b1ec31c7639a22.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gacf726da0f1958a7f56b1ec31c7639a22.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWLAN_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char sele

### RFmxWLAN_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gad716f99ba1752dbe181ba9adeb663603.html language=enus -->
## TOPIC 00228: RFmxWLAN_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gad716f99ba1752dbe181ba9adeb663603.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__set__and__get__attributes__set__attributes_1gad716f99ba1752dbe181ba9adeb663603.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWLAN_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorS

### RFmxWLAN_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWLAN_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga61c89fbcab60bd7be4fa5242f717fb44.html language=enus -->
## TOPIC 00229: RFmxWLAN_ResetToDefault

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga61c89fbcab60bd7be4fa5242f717fb44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga61c89fbcab60bd7be4fa5242f717fb44.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. Syntaxint32 __stdcall RFmxWLAN_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtained

### RFmxWLAN_ResetToDefault

Resets a signal to the default values.

#### Syntax

int32 __stdcall RFmxWLAN_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr_InitializeFromNIRFSASessionArray function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"""signal::sig1"You can use the RFmxWLAN_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga738e01f46d4ec4c182eb7460d7d4e836.html language=enus -->
## TOPIC 00230: RFmxWLAN_InitializeFromNIRFSASession

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga738e01f46d4ec4c182eb7460d7d4e836.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__utility_1ga738e01f46d4ec4c182eb7460d7d4e836.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device

### RFmxWLAN_InitializeFromNIRFSASession

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxWLAN_InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle *handleOut)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| nirfsaSession | [in] | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| handleOut | [out] | niRFmxInstrHandle * | Returns an RFmx instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlan-c-api-ref path=group____root__ni_r_fmx_w_l_a_n__functions__utility_1gabc6deb8199b69ae53c844bf8fdb1b3ce.html language=enus -->
## TOPIC 00231: RFmxWLAN_WaitForAcquisitionComplete

- bundle_id: `rfmxwlan-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_l_a_n__functions__utility_1gabc6deb8199b69ae53c844bf8fdb1b3ce.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_l_a_n__functions__utility_1gabc6deb8199b69ae53c844bf8fdb1b3ce.html
- document_id: `rfmxwlan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxWLAN_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instrume

### RFmxWLAN_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxWLAN_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWLAN_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWLAN_GetError](group____root__ni_r_fmx_w_l_a_n__functions_1ga7087aaf60dfda55abe8d54bb86a19247.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility
