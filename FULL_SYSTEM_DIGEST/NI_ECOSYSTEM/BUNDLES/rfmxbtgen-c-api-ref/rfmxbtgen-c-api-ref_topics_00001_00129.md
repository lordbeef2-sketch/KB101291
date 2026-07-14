# NI DOCUMENT BUNDLE: rfmxbtgen-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxbtgen-c-api-ref start=1 end=129 -->
<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes.html language=enus -->
## TOPIC 00001: Attributes

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedHardware SettingsImpairmentsPacket SettingsPower Ramp SettingsRun Time ScalingWaveform File VersionGroup membersNameDescriptionNIBTSG_ATTR_ACTIVE_CHANNELSpecifies the active channel string is used to access all subsequent properties in a property node until a new active channel is spec

### Attributes

#### Groups

- Advanced
- Hardware Settings
- Impairments
- Packet Settings
- Power Ramp Settings
- Run Time Scaling
- Waveform File Version

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_ACTIVE_CHANNEL | Specifies the active channel string is used to access all subsequent properties in a property node until a new active channel is specified. |
| NIBTSG_ATTR_CARRIER_FREQUENCY | Specifies the carrier frequency. This value is expressed in Hz. |
| NIBTSG_ATTR_CARRIER_MODE | Specifies whether the carrier is continuous or includes bursts. |
| NIBTSG_ATTR_OVERSAMPLING_FACTOR | Specifies the number of times the Nyquist sample rate is increased to obtain the final sample rate of a signal. |

#### Attachments

None

Parent topic:

niBTGeneration.h

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes_1ga012e7586b9799589ff15f719047e3341.html language=enus -->
## TOPIC 00002: NIBTSG_ATTR_CARRIER_MODE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes_1ga012e7586b9799589ff15f719047e3341.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes_1ga012e7586b9799589ff15f719047e3341.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the carrier is continuous or includes bursts. SyntaxNIBTSG_ATTR_CARRIER_MODENumeric ValueData TypeAccessApplies To1int32Read/WriteN/ARemarks If you set this attribute to NIBTSG_VAL_CARRIER_MODE_BURST, the BT Generation generates the burst signal by adding zeros at the end of the pa

### NIBTSG_ATTR_CARRIER_MODE

Specifies whether the carrier is continuous or includes bursts.

#### Syntax

NIBTSG_ATTR_CARRIER_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1 | int32 | Read/Write | N/A |

#### Remarks

If you set this attribute to NIBTSG_VAL_CARRIER_MODE_BURST, the BT Generation generates the burst signal by adding zeros at the end of the packet to create one or more complete slots, depending on the packet type. In this mode, the BT Generation also shapes the generated waveform to meet the burst ramp characteristics specified in the Bluetooth Test Purposes (TP) specification 1.2/2.0+EDR/2.1/2.1+EDR/3.0/3.0+HS. If you set this attribute to NIBTSG_VAL_CARRIER_MODE_CONTINUOUS, the BT Generation generates a phase continuous Bluetooth signal, which is used as an interference signal. This mode is useful to generate an interference signal with pseudorandom bits and continuous phase. In this mode, the [NIBTSG_ATTR_NUMBER_OF_IDLE_SLOTS](group____root__ni_b_t_generation__attributes__packet__settings_1gac4009755ee37a3015d84b80106b591e3.html) attribute is not used, and the number of idle slots is assumed be zero. In this mode, NI recommends you to leave the [NIBTSG_ATTR_NUMBER_OF_UNIQUE_PACKETS](group____root__ni_b_t_generation__attributes__packet__settings_1ga6466966ade8a9fc9ee9dda46821d5931.html), [NIBTSG_ATTR_PAYLOAD_DATA_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga9d852f50a7b7c63fb129b8776e8c8655.html), and [NIBTSG_ATTR_DIRTY_TX_ENABLED](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga76d807fea6b4980a0976e6d0a871700b.html) attributes at their default values. Refer to the Carrier Mode topic for more information about the [NIBTSG_ATTR_CARRIER_MODE](group____root__ni_b_t_generation__attributes_1ga012e7586b9799589ff15f719047e3341.html) attribute.

The default value is NIBTSG_VAL_CARRIER_MODE_BURST.

Get Function: niBTSG_GetCarrierMode 
 Set Function: niBTSG_SetCarrierMode

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_CARRIER_MODE_BURST | 0 (0x0) | Specifies that the carrier mode includes bursts. |
| NIBTSG_VAL_CARRIER_MODE_CONTINUOUS | 1 (0x1) | Specifies that the carrier mode is continuous. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes_1gaa63c19255c2449e466bd0085b421c1e3.html language=enus -->
## TOPIC 00003: NIBTSG_ATTR_OVERSAMPLING_FACTOR

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes_1gaa63c19255c2449e466bd0085b421c1e3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes_1gaa63c19255c2449e466bd0085b421c1e3.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of times the Nyquist sample rate is increased to obtain the final sample rate of a signal. SyntaxNIBTSG_ATTR_OVERSAMPLING_FACTORNumeric ValueData TypeAccessApplies To70int32Read/WriteN/ARemarks The default value is 8.Get Function: niBTSG_GetOversamplingFactor Set Function: niBTS

### NIBTSG_ATTR_OVERSAMPLING_FACTOR

Specifies the number of times the Nyquist sample rate is increased to obtain the final sample rate of a signal.

#### Syntax

NIBTSG_ATTR_OVERSAMPLING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 70 | int32 | Read/Write | N/A |

#### Remarks

The default value is 8.

Get Function: niBTSG_GetOversamplingFactor 
 Set Function: niBTSG_SetOversamplingFactor

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__advanced_1gac425ddfc18641195b73380947577a1d6.html language=enus -->
## TOPIC 00004: NIBTSG_ATTR_IQ_WAVEFORM_SIZE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__advanced_1gac425ddfc18641195b73380947577a1d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__advanced_1gac425ddfc18641195b73380947577a1d6.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size, in complex samples, for a packet as specified by the NIBTSG_ATTR_PACKET_TYPE attribute and the number of idle slots specified by the NIBTSG_ATTR_NUMBER_OF_IDLE_SLOTS attribute. SyntaxNIBTSG_ATTR_IQ_WAVEFORM_SIZENumeric ValueData TypeAccessApplies To45int32Read/WriteN/ARemarks Get F

### NIBTSG_ATTR_IQ_WAVEFORM_SIZE

Returns the size, in complex samples, for a packet as specified by the [NIBTSG_ATTR_PACKET_TYPE](group____root__ni_b_t_generation__attributes__packet__settings_1gae23e33e3a7ed97a782c08c01619cb9b5.html) attribute and the number of idle slots specified by the [NIBTSG_ATTR_NUMBER_OF_IDLE_SLOTS](group____root__ni_b_t_generation__attributes__packet__settings_1gac4009755ee37a3015d84b80106b591e3.html) attribute.

#### Syntax

NIBTSG_ATTR_IQ_WAVEFORM_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 45 | int32 | Read/Write | N/A |

#### Remarks

Get Function: niBTSG_GetIQWaveformSize

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__hardware__settings.html language=enus -->
## TOPIC 00005: Hardware Settings

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__hardware__settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__hardware__settings.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsRecommended SettingsGroup membersNameDescriptionNIBTSG_ATTR_AUTO_HEADROOM_ENABLEDSpecifies whether the BT Generation calculates the headroom or uses the value that you specify in the NIBTSG_ATTR_HEADROOM attribute. NIBTSG_ATTR_HEADROOMSpecifies the value for the headroom. This value is express

### Hardware Settings

#### Groups

- Recommended Settings

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_AUTO_HEADROOM_ENABLED | Specifies whether the BT Generation calculates the headroom or uses the value that you specify in the NIBTSG_ATTR_HEADROOM attribute. |
| NIBTSG_ATTR_HEADROOM | Specifies the value for the headroom. This value is expressed in dB. The BT Generation uses this attribute for scaling the waveform when you set the NIBTSG_ATTR_AUTO_HEADROOM_ENABLED attribute to NIBTSG_VAL_FALSE. |
| NIBTSG_ATTR_MAXIMUM_HARDWARE_IQ_RATE | Specifies the maximum I/Q rate that the NI RF vector signal generator supports. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__hardware__settings_1ga38f9316d59bceb0934561711123c17a9.html language=enus -->
## TOPIC 00006: NIBTSG_ATTR_MAXIMUM_HARDWARE_IQ_RATE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__hardware__settings_1ga38f9316d59bceb0934561711123c17a9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__hardware__settings_1ga38f9316d59bceb0934561711123c17a9.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum I/Q rate that the NI RF vector signal generator supports. SyntaxNIBTSG_ATTR_MAXIMUM_HARDWARE_IQ_RATENumeric ValueData TypeAccessApplies To69float64Read/WriteN/ARemarks This property will be set according to the device model in the niBTSG_RFSGCreateAndDownloadWaveform function.G

### NIBTSG_ATTR_MAXIMUM_HARDWARE_IQ_RATE

Specifies the maximum I/Q rate that the NI RF vector signal generator supports.

#### Syntax

NIBTSG_ATTR_MAXIMUM_HARDWARE_IQ_RATE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 69 | float64 | Read/Write | N/A |

#### Remarks

This property will be set according to the device model in the [niBTSG_RFSGCreateAndDownloadWaveform](group____root__ni_b_t_generation__functions__rfsg__waveform__database_1ga37597cb904f8cac38985e732856d395e.html) function.

Get Function: niBTSG_GetMaximumHardwareIqRate 
 Set Function: niBTSG_SetMaximumHardwareIqRate

Parent topic:

Hardware Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__hardware__settings_1ga4876b23b4d3f2ca957bacf4f1e373926.html language=enus -->
## TOPIC 00007: NIBTSG_ATTR_AUTO_HEADROOM_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__hardware__settings_1ga4876b23b4d3f2ca957bacf4f1e373926.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__hardware__settings_1ga4876b23b4d3f2ca957bacf4f1e373926.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the BT Generation calculates the headroom or uses the value that you specify in the NIBTSG_ATTR_HEADROOM attribute. SyntaxNIBTSG_ATTR_AUTO_HEADROOM_ENABLEDNumeric ValueData TypeAccessApplies To3int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_TRUE.Get Function: niBTSG_GetA

### NIBTSG_ATTR_AUTO_HEADROOM_ENABLED

Specifies whether the BT Generation calculates the headroom or uses the value that you specify in the [NIBTSG_ATTR_HEADROOM](group____root__ni_b_t_generation__attributes__hardware__settings_1gad2634f53369b3b1bb3f24b9efa6adebd.html) attribute.

#### Syntax

NIBTSG_ATTR_AUTO_HEADROOM_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 3 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_TRUE.

Get Function: niBTSG_GetAutoHeadroomEnabled 
 Set Function: niBTSG_SetAutoHeadroomEnabled

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Specifies that the BT Generation uses the headroom that you specify in the NIBTSG_HEADROOM attribute. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Specifies that the BT Generation computes the headroom value based on the peak power of the signal. The BT Generation assumes that the generated signal average power is 0 dB. The BT Generation adds a power margin of 1.5 dB to the peak power to give some room for the filters in the NI RF vector signal generator. You can read the value of the computed headroom using the NIBTSG_ACTUAL_HEADROOM attribute. |

Parent topic:

Hardware Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__hardware__settings_1gad2634f53369b3b1bb3f24b9efa6adebd.html language=enus -->
## TOPIC 00008: NIBTSG_ATTR_HEADROOM

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__hardware__settings_1gad2634f53369b3b1bb3f24b9efa6adebd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__hardware__settings_1gad2634f53369b3b1bb3f24b9efa6adebd.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value for the headroom. This value is expressed in dB. The BT Generation uses this attribute for scaling the waveform when you set the NIBTSG_ATTR_AUTO_HEADROOM_ENABLED attribute to NIBTSG_VAL_FALSE. SyntaxNIBTSG_ATTR_HEADROOMNumeric ValueData TypeAccessApplies To4float64Read/WriteN/AR

### NIBTSG_ATTR_HEADROOM

Specifies the value for the headroom. This value is expressed in dB. The BT Generation uses this attribute for scaling the waveform when you set the [NIBTSG_ATTR_AUTO_HEADROOM_ENABLED](group____root__ni_b_t_generation__attributes__hardware__settings_1ga4876b23b4d3f2ca957bacf4f1e373926.html) attribute to NIBTSG_VAL_FALSE.

#### Syntax

NIBTSG_ATTR_HEADROOM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 4 | float64 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetHeadroom 
 Set Function: niBTSG_SetHeadroom

Parent topic:

Hardware Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings.html language=enus -->
## TOPIC 00009: Recommended Settings

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_ACTUAL_HEADROOMReturns the actual headroom used by the BT Generation. This value is expressed in dB. You can use this value to configure the peak power of the generation hardware. NIBTSG_ATTR_BURST_START_LOCATIONSReturns an array of sample positions

### Recommended Settings

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_ACTUAL_HEADROOM | Returns the actual headroom used by the BT Generation. This value is expressed in dB. You can use this value to configure the peak power of the generation hardware. |
| NIBTSG_ATTR_BURST_START_LOCATIONS | Returns an array of sample positions for the start of all bursts, within the waveform. |
| NIBTSG_ATTR_BURST_STOP_LOCATIONS | Returns an array of sample positions for the end of all bursts, within the waveform. |
| NIBTSG_ATTR_IQ_RATE | Returns the sample rate for generation. This value is expressed in samples per second (S/s). The symbol rate of the Bluetooth signal is 1 megasymbol per second. The sample rate of the generated signal is the product of the symbol rate and the oversampling factor. The BT Generation uses an oversampling factor of 8. |

#### Attachments

None

Parent topic:

Hardware Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings_1gaccee86a93c42c55b058dd9b807b106c9.html language=enus -->
## TOPIC 00010: NIBTSG_ATTR_BURST_STOP_LOCATIONS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings_1gaccee86a93c42c55b058dd9b807b106c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings_1gaccee86a93c42c55b058dd9b807b106c9.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of sample positions for the end of all bursts, within the waveform. SyntaxNIBTSG_ATTR_BURST_STOP_LOCATIONSNumeric ValueData TypeAccessApplies To91int32 []Read/WriteN/ARemarks Get Function: niBTSG_GetBurstStopLocations

### NIBTSG_ATTR_BURST_STOP_LOCATIONS

Returns an array of sample positions for the end of all bursts, within the waveform.

#### Syntax

NIBTSG_ATTR_BURST_STOP_LOCATIONS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 91 | int32 [] | Read/Write | N/A |

#### Remarks

Get Function: niBTSG_GetBurstStopLocations

Parent topic:

Recommended Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__impairments.html language=enus -->
## TOPIC 00011: Impairments

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__impairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__impairments.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAWGNIQ ImpairmentsGroup membersNameDescriptionNIBTSG_ATTR_CARRIER_FREQUENCY_OFFSETSpecifies the carrier frequency offset from the value that you specify as the center frequency of the RF signal generator. This value is expressed in Hz. NIBTSG_ATTR_SAMPLE_CLOCK_OFFSETSpecifies the offset in the

### Impairments

#### Groups

- AWGN
- IQ Impairments

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_CARRIER_FREQUENCY_OFFSET | Specifies the carrier frequency offset from the value that you specify as the center frequency of the RF signal generator. This value is expressed in Hz. |
| NIBTSG_ATTR_SAMPLE_CLOCK_OFFSET | Specifies the offset in the Sample Clock frequency from the sample frequency for CS packets. This value is expressed in parts per million (ppm). |
| NIBTSG_ATTR_TIME_DELAY | Specifies the time delay for CS packets This value is expressed in seconds. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__impairments_1ga25bb2aad5f220c438b92f10ad52be3a2.html language=enus -->
## TOPIC 00012: NIBTSG_ATTR_CARRIER_FREQUENCY_OFFSET

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__impairments_1ga25bb2aad5f220c438b92f10ad52be3a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__impairments_1ga25bb2aad5f220c438b92f10ad52be3a2.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier frequency offset from the value that you specify as the center frequency of the RF signal generator. This value is expressed in Hz. SyntaxNIBTSG_ATTR_CARRIER_FREQUENCY_OFFSETNumeric ValueData TypeAccessApplies To37float64Read/WriteN/ARemarks The default value is 0.Get Function:

### NIBTSG_ATTR_CARRIER_FREQUENCY_OFFSET

Specifies the carrier frequency offset from the value that you specify as the center frequency of the RF signal generator. This value is expressed in Hz.

#### Syntax

NIBTSG_ATTR_CARRIER_FREQUENCY_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 37 | float64 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetCarrierFrequencyOffset 
 Set Function: niBTSG_SetCarrierFrequencyOffset

Parent topic:

Impairments

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__impairments__awgn.html language=enus -->
## TOPIC 00013: AWGN

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__impairments__awgn.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__impairments__awgn.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_AWGN_ENABLEDSpecifies whether to add additive white Gaussian noise (AWGN) to the baseband waveform. NIBTSG_ATTR_CARRIER_TO_NOISE_RATIOSpecifies the carrier-to-noise ratio (CNR)of the waveform generated. This value is expressed in dB. Noise bandwidth

### AWGN

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_AWGN_ENABLED | Specifies whether to add additive white Gaussian noise (AWGN) to the baseband waveform. |
| NIBTSG_ATTR_CARRIER_TO_NOISE_RATIO | Specifies the carrier-to-noise ratio (CNR)of the waveform generated. This value is expressed in dB. Noise bandwidth is equal to half the value of the NIBTSG_ATTR_IQ_RATE attribute. Configure the NIBTSG_ATTR_CARRIER_TO_NOISE_RATIO attribute only if you set the NIBTSG_ATTR_AWGN_ENABLED attribute to NIBTSG_VAL_TRUE. |

#### Attachments

None

Parent topic:

Impairments

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__impairments__awgn_1gaaff721aeee6963703bff308e293e8af0.html language=enus -->
## TOPIC 00014: NIBTSG_ATTR_AWGN_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__impairments__awgn_1gaaff721aeee6963703bff308e293e8af0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__impairments__awgn_1gaaff721aeee6963703bff308e293e8af0.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to add additive white Gaussian noise (AWGN) to the baseband waveform. SyntaxNIBTSG_ATTR_AWGN_ENABLEDNumeric ValueData TypeAccessApplies To38int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_FALSE.Get Function: niBTSG_GetAWGNEnabled Set Function: niBTSG_SetAWGNEnabledNameVal

### NIBTSG_ATTR_AWGN_ENABLED

Specifies whether to add additive white Gaussian noise (AWGN) to the baseband waveform.

#### Syntax

NIBTSG_ATTR_AWGN_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 38 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_FALSE.

Get Function: niBTSG_GetAWGNEnabled 
 Set Function: niBTSG_SetAWGNEnabled

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Specifies that the BT Generation does not add AWGN to the baseband waveform. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Specifies that the BT Generation adds AWGN to the baseband waveform. |

Parent topic:

AWGN

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__impairments__awgn_1gad9171a448a31f7bf6a3460023a6420ac.html language=enus -->
## TOPIC 00015: NIBTSG_ATTR_CARRIER_TO_NOISE_RATIO

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__impairments__awgn_1gad9171a448a31f7bf6a3460023a6420ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__impairments__awgn_1gad9171a448a31f7bf6a3460023a6420ac.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier-to-noise ratio (CNR)of the waveform generated. This value is expressed in dB. Noise bandwidth is equal to half the value of the NIBTSG_ATTR_IQ_RATE attribute. Configure the NIBTSG_ATTR_CARRIER_TO_NOISE_RATIO attribute only if you set the NIBTSG_ATTR_AWGN_ENABLED attribute to NI

### NIBTSG_ATTR_CARRIER_TO_NOISE_RATIO

Specifies the carrier-to-noise ratio (CNR)of the waveform generated. This value is expressed in dB. Noise bandwidth is equal to half the value of the [NIBTSG_ATTR_IQ_RATE](group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings_1ga6b0723d1da00183f276e82dd38132b57.html) attribute. Configure the [NIBTSG_ATTR_CARRIER_TO_NOISE_RATIO](group____root__ni_b_t_generation__attributes__impairments__awgn_1gad9171a448a31f7bf6a3460023a6420ac.html) attribute only if you set the [NIBTSG_ATTR_AWGN_ENABLED](group____root__ni_b_t_generation__attributes__impairments__awgn_1gaaff721aeee6963703bff308e293e8af0.html) attribute to NIBTSG_VAL_TRUE.

#### Syntax

NIBTSG_ATTR_CARRIER_TO_NOISE_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 39 | float64 | Read/Write | N/A |

#### Remarks

The default value is 50.

Get Function: niBTSG_GetCarrierToNoiseRatio 
 Set Function: niBTSG_SetCarrierToNoiseRatio

Parent topic:

AWGN

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__impairments__iq__impairments_1ga221aa2c427ffb0fde02ac54dad4c927a.html language=enus -->
## TOPIC 00016: NIBTSG_ATTR_QUADRATURE_SKEW

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__impairments__iq__impairments_1ga221aa2c427ffb0fde02ac54dad4c927a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__impairments__iq__impairments_1ga221aa2c427ffb0fde02ac54dad4c927a.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the deviation in angle from 90 degrees between the in-phase (I) and quadrature-phase (Q) signals. SyntaxNIBTSG_ATTR_QUADRATURE_SKEWNumeric ValueData TypeAccessApplies To34float64Read/WriteN/ARemarks For more information on quadrature skew equations, refer to the IQ Gain Imbalance topic RFm

### NIBTSG_ATTR_QUADRATURE_SKEW

Specifies the deviation in angle from 90 degrees between the in-phase (I) and quadrature-phase (Q) signals.

#### Syntax

NIBTSG_ATTR_QUADRATURE_SKEW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 34 | float64 | Read/Write | N/A |

#### Remarks

For more information on quadrature skew equations, refer to the IQ Gain Imbalance topic RFmx BT Generation Help.

The default value is 0. Valid values are -30 to 30, inclusive.

Get Function: niBTSG_GetQuadratureSkew 
 Set Function: niBTSG_SetQuadratureSkew

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__impairments__iq__impairments_1ga25fffe41bcb33426a7ecdb0bc15cdd7b.html language=enus -->
## TOPIC 00017: NIBTSG_ATTR_I_DC_OFFSET

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__impairments__iq__impairments_1ga25fffe41bcb33426a7ecdb0bc15cdd7b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__impairments__iq__impairments_1ga25fffe41bcb33426a7ecdb0bc15cdd7b.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the DC offset in the in-phase (I) signal as a percentage of the peak magnitude of the complex I/Q signal. SyntaxNIBTSG_ATTR_I_DC_OFFSETNumeric ValueData TypeAccessApplies To35float64Read/WriteN/ARemarks The default value is 0. Valid values are -100 to 100, inclusive.Get Functi

### NIBTSG_ATTR_I_DC_OFFSET

Specifies the value of the DC offset in the in-phase (I) signal as a percentage of the peak magnitude of the complex I/Q signal.

#### Syntax

NIBTSG_ATTR_I_DC_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 35 | float64 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are -100 to 100, inclusive.

Get Function: niBTSG_GetIDCOffset 
 Set Function: niBTSG_SetIDCOffset

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings_1ga8deaefb1ac33e4f6360997b6f599e9ec.html language=enus -->
## TOPIC 00018: NIBTSG_ATTR_LE_ACCESS_ADDRESS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings_1ga8deaefb1ac33e4f6360997b6f599e9ec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings_1ga8deaefb1ac33e4f6360997b6f599e9ec.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 32-bit LE access address. SyntaxNIBTSG_ATTR_LE_ACCESS_ADDRESSNumeric ValueData TypeAccessApplies To61int32Read/WriteN/ARemarks The Bluetooth core specification recommends to use 0x71764129 as the LE access address for all test packets. The preamble of LE-TP/LE-TP-EXT packets is either

### NIBTSG_ATTR_LE_ACCESS_ADDRESS

Specifies the 32-bit LE access address.

#### Syntax

NIBTSG_ATTR_LE_ACCESS_ADDRESS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 61 | int32 | Read/Write | N/A |

#### Remarks

The Bluetooth core specification recommends to use 0x71764129 as the LE access address for all test packets. The preamble of LE-TP/LE-TP-EXT packets is either 01010101b or 10101010b, depending on the LSB of the LE access address. If the LSB of the LE access address is 1, the preamble shall be 01010101b, otherwise the preamble shall be 10101010b. This will be 0101010101010101b, 1010101010101010b respectively for LE-Enhanced packets.

The default value is 0x71764129.

Note: This attribute is applicable for LE packets.

Get Function: niBTSG_GetLEAccessAddress 
 Set Function: niBTSG_SetLEAccessAddress

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings_1gac4009755ee37a3015d84b80106b591e3.html language=enus -->
## TOPIC 00019: NIBTSG_ATTR_NUMBER_OF_IDLE_SLOTS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings_1gac4009755ee37a3015d84b80106b591e3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings_1gac4009755ee37a3015d84b80106b591e3.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of idle slots that the BT Generation appends at the end of each valid packet. SyntaxNIBTSG_ATTR_NUMBER_OF_IDLE_SLOTSNumeric ValueData TypeAccessApplies To52int32Read/WriteN/ARemarks The default value is 0.Get Function: niBTSG_GetNumberOfIdleSlots Set Function: niBTSG_SetNumberOf

### NIBTSG_ATTR_NUMBER_OF_IDLE_SLOTS

Specifies the number of idle slots that the BT Generation appends at the end of each valid packet.

#### Syntax

NIBTSG_ATTR_NUMBER_OF_IDLE_SLOTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 52 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetNumberOfIdleSlots 
 Set Function: niBTSG_SetNumberOfIdleSlots

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings_1gaef7846b547532b5466e4fc215deb9cf2.html language=enus -->
## TOPIC 00020: NIBTSG_ATTR_DATA_RATE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings_1gaef7846b547532b5466e4fc215deb9cf2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings_1gaef7846b547532b5466e4fc215deb9cf2.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Higher Data Throughput (HDT) Bit Rate. This property is applicable only when you set the packet type to LE-HDT. The default value is 2000000. Valid values are 2000000, 3000000, 4000000, 6000000, 7500000. SyntaxNIBTSG_ATTR_DATA_RATENumeric ValueData TypeAccessApplies To102int32Read/Writ

### NIBTSG_ATTR_DATA_RATE

Specifies the Higher Data Throughput (HDT) Bit Rate. This property is applicable only when you set the packet type to LE-HDT. The default value is 2000000. Valid values are 2000000, 3000000, 4000000, 6000000, 7500000.

#### Syntax

NIBTSG_ATTR_DATA_RATE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 102 | int32 | Read/Write | N/A |

#### Remarks

Get Function: niBTSG_GetDataRate 
 Set Function: niBTSG_SetDataRate

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga190d3f800b7306de370264a36bbe2941.html language=enus -->
## TOPIC 00021: NIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_POSITIONS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga190d3f800b7306de370264a36bbe2941.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga190d3f800b7306de370264a36bbe2941.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of sounding sequence marker positions at which sounding sequence marker signals are inserted. This property is applicable only when you set the CS SYNC Sequence to Sounding Sequence. SyntaxNIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_POSITIONSNumeric ValueData TypeAccessApplies To97int32R

### NIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_POSITIONS

Specifies an array of sounding sequence marker positions at which sounding sequence marker signals are inserted. This property is applicable only when you set the CS SYNC Sequence to Sounding Sequence.

#### Syntax

NIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_POSITIONS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 97 | int32 | Read/Write | N/A |

#### Remarks

When sounding sequence length property is set to 32, only the first element from the sounding sequence marker positions array is considered, and remaining elements are discarded. Valid values are from 0 to 28. 
 When sounding sequence length property is set to 96, up to the first two elements from sounding sequence marker positions array are considered and remaining elements are discarded. Valid values for array index 0 are from 0 to 63 and for array index 1 are from 67 to 92. 
 The default value is 0.

Get Function: niBTSG_GetSoundingSequenceMarkerPositions 
 Set Function: niBTSG_SetSoundingSequenceMarkerPositions

Parent topic:

Channel Sounding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga1fc3a5bd734dac6e172d766fefe7c862.html language=enus -->
## TOPIC 00022: NIBTSG_ATTR_CS_PACKET_FORMAT

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga1fc3a5bd734dac6e172d766fefe7c862.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga1fc3a5bd734dac6e172d766fefe7c862.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel sounding (CS) packet format. This property is applicable only when you set the packet type to either LE-CS-1M or LE-CS-2M. SyntaxNIBTSG_ATTR_CS_PACKET_FORMATNumeric ValueData TypeAccessApplies To92int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_PACKET_FORMAT_SYNC.Get

### NIBTSG_ATTR_CS_PACKET_FORMAT

Specifies the channel sounding (CS) packet format. This property is applicable only when you set the packet type to either LE-CS-1M or LE-CS-2M.

#### Syntax

NIBTSG_ATTR_CS_PACKET_FORMAT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 92 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_PACKET_FORMAT_SYNC.

Get Function: niBTSG_GetCSPacketFormat 
 Set Function: niBTSG_SetCSPacketFormat

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_CS_PACKET_FORMAT_SYNC | 0 (0x0) | Specifies that the CS packet format is SYNC. This packet consists of preamble, CS access address, trailer and sounding sequence field. The sounding sequence field is optional. |
| NIBTSG_VAL_CS_PACKET_FORMAT_CS_TONE | 1 (0x1) | Specifies that the CS packet format is CS Tone. This packet consists of unmodulated carrier. |
| NIBTSG_VAL_CS_PACKET_FORMAT_CS_TONE_AFTER_SYNC | 2 (0x2) | Specifies that the CS packet format is CS Tone after SYNC. This packet consists of SYNC followed by a CS Tone. |
| NIBTSG_VAL_CS_PACKET_FORMAT_CS_TONE_BEFORE_SYNC | 3 (0x3) | Specifies that the CS packet format is CS Tone before SYNC. This packet consists of CS Tone followed by a SYNC. |

Parent topic:

Channel Sounding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga29f37240a33afef1b32a371ac23c3245.html language=enus -->
## TOPIC 00023: NIBTSG_ATTR_CS_TONE_EXTENSION_SLOT_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga29f37240a33afef1b32a371ac23c3245.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga29f37240a33afef1b32a371ac23c3245.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether CS tone extension slot is present in generated LE CS packets. This property is applicable for all CS packet formats except NIBTSG_VAL_PACKET_FORMAT_SYNC. SyntaxNIBTSG_ATTR_CS_TONE_EXTENSION_SLOT_ENABLEDNumeric ValueData TypeAccessApplies To98int32Read/WriteN/ARemarks The default va

### NIBTSG_ATTR_CS_TONE_EXTENSION_SLOT_ENABLED

Specifies whether CS tone extension slot is present in generated LE CS packets. This property is applicable for all CS packet formats except NIBTSG_VAL_PACKET_FORMAT_SYNC.

#### Syntax

NIBTSG_ATTR_CS_TONE_EXTENSION_SLOT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 98 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_FALSE.

Get Function: niBTSG_GetCSToneExtensionSlotEnabled 
 Set Function: niBTSG_SetCSToneExtensionSlotEnabled

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Specifies that the generated LE CS packet does not contain CS tone extension slot. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Specifies that the generated LE CS packet contains CS tone extension slot. |

Parent topic:

Channel Sounding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga7d54de0e54794944f45b10cf79eab4fd.html language=enus -->
## TOPIC 00024: NIBTSG_ATTR_SOUNDING_SEQUENCE_LENGTH

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga7d54de0e54794944f45b10cf79eab4fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1ga7d54de0e54794944f45b10cf79eab4fd.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies sounding sequence length, in bits. This property is applicable only when you set the CS SYNC Sequence to Sounding Sequence. SyntaxNIBTSG_ATTR_SOUNDING_SEQUENCE_LENGTHNumeric ValueData TypeAccessApplies To95int32Read/WriteN/ARemarks The default value is 32. Valid values are 32 and 96. Get F

### NIBTSG_ATTR_SOUNDING_SEQUENCE_LENGTH

Specifies sounding sequence length, in bits. This property is applicable only when you set the CS SYNC Sequence to Sounding Sequence.

#### Syntax

NIBTSG_ATTR_SOUNDING_SEQUENCE_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 95 | int32 | Read/Write | N/A |

#### Remarks

The default value is 32. Valid values are 32 and 96. 
 Get Function: niBTSG_GetSoundingSequenceLength 
 Set Function: niBTSG_SetSoundingSequenceLength

Parent topic:

Channel Sounding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gab766ed1480802bb4237b4edd2d455ac6.html language=enus -->
## TOPIC 00025: NIBTSG_ATTR_CS_SYNC_SEQUENCE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gab766ed1480802bb4237b4edd2d455ac6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gab766ed1480802bb4237b4edd2d455ac6.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the sounding sequence field is present in SYNC packet. This property is applicable for all CS Packet formats except CS Tone. SyntaxNIBTSG_ATTR_CS_SYNC_SEQUENCENumeric ValueData TypeAccessApplies To93int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_SYNC_SEQUENCE_SOUNDING_SE

### NIBTSG_ATTR_CS_SYNC_SEQUENCE

Specifies whether the sounding sequence field is present in SYNC packet. This property is applicable for all CS Packet formats except CS Tone.

#### Syntax

NIBTSG_ATTR_CS_SYNC_SEQUENCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 93 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_SYNC_SEQUENCE_SOUNDING_SEQUENCE.

Get Function: niBTSG_GetCSSyncSequence 
 Set Function: niBTSG_SetCSSyncSequence

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_CS_SYNC_SEQUENCE_NONE | 0 (0x0) | Specifies that the LE CS packet does not contain sounding sequence field. |
| NIBTSG_VAL_CS_SYNC_SEQUENCE_SOUNDING_SEQUENCE | 1 (0x1) | Specifies that the LE CS packet contain sounding sequence field. |
| NIBTSG_VAL_CS_SYNC_SEQUENCE_PAYLOAD_PATTERN | 2 (0x2) | Specifies that the LE CS packet contain payload bit pattern field. |

Parent topic:

Channel Sounding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gac2434725d685e90ac0e7bb90329068c9.html language=enus -->
## TOPIC 00026: NIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_SIGNALS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gac2434725d685e90ac0e7bb90329068c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gac2434725d685e90ac0e7bb90329068c9.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of sounding sequence marker signals. This property is applicable only when you set the CS SYNC Sequence to Sounding Sequence. SyntaxNIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_SIGNALSNumeric ValueData TypeAccessApplies To96int32Read/WriteN/ARemarks When sounding sequence length property

### NIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_SIGNALS

Specifies an array of sounding sequence marker signals. This property is applicable only when you set the CS SYNC Sequence to Sounding Sequence.

#### Syntax

NIBTSG_ATTR_SOUNDING_SEQUENCE_MARKER_SIGNALS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 96 | int32 | Read/Write | N/A |

#### Remarks

When sounding sequence length property is set to 32, only the first element shall be inserted in the sounding sequence, and remaining elements shall be discarded. 
 When sounding sequence length property is set to 96, up to the first two elements shall be inserted in the sounding sequence, and remaining elements shall be discarded. 
 The default value is NIBTSG_VAL_SOUNDING_SEQUENCE_MARKER_SIGNALS_1100.

Get Function: niBTSG_GetSoundingSequenceMarkerSignals 
 Set Function: niBTSG_SetSoundingSequenceMarkerSignals

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_SOUNDING_SEQUENCE_MARKER_SIGNALS_1100 | 0 (0x0) | Specifies that the sounding sequence marker signal inserted in the sounding sequence is 1100 |
| NIBTSG_VAL_SOUNDING_SEQUENCE_MARKER_SIGNALS_0011 | 1 (0x1) | Specifies that the sounding sequence marker signal inserted in the sounding sequence is 0011 |

Parent topic:

Channel Sounding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gac6cc989b393df4309766a4956f82b814.html language=enus -->
## TOPIC 00027: NIBTSG_ATTR_CS_PHASE_MEASUREMENT_PERIOD

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gac6cc989b393df4309766a4956f82b814.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__channel__sounding_1gac6cc989b393df4309766a4956f82b814.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase measurement period in the generated CS packet. This property is applicable for all CS packet formats except NIBTSG_VAL_PACKET_FORMAT_SYNC. SyntaxNIBTSG_ATTR_CS_PHASE_MEASUREMENT_PERIODNumeric ValueData TypeAccessApplies To94float64Read/WriteN/ARemarks The default value is 10us. V

### NIBTSG_ATTR_CS_PHASE_MEASUREMENT_PERIOD

Specifies the phase measurement period in the generated CS packet. This property is applicable for all CS packet formats except NIBTSG_VAL_PACKET_FORMAT_SYNC.

#### Syntax

NIBTSG_ATTR_CS_PHASE_MEASUREMENT_PERIOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 94 | float64 | Read/Write | N/A |

#### Remarks

The default value is 10us. Valid values are 10 us, 20us and 40 us.

Get Function: niBTSG_GetCSPhaseMeasurementPeriod 
 Set Function: niBTSG_SetCSPhaseMeasurementPeriod

Parent topic:

Channel Sounding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding.html language=enus -->
## TOPIC 00028: Direction Finding

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATIONSpecifies the duration for which the transitions of phase and amplitude take place in the switching slots of the constant tone extension (CTE) portion of the low energy (LE) packet. This attribute is applic

### Direction Finding

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION | Specifies the duration for which the transitions of phase and amplitude take place in the switching slots of the constant tone extension (CTE) portion of the low energy (LE) packet. This attribute is applicable only when the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED attribute to NIBTSG_VAL_TRUE. |
| NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION_USED | Returns the actual duration used to make the transitions of phase and amplitude in the switching slots of the constant tone extension (CTE) portion of low energy (LE) packet. This attribute is applicable only when you set the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED attribute to NIBTSG_VAL_TRUE. |
| NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED | Specifies whether antenna switching is enabled for the generated low energy (LE) packets. This attribute is valid only when you set the NIBTSG_ATTR_DIRECTION_FINDING_MODE attribute to NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBTSG_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. |
| NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN | Specifies the pattern in which the antennas switch in constant tone extension (CTE) portion of the low energy (LE) packet. The current definition always treats A0 as the reference antenna. A1, A2, A3...Am are all non-reference antennas. This attribute is applicable only when you set the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED to NIBTSG_VAL_TRUE. |
| NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_LENGTH | Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the NIBTSG_ATTR_DIRECTION_FINDING_MODE attribute to either NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBTSG_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. |
| NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_SLOT_DURATION | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. |
| NIBTSG_ATTR_DIRECTION_FINDING_MODE | Specifies the mode for direction finding. The attribute is valid only for LE-TP, LE-TP EXT, LE-Enhanced and LE-HDT packet type. |
| NIBTSG_ATTR_DIRECTION_FINDING_NUMBER_OF_ANTENNAS | Specifies the number of antennas used to transmit or receive the constant tone extension (CTE) portion of low energy (LE) packet. This attribute is applicable only when you set the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED to NIBTSG_VAL_TRUE. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga3151eaff0490694158b04e6c7e232023.html language=enus -->
## TOPIC 00029: NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_SLOT_DURATION

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga3151eaff0490694158b04e6c7e232023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga3151eaff0490694158b04e6c7e232023.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. SyntaxNIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_SLOT_DURATIONNumeric ValueData TypeAccessApplies To78float64Read/WriteN/ARemarks The default value is

### NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_SLOT_DURATION

Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_SLOT_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 78 | float64 | Read/Write | N/A |

#### Remarks

The default value is 1 us. Valid values are 1 us and 2 us.

Get Function: niBTSG_GetDirectionFindingConstantToneExtensionSlotDuration 
 Set Function: niBTSG_SetDirectionFindingConstantToneExtensionSlotDuration

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga6dfd5dd7b7de3b503b7ec5e3977716c5.html language=enus -->
## TOPIC 00030: NIBTSG_ATTR_DIRECTION_FINDING_NUMBER_OF_ANTENNAS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga6dfd5dd7b7de3b503b7ec5e3977716c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga6dfd5dd7b7de3b503b7ec5e3977716c5.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of antennas used to transmit or receive the constant tone extension (CTE) portion of low energy (LE) packet. This attribute is applicable only when you set the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED to NIBTSG_VAL_TRUE. SyntaxNIBTSG_ATTR_DIRECTION_FINDING_NUMBER_

### NIBTSG_ATTR_DIRECTION_FINDING_NUMBER_OF_ANTENNAS

Specifies the number of antennas used to transmit or receive the constant tone extension (CTE) portion of low energy (LE) packet. This attribute is applicable only when you set the [NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html) to NIBTSG_VAL_TRUE.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_NUMBER_OF_ANTENNAS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 82 | int32 | Read/Write | N/A |

#### Remarks

Get Function: niBTSG_GetDirectionFindingNumberOfAntennas 
 Set Function: niBTSG_SetDirectionFindingNumberOfAntennas

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga861e2a1e711b26760f76fa41af760778.html language=enus -->
## TOPIC 00031: NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga861e2a1e711b26760f76fa41af760778.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga861e2a1e711b26760f76fa41af760778.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration for which the transitions of phase and amplitude take place in the switching slots of the constant tone extension (CTE) portion of the low energy (LE) packet. This attribute is applicable only when the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED attribute to NIBTSG

### NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION

Specifies the duration for which the transitions of phase and amplitude take place in the switching slots of the constant tone extension (CTE) portion of the low energy (LE) packet. This attribute is applicable only when the [NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html) attribute to NIBTSG_VAL_TRUE.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 87 | float64 | Read/Write | N/A |

#### Remarks

The default value is 500n.

Get Function: niBTSG_GetDirectionFindingAntennaSwitchingDuration 
 Set Function: niBTSG_SetDirectionFindingAntennaSwitchingDuration

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga8c8615a65828d1e6a8b857ccf95cefac.html language=enus -->
## TOPIC 00032: NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga8c8615a65828d1e6a8b857ccf95cefac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga8c8615a65828d1e6a8b857ccf95cefac.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pattern in which the antennas switch in constant tone extension (CTE) portion of the low energy (LE) packet. The current definition always treats A0 as the reference antenna. A1, A2, A3...Am are all non-reference antennas. This attribute is applicable only when you set the NIBTSG_ATTR_

### NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN

Specifies the pattern in which the antennas switch in constant tone extension (CTE) portion of the low energy (LE) packet. The current definition always treats A0 as the reference antenna. A1, A2, A3...Am are all non-reference antennas. This attribute is applicable only when you set the [NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html) to NIBTSG_VAL_TRUE.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 85 | ViChar | Read/Write | N/A |

#### Remarks

Get Function: niBTSG_GetDirectionFindingAntennaSwitchingPattern 
 Set Function: niBTSG_SetDirectionFindingAntennaSwitchingPattern

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga91c2bbe68cc90eacf187882d4958d496.html language=enus -->
## TOPIC 00033: NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION_USED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga91c2bbe68cc90eacf187882d4958d496.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga91c2bbe68cc90eacf187882d4958d496.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual duration used to make the transitions of phase and amplitude in the switching slots of the constant tone extension (CTE) portion of low energy (LE) packet. This attribute is applicable only when you set the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED attribute to NIBTS

### NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION_USED

Returns the actual duration used to make the transitions of phase and amplitude in the switching slots of the constant tone extension (CTE) portion of low energy (LE) packet. This attribute is applicable only when you set the [NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html) attribute to NIBTSG_VAL_TRUE.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION_USED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 88 | float64 | Read/Write | N/A |

#### Remarks

Get Function: niBTSG_GetDirectionFindingAntennaSwitchingDurationUsed

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html language=enus -->
## TOPIC 00034: NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether antenna switching is enabled for the generated low energy (LE) packets. This attribute is valid only when you set the NIBTSG_ATTR_DIRECTION_FINDING_MODE attribute to NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBTSG_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. SyntaxNIBTSG

### NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED

Specifies whether antenna switching is enabled for the generated low energy (LE) packets. This attribute is valid only when you set the [NIBTSG_ATTR_DIRECTION_FINDING_MODE](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gafc1623bfb99ffb904506fed1d2778b5d.html) attribute to NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBTSG_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 86 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_FALSE.

Get Function: niBTSG_GetDirectionFindingAntennaSwitchingEnabled 
 Set Function: niBTSG_SetDirectionFindingAntennaSwitchingEnabled

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gabd37834e3bafaf7378440e4f39e47414.html language=enus -->
## TOPIC 00035: NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_LENGTH

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gabd37834e3bafaf7378440e4f39e47414.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gabd37834e3bafaf7378440e4f39e47414.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the NIBTSG_ATTR_DIRECTION_FINDING_MODE attribute to either NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBTSG_DIRECTION_FIND

### NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_LENGTH

Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the [NIBTSG_ATTR_DIRECTION_FINDING_MODE](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gafc1623bfb99ffb904506fed1d2778b5d.html) attribute to either NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBTSG_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 77 | float64 | Read/Write | N/A |

#### Remarks

The default value is 0.00016.

Get Function: niBTSG_GetDirectionFindingConstantToneExtensionLength 
 Set Function: niBTSG_SetDirectionFindingConstantToneExtensionLength

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gafc1623bfb99ffb904506fed1d2778b5d.html language=enus -->
## TOPIC 00036: NIBTSG_ATTR_DIRECTION_FINDING_MODE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gafc1623bfb99ffb904506fed1d2778b5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gafc1623bfb99ffb904506fed1d2778b5d.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode for direction finding. The attribute is valid only for LE-TP, LE-TP EXT, LE-Enhanced and LE-HDT packet type. SyntaxNIBTSG_ATTR_DIRECTION_FINDING_MODENumeric ValueData TypeAccessApplies To75int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_DIRECTION_FINDING_MODE_DISABLE.Get

### NIBTSG_ATTR_DIRECTION_FINDING_MODE

Specifies the mode for direction finding. The attribute is valid only for LE-TP, LE-TP EXT, LE-Enhanced and LE-HDT packet type.

#### Syntax

NIBTSG_ATTR_DIRECTION_FINDING_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 75 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_DIRECTION_FINDING_MODE_DISABLE.

Get Function: niBTSG_GetDirectionFindingMode 
 Set Function: niBTSG_SetDirectionFindingMode

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_DIRECTION_FINDING_MODE_DISABLED | 0 (0x0) | Specifies that the LE uncoded packets does not have CTE field. |
| NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL | 1 (0x1) | Specifies that the LE uncoded packets have AoA CTE field. |
| NIBTSG_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE | 2 (0x2) | Specifies that the LE uncoded packets have AoD CTE field. |

Parent topic:

Direction Finding

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings.html language=enus -->
## TOPIC 00037: Dirty Tx Settings

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SETSpecifies the offset value of each of the impairment set that you enable in the NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET attribute. NIBTSG_ATTR_DIRTY_TX_ENABLEDSpecifies whether to enable the dirty transmitter.

### Dirty Tx Settings

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SET | Specifies the offset value of each of the impairment set that you enable in the NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET attribute. |
| NIBTSG_ATTR_DIRTY_TX_ENABLED | Specifies whether to enable the dirty transmitter. |
| NIBTSG_ATTR_DIRTY_TX_MODE | Specifies whether to enable the dirty transmitter with the standard settings, the user-defined settings or the frequency drift. |
| NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_SET | Specifies the modulation index value of each of the impairment set that you enable in the NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET attribute. |
| NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_TYPE | Specifies whether the modulation index type is NIBTSG_DIRTY_TX_MODULATION_INDEX_TYPE_STANDARD or NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STABLE. |
| NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET | Specifies the impairment sets that you must enable out of the ten sets in LE and BR or the three sets in EDR. |
| NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_DEVIATION | Specifies the frequency of the modulated signal to provide the additional frequency drift. This value is expressed in Hz. |
| NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_FREQUENCY | Specifies the frequency deviation of the modulated signal to provide the additional frequency drift. This value is expressed in Hz. |
| NIBTSG_ATTR_DIRTY_TX_SYMBOL_TIMING_ERROR_SET | Specifies the symbol timing error value of each of the impairment set that you enable in the NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET attribute. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga0eabd9d2714e8483adf1098a02fb308a.html language=enus -->
## TOPIC 00038: NIBTSG_ATTR_DIRTY_TX_SYMBOL_TIMING_ERROR_SET

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga0eabd9d2714e8483adf1098a02fb308a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga0eabd9d2714e8483adf1098a02fb308a.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the symbol timing error value of each of the impairment set that you enable in the NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET attribute. SyntaxNIBTSG_ATTR_DIRTY_TX_SYMBOL_TIMING_ERROR_SETNumeric ValueData TypeAccessApplies To59int32 []Read/WriteN/ARemarks This attribute is applicable with

### NIBTSG_ATTR_DIRTY_TX_SYMBOL_TIMING_ERROR_SET

Specifies the symbol timing error value of each of the impairment set that you enable in the [NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga7fcad9a1354ac8ba159e6e9ca2ec1143.html) attribute.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_SYMBOL_TIMING_ERROR_SET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 59 | int32 [] | Read/Write | N/A |

#### Remarks

This attribute is applicable with you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED. The BT Generation ignores this attribute if you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.

Get Function: niBTSG_GetDirtyTxSymbolTimingErrorSet 
 Set Function: niBTSG_SetDirtyTxSymbolTimingErrorSet

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga13d90ae2c225adccea947acd009a4bf1.html language=enus -->
## TOPIC 00039: NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_DEVIATION

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga13d90ae2c225adccea947acd009a4bf1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga13d90ae2c225adccea947acd009a4bf1.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the modulated signal to provide the additional frequency drift. This value is expressed in Hz. SyntaxNIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_DEVIATIONNumeric ValueData TypeAccessApplies To62float64Read/WriteN/ARemarks This attribute is applicable when you set the NIBTSG_ATTR_DIRT

### NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_DEVIATION

Specifies the frequency of the modulated signal to provide the additional frequency drift. This value is expressed in Hz.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 62 | float64 | Read/Write | N/A |

#### Remarks

This attribute is applicable when you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED. The BT Generation ignores this attribute if you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.

The default value is 0.

Get Function: niBTSG_GetDirtyTxResidualFmFrequency 
 Set Function: niBTSG_SetDirtyTxResidualFmFrequency

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html language=enus -->
## TOPIC 00040: NIBTSG_ATTR_DIRTY_TX_MODE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the dirty transmitter with the standard settings, the user-defined settings or the frequency drift. SyntaxNIBTSG_ATTR_DIRTY_TX_MODENumeric ValueData TypeAccessApplies To55int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.Get Function: niBTSG

### NIBTSG_ATTR_DIRTY_TX_MODE

Specifies whether to enable the dirty transmitter with the standard settings, the user-defined settings or the frequency drift.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 55 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.

Get Function: niBTSG_GetDirtyTxMode 
 Set Function: niBTSG_SetDirtyTxMode

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_DIRTY_TX_MODE_STANDARD | 0 (0x0) | Enables the dirty transmitter with the standard settings. |
| NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED | 1 (0x1) | Enables the dirty transmitter with the user-defined settings. |
| NIBTSG_VAL_DIRTY_TX_MODE_FREQUENCY_DRIFT | 2 (0x2) | Enables the dirty transmitter with the standard defined frequency drift only for LE HDT packets. |

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga54828413e91135f5a21bc36477b35f73.html language=enus -->
## TOPIC 00041: NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_FREQUENCY

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga54828413e91135f5a21bc36477b35f73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga54828413e91135f5a21bc36477b35f73.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency deviation of the modulated signal to provide the additional frequency drift. This value is expressed in Hz. SyntaxNIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_FREQUENCYNumeric ValueData TypeAccessApplies To63float64Read/WriteN/ARemarks This attribute is applicable when you set the NIBTSG

### NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_FREQUENCY

Specifies the frequency deviation of the modulated signal to provide the additional frequency drift. This value is expressed in Hz.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_RESIDUAL_FM_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 63 | float64 | Read/Write | N/A |

#### Remarks

This attribute is applicable when you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED. The BT Generation ignores this attribute if you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.

The default value is 0.

Get Function: niBTSG_GetDirtyTxResidualFmDeviation 
 Set Function: niBTSG_SetDirtyTxResidualFmDeviation

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga76d807fea6b4980a0976e6d0a871700b.html language=enus -->
## TOPIC 00042: NIBTSG_ATTR_DIRTY_TX_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga76d807fea6b4980a0976e6d0a871700b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga76d807fea6b4980a0976e6d0a871700b.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the dirty transmitter. SyntaxNIBTSG_ATTR_DIRTY_TX_ENABLEDNumeric ValueData TypeAccessApplies To30int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_FALSE.Get Function: niBTSG_GetDirtyTxEnabled Set Function: niBTSG_SetDirtyTxEnabledNameValueDescriptionNIBTSG_VAL_FAL

### NIBTSG_ATTR_DIRTY_TX_ENABLED

Specifies whether to enable the dirty transmitter.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 30 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_FALSE.

Get Function: niBTSG_GetDirtyTxEnabled 
 Set Function: niBTSG_SetDirtyTxEnabled

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Disables the dirty transmitter. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Enables the dirty transmitter. |

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga7fcad9a1354ac8ba159e6e9ca2ec1143.html language=enus -->
## TOPIC 00043: NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga7fcad9a1354ac8ba159e6e9ca2ec1143.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga7fcad9a1354ac8ba159e6e9ca2ec1143.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the impairment sets that you must enable out of the ten sets in LE and BR or the three sets in EDR. SyntaxNIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SETNumeric ValueData TypeAccessApplies To56int32 []Read/WriteN/ARemarks This attribute is applicable if you set the NIBTSG_ATTR_DIRTY_TX_MODE at

### NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET

Specifies the impairment sets that you must enable out of the ten sets in LE and BR or the three sets in EDR.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 56 | int32 [] | Read/Write | N/A |

#### Remarks

This attribute is applicable if you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED. The BT Generation ignores this attribute when the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute is set to NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.

Get Function: niBTSG_GetDirtyTxParametersEnabledSet 
 Set Function: niBTSG_SetDirtyTxParametersEnabledSet

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Specifies that the BT Generation does not use the parameters in the impairment sets. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Specifies that the BT Generation uses the parameters in the impairment sets. |

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga8e5649ce295ae587d63b11fe18cdef60.html language=enus -->
## TOPIC 00044: NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_TYPE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga8e5649ce295ae587d63b11fe18cdef60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga8e5649ce295ae587d63b11fe18cdef60.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the modulation index type is NIBTSG_DIRTY_TX_MODULATION_INDEX_TYPE_STANDARD or NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STABLE. SyntaxNIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_TYPENumeric ValueData TypeAccessApplies To67int32Read/WriteN/ARemarks This attribute is valid only for LE pac

### NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_TYPE

Specifies whether the modulation index type is NIBTSG_DIRTY_TX_MODULATION_INDEX_TYPE_STANDARD or NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STABLE.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 67 | int32 | Read/Write | N/A |

#### Remarks

This attribute is valid only for LE packets. This attribute is applicable only if [NIBTSG_ATTR_DIRTY_TX_ENABLED](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga76d807fea6b4980a0976e6d0a871700b.html) attribute is set to NIBTSG_VAL_TRUE. 
 The default value is NIBTSG_DIRTY_TX_MODULATION_INDEX_TYPE_STANDARD.

Get Function: niBTSG_GetDirtyTxModulationIndexType 
 Set Function: niBTSG_SetDirtyTxModulationIndexType

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STANDARD | 0 (0x0) | Specifies that the modulation index type is standard. |
| NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STABLE | 1 (0x1) | Specifies that the modulation index type is stable. |

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1gabe8dab0b77c2607c24ab26e0d08f8706.html language=enus -->
## TOPIC 00045: NIBTSG_ATTR_DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SET

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1gabe8dab0b77c2607c24ab26e0d08f8706.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1gabe8dab0b77c2607c24ab26e0d08f8706.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset value of each of the impairment set that you enable in the NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET attribute. SyntaxNIBTSG_ATTR_DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SETNumeric ValueData TypeAccessApplies To57int32 []Read/WriteN/ARemarks This attribute is applicable with you set

### NIBTSG_ATTR_DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SET

Specifies the offset value of each of the impairment set that you enable in the [NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga7fcad9a1354ac8ba159e6e9ca2ec1143.html) attribute.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 57 | int32 [] | Read/Write | N/A |

#### Remarks

This attribute is applicable with you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED. The BT Generation ignores this attribute if you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.

Get Function: niBTSG_GetDirtyTxCarrierFrequencyOffsetSet 
 Set Function: niBTSG_SetDirtyTxCarrierFrequencyOffsetSet

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1gade9886efb291b9782be1b9b5ab65b3d8.html language=enus -->
## TOPIC 00046: NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_SET

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1gade9886efb291b9782be1b9b5ab65b3d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1gade9886efb291b9782be1b9b5ab65b3d8.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation index value of each of the impairment set that you enable in the NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET attribute. SyntaxNIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_SETNumeric ValueData TypeAccessApplies To58float64 []Read/WriteN/ARemarks This attribute is applicable when you

### NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_SET

Specifies the modulation index value of each of the impairment set that you enable in the [NIBTSG_ATTR_DIRTY_TX_PARAMETERS_ENABLED_SET](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga7fcad9a1354ac8ba159e6e9ca2ec1143.html) attribute.

#### Syntax

NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_SET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 58 | float64 [] | Read/Write | N/A |

#### Remarks

This attribute is applicable when you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_USER_DEFINED. The BT Generation ignores this attribute if you set the [NIBTSG_ATTR_DIRTY_TX_MODE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga37df6b1d4c6757ac0405972756a46284.html) attribute to NIBTSG_VAL_DIRTY_TX_MODE_STANDARD.

Valid values are 0.28 to 0.4 for Basic Rate and EDR packets and 0.45 to 0.55 for LE packets, inclusive. The valid values are 0.495 to 0.505, inclusive, for LE packets when you set the [NIBTSG_ATTR_DIRTY_TX_MODULATION_INDEX_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__dirty__tx__settings_1ga8e5649ce295ae587d63b11fe18cdef60.html) attribute to NIBTSG_VAL_DIRTY_TX_MODULATION_INDEX_TYPE_STABLE.

Get Function: niBTSG_GetDirtyTxModulationIndexSet 
 Set Function: niBTSG_SetDirtyTxModulationIndexSet

Parent topic:

Dirty Tx Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload.html language=enus -->
## TOPIC 00047: DV Voice Payload

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPESpecifies the type of payload for the data voice (DV) packet. NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDERSpecifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_DV_VOICE

### DV Voice Payload

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE | Specifies the type of payload for the data voice (DV) packet. |
| NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDER | Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDER attribute. |
| NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_SEED | Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_SEED attribute. |
| NIBTSG_ATTR_DV_VOICE_PAYLOAD_USER_DEFINED_BITS | Specifies a bit pattern as an array of zeros and ones. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga26722bd3c450ea5f7a966a3b8eed4288.html language=enus -->
## TOPIC 00048: NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_SEED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga26722bd3c450ea5f7a966a3b8eed4288.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga26722bd3c450ea5f7a966a3b8eed4288.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_SEED attribute. SyntaxNIBTSG_ATT

### NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_SEED

Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the [NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga9f0b7069e5574ee746aa454005f80627.html) attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the [NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_SEED](group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga26722bd3c450ea5f7a966a3b8eed4288.html) attribute.

#### Syntax

NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_SEED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 47 | int32 | Read/Write | N/A |

#### Remarks

The default value is 497.

Get Function: niBTSG_GetDVVoicePayloadPNSeed 
 Set Function: niBTSG_SetDVVoicePayloadPNSeed

Parent topic:

DV Voice Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga8c2f24d35ec17e6a0df0c15f17879146.html language=enus -->
## TOPIC 00049: NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDER

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga8c2f24d35ec17e6a0df0c15f17879146.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga8c2f24d35ec17e6a0df0c15f17879146.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDER attribute. SyntaxNIBTSG_ATT

### NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDER

Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the [NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga9f0b7069e5574ee746aa454005f80627.html) attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the [NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDER](group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga8c2f24d35ec17e6a0df0c15f17879146.html) attribute.

#### Syntax

NIBTSG_ATTR_DV_VOICE_PAYLOAD_PN_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 46 | int32 | Read/Write | N/A |

#### Remarks

The default value is 9. Valid values are 5 to 31, inclusive.

Get Function: niBTSG_GetDVVoicePayloadPNOrder 
 Set Function: niBTSG_SetDVVoicePayloadPNOrder

Parent topic:

DV Voice Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga9f0b7069e5574ee746aa454005f80627.html language=enus -->
## TOPIC 00050: NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga9f0b7069e5574ee746aa454005f80627.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga9f0b7069e5574ee746aa454005f80627.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of payload for the data voice (DV) packet. SyntaxNIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPENumeric ValueData TypeAccessApplies To49int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE.Get Function: niBTSG_GetDvVoicePayloadDataType Set Function: niBTS

### NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE

Specifies the type of payload for the data voice (DV) packet.

#### Syntax

NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 49 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE.

Get Function: niBTSG_GetDvVoicePayloadDataType 
 Set Function: niBTSG_SetDvVoicePayloadDataType

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE | 0 (0x0) | Specifies that the BT Generation uses a Galois pseudonoise (PN) bit sequence with a payload order and seed, which you specify in the NIBTSG_DV_VOICE_PAYLOAD_PN_ORDER and NIBTSG_DV_VOICE_PAYLOAD_PN_SEED attributes respectively, to create the payload for generation. |
| NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS | 1 (0x1) | Specifies that the BT Generation repeats the bit pattern, which you specify in the NIBTSG_DV_VOICE_PAYLOAD_USER_DEFINED_BITS attribute, to achieve the necessary payload length. |

Parent topic:

DV Voice Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1gaa12ca85c4d1c70cc569dc33c3b8dcff9.html language=enus -->
## TOPIC 00051: NIBTSG_ATTR_DV_VOICE_PAYLOAD_USER_DEFINED_BITS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1gaa12ca85c4d1c70cc569dc33c3b8dcff9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1gaa12ca85c4d1c70cc569dc33c3b8dcff9.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a bit pattern as an array of zeros and ones. SyntaxNIBTSG_ATTR_DV_VOICE_PAYLOAD_USER_DEFINED_BITSNumeric ValueData TypeAccessApplies To48int32 []Read/WriteN/ARemarks If the array length is greater than the required payload length, the BT Generation uses a subset of the required length from

### NIBTSG_ATTR_DV_VOICE_PAYLOAD_USER_DEFINED_BITS

Specifies a bit pattern as an array of zeros and ones.

#### Syntax

NIBTSG_ATTR_DV_VOICE_PAYLOAD_USER_DEFINED_BITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 48 | int32 [] | Read/Write | N/A |

#### Remarks

If the array length is greater than the required payload length, the BT Generation uses a subset of the required length from the beginning of the array for waveform generation. If the array length is less than the required payload length, the BT Generation repeats the bit pattern until the required length is achieved. If you set the [NIBTSG_ATTR_DV_VOICE_PAYLOAD_DATA_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1ga9f0b7069e5574ee746aa454005f80627.html) attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE, the BT Generation ignores the [NIBTSG_ATTR_DV_VOICE_PAYLOAD_USER_DEFINED_BITS](group____root__ni_b_t_generation__attributes__packet__settings__dv__voice__payload_1gaa12ca85c4d1c70cc569dc33c3b8dcff9.html) attribute.

Get Function: niBTSG_GetDVVoicePayloadUserDefinedBits 
 Set Function: niBTSG_SetDVVoicePayloadUserDefinedBits

Parent topic:

DV Voice Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload.html language=enus -->
## TOPIC 00052: FHS Payload

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsBD AddressGroup membersNameDescriptionNIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLASSSpecifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the class of device of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bl

### FHS Payload

#### Groups

- BD Address

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLASS | Specifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the class of device of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the device class field in the FHS packet payload. |
| NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLOCK | Specifies the 26-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the value of the native clock of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the device clock field of the FHS packet payload. |
| NIBTSG_ATTR_FHS_PAYLOAD_LT_ADDRESS | Specifies the 3-bit logical transport (LT) address of the frequency hop synchronization (FHS) packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth specification v2.1+EDR for more information about the LT address of the FHS packet. |
| NIBTSG_ATTR_FHS_PAYLOAD_PAGE_SCAN_MODE | Specifies the 3-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the default scan mode used by the sender of the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the page scan mode field of the FHS packet payload. |
| NIBTSG_ATTR_FHS_PAYLOAD_SCAN_REPETITION | Specifies the 2-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the interval between two consecutive page scan windows. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth specification v2.1+EDR for more information about the payload scan repetition field of the FHS packet payload. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga2a2fff2bb614710ceb5404c9b582001f.html language=enus -->
## TOPIC 00053: NIBTSG_ATTR_FHS_PAYLOAD_LT_ADDRESS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga2a2fff2bb614710ceb5404c9b582001f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga2a2fff2bb614710ceb5404c9b582001f.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 3-bit logical transport (LT) address of the frequency hop synchronization (FHS) packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth specification v2.1+EDR for more information about the LT address of the FHS packet. SyntaxNIBTSG_ATTR_FHS_PAYLOAD_LT_ADDRESSNumeric ValueD

### NIBTSG_ATTR_FHS_PAYLOAD_LT_ADDRESS

Specifies the 3-bit logical transport (LT) address of the frequency hop synchronization (FHS) packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth specification v2.1+EDR for more information about the LT address of the FHS packet.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_LT_ADDRESS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 21 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0 to 7, inclusive.

Get Function: niBTSG_GetFHSPayloadLTAddress 
 Set Function: niBTSG_SetFHSPayloadLTAddress

Parent topic:

FHS Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga42b8de22d62e3045c1239607ddc9e67e.html language=enus -->
## TOPIC 00054: NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLASS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga42b8de22d62e3045c1239607ddc9e67e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga42b8de22d62e3045c1239607ddc9e67e.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the class of device of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the device class field

### NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLASS

Specifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the class of device of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the device class field in the FHS packet payload.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLASS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 22 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0 to 0xFFFFFF, inclusive.

Get Function: niBTSG_GetFHSPayloadDeviceClass 
 Set Function: niBTSG_SetFHSPayloadDeviceClass

Parent topic:

FHS Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga4459f1c09d65727ef0284f731ed9ce9d.html language=enus -->
## TOPIC 00055: NIBTSG_ATTR_FHS_PAYLOAD_PAGE_SCAN_MODE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga4459f1c09d65727ef0284f731ed9ce9d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga4459f1c09d65727ef0284f731ed9ce9d.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 3-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the default scan mode used by the sender of the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the page scan mode field

### NIBTSG_ATTR_FHS_PAYLOAD_PAGE_SCAN_MODE

Specifies the 3-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the default scan mode used by the sender of the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the page scan mode field of the FHS packet payload.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_PAGE_SCAN_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 25 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0 to 7, inclusive.

Get Function: niBTSG_GetFHSPayloadPageScanMode 
 Set Function: niBTSG_SetFHSPayloadPageScanMode

Parent topic:

FHS Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga8fc5949e32834a49b678465d4d4b2bb6.html language=enus -->
## TOPIC 00056: NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLOCK

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga8fc5949e32834a49b678465d4d4b2bb6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1ga8fc5949e32834a49b678465d4d4b2bb6.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 26-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the value of the native clock of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the device cl

### NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLOCK

Specifies the 26-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the value of the native clock of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the device clock field of the FHS packet payload.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_DEVICE_CLOCK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 26 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetFHSPayloadDeviceClock 
 Set Function: niBTSG_SetFHSPayloadDeviceClock

Parent topic:

FHS Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1gacadcd5a8d0524e0ee446e7fc1a7991f1.html language=enus -->
## TOPIC 00057: NIBTSG_ATTR_FHS_PAYLOAD_SCAN_REPETITION

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1gacadcd5a8d0524e0ee446e7fc1a7991f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload_1gacadcd5a8d0524e0ee446e7fc1a7991f1.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 2-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the interval between two consecutive page scan windows. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth specification v2.1+EDR for more information about the payload scan repetition

### NIBTSG_ATTR_FHS_PAYLOAD_SCAN_REPETITION

Specifies the 2-bit field in the frequency hop synchronization (FHS) packet payload. This field indicates the interval between two consecutive page scan windows. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth specification v2.1+EDR for more information about the payload scan repetition field of the FHS packet payload.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_SCAN_REPETITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 24 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0 to 3, inclusive.

Get Function: niBTSG_GetFHSPayloadScanRepetition 
 Set Function: niBTSG_SetFHSPayloadScanRepetition

Parent topic:

FHS Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address.html language=enus -->
## TOPIC 00058: BD Address

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_LAPSpecifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the lower address part (LAP) of the device that sends the FHS packet. NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_NAPSpecifies

### BD Address

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_LAP | Specifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the lower address part (LAP) of the device that sends the FHS packet. |
| NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_NAP | Specifies the 16-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the non-significant address part (NAP) of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the NAP field. |
| NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_UAP | Specifies the 8-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the upper address part (UAP) of the device that sends the FHS packet. |

#### Attachments

None

Parent topic:

FHS Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1ga37fd91b06572e38ce92948f1db2812b1.html language=enus -->
## TOPIC 00059: NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_LAP

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1ga37fd91b06572e38ce92948f1db2812b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1ga37fd91b06572e38ce92948f1db2812b1.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the lower address part (LAP) of the device that sends the FHS packet. SyntaxNIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_LAPNumeric ValueData TypeAccessApplies To27int32Read/WriteN/ARemarks The default va

### NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_LAP

Specifies the 24-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the lower address part (LAP) of the device that sends the FHS packet.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_LAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 27 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetFHSPayloadBDAddress 
 Set Function: niBTSG_SetFHSPayloadBDAddress

Parent topic:

BD Address

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1ga6f3c63d567169f777966b2ae4c3a2966.html language=enus -->
## TOPIC 00060: NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_NAP

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1ga6f3c63d567169f777966b2ae4c3a2966.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1ga6f3c63d567169f777966b2ae4c3a2966.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 16-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the non-significant address part (NAP) of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the

### NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_NAP

Specifies the 16-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the non-significant address part (NAP) of the device that sends the FHS packet. Refer to Section 6.5.1.4, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the NAP field.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_NAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 29 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetFHSPayloadBDAddress 
 Set Function: niBTSG_SetFHSPayloadBDAddress

Parent topic:

BD Address

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1gaf60a6e864796aa3de9b378454dcefd66.html language=enus -->
## TOPIC 00061: NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_UAP

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1gaf60a6e864796aa3de9b378454dcefd66.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__fhs__payload__bd__address_1gaf60a6e864796aa3de9b378454dcefd66.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 8-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the upper address part (UAP) of the device that sends the FHS packet. SyntaxNIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_UAPNumeric ValueData TypeAccessApplies To28int32Read/WriteN/ARemarks The default val

### NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_UAP

Specifies the 8-bit field in the frequency hop synchronization (FHS) packet payload. This field contains the upper address part (UAP) of the device that sends the FHS packet.

#### Syntax

NIBTSG_ATTR_FHS_PAYLOAD_BD_ADDRESS_UAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 28 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetFHSPayloadBDAddress 
 Set Function: niBTSG_SetFHSPayloadBDAddress

Parent topic:

BD Address

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput.html language=enus -->
## TOPIC 00062: High Data Throughput

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_HDT_PACKET_FORMATSpecifies the Higher Data Throughput (HDT) packet format. This property is applicable only for LE HDT packet type. NIBTSG_ATTR_HDT_PHY_INTERVALSpecifies the physical layer intervals. This property is only valid for Format1 packet for

### High Data Throughput

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_HDT_PACKET_FORMAT | Specifies the Higher Data Throughput (HDT) packet format. This property is applicable only for LE HDT packet type. |
| NIBTSG_ATTR_HDT_PHY_INTERVAL | Specifies the physical layer intervals. This property is only valid for Format1 packet format. This value is expressed in seconds. |
| NIBTSG_ATTR_PAYLOAD_CRC_SEED | Specifies the 32 bit CRC initialization seed value. This property is applicable only when user set the Packet Type to LE-HDT and NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT0 or NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1. |
| NIBTSG_ATTR_PHYSICAL_CHANNEL_ADDRESS | Specifies the 40-bit physical channel address of Higher Data Throughput (HDT) packet. |
| NIBTSG_ATTR_VHDT_MODE_ENABLED |  |
| NIBTSG_ATTR_ZADOFF_CHU_INDEX | Specifies Zadoff-Chu Index for the Long Training Sequence in the preamble. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga2b28f0d7350dba789d4d8e1b9641148b.html language=enus -->
## TOPIC 00063: NIBTSG_ATTR_PAYLOAD_CRC_SEED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga2b28f0d7350dba789d4d8e1b9641148b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga2b28f0d7350dba789d4d8e1b9641148b.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 32 bit CRC initialization seed value. This property is applicable only when user set the Packet Type to LE-HDT and NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT0 or NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1. SyntaxNIBTSG_ATTR_PAYLOAD_CRC_SEEDNumeric ValueData T

### NIBTSG_ATTR_PAYLOAD_CRC_SEED

Specifies the 32 bit CRC initialization seed value. This property is applicable only when user set the Packet Type to LE-HDT and [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT0 or NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1.

#### Syntax

NIBTSG_ATTR_PAYLOAD_CRC_SEED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 118 | int64 | Read/Write | N/A |

#### Remarks

The default value is 0x00000000. The valid values are 0x00000000 to 0xFFFFFFFF.

Get Function: niBTSG_GetPayloadCRCSeed 
 Set Function: niBTSG_SetPayloadCRCSeed

Parent topic:

High Data Throughput

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga3dc086f6a6a8098fa371a6d9a4232198.html language=enus -->
## TOPIC 00064: NIBTSG_ATTR_PHYSICAL_CHANNEL_ADDRESS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga3dc086f6a6a8098fa371a6d9a4232198.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga3dc086f6a6a8098fa371a6d9a4232198.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 40-bit physical channel address of Higher Data Throughput (HDT) packet. SyntaxNIBTSG_ATTR_PHYSICAL_CHANNEL_ADDRESSNumeric ValueData TypeAccessApplies To106int64Read/WriteN/ARemarks The default value is 0x9F15555555.Get Function: niBTSG_GetPhysicalChannelAddress Set Function: niBTSG_Set

### NIBTSG_ATTR_PHYSICAL_CHANNEL_ADDRESS

Specifies the 40-bit physical channel address of Higher Data Throughput (HDT) packet.

#### Syntax

NIBTSG_ATTR_PHYSICAL_CHANNEL_ADDRESS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 106 | int64 | Read/Write | N/A |

#### Remarks

The default value is 0x9F15555555.

Get Function: niBTSG_GetPhysicalChannelAddress 
 Set Function: niBTSG_SetPhysicalChannelAddress

Parent topic:

High Data Throughput

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga7cd346f23462a62199bbe72d6ee0289b.html language=enus -->
## TOPIC 00065: NIBTSG_ATTR_VHDT_MODE_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga7cd346f23462a62199bbe72d6ee0289b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga7cd346f23462a62199bbe72d6ee0289b.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNIBTSG_ATTR_VHDT_MODE_ENABLEDNumeric ValueData TypeAccessApplies To107int32Read/WriteN/ARemarks Get Function: niBTSG_GetVHDTModeEnabled Set Function: niBTSG_SetVHDTModeEnabled

### NIBTSG_ATTR_VHDT_MODE_ENABLED

#### Syntax

NIBTSG_ATTR_VHDT_MODE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 107 | int32 | Read/Write | N/A |

#### Remarks

Get Function: niBTSG_GetVHDTModeEnabled 
 Set Function: niBTSG_SetVHDTModeEnabled

Parent topic:

High Data Throughput

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga975ebb420df95531ce9d71c0938c8567.html language=enus -->
## TOPIC 00066: NIBTSG_ATTR_HDT_PHY_INTERVAL

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga975ebb420df95531ce9d71c0938c8567.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga975ebb420df95531ce9d71c0938c8567.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical layer intervals. This property is only valid for Format1 packet format. This value is expressed in seconds. SyntaxNIBTSG_ATTR_HDT_PHY_INTERVALNumeric ValueData TypeAccessApplies To104float64Read/WriteN/ARemarks The default value is 64us. Valid values are 64us, 128us, 192us and

### NIBTSG_ATTR_HDT_PHY_INTERVAL

Specifies the physical layer intervals. This property is only valid for Format1 packet format. This value is expressed in seconds.

#### Syntax

NIBTSG_ATTR_HDT_PHY_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 104 | float64 | Read/Write | N/A |

#### Remarks

The default value is 64us. Valid values are 64us, 128us, 192us and 256us.

Get Function: niBTSG_GetHDTPHYInterval 
 Set Function: niBTSG_SetHDTPHYInterval

Parent topic:

High Data Throughput

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga98bf0097837adf6b8392243e47dcd829.html language=enus -->
## TOPIC 00067: NIBTSG_ATTR_ZADOFF_CHU_INDEX

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga98bf0097837adf6b8392243e47dcd829.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1ga98bf0097837adf6b8392243e47dcd829.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies Zadoff-Chu Index for the Long Training Sequence in the preamble. SyntaxNIBTSG_ATTR_ZADOFF_CHU_INDEXNumeric ValueData TypeAccessApplies To105int32Read/WriteN/ARemarks The default value is 7. Valid values are in the range of [1 - 16].Get Function: niBTSG_GetZadoffChuIndex Set Function: niBTS

### NIBTSG_ATTR_ZADOFF_CHU_INDEX

Specifies Zadoff-Chu Index for the Long Training Sequence in the preamble.

#### Syntax

NIBTSG_ATTR_ZADOFF_CHU_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 105 | int32 | Read/Write | N/A |

#### Remarks

The default value is 7. Valid values are in the range of [1 - 16].

Get Function: niBTSG_GetZadoffChuIndex 
 Set Function: niBTSG_SetZadoffChuIndex

Parent topic:

High Data Throughput

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__letp__payload.html language=enus -->
## TOPIC 00068: LE-TP Payload

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__letp__payload.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__letp__payload.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_LE_TP_CORRUPT_ALTERNATE_CRCSpecifies whether the BT Generation intentionally corrupts the cyclic redundancy check (CRC) portion of every alternate packet generated. Refer to Section 6.3.7 of the Bluetooth Low Energy RF PHY Test Specification 4.0.0. C

### LE-TP Payload

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_LE_TP_CORRUPT_ALTERNATE_CRC | Specifies whether the BT Generation intentionally corrupts the cyclic redundancy check (CRC) portion of every alternate packet generated. Refer to Section 6.3.7 of the Bluetooth Low Energy RF PHY Test Specification 4.0.0. CRC corruption is done by toggling the seed used for CRC computation. |
| NIBTSG_ATTR_LE_TP_PAYLOAD_TYPE | Specifies the type of payload for the LE and LE CS packets. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__letp__payload_1ga309db08fadd1da56aa2535630271ca2b.html language=enus -->
## TOPIC 00069: NIBTSG_ATTR_LE_TP_PAYLOAD_TYPE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__letp__payload_1ga309db08fadd1da56aa2535630271ca2b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__letp__payload_1ga309db08fadd1da56aa2535630271ca2b.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of payload for the LE and LE CS packets. SyntaxNIBTSG_ATTR_LE_TP_PAYLOAD_TYPENumeric ValueData TypeAccessApplies To50int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_PRBS9.Note: This attribute is applicable for LE and LE CS packets.Get Function: niBTSG_

### NIBTSG_ATTR_LE_TP_PAYLOAD_TYPE

Specifies the type of payload for the LE and LE CS packets.

#### Syntax

NIBTSG_ATTR_LE_TP_PAYLOAD_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 50 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_PRBS9.

Note: This attribute is applicable for LE and LE CS packets.

Get Function: niBTSG_GetLETPPayloadType 
 Set Function: niBTSG_SetLETPPayloadType

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_PRBS9 | 0 (0x0) | Specifies that the payload type is PRBS9. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_11110000 | 1 (0x1) | Specifies that the payload type is 11110000. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_10101010 | 2 (0x2) | Specifies that the payload type is 10101010. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_PRBS15 | 3 (0x3) | Specifies that the payload type is PRBS15. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_11111111 | 4 (0x4) | Specifies that the payload type is 11111111. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_00000000 | 5 (0x5) | Specifies that the payload type is 00000000. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_00001111 | 6 (0x6) | Specifies that the payload type is 00001111. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_01010101 | 7 (0x7) | Specifies that the payload type is 01010101. |
| NIBTSG_VAL_LE_TP_PAYLOAD_TYPE_USER_DEFINED_BITS | 8 (0x8) | Specifies that the BT Generation uses the bit pattern that you specify in the NIBTSG_PAYLOAD_USER_DEFINED_BITS attribute. |

Parent topic:

LE-TP Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__letp__payload_1ga3622d0ee76ab2420f205f2e203da33b6.html language=enus -->
## TOPIC 00070: NIBTSG_ATTR_LE_TP_CORRUPT_ALTERNATE_CRC

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__letp__payload_1ga3622d0ee76ab2420f205f2e203da33b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__letp__payload_1ga3622d0ee76ab2420f205f2e203da33b6.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the BT Generation intentionally corrupts the cyclic redundancy check (CRC) portion of every alternate packet generated. Refer to Section 6.3.7 of the Bluetooth Low Energy RF PHY Test Specification 4.0.0. CRC corruption is done by toggling the seed used for CRC computation. SyntaxNI

### NIBTSG_ATTR_LE_TP_CORRUPT_ALTERNATE_CRC

Specifies whether the BT Generation intentionally corrupts the cyclic redundancy check (CRC) portion of every alternate packet generated. Refer to Section 6.3.7 of the Bluetooth Low Energy RF PHY Test Specification 4.0.0. CRC corruption is done by toggling the seed used for CRC computation.

#### Syntax

NIBTSG_ATTR_LE_TP_CORRUPT_ALTERNATE_CRC

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 54 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_FALSE.

Note: This attribute is applicable for LE packets.

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Disables CRC corruption of alternate LE packets. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Enables CRC corruption of alternate LE packets. Set NIBTSG_NUMBER_OF_UNIQUE_PACKETS attribute to an even number when the NIBTSG_LE_TP_CORRUPT_ALTERNATE_CRC attribute is set to NIBTSG_VAL_TRUE. |

Parent topic:

LE-TP Payload

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__packet__header.html language=enus -->
## TOPIC 00071: Packet Header

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__packet__header.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__packet__header.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_PACKET_HEADER_ARQNSpecifies the value for the automatic repeat request number (ARQN) field in the packet header. This attribute controls the value for the 1-bit acknowledgement indicator, which indicates whether the data packet transfer is successful

### Packet Header

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_PACKET_HEADER_ARQN | Specifies the value for the automatic repeat request number (ARQN) field in the packet header. This attribute controls the value for the 1-bit acknowledgement indicator, which indicates whether the data packet transfer is successful. Refer to sections 6.4.4 and 7.6, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the ARQN field. |
| NIBTSG_ATTR_PACKET_HEADER_FLOW | Specifies the value for the flow control field in the packet header. This field controls the 1-bit flow control parameter in the packet. Refer to Section 6.4.3, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the flow control field. |
| NIBTSG_ATTR_PACKET_HEADER_LT_ADDRESS | Specifies the 3-bit logical transport (LT) address of the packet. The LT address field indicates the destination slave for a packet in a master-to-slave transmission slot and indicates the source slave for a slave-to-master transmission slot. Refer to sections 6.4.1 and 6.4.2, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the LT address of a packet. |
| NIBTSG_ATTR_PACKET_HEADER_SEQN | Specifies the value for the sequential numbering scheme (SEQN) field in the packet header. This attribute controls the value for the 1-bit sequence bit, which allows you to provide a sequential numbering scheme to order the data packet scheme. Refer to sections 6.4.5, 7.6.2, and 7.6.5, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the SEQN field. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1ga74b88accffc5333060d2aa0a23d98f0c.html language=enus -->
## TOPIC 00072: NIBTSG_ATTR_PACKET_HEADER_SEQN

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1ga74b88accffc5333060d2aa0a23d98f0c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1ga74b88accffc5333060d2aa0a23d98f0c.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value for the sequential numbering scheme (SEQN) field in the packet header. This attribute controls the value for the 1-bit sequence bit, which allows you to provide a sequential numbering scheme to order the data packet scheme. Refer to sections 6.4.5, 7.6.2, and 7.6.5, Part B, Volum

### NIBTSG_ATTR_PACKET_HEADER_SEQN

Specifies the value for the sequential numbering scheme (SEQN) field in the packet header. This attribute controls the value for the 1-bit sequence bit, which allows you to provide a sequential numbering scheme to order the data packet scheme. Refer to sections 6.4.5, 7.6.2, and 7.6.5, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the SEQN field.

#### Syntax

NIBTSG_ATTR_PACKET_HEADER_SEQN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 14 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0 and 1.

Get Function: niBTSG_GetPacketHeaderSEQN 
 Set Function: niBTSG_SetPacketHeaderSEQN

Parent topic:

Packet Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gab5d08cf51dbf18b7eb561f8247af765a.html language=enus -->
## TOPIC 00073: NIBTSG_ATTR_PACKET_HEADER_FLOW

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gab5d08cf51dbf18b7eb561f8247af765a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gab5d08cf51dbf18b7eb561f8247af765a.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value for the flow control field in the packet header. This field controls the 1-bit flow control parameter in the packet. Refer to Section 6.4.3, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the flow control field. SyntaxNIBTSG_ATTR_PACKET_HEADER

### NIBTSG_ATTR_PACKET_HEADER_FLOW

Specifies the value for the flow control field in the packet header. This field controls the 1-bit flow control parameter in the packet. Refer to Section 6.4.3, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the flow control field.

#### Syntax

NIBTSG_ATTR_PACKET_HEADER_FLOW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 12 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0, which indicates a Stop condition, and 1, which indicates a Go condition.

Get Function: niBTSG_GetPacketHeaderFlow 
 Set Function: niBTSG_SetPacketHeaderFlow

Parent topic:

Packet Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gae0a5c2cee4e3939c9e15b2d7d94c3b57.html language=enus -->
## TOPIC 00074: NIBTSG_ATTR_PACKET_HEADER_ARQN

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gae0a5c2cee4e3939c9e15b2d7d94c3b57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gae0a5c2cee4e3939c9e15b2d7d94c3b57.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value for the automatic repeat request number (ARQN) field in the packet header. This attribute controls the value for the 1-bit acknowledgement indicator, which indicates whether the data packet transfer is successful. Refer to sections 6.4.4 and 7.6, Part B, Volume 2 of the Bluetooth

### NIBTSG_ATTR_PACKET_HEADER_ARQN

Specifies the value for the automatic repeat request number (ARQN) field in the packet header. This attribute controls the value for the 1-bit acknowledgement indicator, which indicates whether the data packet transfer is successful. Refer to sections 6.4.4 and 7.6, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the ARQN field.

#### Syntax

NIBTSG_ATTR_PACKET_HEADER_ARQN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 13 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_PACKET_HEADER_ARQN_NAK.

Get Function: niBTSG_GetPacketHeaderARQN 
 Set Function: niBTSG_SetPacketHeaderARQN

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_PACKET_HEADER_ARQN_NAK | 0 (0x0) | Specifies a negative acknowledgement. |
| NIBTSG_VAL_PACKET_HEADER_ARQN_ACK | 1 (0x1) | Specifies a positive acknowledgement. |

Parent topic:

Packet Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gaf797782253957d2b5dd7cd97e4dc3311.html language=enus -->
## TOPIC 00075: NIBTSG_ATTR_PACKET_HEADER_LT_ADDRESS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gaf797782253957d2b5dd7cd97e4dc3311.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__packet__header_1gaf797782253957d2b5dd7cd97e4dc3311.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 3-bit logical transport (LT) address of the packet. The LT address field indicates the destination slave for a packet in a master-to-slave transmission slot and indicates the source slave for a slave-to-master transmission slot. Refer to sections 6.4.1 and 6.4.2, Part B, Volume 2 of th

### NIBTSG_ATTR_PACKET_HEADER_LT_ADDRESS

Specifies the 3-bit logical transport (LT) address of the packet. The LT address field indicates the destination slave for a packet in a master-to-slave transmission slot and indicates the source slave for a slave-to-master transmission slot. Refer to sections 6.4.1 and 6.4.2, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the LT address of a packet.

#### Syntax

NIBTSG_ATTR_PACKET_HEADER_LT_ADDRESS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 11 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0 to 7, inclusive.

Get Function: niBTSG_GetPacketHeaderLTAddress 
 Set Function: niBTSG_SetPacketHeaderLTAddress

Parent topic:

Packet Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header.html language=enus -->
## TOPIC 00076: Payload Header

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_ACTUAL_PAYLOAD_LENGTHReturns the actual payload length, in bytes, that is calculated by the BT Generation. NIBTSG_ATTR_BLOCK_SIZESpecifies the block size of each block specified by NIBTSG_ATTR_NUMBER_OF_BLOCKS.This property is valid only for the LE-H

### Payload Header

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_ACTUAL_PAYLOAD_LENGTH | Returns the actual payload length, in bytes, that is calculated by the BT Generation. |
| NIBTSG_ATTR_BLOCK_SIZE | Specifies the block size of each block specified by NIBTSG_ATTR_NUMBER_OF_BLOCKS.This property is valid only for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED. |
| NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE | Specifies the payload zone configuration mode for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED. |
| NIBTSG_ATTR_LAST_BLOCK_SIZE | Specifies the block size of the last block. This property is valid only for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED. |
| NIBTSG_ATTR_NUMBER_OF_BLOCKS | Specifies the number of blocks minus one that the payload is split into.This property is valid only for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED. |
| NIBTSG_ATTR_NUMBER_OF_PAYLOADS | Specifies the number of payloads for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1. The valid values are 1 to 4. |
| NIBTSG_ATTR_PAYLOAD_DATA_TYPE | Specifies the type of payload for the packet. |
| NIBTSG_ATTR_PAYLOAD_HEADER_ENABLED | Specifies whether to enable payload header in the Bluetooth packet to be generated. This is applicable only for LE packets. |
| NIBTSG_ATTR_PAYLOAD_HEADER_FLOW | Specifies the value for the flow control bit in the payload header. This field controls the 1-bit flow control parameter in the packet. |
| NIBTSG_ATTR_PAYLOAD_HEADER_LLID | Specifies whether the payload is the start or continuation fragment of a logical link control and adaptation protocol (L2CAP) or link management protocol (LMP) message. |
| NIBTSG_ATTR_PAYLOAD_LENGTH | Specifies the payload length, in bytes. If the length exceeds the maximum permissible length mentioned in the Bluetooth specification, the BT Generation uses this maximum permissible length as the payload length. For LE-TP-EXT and LE-Enhanced packet types, typical LE packet is generated length up to 255 bytes, and Hyper Length LE packet is generated for length from 256 bytes to 8191 bytes. |
| NIBTSG_ATTR_PAYLOAD_LENGTH_MODE | Specifies whether the BT Generation automatically sets the value of the LENGTH field in the payload header to the maximum permissible length or whether it uses the value that you specify in the NIBTSG_ATTR_PAYLOAD_LENGTH attribute. |
| NIBTSG_ATTR_PAYLOAD_ZONE_LENGTH | Returns the payload zone length of LE-HDT packets. The payload zone length has all payloads and each payload contains blocks followed by CRCs. |
| NIBTSG_ATTR_TXBLOCK_MAP | Specifies the TxBlockMap field of Tx Portion of PDU Header. The TxBlockMap field is 8 or 16 bits depending on the value of NIBTSG_ATTR_TXLEN_SEQUENCE_NUMBER. It indicates which blocks are actually being transmitted in the packet, with bit b set to 1 if block b (counting from 0) is included and 0 if it is not. At least one bit shall be set. |
| NIBTSG_ATTR_TXLEN_SEQUENCE_NUMBER | Specifies the value of TxLen SN field of Tx Portion of PDU Header. This property is valid only for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga0c9e0f511f3dd2ec78cc85888903dfc8.html language=enus -->
## TOPIC 00077: NIBTSG_ATTR_PAYLOAD_LENGTH_MODE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga0c9e0f511f3dd2ec78cc85888903dfc8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga0c9e0f511f3dd2ec78cc85888903dfc8.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the BT Generation automatically sets the value of the LENGTH field in the payload header to the maximum permissible length or whether it uses the value that you specify in the NIBTSG_ATTR_PAYLOAD_LENGTH attribute. SyntaxNIBTSG_ATTR_PAYLOAD_LENGTH_MODENumeric ValueData TypeAccessApp

### NIBTSG_ATTR_PAYLOAD_LENGTH_MODE

Specifies whether the BT Generation automatically sets the value of the LENGTH field in the payload header to the maximum permissible length or whether it uses the value that you specify in the [NIBTSG_ATTR_PAYLOAD_LENGTH](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac594a7c9db5c6df4c4028d0361cf592f.html) attribute.

#### Syntax

NIBTSG_ATTR_PAYLOAD_LENGTH_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 43 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_PAYLOAD_LENGTH_MODE_MAXIMUM_LENGTH.

Get Function: niBTSG_GetPayloadLengthMode 
 Set Function: niBTSG_SetPayloadLengthMode

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_PAYLOAD_LENGTH_MODE_MAXIMUM_LENGTH | 0 (0x0) | Specifies that the BT Generation sets the length to the maximum permissible payload length. |
| NIBTSG_VAL_PAYLOAD_LENGTH_MODE_USER_DEFINED | 1 (0x1) | Specifies that the BT Generation sets the length to the value that you specify in the NIBTSG_PAYLOAD_LENGTH attribute. |

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga14f146d6fb6c0d297ac21edbf76f2c67.html language=enus -->
## TOPIC 00078: NIBTSG_ATTR_PAYLOAD_HEADER_LLID

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga14f146d6fb6c0d297ac21edbf76f2c67.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga14f146d6fb6c0d297ac21edbf76f2c67.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the payload is the start or continuation fragment of a logical link control and adaptation protocol (L2CAP) or link management protocol (LMP) message. SyntaxNIBTSG_ATTR_PAYLOAD_HEADER_LLIDNumeric ValueData TypeAccessApplies To15int32Read/WriteN/ARemarks You must use "payload x" as

### NIBTSG_ATTR_PAYLOAD_HEADER_LLID

Specifies whether the payload is the start or continuation fragment of a logical link control and adaptation protocol (L2CAP) or link management protocol (LMP) message.

#### Syntax

NIBTSG_ATTR_PAYLOAD_HEADER_LLID

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 15 | int32 | Read/Write | N/A |

#### Remarks

You must use "payload x" as the active channel string to configure this property for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and [NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html) is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED.

The default value is 0. Valid values are 0, 1, 2, and 3.

Get Function: niBTSG_GetPayloadHeaderLLID 
 Set Function: niBTSG_SetPayloadHeaderLLID

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga36e65c4799f3db40d26afca082bf72dd.html language=enus -->
## TOPIC 00079: NIBTSG_ATTR_TXLEN_SEQUENCE_NUMBER

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga36e65c4799f3db40d26afca082bf72dd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga36e65c4799f3db40d26afca082bf72dd.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of TxLen SN field of Tx Portion of PDU Header. This property is valid only for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CON

### NIBTSG_ATTR_TXLEN_SEQUENCE_NUMBER

Specifies the value of TxLen SN field of Tx Portion of PDU Header. This property is valid only for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and [NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html) is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED.

#### Syntax

NIBTSG_ATTR_TXLEN_SEQUENCE_NUMBER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 111 | int32 | Read/Write | N/A |

#### Remarks

You must use "payload x" as the active channel string to configure this property.

The default value is NIBTSG_VAL_TXLEN_SEQUENCE_NUMBER_11.

Get Function: niBTSG_GetTxLenSequenceNumber 
 Set Function: niBTSG_SetTxLenSequenceNumber

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_TXLEN_SEQUENCE_NUMBER_00 | 0 (0x0) | Specifies that the packet does not include a payload or any of its blocks. |
| NIBTSG_VAL_TXLEN_SEQUENCE_NUMBER_01 | 1 (0x1) | Specifies that the payload has 1 block and the Payload Length is NIBTSG_ATTR_LAST_BLOCK_SIZE. |
| NIBTSG_VAL_TXLEN_SEQUENCE_NUMBER_10 | 2 (0x2) | Specifies that the payload can have maximum 8 blocks and only bits 0 to 7 of NIBTSG_ATTR_TXBLOCK_MAP are explicit; bits 8 to 15 are always zero. |
| NIBTSG_VAL_TXLEN_SEQUENCE_NUMBER_11 | 3 (0x3) | Specifies that the payload can have maximum 16 blocks. |

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga4ca93061b3979245c1809d3d3515a0cc.html language=enus -->
## TOPIC 00080: NIBTSG_ATTR_TXBLOCK_MAP

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga4ca93061b3979245c1809d3d3515a0cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga4ca93061b3979245c1809d3d3515a0cc.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the TxBlockMap field of Tx Portion of PDU Header. The TxBlockMap field is 8 or 16 bits depending on the value of NIBTSG_ATTR_TXLEN_SEQUENCE_NUMBER. It indicates which blocks are actually being transmitted in the packet, with bit b set to 1 if block b (counting from 0) is included and 0 if

### NIBTSG_ATTR_TXBLOCK_MAP

Specifies the TxBlockMap field of Tx Portion of PDU Header. The TxBlockMap field is 8 or 16 bits depending on the value of [NIBTSG_ATTR_TXLEN_SEQUENCE_NUMBER](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga36e65c4799f3db40d26afca082bf72dd.html). It indicates which blocks are actually being transmitted in the packet, with bit b set to 1 if block b (counting from 0) is included and 0 if it is not. At least one bit shall be set.

#### Syntax

NIBTSG_ATTR_TXBLOCK_MAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 115 | int32 | Read/Write | N/A |

#### Remarks

This property is valid only for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and [NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html) is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED.

You must use "payload x" as the active channel string to configure this property.

The valid values are 1 to 0xFFFF. The default value is 0xFFFF.

Get Function: niBTSG_GetTxBlockMap 
 Set Function: niBTSG_SetTxBlockMap

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga6dbd4921cc01a75f2010132032bb7e4d.html language=enus -->
## TOPIC 00081: NIBTSG_ATTR_NUMBER_OF_PAYLOADS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga6dbd4921cc01a75f2010132032bb7e4d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga6dbd4921cc01a75f2010132032bb7e4d.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of payloads for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1. The valid values are 1 to 4. SyntaxNIBTSG_ATTR_NUMBER_OF_PAYLOADSNumeric ValueData TypeAccessApplies To109int32Read/WriteN/ARemarks The default value is 1.Get Fun

### NIBTSG_ATTR_NUMBER_OF_PAYLOADS

Specifies the number of payloads for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1. The valid values are 1 to 4.

#### Syntax

NIBTSG_ATTR_NUMBER_OF_PAYLOADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 109 | int32 | Read/Write | N/A |

#### Remarks

The default value is 1.

Get Function: niBTSG_GetNumberOfPayloads 
 Set Function: niBTSG_SetNumberOfPayloads

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga8d73458e5dfc6f72ca780ddae69d6307.html language=enus -->
## TOPIC 00082: NIBTSG_ATTR_PAYLOAD_ZONE_LENGTH

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga8d73458e5dfc6f72ca780ddae69d6307.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga8d73458e5dfc6f72ca780ddae69d6307.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the payload zone length of LE-HDT packets. The payload zone length has all payloads and each payload contains blocks followed by CRCs. SyntaxNIBTSG_ATTR_PAYLOAD_ZONE_LENGTHNumeric ValueData TypeAccessApplies To117int32Read/WriteN/ARemarks This property is valid only for the LE-HDT packet.Get

### NIBTSG_ATTR_PAYLOAD_ZONE_LENGTH

Returns the payload zone length of LE-HDT packets. The payload zone length has all payloads and each payload contains blocks followed by CRCs.

#### Syntax

NIBTSG_ATTR_PAYLOAD_ZONE_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 117 | int32 | Read/Write | N/A |

#### Remarks

This property is valid only for the LE-HDT packet.

Get Function: niBTSG_GetPayloadZoneLength 
 Set Function: niBTSG_SetPayloadZoneLength

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga98470caf9dc2526e2d115963627db74e.html language=enus -->
## TOPIC 00083: NIBTSG_ATTR_NUMBER_OF_BLOCKS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga98470caf9dc2526e2d115963627db74e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga98470caf9dc2526e2d115963627db74e.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of blocks minus one that the payload is split into.This property is valid only for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZON

### NIBTSG_ATTR_NUMBER_OF_BLOCKS

Specifies the number of blocks minus one that the payload is split into.This property is valid only for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and [NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html) is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED.

#### Syntax

NIBTSG_ATTR_NUMBER_OF_BLOCKS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 112 | int32 | Read/Write | N/A |

#### Remarks

You must use "payload x" as the active channel string to configure this property.

The default value is 15.

Get Function: niBTSG_GetNumberOfBlocks 
 Set Function: niBTSG_SetNumberOfBlocks

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga984f65eaffbfeb631e722553e0ee9055.html language=enus -->
## TOPIC 00084: NIBTSG_ATTR_PAYLOAD_HEADER_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga984f65eaffbfeb631e722553e0ee9055.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga984f65eaffbfeb631e722553e0ee9055.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable payload header in the Bluetooth packet to be generated. This is applicable only for LE packets. SyntaxNIBTSG_ATTR_PAYLOAD_HEADER_ENABLEDNumeric ValueData TypeAccessApplies To66int32Read/WriteN/ARemarks For generating custom Bluetooth packets, set the value of this propert

### NIBTSG_ATTR_PAYLOAD_HEADER_ENABLED

Specifies whether to enable payload header in the Bluetooth packet to be generated. This is applicable only for LE packets.

#### Syntax

NIBTSG_ATTR_PAYLOAD_HEADER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 66 | int32 | Read/Write | N/A |

#### Remarks

For generating custom Bluetooth packets, set the value of this property to NIBTSG_VAL_FALSE. In this case, the header bits can be given as input to the [NIBTSG_ATTR_PAYLOAD_USER_DEFINED_BITS](group____root__ni_b_t_generation__attributes__packet__settings__user__header_1ga5fc7a9e951a1ddaa6b98bde46c5704a3.html) property along with the payload bits. The default value is NIBTSG_VAL_TRUE.

Get Function: niBTSG_SetPayloadHeaderEnabled 
 Set Function: niBTSG_SetPayloadHeaderEnabled

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Specifies that the header is disabled in the generated Bluetooth packet. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Specifies that the header is enabled in the generated Bluetooth packet. |

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga9d852f50a7b7c63fb129b8776e8c8655.html language=enus -->
## TOPIC 00085: NIBTSG_ATTR_PAYLOAD_DATA_TYPE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga9d852f50a7b7c63fb129b8776e8c8655.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga9d852f50a7b7c63fb129b8776e8c8655.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of payload for the packet. SyntaxNIBTSG_ATTR_PAYLOAD_DATA_TYPENumeric ValueData TypeAccessApplies To18int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE.Get Function: niBTSG_GetPayloadDataType Set Function: niBTSG_SetPayloadDataTypeNameValueDes

### NIBTSG_ATTR_PAYLOAD_DATA_TYPE

Specifies the type of payload for the packet.

#### Syntax

NIBTSG_ATTR_PAYLOAD_DATA_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 18 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE.

Get Function: niBTSG_GetPayloadDataType 
 Set Function: niBTSG_SetPayloadDataType

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE | 0 (0x0) | Specifies that the BT Generation uses a Galois pseudonoise (PN) bit sequence with a payload order and seed, which you specify in the NIBTSG_PAYLOAD_PN_ORDER and NIBTSG_PAYLOAD_PN_SEED attributes respectively, to create the payload for generation. |
| NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS | 1 (0x1) | Specifies that the BT Generation repeats the bit pattern, which you specify in the NIBTSG_PAYLOAD_USER_DEFINED_BITS attribute, to achieve the necessary payload length. |

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html language=enus -->
## TOPIC 00086: NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the payload zone configuration mode for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED. SyntaxNIBTSG_ATTR_F

### NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE

Specifies the payload zone configuration mode for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and [NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html) is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED.

#### Syntax

NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 110 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_AUTO.

Get Function: niBTSG_GetFormat1PayloadZoneConfigurationMode 
 Set Function: niBTSG_SetFormat1PayloadZoneConfigurationMode

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_AUTO | 0 (0x0) | Specifies that the payload zone length is computed based the NIBTSG_ATTR_PAYLOAD_LENGTH_MODE and NIBTSG_ATTR_PAYLOAD_LENGTH. When NIBTSG_ATTR_PAYLOAD_LENGTH_MODE property is set to NIBTSG_VAL_PAYLOAD_LENGTH_MODE_MAXIMUM_LENGTH, the maximum payload length is used for the specified number of payloads. When NIBTSG_ATTR_PAYLOAD_LENGTH_MODE property is set to NIBTSG_VAL_PAYLOAD_LENGTH_MODE_USER_DEFINED, user configured payload length is used for specified NIBTSG_ATTR_NUMBER_OF_PAYLOADS. In this mode, the block size, number of blocks, last block size and TxBlockMap are computed instead of being entered by the user. |
| NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED | 1 (0x1) | Specifies that the payload zone length is configured using the channel specific properties such as NIBTSG_ATTR_NUMBER_OF_BLOCKS, NIBTSG_ATTR_BLOCK_SIZE, NIBTSG_ATTR_LAST_BLOCK_SIZE, NIBTSG_ATTR_TXBLOCK_MAP. |

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac594a7c9db5c6df4c4028d0361cf592f.html language=enus -->
## TOPIC 00087: NIBTSG_ATTR_PAYLOAD_LENGTH

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac594a7c9db5c6df4c4028d0361cf592f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac594a7c9db5c6df4c4028d0361cf592f.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the payload length, in bytes. If the length exceeds the maximum permissible length mentioned in the Bluetooth specification, the BT Generation uses this maximum permissible length as the payload length. For LE-TP-EXT and LE-Enhanced packet types, typical LE packet is generated length up to

### NIBTSG_ATTR_PAYLOAD_LENGTH

Specifies the payload length, in bytes. If the length exceeds the maximum permissible length mentioned in the Bluetooth specification, the BT Generation uses this maximum permissible length as the payload length. For LE-TP-EXT and LE-Enhanced packet types, typical LE packet is generated length up to 255 bytes, and Hyper Length LE packet is generated for length from 256 bytes to 8191 bytes.

#### Syntax

NIBTSG_ATTR_PAYLOAD_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 17 | int32 | Read/Write | N/A |

#### Remarks

For LE HDT packet, Format0 supports payload length up to 510 bytes, whereas Format1 supports up to 8191 bytes per payload. In the case of LE HDT Format1, when the Payload Zone Configuration Mode is set to Auto and the Payload Length Mode is set to User Defined, you must specify "payload x" as the active channel string to configure this property.

The default value is 0.

Get Function: niBTSG_GetPayloadLength 
 Set Function: niBTSG_SetPayloadLength

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac8d65844f7046126e61f6bab6f114918.html language=enus -->
## TOPIC 00088: NIBTSG_ATTR_PAYLOAD_HEADER_FLOW

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac8d65844f7046126e61f6bab6f114918.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac8d65844f7046126e61f6bab6f114918.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value for the flow control bit in the payload header. This field controls the 1-bit flow control parameter in the packet. SyntaxNIBTSG_ATTR_PAYLOAD_HEADER_FLOWNumeric ValueData TypeAccessApplies To16int32Read/WriteN/ARemarks The default value is 0. Valid values are 0, which indicates a

### NIBTSG_ATTR_PAYLOAD_HEADER_FLOW

Specifies the value for the flow control bit in the payload header. This field controls the 1-bit flow control parameter in the packet.

#### Syntax

NIBTSG_ATTR_PAYLOAD_HEADER_FLOW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 16 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. Valid values are 0, which indicates a Stop condition, and 1, which indicates a Go condition.

Get Function: niBTSG_GetPayloadHeaderFlow 
 Set Function: niBTSG_SetPayloadHeaderFlow

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gadb0e87dc9c58030e2111a3e54b95e653.html language=enus -->
## TOPIC 00089: NIBTSG_ATTR_BLOCK_SIZE

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gadb0e87dc9c58030e2111a3e54b95e653.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gadb0e87dc9c58030e2111a3e54b95e653.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the block size of each block specified by NIBTSG_ATTR_NUMBER_OF_BLOCKS.This property is valid only for the LE-HDT packet when NIBTSG_ATTR_HDT_PACKET_FORMAT is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE is set to NIBTSG_VAL_FORMAT1_PA

### NIBTSG_ATTR_BLOCK_SIZE

Specifies the block size of each block specified by NIBTSG_ATTR_NUMBER_OF_BLOCKS.This property is valid only for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and [NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html) is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED.

#### Syntax

NIBTSG_ATTR_BLOCK_SIZE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 113 | int32 | Read/Write | N/A |

#### Remarks

You must use "payload x" as the active channel string to configure this property.

The valid values are 32 to 511. The default value is 511.

Get Function: niBTSG_GetBlockSize 
 Set Function: niBTSG_SetBlockSize

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gafcadfe6cd02c95655be5ec9273107445.html language=enus -->
## TOPIC 00090: NIBTSG_ATTR_ACTUAL_PAYLOAD_LENGTH

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gafcadfe6cd02c95655be5ec9273107445.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gafcadfe6cd02c95655be5ec9273107445.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual payload length, in bytes, that is calculated by the BT Generation. SyntaxNIBTSG_ATTR_ACTUAL_PAYLOAD_LENGTHNumeric ValueData TypeAccessApplies To44int32Read/WriteN/ARemarks If you set the NIBTSG_ATTR_PAYLOAD_LENGTH_MODE attribute to NIBTSG_VAL_PAYLOAD_LENGTH_MODE_MAXIMUM_LENGTH, th

### NIBTSG_ATTR_ACTUAL_PAYLOAD_LENGTH

Returns the actual payload length, in bytes, that is calculated by the BT Generation.

#### Syntax

NIBTSG_ATTR_ACTUAL_PAYLOAD_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 44 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIBTSG_ATTR_PAYLOAD_LENGTH_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga0c9e0f511f3dd2ec78cc85888903dfc8.html) attribute to NIBTSG_VAL_PAYLOAD_LENGTH_MODE_MAXIMUM_LENGTH, the BT Generation returns the maximum permissible payload data length as specified in the Bluetooth specifications. If you set the [NIBTSG_ATTR_PAYLOAD_LENGTH_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga0c9e0f511f3dd2ec78cc85888903dfc8.html) attribute to NIBTSG_VAL_PAYLOAD_LENGTH_MODE_USER_DEFINED, the BT Generation returns the value that you specify in the [NIBTSG_ATTR_PAYLOAD_LENGTH](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac594a7c9db5c6df4c4028d0361cf592f.html) attribute. If the value that you specify in the [NIBTSG_ATTR_PAYLOAD_LENGTH](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gac594a7c9db5c6df4c4028d0361cf592f.html) attribute exceeds the maximum permissible payload length for the packet, the BT Generation returns this maximum permissible payload length.

For LE-HDT Packets when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1 and [NIBTSG_ATTR_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gab3a48d37c8bced4c8fd802619c45a61e.html) is set to NIBTSG_VAL_FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE_USER_DEFINED, the Actual Payload Length is computed as Payload length = (Nb * [NIBTSG_ATTR_BLOCK_SIZE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gadb0e87dc9c58030e2111a3e54b95e653.html)) + [NIBTSG_ATTR_LAST_BLOCK_SIZE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1gaeca5f65b6cb1a181cde2c6a276bcd0dc.html) for each payload. Here Nb is number of transmitted blocks depends on the [NIBTSG_ATTR_TXBLOCK_MAP](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga4ca93061b3979245c1809d3d3515a0cc.html) attribute.

You must use "payload x" as the active channel string to configure this property for the LE-HDT packet when [NIBTSG_ATTR_HDT_PACKET_FORMAT](group____root__ni_b_t_generation__attributes__packet__settings__high__data__throughput_1gad26560732e099c9ed7d528d4b62cf5a3.html) is set to NIBTSG_VAL_HDT_PACKET_FORMAT_FORMAT1.

Get Function: niBTSG_GetActualPayloadLength

Parent topic:

Payload Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__user__header.html language=enus -->
## TOPIC 00091: User Header

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__user__header.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__user__header.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_PAYLOAD_PN_ORDERSpecifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_A

### User Header

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_PAYLOAD_PN_ORDER | Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_PAYLOAD_PN_ORDER attribute. |
| NIBTSG_ATTR_PAYLOAD_PN_SEED | Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_PAYLOAD_PN_SEED attribute. |
| NIBTSG_ATTR_PAYLOAD_USER_DEFINED_BITS | Specifies a bit pattern as an array of zeros and ones. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__user__header_1ga5fc7a9e951a1ddaa6b98bde46c5704a3.html language=enus -->
## TOPIC 00092: NIBTSG_ATTR_PAYLOAD_USER_DEFINED_BITS

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__user__header_1ga5fc7a9e951a1ddaa6b98bde46c5704a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__user__header_1ga5fc7a9e951a1ddaa6b98bde46c5704a3.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a bit pattern as an array of zeros and ones. SyntaxNIBTSG_ATTR_PAYLOAD_USER_DEFINED_BITSNumeric ValueData TypeAccessApplies To20int32 []Read/WriteN/ARemarks If the array length is greater than the required payload length, the BT Generation uses a subset of the required length from the begi

### NIBTSG_ATTR_PAYLOAD_USER_DEFINED_BITS

Specifies a bit pattern as an array of zeros and ones.

#### Syntax

NIBTSG_ATTR_PAYLOAD_USER_DEFINED_BITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 20 | int32 [] | Read/Write | N/A |

#### Remarks

If the array length is greater than the required payload length, the BT Generation uses a subset of the required length from the beginning of the array for waveform generation. If the array length is less than the required payload length, the BT Generation repeats the bit pattern until the required length is achieved. If you set the [NIBTSG_ATTR_PAYLOAD_DATA_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga9d852f50a7b7c63fb129b8776e8c8655.html) attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_PN_SEQUENCE, the BT Generation ignores the [NIBTSG_ATTR_PAYLOAD_USER_DEFINED_BITS](group____root__ni_b_t_generation__attributes__packet__settings__user__header_1ga5fc7a9e951a1ddaa6b98bde46c5704a3.html) attribute.

Get Function: niBTSG_GetPayloadUserDefinedBits 
 Set Function: niBTSG_SetPayloadUserDefinedBits

Parent topic:

User Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gaa27256951075d00fdf744fa20d6168d6.html language=enus -->
## TOPIC 00093: NIBTSG_ATTR_PAYLOAD_PN_ORDER

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gaa27256951075d00fdf744fa20d6168d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gaa27256951075d00fdf744fa20d6168d6.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_PAYLOAD_PN_ORDER attribute. SyntaxNIBTSG_ATTR_PAYLOAD_PN_ORDER

### NIBTSG_ATTR_PAYLOAD_PN_ORDER

Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. If you set the [NIBTSG_ATTR_PAYLOAD_DATA_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga9d852f50a7b7c63fb129b8776e8c8655.html) attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the [NIBTSG_ATTR_PAYLOAD_PN_ORDER](group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gaa27256951075d00fdf744fa20d6168d6.html) attribute.

#### Syntax

NIBTSG_ATTR_PAYLOAD_PN_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 41 | int32 | Read/Write | N/A |

#### Remarks

The default value is 9. Valid values are 5 to 31, inclusive.

Get Function: niBTSG_GetPayloadPNOrder 
 Set Function: niBTSG_SetPayloadPNOrder

Parent topic:

User Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gabc7bf5e5a3444b39c08a66822dd874b5.html language=enus -->
## TOPIC 00094: NIBTSG_ATTR_PAYLOAD_PN_SEED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gabc7bf5e5a3444b39c08a66822dd874b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gabc7bf5e5a3444b39c08a66822dd874b5.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the NIBTSG_ATTR_PAYLOAD_DATA_TYPE attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the NIBTSG_ATTR_PAYLOAD_PN_SEED attribute. SyntaxNIBTSG_ATTR_PAYLOAD_PN_SEEDN

### NIBTSG_ATTR_PAYLOAD_PN_SEED

Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the [NIBTSG_ATTR_PAYLOAD_DATA_TYPE](group____root__ni_b_t_generation__attributes__packet__settings__payload__header_1ga9d852f50a7b7c63fb129b8776e8c8655.html) attribute to NIBTSG_VAL_PAYLOAD_DATA_TYPE_USER_DEFINED_BITS, the BT Generation ignores the [NIBTSG_ATTR_PAYLOAD_PN_SEED](group____root__ni_b_t_generation__attributes__packet__settings__user__header_1gabc7bf5e5a3444b39c08a66822dd874b5.html) attribute.

#### Syntax

NIBTSG_ATTR_PAYLOAD_PN_SEED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 42 | int32 | Read/Write | N/A |

#### Remarks

The default value is 497.

Get Function: niBTSG_GetPayloadPNSeed 
 Set Function: niBTSG_SetPayloadPNSeed

Parent topic:

User Header

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings.html language=enus -->
## TOPIC 00095: Whitening Settings

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_WHITENING_CLOCKSpecifies the 28-bit master Bluetooth device clock. This attribute is applicable only to BR and EDR packets. The BT Generation uses this attribute to initialize the linear feedback shift register used for calculating the whitening word

### Whitening Settings

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_WHITENING_CLOCK | Specifies the 28-bit master Bluetooth device clock. This attribute is applicable only to BR and EDR packets. The BT Generation uses this attribute to initialize the linear feedback shift register used for calculating the whitening word. The BT Generation uses bits 1 to 6 for this purpose. Refer to sections 1.1 and 7.2, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the Bluetooth device clock. |
| NIBTSG_ATTR_WHITENING_ENABLED | Specifies whether to enable the whitening settings. |

#### Attachments

None

Parent topic:

Packet Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings_1ga19b307d4049a43ec60ef63d564d52b2c.html language=enus -->
## TOPIC 00096: NIBTSG_ATTR_WHITENING_CLOCK

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings_1ga19b307d4049a43ec60ef63d564d52b2c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings_1ga19b307d4049a43ec60ef63d564d52b2c.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 28-bit master Bluetooth device clock. This attribute is applicable only to BR and EDR packets. The BT Generation uses this attribute to initialize the linear feedback shift register used for calculating the whitening word. The BT Generation uses bits 1 to 6 for this purpose. Refer to s

### NIBTSG_ATTR_WHITENING_CLOCK

Specifies the 28-bit master Bluetooth device clock. This attribute is applicable only to BR and EDR packets. The BT Generation uses this attribute to initialize the linear feedback shift register used for calculating the whitening word. The BT Generation uses bits 1 to 6 for this purpose. Refer to sections 1.1 and 7.2, Part B, Volume 2 of the Bluetooth Specification v2.1+EDR for more information about the Bluetooth device clock.

#### Syntax

NIBTSG_ATTR_WHITENING_CLOCK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 32 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

Get Function: niBTSG_GetWhiteningClock 
 Set Function: niBTSG_SetWhiteningClock

Parent topic:

Whitening Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings_1gaf9616cc4f9d13ecd3c4914edf3e4a095.html language=enus -->
## TOPIC 00097: NIBTSG_ATTR_WHITENING_ENABLED

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings_1gaf9616cc4f9d13ecd3c4914edf3e4a095.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__packet__settings__whitening__settings_1gaf9616cc4f9d13ecd3c4914edf3e4a095.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the whitening settings. SyntaxNIBTSG_ATTR_WHITENING_ENABLEDNumeric ValueData TypeAccessApplies To31int32Read/WriteN/ARemarks The default value is NIBTSG_VAL_FALSE.If you set this attribute to NIBTSG_VAL_TRUE and the NIBTSG_ATTR_PACKET_TYPE attribute to any LE packets, you

### NIBTSG_ATTR_WHITENING_ENABLED

Specifies whether to enable the whitening settings.

#### Syntax

NIBTSG_ATTR_WHITENING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 31 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIBTSG_VAL_FALSE.

If you set this attribute to NIBTSG_VAL_TRUE and the [NIBTSG_ATTR_PACKET_TYPE](group____root__ni_b_t_generation__attributes__packet__settings_1gae23e33e3a7ed97a782c08c01619cb9b5.html) attribute to any LE packets, you should set a value for the [NIBTSG_ATTR_CARRIER_FREQUENCY](group____root__ni_b_t_generation__attributes_1gac799f323e42f189786626e4fc6a085c9.html) attribute.

Get Function: niBTSG_GetWhiteningEnabled 
 Set Function: niBTSG_SetWhiteningEnabled

| Name | Value | Description |
| --- | --- | --- |
| NIBTSG_VAL_FALSE | 0 (0x0) | Disables whitening. |
| NIBTSG_VAL_TRUE | 1 (0x1) | Enables whitening. |

Parent topic:

Whitening Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__power__ramp__settings.html language=enus -->
## TOPIC 00098: Power Ramp Settings

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__power__ramp__settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__power__ramp__settings.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_POWER_RAMP_SETTLING_TIMESpecifies the settling time of the burst. The settling time is the time interval from the time when output power is 40 dB less than the final output power to the time when the output power is ±1 dB of the final output power. T

### Power Ramp Settings

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_POWER_RAMP_SETTLING_TIME | Specifies the settling time of the burst. The settling time is the time interval from the time when output power is 40 dB less than the final output power to the time when the output power is ±1 dB of the final output power. This value is expressed in seconds. |
| NIBTSG_ATTR_POWER_RAMP_TIME | Specifies the ramp time of the burst. The settling time is the time interval from the time when output power (X dBm) is 40 dB less than the final output power to the time when the output power is ±1 dB of the final output power. This value is expressed in seconds. The default value is 2 microseconds. Valid values are from 1 microseconds to 10 microseconds, inclusive. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__power__ramp__settings_1ga75349890320cc0549c9d52dab8f1cbdd.html language=enus -->
## TOPIC 00099: NIBTSG_ATTR_POWER_RAMP_TIME

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__power__ramp__settings_1ga75349890320cc0549c9d52dab8f1cbdd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__power__ramp__settings_1ga75349890320cc0549c9d52dab8f1cbdd.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ramp time of the burst. The settling time is the time interval from the time when output power (X dBm) is 40 dB less than the final output power to the time when the output power is ±1 dB of the final output power. This value is expressed in seconds. The default value is 2 microseconds

### NIBTSG_ATTR_POWER_RAMP_TIME

Specifies the ramp time of the burst. The settling time is the time interval from the time when output power (X dBm) is 40 dB less than the final output power to the time when the output power is ±1 dB of the final output power. This value is expressed in seconds. The default value is 2 microseconds. Valid values are from 1 microseconds to 10 microseconds, inclusive.

#### Syntax

NIBTSG_ATTR_POWER_RAMP_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 72 | float64 | Read/Write | N/A |

#### Remarks

Note: The value of ramp time should not exceed the value of settling time.

Get Function: niBTSG_GetPowerRampTime 
 Set Function: niBTSG_SetPowerRampTime

Parent topic:

Power Ramp Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__power__ramp__settings_1gaf6f015cfbc3c2fe4f8ef9d2628738317.html language=enus -->
## TOPIC 00100: NIBTSG_ATTR_POWER_RAMP_SETTLING_TIME

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__power__ramp__settings_1gaf6f015cfbc3c2fe4f8ef9d2628738317.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__power__ramp__settings_1gaf6f015cfbc3c2fe4f8ef9d2628738317.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the settling time of the burst. The settling time is the time interval from the time when output power is 40 dB less than the final output power to the time when the output power is ±1 dB of the final output power. This value is expressed in seconds. SyntaxNIBTSG_ATTR_POWER_RAMP_SETTLING_T

### NIBTSG_ATTR_POWER_RAMP_SETTLING_TIME

Specifies the settling time of the burst. The settling time is the time interval from the time when output power is 40 dB less than the final output power to the time when the output power is ±1 dB of the final output power. This value is expressed in seconds.

#### Syntax

NIBTSG_ATTR_POWER_RAMP_SETTLING_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 71 | float64 | Read/Write | N/A |

#### Remarks

The default value is 4 microseconds. Valid values are from 1 microseconds to 20 microseconds, inclusive.

Get Function: niBTSG_GetPowerRampSettlingTime 
 Set Function: niBTSG_SetPowerRampSettlingTime

Parent topic:

Power Ramp Settings

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__run__time__scaling.html language=enus -->
## TOPIC 00101: Run Time Scaling

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__run__time__scaling.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__run__time__scaling.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_RUN_TIME_SCALINGGet Function: niBTSG_GetRunTimeScaling AttachmentsNone

### Run Time Scaling

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_RUN_TIME_SCALING | Get Function: niBTSG_GetRunTimeScaling |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__run__time__scaling_1ga25da46fba7564e461474af55decd93b3.html language=enus -->
## TOPIC 00102: NIBTSG_ATTR_RUN_TIME_SCALING

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__run__time__scaling_1ga25da46fba7564e461474af55decd93b3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__run__time__scaling_1ga25da46fba7564e461474af55decd93b3.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Function: niBTSG_GetRunTimeScaling SyntaxNIBTSG_ATTR_RUN_TIME_SCALINGNumeric ValueData TypeAccessApplies To79float64Read/WriteN/ARemarks Set Function: niBTSG_SetRunTimeScaling

### NIBTSG_ATTR_RUN_TIME_SCALING

Get Function: niBTSG_GetRunTimeScaling

#### Syntax

NIBTSG_ATTR_RUN_TIME_SCALING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 79 | float64 | Read/Write | N/A |

#### Remarks

Set Function: niBTSG_SetRunTimeScaling

Parent topic:

Run Time Scaling

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__waveform__file__version.html language=enus -->
## TOPIC 00103: Waveform File Version

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__waveform__file__version.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__waveform__file__version.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIBTSG_ATTR_WAVEFORM_FILE_VERSIONGet Function: niBTSG_GetWaveformFileVersion AttachmentsNone

### Waveform File Version

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIBTSG_ATTR_WAVEFORM_FILE_VERSION | Get Function: niBTSG_GetWaveformFileVersion |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__attributes__waveform__file__version_1gaa67b8a6d1284a128f3e701cd873700db.html language=enus -->
## TOPIC 00104: NIBTSG_ATTR_WAVEFORM_FILE_VERSION

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__attributes__waveform__file__version_1gaa67b8a6d1284a128f3e701cd873700db.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__attributes__waveform__file__version_1gaa67b8a6d1284a128f3e701cd873700db.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Function: niBTSG_GetWaveformFileVersion SyntaxNIBTSG_ATTR_WAVEFORM_FILE_VERSIONNumeric ValueData TypeAccessApplies To81int32Read/WriteN/ARemarks Set Function: niBTSG_SetWaveformFileVersion

### NIBTSG_ATTR_WAVEFORM_FILE_VERSION

Get Function: niBTSG_GetWaveformFileVersion

#### Syntax

NIBTSG_ATTR_WAVEFORM_FILE_VERSION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 81 | int32 | Read/Write | N/A |

#### Remarks

Set Function: niBTSG_SetWaveformFileVersion

Parent topic:

Waveform File Version

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions.html language=enus -->
## TOPIC 00105: Functions

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsConfigure GenerationRFSG Waveform DatabaseUtilityGroup membersNameDescriptionniBTSG_ChannelNumberToCarrierFrequencyComputes the carrier frequency of the Bluetooth signal to generate based on the value that you specify in the channelNumber parameter. The BT Generation computes the center freque

### Functions

#### Groups

- Configure Generation
- RFSG Waveform Database
- Utility

#### Group members

| Name | Description |
| --- | --- |
| niBTSG_ChannelNumberToCarrierFrequency | Computes the carrier frequency of the Bluetooth signal to generate based on the value that you specify in the channelNumber parameter. The BT Generation computes the center frequency according to section 2, Part A, Volume 2 of the Bluetooth Specification Version 4.2. |
| niBTSG_CloseSession | Closes the niBT SG session and releases resources associated with that session. Call this function once for each unique named session that you have created. |
| niBTSG_CreateWaveformComplexF64 | Creates a waveform according to the values that you specify. This function generates one frame at a time. |
| niBTSG_OpenSession | Looks up an existing niBT SG session using the sessionName parameter and returns the refnum that you can pass to subsequent niBT SG functions. If the lookup fails, the niBTSG_OpenSession function creates a new niBT SG session and returns a new refnum. |
| niBTSG_ResetSession | Resets all the attributes of the session to their default values. |
| niBTSG_SetAntennaRelativePhaseAndAmplitude | Sets the Relative Phase and Relative Amplitude values for the non reference antennas An (1<n<=256) relative to the reference antenna A0 when you set the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED attribute to NIBTSG_VAL_TRUE. The reference period and sampling slots in the constant tone extension (CTE) field are modulated in amplitude and phase as specified in the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN attribute. |

#### Attachments

None

Parent topic:

niBTGeneration.h

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions_1ga15c5fbb2f93dff65fd848a27b6e8aaed.html language=enus -->
## TOPIC 00106: niBTSG_CloseSession

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions_1ga15c5fbb2f93dff65fd848a27b6e8aaed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions_1ga15c5fbb2f93dff65fd848a27b6e8aaed.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the niBT SG session and releases resources associated with that session. Call this function once for each unique named session that you have created. Syntaxint32 __stdcall niBTSG_CloseSession(niBTSGSession session)ParametersNameDirectionTypeDescriptionsession[out]niBTSGSessionSpecifies the ni

### niBTSG_CloseSession

Closes the niBT SG session and releases resources associated with that session. Call this function once for each unique named session that you have created.

#### Syntax

int32 __stdcall niBTSG_CloseSession(niBTSGSession session)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions_1ga6d821440ea6d8bdfbe73d1e0b4a0e150.html language=enus -->
## TOPIC 00107: niBTSG_ChannelNumberToCarrierFrequency

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions_1ga6d821440ea6d8bdfbe73d1e0b4a0e150.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions_1ga6d821440ea6d8bdfbe73d1e0b4a0e150.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the carrier frequency of the Bluetooth signal to generate based on the value that you specify in the channelNumber parameter. The BT Generation computes the center frequency according to section 2, Part A, Volume 2 of the Bluetooth Specification Version 4.2. Syntaxint32 __stdcall niBTSG_Cha

### niBTSG_ChannelNumberToCarrierFrequency

Computes the carrier frequency of the Bluetooth signal to generate based on the value that you specify in the **channelNumber** parameter. The BT Generation computes the center frequency according to section 2, Part A, Volume 2 of the *Bluetooth Specification Version 4.2*.

#### Syntax

int32 __stdcall niBTSG_ChannelNumberToCarrierFrequency(int32 channelNumber, int32 standard, float64 *carrierFrequency)

#### Remarks

The Bluetooth system operates in the 2.4 GHz ISM band. This frequency band is 2,400 MHz to 2,483.5 MHz. RF channels are spaced 1 MHz apart and are ordered in channel number *k* according to the following formula: *f* = 2,402 + *k* MHz, where *k* = 0, 1, ..., 78 for Basic Rate/Enhanced Data Rate packets and *f* = 2,402 + (2 * *k*) MHz, where *k* = 0, 1, ..., 39 for a Low Energy packet, and *f* is the frequency of the RF channels.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| channelNumber | [in] | int32 | Specifies the channel number. |
| standard | [in] | int32 | Specifies the standard. The default value is NIBTSG_STANDARD_BASIC_OR_EDR.NIBTSG_STANDARD_BASIC_OR_EDR(0)Specifies that the standard is basic rate or enhanced data rate (EDR).NIBTSG_STANDARD_LE(1)Specifies that the standard is low energy (LE). |
|  |  |  |  |
| NIBTSG_STANDARD_BASIC_OR_EDR(0) | Specifies that the standard is basic rate or enhanced data rate (EDR). |  |  |
| NIBTSG_STANDARD_LE(1) | Specifies that the standard is low energy (LE). |  |  |
| carrierFrequency | [out] | float64 * | Returns the RF frequency (f) corresponding to the channel number k, where f = 2,402 + k MHz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions_1gac3082266eeddda5c672366452fdeb3d6.html language=enus -->
## TOPIC 00108: niBTSG_CreateWaveformComplexF64

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions_1gac3082266eeddda5c672366452fdeb3d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions_1gac3082266eeddda5c672366452fdeb3d6.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a waveform according to the values that you specify. This function generates one frame at a time. Syntaxint32 __stdcall niBTSG_CreateWaveformComplexF64(niBTSGSession session, int32 reset, float64 *t0, float64 *dt, NIComplexNumber waveform, int32 waveformSize, int32 *actualWaveformSize, int32

### niBTSG_CreateWaveformComplexF64

Creates a waveform according to the values that you specify. This function generates one frame at a time.

#### Syntax

int32 __stdcall niBTSG_CreateWaveformComplexF64(niBTSGSession session, int32 reset, float64 *t0, float64 *dt, NIComplexNumber waveform, int32 waveformSize, int32 *actualWaveformSize, int32 *generationDone)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| reset | [in] | int32 | Specifies whether to reset the internal states in the created waveform. |
| t0 | [out] | float64 * | Returns the starting time, in seconds. |
| dt | [out] | float64 * | Returns the time interval between baseband I/Q samples, in seconds. |
| waveform | [out] | NIComplexNumber | Returns the array of baseband complex I/Q samples. |
| waveformSize | [in] | int32 | Specifies the waveform size, in samples. |
| actualWaveformSize | [out] | int32 * | Returns the actual size of the waveform. |
| generationDone | [out] | int32 * | Indicates whether the function has generated all the frames. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions_1gad43e6f7dc237a0a76c7a89843eaefba9.html language=enus -->
## TOPIC 00109: niBTSG_ResetSession

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions_1gad43e6f7dc237a0a76c7a89843eaefba9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions_1gad43e6f7dc237a0a76c7a89843eaefba9.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all the attributes of the session to their default values. Syntaxint32 __stdcall niBTSG_ResetSession(niBTSGSession session)ParametersNameDirectionTypeDescriptionsession[out]niBTSGSessionSpecifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriat

### niBTSG_ResetSession

Resets all the attributes of the session to their default values.

#### Syntax

int32 __stdcall niBTSG_ResetSession(niBTSGSession session)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions_1gaf29390443389ffe60bafcb94e0ec16a1.html language=enus -->
## TOPIC 00110: niBTSG_SetAntennaRelativePhaseAndAmplitude

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions_1gaf29390443389ffe60bafcb94e0ec16a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions_1gaf29390443389ffe60bafcb94e0ec16a1.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Relative Phase and Relative Amplitude values for the non reference antennas An (1<n<=256) relative to the reference antenna A0 when you set the NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED attribute to NIBTSG_VAL_TRUE. The reference period and sampling slots in the constant tone

### niBTSG_SetAntennaRelativePhaseAndAmplitude

Sets the Relative Phase and Relative Amplitude values for the non reference antennas An (1<n<=256) relative to the reference antenna A0 when you set the [NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1gab6a8af5abb3e1d86bdba635dd958048b.html) attribute to NIBTSG_VAL_TRUE. The reference period and sampling slots in the constant tone extension (CTE) field are modulated in amplitude and phase as specified in the [NIBTSG_ATTR_DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN](group____root__ni_b_t_generation__attributes__packet__settings__direction__finding_1ga8c8615a65828d1e6a8b857ccf95cefac.html) attribute.

#### Syntax

int32 __stdcall niBTSG_SetAntennaRelativePhaseAndAmplitude(niBTSGSession session, ViChar channelString, float64 relativeAmplitudeDb, float64 relativePhaseDeg, int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [out] | ViChar | Specifies the RFSG device channel. Set this parameter to "" (empty string) or NULL. |
| relativeAmplitudeDb | [out] | float64 | Specifies the array of amplitudes of each non-reference antenna An (1<n<=256) relative to the reference antenna A0. The first element of the array corresponds to the amplitude of antenna A1, the second element of the array corresponds to amplitude of antenna A2, and so on. |
| relativePhaseDeg | [out] | float64 | Specifies the array of phases of each non-reference antenna An (1<n<=256) relative to the reference antenna A0. The first element of the array corresponds to the phase of antenna A1, the second element of the array corresponds to phase of antenna A2, and so on. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions_1gafd000327e7f008d3f682f57df2e11822.html language=enus -->
## TOPIC 00111: niBTSG_OpenSession

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions_1gafd000327e7f008d3f682f57df2e11822.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions_1gafd000327e7f008d3f682f57df2e11822.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Looks up an existing niBT SG session using the sessionName parameter and returns the refnum that you can pass to subsequent niBT SG functions. If the lookup fails, the niBTSG_OpenSession function creates a new niBT SG session and returns a new refnum. Syntaxint32 __stdcall niBTSG_OpenSession(ViChar

### niBTSG_OpenSession

Looks up an existing niBT SG session using the **sessionName** parameter and returns the refnum that you can pass to subsequent niBT SG functions. If the lookup fails, the [niBTSG_OpenSession](group____root__ni_b_t_generation__functions_1gafd000327e7f008d3f682f57df2e11822.html) function creates a new niBT SG session and returns a new refnum.

#### Syntax

int32 __stdcall niBTSG_OpenSession(ViChar sessionName, int32 toolkitCompatibilityVersion, niBTSGSession *session, int32 *isNewSession)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| sessionName | [out] | ViChar | Specifies the name of the session that you are looking up or creating. If a session with the same name already exists, this function returns a reference to that session. To get the reference to an already-opened session x, specify x as the session name.You can obtain the reference to an existing session multiple times if you have not called the niBTSG_CloseSession function in that session. You do not need to close the session multiple times. To create an unnamed session, pass an empty string or NULL to the sessionName parameter.Tip- NI recommends that you call the niBTSG_CloseSession function for each uniquely named instance of the niBTSG_OpenSession function or each instance of the niBTSG_OpenSession function with an unnamed session. |
| toolkitCompatibilityVersion | [in] | int32 | Specifies the version of the BT Generation to which the current version of the BT Generation is compatible. If the behavior of the BT Generation changes in a new version, use this parameter to specify that you want to continue using the behavior of the previous release.NIBTSG_VAL_TOOLKIT_COMPATIBILITY_VERSION_010000 (10000)Specifies that the current version of the toolkit is compatible with 1.0.0.NIBTSG_VAL_TOOLKIT_COMPATIBILITY_VERSION_020000 (20000)Specifies that the current version of the toolkit is compatible with 2.0.0. |
|  |  |  |  |
| NIBTSG_VAL_TOOLKIT_COMPATIBILITY_VERSION_010000 (10000) | Specifies that the current version of the toolkit is compatible with 1.0.0. |  |  |
| NIBTSG_VAL_TOOLKIT_COMPATIBILITY_VERSION_020000 (20000) | Specifies that the current version of the toolkit is compatible with 2.0.0. |  |  |
| session | [out] | niBTSGSession * | Returns the niBT SG session. |
| isNewSession | [out] | int32 * | Indicates whether the function creates a new session.NIBTSG_VAL_TRUE (0)Indicates that the function creates a new session.NIBTSG_VAL_FALSE (1)Indicates that the function returns a reference to an existing session. |
|  |  |  |  |
| NIBTSG_VAL_TRUE (0) | Indicates that the function creates a new session. |  |  |
| NIBTSG_VAL_FALSE (1) | Indicates that the function returns a reference to an existing session. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation.html language=enus -->
## TOPIC 00112: Configure Generation

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsSet/Get/Reset AttributesGroup membersNoneAttachmentsNone

### Configure Generation

#### Groups

- Set/Get/Reset Attributes

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes.html language=enus -->
## TOPIC 00113: Set/Get/Reset Attributes

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsGet AttributesSet AttributesGroup membersNameDescriptionniBTSG_ResetAttributeResets the attribute specified in the attributeID parameter to its default value. You can reset only a writable attribute using this function. AttachmentsNone

### Set/Get/Reset Attributes

#### Groups

- Get Attributes
- Set Attributes

#### Group members

| Name | Description |
| --- | --- |
| niBTSG_ResetAttribute | Resets the attribute specified in the attributeID parameter to its default value. You can reset only a writable attribute using this function. |

#### Attachments

None

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes_1ga60e704f46c9be513e08a6c410df947a9.html language=enus -->
## TOPIC 00114: niBTSG_ResetAttribute

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes_1ga60e704f46c9be513e08a6c410df947a9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes_1ga60e704f46c9be513e08a6c410df947a9.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute specified in the attributeID parameter to its default value. You can reset only a writable attribute using this function. Syntaxint32 __stdcall niBTSG_ResetAttribute(niBTSGSession session, ViChar channelString, int32 attributeID)ParametersNameDirectionTypeDescriptionsession[out]

### niBTSG_ResetAttribute

Resets the attribute specified in the **attributeID** parameter to its default value. You can reset only a writable attribute using this function.

#### Syntax

int32 __stdcall niBTSG_ResetAttribute(niBTSGSession session, ViChar channelString, int32 attributeID)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| attributeID | [in] | int32 | Specifies the ID of the niBT SG attribute that you want to reset. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set/Get/Reset Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes.html language=enus -->
## TOPIC 00115: Get Attributes

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniBTSG_GetScalarAttributeF64Queries the value of an niBT SG 64-bit floating point number (float64) scalar attribute. niBTSG_GetScalarAttributeI32Queries the value of an niBT SG 32-bit integer (int32) scalar attribute. niBTSG_GetVectorAttributeF64Queries the valu

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niBTSG_GetScalarAttributeF64 | Queries the value of an niBT SG 64-bit floating point number (float64) scalar attribute. |
| niBTSG_GetScalarAttributeI32 | Queries the value of an niBT SG 32-bit integer (int32) scalar attribute. |
| niBTSG_GetVectorAttributeF64 | Queries the value of an niBT SG 64-bit integer (int32) vector attribute. |
| niBTSG_GetVectorAttributeI32 | Queries the value of an niBT SG 32-bit integer (int32) vector attribute. |

#### Attachments

None

Parent topic:

Set/Get/Reset Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1ga4a630bb2853578a9ecf032eeb35299be.html language=enus -->
## TOPIC 00116: niBTSG_GetScalarAttributeF64

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1ga4a630bb2853578a9ecf032eeb35299be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1ga4a630bb2853578a9ecf032eeb35299be.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an niBT SG 64-bit floating point number (float64) scalar attribute. Syntaxint32 __stdcall niBTSG_GetScalarAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, float64 *attributeValue)ParametersNameDirectionTypeDescriptionsession[in]niBTSGSessionSpec

### niBTSG_GetScalarAttributeF64

Queries the value of an niBT SG 64-bit floating point number (float64) scalar attribute.

#### Syntax

int32 __stdcall niBTSG_GetScalarAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, float64 *attributeValue)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| attributeID | [in] | niBTSG_Attr | Specifies the ID of a float64 niBT SG scalar attribute. |
| attributeValue | [out] | float64 * | Returns the value of the attribute that you specify using the attributeID parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1ga55aab1cb568298f6aba424a527d70ea1.html language=enus -->
## TOPIC 00117: niBTSG_GetScalarAttributeI32

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1ga55aab1cb568298f6aba424a527d70ea1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1ga55aab1cb568298f6aba424a527d70ea1.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an niBT SG 32-bit integer (int32) scalar attribute. Syntaxint32 __stdcall niBTSG_GetScalarAttributeI32(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, int32 *attributeValue)ParametersNameDirectionTypeDescriptionsession[in]niBTSGSessionSpecifies the niBT SG

### niBTSG_GetScalarAttributeI32

Queries the value of an niBT SG 32-bit integer (int32) scalar attribute.

#### Syntax

int32 __stdcall niBTSG_GetScalarAttributeI32(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, int32 *attributeValue)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| attributeID | [in] | niBTSG_Attr | Specifies the ID of an int32 niBT SG scalar attribute. |
| attributeValue | [out] | int32 * | Returns the value of the attribute that you specify using the attributeID parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1gadd7dd33fcec293372992b1d322b04499.html language=enus -->
## TOPIC 00118: niBTSG_GetVectorAttributeI32

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1gadd7dd33fcec293372992b1d322b04499.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1gadd7dd33fcec293372992b1d322b04499.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an niBT SG 32-bit integer (int32) vector attribute. Syntaxint32 __stdcall niBTSG_GetVectorAttributeI32(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, int32 dataArraySize, int32 dataArray, int32 *actualNumDataArrayElements)ParametersNameDirectionTypeDescrip

### niBTSG_GetVectorAttributeI32

Queries the value of an niBT SG 32-bit integer (int32) vector attribute.

#### Syntax

int32 __stdcall niBTSG_GetVectorAttributeI32(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, int32 dataArraySize, int32 dataArray, int32 *actualNumDataArrayElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| attributeID | [in] | niBTSG_Attr | Specifies the ID of an int32 niBT SG vector attribute. |
| dataArraySize | [in] | int32 | Specifies the number of elements in the int32 array. |
| dataArray | [out] | int32 | Returns the value of the attribute that you specify using the attributeID parameter. Pass NULL to the dataArray parameter to get the size of the array in the actualNumDataArrayElements parameter. |
| actualNumDataArrayElements | [out] | int32 * | Returns the actual number of elements in the dataArray array. If the dataArray array is not large enough to hold all the samples, the function returns an error code, and the actualNumDataArrayElements parameter returns the minimum expected size of the output array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1gafa625941d617c6605e7ed425481caa5f.html language=enus -->
## TOPIC 00119: niBTSG_GetVectorAttributeF64

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1gafa625941d617c6605e7ed425481caa5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__get__attributes_1gafa625941d617c6605e7ed425481caa5f.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an niBT SG 64-bit integer (int32) vector attribute. Syntaxint32 __stdcall niBTSG_GetVectorAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, int32 dataArraySize, float64 data, int32 *actualNumDataArrayElements)ParametersNameDirectionTypeDescriptio

### niBTSG_GetVectorAttributeF64

Queries the value of an niBT SG 64-bit integer (int32) vector attribute.

#### Syntax

int32 __stdcall niBTSG_GetVectorAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, int32 dataArraySize, float64 data, int32 *actualNumDataArrayElements)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| attributeID | [in] | niBTSG_Attr | Specifies the ID of an int32 niBT SG vector attribute. |
| dataArraySize | [in] | int32 | Specifies the number of elements in the data array. |
| data | [out] | float64 | Returns the value of the attribute that you specify using the attributeID parameter. Pass NULL to the data parameter to get the size of the array in the actualNumDataArrayElements parameter. |
| actualNumDataArrayElements | [out] | int32 * | Returns the actual number of elements in the data array. If the data array is not large enough to hold all the samples, the function returns an error code, and the actualNumDataArrayElements parameter returns the minimum expected size of the output array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__set__attributes_1ga99aeccf025866d5b824059ef41b86baa.html language=enus -->
## TOPIC 00120: niBTSG_SetVectorAttributeF64

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__set__attributes_1ga99aeccf025866d5b824059ef41b86baa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__set__attributes_1ga99aeccf025866d5b824059ef41b86baa.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an niBT SG 64-bit floating point number (float64) vector attribute. Syntaxint32 __stdcall niBTSG_SetVectorAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, float64 data, int32 dataArraySize)ParametersNameDirectionTypeDescriptionsession[in]niBTSGSess

### niBTSG_SetVectorAttributeF64

Sets the value of an niBT SG 64-bit floating point number (float64) vector attribute.

#### Syntax

int32 __stdcall niBTSG_SetVectorAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, float64 data, int32 dataArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| attributeID | [in] | niBTSG_Attr | Specifies the ID of a float64 niBT SG vector attribute. |
| data | [in] | float64 | Specifies the pointer to the int32 array for which you want to set the attribute. |
| dataArraySize | [in] | int32 | Specifies the number of elements in the data array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__set__attributes_1gaf446b1159d23a525aecabe64bcc309c5.html language=enus -->
## TOPIC 00121: niBTSG_SetScalarAttributeF64

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__set__attributes_1gaf446b1159d23a525aecabe64bcc309c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__configure__generation__setgetreset__attributes__set__attributes_1gaf446b1159d23a525aecabe64bcc309c5.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an niBT SG 64-bit floating point number (float64) vector attribute. Syntaxint32 __stdcall niBTSG_SetScalarAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, float64 attributeValue)ParametersNameDirectionTypeDescriptionsession[in]niBTSGSessionSpeci

### niBTSG_SetScalarAttributeF64

Queries the value of an niBT SG 64-bit floating point number (float64) vector attribute.

#### Syntax

int32 __stdcall niBTSG_SetScalarAttributeF64(niBTSGSession session, ViChar channelString, niBTSG_Attr attributeID, float64 attributeValue)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| attributeID | [in] | niBTSG_Attr | Specifies the ID of a float64 niBT SG scalar attribute. |
| attributeValue | [in] | float64 | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__rfsg__waveform__database_1ga5878b6562266c95d012851530c8f0226.html language=enus -->
## TOPIC 00122: niBTSG_RFSGConfigureScript

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__rfsg__waveform__database_1ga5878b6562266c95d012851530c8f0226.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__rfsg__waveform__database_1ga5878b6562266c95d012851530c8f0226.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the I/Q rate and power level of the waveforms that you specify in the script parameter. This function sets the NIRFSG_ATTR_IQ_RATE attribute to the I/Q rate in the RFSG database if the I/Q rates are the same for all the waveforms. The function sets the NIRFSG_ATTR_POWER_LEVEL attribute to

### niBTSG_RFSGConfigureScript

Configures the I/Q rate and power level of the waveforms that you specify in the **script** parameter. This function sets the NIRFSG_ATTR_IQ_RATE attribute to the I/Q rate in the RFSG database if the I/Q rates are the same for all the waveforms. The function sets the NIRFSG_ATTR_POWER_LEVEL attribute to the sum of the power level that you specify in the **powerLevel** parameter and the minimum headrooms of all the waveforms.

#### Syntax

int32 __stdcall niBTSG_RFSGConfigureScript(ViSession rfsgHandle, ViChar channelString, ViChar script, float64 powerLevel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgHandle | [in] | ViSession | Identifies the instrument session. You can obtain this parameter from the niRFSG_init function or the niRFSG_InitWithOptions function. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| script | [in] | ViChar | Specifies the script that controls waveform generation. NI-RFSG supports multiple scripts that you can select using the NIRFSG_ATTR_SELECTED_SCRIPT attribute. |
| powerLevel | [in] | float64 | Specifies the power level. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

RFSG Waveform Database

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__rfsg__waveform__database_1ga8888244382b76a98167d97435be06941.html language=enus -->
## TOPIC 00123: niBTSG_RFSGRetrieveIQRate

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__rfsg__waveform__database_1ga8888244382b76a98167d97435be06941.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__rfsg__waveform__database_1ga8888244382b76a98167d97435be06941.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q rate stored in the RFSG database. The function uses the waveform name as the key to retrieve the waveform attributes. Syntaxint32 __stdcall niBTSG_RFSGRetrieveIQRate(ViSession rfsgHandle, ViChar channelString, ViChar waveformName, float64 *iqRate)RemarksParametersNameDirectionTypeDes

### niBTSG_RFSGRetrieveIQRate

Returns the I/Q rate stored in the RFSG database. The function uses the waveform name as the key to retrieve the waveform attributes.

#### Syntax

int32 __stdcall niBTSG_RFSGRetrieveIQRate(ViSession rfsgHandle, ViChar channelString, ViChar waveformName, float64 *iqRate)

#### Remarks

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgHandle | [in] | ViSession | Identifies the instrument session. You can obtain this parameter from the niRFSG_init function or the niRFSG_InitWithOptions function. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| waveformName | [in] | ViChar | Specifies the name of the waveform for which you want to retrieve the I/Q rate. The BT Generation uses the waveformName parameter as the key to retrieve the waveform attributes from the RFSG database. |
| iqRate | [out] | float64 * | Returns the I/Q rate stored in the RFSG database for the waveform that you specify in the waveformName parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

RFSG Waveform Database

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__rfsg__waveform__database_1gad1c391b21321d382f85d22b2f4ecca60.html language=enus -->
## TOPIC 00124: niBTSG_RFSGRetrieveIQRateAllWaveforms

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__rfsg__waveform__database_1gad1c391b21321d382f85d22b2f4ecca60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__rfsg__waveform__database_1gad1c391b21321d382f85d22b2f4ecca60.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the I/Q rate of all the waveforms in the script that you specify in the script parameter. This function returns the I/Q rate if the I/Q rates are the same for all the waveforms. If the I/Q rates are different, the function returns an error. Syntaxint32 __stdcall niBTSG_RFSGRetrieveIQRateAllWa

### niBTSG_RFSGRetrieveIQRateAllWaveforms

Checks the I/Q rate of all the waveforms in the script that you specify in the **script** parameter. This function returns the I/Q rate if the I/Q rates are the same for all the waveforms. If the I/Q rates are different, the function returns an error.

#### Syntax

int32 __stdcall niBTSG_RFSGRetrieveIQRateAllWaveforms(ViSession rfsgHandle, ViChar channelString, ViChar script, float64 *iqRate)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgHandle | [in] | ViSession | Identifies the instrument session. You can obtain this parameter from the niRFSG_init function or the niRFSG_InitWithOptions function. |
| channelString | [in] | ViChar | Set this parameter to "" (empty string) or NULL. |
| script | [in] | ViChar | Specifies the RFSG script used to generate the signal. The function looks up the I/Q rate of all the waveforms contained in the script. |
| iqRate | [out] | float64 * | Returns the I/Q rate if the I/Q rates are the same for all the waveforms that you specify in the script parameter. If the I/Q rates are different, the function returns an error. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

RFSG Waveform Database

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__utility.html language=enus -->
## TOPIC 00125: Utility

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__utility.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniBTSG_CreateAndWriteWaveformsToFileCreates waveforms according to the parameters you specify, and saves the waveforms to a file. niBTSG_GetErrorStringTakes the error code returned by niBT generation functions and returns the interpretation as a user-readable st

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niBTSG_CreateAndWriteWaveformsToFile | Creates waveforms according to the parameters you specify, and saves the waveforms to a file. |
| niBTSG_GetErrorString | Takes the error code returned by niBT generation functions and returns the interpretation as a user-readable string. |
| niBTSG_LoadConfigurationFromFile | Reads values of session attributes (configuration) saved in a file and sets these values to the corresponding attributes on the session, thus restoring the state of the BT Generation to the original state when the file was saved. |
| niBTSG_ReadWaveformFromFile | Reads a waveform from a TDMS file. You can save this file using the Generation Interactive Example for Bluetooth. The niBTSG_ReadWaveformFromFile function returns the I/Q complex waveform data that you can subsequently download to an RF signal generator device. |
| niBTSG_SaveConfigurationToFile | Saves attributes of the session, which you may have modified after opening the session, to a file located at the specified path. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html language=enus -->
## TOPIC 00126: niBTSG_GetErrorString

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes the error code returned by niBT generation functions and returns the interpretation as a user-readable string. Syntaxint32 __stdcall niBTSG_GetErrorString(niBTSGSession session, int32 errorCode, int32 errorMessageLength, ViChar errorMessage)ParametersNameDirectionTypeDescriptionsession[in]niBT

### niBTSG_GetErrorString

Takes the error code returned by niBT generation functions and returns the interpretation as a user-readable string.

#### Syntax

int32 __stdcall niBTSG_GetErrorString(niBTSGSession session, int32 errorCode, int32 errorMessageLength, ViChar errorMessage)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| errorCode | [in] | int32 | Specifies the error code that is returned by any of the niBT generation functions. |
| errorMessageLength | [in] | int32 | Specifies the length of the errorMessage buffer. |
| errorMessage | [in] | ViChar | Returns the user-readable message string that corresponds to the error code you specify. The errorMessage buffer must have at least as many elements as are indicated in the errorMessageLength parameter. If you pass NULL to the errorMessage parameter, the function returns the actual length of the error message. |

#### Returns

Returns the actual length of the error message string.

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__utility_1gaa2bc0cce2d5439af76b953f91a572192.html language=enus -->
## TOPIC 00127: niBTSG_ReadWaveformFromFile

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__utility_1gaa2bc0cce2d5439af76b953f91a572192.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__utility_1gaa2bc0cce2d5439af76b953f91a572192.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform from a TDMS file. You can save this file using the Generation Interactive Example for Bluetooth. The niBTSG_ReadWaveformFromFile function returns the I/Q complex waveform data that you can subsequently download to an RF signal generator device. Syntaxint32 __stdcall niBTSG_ReadWavef

### niBTSG_ReadWaveformFromFile

Reads a waveform from a TDMS file. You can save this file using the *Generation Interactive Example for Bluetooth*. The [niBTSG_ReadWaveformFromFile](group____root__ni_b_t_generation__functions__utility_1gaa2bc0cce2d5439af76b953f91a572192.html) function returns the I/Q complex waveform data that you can subsequently download to an RF signal generator device.

#### Syntax

int32 __stdcall niBTSG_ReadWaveformFromFile(ViChar filePath, ViChar waveformName, int64_t offset, int64_t count, float64 *t0, float64 *dt, NIComplexNumber waveform, int32 waveformSize, int32 *actualNumWaveformSamples, float64 *iqRate, float64 *headroom, int32 *eof)

#### Remarks

In addition to the I/Q complex waveform data, the *Generation Interactive Example for Bluetooth* also saves the [NIBTSG_ATTR_HEADROOM](group____root__ni_b_t_generation__attributes__hardware__settings_1gad2634f53369b3b1bb3f24b9efa6adebd.html) and [NIBTSG_ATTR_IQ_RATE](group____root__ni_b_t_generation__attributes__hardware__settings__recommended__settings_1ga6b0723d1da00183f276e82dd38132b57.html) attributes of the waveform to the file. Use the [niBTSG_ReadWaveformFromFile](group____root__ni_b_t_generation__functions__utility_1gaa2bc0cce2d5439af76b953f91a572192.html) function or TDMS file attributes in your programming environment to read the values of these attributes. The NI_RF_IQRate and NI_RF_Headroom attributes are located in the following locations within the TDMS file.

| Attribute Name | Datatype | Group Name | Channel Name |
| --- | --- | --- | --- |
| NI_RF_IQRate | float64 | waveforms | niBT SG Waveform |
| NI_RF_Headroom | float64 | waveforms | niBT SG Waveform |

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [out] | ViChar | Specifies the complete path to the TDMS file from which the BT Generation reads the waveform. |
| waveformName | [out] | ViChar | Specifies the name of the waveform to read from the file. |
| offset | [in] | int64_t | Specifies the number of samples into the waveform at which the function begins reading the I/Q data. The default value is 0. If you set count to 1,000 and offset to 2, the function returns 1,000 samples, starting from index 2 and ending at index 1,002. |
| count | [in] | int64_t | Specifies the maximum number of samples of the I/Q complex waveform to read from the file. The default value is -1, which returns all samples. If you set count to 1,000 and offset to 2, the function returns 1,000 samples, starting from index 2 and ending at index 1,002. |
| t0 | [out] | float64 * | Returns the starting time, in seconds. |
| dt | [out] | float64 * | Returns the time interval between baseband I/Q samples, in seconds. |
| waveform | [out] | NIComplexNumber | Returns the array of baseband complex I/Q samples. |
| waveformSize | [in] | int32 | Specifies the waveform size, in samples. |
| actualNumWaveformSamples | [out] | int32 * | Returns the actual length of the waveform. |
| iqRate | [out] | float64 * | Returns the I/Q rate, in samples per second (S/s), of the waveform. |
| headroom | [out] | float64 * | Returns the headroom of the waveform. This value is expressed in dB. |
| eof | [out] | int32 * | Indicates whether the end of file has been reached with this read. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__utility_1gad12acc2e74c73567c4010dc676830066.html language=enus -->
## TOPIC 00128: niBTSG_LoadConfigurationFromFile

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__utility_1gad12acc2e74c73567c4010dc676830066.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__utility_1gad12acc2e74c73567c4010dc676830066.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads values of session attributes (configuration) saved in a file and sets these values to the corresponding attributes on the session, thus restoring the state of the BT Generation to the original state when the file was saved. Syntaxint32 __stdcall niBTSG_LoadConfigurationFromFile(niBTSGSession s

### niBTSG_LoadConfigurationFromFile

Reads values of session attributes (configuration) saved in a file and sets these values to the corresponding attributes on the session, thus restoring the state of the BT Generation to the original state when the file was saved.

#### Syntax

int32 __stdcall niBTSG_LoadConfigurationFromFile(niBTSGSession session, ViChar filePath, int32 reset)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| filePath | [out] | ViChar | Specifies the absolute path to the file from which the BT Generation loads the configuration. |
| reset | [in] | int32 | Specifies whether BT Generation must reset all the attributes of the session to their default values before setting the new values specified in the file. The default value is NIBTSG_VAL_TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxbtgen-c-api-ref path=group____root__ni_b_t_generation__functions__utility_1gad71752e4d9de973c16cf96c49773daf9.html language=enus -->
## TOPIC 00129: niBTSG_SaveConfigurationToFile

- bundle_id: `rfmxbtgen-c-api-ref`
- source_path: `group____root__ni_b_t_generation__functions__utility_1gad71752e4d9de973c16cf96c49773daf9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbtgen-c-api-ref/raw/resource/enus/group____root__ni_b_t_generation__functions__utility_1gad71752e4d9de973c16cf96c49773daf9.html
- document_id: `rfmxbtgen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves attributes of the session, which you may have modified after opening the session, to a file located at the specified path. Syntaxint32 __stdcall niBTSG_SaveConfigurationToFile(niBTSGSession session, ViChar filePath, int32 operation)RemarksYou can use this function to save the current state of

### niBTSG_SaveConfigurationToFile

Saves attributes of the session, which you may have modified after opening the session, to a file located at the specified path.

#### Syntax

int32 __stdcall niBTSG_SaveConfigurationToFile(niBTSGSession session, ViChar filePath, int32 operation)

#### Remarks

You can use this function to save the current state of the BT Generation session to a file. You can later load the saved configuration using the [niBTSG_LoadConfigurationFromFile](group____root__ni_b_t_generation__functions__utility_1gad12acc2e74c73567c4010dc676830066.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBTSGSession | Specifies the niBT SG session. Use this parameter to configure the behavior and operation of the appropriate RFmx BT Generation function that accepts the niBTSGSession as an input. |
| filePath | [out] | ViChar | Specifies the absolute path to the TDMS file to which the BT Generation saves the configuration. |
| operation | [in] | int32 | Specifies the operation to perform on the file. The default value is NIBTSG_FILE_OPERATION_MODE_CREATEORREPLACE.NIBTSG_FILE_OPERATION_MODE_OPEN(0)Opens an existing file to write the niBT SG session attribute values.NIBTSG_FILE_OPERATION_MODE_OPENORCREATE(1)Opens an existing file or creates a new file if the file does not exist.NIBTSG_FILE_OPERATION_MODE_CREATEORREPLACE(2)Creates a new file or replaces an existing file.NIBTSG_FILE_OPERATION_MODE_CREATE(3)Creates a new file. |
|  |  |  |  |
| NIBTSG_FILE_OPERATION_MODE_OPEN(0) | Opens an existing file to write the niBT SG session attribute values. |  |  |
| NIBTSG_FILE_OPERATION_MODE_OPENORCREATE(1) | Opens an existing file or creates a new file if the file does not exist. |  |  |
| NIBTSG_FILE_OPERATION_MODE_CREATEORREPLACE(2) | Creates a new file or replaces an existing file. |  |  |
| NIBTSG_FILE_OPERATION_MODE_CREATE(3) | Creates a new file. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBT SG function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niBTSG_GetErrorString](group____root__ni_b_t_generation__functions__utility_1ga204ab69a4854ad6574f46d52349c66a6.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility
