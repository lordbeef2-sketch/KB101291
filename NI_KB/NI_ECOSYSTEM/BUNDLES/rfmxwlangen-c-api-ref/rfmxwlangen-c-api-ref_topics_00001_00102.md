# NI DOCUMENT BUNDLE: rfmxwlangen-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwlangen-c-api-ref start=1 end=102 -->
<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes_1ga062d645caf7b2f41bff1457b6837dd99.html language=enus -->
## TOPIC 00001: NIWLANG_ATTR_UNEQUAL_MODULATION_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes_1ga062d645caf7b2f41bff1457b6837dd99.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes_1ga062d645caf7b2f41bff1457b6837dd99.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable unequal modulation (UEQM) for 802.11bn MU PPDU signals with 2 to 4 spatial streams. UEQM is only supported in non-MU-MIMO beamformed transmission. Modulation order of different spatial streams is determined by value of Pattern Index attribute. This attribute is applicable

### NIWLANG_ATTR_UNEQUAL_MODULATION_ENABLED

Specifies whether to enable unequal modulation (UEQM) for 802.11bn MU PPDU signals with 2 to 4 spatial streams. UEQM is only supported in non-MU-MIMO beamformed transmission. Modulation order of different spatial streams is determined by value of Pattern Index attribute. This attribute is applicable only when Standard attribute is set to 80211BN MIMOOFDM.

#### Syntax

NIWLANG_ATTR_UNEQUAL_MODULATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 229 | int32 | Read/Write | N/A |

#### Remarks

You must use the following [active channel](https://www.ni.com/docs/en-US/bundle/rfmx-waveform-creator/page/configuring-active-channels-labview2.html) string formats to configure this attribute.

| Standard Attribute Value | Active Channel String Format |
| --- | --- |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU |

The default value is NIWLANG_VAL_FALSE.

Set Function: niWLANG_SetSetUnequalModulationEnabled 
 Get Function: niWLANG_GetSetUnequalModulationEnabled

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes_1ga5a3cabfb1f866edcb759467a4052270d.html language=enus -->
## TOPIC 00002: NIWLANG_ATTR_UNEQUAL_MODULATION_PATTERN_INDEX

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes_1ga5a3cabfb1f866edcb759467a4052270d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes_1ga5a3cabfb1f866edcb759467a4052270d.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unequal modulation pattern index when Unequal Modulation Enabled attribute is set to True. This attribute is applicable only when Standard attribute is set to 80211BN MIMOOFDM. The allowed modulation orders for unequal modulation are QPSK, 16-QAM, 64-QAM, 256-QAM, 1024-QAM and 4096-QAM

### NIWLANG_ATTR_UNEQUAL_MODULATION_PATTERN_INDEX

Specifies the unequal modulation pattern index when Unequal Modulation Enabled attribute is set to True. This attribute is applicable only when Standard attribute is set to 80211BN MIMOOFDM. The allowed modulation orders for unequal modulation are QPSK, 16-QAM, 64-QAM, 256-QAM, 1024-QAM and 4096-QAM. Modulation order of the first spatial stream is determined by the MCS Index property value. Pattern Index value determines the modulation order of remaining spatial streams with respect to the first spatial stream, as defined in the Table 38-29 of IEEE P802.11bn/D1.3.

#### Syntax

NIWLANG_ATTR_UNEQUAL_MODULATION_PATTERN_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 230 | int32 | Read/Write | N/A |

#### Remarks

You must use the following [active channel](https://www.ni.com/docs/en-US/bundle/rfmx-waveform-creator/page/configuring-active-channels-labview2.html) string formats to configure this attribute.

| Standard Attribute Value | Active Channel String Format |
| --- | --- |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU |

The default value is 0. The valid values are 0 to 3, inclusive.

Set Function: niWLANG_SetSetUnequalModulationEnabled 
 Get Function: niWLANG_GetSetUnequalModulationEnabled

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes_1gaeb3fda6cfb79fa551265a6130e6bfe53.html language=enus -->
## TOPIC 00003: NIWLANG_ATTR_CHANNELIZATION

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes_1gaeb3fda6cfb79fa551265a6130e6bfe53.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes_1gaeb3fda6cfb79fa551265a6130e6bfe53.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 320 MHz channelization value if you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211BE_OFDM or NIWLANG_VAL_STANDARD_80211BN_OFDM. As defined in section 36.3.24.2 of IEEE P802.11be/D7.0 for 320 MHz channel. 320 MHz-1 consists of 320 MHz channels with channel center

### NIWLANG_ATTR_CHANNELIZATION

Specifies the 320 MHz channelization value if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_OFDM or NIWLANG_VAL_STANDARD_80211BN_OFDM. As defined in section 36.3.24.2 of IEEE P802.11be/D7.0 for 320 MHz channel. 320 MHz-1 consists of 320 MHz channels with channel center frequency numbers 31, 95 and 159. 320 MHz-2 consists of 320 MHz channels with channel center frequency numbers 63, 127 and 191.

#### Syntax

NIWLANG_ATTR_CHANNELIZATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 231 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_CHANNEL_320MHZ_1.

Set Function: niWLANG_SetChannelization 
 Get Function: niWLANG_GetChannelization

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_CHANNEL_320MHZ_1 | 0 (0x0) | 320 MHz channel with channel center frequency numbered 31, 95, and 15. |
| NIWLANG_VAL_CHANNEL_320MHZ_2 | 1 (0x1) | 320 MHz channel with channel center frequency numbered 63, 127, and 191. |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gac7baab0383e3bb3fe3b3f3ce020ecc13.html language=enus -->
## TOPIC 00004: NIWLANG_ATTR_SIG_COMPRESSION_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gac7baab0383e3bb3fe3b3f3ce020ecc13.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gac7baab0383e3bb3fe3b3f3ce020ecc13.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the generated 802.11be and 802.11bn signal is a non-OFDMA signal or not. SyntaxNIWLANG_ATTR_SIG_COMPRESSION_ENABLEDNumeric ValueData TypeAccessApplies To213int32Read/WriteN/ARemarks The default value is NIWLANG_VAL_SIG_COMPRESSION_ENABLED_TRUE.Set Function: niWLANG_SetSIGCompressio

### NIWLANG_ATTR_SIG_COMPRESSION_ENABLED

Specifies whether the generated 802.11be and 802.11bn signal is a non-OFDMA signal or not.

#### Syntax

NIWLANG_ATTR_SIG_COMPRESSION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 213 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_SIG_COMPRESSION_ENABLED_TRUE.

Set Function: niWLANG_SetSIGCompressionEnabled 
 Get Function: niWLANG_GetSIGCompressionEnabled

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_SIG_COMPRESSION_ENABLED_FALSE | 0 (0x0) | Disables SIG compression. |
| NIWLANG_VAL_SIG_COMPRESSION_ENABLED_TRUE | 1 (0x1) | Enables SIG compression. |

Parent topic:

Data Rate and Frame Format

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gad906cfe9d11d38ce2098ef375d230974.html language=enus -->
## TOPIC 00005: NIWLANG_ATTR_SIG_MCS_INDEX

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gad906cfe9d11d38ce2098ef375d230974.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gad906cfe9d11d38ce2098ef375d230974.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the modulation and coding scheme (MCS) index of the SIG field of 802.11be and 802.11bn signal when you set the NIWLANG_ATTR_PPDU_TYPE attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU. SyntaxNIWLANG_ATTR_SIG_MCS_INDEXNumeric ValueData TypeAccessApplies To212int32Read/WriteN/ARemarks

### NIWLANG_ATTR_SIG_MCS_INDEX

Specifies the value of the modulation and coding scheme (MCS) index of the SIG field of 802.11be and 802.11bn signal when you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU.

#### Syntax

NIWLANG_ATTR_SIG_MCS_INDEX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 212 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. The valid values are 0 to 3, inclusive.

Set Function: niWLANG_SetSIGmcsIndex 
 Get Function: niWLANG_GetSIGmcsIndex

Parent topic:

Data Rate and Frame Format

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__phase__rotation_1ga63afb99afc74ec53e5154d9023bd0487.html language=enus -->
## TOPIC 00006: NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_2

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__phase__rotation_1ga63afb99afc74ec53e5154d9023bd0487.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__phase__rotation_1ga63afb99afc74ec53e5154d9023bd0487.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This attribute is valid only for 802.11be or 802.11bn and 320 MHz

### NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_2

Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This attribute is valid only for 802.11be or 802.11bn and 320 MHz bandwidth.

#### Syntax

NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_2

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 215 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_2_MINUS_ONE.

Set Function: niWLANG_SetPhaseRotationCoefficient2 
 Get Function: niWLANG_GetPhaseRotationCoefficient2

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_2_PLUS_ONE | 0 (0x0) | Specifies that phase rotation coefficient 2 is +1. |
| NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_2_MINUS_ONE | 1 (0x1) | Specifies that phase rotation coefficient 2 is -1. |

Parent topic:

Phase Rotation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__phase__rotation_1ga8c31dc6f96405a9a3143ea66ff0c27f3.html language=enus -->
## TOPIC 00007: NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_1

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__phase__rotation_1ga8c31dc6f96405a9a3143ea66ff0c27f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__phase__rotation_1ga8c31dc6f96405a9a3143ea66ff0c27f3.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This attribute is valid only for 802.11be or 802.11bn and 320 MHz

### NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_1

Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This attribute is valid only for 802.11be or 802.11bn and 320 MHz bandwidth.

#### Syntax

NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_1

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 214 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_ATTR_PHASE_ROTATION_COEFFICIENT_1_PLUS_ONE.

Set Function: niWLANG_SetPhaseRotationCoefficient1 
 Get Function: niWLANG_GetPhaseRotationCoefficient1

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_1_PLUS_ONE | 0 (0x0) | Specifies that phase rotation coefficient 1 is +1. |
| NIWLANG_VAL_PHASE_ROTATION_COEFFICIENT_1_MINUS_ONE | 1 (0x1) | Specifies that phase rotation coefficient 1 is -1. |

Parent topic:

Phase Rotation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__preamble__puncturing.html language=enus -->
## TOPIC 00008: Preamble Puncturing

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__preamble__puncturing.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format__preamble__puncturing.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIWLANG_ATTR_PREAMBLE_PUNCTURING_ENABLEDSpecifies whether to enable the preamble puncturing (channel puncturing) on 802.11ax MU PPDU, 802.11be MU PPDU and 802.11bn MU PPDU signals. Preamble puncturing is valid only when you set the NIWLANG_ATTR_CHANNEL_BANDWIDTH

### Preamble Puncturing

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_PREAMBLE_PUNCTURING_ENABLED | Specifies whether to enable the preamble puncturing (channel puncturing) on 802.11ax MU PPDU, 802.11be MU PPDU and 802.11bn MU PPDU signals. Preamble puncturing is valid only when you set the NIWLANG_ATTR_CHANNEL_BANDWIDTH attribute to 80 MHz, 160 MHz, or 320 MHz. |
| NIWLANG_ATTR_PREAMBLE_PUNCTURING_MASK | Specifies the 20 MHz sub-channels to be punctured in the 802.11ax MU PPDU, 802.11be MU PPDU signals and 802.11bn MU PPDU signals when preamble puncturing is enabled. The mask value specified here is a binary mask represented as an integer, where bit '0' represents the punctured sub-channel. |
| NIWLANG_ATTR_PRIMARY_20MHZ_CHANNEL_INDEX | Specifies the index of the primary 20 MHz sub-channel in the channel bandwidth. This attribute along with the puncturing information defines the mode of puncturing. |

#### Attachments

None

Parent topic:

Data Rate and Frame Format

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__impairments_1ga3d82f8dbba9b3689a500ca7d7adf5f83.html language=enus -->
## TOPIC 00009: NIWLANG_ATTR_CARRIER_FREQUENCY_OFFSET

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__impairments_1ga3d82f8dbba9b3689a500ca7d7adf5f83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__impairments_1ga3d82f8dbba9b3689a500ca7d7adf5f83.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset in the center frequency of the complex baseband signal from the Carrier Frequency. This value is expressed in Hz. SyntaxNIWLANG_ATTR_CARRIER_FREQUENCY_OFFSETNumeric ValueData TypeAccessApplies To20float64Read/WriteN/ARemarks You must use the following active channel string forma

### NIWLANG_ATTR_CARRIER_FREQUENCY_OFFSET

Specifies the offset in the center frequency of the complex baseband signal from the Carrier Frequency. This value is expressed in Hz.

#### Syntax

NIWLANG_ATTR_CARRIER_FREQUENCY_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 20 | float64 | Read/Write | N/A |

#### Remarks

You must use the following [active channel](https://www.ni.com/docs/en-US/bundle/rfmx-waveform-creator/page/configuring-active-channels-labview2.html) string formats to configure this attribute.

| Standard Attribute Attribute | Active Channel String Format |
| --- | --- |
| 80211AC MIMOOFDM, 80211AF MIMOOFDM | "segmentx" |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM, 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211AF MIMOOFDM | "" (empty string) |
| 80211AX MIMOOFDM | "segmentx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_MU_PPDU |
| 80211AX MIMOOFDM | "[userx]/segmenty", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |
| 80211BE MIMOOFDM | "" (empty string), if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU |
| 80211BE MIMOOFDM | "[userx]", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_ELR_PPDU |
| 80211BN MIMOOFDM | "[userx]", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |

The default value is 0. Valid value is -(1/2) * IQ Rate to (1/2) * IQ Rate, inclusive, where IQ Rate is the value of the [NIWLANG_ATTR_IQ_RATE](group____root__ni_w_l_a_n_generation__attributes__hardware__settings__recommended__settings_1gaed346ba78dbf6422e0a239e3ca5d81f7.html) attribute.

Set Function: niWLANG_SetCarrierFrequencyOffset 
 Get Function: niWLANG_GetCarrierFrequencyOffset

Parent topic:

Impairments

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments_1ga789ce061bbbfdc10d32a554e140bce77.html language=enus -->
## TOPIC 00010: NIWLANG_ATTR_IQ_GAIN_IMBALANCE

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments_1ga789ce061bbbfdc10d32a554e140bce77.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments_1ga789ce061bbbfdc10d32a554e140bce77.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of the mean amplitude of the in-phase (I) signal to the mean amplitude of the quadrature-phase (Q) signal. This value is expressed in dB. SyntaxNIWLANG_ATTR_IQ_GAIN_IMBALANCENumeric ValueData TypeAccessApplies To21float64Read/WriteN/ARemarks If you set this attribute to a large v

### NIWLANG_ATTR_IQ_GAIN_IMBALANCE

Specifies the ratio of the mean amplitude of the in-phase (I) signal to the mean amplitude of the quadrature-phase (Q) signal. This value is expressed in dB.

#### Syntax

NIWLANG_ATTR_IQ_GAIN_IMBALANCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 21 | float64 | Read/Write | N/A |

#### Remarks

If you set this attribute to a large value, there may be loss of dynamic range at the digital-to-analog converter (DAC).

I/Q gain imbalance follows the definition shown in the following equation:

I' = I - (gamma) * sin(phi) * Q + I0 
 Q' = (gamma) * cos(phi) * Q + Q0 
 where 
 gamma = 10^(I/Q gain imbalance/20) 
 phi is the quadrature skew 
 I is the in-phase component of the waveform before applying impairments 
 Q is the quadrature component of the waveform before applying impairments 
 I' is the in-phase component of the waveform after applying impairments 
 Q' is the quadrature component of the waveform before applying impairments 
 I0 is the (RMS value of I) * (I DC Offset)/100 
 Q0 is the (RMS value of Q) * (Q DC Offset)/100

| Standard Attribute Attribute | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx" |
| 80211AC MIMOOFDM, 80211AF MIMOOFDM | "segmentx/channely" |
| 80211AX MIMOOFDM | "segmentx/channely", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_MU_PPDU |
| 80211AX MIMOOFDM | "[userx]/segmenty/channelz", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |
| 80211BE MIMOOFDM | "channelx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU |
| 80211BE MIMOOFDM | "[userx]/channely", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |
| 80211BN MIMOOFDM | "channelx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_ELR_PPDU |
| 80211BN MIMOOFDM | "[userx]/channely", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |

The default value is 0. Valid values are -6 to +6, inclusive.

Set Function: niWLANG_SetIQGainImbalance 
 Get Function: niWLANG_GetIQGainImbalance

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments_1gac05f4819168107f00ca0302919070fe7.html language=enus -->
## TOPIC 00011: NIWLANG_ATTR_ALL_IQ_IMPAIRMENTS_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments_1gac05f4819168107f00ca0302919070fe7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments_1gac05f4819168107f00ca0302919070fe7.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply I/Q impairments such as I DC offset, Q DC offset, quadrature skew, and I/Q gain imbalance to the waveform. SyntaxNIWLANG_ATTR_ALL_IQ_IMPAIRMENTS_ENABLEDNumeric ValueData TypeAccessApplies To96int32Read/WriteN/ARemarks The default value is NIWLANG_VAL_TRUE.Set Function: niW

### NIWLANG_ATTR_ALL_IQ_IMPAIRMENTS_ENABLED

Specifies whether to apply I/Q impairments such as I DC offset, Q DC offset, quadrature skew, and I/Q gain imbalance to the waveform.

#### Syntax

NIWLANG_ATTR_ALL_IQ_IMPAIRMENTS_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 96 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetAllIQImpairmentsEnabled 
 Get Function: niWLANG_GetAllIQImpairmentsEnabled

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments__niwlangquadratureskew.html language=enus -->
## TOPIC 00012: NIWLANG_QUADRATURE_SKEW

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments__niwlangquadratureskew.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments__niwlangquadratureskew.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIWLANG_ATTR_TIMING_SKEWSpecifies the difference between the sampling instants of I and Q streams. This value is expressed in seconds. AttachmentsNone

### NIWLANG_QUADRATURE_SKEW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_TIMING_SKEW | Specifies the difference between the sampling instants of I and Q streams. This value is expressed in seconds. |

#### Attachments

None

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments__niwlangquadratureskew_1ga5d507cbf84906591819e109d98b31e1d.html language=enus -->
## TOPIC 00013: NIWLANG_ATTR_TIMING_SKEW

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments__niwlangquadratureskew_1ga5d507cbf84906591819e109d98b31e1d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__impairments__iq__impairments__niwlangquadratureskew_1ga5d507cbf84906591819e109d98b31e1d.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the difference between the sampling instants of I and Q streams. This value is expressed in seconds. SyntaxNIWLANG_ATTR_TIMING_SKEWNumeric ValueData TypeAccessApplies To79float64Read/WriteN/ARemarksStandard Attribute AttributeActive Channel String Format80211A/G OFDM, 80211J OFDM, 80211P O

### NIWLANG_ATTR_TIMING_SKEW

Specifies the difference between the sampling instants of I and Q streams. This value is expressed in seconds.

#### Syntax

NIWLANG_ATTR_TIMING_SKEW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 79 | float64 | Read/Write | N/A |

#### Remarks

| Standard Attribute Attribute | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx" |
| 80211AC MIMOOFDM, 80211AF MIMOOFDM | "segmentx/channely" |
| 80211AX MIMOOFDM | "segmentx/channely", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_MU_PPDU |
| 80211AX MIMOOFDM | "[userx]/segmenty/channelz", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |
| 80211BE MIMOOFDM | "channelx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU |
| 80211BE MIMOOFDM | "[userx]/channely", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |
| 80211BN MIMOOFDM | "channelx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_ELR_PPDU |
| 80211BN MIMOOFDM | "[userx]/channely", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU (userx is optional if you want to apply to all users) |

The default value is 0. Valid values are -1 microsecond to 1 microsecond, inclusive.

Set Function: niWLANG_SetTimingSkew 
 Get Function: niWLANG_GetTimingSkew

Parent topic:

NIWLANG_QUADRATURE_SKEW

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo.html language=enus -->
## TOPIC 00014: MIMO

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIWLANG_ATTR_CYCLIC_TIME_SHIFTSpecifies the value of Cyclic Time Shift applied to each Transmit Chain signals. NIWLANG_ATTR_MAPPING_MATRIX_TYPESpecifies the mapping matrix type for mapping space-time streams to transmit channels as defined in section 20.3.11.10.

### MIMO

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_CYCLIC_TIME_SHIFT | Specifies the value of Cyclic Time Shift applied to each Transmit Chain signals. |
| NIWLANG_ATTR_MAPPING_MATRIX_TYPE | Specifies the mapping matrix type for mapping space-time streams to transmit channels as defined in section 20.3.11.10.1 of IEEE Standard 802.11n-2009. |
| NIWLANG_ATTR_MULTI_SEGMENT_GENERATION_MODE | Specifies whether to use a single generator or two generators for each channel of a multi-segment (80+80) MHz 802.11ac signal. This attribute is applicable when you set the NIWLANG_ATTR_NUMBER_OF_SEGMENTS attribute to 2 and the channel bandwidth is 80 MHz. When you set this attribute to NIWLANG_VAL_SINGLE_GENERATOR, you have to specify the value of the NIWLANG_ATTR_CARRIER_FREQUENCY attribute for both the segments. |
| NIWLANG_ATTR_MU_MIMO_LTF_MODE_ENABLED | Specifies whether the HE-LTF sequence corresponding to each space time stream is masked by distinct orthogonal code, if the NIWLANG_ATTR_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM and the NIWLANG_ATTR_PPDU_TYPE attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU. |
| NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS | Specifies the number of extension spatial streams (N_ESS) as defined in section 20.3.9.4.6 of IEEE Standard 802.11n-2009. |
| NIWLANG_ATTR_NUMBER_OF_LTF_SYMBOLS | Specifies the number of HE-LTF symbols in the transmitted 802.11ax signal when you set the NIWLANG_ATTR_PPDU_TYPE attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and specifies the number of EHT-LTF symbols in the transmitted 802.11be signal. |
| NIWLANG_ATTR_NUMBER_OF_SEGMENTS | Specifies the number of frequency segments for 802.11ac or 802.11ax signals. |
| NIWLANG_ATTR_NUMBER_OF_SPACE_TIME_STREAMS | Specifies the number of space-time streams into which the data is divided. |
| NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS | Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of IEEE Standard 802.11n-2009. |
| NIWLANG_ATTR_NUMBER_OF_USERS | Specifies the number of users in a multi-user (MU) physical layer convergence procedure (PLCP) protocol data unit (PPDU). The default value is 1. |
| NIWLANG_ATTR_SPACE_TIME_STREAM_OFFSET | Specifies the per user space time stream offset which is used for 802.11ax, 802.11be and 802.11bn Trigger-Based PPDU generation. |
| NIWLANG_ATTR_SPATIAL_MAPPING_MODE | Specifies whether the spatial mapping is created from a single global matrix or per user. This attribute is applicable, only when you set the NIWLANG_ATTR_PPDU_TYPE attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU. |
| NIWLANG_ATTR_STBC_ALL_STREAMS_ENABLED | Specifies whether space-time block coding (STBC) is performed at the transmitter when the NIWLANG_ATTR_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM. Whenever STBC is performed, the number of space-time streams is equal to two times the number of spatial streams. |
| NIWLANG_ATTR_STBC_INDEX | Specifies the difference between the number of space-time streams and the number of spatial streams, as defined in section 20.3.9.4.3 of IEEE Standard 802.11n-2009. the WLAN Generation derives the number of spatial streams from the specified value of the NIWLANG_ATTR_MCS_INDEX attribute. Different space-time coding schemes are defined in section 20.3.11.8.1 of IEEE Standard 802.11n-2009. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3a4d24ed3af49242d0ca3e6cfaa5678b.html language=enus -->
## TOPIC 00015: NIWLANG_ATTR_CYCLIC_TIME_SHIFT

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3a4d24ed3af49242d0ca3e6cfaa5678b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3a4d24ed3af49242d0ca3e6cfaa5678b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of Cyclic Time Shift applied to each Transmit Chain signals. SyntaxNIWLANG_ATTR_CYCLIC_TIME_SHIFTNumeric ValueData TypeAccessApplies To217float64Read/WriteN/ARemarks This attribute is applicable only if the NIWLANG_ATTR_MAPPING_MATRIX_TYPE attribute is set to NIWLANG_VAL_MAPPING_

### NIWLANG_ATTR_CYCLIC_TIME_SHIFT

Specifies the value of Cyclic Time Shift applied to each Transmit Chain signals.

#### Syntax

NIWLANG_ATTR_CYCLIC_TIME_SHIFT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 217 | float64 | Read/Write | N/A |

#### Remarks

This attribute is applicable only if the [NIWLANG_ATTR_MAPPING_MATRIX_TYPE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html) attribute is set to NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT, NIWLANG_VAL_MAPPING_MATRIX_TYPE_HADAMARD or NIWLANG_VAL_MAPPING_MATRIX_TYPE_FOURIER and standard is set to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, and [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, NIWLANG_VAL_PPDU_TYPE_MU_PPDU, NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU, or NIWLANG_VAL_PPDU_TYPE_ELR_PPDU.

This attribute is not applicable if [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) is set to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and MNIWLANG_MAPPING_MATRIX_TYPE is set to NIWLANG_VAL_MAPPING_MATRIX_TYPE_USER_SPECIFIC.

The default value is 0. The supported range for this attribute is -32 us to 32 us. You must use Active Channel String as Channelx for all standards to set this attribute.

Set Function: niWLANG_SetCyclicTimeShift 
 Get Function: niWLANG_GetCyclicTimeShift

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3b823e4b1a3cbf3021db793a19d9a8ad.html language=enus -->
## TOPIC 00016: NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3b823e4b1a3cbf3021db793a19d9a8ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3b823e4b1a3cbf3021db793a19d9a8ad.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of IEEE Standard 802.11n-2009. SyntaxNIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELSNumeric ValueData TypeAccessApplies To47int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_MAPPING

### NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS

Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of IEEE Standard 802.11n-2009.

#### Syntax

NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 47 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_MAPPING_MATRIX_TYPE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html) attribute to NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT, the number of transmit channels must be equal to the number of space-time streams. If you set the [NIWLANG_ATTR_MAPPING_MATRIX_TYPE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html) attribute to values other than NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT, the number of transmit channels must be greater than or equal to the sum of the number of space-time streams and the [NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS](group____root__ni_w_l_a_n_generation__attributes__mimo_1gaf6714a8f66c7ea52ec872c6e43aeb940.html) attribute.

the WLAN Generation defines the number of space-time streams using the [NIWLANG_ATTR_MCS_INDEX](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga5ff81d7f7fae518b786a3bc909ef372c.html) attribute and [NIWLANG_ATTR_STBC_INDEX](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga6f375c08a44794251d8f09eed2f48ad2.html) attribute, as specified in IEEE Standard 802.11n-2009.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, and the [NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3b823e4b1a3cbf3021db793a19d9a8ad.html) attribute to greater than one, the same waveform is generated on multiple RFSG devices inside the [niWLANG_RFSGCreateAndDownloadMIMOWaveforms](group____root__ni_w_l_a_n_generation__functions__rfsg__database__retrieve_1ga649cf1856a36effe23b5ba140fe217e9.html) function.

The default value is 1. If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, the valid values are 1 to 4, inclusive. If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to any other value, the valid values are 1 to 8, inclusive.

Set Function: niWLANG_SetNumberOfTransmitChannels 
 Get Function: niWLANG_GetNumberOfTransmitChannels

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html language=enus -->
## TOPIC 00017: NIWLANG_ATTR_MAPPING_MATRIX_TYPE

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mapping matrix type for mapping space-time streams to transmit channels as defined in section 20.3.11.10.1 of IEEE Standard 802.11n-2009. SyntaxNIWLANG_ATTR_MAPPING_MATRIX_TYPENumeric ValueData TypeAccessApplies To55int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_MAPPING_MATRIX_T

### NIWLANG_ATTR_MAPPING_MATRIX_TYPE

Specifies the mapping matrix type for mapping space-time streams to transmit channels as defined in section 20.3.11.10.1 of IEEE Standard 802.11n-2009.

#### Syntax

NIWLANG_ATTR_MAPPING_MATRIX_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 55 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_MAPPING_MATRIX_TYPE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html) attribute to values other than NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT, the number of transmit channels must be greater than or equal to the sum of the number of space-time streams and the [NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS](group____root__ni_w_l_a_n_generation__attributes__mimo_1gaf6714a8f66c7ea52ec872c6e43aeb940.html) attribute if the standard is set to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM.

The default value is NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT. If the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute is set to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_STANDARD_TRIGGER_BASED_PPDU then N-STS value is dependent on the [NIWLANG_ATTR_SPATIAL_MAPPING_MODE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga6dd3560fa0e5c8ad967ffa942a6c3b04.html) attribute. If you set the [NIWLANG_ATTR_SPATIAL_MAPPING_MODE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga6dd3560fa0e5c8ad967ffa942a6c3b04.html) attribute to NIWLANG_VAL_COMMON, the N STS value is the maximum number of space time streams across Resource Units (RUs). If you set the [NIWLANG_ATTR_SPATIAL_MAPPING_MODE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga6dd3560fa0e5c8ad967ffa942a6c3b04.html) attribute to NIWLANG_VAL_USER_SPECIFIC, the N STS value is the number of space time streams for the specified user. You must use the following active channel string formats when [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute is set to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_STANDARD_TRIGGER_BASED_PPDU. If you set the [NIWLANG_ATTR_SPATIAL_MAPPING_MODE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga6dd3560fa0e5c8ad967ffa942a6c3b04.html) attribute to NIWLANG_VAL_COMMON, the active channel string format is an empty string. If you set the [NIWLANG_ATTR_SPATIAL_MAPPING_MODE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga6dd3560fa0e5c8ad967ffa942a6c3b04.html) attribute to NIWLANG_VAL_USER_SPECIFIC, the active channel string format is 'userx'.

Set Function: niWLANG_SetMappingMatrixType 
 Get Function: niWLANG_GetMappingMatrixType

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT | 0 (0x0) | Refer to the Mapping Matrix Type Values topic. |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_HADAMARD | 1 (0x1) | Refer to the Mapping Matrix Type Values topic. |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_FOURIER | 2 (0x2) | Refer to the Mapping Matrix Type Values topic. |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_USER_DEFINED | 3 (0x3) | Refer to the Mapping Matrix Type Values topic. |

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo_1gaa46830e714c5e984fc2a0dc35d85168b.html language=enus -->
## TOPIC 00018: NIWLANG_ATTR_SPACE_TIME_STREAM_OFFSET

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo_1gaa46830e714c5e984fc2a0dc35d85168b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo_1gaa46830e714c5e984fc2a0dc35d85168b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the per user space time stream offset which is used for 802.11ax, 802.11be and 802.11bn Trigger-Based PPDU generation. SyntaxNIWLANG_ATTR_SPACE_TIME_STREAM_OFFSETNumeric ValueData TypeAccessApplies To187int32Read/WriteN/ARemarks The default value is 0.You must use the following active chan

### NIWLANG_ATTR_SPACE_TIME_STREAM_OFFSET

Specifies the per user space time stream offset which is used for 802.11ax, 802.11be and 802.11bn Trigger-Based PPDU generation.

#### Syntax

NIWLANG_ATTR_SPACE_TIME_STREAM_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 187 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0.

You must use the following active channel string formats to set this attribute. If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU, use 'userx' as the active channel string format to set this attribute.

Set Function: niWLANG_SetSpaceTimeStreamOffset 
 Get Function: niWLANG_GetSpaceTimeStreamOffset

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo_1gadc6586f6f262c3804ec369961c5d4c29.html language=enus -->
## TOPIC 00019: NIWLANG_ATTR_MU_MIMO_LTF_MODE_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo_1gadc6586f6f262c3804ec369961c5d4c29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo_1gadc6586f6f262c3804ec369961c5d4c29.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the HE-LTF sequence corresponding to each space time stream is masked by distinct orthogonal code, if the NIWLANG_ATTR_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM and the NIWLANG_ATTR_PPDU_TYPE attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU. SyntaxNIW

### NIWLANG_ATTR_MU_MIMO_LTF_MODE_ENABLED

Specifies whether the HE-LTF sequence corresponding to each space time stream is masked by distinct orthogonal code, if the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute is set to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU.

#### Syntax

NIWLANG_ATTR_MU_MIMO_LTF_MODE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 186 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetMUMIMOLTFModeEnabled 
 Get Function: niWLANG_GetMUMIMOLTFModeEnabled

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo_1gae59558e9d398123460da4fd6f6807fed.html language=enus -->
## TOPIC 00020: NIWLANG_ATTR_NUMBER_OF_LTF_SYMBOLS

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo_1gae59558e9d398123460da4fd6f6807fed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo_1gae59558e9d398123460da4fd6f6807fed.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of HE-LTF symbols in the transmitted 802.11ax signal when you set the NIWLANG_ATTR_PPDU_TYPE attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and specifies the number of EHT-LTF symbols in the transmitted 802.11be signal. SyntaxNIWLANG_ATTR_NUMBER_OF_LTF_SYMBOLSNumeric Valu

### NIWLANG_ATTR_NUMBER_OF_LTF_SYMBOLS

Specifies the number of HE-LTF symbols in the transmitted 802.11ax signal when you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and specifies the number of EHT-LTF symbols in the transmitted 802.11be signal.

#### Syntax

NIWLANG_ATTR_NUMBER_OF_LTF_SYMBOLS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 165 | int32 | Read/Write | N/A |

#### Remarks

The default value is -1, which indicates that the value is derived from the maximum index of space time streams across users. The valid values for this attribute are as follows:

| Standard Attribute Value | Valid Values(Inclusive) |
| --- | --- |
| 80211AX MIMOOFDM | -1, 1, 2, 4, 6, and 8 |
| 80211BE MIMOOFDM | -1, 1, 2, 4, and 8, if you set the NIWLANG_ATTR_SIG_COMPRESSION_ENABLED attribute to NIWLANG_VAL_SIG_COMPRESSION_ENABLED_TRUE |
| 80211BE MIMOOFDM | -1, 1, 2, 4, 6, and 8, if you set the NIWLANG_ATTR_SIG_COMPRESSION_ENABLED attribute to NIWLANG_VAL_SIG_COMPRESSION_ENABLED_FALSE |
| 80211BN MIMOOFDM | -1, 1, 2, 4, and 8, if you set the NIWLANG_ATTR_SIG_COMPRESSION_ENABLED attribute to NIWLANG_VAL_SIG_COMPRESSION_ENABLED_TRUE |
| 80211BN MIMOOFDM | -1, 1, 2, 4, 6, and 8, if you set the NIWLANG_ATTR_SIG_COMPRESSION_ENABLED attribute to NIWLANG_VAL_SIG_COMPRESSION_ENABLED_FALSE |
| 80211BN MIMOOFDM | -1, 2, if you set the ppdu type attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU |

Set Function: niWLANG_SetNumberOfLTFSymbols 
 Get Function: niWLANG_GetNumberOfLTFSymbols

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__mimo_1gaf6714a8f66c7ea52ec872c6e43aeb940.html language=enus -->
## TOPIC 00021: NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__mimo_1gaf6714a8f66c7ea52ec872c6e43aeb940.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__mimo_1gaf6714a8f66c7ea52ec872c6e43aeb940.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of extension spatial streams (N_ESS) as defined in section 20.3.9.4.6 of IEEE Standard 802.11n-2009. SyntaxNIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMSNumeric ValueData TypeAccessApplies To46int32Read/WriteN/ARemarks The value of N_ESS follows the definition shown in the fol

### NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS

Specifies the number of extension spatial streams (N_ESS) as defined in section 20.3.9.4.6 of IEEE Standard 802.11n-2009.

#### Syntax

NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 46 | int32 | Read/Write | N/A |

#### Remarks

The value of N_ESS follows the definition shown in the following equation: 
 N_STS + N_ESS is less than or equal to N_Tx.

where N_STS is the number of space-time streams and is determined by the MCS index and STBC index. N_Tx is the number of transmit channels specified by the [NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga3b823e4b1a3cbf3021db793a19d9a8ad.html) attribute.

N_TX must be greater than or equal to N_STS.

The default value is 0. Valid values are 0 to 3, inclusive.

Set Function: niWLANG_SetNumberOfExtensionSpatialStreams 
 Get Function: niWLANG_GetNumberOfExtensionSpatialStreams

Parent topic:

MIMO

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__obsolete_1ga51c6d692b75fd9232d68a7dcd59f390a.html language=enus -->
## TOPIC 00022: NIWLANG_ATTR_PEAK_TO_AVERAGE_POWER_RATIO

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__obsolete_1ga51c6d692b75fd9232d68a7dcd59f390a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__obsolete_1ga51c6d692b75fd9232d68a7dcd59f390a.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak-to-average power ratio (PAPR)of the output complex waveform. This value is expressed in dB. SyntaxNIWLANG_ATTR_PEAK_TO_AVERAGE_POWER_RATIONumeric ValueData TypeAccessApplies To30float64Read/WriteN/ARemarks This attribute is available only if you set the compatibilityVersion paramete

### NIWLANG_ATTR_PEAK_TO_AVERAGE_POWER_RATIO

Returns the peak-to-average power ratio (PAPR)of the output complex waveform. This value is expressed in dB.

#### Syntax

NIWLANG_ATTR_PEAK_TO_AVERAGE_POWER_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 30 | float64 | Read/Write | N/A |

#### Remarks

This attribute is available only if you set the compatibilityVersion parameter of the [niWLANG_OpenSession](group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html) function to NIWLANG_VAL_COMPATIBILITY_VERSION_010000.

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__obsolete_1gad41c6a273770da3a3e4a2ce993b82da3.html language=enus -->
## TOPIC 00023: NIWLANG_ATTR_WAVEFORM_SCALING_FACTOR

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__obsolete_1gad41c6a273770da3a3e4a2ce993b82da3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__obsolete_1gad41c6a273770da3a3e4a2ce993b82da3.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the scaling factor for the waveform, as a percentage of the maximum sample magnitude, to reduce the overshoot associated with the digital-to-analog converter (DAC) interpolation filter and other finite impulse response (FIR) filters in the NI RF vector signal generators. SyntaxNIWLANG_ATTR

### NIWLANG_ATTR_WAVEFORM_SCALING_FACTOR

Specifies the scaling factor for the waveform, as a percentage of the maximum sample magnitude, to reduce the overshoot associated with the digital-to-analog converter (DAC) interpolation filter and other finite impulse response (FIR) filters in the NI RF vector signal generators.

#### Syntax

NIWLANG_ATTR_WAVEFORM_SCALING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 36 | float64 | Read/Write | N/A |

#### Remarks

This attribute is available only if you set the compatibilityVersion parameter of the [niWLANG_OpenSession](group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html) function to NIWLANG_VAL_COMPATIBILITY_VERSION_010000.

The default value is 99. Valid values are 1 to 100, inclusive. You can reduce the value to avoid clipping, but you may lose dynamic range.

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__obsolete_1gadd4a1710b6887f73d69f6f18374b383d.html language=enus -->
## TOPIC 00024: NIWLANG_ATTR_POWER_LEVEL

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__obsolete_1gadd4a1710b6887f73d69f6f18374b383d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__obsolete_1gadd4a1710b6887f73d69f6f18374b383d.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the average power level of the active portion of the burst for signal generation. This value is expressed in dBm. The active portion of the burst is the WLAN packet excluding the interframe spacing. SyntaxNIWLANG_ATTR_POWER_LEVELNumeric ValueData TypeAccessApplies To1float64Read/WriteN/ARe

### NIWLANG_ATTR_POWER_LEVEL

Specifies the average power level of the active portion of the burst for signal generation. This value is expressed in dBm. The active portion of the burst is the WLAN packet excluding the interframe spacing.

#### Syntax

NIWLANG_ATTR_POWER_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1 | float64 | Read/Write | N/A |

#### Remarks

This attribute is available only if you set the compatibilityVersion parameter of the [niWLANG_OpenSession](group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html) function to NIWLANG_VAL_COMPATIBILITY_VERSION_010000 or NIWLANG_VAL_COMPATIBILITY_VERSION_020000.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, use an active channel string to configure this attribute. Refer to the Configuring Active Channels (LabWindows/CVI) help topic for more information about configuring active channels.

The default value is -10.

Set Function: niWLANG_SetPowerLevel

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload.html language=enus -->
## TOPIC 00025: Payload

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsMAC HeaderTrigger FrameGroup membersNameDescriptionNIWLANG_ATTR_AMPDU_ENABLEDSpecifies whether all medium access control (MAC) protocol data units (MPDUs) are transmitted as aggregate-MPDU (A-MPDU). NIWLANG_ATTR_AUTO_PAYLOAD_DATA_LENGTH_MODESpecifies whether to use the value specified in NIWLA

### Payload

#### Groups

- MAC Header
- Trigger Frame

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_AMPDU_ENABLED | Specifies whether all medium access control (MAC) protocol data units (MPDUs) are transmitted as aggregate-MPDU (A-MPDU). |
| NIWLANG_ATTR_AUTO_PAYLOAD_DATA_LENGTH_MODE | Specifies whether to use the value specified in NIWLANG_ATTR_PAYLOAD_DATA_LENGTH attribute or automatically compute the data length of the MPDUs in an AMPDU. The default value is NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_DISABLED. |
| NIWLANG_ATTR_MAC_FCS_ENABLED | Specifies whether to enable the medium access control (MAC) frame check sequence (FCS), as defined in section 7.1.2 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. |
| NIWLANG_ATTR_MAC_FRAME_FORMAT | Specifies whether the medium access control (MAC) frame is long or short. |
| NIWLANG_ATTR_MPDU_LENGTH | Returns the length of the medium access control (MAC) protocol data unit (MPDU). This value is expressed in bytes. An MPDU comprises of a MAC header, a frame body, and a frame check sequence (FCS). The NIWLANG_ATTR_MPDU_LENGTH attribute is the sum of the length of MAC header, the value of the NIWLANG_ATTR_PAYLOAD_DATA_LENGTH attribute, and the length of FCS, which is four bytes. If you disable the NIWLANG_ATTR_MAC_HEADER_ENABLED and NIWLANG_ATTR_MAC_FCS_ENABLED attributes, the lengths of MAC header and FCS are zero. |
| NIWLANG_ATTR_NUMBER_OF_DATA_SYMBOLS | Returns the number of symbols in the data portion of the generated WLAN frame. Symbol refers to the chip if the NIWLANG_ATTR_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211BG_DSSS, and the symbol refers to the OFDM symbol for other values of the NIWLANG_ATTR_STANDARD attribute. |
| NIWLANG_ATTR_PAYLOAD_AUTO_NUMBER_OF_MPDUS | Specifies whether to compute the number of MPDUs in an AMPDU of 802.11ax Trigger-Based PPDU, 802.11be Trigger-Based PPDU and 802.11bn Trigger-Based PPDU using the following frame parameters: |
| NIWLANG_ATTR_PAYLOAD_DATA_LENGTH | Specifies the length of the payload, excluding the length of the medium access control (MAC) header and frame check sequence (FCS). This value is expressed in bytes. The payload length encoded into the physical layer (PHY) header is the sum of the payload data length and the length of the MAC header and FCS. |
| NIWLANG_ATTR_PAYLOAD_DATA_TYPE | Specifies the type of payload for waveform generation. |
| NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE | Specifies the type of frame for the MPDU. |
| NIWLANG_ATTR_PAYLOAD_NUMBER_OF_MPDUS | Specifies the number of medium access control (MAC) protocol data units (MPDUs) to combine into one aggregate-MPDU (A-MPDU). |
| NIWLANG_ATTR_PAYLOAD_PN_ORDER | Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. The generated sequence is repeated (2^PN order) - 1 bits. If you set the NIWLANG_ATTR_PAYLOAD_DATA_TYPE attribute to NIWLANG_VAL_USER_DEFINED, the WLAN Generation ignores the NIWLANG_ATTR_PAYLOAD_PN_ORDER attribute. |
| NIWLANG_ATTR_PAYLOAD_PN_SEED | Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the NIWLANG_ATTR_PAYLOAD_DATA_TYPE attribute to NIWLANG_VAL_USER_DEFINED, the WLAN Generation ignores NIWLANG_ATTR_PAYLOAD_PN_SEED attribute. |
| NIWLANG_ATTR_PAYLOAD_SCRAMBLER_SEED | Specifies the initial state of the scrambler seed. |
| NIWLANG_ATTR_PAYLOAD_USER_DEFINED_BITS | Specifies a user-defined bit pattern as an array of zeros and ones. If the array length is greater than the configured payload length, the WLAN Generation uses a subset of the required length from the beginning of the array for waveform generation. If the array length is less than the configured payload length, the WLAN Generation repeats the user-defined bit pattern until the required length is achieved. If you set the NIWLANG_ATTR_PAYLOAD_DATA_TYPE attribute to NIWLANG_VAL_PN_SEQUENCE, the WLAN Generation ignores the NIWLANG_ATTR_PAYLOAD_USER_DEFINED_BITS attribute. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga0b709352374b8da6d4601cf7b3ae03ad.html language=enus -->
## TOPIC 00026: NIWLANG_ATTR_MAC_FCS_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga0b709352374b8da6d4601cf7b3ae03ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga0b709352374b8da6d4601cf7b3ae03ad.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the medium access control (MAC) frame check sequence (FCS), as defined in section 7.1.2 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 o

### NIWLANG_ATTR_MAC_FCS_ENABLED

Specifies whether to enable the medium access control (MAC) frame check sequence (FCS), as defined in section 7.1.2 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3.

#### Syntax

NIWLANG_ATTR_MAC_FCS_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 100 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetMacFCSEnabled 
 Get Function: niWLANG_GetMacFCSEnabled

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga0d7ea66bfffa1df82a181495750373e2.html language=enus -->
## TOPIC 00027: NIWLANG_ATTR_PAYLOAD_NUMBER_OF_MPDUS

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga0d7ea66bfffa1df82a181495750373e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga0d7ea66bfffa1df82a181495750373e2.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of medium access control (MAC) protocol data units (MPDUs) to combine into one aggregate-MPDU (A-MPDU). SyntaxNIWLANG_ATTR_PAYLOAD_NUMBER_OF_MPDUSNumeric ValueData TypeAccessApplies To104int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STAN

### NIWLANG_ATTR_PAYLOAD_NUMBER_OF_MPDUS

Specifies the number of medium access control (MAC) protocol data units (MPDUs) to combine into one aggregate-MPDU (A-MPDU).

#### Syntax

NIWLANG_ATTR_PAYLOAD_NUMBER_OF_MPDUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 104 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, or use 'userx' as the active channel string format if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU, or use 'userx' as the active channel string format if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx' as the active channel string format if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use 'userx' as the active channel string format if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU, or use an empty string active channel string format, if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU to configure this attribute.

the WLAN Generation ignores this attribute if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE or if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to a value other than NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM; or if you set the [NIWLANG_ATTR_NON_HT_MODULATION_MODE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gab6f2cae6784b54c7650138031537a720.html) attribute to NIWLANG_VAL_NON_HT_MODULATION_MODE_ON, or if you set the NIWLANG_VAL_AUTO_NUMBER_OF_MPDUS attribute to NIWLANG_VAL_TRUE.

The default value is 1.

Set Function: niWLANG_SetNumberOfMPDUS 
 Get Function: niWLANG_GetNumberOfMPDUS

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html language=enus -->
## TOPIC 00028: NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of frame for the MPDU. SyntaxNIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPENumeric ValueData TypeAccessApplies To188int32Read/WriteN/ARemarks You can set this attribute to NIWLANG_TRIGGER_FRAME, only if you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG

### NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE

Specifies the type of frame for the MPDU.

#### Syntax

NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 188 | int32 | Read/Write | N/A |

#### Remarks

You can set this attribute to NIWLANG_TRIGGER_FRAME, only if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211B/G_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, use an empty string active channel string format to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE, or use 'mpdux' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, use 'mpdux' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, or use 'userx/mpduy' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, or use 'mpdux' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_EXTENDED_RANGE_SU_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, 'mpdux' as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU, or use 'userx/mpduy' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_TRIGGER_BASED_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use 'userx/mpduy' as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU, an empty string as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE, and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU, or use 'mpdux' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU to configure this attribute.

The default value is NIWLANG_VAL_PAYLOAD_FRAME_TYPE_GENERAL_FRAME.

Set Function: niWLANG_SetMacFrameType 
 Get Function: niWLANG_GetMacFrameType

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga478858971f41af58ffacc712c8c6bdca.html language=enus -->
## TOPIC 00029: NIWLANG_ATTR_AUTO_PAYLOAD_DATA_LENGTH_MODE

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga478858971f41af58ffacc712c8c6bdca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga478858971f41af58ffacc712c8c6bdca.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use the value specified in NIWLANG_ATTR_PAYLOAD_DATA_LENGTH attribute or automatically compute the data length of the MPDUs in an AMPDU. The default value is NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_DISABLED. SyntaxNIWLANG_ATTR_AUTO_PAYLOAD_DATA_LENGTH_MODENumeric ValueData Typ

### NIWLANG_ATTR_AUTO_PAYLOAD_DATA_LENGTH_MODE

Specifies whether to use the value specified in [NIWLANG_ATTR_PAYLOAD_DATA_LENGTH](group____root__ni_w_l_a_n_generation__attributes__payload_1ga8541a94ece14d443b3d10f9218038042.html) attribute or automatically compute the data length of the MPDUs in an AMPDU. The default value is NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_DISABLED.

#### Syntax

NIWLANG_ATTR_AUTO_PAYLOAD_DATA_LENGTH_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 179 | int32 | Read/Write | N/A |

#### Remarks

Set Function: niWLANG_SetAutoPayloadDataLengthMode Get Function: niWLANG_GetAutoPayloadDataLengthMode

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_DISABLED | 0 (0x0) | Specifies that the WLAN Generation uses the value specified in NIWLANG_PAYLOAD_DATA_LENGTH attribute. |
| NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_L_SIG_LENGTH | 1 (0x1) | Specifies that the WLAN Generation computes the data length of the MPDUs in an AMPDU of 802.11ax, 802.11be and 802.11bn Trigger-Based PPDU using the following trigger frame parameters; NIWLANG_L_SIG_LENGTH, NIWLANG_PRE_FEC_PADDING_FACTOR, NIWLANG_PE_DISAMBIGUITY, and NIWLANG_LDPC_EXTRA_SYMBOL_SEGMENT attribute. |
| NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_FRAME_DURATION | 2 (0x2) | Specifies that the WLAN Generation computes the data length of the MPDUs in an AMPDU using the value specified in NIWLANG_FRAME_DURATION attribute. |

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga550109fdd6b4c4cd4818643a46bce153.html language=enus -->
## TOPIC 00030: NIWLANG_ATTR_PAYLOAD_DATA_TYPE

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga550109fdd6b4c4cd4818643a46bce153.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga550109fdd6b4c4cd4818643a46bce153.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of payload for waveform generation. SyntaxNIWLANG_ATTR_PAYLOAD_DATA_TYPENumeric ValueData TypeAccessApplies To7int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_8021

### NIWLANG_ATTR_PAYLOAD_DATA_TYPE

Specifies the type of payload for waveform generation.

#### Syntax

NIWLANG_ATTR_PAYLOAD_DATA_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 7 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_PN_SEQUENCE.

Set Function: niWLANG_SetPayloadDataType 
 Get Function: niWLANG_GetPayloadDataType

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html language=enus -->
## TOPIC 00031: NIWLANG_ATTR_AMPDU_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether all medium access control (MAC) protocol data units (MPDUs) are transmitted as aggregate-MPDU (A-MPDU). SyntaxNIWLANG_ATTR_AMPDU_ENABLEDNumeric ValueData TypeAccessApplies To103int32Read/WriteN/ARemarks This attribute is applicable only if you set the NIWLANG_ATTR_STANDARD attribut

### NIWLANG_ATTR_AMPDU_ENABLED

Specifies whether all medium access control (MAC) protocol data units (MPDUs) are transmitted as aggregate-MPDU (A-MPDU).

#### Syntax

NIWLANG_ATTR_AMPDU_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 103 | int32 | Read/Write | N/A |

#### Remarks

This attribute is applicable only if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM and the [NIWLANG_ATTR_NON_HT_MODULATION_MODE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1gab6f2cae6784b54c7650138031537a720.html) attribute to NIWLANG_VAL_NON_HT_MODULATION_MODE_OFF.

The default value is NIWLANG_VAL_TRUE, if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM.

The default value is NIWLANG_VAL_TRUE, if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM.

Set Function: niWLANG_SetAMPDUEnabled 
 Get Function: niWLANG_GetAMPDUEnabled

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga75496a7ac1fa5d1999943be865e68f7e.html language=enus -->
## TOPIC 00032: NIWLANG_ATTR_PAYLOAD_AUTO_NUMBER_OF_MPDUS

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga75496a7ac1fa5d1999943be865e68f7e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga75496a7ac1fa5d1999943be865e68f7e.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compute the number of MPDUs in an AMPDU of 802.11ax Trigger-Based PPDU, 802.11be Trigger-Based PPDU and 802.11bn Trigger-Based PPDU using the following frame parameters: SyntaxNIWLANG_ATTR_PAYLOAD_AUTO_NUMBER_OF_MPDUSNumeric ValueData TypeAccessApplies To178int32Read/WriteN/ARem

### NIWLANG_ATTR_PAYLOAD_AUTO_NUMBER_OF_MPDUS

Specifies whether to compute the number of MPDUs in an AMPDU of 802.11ax Trigger-Based PPDU, 802.11be Trigger-Based PPDU and 802.11bn Trigger-Based PPDU using the following frame parameters:

#### Syntax

NIWLANG_ATTR_PAYLOAD_AUTO_NUMBER_OF_MPDUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 178 | int32 | Read/Write | N/A |

#### Remarks

NIWLANG_ATTR_L_SIG_LENGTH_SIG_LENGTH Length attribute, [NIWLANG_ATTR_PRE_FEC_PADDING_FACTOR](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga98cb9ec6b764e97cae85dbc4a2fe451a.html) attribute, and [NIWLANG_ATTR_LDPC_EXTRA_SYMBOL_SEGMENT](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga18d2003ceed7910f918c990debeef4cb.html) attribute.

The default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetAutoNumberOfMPDUS 
 Get Function: niWLANG_GetAutoNumberOfMPDUS

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1ga8541a94ece14d443b3d10f9218038042.html language=enus -->
## TOPIC 00033: NIWLANG_ATTR_PAYLOAD_DATA_LENGTH

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1ga8541a94ece14d443b3d10f9218038042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1ga8541a94ece14d443b3d10f9218038042.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the payload, excluding the length of the medium access control (MAC) header and frame check sequence (FCS). This value is expressed in bytes. The payload length encoded into the physical layer (PHY) header is the sum of the payload data length and the length of the MAC header

### NIWLANG_ATTR_PAYLOAD_DATA_LENGTH

Specifies the length of the payload, excluding the length of the medium access control (MAC) header and frame check sequence (FCS). This value is expressed in bytes. The payload length encoded into the physical layer (PHY) header is the sum of the payload data length and the length of the MAC header and FCS.

#### Syntax

NIWLANG_ATTR_PAYLOAD_DATA_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 5 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, use an empty string active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if the you set [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx' as the active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE and use the [niWLANG_CreateTriggerFrameMSDU](group____root__ni_w_l_a_n_generation__functions__utility_1ga8afbf998ee6230f6dc66cf2a92b7832d.html) to generate trigger frame.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE, or use the 'userx' as the active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE and use the [niWLANG_CreateTriggerFrameMSDU](group____root__ni_w_l_a_n_generation__functions__utility_1ga8afbf998ee6230f6dc66cf2a92b7832d.html) to generate trigger frame.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx' as the active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE and use the [niWLANG_CreateTriggerFrameMSDU](group____root__ni_w_l_a_n_generation__functions__utility_1ga8afbf998ee6230f6dc66cf2a92b7832d.html) to generate trigger frame.

The default values are as follows:

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 1,024, and the limits on MPDU length are 0 to 4,095 (inclusive) and the limits on PSDU length are 0 to 65,535 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4,096, and the limits on PSDU length are 0 to 65,535 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4,096 and the limits on MPDU length are 0 to 16,383 (inclusive) and the limits on PSDU length are 0 to 46,92,480 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4,096, and the limits on PSDU length are 0 to 46,92,480 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 256 and the limits on MPDU length are 0 to 16,383 (inclusive) and the limits on PSDU length are 0 to 797,159 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 256, and the limits on PSDU length are 0 to 511 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to any other value, the default value is 1,024 and valid values are 0 to 4,095 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive) and the limits on PSDU length are 0 to 1,065,600 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096 and the limits on PSDU length are 0 to 1,065,600 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive) and the limits on PSDU length are 0 to 65,00,631 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096 and the limits on PSDU length are 0 to 65,00,631 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive) and the limits on PSDU length are 0 to 1,55,23,198 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096 and the limits on PSDU length are 0 to 1,55,23,198 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive) and the limits on PSDU length are 0 to 1,55,23,198 (inclusive).

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, the default value is 4096 and the limits on PSDU length are 0 to 1,55,23,198 (inclusive). If you set the NIWLANG_AUTO_DATA_LENGTH attribute to NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_L_SIG_LENGTH or NIWLANG_VAL_AUTO_PAYLOAD_DATA_LENGTH_MODE_FRAME_DURATION, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetPayloadDataLength 
 Get Function: niWLANG_GetPayloadDataLength

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1gaa58cc14c66eccf74928aa95fb6b478a3.html language=enus -->
## TOPIC 00034: NIWLANG_ATTR_MPDU_LENGTH

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1gaa58cc14c66eccf74928aa95fb6b478a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1gaa58cc14c66eccf74928aa95fb6b478a3.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the length of the medium access control (MAC) protocol data unit (MPDU). This value is expressed in bytes. An MPDU comprises of a MAC header, a frame body, and a frame check sequence (FCS). The NIWLANG_ATTR_MPDU_LENGTH attribute is the sum of the length of MAC header, the value of the NIWLAN

### NIWLANG_ATTR_MPDU_LENGTH

Returns the length of the medium access control (MAC) protocol data unit (MPDU). This value is expressed in bytes. An MPDU comprises of a MAC header, a frame body, and a frame check sequence (FCS). The [NIWLANG_ATTR_MPDU_LENGTH](group____root__ni_w_l_a_n_generation__attributes__payload_1gaa58cc14c66eccf74928aa95fb6b478a3.html) attribute is the sum of the length of MAC header, the value of the [NIWLANG_ATTR_PAYLOAD_DATA_LENGTH](group____root__ni_w_l_a_n_generation__attributes__payload_1ga8541a94ece14d443b3d10f9218038042.html) attribute, and the length of FCS, which is four bytes. If you disable the [NIWLANG_ATTR_MAC_HEADER_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga2b4f186912ec97d6c39f0b4f8961447b.html) and [NIWLANG_ATTR_MAC_FCS_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga0b709352374b8da6d4601cf7b3ae03ad.html) attributes, the lengths of MAC header and FCS are zero.

#### Syntax

NIWLANG_ATTR_MPDU_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 83 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to query this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to query this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to query this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to query this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

Get Function: niWLANG_GetMPDULength

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1gab31d8548769ff516d5819ff92628210c.html language=enus -->
## TOPIC 00035: NIWLANG_ATTR_PAYLOAD_USER_DEFINED_BITS

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1gab31d8548769ff516d5819ff92628210c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1gab31d8548769ff516d5819ff92628210c.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a user-defined bit pattern as an array of zeros and ones. If the array length is greater than the configured payload length, the WLAN Generation uses a subset of the required length from the beginning of the array for waveform generation. If the array length is less than the configured pay

### NIWLANG_ATTR_PAYLOAD_USER_DEFINED_BITS

Specifies a user-defined bit pattern as an array of zeros and ones. If the array length is greater than the configured payload length, the WLAN Generation uses a subset of the required length from the beginning of the array for waveform generation. If the array length is less than the configured payload length, the WLAN Generation repeats the user-defined bit pattern until the required length is achieved. If you set the [NIWLANG_ATTR_PAYLOAD_DATA_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga550109fdd6b4c4cd4818643a46bce153.html) attribute to NIWLANG_VAL_PN_SEQUENCE, the WLAN Generation ignores the [NIWLANG_ATTR_PAYLOAD_USER_DEFINED_BITS](group____root__ni_w_l_a_n_generation__attributes__payload_1gab31d8548769ff516d5819ff92628210c.html) attribute.

#### Syntax

NIWLANG_ATTR_PAYLOAD_USER_DEFINED_BITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 10 | Aint32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, use an empty string active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 An empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if the you set [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default is an empty array. Valid values include arrays of zeros and ones.

Set Function: niWLANG_SetPayloadUserDefinedBits 
 Get Function: niWLANG_GetPayloadUserDefinedBits

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1gac8c8b9b947a6fdfabe35bae77fcd906e.html language=enus -->
## TOPIC 00036: NIWLANG_ATTR_PAYLOAD_PN_ORDER

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1gac8c8b9b947a6fdfabe35bae77fcd906e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1gac8c8b9b947a6fdfabe35bae77fcd906e.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. The generated sequence is repeated (2^PN order) - 1 bits. If you set the NIWLANG_ATTR_PAYLOAD_DATA_TYPE attribute to NIWLANG_VAL_USER_DEFINED, the WLAN Generation ignores the NIWLANG_ATTR_PAYLOAD_PN_ORDER attri

### NIWLANG_ATTR_PAYLOAD_PN_ORDER

Specifies the order (length of memory) of the pseudorandom bit sequence (PRBS) generator. The generated sequence is repeated (2^PN order) - 1 bits. If you set the [NIWLANG_ATTR_PAYLOAD_DATA_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga550109fdd6b4c4cd4818643a46bce153.html) attribute to NIWLANG_VAL_USER_DEFINED, the WLAN Generation ignores the [NIWLANG_ATTR_PAYLOAD_PN_ORDER](group____root__ni_w_l_a_n_generation__attributes__payload_1gac8c8b9b947a6fdfabe35bae77fcd906e.html) attribute.

#### Syntax

NIWLANG_ATTR_PAYLOAD_PN_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 8 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 9. Valid values are 5 to 31, inclusive.

Set Function: niWLANG_SetPayloadPNOrder 
 Get Function: niWLANG_GetPayloadPNOrder

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1gaca0319b1c887e020efb8f4d179cbcb65.html language=enus -->
## TOPIC 00037: NIWLANG_ATTR_PAYLOAD_PN_SEED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1gaca0319b1c887e020efb8f4d179cbcb65.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1gaca0319b1c887e020efb8f4d179cbcb65.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the NIWLANG_ATTR_PAYLOAD_DATA_TYPE attribute to NIWLANG_VAL_USER_DEFINED, the WLAN Generation ignores NIWLANG_ATTR_PAYLOAD_PN_SEED attribute. SyntaxNIWLANG_ATTR_PAYLOAD_PN_SEEDNumeric ValueData Type

### NIWLANG_ATTR_PAYLOAD_PN_SEED

Specifies the initialization seed used for the pseudorandom bit sequence (PRBS) generator. If you set the [NIWLANG_ATTR_PAYLOAD_DATA_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga550109fdd6b4c4cd4818643a46bce153.html) attribute to NIWLANG_VAL_USER_DEFINED, the WLAN Generation ignores [NIWLANG_ATTR_PAYLOAD_PN_SEED](group____root__ni_w_l_a_n_generation__attributes__payload_1gaca0319b1c887e020efb8f4d179cbcb65.html) attribute.

#### Syntax

NIWLANG_ATTR_PAYLOAD_PN_SEED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 9 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_NUMBER_OF_FRAMES](group____root__ni_w_l_a_n_generation__attributes_1ga5fade9b5ca8e507e79a898b7d34d9aed.html) attribute to a value greater than 1 and the reset parameter of the [niWLANG_CreateWaveformComplexF64](group____root__ni_w_l_a_n_generation__functions_1gaa4ac6585af68e929d798599b3a0788fb.html) function or the [niWLANG_CreateWaveformComplexF64](group____root__ni_w_l_a_n_generation__functions_1gaa4ac6585af68e929d798599b3a0788fb.html) function to NIWLANG_VAL_TRUE, the WLAN Generation uses the PRBS generator state at the end of the payload in frame n as the seed for frame n + 1. If you set the reset parameter of the [niWLANG_CreateWaveformComplexF64](group____root__ni_w_l_a_n_generation__functions_1gaa4ac6585af68e929d798599b3a0788fb.html) function or the [niWLANG_CreateWaveformComplexF64](group____root__ni_w_l_a_n_generation__functions_1gaa4ac6585af68e929d798599b3a0788fb.html) function to NIWLANG_VAL_TRUE, all frames use the value of the [NIWLANG_ATTR_PAYLOAD_PN_SEED](group____root__ni_w_l_a_n_generation__attributes__payload_1gaca0319b1c887e020efb8f4d179cbcb65.html) attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 0xD6BF7DF2.

Set Function: niWLANG_SetPayloadPNSeed 
 Get Function: niWLANG_GetPayloadPNSeed

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1gaca69c50c7a7ff301b921da9c7058e65a.html language=enus -->
## TOPIC 00038: NIWLANG_ATTR_NUMBER_OF_DATA_SYMBOLS

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1gaca69c50c7a7ff301b921da9c7058e65a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1gaca69c50c7a7ff301b921da9c7058e65a.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of symbols in the data portion of the generated WLAN frame. Symbol refers to the chip if the NIWLANG_ATTR_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211BG_DSSS, and the symbol refers to the OFDM symbol for other values of the NIWLANG_ATTR_STANDARD attribute. SyntaxNIWLANG

### NIWLANG_ATTR_NUMBER_OF_DATA_SYMBOLS

Returns the number of symbols in the data portion of the generated WLAN frame. Symbol refers to the chip if the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute is set to NIWLANG_VAL_STANDARD_80211BG_DSSS, and the symbol refers to the OFDM symbol for other values of the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute.

#### Syntax

NIWLANG_ATTR_NUMBER_OF_DATA_SYMBOLS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 94 | int32 | Read/Write | N/A |

#### Remarks

Set Function: niWLANG_SetNumberOfDataSymbols 
 Get Function: niWLANG_GetNumberOfDataSymbols

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html language=enus -->
## TOPIC 00039: NIWLANG_ATTR_MAC_FRAME_FORMAT

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the medium access control (MAC) frame is long or short. SyntaxNIWLANG_ATTR_MAC_FRAME_FORMATNumeric ValueData TypeAccessApplies To120int32Read/WriteN/ARemarks The default value is NIWLANG_VAL_MAC_FRAME_FORMAT_LONG.Configure this attribute only when you set the NIWLANG_ATTR_STANDARD

### NIWLANG_ATTR_MAC_FRAME_FORMAT

Specifies whether the medium access control (MAC) frame is long or short.

#### Syntax

NIWLANG_ATTR_MAC_FRAME_FORMAT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 120 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_MAC_FRAME_FORMAT_LONG.

Configure this attribute only when you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use the following active channel string formats to configure this attribute. 
 An empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetMacFrameFormat 
 Get Function: niWLANG_GetMacFrameFormat

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_MAC_FRAME_FORMAT_LONG | 0 (0x0) | Specifies that the MAC frame format is long. The long format follows the general frame structure as defined in section 8.2.3 of IEEE Standard 802.11-2012. |
| NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT | 1 (0x1) | Specifies that the MAC frame format is short. The short format follows the short frame structure as defined in section 8.8 of IEEE Standard P802.11ah/D1.3. |

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload_1gaeed1428bc02b5a5c83bdbbfa553fe812.html language=enus -->
## TOPIC 00040: NIWLANG_ATTR_PAYLOAD_SCRAMBLER_SEED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload_1gaeed1428bc02b5a5c83bdbbfa553fe812.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload_1gaeed1428bc02b5a5c83bdbbfa553fe812.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the scrambler seed. SyntaxNIWLANG_ATTR_PAYLOAD_SCRAMBLER_SEEDNumeric ValueData TypeAccessApplies To17int32Read/WriteN/ARemarks You must use the following active channel string formats to configure this attribute.Standard attribute ValueActive Channel String Format80211

### NIWLANG_ATTR_PAYLOAD_SCRAMBLER_SEED

Specifies the initial state of the scrambler seed.

#### Syntax

NIWLANG_ATTR_PAYLOAD_SCRAMBLER_SEED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 17 | int32 | Read/Write | N/A |

#### Remarks

You must use the following [active channel](https://www.ni.com/docs/en-US/bundle/rfmx-waveform-creator/page/configuring-active-channels-labview2.html) string formats to configure this attribute.

| Standard attribute Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM, 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211AF MIMOOFDM | "" (empty string) |
| 80211AC MIMOOFDM | "", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU |
| 80211AC MIMOOFDM | "userx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU |
| 80211AX MIMOOFDM | "userx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU |
| 80211BE MIMOOFDM | "userx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU |

For direct sequence spread spectrum (DSSS) packets, the default value follows the requirements defined in sections 18.2.3.1 and section 18.2.3.8 of IEEE Standard 802.11b-1999.

For OFDM and DSSS-OFDM packets, the default value is 93.

Set Function: niWLANG_SetPayloadScramblerSeed 
 Get Function: niWLANG_GetPayloadScramblerSeed

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header.html language=enus -->
## TOPIC 00041: MAC Header

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsSequence ControlGroup membersNameDescriptionNIWLANG_ATTR_MAC_ADDRESS1Specifies the Address1 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0,

### MAC Header

#### Groups

- Sequence Control

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_MAC_ADDRESS1 | Specifies the Address1 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. The length of this field is defined by the NIWLANG_ATTR_MAC_ADDRESS1 Length attribute if you set the NIWLANG_ATTR_MAC_FRAME_FORMAT attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT; otherwise, the length is six bytes. If this field is a MAC address, it is represented with the least significant byte in the leftmost position and each byte is represented with the least significant bit in the rightmost position. |
| NIWLANG_ATTR_MAC_ADDRESS1_ENABLED | Specifies whether to enable the Address1 field of the medium access control (MAC) header. |
| NIWLANG_ATTR_MAC_ADDRESS1_LENGTH | Specifies the length of Address1 field when the NIWLANG_ATTR_MAC_FRAME_FORMAT attribute is set to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT. |
| NIWLANG_ATTR_MAC_ADDRESS2 | Specifies the Address2 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. |
| NIWLANG_ATTR_MAC_ADDRESS2_ENABLED | Specifies whether to enable the Address2 field of the medium access control (MAC) header. |
| NIWLANG_ATTR_MAC_ADDRESS2_LENGTH | Specifies the length of Address2 field if you set the NIWLANG_ATTR_MAC_FRAME_FORMAT attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT. |
| NIWLANG_ATTR_MAC_ADDRESS3 | Specifies the six-byte Address3 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. |
| NIWLANG_ATTR_MAC_ADDRESS3_ENABLED | Specifies whether to enable the Address3 field of the medium access control (MAC) header. |
| NIWLANG_ATTR_MAC_ADDRESS4 | Specifies the six-byte Address4 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. |
| NIWLANG_ATTR_MAC_ADDRESS4_ENABLED | Specifies whether to the enable Address4 field of the medium access control (MAC) header. |
| NIWLANG_ATTR_MAC_DURATION_OR_ID | Specifies the two-byte duration ID field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013, IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit (LSB) in the rightmost position. |
| NIWLANG_ATTR_MAC_FRAME_CONTROL | Specifies the two-byte frame control field of the medium access control (MAC) header as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit (LSB) at the rightmost position. |
| NIWLANG_ATTR_MAC_HEADER_ENABLED | Specifies whether to enable the medium access control (MAC) header, as defined in section 7.1.2 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013, IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. |
| NIWLANG_ATTR_MAC_HT_CONTROL | Specifies the four-byte HT Control field as defined in section 7.1.3 of IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit in the rightmost position. |
| NIWLANG_ATTR_MAC_HT_CONTROL_ENABLED | Specifies whether to enable the HT Control field of the medium access control (MAC) header. |
| NIWLANG_ATTR_MAC_QOS_CONTROL | Specifies the two-byte QoS Control field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit in the rightmost position. |
| NIWLANG_ATTR_MAC_QOS_CONTROL_ENABLED | Specifies whether to enable the QoS Control field of the medium access control (MAC) header. |
| NIWLANG_ATTR_MAC_SEQUENCE_CONTROL | Specifies the two-byte Sequence Control field as defined in section 7.1.3 of IEEE Standard 802.11-2007, IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. |
| NIWLANG_ATTR_MAC_SEQUENCE_CONTROL_ENABLED | Specifies whether to enable the Sequence Control field of the medium access control (MAC) header. |

#### Attachments

None

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga1f262858b8f77f1ee4d5a85324cec6d7.html language=enus -->
## TOPIC 00042: NIWLANG_ATTR_MAC_SEQUENCE_CONTROL

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga1f262858b8f77f1ee4d5a85324cec6d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga1f262858b8f77f1ee4d5a85324cec6d7.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the two-byte Sequence Control field as defined in section 7.1.3 of IEEE Standard 802.11-2007, IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of I

### NIWLANG_ATTR_MAC_SEQUENCE_CONTROL

Specifies the two-byte Sequence Control field as defined in section 7.1.3 of IEEE Standard 802.11-2007, IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3.

#### Syntax

NIWLANG_ATTR_MAC_SEQUENCE_CONTROL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 66 | int32 | Read/Write | N/A |

#### Remarks

This field is represented with the least significant bit in the rightmost position.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 0x0. Valid values are 0x0 to 0xFFFF. For values outside this range, the WLAN Generation uses the least significant 2 bytes.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacSequenceControl 
 Get Function: niWLANG_GetMacSequenceControl

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga2b4f186912ec97d6c39f0b4f8961447b.html language=enus -->
## TOPIC 00043: NIWLANG_ATTR_MAC_HEADER_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga2b4f186912ec97d6c39f0b4f8961447b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga2b4f186912ec97d6c39f0b4f8961447b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the medium access control (MAC) header, as defined in section 7.1.2 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013, IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0,

### NIWLANG_ATTR_MAC_HEADER_ENABLED

Specifies whether to enable the medium access control (MAC) header, as defined in section 7.1.2 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013, IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3.

#### Syntax

NIWLANG_ATTR_MAC_HEADER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 11 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetMacHeaderEnabled 
 Get Function: niWLANG_GetMacHeaderEnabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga2e1a2b0729fe93d39c8fcb86292a8d96.html language=enus -->
## TOPIC 00044: NIWLANG_ATTR_MAC_DURATION_OR_ID

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga2e1a2b0729fe93d39c8fcb86292a8d96.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga2e1a2b0729fe93d39c8fcb86292a8d96.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the two-byte duration ID field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013, IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P

### NIWLANG_ATTR_MAC_DURATION_OR_ID

Specifies the two-byte duration ID field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013, IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit (LSB) in the rightmost position.

#### Syntax

NIWLANG_ATTR_MAC_DURATION_OR_ID

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 58 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, use an empty string active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if the you set [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

the WLAN Generation ignores this attribute if you set the [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT.

The default value is 0x0. Valid values are 0x0 to 0xFFFF. For values outside this range, the WLAN Generation uses the least significant two bytes.

the WLAN Generation ignores this attribute, if you set the [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT.

Set Function: niWLANG_SetMacDurationOrID 
 Get Function: niWLANG_GetMacDurationOrID

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga3895668d20b799b1be853a43c4e8cf72.html language=enus -->
## TOPIC 00045: NIWLANG_ATTR_MAC_ADDRESS4_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga3895668d20b799b1be853a43c4e8cf72.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga3895668d20b799b1be853a43c4e8cf72.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to the enable Address4 field of the medium access control (MAC) header. SyntaxNIWLANG_ATTR_MAC_ADDRESS4_ENABLEDNumeric ValueData TypeAccessApplies To67int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD

### NIWLANG_ATTR_MAC_ADDRESS4_ENABLED

Specifies whether to the enable Address4 field of the medium access control (MAC) header.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS4_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 67 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_TRUE. If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacAddress4Enabled 
 Get Function: niWLANG_GetMacAddress4Enabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga39aec343bb6345c34bcac1225b66aecd.html language=enus -->
## TOPIC 00046: NIWLANG_ATTR_MAC_QOS_CONTROL_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga39aec343bb6345c34bcac1225b66aecd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga39aec343bb6345c34bcac1225b66aecd.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the QoS Control field of the medium access control (MAC) header. SyntaxNIWLANG_ATTR_MAC_QOS_CONTROL_ENABLEDNumeric ValueData TypeAccessApplies To53int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_ST

### NIWLANG_ATTR_MAC_QOS_CONTROL_ENABLED

Specifies whether to enable the QoS Control field of the medium access control (MAC) header.

#### Syntax

NIWLANG_ATTR_MAC_QOS_CONTROL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 53 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_TRUE. If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacQOSControlEnabled 
 Get Function: niWLANG_GetMacQOSControlEnabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga4e4b76dcfe49f5fc6b7ef897ad0f8aac.html language=enus -->
## TOPIC 00047: NIWLANG_ATTR_MAC_HT_CONTROL_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga4e4b76dcfe49f5fc6b7ef897ad0f8aac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga4e4b76dcfe49f5fc6b7ef897ad0f8aac.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the HT Control field of the medium access control (MAC) header. SyntaxNIWLANG_ATTR_MAC_HT_CONTROL_ENABLEDNumeric ValueData TypeAccessApplies To72int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STAN

### NIWLANG_ATTR_MAC_HT_CONTROL_ENABLED

Specifies whether to enable the HT Control field of the medium access control (MAC) header.

#### Syntax

NIWLANG_ATTR_MAC_HT_CONTROL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 72 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT or the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_TRIGGER_FRAME, the WLAN Generation ignores the [NIWLANG_ATTR_MAC_HT_CONTROL_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga4e4b76dcfe49f5fc6b7ef897ad0f8aac.html) attribute.

The default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetMacHTControlEnabled 
 Get Function: niWLANG_GetMacHTControlEnabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga5aa30b7b7d941e07232f66cf57ae29a4.html language=enus -->
## TOPIC 00048: NIWLANG_ATTR_MAC_FRAME_CONTROL

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga5aa30b7b7d941e07232f66cf57ae29a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga5aa30b7b7d941e07232f66cf57ae29a4.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the two-byte frame control field of the medium access control (MAC) header as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of I

### NIWLANG_ATTR_MAC_FRAME_CONTROL

Specifies the two-byte frame control field of the medium access control (MAC) header as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit (LSB) at the rightmost position.

#### Syntax

NIWLANG_ATTR_MAC_FRAME_CONTROL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 57 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default values are as follows:

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_GENERAL_FRAME, the default value is 0x0.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_DATA_FRAME, the default value is 0x8.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the default value is 0x24.

Valid values are 0x0 to 0xFFFF. For values outside this range, the WLAN Generation uses the least significant two bytes.

Set Function: niWLANG_SetMacFrameControl 
 Get Function: niWLANG_GetMacFrameControl

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga770c7d6ec9be161efc7cd8aa78990aab.html language=enus -->
## TOPIC 00049: NIWLANG_ATTR_MAC_ADDRESS2

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga770c7d6ec9be161efc7cd8aa78990aab.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga770c7d6ec9be161efc7cd8aa78990aab.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Address2 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/

### NIWLANG_ATTR_MAC_ADDRESS2

Specifies the Address2 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS2

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 62 | int64 | Read/Write | N/A |

#### Remarks

The length of this field is defined by the [NIWLANG_ATTR_MAC_ADDRESS2_LENGTH](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gabc311d19c36ae40f8a9c98a78f4e37b0.html) attribute if you set the [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT; otherwise, the length is six bytes. If this field is a MAC address, it is represented with the least significant byte in the leftmost position and each byte is represented with the least significant bit in the rightmost position.

For example, the medium access control (MAC) address 12-34-56-78-9A-BC is represented by the number 0 x 123456789ABC.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant six bytes.

Set Function: niWLANG_SetMacAddress2 
 Get Function: niWLANG_GetMacAddress2

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga807da9da620556694068f9cd8ec778a0.html language=enus -->
## TOPIC 00050: NIWLANG_ATTR_MAC_HT_CONTROL

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga807da9da620556694068f9cd8ec778a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga807da9da620556694068f9cd8ec778a0.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the four-byte HT Control field as defined in section 7.1.3 of IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field i

### NIWLANG_ATTR_MAC_HT_CONTROL

Specifies the four-byte HT Control field as defined in section 7.1.3 of IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit in the rightmost position.

#### Syntax

NIWLANG_ATTR_MAC_HT_CONTROL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 73 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant four bytes.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacHTControl 
 Get Function: niWLANG_GetMacHTControl

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga84e6dec6df4b2d0905edb95c539c477a.html language=enus -->
## TOPIC 00051: NIWLANG_ATTR_MAC_ADDRESS1_LENGTH

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga84e6dec6df4b2d0905edb95c539c477a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga84e6dec6df4b2d0905edb95c539c477a.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of Address1 field when the NIWLANG_ATTR_MAC_FRAME_FORMAT attribute is set to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT. SyntaxNIWLANG_ATTR_MAC_ADDRESS1_LENGTHNumeric ValueData TypeAccessApplies To121int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL

### NIWLANG_ATTR_MAC_ADDRESS1_LENGTH

Specifies the length of Address1 field when the [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute is set to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS1_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 121 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use the following active channel string formats to configure this attribute. 
 An empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE.

The default value is 2. Valid values are 2 and 6.

Set Function: niWLANG_SetMacAddress1Length 
 Get Function: niWLANG_GetMacAddress1Length

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga8aa0be52e9a14233c4a1b3440d087d43.html language=enus -->
## TOPIC 00052: NIWLANG_ATTR_MAC_ADDRESS1

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga8aa0be52e9a14233c4a1b3440d087d43.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga8aa0be52e9a14233c4a1b3440d087d43.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Address1 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/

### NIWLANG_ATTR_MAC_ADDRESS1

Specifies the Address1 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. The length of this field is defined by the [NIWLANG_ATTR_MAC_ADDRESS1](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga8aa0be52e9a14233c4a1b3440d087d43.html) Length attribute if you set the [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT; otherwise, the length is six bytes. If this field is a MAC address, it is represented with the least significant byte in the leftmost position and each byte is represented with the least significant bit in the rightmost position.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS1

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 60 | int64 | Read/Write | N/A |

#### Remarks

For example, the medium access control (MAC) address 12-34-56-78-9A-BC is represented by the number 0 x 123456789ABC.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant six bytes.

Set Function: niWLANG_SetMacAddress1 
 Get Function: niWLANG_GetMacAddress1

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga8de0bca4774985b95d6d0a431bc81f21.html language=enus -->
## TOPIC 00053: NIWLANG_ATTR_MAC_ADDRESS1_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga8de0bca4774985b95d6d0a431bc81f21.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga8de0bca4774985b95d6d0a431bc81f21.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Address1 field of the medium access control (MAC) header. SyntaxNIWLANG_ATTR_MAC_ADDRESS1_ENABLEDNumeric ValueData TypeAccessApplies To59int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD

### NIWLANG_ATTR_MAC_ADDRESS1_ENABLED

Specifies whether to enable the Address1 field of the medium access control (MAC) header.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS1_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 59 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetMacAddress1Enabled 
 Get Function: niWLANG_GetMacAddress1Enabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga95e761ce1f51f6858b7d3dd6488bb9e5.html language=enus -->
## TOPIC 00054: NIWLANG_ATTR_MAC_QOS_CONTROL

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga95e761ce1f51f6858b7d3dd6488bb9e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga95e761ce1f51f6858b7d3dd6488bb9e5.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the two-byte QoS Control field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEE

### NIWLANG_ATTR_MAC_QOS_CONTROL

Specifies the two-byte QoS Control field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field is represented with the least significant bit in the rightmost position.

#### Syntax

NIWLANG_ATTR_MAC_QOS_CONTROL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 71 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0x0. Valid values are 0x0 to 0xFFFF. For values outside this range, the WLAN Generation uses the least significant two bytes.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT or the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_MAC_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores the [NIWLANG_ATTR_MAC_QOS_CONTROL](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga95e761ce1f51f6858b7d3dd6488bb9e5.html) attribute.

The default value is 0x0. Valid values are 0x0 to 0xFFFF. For values outside this range, the WLAN Generation uses the least significant two bytes.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacQOSControl 
 Get Function: niWLANG_GetMacQOSControl

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaa56c3034b736582cfd65a188458c86bd.html language=enus -->
## TOPIC 00055: NIWLANG_ATTR_MAC_ADDRESS3

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaa56c3034b736582cfd65a188458c86bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaa56c3034b736582cfd65a188458c86bd.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the six-byte Address3 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P

### NIWLANG_ATTR_MAC_ADDRESS3

Specifies the six-byte Address3 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS3

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 64 | int64 | Read/Write | N/A |

#### Remarks

This field is represented with the least significant byte in the leftmost position, and each byte is represented with the least significant bit in the rightmost position.

For example, the medium access control (MAC) address 12-34-56-78-9A-BC is represented by the number 0x123456789ABC.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant six bytes.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacAddress3 
 Get Function: niWLANG_GetMacAddress3

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gabc311d19c36ae40f8a9c98a78f4e37b0.html language=enus -->
## TOPIC 00056: NIWLANG_ATTR_MAC_ADDRESS2_LENGTH

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gabc311d19c36ae40f8a9c98a78f4e37b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gabc311d19c36ae40f8a9c98a78f4e37b0.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of Address2 field if you set the NIWLANG_ATTR_MAC_FRAME_FORMAT attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT. SyntaxNIWLANG_ATTR_MAC_ADDRESS2_LENGTHNumeric ValueData TypeAccessApplies To122int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_

### NIWLANG_ATTR_MAC_ADDRESS2_LENGTH

Specifies the length of Address2 field if you set the [NIWLANG_ATTR_MAC_FRAME_FORMAT](group____root__ni_w_l_a_n_generation__attributes__payload_1gad131ebf3dc6ccf53464aa425926175eb.html) attribute to NIWLANG_VAL_MAC_FRAME_FORMAT_SHORT.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS2_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 122 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use the following active channel string formats to configure this attribute. 
 An empty string active channel string format if you set the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE.

The default value is 2. Valid values are 2 and 6.

Set Function: niWLANG_SetMacAddress2Length 
 Get Function: niWLANG_GetMacAddress2Length

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gac24832dc2ebf7d2f85676ed231039935.html language=enus -->
## TOPIC 00057: NIWLANG_ATTR_MAC_ADDRESS2_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gac24832dc2ebf7d2f85676ed231039935.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gac24832dc2ebf7d2f85676ed231039935.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Address2 field of the medium access control (MAC) header. SyntaxNIWLANG_ATTR_MAC_ADDRESS2_ENABLEDNumeric ValueData TypeAccessApplies To61int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD

### NIWLANG_ATTR_MAC_ADDRESS2_ENABLED

Specifies whether to enable the Address2 field of the medium access control (MAC) header.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS2_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 61 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetMacAddress2Enabled 
 Get Function: niWLANG_GetMacAddress2Enabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gacbad2d6926089d116c181b1abd673c65.html language=enus -->
## TOPIC 00058: NIWLANG_ATTR_MAC_ADDRESS3_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gacbad2d6926089d116c181b1abd673c65.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gacbad2d6926089d116c181b1abd673c65.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Address3 field of the medium access control (MAC) header. SyntaxNIWLANG_ATTR_MAC_ADDRESS3_ENABLEDNumeric ValueData TypeAccessApplies To63int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD

### NIWLANG_ATTR_MAC_ADDRESS3_ENABLED

Specifies whether to enable the Address3 field of the medium access control (MAC) header.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS3_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 63 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_TRUE. If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacAddress3Enabled 
 Get Function: niWLANG_GetMacAddress3Enabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaf3b365bde8c7bd478979b34e8063521a.html language=enus -->
## TOPIC 00059: NIWLANG_ATTR_MAC_ADDRESS4

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaf3b365bde8c7bd478979b34e8063521a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaf3b365bde8c7bd478979b34e8063521a.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the six-byte Address4 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P

### NIWLANG_ATTR_MAC_ADDRESS4

Specifies the six-byte Address4 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3.

#### Syntax

NIWLANG_ATTR_MAC_ADDRESS4

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 68 | int64 | Read/Write | N/A |

#### Remarks

This field is represented with the least significant byte in the leftmost position, and each byte is represented with the least significant bit in the rightmost position.

For example, the medium access control (MAC) address 12-34-56-78-9A-BC is represented by the number 0 x 123456789ABC.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant six bytes.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacAddress4 
 Get Function: niWLANG_GetMacAddress4

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaf6bde53f49a8a85c9a3ed339a382137b.html language=enus -->
## TOPIC 00060: NIWLANG_ATTR_MAC_SEQUENCE_CONTROL_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaf6bde53f49a8a85c9a3ed339a382137b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1gaf6bde53f49a8a85c9a3ed339a382137b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Sequence Control field of the medium access control (MAC) header. SyntaxNIWLANG_ATTR_MAC_SEQUENCE_CONTROL_ENABLEDNumeric ValueData TypeAccessApplies To65int32Read/WriteN/ARemarks If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWL

### NIWLANG_ATTR_MAC_SEQUENCE_CONTROL_ENABLED

Specifies whether to enable the Sequence Control field of the medium access control (MAC) header.

#### Syntax

NIWLANG_ATTR_MAC_SEQUENCE_CONTROL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 65 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, you must use an empty string to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, you must use an empty string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, you must use the following active channel string formats to configure this attribute: 
 An empty string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'mpdux' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE, or use the 'mpdux' active channel string if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or NIWLANG_VAL_PPDU_TYPE_EXTENDED_RANGE_SU_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. 
 Use the 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, use 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use the following active channel string formats to configure this attribute: 
 'userx/mpduy' as the active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_MU_PPDU or NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE. Use an empty string active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_FALSE. 
 Use the 'mpdux' active channel string format if you set the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute to NIWLANG_VAL_PPDU_TYPE_ELR_PPDU and the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute to NIWLANG_VAL_TRUE.

The default value is NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacSequenceControlEnabled 
 Get Function: niWLANG_GetMacSequenceControlEnabled

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control.html language=enus -->
## TOPIC 00061: Sequence Control

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLEDSpecifies whether to increment fragment number in a sequence of frames. The starting number is the value represented by the fragment number sub-field of the NIWLANG_ATTR_MAC_SEQUENCE_CONTROL attribute. If you set

### Sequence Control

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED | Specifies whether to increment fragment number in a sequence of frames. The starting number is the value represented by the fragment number sub-field of the NIWLANG_ATTR_MAC_SEQUENCE_CONTROL attribute. If you set the NIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED attribute to NIWLANG_VAL_TRUE, the fragment number increments by 1 for every successive frame having the same sequence number. The fragment number wraps to the starting number when the sequence number increments. The fragment number wraps to 0 after reaching the value 15. |
| NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_ENABLED | Specifies whether to increment the sequence number in a sequence of frames. |
| NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_INTERVAL | Specifies the number of frames after which the WLAN Generation increments the sequence number by 1. The starting number is the value represented by the sequence number sub-field of the Sequence Control field. The sequence number is wrapped to 0 after reaching the value 4,095 or (2^12-1). |

#### Attachments

None

Parent topic:

MAC Header

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga0cd7d48a28680426e3aff01eefb7eebd.html language=enus -->
## TOPIC 00062: NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_INTERVAL

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga0cd7d48a28680426e3aff01eefb7eebd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga0cd7d48a28680426e3aff01eefb7eebd.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of frames after which the WLAN Generation increments the sequence number by 1. The starting number is the value represented by the sequence number sub-field of the Sequence Control field. The sequence number is wrapped to 0 after reaching the value 4,095 or (2^12-1). SyntaxNIWLA

### NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_INTERVAL

Specifies the number of frames after which the WLAN Generation increments the sequence number by 1. The starting number is the value represented by the sequence number sub-field of the Sequence Control field. The sequence number is wrapped to 0 after reaching the value 4,095 or (2^12-1).

#### Syntax

NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 81 | int32 | Read/Write | N/A |

#### Remarks

the WLAN Generation ignores this attribute if you set the [NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga8a9ab5c76b7e37ada48c045816dc7211.html) attribute to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME.

The default value is 1. Valid values are 0 to 4,095, inclusive.

Set Function: niWLANG_SetMacSequenceNumberIncrementInterval 
 Get Function: niWLANG_GetMacSequenceNumberIncrementInterval

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga8a9ab5c76b7e37ada48c045816dc7211.html language=enus -->
## TOPIC 00063: NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga8a9ab5c76b7e37ada48c045816dc7211.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga8a9ab5c76b7e37ada48c045816dc7211.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to increment the sequence number in a sequence of frames. SyntaxNIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_ENABLEDNumeric ValueData TypeAccessApplies To80int32Read/WriteN/ARemarks The default value is NIWLANG_VAL_TRUE. If you set the NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE attribute to

### NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_ENABLED

Specifies whether to increment the sequence number in a sequence of frames.

#### Syntax

NIWLANG_ATTR_MAC_SEQUENCE_NUMBER_INCREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 80 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_TRUE. If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacSequenceNumberIncrementEnabled 
 Get Function: niWLANG_GetMacSequenceNumberIncrementEnabled

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga94458bbf28478bba2d03e07a3f1097a7.html language=enus -->
## TOPIC 00064: NIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga94458bbf28478bba2d03e07a3f1097a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga94458bbf28478bba2d03e07a3f1097a7.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to increment fragment number in a sequence of frames. The starting number is the value represented by the fragment number sub-field of the NIWLANG_ATTR_MAC_SEQUENCE_CONTROL attribute. If you set the NIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED attribute to NIWLANG_VAL_TRUE, t

### NIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED

Specifies whether to increment fragment number in a sequence of frames. The starting number is the value represented by the fragment number sub-field of the [NIWLANG_ATTR_MAC_SEQUENCE_CONTROL](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header_1ga1f262858b8f77f1ee4d5a85324cec6d7.html) attribute. If you set the [NIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload__mac__header__sequence__control_1ga94458bbf28478bba2d03e07a3f1097a7.html) attribute to NIWLANG_VAL_TRUE, the fragment number increments by 1 for every successive frame having the same sequence number. The fragment number wraps to the starting number when the sequence number increments. The fragment number wraps to 0 after reaching the value 15.

#### Syntax

NIWLANG_ATTR_MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 82 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_TRUE.

If you set the [NIWLANG_ATTR_PAYLOAD_MAC_FRAME_TYPE](group____root__ni_w_l_a_n_generation__attributes__payload_1ga473d8f92c9c628768850b0646b6a1fbe.html) attribute to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME, the WLAN Generation ignores this attribute.

Set Function: niWLANG_SetMacFragmentNumberIncrementEnabled 
 Get Function: niWLANG_GetMacFragmentNumberIncrementEnabled

Parent topic:

Sequence Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame.html language=enus -->
## TOPIC 00065: Trigger Frame

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIWLANG_ATTR_TRIGGER_FRAME_AID12Specifies the value of the AID12 field in the trigger frame. NIWLANG_ATTR_TRIGGER_FRAME_AP_TX_POWERSpecifies the value of the AP Tx Power field of the Trigger frame. The power values -20 dBm to 40 dBm are mapped to the field value

### Trigger Frame

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_TRIGGER_FRAME_AID12 | Specifies the value of the AID12 field in the trigger frame. |
| NIWLANG_ATTR_TRIGGER_FRAME_AP_TX_POWER | Specifies the value of the AP Tx Power field of the Trigger frame. The power values -20 dBm to 40 dBm are mapped to the field values 0 to 60 respectively. |
| NIWLANG_ATTR_TRIGGER_FRAME_CS_REQUIRED | Specifies the CS required sub-field in the 802.11ax, 802.11be and 802.11bn Trigger Frame. |
| NIWLANG_ATTR_TRIGGER_FRAME_MAC_PADDING_DURATION | Specifies the padding duration when the NIWLANG_FRAME_TYPE attribute is set to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME. |
| NIWLANG_ATTR_TRIGGER_FRAME_TARGET_RSSI | Specifies the value of the UL-Target RSSI field of the Trigger frame. The power values -110 dBm to -20 dBm are mapped to the field values 0 to 90, respectively. To specify maximum transmit power for the assigned MCS, you must set a value of 127. |

#### Attachments

None

Parent topic:

Payload

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga051644cd60d480c5dcfce9d0890e031a.html language=enus -->
## TOPIC 00066: NIWLANG_ATTR_TRIGGER_FRAME_CS_REQUIRED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga051644cd60d480c5dcfce9d0890e031a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga051644cd60d480c5dcfce9d0890e031a.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the CS required sub-field in the 802.11ax, 802.11be and 802.11bn Trigger Frame. SyntaxNIWLANG_ATTR_TRIGGER_FRAME_CS_REQUIREDNumeric ValueData TypeAccessApplies To190int32Read/WriteN/ARemarks The default value is 0. The valid values are 0 and 1.Set Function: niWLANG_SetCSRequired Get Functi

### NIWLANG_ATTR_TRIGGER_FRAME_CS_REQUIRED

Specifies the CS required sub-field in the 802.11ax, 802.11be and 802.11bn Trigger Frame.

#### Syntax

NIWLANG_ATTR_TRIGGER_FRAME_CS_REQUIRED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 190 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. The valid values are 0 and 1.

Set Function: niWLANG_SetCSRequired 
 Get Function: niWLANG_GetCSRequired

Parent topic:

Trigger Frame

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga09527c238e26d9d169c4c141cba8aa76.html language=enus -->
## TOPIC 00067: NIWLANG_ATTR_TRIGGER_FRAME_AID12

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga09527c238e26d9d169c4c141cba8aa76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga09527c238e26d9d169c4c141cba8aa76.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the AID12 field in the trigger frame. SyntaxNIWLANG_ATTR_TRIGGER_FRAME_AID12Numeric ValueData TypeAccessApplies To196int32Read/WriteN/ARemarks The valid values are 1 to 2007, which are used for indication of RUs used by Trigger-based PPDU.The values 0 and 2045 are used for Ran

### NIWLANG_ATTR_TRIGGER_FRAME_AID12

Specifies the value of the AID12 field in the trigger frame.

#### Syntax

NIWLANG_ATTR_TRIGGER_FRAME_AID12

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 196 | int32 | Read/Write | N/A |

#### Remarks

The valid values are 1 to 2007, which are used for indication of RUs used by Trigger-based PPDU.

The values 0 and 2045 are used for Random Access RU information specification, the value 2046 is used for unassigned RU location indication, and the value 4095 is reserved for trigger frame padding indication.

When you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU, use 'userx' as active channel string formats to configure this attribute.

The default value is 1.

Set Function: niWLANG_SetAID12 
 Get Function: niWLANG_GetAID12

Parent topic:

Trigger Frame

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga1e71a21cde8e1e5b2d4dfe817b94dcb8.html language=enus -->
## TOPIC 00068: NIWLANG_ATTR_TRIGGER_FRAME_AP_TX_POWER

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga1e71a21cde8e1e5b2d4dfe817b94dcb8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga1e71a21cde8e1e5b2d4dfe817b94dcb8.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the AP Tx Power field of the Trigger frame. The power values -20 dBm to 40 dBm are mapped to the field values 0 to 60 respectively. SyntaxNIWLANG_ATTR_TRIGGER_FRAME_AP_TX_POWERNumeric ValueData TypeAccessApplies To172int32Read/WriteN/ARemarks The default value is 0. The valid

### NIWLANG_ATTR_TRIGGER_FRAME_AP_TX_POWER

Specifies the value of the AP Tx Power field of the Trigger frame. The power values -20 dBm to 40 dBm are mapped to the field values 0 to 60 respectively.

#### Syntax

NIWLANG_ATTR_TRIGGER_FRAME_AP_TX_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 172 | int32 | Read/Write | N/A |

#### Remarks

The default value is 0. The valid values are 0 to 63, inclusive.

Set Function: niWLANG_SetAPTxPower 
 Get Function: niWLANG_GetAPTxPower

Parent topic:

Trigger Frame

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga3ebf927977d860987252557b8d87520a.html language=enus -->
## TOPIC 00069: NIWLANG_ATTR_TRIGGER_FRAME_MAC_PADDING_DURATION

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga3ebf927977d860987252557b8d87520a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga3ebf927977d860987252557b8d87520a.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the padding duration when the NIWLANG_FRAME_TYPE attribute is set to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME. SyntaxNIWLANG_ATTR_TRIGGER_FRAME_MAC_PADDING_DURATIONNumeric ValueData TypeAccessApplies To189int32Read/WriteN/ARemarks This attribute is valid, if you set the NIWLANG_ATTR_ST

### NIWLANG_ATTR_TRIGGER_FRAME_MAC_PADDING_DURATION

Specifies the padding duration when the NIWLANG_FRAME_TYPE attribute is set to NIWLANG_VAL_PAYLOAD_FRAME_TYPE_TRIGGER_FRAME.

#### Syntax

NIWLANG_ATTR_TRIGGER_FRAME_MAC_PADDING_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 189 | int32 | Read/Write | N/A |

#### Remarks

This attribute is valid, if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, and NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM use an empty string active channel string format to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE, or use 'mpdux' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, use an empty string as the active channel string format, if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU or use 'mpdux' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE and the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_SU_PPDU to configure this attribute.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, use 'mpdux' as the active channel string format if the [NIWLANG_ATTR_AMPDU_ENABLED](group____root__ni_w_l_a_n_generation__attributes__payload_1ga63f7b871f361b71c28af7fc400837453.html) attribute is set to NIWLANG_VAL_TRUE to configure this attribute.

The default value is NIWLANG_VAL_MAXIMUM_PADDING_DURATION_0US. Set Function: niWLANG_SetMaximumMacPaddingDuration

Get Function: niWLANG_GetMaximumMacPaddingDuration

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_PADDING_DURATION_0US | 0 (0x0) | Specifies that there is no padding. |
| NIWLANG_VAL_PADDING_DURATION_8US | 1 (0x1) | Specifies that the padding duration is 8us. |
| NIWLANG_VAL_PADDING_DURATION_16US | 2 (0x2) | Specifies that the padding duration is 16us. |

Parent topic:

Trigger Frame

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga9a20d27e66004cfd41e646d4c0d8dd54.html language=enus -->
## TOPIC 00070: NIWLANG_ATTR_TRIGGER_FRAME_TARGET_RSSI

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga9a20d27e66004cfd41e646d4c0d8dd54.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__payload__trigger__frame_1ga9a20d27e66004cfd41e646d4c0d8dd54.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the UL-Target RSSI field of the Trigger frame. The power values -110 dBm to -20 dBm are mapped to the field values 0 to 90, respectively. To specify maximum transmit power for the assigned MCS, you must set a value of 127. SyntaxNIWLANG_ATTR_TRIGGER_FRAME_TARGET_RSSINumeric Va

### NIWLANG_ATTR_TRIGGER_FRAME_TARGET_RSSI

Specifies the value of the UL-Target RSSI field of the Trigger frame. The power values -110 dBm to -20 dBm are mapped to the field values 0 to 90, respectively. To specify maximum transmit power for the assigned MCS, you must set a value of 127.

#### Syntax

NIWLANG_ATTR_TRIGGER_FRAME_TARGET_RSSI

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 173 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, you must use 'userx' as the active channel string format to configure this attribute if the [NIWLANG_ATTR_PPDU_TYPE](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga3ad02da6d409526f7cb2311ff403fa31.html) attribute is set to NIWLANG_VAL_PPDU_TYPE_TRIGGER_BASED_PPDU.

The default value is 78, which is the corresponding power value -32 dBm. The valid values are 0 to 127,inclusive.

Set Function: niWLANG_SetTargetRSSI 
 Get Function: niWLANG_GetTargetRSSI

Parent topic:

Trigger Frame

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control.html language=enus -->
## TOPIC 00071: Spectrum Control

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIWLANG_ATTR_DSSS_WINDOW_LENGTHSpecifies the window length for direct spread spectrum signals. This value is expressed in seconds. If you do not want windowing, set this attribute to 0. NIWLANG_ATTR_OFDM_WINDOW_LENGTHSpecifies the window length for OFDM signals

### Spectrum Control

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIWLANG_ATTR_DSSS_WINDOW_LENGTH | Specifies the window length for direct spread spectrum signals. This value is expressed in seconds. If you do not want windowing, set this attribute to 0. |
| NIWLANG_ATTR_OFDM_WINDOW_LENGTH | Specifies the window length for OFDM signals at the sampling rate equal to the channel bandwidth. This value is expressed in samples. For example, if the window length is 2, the channel bandwidth is 20 MHz and the oversampling ratio is 4, then the samples over which windowing is applied is 8. |
| NIWLANG_ATTR_PULSE_SHAPING_FILTER_ENABLED | Specifies whether to apply pulse-shaping filter to the generated signal. |
| NIWLANG_ATTR_PULSE_SHAPING_FILTER_LENGTH | Specifies the length of the pulse-shaping filter. This value is expressed in symbols. The length affects the frequency response of the filter. the WLAN Generation ignores this attribute when the NIWLANG_ATTR_PULSE_SHAPING_FILTER_LENGTH attribute is set to NIWLANG_VAL_TRUE. |
| NIWLANG_ATTR_PULSE_SHAPING_FILTER_PARAMETER | Specifies the value of the rolloff factor (alpha) if you set the NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE attribute to NIWLANG_VAL_FILTER_RAISED_COSINE or NIWLANG_VAL_FILTER_ROOT_RAISED_COSINE. If you set the NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE attribute to NIWLANG_VAL_FILTER_GAUSSIAN, you can calculate the NIWLANG_ATTR_PULSE_SHAPING_FILTER_PARAMETER attribute by multiplying B and T, where B is the 3 dB bandwidth and T is the symbol period for a Gaussian filter. |
| NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE | Specifies the pulse-shaping filter type to use to ensure that the signal spectrum meets the spectral mask criteria as defined in section 17.3.9.2 of IEEE Standard 802.11a-1999, section 18.4.7.3 of IEEE Standard 802.11b-1999, and section 20.3.21.1 of IEEE Standard 802.11n-2009. |
| NIWLANG_ATTR_WINDOWING_METHOD | Specifies the method of applying window to the baseband signal, if you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM. This attribute is ignored if you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211BG_DSSS. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga242197478d3d53cf767ac9c960831ca8.html language=enus -->
## TOPIC 00072: NIWLANG_ATTR_PULSE_SHAPING_FILTER_ENABLED

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga242197478d3d53cf767ac9c960831ca8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga242197478d3d53cf767ac9c960831ca8.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply pulse-shaping filter to the generated signal. SyntaxNIWLANG_ATTR_PULSE_SHAPING_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To54int32Read/WriteN/ARemarks the WLAN Generation ignores this attribute and enables the pulse shaping filter, if you set the NIWLANG_ATTR_COMPA

### NIWLANG_ATTR_PULSE_SHAPING_FILTER_ENABLED

Specifies whether to apply pulse-shaping filter to the generated signal.

#### Syntax

NIWLANG_ATTR_PULSE_SHAPING_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 54 | int32 | Read/Write | N/A |

#### Remarks

the WLAN Generation ignores this attribute and enables the pulse shaping filter, if you set the [NIWLANG_ATTR_COMPATIBILITY_VERSION](group____root__ni_w_l_a_n_generation__attributes__advanced_1ga5330819675827a189ebc1a48f85a6a77.html) attribute to NIWLANG_VAL_COMPATIBILITY_VERSION_010000.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BG_DSSS or NIWLANG_VAL_STANDARD_80211P_OFDM , the default value is NIWLANG_VAL_TRUE. 
 If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM, the default value is NIWLANG_VAL_TRUE.

Set Function: niWLANG_SetPulseShapingFilterEnabled 
 Get Function: niWLANG_GetPulseShapingFilterEnabled

Parent topic:

Spectrum Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga500b90e1e787813ff49050008db7df64.html language=enus -->
## TOPIC 00073: NIWLANG_ATTR_OFDM_WINDOW_LENGTH

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga500b90e1e787813ff49050008db7df64.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga500b90e1e787813ff49050008db7df64.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the window length for OFDM signals at the sampling rate equal to the channel bandwidth. This value is expressed in samples. For example, if the window length is 2, the channel bandwidth is 20 MHz and the oversampling ratio is 4, then the samples over which windowing is applied is 8. Syntax

### NIWLANG_ATTR_OFDM_WINDOW_LENGTH

Specifies the window length for OFDM signals at the sampling rate equal to the channel bandwidth. This value is expressed in samples. For example, if the window length is 2, the channel bandwidth is 20 MHz and the oversampling ratio is 4, then the samples over which windowing is applied is 8.

#### Syntax

NIWLANG_ATTR_OFDM_WINDOW_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 125 | int32 | Read/Write | N/A |

#### Remarks

This attribute provides a smooth, spurious free transition from the end of one OFDM symbol to the cyclic prefix of the next symbol. If you do not want windowing, set this attribute to 0.

Refer to the Windowing help topic for more information about windowing for OFDM signals.

The default value is 2.

Set Function: niWLANG_SetOFDMWindowLength 
 Get Function: niWLANG_GetOFDMWindowLength

Parent topic:

Spectrum Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga759d94a14c5375af521838fbf276b6b8.html language=enus -->
## TOPIC 00074: NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga759d94a14c5375af521838fbf276b6b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga759d94a14c5375af521838fbf276b6b8.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse-shaping filter type to use to ensure that the signal spectrum meets the spectral mask criteria as defined in section 17.3.9.2 of IEEE Standard 802.11a-1999, section 18.4.7.3 of IEEE Standard 802.11b-1999, and section 20.3.21.1 of IEEE Standard 802.11n-2009. SyntaxNIWLANG_ATTR_PUL

### NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE

Specifies the pulse-shaping filter type to use to ensure that the signal spectrum meets the spectral mask criteria as defined in section 17.3.9.2 of IEEE Standard 802.11a-1999, section 18.4.7.3 of IEEE Standard 802.11b-1999, and section 20.3.21.1 of IEEE Standard 802.11n-2009.

#### Syntax

NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 26 | int32 | Read/Write | N/A |

#### Remarks

The default value is NIWLANG_VAL_FILTER_RECTANGULAR if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM.

The default value is NIWLANG_VAL_FILTER_ROOT_RAISED_COSINE if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BG_DSSS.

The default value is NIWLANG_VAL_FILTER_RAISED_COSINE if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211P_DSSS.

Set Function: niWLANG_SetPulseShapingFilterType 
 Get Function: niWLANG_GetPulseShapingFilterType

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_FILTER_RECTANGULAR | 0 (0x0) | Refer to the Pulse Shaping Filter Type Values help topic in the RFmx WLAN Generation Help. |
| NIWLANG_VAL_FILTER_RAISED_COSINE | 1 (0x1) | Refer to the Pulse Shaping Filter Type Values help topic in the RFmx WLAN Generation Help. |
| NIWLANG_VAL_FILTER_ROOT_RAISED_COSINE | 2 (0x2) | Refer to the Pulse Shaping Filter Type Values help topic in the RFmx WLAN Generation Help. |
| NIWLANG_VAL_FILTER_GAUSSIAN | 3 (0x3) | Refer to the Pulse Shaping Filter Type Values help topic in the RFmx WLAN Generation Help. |

Parent topic:

Spectrum Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga8c78c1ea667733b33f15e82a9d43131c.html language=enus -->
## TOPIC 00075: NIWLANG_ATTR_PULSE_SHAPING_FILTER_LENGTH

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga8c78c1ea667733b33f15e82a9d43131c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga8c78c1ea667733b33f15e82a9d43131c.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the pulse-shaping filter. This value is expressed in symbols. The length affects the frequency response of the filter. the WLAN Generation ignores this attribute when the NIWLANG_ATTR_PULSE_SHAPING_FILTER_LENGTH attribute is set to NIWLANG_VAL_TRUE. SyntaxNIWLANG_ATTR_PULSE_S

### NIWLANG_ATTR_PULSE_SHAPING_FILTER_LENGTH

Specifies the length of the pulse-shaping filter. This value is expressed in symbols. The length affects the frequency response of the filter. the WLAN Generation ignores this attribute when the [NIWLANG_ATTR_PULSE_SHAPING_FILTER_LENGTH](group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga8c78c1ea667733b33f15e82a9d43131c.html) attribute is set to NIWLANG_VAL_TRUE.

#### Syntax

NIWLANG_ATTR_PULSE_SHAPING_FILTER_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 112 | int32 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211P_OFDM, the default value is 100. In all other instances, The default value is 8.

Set Function: niWLANG_SetPulseShapingFilterLength 
 Get Function: niWLANG_GetPulseShapingFilterLength

Parent topic:

Spectrum Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gacbf49c4ab46d23030fab8e4bf41d4eb4.html language=enus -->
## TOPIC 00076: NIWLANG_ATTR_PULSE_SHAPING_FILTER_PARAMETER

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gacbf49c4ab46d23030fab8e4bf41d4eb4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gacbf49c4ab46d23030fab8e4bf41d4eb4.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the rolloff factor (alpha) if you set the NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE attribute to NIWLANG_VAL_FILTER_RAISED_COSINE or NIWLANG_VAL_FILTER_ROOT_RAISED_COSINE. If you set the NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE attribute to NIWLANG_VAL_FILTER_GAUSSIAN, you can calc

### NIWLANG_ATTR_PULSE_SHAPING_FILTER_PARAMETER

Specifies the value of the rolloff factor (alpha) if you set the [NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE](group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga759d94a14c5375af521838fbf276b6b8.html) attribute to NIWLANG_VAL_FILTER_RAISED_COSINE or NIWLANG_VAL_FILTER_ROOT_RAISED_COSINE. If you set the [NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE](group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga759d94a14c5375af521838fbf276b6b8.html) attribute to NIWLANG_VAL_FILTER_GAUSSIAN, you can calculate the [NIWLANG_ATTR_PULSE_SHAPING_FILTER_PARAMETER](group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gacbf49c4ab46d23030fab8e4bf41d4eb4.html) attribute by multiplying B and T, where B is the 3 dB bandwidth and T is the symbol period for a Gaussian filter.

#### Syntax

NIWLANG_ATTR_PULSE_SHAPING_FILTER_PARAMETER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 27 | float64 | Read/Write | N/A |

#### Remarks

If you set the [NIWLANG_ATTR_PULSE_SHAPING_FILTER_TYPE](group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1ga759d94a14c5375af521838fbf276b6b8.html) attribute to NIWLANG_VAL_FILTER_RECTANGULAR, the WLAN Generation ignores this attribute.

The default value is 0.5. Valid values are 0.1 to 0.95, inclusive.

Set Function: niWLANG_SetPulseShapingFilterParameter 
 Get Function: niWLANG_GetPulseShapingFilterParameter

Parent topic:

Spectrum Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gaf3bca9a2c4215244fb171873a4aab050.html language=enus -->
## TOPIC 00077: NIWLANG_ATTR_WINDOWING_METHOD

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gaf3bca9a2c4215244fb171873a4aab050.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gaf3bca9a2c4215244fb171873a4aab050.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method of applying window to the baseband signal, if you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLA

### NIWLANG_ATTR_WINDOWING_METHOD

Specifies the method of applying window to the baseband signal, if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM, NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM. This attribute is ignored if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BG_DSSS.

#### Syntax

NIWLANG_ATTR_WINDOWING_METHOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 74 | int32 | Read/Write | N/A |

#### Remarks

Refer to the Windowing topic for more information about windowing for OFDM signals.

The default value is NIWLANG_VAL_WIN_METHOD_CENTERED_AT_SYMBOL_BOUNDARY.

Set Function: niWLANG_SetWindowingMethod 
 Get Function: niWLANG_GetWindowingMethod

| Name | Value | Description |
| --- | --- | --- |
| NIWLANG_VAL_WIN_METHOD_CENTERED_AT_SYMBOL_BOUNDARY | 0 (0x0) | Specifies that the window is applied with its center at the boundary between two OFDM symbols. |
| NIWLANG_VAL_WIN_METHOD_STARTING_AT_SYMBOL_BOUNDARY | 1 (0x1) | Specifies that the window is applied with its starting position at the boundary between two OFDM symbols. |

Parent topic:

Spectrum Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gaf408b913ed2dfadd2edde9f60b4f6747.html language=enus -->
## TOPIC 00078: NIWLANG_ATTR_DSSS_WINDOW_LENGTH

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gaf408b913ed2dfadd2edde9f60b4f6747.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__attributes__spectrum__control_1gaf408b913ed2dfadd2edde9f60b4f6747.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the window length for direct spread spectrum signals. This value is expressed in seconds. If you do not want windowing, set this attribute to 0. SyntaxNIWLANG_ATTR_DSSS_WINDOW_LENGTHNumeric ValueData TypeAccessApplies To29float64Read/WriteN/ARemarks This attribute provides power ramp-up an

### NIWLANG_ATTR_DSSS_WINDOW_LENGTH

Specifies the window length for direct spread spectrum signals. This value is expressed in seconds. If you do not want windowing, set this attribute to 0.

#### Syntax

NIWLANG_ATTR_DSSS_WINDOW_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 29 | float64 | Read/Write | N/A |

#### Remarks

This attribute provides power ramp-up and ramp-down for the entire burst.

Refer to the Windowing help topic for more information about windowing for DSSS signals.

The default value is 2 microseconds.

Set Function: niWLANG_SetDSSSWindowLength 
 Get Function: niWLANG_GetDSSSWindowLength

Parent topic:

Spectrum Control

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions.html language=enus -->
## TOPIC 00079: Functions

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsConfigure GenerationGeneration InformationRFSG DatabaseUtilityGroup membersNameDescriptionniWLANG_CloseSessionCloses the niWLAN generation session and releases resources associated with that session. Call this function once for each unique named session that you have created. niWLANG_CreateMIM

### Functions

#### Groups

- Configure Generation
- Generation Information
- RFSG Database
- Utility

#### Group members

| Name | Description |
| --- | --- |
| niWLANG_CloseSession | Closes the niWLAN generation session and releases resources associated with that session. Call this function once for each unique named session that you have created. |
| niWLANG_CreateMIMOWaveformsComplexF64 | Creates WLAN I/Q data for multiple channels and returns the data as an array of complex waveforms. This function returns one frame, including the idle interval, at a time. |
| niWLANG_CreateWaveformComplexF64 | Creates WLAN I/Q data and returns the data as a complex waveform. This function returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset parameter to NIWLANG_VAL_FALSE and run the function in a loop for the specified number of times or until the done parameter is NIWLANG_VAL_TRUE. |
| niWLANG_OpenSession | Looks up an existing niWLAN generation session using the sessionName parameter and returns the refnum that you can pass to subsequent niWLAN generation functions. If the lookup fails, the niWLANG_OpenSession function creates a new niWLAN generation session and returns a new refnum. |
| niWLANG_RFSGConfigureFrequencyMultipleLO | Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external LO devices. This function also configures LO frequency offset based on the NIWLANG_ATTR_LO_FREQUENCY_OFFSET_MODE and NIWLANG_ATTR_LO_FREQUENCY_OFFSET attributes. This function equally divides the NI RF vector signal generators and NI RF synthesizers into sets such that each set corresponds to one carrier frequency. The number of sets is equal to the size of the carrier frequencies array. In each set, the first NI RF vector signal generator is used as the master device for LO daisy chaining. It also configures the Signal Bandwidth and IQ Rate attributes on NI RF vector signal generators and the NIWLANG_ATTR_CARRIER_FREQUENCY attribute. You must ensure that after a frequency configuration change, the output of the external LO device settles before generating the WLAN signal. You must use one of the following programming flows: |
| niWLANG_RFSGConfigureFrequencySingleLO | Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external local oscillator (LO) devices. This function also configures LO frequency offset based on the NIWLANG_ATTR_LO_FREQUENCY_OFFSET_MODE and NIWLANG_ATTR_LO_FREQUENCY_OFFSET attributes. It also configures the Signal Bandwidth and IQ Rate attributes on NI RF vector signal generators and the NIWLANG_ATTR_CARRIER_FREQUENCY attribute. You must ensure that after a frequency configuration change, the output of the external LO device settles before generating the WLAN signal. You must use one of the following programming flows: |
| niWLANG_RFSGConfigureMultipleDeviceSynchronization | Configures multiple NI RF vector signal generators for sharing the local oscillator (LO), configures Reference Clock settings, and synchronizes multiple devices. For PXIe-5673/5673E/5840/5841/5830/5831 RF vector signal generators, this function configures LO sharing and clock settings in daisy-chained manner. For PXIe-5644, PXIe-5645, and PXIe-5646 RF vector signal transceiver (VST) devices, this function configures daisy-chained LO sharing and low-level properties for multiple device synchronization. These VSTs do not support daisy-chained Reference Clocks for synchronization. You must set the MasterReferenceClockSource to PXI_CLK for these devices. |
| niWLANG_RFSGMultipleDeviceInitiate | Commits settings to hardware, waits for hardware settling, and starts multi-device synchronized generation. |
| niWLANG_ResetSession | Resets all the attributes of the session to their default values. |

#### Attachments

None

Parent topic:

niWLANGeneration.h

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1ga05e4e87a5c18b508b84f92c43dad8c45.html language=enus -->
## TOPIC 00080: niWLANG_CreateMIMOWaveformsComplexF64

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1ga05e4e87a5c18b508b84f92c43dad8c45.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1ga05e4e87a5c18b508b84f92c43dad8c45.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates WLAN I/Q data for multiple channels and returns the data as an array of complex waveforms. This function returns one frame, including the idle interval, at a time. Syntaxint32 __stdcall niWLANG_CreateMIMOWaveformsComplexF64(niWLANGenerationSession session, int32 reset, float64 t0, float64 dt

### niWLANG_CreateMIMOWaveformsComplexF64

Creates WLAN I/Q data for multiple channels and returns the data as an array of complex waveforms. This function returns one frame, including the idle interval, at a time.

#### Syntax

int32 __stdcall niWLANG_CreateMIMOWaveformsComplexF64(niWLANGenerationSession session, int32 reset, float64 t0, float64 dt, NIComplexNumber *waveforms, int32 numberOfTXChains, int32 individualWaveformSize, int32 *actualNumSamplesInEachWfm, int32 *done)

#### Remarks

For multiframe generation, set the reset parameter to NIWLANG_VAL_FALSE and run the function in a loop for the specified number of times or until the done parameter is NIWLANG_VAL_TRUE.

Use this function if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM, NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM, or NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| reset | [in] | int32 | Specifies whether to reset the internal states in the created waveform. Set this parameter to NIWLANG_VAL_TRUE for the first frame of the generation or if you want to reset the pseudonoise (PN) seed. |
| t0 | [out] | float64 | Returns the starting time The size of this array must be at least equal to value of the of the numberOfTxChains parameter. This value is expressed in seconds. |
| dt | [out] | float64 | Returns the time interval between baseband I/Q samples. The size array must be at least equal to value of the the numberOfTXChains parameter. This value is expressed in seconds. |
| waveforms | [out] | NIComplexNumber * | Returns the WLAN I/Q data. The waveforms are written sequentially in the array. Allocate an array at least as large as numberOfTxChains times individualWaveformSize for this parameter. |
| numberOfTXChains | [in] | int32 | Specifies the number of Transmit chains. The value of this parameter should be product of the values configured using the NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS and NIWLANG_ATTR_NUMBER_OF_SEGMENTS attributes. |
| individualWaveformSize | [in] | int32 | Specifies the size of the waveform per WLAN channel. The size of the waveform is given by the NIWLANG_ATTR_IQ_WAVEFORM_SIZE attribute. |
| actualNumSamplesInEachWfm | [out] | int32 * | Returns the actual number of samples for each WLAN channel waveform. If the array is not large enough to hold all the samples, the function returns an error and this parameter returns the minimum expected size of the output array. |
| done | [out] | int32 * | Indicates whether the function has generated all data. If you generate multiple frames, you can include this function in a while loop and use the done parameter as the terminating condition. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1ga11062fa190ae127926bb156f33b9fae3.html language=enus -->
## TOPIC 00081: niWLANG_RFSGConfigureMultipleDeviceSynchronization

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1ga11062fa190ae127926bb156f33b9fae3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1ga11062fa190ae127926bb156f33b9fae3.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures multiple NI RF vector signal generators for sharing the local oscillator (LO), configures Reference Clock settings, and synchronizes multiple devices. For PXIe-5673/5673E/5840/5841/5830/5831 RF vector signal generators, this function configures LO sharing and clock settings in daisy-chain

### niWLANG_RFSGConfigureMultipleDeviceSynchronization

Configures multiple NI RF vector signal generators for sharing the local oscillator (LO), configures Reference Clock settings, and synchronizes multiple devices. For PXIe-5673/5673E/5840/5841/5830/5831 RF vector signal generators, this function configures LO sharing and clock settings in daisy-chained manner. For PXIe-5644, PXIe-5645, and PXIe-5646 RF vector signal transceiver (VST) devices, this function configures daisy-chained LO sharing and low-level properties for multiple device synchronization. These VSTs do not support daisy-chained Reference Clocks for synchronization. You must set the **MasterReferenceClockSource** to PXI_CLK for these devices.

#### Syntax

int32 __stdcall niWLANG_RFSGConfigureMultipleDeviceSynchronization(int32 noOfChannels, ViSession rfsgSessions, niWLANGenerationSession session, ViChar masterReferenceClockSource, int32 triggerLines, int32 noOfTriggerLines)

#### Remarks

For PXIe-5840/5841/5830/5831 RF VST devices, this VI configures daisy-chained LO sharing and Reference Clocks for synchronization, and for PXIe-5820 baseband I/Q VST devices, this VI configures daisy-chained Reference Clocks for synchronization. For additional information, refer to Synchronization Using NI-RFSA and NI-RFSG topic in the NI RF Signal Generators Help.

For PXIe-5842/5860 RF VST devices, this VI configures Reference Clock settings for synchronization and applies NI-TClk trigger configuration for multi-chassis setups. PXIe-5860 does not support LO sharing, and synchronization is achieved through a common reference clock and NI-TClk.

This function assumes that the devices are interconnected in the order of elements in the instrument handles array. In time synchronization, the first device is assumed to be the master device, and the remaining devices are assumed to be slave devices. The devices are divided into two sets when the number of segments are two. In LO sharing, the first device in the each set is assumed to be the master device, and the remaining devices in the set are assumed to be slave devices. To interconnect multiple devices, refer to the following topics in the NI RF Signal Generators Help:

- Interconnecting Multiple PXIe-5673E Modules
- Interconnecting Multiple PXIe-5673 Modules
- Interconnecting Multiple PXIe-5644 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5645 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5646 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5840 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5841 RF Channels (Homogeneous Channel Types)

If you use the PXIe-5644, PXIe-5645, or PXIe-5646 RF vector signal transceiver (VST) devices, the function completes the following actions:

- Sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to the value you specify in **masterReferenceClockSource** parameter.
- If you set the [NIWLANG_ATTR_LO_SHARING_ENABLED](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga5358985c1e7c118659bd9f1b299011ac.html) attribute to NIWLANG_VAL_TRUE, the function completes the following actions:For the master device, the function exports the LO by setting the NIRFSG_ATTR_LO_EXPORT_ENABLED attribute to VI_TRUE. The function also reads the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute so that the value can be set on slave devices.For the slave devices, the function sets the NIRFSG_ATTR_LO_SOURCE attribute to NIRFSG_VAL_LO_IN_STR and the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute to the value read from the master device. With the exception of the last slave device, the function also exports the LO to the next device in the daisy chain by setting the NIRFSG_ATTR_LO_EXPORT_ENABLED attribute to VI_TRUE.
- The function configures the trigger synchronization for the master and slave devices.
- For the master device, the function completes the following actions:Sets the NIRFSG_ATTR_SYNC_START_TRIGGER_MASTER attribute and the NIRFSG_ATTR_SYNC_REF_TRIGGER_MASTER attribute to VI_TRUE. For the PXIe-5646, it sets NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_MASTER attribute to VI_TRUE.Sets the NIRFSG_ATTR_SYNC_START_TRIGGER_DIST_LINE attribute and the NIRFSG_ATTR_SYNC_REF_TRIGGER_DIST_LINE attribute to the first and second element of the **triggerLines** array, respectively. For the PXIe-5646, it sets the NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE attribute to the third element of the **triggerLines** array.Calls the niRFSG_Commit function to commit the synchronization settings to the device.
- For the slave devices, the function completes the following actions:Sets the NIRFSG_ATTR_SYNC_START_TRIGGER_MASTER attribute and NIRFSG_ATTR_SYNC_REF_TRIGGER_MASTER attribute to VI_FALSE. For the PXIe-5646, it sets NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_MASTER attribute to VI_FALSE.Sets the NIRFSG_ATTR_SYNC_START_TRIGGER_DIST_LINE attribute and the NIRFSG_ATTR_SYNC_REF_TRIGGER_DIST_LINE attribute to the first and second element of the **triggerLines** array, respectively. For the PXIe-5646, it sets the NIRFSG_ATTR_SYNC_START_TRIGGER_DIST_LINE attribute to the third element of the **triggerLines** array.Sets the NIRFSG_ATTR_REF_TRIGGER_TYPE attribute to NIRFSG_VAL_DIGITAL_EDGE, the NIRFSG_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE attribute to NIRFSG_VAL_SYNC_REF_TRIGGER_STR, and the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to NIRFSG_VAL_SYNC_START_TRIGGER_STR.

If you use the PXIe-5673/5673E RF vector signal analyzers, the function completes the following actions:

- Configures the devices for daisy-chained Reference Clock synchronization.For the master device, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to the value you specify in **masterReferenceClockSource** and the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_CLK_OUT_STR.For the slave devices, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to NIRFSG_VAL_CLK_IN_STR and the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_CLK_OUT_STR. The function also sets the NIRFSG_ATTR_REF_CLOCK_RATE attribute according to the device model.If [NIWLANG_ATTR_LO_SHARING_ENABLED](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga5358985c1e7c118659bd9f1b299011ac.html) attribute is set to NIWLANG_VAL_TRUE, the function completes the following actions:For the master device, it exports the LO by setting the NIRFSG_ATTR_LO_EXPORT_ENABLED attribute to VI_TRUE. The function also reads the NIRFSG_ATTR_LO_FREQUENCY attribute so that the value can be set on slave devices.For the slave devices, the function sets the NIRFSG_ATTR_LO_SOURCE attribute to NIRFSG_VAL_LO_IN_STR, the NIRFSG_ATTR_LO_FREQUENCY attribute to the value read from the master and exports the LO to the next device in the daisy chain by setting the NIRFSG_ATTR_LO_EXPORT_ENABLED attribute to VI_TRUE.

If you use PXIe-5840, PXIe-5841, PXIe-5830 or PXIe-5831 RF vector signal generators, the function completes the following actions:

- For reference clock synchronization:The function configures all the devices to use PXI_CLK as reference clock if you set the **MasterReferenceClockSource** parameter to NIRFSA_VAL_PXI_CLK_STR.The function configures the devices for daisy-chained reference clock synchronization, if you set the **MasterReferenceClockSource** parameter to a value other than NIRFSA_VAL_PXI_CLK_STR.For the master device, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to the value you specify in the **MasterReferenceClockSource** parameter and sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT_STR.For the slave devices, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to NIRFSG_VAL_REF_IN_STR. Except for the last slave device, this function also sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT_STR.
- If you set the [NIWLANG_ATTR_LO_SHARING_ENABLED](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga5358985c1e7c118659bd9f1b299011ac.html) attribute to NIWLANG_VAL_LO_SHARING_ENABLED_TRUE, the function completes the following actions:For the master device, the function exports the LO by setting the NIRFSG_ATTR_LO_OUT_ENABLED attribute to VI_TRUE. The function also reads the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute so that the value can be set on slave devices.For the slave devices, the function sets the NIRFSG_ATTR_LO_SOURCE attribute to NIRFSG_VAL_LO_IN_STR and the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute to the value read from the master device. Except for the last slave device, this function also exports the LO to the next device in the daisy chain by setting the NIRFSG_ATTR_LO_OUT_ENABLED attribute to VI_TRUE.

If you use PXIe-5842, or PXIe-5860 RF vector signal generators, the function completes the following actions:

- For reference clock synchronization:The function configures all the devices to use PXI_CLK as reference clock if you set the **MasterReferenceClockSource** parameter to NIRFSA_VAL_PXI_CLK_STR.The function configures the devices for daisy-chained reference clock synchronization, if you set the **MasterReferenceClockSource** parameter to a value other than NIRFSA_VAL_PXI_CLK_STR.For the master device, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to the value you specify in the **MasterReferenceClockSource** parameter and sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT_STR.For the slave devices, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to NIRFSG_VAL_REF_IN_STR. Except for the last slave device, this function also sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT_STR.For multi-chassis synchronization:If you set the Multi-Chassis TClk Synchronization Mode attribute to NIWLANG_VAL_MULTI_CHASSIS_TCLK_SYNCHRONIZATION_MODE_TIMING_MODULE, the function performs Multi-Chassis TClk Synchronization using Timing Module.If you set the Multi-Chassis TClk Synchronization Mode attribute to NIWLANG_VAL_MULTI_CHASSIS_TCLK_SYNCHRONIZATION_MODE_AUTO, the function performs Multi-Chassis TClk Synchronization automatically.

If you use PXIe-5820 baseband I/Q vector signal generators, the function completes the following actions:

- For reference clock synchronization:The function configures all the devices to use PXI_CLK as reference clock if you set the **MasterReferenceClockSource** parameter to NIRFSA_VAL_PXI_CLK_STR.The function configures the devices for daisy-chained reference clock synchronization, if you set the **MasterReferenceClockSource** parameter to a value other than NIRFSA_VAL_PXI_CLK_STR.For the master device, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to the value you specify in the **MasterReferenceClockSource** parameter and sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT.For the slave devices, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to NIRFSG_VAL_REF_IN. Except for the last slave device, this function also sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT.

If you use PXIe-5830 or PXIe-5831 RF vector signal generators, the function completes the following actions:

- For reference clock synchronization:The function configures all the devices to use PXI_CLK as reference clock if you set the **MasterReferenceClockSource** parameter to NIRFSA_VAL_PXI_CLK_STR.The function configures the devices for daisy-chained reference clock synchronization, if you set the **MasterReferenceClockSource** parameter to a value other than NIRFSA_VAL_PXI_CLK_STR.For the master device, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to the value you specify in the **MasterReferenceClockSource** parameter and sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT_STR.For the slave devices, the function sets the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute to NIRFSG_VAL_REF_IN_STR. Except for the last slave device, this function also sets the NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL attribute to NIRFSG_VAL_REF_OUT_STR.
- If you set the [NIWLANG_ATTR_LO_SHARING_ENABLED](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga5358985c1e7c118659bd9f1b299011ac.html) attribute to NIWLANG_VAL_LO_SHARING_ENABLED_TRUE, the function completes the following actions:For the master device, the function exports the LO by setting the NIRFSG_ATTR_LO_OUT_ENABLED attribute to VI_TRUE. The function also reads the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute so that the value can be set on slave devices.For the slave devices, the function sets the NIRFSG_ATTR_LO_SOURCE attribute to NIRFSG_VAL_LO_IN_STR and the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute to the value read from the master device. Except for the last slave device, this function also exports the LO to the next device in the daisy chain by setting the NIRFSG_ATTR_LO_OUT_ENABLED attribute to VI_TRUE.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| noOfChannels | [in] | int32 | Specifies the number of Transmit chains. The value of this parameter should be product of the values configured using the NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS and NIWLANG_ATTR_NUMBER_OF_SEGMENTS attributes. |
| rfsgSessions | [in] | ViSession | Specifies an array of references to multiple NI-RFSG instrument sessions. This parameter is obtained from the niRFSG_init or niRFSG_InitWithOptions function and identifies a particular instrument session. |
| session | [in] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| masterReferenceClockSource | [in] | ViChar | Specifies the device Reference Clock to configure on the master NI RF vector signal generator. |
| triggerLines | [in] | int32 | Specifies trigger lines used for distribution of synchronized trigger signals. |
| noOfTriggerLines | [in] | int32 | Specifies the actual number of elements populated in the triggerLines array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1ga3db97979ea79cbe548097be86a8ca1cb.html language=enus -->
## TOPIC 00082: niWLANG_RFSGConfigureFrequencySingleLO

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1ga3db97979ea79cbe548097be86a8ca1cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1ga3db97979ea79cbe548097be86a8ca1cb.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external local oscillator (LO) devices. This function also configures LO frequency offset based on the NIWLANG_ATTR_LO_FREQUENCY_OFFSET_MODE and NIWLANG_ATTR_LO_FREQUENCY_OFFSET attribut

### niWLANG_RFSGConfigureFrequencySingleLO

Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external local oscillator (LO) devices. This function also configures LO frequency offset based on the [NIWLANG_ATTR_LO_FREQUENCY_OFFSET_MODE](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga8548ad08b1937d08a3ac18bde7774cb1.html) and [NIWLANG_ATTR_LO_FREQUENCY_OFFSET](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga0dbd9cd8bc617d68a084e94688dc1de8.html) attributes. It also configures the Signal Bandwidth and IQ Rate attributes on NI RF vector signal generators and the [NIWLANG_ATTR_CARRIER_FREQUENCY](group____root__ni_w_l_a_n_generation__attributes_1gac50607c539fe0c218ca6684f2022046b.html) attribute. You must ensure that after a frequency configuration change, the output of the external LO device settles before generating the WLAN signal. You must use one of the following programming flows:

#### Syntax

int32 __stdcall niWLANG_RFSGConfigureFrequencySingleLO(int16 loSource, int32 numberOfRFSGSessions, ViSession rfsgSessions, niWLANGenerationSession session, ViSession externalLOHandle, float64 carrierFrequency, int32 rfsgLODaisyChainEnabled, int32 loExportToExternalDevicesEnabled)

#### Remarks

- Before calling the [niWLANG_RFSGConfigureFrequencySingleLO](group____root__ni_w_l_a_n_generation__functions_1ga3db97979ea79cbe548097be86a8ca1cb.html) function, if the external LO device is in generation state, ensure that it is brought in configuration state, by stopping signal generation. Initiate signal generation on the external LO device after calling the [niWLANG_RFSGConfigureFrequencySingleLO](group____root__ni_w_l_a_n_generation__functions_1ga3db97979ea79cbe548097be86a8ca1cb.html) function.
- You may choose to do on-the-fly frequency change on the external LO device while the device is in generation state. You must allow it's output to settle by calling the niRFSG_WaitUntilSettled function after the [niWLANG_RFSGConfigureFrequencySingleLO](group____root__ni_w_l_a_n_generation__functions_1ga3db97979ea79cbe548097be86a8ca1cb.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| loSource | [in] | int16 | Specifies whether to use the internal or the external LO source. This value is applicable only for the first RFSG device if the rfsgLODaisyChainEnabled parameter is set to TRUE. The default value is NIWLANG_VAL_LO_SOURCE_ONBOARD.ValueDescriptionNIWLANG_VAL_LO_SOURCE_ONBOARD (0)Uses an internal LO as the LO source.NIWLANG_VAL_LO_SOURCE_EXTERNAL (1)Uses an external LO as the LO source.NIWLANG_VAL_LO_SOURCE_SG_SA_SHARED (2)Shares the internal RFSG LO between RFSG and RFSA. |
| Value | Description |  |  |
| NIWLANG_VAL_LO_SOURCE_ONBOARD (0) | Uses an internal LO as the LO source. |  |  |
| NIWLANG_VAL_LO_SOURCE_EXTERNAL (1) | Uses an external LO as the LO source. |  |  |
| NIWLANG_VAL_LO_SOURCE_SG_SA_SHARED (2) | Shares the internal RFSG LO between RFSG and RFSA. |  |  |
| numberOfRFSGSessions | [in] | int32 | Specifies the number of Transmit chains. The value of this parameter should be product of the values configured using the NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS and NIWLANG_ATTR_NUMBER_OF_SEGMENTS attributes. |
| rfsgSessions | [in] | ViSession | Specifies a reference to an NI-RFSG instrument session. This parameter is obtained from the niRFSG_init or niRFSG_InitWithOptions functions and identifies a particular instrument session. |
| session | [in] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| externalLOHandle | [in] | ViSession | Identifies the instrument session of the external LO device. This parameter is obtained from the niRFSG_Initialize function or the niRFSG_InitializeWithOptions function. |
| carrierFrequency | [in] | float64 | Specifies the carrier frequency used to generate signals. This value is expressed in Hz. |
| rfsgLODaisyChainEnabled | [in] | int32 | Specifies whether to export the LO signal from one RFSG device to the next. The default value is FALSE. |
| loExportToExternalDevicesEnabled | [in] | int32 | Specifies whether to export the LO signal from each RFSG device on its LO OUT terminal, which you can use to share the LO signal with an external device. An example of an external device would be an RFSA device. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1gaa4ac6585af68e929d798599b3a0788fb.html language=enus -->
## TOPIC 00083: niWLANG_CreateWaveformComplexF64

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1gaa4ac6585af68e929d798599b3a0788fb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1gaa4ac6585af68e929d798599b3a0788fb.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates WLAN I/Q data and returns the data as a complex waveform. This function returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset parameter to NIWLANG_VAL_FALSE and run the function in a loop for the specified number of times or until the done param

### niWLANG_CreateWaveformComplexF64

Creates WLAN I/Q data and returns the data as a complex waveform. This function returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset parameter to NIWLANG_VAL_FALSE and run the function in a loop for the specified number of times or until the done parameter is NIWLANG_VAL_TRUE.

#### Syntax

int32 __stdcall niWLANG_CreateWaveformComplexF64(niWLANGenerationSession session, int32 reset, float64 *t0, float64 *dt, NIComplexNumber waveform, int32 waveformSize, int32 *actualNumWaveformSamples, int32 *done)

#### Remarks

Use this function if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| reset | [in] | int32 | Specifies whether to reset the internal states in the created waveform. Set this parameter to NIWLANG_VAL_TRUE for the first frame of the generation or if you want to reset the pseudonoise (PN) seed. |
| t0 | [out] | float64 * | Returns the starting time. This value is expressed in seconds. |
| dt | [out] | float64 * | Returns the time interval between baseband I/Q samples. This value is expressed in seconds. |
| waveform | [out] | NIComplexNumber | Returns the WLAN I/Q data. This parameter must be at least the size of the |
| waveformSize | [in] | int32 | Specifies the waveform size in samples. The size of the waveform is given by the NIWLANG_ATTR_IQ_WAVEFORM_SIZE attribute. |
| actualNumWaveformSamples | [out] | int32 * | Returns the actual number of samples populated in the waveform array. If the array is not large enough to hold all the samples, the function returns an error and this parameter returns the minimum expected size of the output array. |
| done | [out] | int32 * | Indicates whether the function has generated all the data. If you generate multiple frames, you can include this function in a while loop and use the done parameter as the terminating condition. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1gac01b3647720fa1c34404451db16cf0a7.html language=enus -->
## TOPIC 00084: niWLANG_RFSGConfigureFrequencyMultipleLO

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1gac01b3647720fa1c34404451db16cf0a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1gac01b3647720fa1c34404451db16cf0a7.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external LO devices. This function also configures LO frequency offset based on the NIWLANG_ATTR_LO_FREQUENCY_OFFSET_MODE and NIWLANG_ATTR_LO_FREQUENCY_OFFSET attributes. This function e

### niWLANG_RFSGConfigureFrequencyMultipleLO

Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external LO devices. This function also configures LO frequency offset based on the [NIWLANG_ATTR_LO_FREQUENCY_OFFSET_MODE](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga8548ad08b1937d08a3ac18bde7774cb1.html) and [NIWLANG_ATTR_LO_FREQUENCY_OFFSET](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga0dbd9cd8bc617d68a084e94688dc1de8.html) attributes. This function equally divides the NI RF vector signal generators and NI RF synthesizers into sets such that each set corresponds to one carrier frequency. The number of sets is equal to the size of the carrier frequencies array. In each set, the first NI RF vector signal generator is used as the master device for LO daisy chaining. It also configures the Signal Bandwidth and IQ Rate attributes on NI RF vector signal generators and the [NIWLANG_ATTR_CARRIER_FREQUENCY](group____root__ni_w_l_a_n_generation__attributes_1gac50607c539fe0c218ca6684f2022046b.html) attribute. You must ensure that after a frequency configuration change, the output of the external LO device settles before generating the WLAN signal. You must use one of the following programming flows:

#### Syntax

int32 __stdcall niWLANG_RFSGConfigureFrequencyMultipleLO(int16 loSource, int32 numberOfRFSGSessions, ViSession rfsgSessions, niWLANGenerationSession session, ViSession externalLOHandles, int32 numberOfExternalLOHandles, float64 carrierFrequency, int32 dataArraySize, int32 rfsgLODaisyChainEnabled, int32 loExportToExternalDevicesEnabled)

#### Remarks

- Before calling the [niWLANG_RFSGConfigureFrequencyMultipleLO](group____root__ni_w_l_a_n_generation__functions_1gac01b3647720fa1c34404451db16cf0a7.html) function, if the external LO device is in generation state, ensure that it is brought in configuration state, by stopping signal generation. Initiate signal generation on the external LO device after calling the [niWLANG_RFSGConfigureFrequencyMultipleLO](group____root__ni_w_l_a_n_generation__functions_1gac01b3647720fa1c34404451db16cf0a7.html) function.
- You may choose to do on-the-fly frequency change on the external LO device while the device is in generation state. You must allow it's output to settle by calling the niRFSG_WaitUntilSettled function after the [niWLANG_RFSGConfigureFrequencyMultipleLO](group____root__ni_w_l_a_n_generation__functions_1gac01b3647720fa1c34404451db16cf0a7.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| loSource | [in] | int16 | Specifies whether to use the internal or the external LO source. This value is applicable only for the first RFSG device within a set if the rfsgLODaisyChainEnabled parameter is set to TRUE. The default value is NIWLANG_VAL_LO_SOURCE_ONBOARD.ValueDescriptionNIWLANG_VAL_LO_SOURCE_ONBOARD (0)Uses an internal LO as the LO source.NIWLANG_VAL_LO_SOURCE_EXTERNAL (1)Uses an external LO as the LO source.NIWLANG_VAL_LO_SOURCE_SGSA_SHARED (2)Shares the internal RFSG LO between RFSG and RFSA. |
| Value | Description |  |  |
| NIWLANG_VAL_LO_SOURCE_ONBOARD (0) | Uses an internal LO as the LO source. |  |  |
| NIWLANG_VAL_LO_SOURCE_EXTERNAL (1) | Uses an external LO as the LO source. |  |  |
| NIWLANG_VAL_LO_SOURCE_SGSA_SHARED (2) | Shares the internal RFSG LO between RFSG and RFSA. |  |  |
| numberOfRFSGSessions | [in] | int32 | Specifies the number of Transmit chains. The value of this parameter should be product of the values configured using the NIWLANG_ATTR_NUMBER_OF_TRANSMIT_CHANNELS and NIWLANG_ATTR_NUMBER_OF_SEGMENTS attributes. |
| rfsgSessions | [in] | ViSession | Specifies a reference to an NI-RFSG instrument session. This parameter is obtained from the niRFSG_init or niRFSG_InitWithOptions functions and identifies a particular instrument session. |
| session | [in] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| externalLOHandles | [in] | ViSession | Identifies the instrument sessions of external LO devices. This parameter is obtained from the niRFSG_init or niRFSG_InitWithOptions functions. |
| numberOfExternalLOHandles | [in] | int32 | Specifies the number of external LO handles. |
| carrierFrequency | [in] | float64 | Specifies an array of the carrier frequencies used to generate signals. This value is expressed in Hz. |
| dataArraySize | [in] | int32 | Specifies the number of elements in the carrierFrequency array. This value should be the same as the value you set for the NIWLANG_ATTR_NUMBER_OF_SEGMENTS attribute. |
| rfsgLODaisyChainEnabled | [in] | int32 | Specifies whether to export the LO signal from one RFSG device to the next. The default value is FALSE. |
| loExportToExternalDevicesEnabled | [in] | int32 | Specifies whether to export the LO signal from each RFSG device on its LO OUT terminal, which you can use to share the LO signal with an external device. An example of an external device would be an RFSA device. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1gad8162ab44e954479a80e4cb111edc330.html language=enus -->
## TOPIC 00085: niWLANG_CloseSession

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1gad8162ab44e954479a80e4cb111edc330.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1gad8162ab44e954479a80e4cb111edc330.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the niWLAN generation session and releases resources associated with that session. Call this function once for each unique named session that you have created. Syntaxint32 __stdcall niWLANG_CloseSession(niWLANGenerationSession session)ParametersNameDirectionTypeDescriptionsession[out]niWLANGe

### niWLANG_CloseSession

Closes the niWLAN generation session and releases resources associated with that session. Call this function once for each unique named session that you have created.

#### Syntax

int32 __stdcall niWLANG_CloseSession(niWLANGenerationSession session)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html language=enus -->
## TOPIC 00086: niWLANG_OpenSession

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Looks up an existing niWLAN generation session using the sessionName parameter and returns the refnum that you can pass to subsequent niWLAN generation functions. If the lookup fails, the niWLANG_OpenSession function creates a new niWLAN generation session and returns a new refnum. Syntaxint32 __std

### niWLANG_OpenSession

Looks up an existing niWLAN generation session using the **sessionName** parameter and returns the refnum that you can pass to subsequent niWLAN generation functions. If the lookup fails, the [niWLANG_OpenSession](group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html) function creates a new niWLAN generation session and returns a new refnum.

#### Syntax

int32 __stdcall niWLANG_OpenSession(ViChar sessionName, int32 compatibilityVersion, niWLANGenerationSession *session, int32 *isNewSession)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| sessionName | [out] | ViChar | Specifies the name of the session that you are looking up or creating. If a session with the same name already exists, this function returns a reference to that session. To get the reference to an already-opened session x, specify x as the session name.You can obtain the reference to an existing session multiple times if you have not called the niWLANG_CloseSession function in that session. You do not need to close the session multiple times. To create an unnamed session, pass an empty string or NULL to the sessionName parameter.Tip- NI recommends that you call the niWLANG_CloseSession function for each unique named instance of the niWLANG_OpenSession function or each instance of the niWLANG_OpenSession function with an unnamed session. |
| compatibilityVersion | [in] | int32 | Specifies the version of the WLAN Generation to which the current version of the WLAN Generation is compatible. If the behavior of the WLAN Generation changes in a new version, use this parameter to specify that you want to continue using the behavior of the previous release. The default value is NIWLANG_VAL_COMPATIBILITY_VERSION_050000.ValueDescriptionNIWLANG_VAL_COMPATIBILITY_VERSION_010000 (10000)Specifies that the WLAN Generation exhibits version 1.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 1.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 1.0.0 and later versions.NIWLANG_VAL_COMPATIBILITY_VERSION_020000 (20000)Specifies that the WLAN Generation exhibits version 2.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 2.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 1.0.0 and 2.0.0.NIWLANG_VAL_COMPATIBILITY_VERSION_030000 (30000)Specifies that the WLAN Generation exhibits version 3.0.0 behavior. Select this option to if you want 3.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 2.0.0 and 3.0.0.NIWLANG_VAL_COMPATIBILITY_VERSION_040000 (40000)Specifies that the WLAN Generation exhibits version 4.0.0 behavior. Select this option to if you want 4.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 3.0.0 and 4.0.0.NIWLANG_VAL_COMPATIBILITY_VERSION_050000(50000)Specifies that the WLAN Generation exhibits version 5.0.0 behavior. Select this option to if you want 5.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 4.0.0 and 5.0.0.NIWLANG_VAL_COMPATIBILITY_VERSION_060000 (60000)Specifies that the WLAN Generation exhibits version 6.0.0 behavior. Select this option to if you want 6.0.0 behavior and access to new features and bug fixes. Refer the to RFmx WLAN Generation Readme for a list of changes between versions 5.0.0 and 6.0.0. |
| Value | Description |  |  |
| NIWLANG_VAL_COMPATIBILITY_VERSION_010000 (10000) | Specifies that the WLAN Generation exhibits version 1.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 1.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 1.0.0 and later versions. |  |  |
| NIWLANG_VAL_COMPATIBILITY_VERSION_020000 (20000) | Specifies that the WLAN Generation exhibits version 2.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 2.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 1.0.0 and 2.0.0. |  |  |
| NIWLANG_VAL_COMPATIBILITY_VERSION_030000 (30000) | Specifies that the WLAN Generation exhibits version 3.0.0 behavior. Select this option to if you want 3.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 2.0.0 and 3.0.0. |  |  |
| NIWLANG_VAL_COMPATIBILITY_VERSION_040000 (40000) | Specifies that the WLAN Generation exhibits version 4.0.0 behavior. Select this option to if you want 4.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 3.0.0 and 4.0.0. |  |  |
| NIWLANG_VAL_COMPATIBILITY_VERSION_050000(50000) | Specifies that the WLAN Generation exhibits version 5.0.0 behavior. Select this option to if you want 5.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 4.0.0 and 5.0.0. |  |  |
| NIWLANG_VAL_COMPATIBILITY_VERSION_060000 (60000) | Specifies that the WLAN Generation exhibits version 6.0.0 behavior. Select this option to if you want 6.0.0 behavior and access to new features and bug fixes. Refer the to RFmx WLAN Generation Readme for a list of changes between versions 5.0.0 and 6.0.0. |  |  |
| session | [out] | niWLANGenerationSession * | Returns the niWLAN generation session refnum. Use this parameter to configure the behavior and operation of the appropriate RFmx WLAN Generation functions that accept the session reference as an input.Close the niWLAN generation session reference using the niWLANG Close Session function before the completion of execution to avoid possible memory leak issues. |
| isNewSession | [out] | int32 * | Indicates whether the function creates a new session.ValueDescriptionNIWLANG_VAL_FALSE (0)Indicates that the function returns a reference to an existing session.NIWLANG_VAL_TRUE (1)Indicates that the function creates a new session. |
| Value | Description |  |  |
| NIWLANG_VAL_FALSE (0) | Indicates that the function returns a reference to an existing session. |  |  |
| NIWLANG_VAL_TRUE (1) | Indicates that the function creates a new session. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1gadd29fd788a857bdc9849dce844e487ae.html language=enus -->
## TOPIC 00087: niWLANG_RFSGMultipleDeviceInitiate

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1gadd29fd788a857bdc9849dce844e487ae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1gadd29fd788a857bdc9849dce844e487ae.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to hardware, waits for hardware settling, and starts multi-device synchronized generation. Syntaxint32 __stdcall niWLANG_RFSGMultipleDeviceInitiate(int32 numberOfRFSGSessions, ViSession rfsgSessions, niWLANGenerationSession session)RemarksIf you use PXIe-5644, PXIe-5645, or PXIe-564

### niWLANG_RFSGMultipleDeviceInitiate

Commits settings to hardware, waits for hardware settling, and starts multi-device synchronized generation.

#### Syntax

int32 __stdcall niWLANG_RFSGMultipleDeviceInitiate(int32 numberOfRFSGSessions, ViSession rfsgSessions, niWLANGenerationSession session)

#### Remarks

If you use PXIe-5644, PXIe-5645, or PXIe-5646, this function performs the following steps:

- Commits the device settings to the master device by calling the niRFSG Commit function.
- Initializes generation first for slave devices and then for the master device by calling the niRFSG Initiate function in a loop.

If you use PXIe-5673/5673E, PXIe-5840, PXIe-5841, PXIe-5820, PXIe-5830, PXIe-5831, PXIe-5842, or PXIe-5860, this function performs the following steps:

- If number of devices required is more than 1, this function uses the niWLANG RFSG Configure TClk For Homogeneous Triggers function, niWLANG RFSG Synchronize TClk function, and the niTClk Initiate function for synchronized generation. Refer to the NI-TClk Synchronization section of NI RF Vector Signal Generators help for more information about the niTClk functions.
- Otherwise, this function calls the niRFSG Initiate function for the first device.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| numberOfRFSGSessions | [in] | int32 | Passes a reference of the WLAN generation session to the next function. |
| rfsgSessions | [in] | ViSession | Specifies a reference to an NI-RFSG instrument session. This parameter is obtained from the niRFSG_init or niRFSG_InitWithOptions functions and identifies a particular instrument session. |
| session | [in] | niWLANGenerationSession | Specifies the niWLAN generation session. Close the niWLAN generation session reference using the niWLANG_CloseSession function before the completion of execution to avoid possible memory leak issues. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions_1gae637fff72e290ccdfdfa7a5dd2b1f691.html language=enus -->
## TOPIC 00088: niWLANG_ResetSession

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions_1gae637fff72e290ccdfdfa7a5dd2b1f691.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions_1gae637fff72e290ccdfdfa7a5dd2b1f691.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all the attributes of the session to their default values. Syntaxint32 __stdcall niWLANG_ResetSession(niWLANGenerationSession session)ParametersNameDirectionTypeDescriptionsession[out]niWLANGenerationSessionSpecifies the niWLAN generation session. ReturnsReturns the status code of this operat

### niWLANG_ResetSession

Resets all the attributes of the session to their default values.

#### Syntax

int32 __stdcall niWLANG_ResetSession(niWLANGenerationSession session)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation.html language=enus -->
## TOPIC 00089: Configure Generation

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsGet and Set AttributesGroup membersNameDescriptionniWLANG_Set80211AhPreambleTypeSpecifies the preamble type of packet. niWLANG_Set80211NPLCPFrameFormatSpecifies the format of the physical layer convergence protocol (PLCP) frame structure. niWLANG_SetAutoHeadroomEnabledSpecifies whether the WLA

### Configure Generation

#### Groups

- Get and Set Attributes

#### Group members

| Name | Description |
| --- | --- |
| niWLANG_Set80211AhPreambleType | Specifies the preamble type of packet. |
| niWLANG_Set80211NPLCPFrameFormat | Specifies the format of the physical layer convergence protocol (PLCP) frame structure. |
| niWLANG_SetAutoHeadroomEnabled | Specifies whether the WLAN Generation calculates the headroom or uses the value that you specify. For multiframe generation, the WLAN Generation uses the headroom calculated on the first frame to scale the waveform for every frame. NI recommends that you do not set the enabled parameter to NIWLANG_VAL_TRUE for multiframe generation because variation of the peak-to-average power ratio (PAPR) across frames may lead to excessive clipping. To avoid excessive clipping, set the enabled parameter to NIWLANG_VAL_FALSE and use the default values for the NIWLANG_ATTR_HEADROOM attribute. |
| niWLANG_SetChannelBandwidth | Specifies the channel width used for transmitting the signal. This value is expressed in Hz. |
| niWLANG_SetDSSSDataRate | Specifies the data rate for the direct sequence spread spectrum (DSSS) payload, as defined in IEEE Standard 802.11b-1999 and the extended rate physical layer-packet binary convolutional coding (ERP-PBCC) mode in IEEE Standard 802.11g-2003. |
| niWLANG_SetDSSSPreambleType | Specifies whether to use a long or short preamble for direct sequence spread spectrum (DSSS) and DSSS-OFDM packets as defined in IEEE Standard 802.11b-1999. |
| niWLANG_SetHeadroom | Specifies the headroom for each transmit channel. This value represents the maximum peak-to-average power ratio (PAPR) allowed in the generated signal. The WLAN Generation clips any portion of the signal that exceeds the peak power corresponding to this value. The WLAN Generation ignores the headroom parameter set by this function if you set the enabled parameter of the niWLANG_SetAutoHeadroomEnabled function to NIWLANG_VAL_TRUE. If you set the enabled parameter to NIWLANG_VAL_FALSE, the WLAN Generation uses default values based on the niWLANG_SetStandard function. |
| niWLANG_SetIdleInterval | Specifies the interframe spacing for signal generation. If you set the NIWLANG_ATTR_RF_BLANKING_ENABLED attribute to NIWLANG_VAL_FALSE, the WLAN Generation places half of the interframe spacing on either side of the burst in the generated waveform. If you set the NIWLANG_ATTR_RF_BLANKING_ENABLED attribute to NIWLANG_VAL_TRUE, the WLAN Generation places the interframe spacing at the end of the waveform. The waveform contains zeros for the duration of the interframe spacing. |
| niWLANG_SetMCSIndex | Specifies the value of the modulation and coding scheme (MCS) index. |
| niWLANG_SetMappingMatrix | Specifies the matrix for mapping space-time streams to the transmit channels as specified in section 20.3.11.10.1 of IEEE Standard 802.11n-2009. |
| niWLANG_SetMappingMatrixType | Specifies the mapping matrix type for mapping space-time streams to transmit channels as defined in section 20.3.11.10.1 of IEEE Standard 802.11n-2009. |
| niWLANG_SetNumberOfFrames | Specifies the number of frames to generate. Each iteration of the niWLANG_CreateWaveformComplexF64 or niWLANG_CreateMIMOWaveformsComplexF64 function generates only one frame along with the idle interval that you specify using the NIWLANG_ATTR_IDLE_INTERVAL attribute. |
| niWLANG_SetNumberOfTransmitChannels | Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of IEEE Standard 802.11n-2009. |
| niWLANG_SetOFDMDataRate | Specifies the data rate for the OFDM payload, as defined in section 17.3.2.2 of IEEE Standard 802.11a-1999. This value is expressed is Mbps. |
| niWLANG_SetOFDMGuardIntervalType | Specifies the type of guard interval (cyclic prefix) in a OFDM symbol. |
| niWLANG_SetOFDMPacketExtensionThresholds | Configures the packet extension (PE) thresholds that determine the nominal packet padding of the 802.11ax, 802.11be or 802.11bn signal. This function configures the thresholds for each resource unit (RU) size and each space-time stream of the 802.11ax, 802.11be or 802.11bn DUT. You must configure this table based on the nominal packet padding requirements of the DUT. |
| niWLANG_SetOverSamplingRatio | Specifies the number of times the WLAN Generation increases the Nyquist sample rate to obtain the final sample rate of the signal. |
| niWLANG_SetSTBCIndex | Specifies the difference between the number of space-time streams and the number of spatial streams, as defined in section 20.3.9.4.3 of IEEE Standard 802.11n-2009. The WLAN Generation derives the number of spatial streams from the specified value of the NIWLANG_ATTR_MCS_INDEX attribute. Different space-time coding schemes are defined in section 20.3.11.8.1 of IEEE Standard 802.11n-2009. |
| niWLANG_SetStandard | Specifies the IEEE 802.11 standard, which indicates the type of physical layer, for signal generation. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga078d6caa8ad51d76427f1f46885cc76b.html language=enus -->
## TOPIC 00090: niWLANG_SetOFDMPacketExtensionThresholds

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga078d6caa8ad51d76427f1f46885cc76b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga078d6caa8ad51d76427f1f46885cc76b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the packet extension (PE) thresholds that determine the nominal packet padding of the 802.11ax, 802.11be or 802.11bn signal. This function configures the thresholds for each resource unit (RU) size and each space-time stream of the 802.11ax, 802.11be or 802.11bn DUT. You must configure th

### niWLANG_SetOFDMPacketExtensionThresholds

Configures the packet extension (PE) thresholds that determine the nominal packet padding of the 802.11ax, 802.11be or 802.11bn signal. This function configures the thresholds for each resource unit (RU) size and each space-time stream of the 802.11ax, 802.11be or 802.11bn DUT. You must configure this table based on the nominal packet padding requirements of the DUT.

#### Syntax

int32 __stdcall niWLANG_SetOFDMPacketExtensionThresholds(niWLANGenerationSession session, ViChar channelString, int32 ppet16, int32 ppet8, int32 numberOfSpaceTimeStreams, int32 ruSize, int32 ppet16ArraySize, int32 ppet8ArraySize, int32 numberOfSpaceTimeStreamsArraySize, int32 ruArraySize)

#### Remarks

The PE field of in 802.11ax, 802.11be or 802.11bn signal provides additional processing time to the receiver to decode the last symbol. The possible durations of the PE field are 0 microseconds, 4 microseconds, 8 microseconds, 12 microseconds, 16 microseconds, or 20 microseconds. The PE duration is determined by both the pre-FEC padding factor of the data field, and the nominal packet padding requested by the recipient, and the modulation scheme of the current PPDU. The nominal packet padding as defined by the HE/EHT/UHR Capabilities element are 0 microseconds, 8 microseconds, 16 microseconds, and 20 microseconds, which can be specified using this function.

The nominal packet padding is computed by comparing the constellation index and the threshold values. Packet extension device capability threshold values are defined for all RU sizes greater than or equal to 242 tones. No thresholds are defined for an RU size less than 242 tones. The supported constellations are assigned with a unique index value as shown in following table.

| Modulation Scheme | Constellation Index Value |
| --- | --- |
| BPSK | 0 |
| QPSK | 1 |
| 16-QAM | 2 |
| 64-QAM | 3 |
| 256-QAM | 4 |
| 1024-QAM | 5 |
| 4096-QAM | 6 |
| None | 7 |

1. Nominal PE mode 8 microseconds: PE duration is 0, 0, 4, and 8 microseconds for pre-FEC padding factor of 1, 2, 3, and 4 respectively.
2. Nominal PE mode 16 microseconds: PE duration is 4, 8, 12, and 16 microseconds for pre-FEC padding factor of 1, 2, 3, and 4 respectively.
3. Nominal PE mode 20 microseconds: PE duration is 8, 12, 16, and 20 microseconds for pre-FEC padding factor of 1, 2, 3, and 4 respectively.

- If the constellation is greater than or equal to PPET16, you must apply the value of the maximum PPET16 parameter, or if the constellation is greater than or equal to PPET8, you must apply the value of the maximum **ppet8** parameter; otherwise, there is no packet extension.
- If no PE is required for all constellations, set **ppet8** and **ppet16** to "" (empty array).
- If only the nominal PE 8 microseconds mode is required, set **ppet16** to be "" (empty array), and **ppet8** to be the constellation at which max PE 8 microseconds mode starts.
- If only the nominal PE 16 microseconds mode is required, set **ppet16** to be the constellation at which max PE 16 microseconds mode starts, and **ppet8** to be "" (empty array).

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| ppet16 | [out] | int32 | Specifies the 16 microsecond mode PE threshold values. The default value is "" (empty array). |
| ppet8 | [out] | int32 | Specifies the 8 microsecond mode PE threshold values. The default value is "" (empty array). |
| numberOfSpaceTimeStreams | [out] | int32 | Specifies the number of space-time streams for the corresponding RU size. The default value is "" (empty array). |
| ruSize | [out] | int32 | Specifies the size of the RU in terms of the number of subcarriers. The default value is "" (empty array). |
| ppet16ArraySize | [in] | int32 | Specifies the size of PPET16 array. |
| ppet8ArraySize | [in] | int32 | Specifies the size of PPET8 array. |
| numberOfSpaceTimeStreamsArraySize | [in] | int32 | Specifies the size of numberOfSpaceTimeStreams array. |
| ruArraySize | [in] | int32 | Specifies the size of RU size array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga1dddbaa36ba93405e5cf890bcfb66d44.html language=enus -->
## TOPIC 00091: niWLANG_SetMappingMatrixType

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga1dddbaa36ba93405e5cf890bcfb66d44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga1dddbaa36ba93405e5cf890bcfb66d44.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mapping matrix type for mapping space-time streams to transmit channels as defined in section 20.3.11.10.1 of IEEE Standard 802.11n-2009. Syntaxint32 __stdcall niWLANG_SetMappingMatrixType(niWLANGenerationSession session, ViChar channelString, int32 mappingMatrixType)RemarksIf you set

### niWLANG_SetMappingMatrixType

Specifies the mapping matrix type for mapping space-time streams to transmit channels as defined in section 20.3.11.10.1 of IEEE Standard 802.11n-2009.

#### Syntax

int32 __stdcall niWLANG_SetMappingMatrixType(niWLANGenerationSession session, ViChar channelString, int32 mappingMatrixType)

#### Remarks

If you set this function to values other than NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT, the number of transmit channels must be greater than or equal to the sum of the number of space-time streams and the [NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS](group____root__ni_w_l_a_n_generation__attributes__mimo_1gaf6714a8f66c7ea52ec872c6e43aeb940.html) attribute if the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute is set to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| mappingMatrixType | [in] | int32 | Specifies the mapping matrix type for mapping space-time streams to transmit channels.The default value is NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT.Mapping Matrix TypeDescriptionNIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT (0)Specifies direct mapping for space-time streams. The direct mapping matrix is given by NTx = NSTS. Direct mapping matrix is derived by taking the subset (NSTS× NSTS) of the 8 × 8 identity matrix. Where: NTx is the number of transmit channels.NSTS is the number of space-time streams.If the NIWLANG_ATTR_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, this value is determined by the modulation and coding scheme (MCS) index and space-time block coding (STBC) index. Example: A 4 × 4 identity matrix:NIWLANG_VAL_MAPPING_MATRIX_TYPE_HADAMARD (1)Specifies Hadamard mapping for space-time streams and extension spatial streams. The Hadamard mapping matrix is of size NTx× (NSTS + NESS), where NTx≥ (NSTS + NESS), if the NIWLANG_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM. For other standards (e.g., 80211AC, 80211AX, etc.), NTx≥ NSTS. Where: NTx: Number of transmit channels.NSTS: Number of space-time streams (determined by the MCS index and STBC index).NESS: Number of extension spatial streams. Example: A 4 × 4 Hadamard matrix:NIWLANG_VAL_MAPPING_MATRIX_TYPE_FOURIER (2)Specifies Fourier mapping for space-time streams and extension spatial streams. The Fourier mapping matrix is defined as: Where: n = 0 ... (N - 1).N = NTx, where NTx is the number of transmit channels.k = 0 ... ((NSTS + NESS) - 1), or k = 0 ... (NSTS - 1) for certain standards.NSTS: Number of space-time streams (determined by the MCS index and STBC index).NESS: Number of extension spatial streams. Examples: Fourier matrices for 2 × 2, 3 × 3, and 4 × 4:NIWLANG_VAL_MAPPING_MATRIX_TYPE_USER_DEFINED (3)Specifies user-defined mapping for space-time streams and extension spatial streams. You can set this matrix using the niWLANG_SetMappingMatrix function. |
| Mapping Matrix Type | Description |  |  |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT (0) | Specifies direct mapping for space-time streams. The direct mapping matrix is given by NTx = NSTS. Direct mapping matrix is derived by taking the subset (NSTS× NSTS) of the 8 × 8 identity matrix. Where: NTx is the number of transmit channels.NSTS is the number of space-time streams.If the NIWLANG_ATTR_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM, this value is determined by the modulation and coding scheme (MCS) index and space-time block coding (STBC) index. Example: A 4 × 4 identity matrix: |  |  |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_HADAMARD (1) | Specifies Hadamard mapping for space-time streams and extension spatial streams. The Hadamard mapping matrix is of size NTx× (NSTS + NESS), where NTx≥ (NSTS + NESS), if the NIWLANG_STANDARD attribute is set to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM. For other standards (e.g., 80211AC, 80211AX, etc.), NTx≥ NSTS. Where: NTx: Number of transmit channels.NSTS: Number of space-time streams (determined by the MCS index and STBC index).NESS: Number of extension spatial streams. Example: A 4 × 4 Hadamard matrix: |  |  |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_FOURIER (2) | Specifies Fourier mapping for space-time streams and extension spatial streams. The Fourier mapping matrix is defined as: Where: n = 0 ... (N - 1).N = NTx, where NTx is the number of transmit channels.k = 0 ... ((NSTS + NESS) - 1), or k = 0 ... (NSTS - 1) for certain standards.NSTS: Number of space-time streams (determined by the MCS index and STBC index).NESS: Number of extension spatial streams. Examples: Fourier matrices for 2 × 2, 3 × 3, and 4 × 4: |  |  |
| NIWLANG_VAL_MAPPING_MATRIX_TYPE_USER_DEFINED (3) | Specifies user-defined mapping for space-time streams and extension spatial streams. You can set this matrix using the niWLANG_SetMappingMatrix function. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga2cb76350d2aba540004bd5b41ba0894b.html language=enus -->
## TOPIC 00092: niWLANG_SetNumberOfTransmitChannels

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga2cb76350d2aba540004bd5b41ba0894b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga2cb76350d2aba540004bd5b41ba0894b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of IEEE Standard 802.11n-2009. Syntaxint32 __stdcall niWLANG_SetNumberOfTransmitChannels(niWLANGenerationSession session, ViChar channelString, int32 numberOfTransmitChannels)Rem

### niWLANG_SetNumberOfTransmitChannels

Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of IEEE Standard 802.11n-2009.

#### Syntax

int32 __stdcall niWLANG_SetNumberOfTransmitChannels(niWLANGenerationSession session, ViChar channelString, int32 numberOfTransmitChannels)

#### Remarks

The number of transmit channels must be greater than or equal to the number of space-time streams if you set the [NIWLANG_ATTR_MAPPING_MATRIX_TYPE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html) attribute to NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT. If you set the [NIWLANG_ATTR_MAPPING_MATRIX_TYPE](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga589319fa889660fda35e6e024603da98.html) attribute to values other than NIWLANG_VAL_MAPPING_MATRIX_TYPE_DIRECT, the number of transmit channels must be greater than or equal to the sum of the number of space-time streams and the [NIWLANG_ATTR_NUMBER_OF_EXTENSION_SPATIAL_STREAMS](group____root__ni_w_l_a_n_generation__attributes__mimo_1gaf6714a8f66c7ea52ec872c6e43aeb940.html) attribute. The WLAN Generation defines the number of space-time streams using the [NIWLANG_ATTR_MCS_INDEX](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga5ff81d7f7fae518b786a3bc909ef372c.html) attribute and the [NIWLANG_ATTR_STBC_INDEX](group____root__ni_w_l_a_n_generation__attributes__mimo_1ga6f375c08a44794251d8f09eed2f48ad2.html) attribute as specified in IEEE Standard 802.11n-2009.

If you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM, NIWLANG_VAL_STANDARD_80211BG_DSSS, or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM and the [niWLANG_SetNumberOfTransmitChannels](group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga2cb76350d2aba540004bd5b41ba0894b.html) function to greater than one, the same waveform is generated on multiple RFSG devices inside the [niWLANG_RFSGCreateAndDownloadMIMOWaveforms](group____root__ni_w_l_a_n_generation__functions__rfsg__database__retrieve_1ga649cf1856a36effe23b5ba140fe217e9.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| numberOfTransmitChannels | [in] | int32 | Specifies the number of transmit channels for MIMO signals. The default value is 1. If you set the NIWLANG_ATTR_STANDARD attribute to NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM or NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM, the valid values are 1 to 4, inclusive. If you set the NIWLANG_ATTR_STANDARD attribute to any other value, the valid values are 1 to 8, inclusive. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga3a1fc57779ed8ae14e8610200f7d3a6a.html language=enus -->
## TOPIC 00093: niWLANG_SetDSSSDataRate

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga3a1fc57779ed8ae14e8610200f7d3a6a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga3a1fc57779ed8ae14e8610200f7d3a6a.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data rate for the direct sequence spread spectrum (DSSS) payload, as defined in IEEE Standard 802.11b-1999 and the extended rate physical layer-packet binary convolutional coding (ERP-PBCC) mode in IEEE Standard 802.11g-2003. Syntaxint32 __stdcall niWLANG_SetDSSSDataRate(niWLANGenerati

### niWLANG_SetDSSSDataRate

Specifies the data rate for the direct sequence spread spectrum (DSSS) payload, as defined in IEEE Standard 802.11b-1999 and the extended rate physical layer-packet binary convolutional coding (ERP-PBCC) mode in IEEE Standard 802.11g-2003.

#### Syntax

int32 __stdcall niWLANG_SetDSSSDataRate(niWLANGenerationSession session, ViChar channelString, int32 dsssDataRate)

#### Remarks

Configure this function only if you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211BG_DSSS.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| dsssDataRate | [in] | int32 | Specifies the data rate for the DSSS payload. The default value is NIWLANG_VAL_DSSS_DATA_RATE_1.ValueDescriptionNIWLANG_VAL_DSSS_DATA_RATE_1 (0)Specifies a data rate of 1, as defined in sections 18.4.6.3 and 18.4.6.4 of IEEE Standard 802.11b-1999.NIWLANG_VAL_DSSS_DATA_RATE_2 (1)Specifies a data rate of 2, as defined in sections 18.4.6.3 and 18.4.6.4 of IEEE Standard 802.11b-1999.NIWLANG_VAL_DSSS_DATA_RATE_5P5_CCK (2)Specifies a data rate of 5.5 complementary code keying (CCK), as defined in section 18.4.6.5 of IEEE Standard 802.11b-1999.NIWLANG_VAL_DSSS_DATA_RATE_5P5_PBCC (3)Specifies a data rate of 5.5 PBCC, as defined in section 18.4.6.6 of IEEE Standard 802.11b-1999.NIWLANG_VAL_DSSS_DATA_RATE_11_CCK (4)Specifies a data rate of 11 CCK, as defined in section 18.4.6.5 of IEEE Standard 802.11b-1999.NIWLANG_VAL_DSSS_DATA_RATE_11_PBCC (5)Specifies a data rate of 11 PBCC, as defined in section 18.4.6.6 of IEEE Standard 802.11b-1999.NIWLANG_VAL_DSSS_DATA_RATE_22 (6)Specifies a data rate of 22, as defined in section 19.3.3.2 of IEEE Standard 802.11g-2003.NIWLANG_VAL_DSSS_DATA_RATE_33 (7)Specifies a data rate of 33, as defined in section 19.3.3.2 of IEEE Standard 802.11g-2003. |
| Value | Description |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_1 (0) | Specifies a data rate of 1, as defined in sections 18.4.6.3 and 18.4.6.4 of IEEE Standard 802.11b-1999. |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_2 (1) | Specifies a data rate of 2, as defined in sections 18.4.6.3 and 18.4.6.4 of IEEE Standard 802.11b-1999. |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_5P5_CCK (2) | Specifies a data rate of 5.5 complementary code keying (CCK), as defined in section 18.4.6.5 of IEEE Standard 802.11b-1999. |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_5P5_PBCC (3) | Specifies a data rate of 5.5 PBCC, as defined in section 18.4.6.6 of IEEE Standard 802.11b-1999. |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_11_CCK (4) | Specifies a data rate of 11 CCK, as defined in section 18.4.6.5 of IEEE Standard 802.11b-1999. |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_11_PBCC (5) | Specifies a data rate of 11 PBCC, as defined in section 18.4.6.6 of IEEE Standard 802.11b-1999. |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_22 (6) | Specifies a data rate of 22, as defined in section 19.3.3.2 of IEEE Standard 802.11g-2003. |  |  |
| NIWLANG_VAL_DSSS_DATA_RATE_33 (7) | Specifies a data rate of 33, as defined in section 19.3.3.2 of IEEE Standard 802.11g-2003. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga56f9af1b26046d60d822f9c1ef0d4abb.html language=enus -->
## TOPIC 00094: niWLANG_SetAutoHeadroomEnabled

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga56f9af1b26046d60d822f9c1ef0d4abb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga56f9af1b26046d60d822f9c1ef0d4abb.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the WLAN Generation calculates the headroom or uses the value that you specify. For multiframe generation, the WLAN Generation uses the headroom calculated on the first frame to scale the waveform for every frame. NI recommends that you do not set the enabled parameter to NIWLANG_V

### niWLANG_SetAutoHeadroomEnabled

Specifies whether the WLAN Generation calculates the headroom or uses the value that you specify. For multiframe generation, the WLAN Generation uses the headroom calculated on the first frame to scale the waveform for every frame. NI recommends that you do not set the enabled parameter to NIWLANG_VAL_TRUE for multiframe generation because variation of the peak-to-average power ratio (PAPR) across frames may lead to excessive clipping. To avoid excessive clipping, set the enabled parameter to NIWLANG_VAL_FALSE and use the default values for the [NIWLANG_ATTR_HEADROOM](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1ga76c254979e2472f290a4621f03029dfd.html) attribute.

#### Syntax

int32 __stdcall niWLANG_SetAutoHeadroomEnabled(niWLANGenerationSession session, ViChar channelString, int32 enabled)

#### Remarks

This function is available only if you set the compatibilityVersion parameter of the [niWLANG_OpenSession](group____root__ni_w_l_a_n_generation__functions_1gadad00f020668c96d94cb17f7212ee0ad.html) function to NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000 .

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| enabled | [in] | int32 | Specifies whether the WLAN Generation calculates the headroom or uses the value that you specify.The default value is NIWLANG_VAL_TRUE.ValueDescriptionNIWLANG_VAL_FALSE (0)Specifies that the WLAN Generation uses the headroom that you specify in the NIWLANG_ATTR_HEADROOM attribute.NIWLANG_VAL_TRUE (1)Specifies that the WLAN Generation calculates the headroom automatically. |
| Value | Description |  |  |
| NIWLANG_VAL_FALSE (0) | Specifies that the WLAN Generation uses the headroom that you specify in the NIWLANG_ATTR_HEADROOM attribute. |  |  |
| NIWLANG_VAL_TRUE (1) | Specifies that the WLAN Generation calculates the headroom automatically. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga5afe2dec584095f4d930a137cdb2cc6f.html language=enus -->
## TOPIC 00095: niWLANG_SetOverSamplingRatio

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga5afe2dec584095f4d930a137cdb2cc6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga5afe2dec584095f4d930a137cdb2cc6f.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of times the WLAN Generation increases the Nyquist sample rate to obtain the final sample rate of the signal. Syntaxint32 __stdcall niWLANG_SetOverSamplingRatio(niWLANGenerationSession session, ViChar channelString, float64 overSamplingRatio)ParametersNameDirectionTypeDescriptio

### niWLANG_SetOverSamplingRatio

Specifies the number of times the WLAN Generation increases the Nyquist sample rate to obtain the final sample rate of the signal.

#### Syntax

int32 __stdcall niWLANG_SetOverSamplingRatio(niWLANGenerationSession session, ViChar channelString, float64 overSamplingRatio)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| overSamplingRatio | [in] | float64 | Specifies the oversampling ratio. If you set the Standard property to 80211B/G DSSS or 80211G DSSSOFDM, the default value is 4 and the minimum value is 2. If you set the Standard property to other Standards, the default and minimum value are both 1.25. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga6ad3c53375581e2043f135a7cf971111.html language=enus -->
## TOPIC 00096: niWLANG_SetIdleInterval

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga6ad3c53375581e2043f135a7cf971111.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga6ad3c53375581e2043f135a7cf971111.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interframe spacing for signal generation. If you set the NIWLANG_ATTR_RF_BLANKING_ENABLED attribute to NIWLANG_VAL_FALSE, the WLAN Generation places half of the interframe spacing on either side of the burst in the generated waveform. If you set the NIWLANG_ATTR_RF_BLANKING_ENABLED att

### niWLANG_SetIdleInterval

Specifies the interframe spacing for signal generation. If you set the [NIWLANG_ATTR_RF_BLANKING_ENABLED](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1gaf3cc9d48e31a8879d64cdff39f33eca3.html) attribute to NIWLANG_VAL_FALSE, the WLAN Generation places half of the interframe spacing on either side of the burst in the generated waveform. If you set the [NIWLANG_ATTR_RF_BLANKING_ENABLED](group____root__ni_w_l_a_n_generation__attributes__hardware__settings_1gaf3cc9d48e31a8879d64cdff39f33eca3.html) attribute to NIWLANG_VAL_TRUE, the WLAN Generation places the interframe spacing at the end of the waveform. The waveform contains zeros for the duration of the interframe spacing.

#### Syntax

int32 __stdcall niWLANG_SetIdleInterval(niWLANGenerationSession session, ViChar channelString, float64 idleInterval)

#### Remarks

For higher values of idle interval, LabWindows/CVI may run out of memory. For a large idle interval, you can create a small idle waveform and generate the waveform multiple times using scripting.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| idleInterval | [in] | float64 | Specifies the interframe spacing for signal generation.The default value is 100 microsecond. Valid values are 0 to 1, inclusive.This value is expressed in seconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga83e57de45e848b820a977a298be35f0f.html language=enus -->
## TOPIC 00097: niWLANG_SetOFDMDataRate

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga83e57de45e848b820a977a298be35f0f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga83e57de45e848b820a977a298be35f0f.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data rate for the OFDM payload, as defined in section 17.3.2.2 of IEEE Standard 802.11a-1999. This value is expressed is Mbps. Syntaxint32 __stdcall niWLANG_SetOFDMDataRate(niWLANGenerationSession session, ViChar channelString, int32 ofdmDataRate)RemarksConfigure this function only whe

### niWLANG_SetOFDMDataRate

Specifies the data rate for the OFDM payload, as defined in section 17.3.2.2 of IEEE Standard 802.11a-1999. This value is expressed is Mbps.

#### Syntax

int32 __stdcall niWLANG_SetOFDMDataRate(niWLANGenerationSession session, ViChar channelString, int32 ofdmDataRate)

#### Remarks

Configure this function only when you set the [NIWLANG_ATTR_STANDARD](group____root__ni_w_l_a_n_generation__attributes_1gab9f572055b43b7e2c70d63ea028b4013.html) attribute to NIWLANG_VAL_STANDARD_80211AG_OFDM, NIWLANG_VAL_STANDARD_80211J_OFDM, NIWLANG_VAL_STANDARD_80211P_OFDM or NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| ofdmDataRate | [in] | int32 | Specifies the data rate for the OFDM payload. This value is expressed in Mbps. The default value is NIWLANG_VAL_OFDM_DATA_RATE_6.ValueDescriptionNIWLANG_VAL_OFDM_DATA_RATE_6 (0)Specifies a data rate of 1.5 Mbps, 3 Mbps, and 6 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz.NIWLANG_VAL_OFDM_DATA_RATE_9 (1)Specifies a data rate of 2.25 Mbps, 4.5 Mbps, and 9 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz.NIWLANG_VAL_OFDM_DATA_RATE_12 (2)Specifies a data rate of 3 Mbps, 6 Mbps, and 12 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz.NIWLANG_VAL_OFDM_DATA_RATE_18 (3)Specifies a data rate of 4.5 Mbps, 9 Mbps, and 18 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz.NIWLANG_VAL_OFDM_DATA_RATE_24 (4)Specifies a data rate of 6 Mbps, 12 Mbps, and 24 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz.NIWLANG_VAL_OFDM_DATA_RATE_36 (5)Specifies a data rate of 9 Mbps, 18 Mbps, and 36 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz.NIWLANG_VAL_OFDM_DATA_RATE_48 (6)Specifies a data rate of 12 Mbps, 24 Mbps, and 48 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz.NIWLANG_VAL_OFDM_DATA_RATE_54 (7)Specifies a data rate of 13.5 Mbps, 27 Mbps, and 54 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| Value | Description |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_6 (0) | Specifies a data rate of 1.5 Mbps, 3 Mbps, and 6 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_9 (1) | Specifies a data rate of 2.25 Mbps, 4.5 Mbps, and 9 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_12 (2) | Specifies a data rate of 3 Mbps, 6 Mbps, and 12 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_18 (3) | Specifies a data rate of 4.5 Mbps, 9 Mbps, and 18 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_24 (4) | Specifies a data rate of 6 Mbps, 12 Mbps, and 24 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_36 (5) | Specifies a data rate of 9 Mbps, 18 Mbps, and 36 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_48 (6) | Specifies a data rate of 12 Mbps, 24 Mbps, and 48 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |
| NIWLANG_VAL_OFDM_DATA_RATE_54 (7) | Specifies a data rate of 13.5 Mbps, 27 Mbps, and 54 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga8d3782593fccd6a4977e417ef2b4cf60.html language=enus -->
## TOPIC 00098: niWLANG_SetSTBCIndex

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga8d3782593fccd6a4977e417ef2b4cf60.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga8d3782593fccd6a4977e417ef2b4cf60.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the difference between the number of space-time streams and the number of spatial streams, as defined in section 20.3.9.4.3 of IEEE Standard 802.11n-2009. The WLAN Generation derives the number of spatial streams from the specified value of the NIWLANG_ATTR_MCS_INDEX attribute. Different s

### niWLANG_SetSTBCIndex

Specifies the difference between the number of space-time streams and the number of spatial streams, as defined in section 20.3.9.4.3 of IEEE Standard 802.11n-2009. The WLAN Generation derives the number of spatial streams from the specified value of the [NIWLANG_ATTR_MCS_INDEX](group____root__ni_w_l_a_n_generation__attributes__data__rate__and__frame__format_1ga5ff81d7f7fae518b786a3bc909ef372c.html) attribute. Different space-time coding schemes are defined in section 20.3.11.8.1 of IEEE Standard 802.11n-2009.

#### Syntax

int32 __stdcall niWLANG_SetSTBCIndex(niWLANGenerationSession session, ViChar channelString, int32 stbcIndex)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| stbcIndex | [in] | int32 | Specifies the value of the space-time block coding (STBC) index. The default value is 0. Valid values are 0 to 2, inclusive. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga97fe056d86caf87d14ecb58f36b9818b.html language=enus -->
## TOPIC 00099: niWLANG_SetStandard

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga97fe056d86caf87d14ecb58f36b9818b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1ga97fe056d86caf87d14ecb58f36b9818b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IEEE 802.11 standard, which indicates the type of physical layer, for signal generation. Syntaxint32 __stdcall niWLANG_SetStandard(niWLANGenerationSession session, ViChar channelString, int32 standard)RemarksIf you do not select a standard, the WLAN Generation returns an error.Paramete

### niWLANG_SetStandard

Specifies the IEEE 802.11 standard, which indicates the type of physical layer, for signal generation.

#### Syntax

int32 __stdcall niWLANG_SetStandard(niWLANGenerationSession session, ViChar channelString, int32 standard)

#### Remarks

If you do not select a standard, the WLAN Generation returns an error.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| standard | [in] | int32 | Specifies the standard for signal generation.ValueDescriptionNIWLANG_VAL_STANDARD_80211AG_OFDM (0)Corresponds to the OFDM mode defined in IEEE Standard 802.11a-1999, IEEE Standard 802.11j-2004, IEEE Standard 802.11p-2010, and the extended rate physical layer-OFDM (ERP-OFDM) mode, as defined in IEEE Standard 802.11g-2003.NIWLANG_VAL_STANDARD_80211P_OFDM (8)Corresponds to the OFDM mode defined in IEEE Standard 802.11p-2010.NIWLANG_VAL_STANDARD_80211BG_DSSS (1)Corresponds to all the compulsory and optional modes defined in IEEE Standard 802.11b-1999 and the ERP-packet binary convolutional coding (ERP-PBCC) mode defined in IEEE Standard 802.11g-2003.NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM (2)Corresponds to the optional direct sequence spread spectrum-OFDM (DSSS-OFDM) mode defined in EEE Standard 802.11g-2003.NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM (3)Corresponds to IEEE Standard 802.11n-2009. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_020000 , NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000.\| NIWLANG_VAL_STANDARD_80211AC_MIMO_OFDM (4) \| Corresponds to IEEE Standard 802.11ac-2013. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000 . \| \| NIWLANG_VAL_STANDARD_80211AH_MIMO_OFDM (5) \| Corresponds to IEEE P802.11ah/D1.3. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000. \| \| NIWLANG_VAL_STANDARD_80211AF_MIMO_OFDM (6) \| Corresponds to IEEE Standard 802.11af-2013. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000. \| \| NIWLANG_VAL_STANDARD_80211AX_MIMO_OFDM (9) \| Corresponds to IEEE P802.11ax/D8.0. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000. \| NIWLANG_VAL_STANDARD_80211BE_MIMO_OFDM (10) \| Corresponds to IEEE P802.11be/D6.0. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000 . \| \| NIWLANG_VAL_STANDARD_80211BN_MIMO_OFDM (11) \| Corresponds to IEEE P802.11be/D0.2. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000 . \| |
| Value | Description |  |  |
| NIWLANG_VAL_STANDARD_80211AG_OFDM (0) | Corresponds to the OFDM mode defined in IEEE Standard 802.11a-1999, IEEE Standard 802.11j-2004, IEEE Standard 802.11p-2010, and the extended rate physical layer-OFDM (ERP-OFDM) mode, as defined in IEEE Standard 802.11g-2003. |  |  |
| NIWLANG_VAL_STANDARD_80211P_OFDM (8) | Corresponds to the OFDM mode defined in IEEE Standard 802.11p-2010. |  |  |
| NIWLANG_VAL_STANDARD_80211BG_DSSS (1) | Corresponds to all the compulsory and optional modes defined in IEEE Standard 802.11b-1999 and the ERP-packet binary convolutional coding (ERP-PBCC) mode defined in IEEE Standard 802.11g-2003. |  |  |
| NIWLANG_VAL_STANDARD_80211G_DSSS_OFDM (2) | Corresponds to the optional direct sequence spread spectrum-OFDM (DSSS-OFDM) mode defined in EEE Standard 802.11g-2003. |  |  |
| NIWLANG_VAL_STANDARD_80211N_MIMO_OFDM (3) | Corresponds to IEEE Standard 802.11n-2009. To use this option, you must set the compatibilityVersion parameter of the niWLANG_OpenSession function to NIWLANG_VAL_COMPATIBILITY_VERSION_020000 , NIWLANG_VAL_COMPATIBILITY_VERSION_030000 , NIWLANG_VAL_COMPATIBILITY_VERSION_040000 , NIWLANG_VAL_COMPATIBILITY_VERSION_050000, or NIWLANG_VAL_COMPATIBILITY_VERSION_060000. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__configure__generation_1gac124cbe71cfbf87e349f92e7251acb13.html language=enus -->
## TOPIC 00100: niWLANG_Set80211NPLCPFrameFormat

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__configure__generation_1gac124cbe71cfbf87e349f92e7251acb13.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__configure__generation_1gac124cbe71cfbf87e349f92e7251acb13.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the format of the physical layer convergence protocol (PLCP) frame structure. Syntaxint32 __stdcall niWLANG_Set80211NPLCPFrameFormat(niWLANGenerationSession session, ViChar channelString, int32 frameFormat)RemarksThe frame structure determines the arrangement of preambles, header (SIGNAL f

### niWLANG_Set80211NPLCPFrameFormat

Specifies the format of the physical layer convergence protocol (PLCP) frame structure.

#### Syntax

int32 __stdcall niWLANG_Set80211NPLCPFrameFormat(niWLANGenerationSession session, ViChar channelString, int32 frameFormat)

#### Remarks

The frame structure determines the arrangement of preambles, header (SIGNAL field), and payload in a frame as defined in section 20.3.2 of IEEE Standard 802.11n-2009.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niWLANGenerationSession | Specifies the niWLAN generation session. |
| channelString | [out] | ViChar | Set this parameter to "" (empty string) or NULL. |
| frameFormat | [in] | int32 | Specifies the PLCP frame structure to use. The default value is NIWLANG_VAL_80211N_PLCP_FRAME_FORMAT_MIXED.ValueDescriptionNIWLANG_VAL_80211N_PLCP_FRAME_FORMAT_MIXED (0)Specifies that the PLCP frame structure consists of non-HT preamble and header (Signal field) followed by high throughput (HT) header, preambles, and payload as specified inIEEE Standard 802.11n-2009.NIWLANG_VAL_80211N_PLCP_FRAME_FORMAT_GREENFIELD (1)Specifies that the PLCP frame structure does not support non-HT, and starts with HT preamble, followed by HT Signal field, and payload. |
| Value | Description |  |  |
| NIWLANG_VAL_80211N_PLCP_FRAME_FORMAT_MIXED (0) | Specifies that the PLCP frame structure consists of non-HT preamble and header (Signal field) followed by high throughput (HT) header, preambles, and payload as specified in |  |  |
|  | IEEE Standard 802.11n-2009. |  |  |
| NIWLANG_VAL_80211N_PLCP_FRAME_FORMAT_GREENFIELD (1) | Specifies that the PLCP frame structure does not support non-HT, and starts with HT preamble, followed by HT Signal field, and payload. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group____root__ni_w_l_a_n_generation__functions__utility_1ga6bc2e55e9998c70b7fae014e478e695b.html language=enus -->
## TOPIC 00101: niWLANG_ChannelNumberToCarrierFrequency80211Abgjpn

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group____root__ni_w_l_a_n_generation__functions__utility_1ga6bc2e55e9998c70b7fae014e478e695b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group____root__ni_w_l_a_n_generation__functions__utility_1ga6bc2e55e9998c70b7fae014e478e695b.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the carrier frequency of 802.11a/b/g/j/p/n channels according to sections 16.4.6, 17.4.6, 18.3.8.4, and 20.3.15 of IEEE Standard 802.11-2012. Syntaxint32 __stdcall niWLANG_ChannelNumberToCarrierFrequency80211Abgjpn(float64 channelStartingFrequency, float64 channelBandwidth, int32 channelN

### niWLANG_ChannelNumberToCarrierFrequency80211Abgjpn

Calculates the carrier frequency of 802.11a/b/g/j/p/n channels according to sections 16.4.6, 17.4.6, 18.3.8.4, and 20.3.15 of IEEE Standard 802.11-2012.

#### Syntax

int32 __stdcall niWLANG_ChannelNumberToCarrierFrequency80211Abgjpn(float64 channelStartingFrequency, float64 channelBandwidth, int32 channelNumber, int32 secondaryFactor, float64 *carrierFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| channelStartingFrequency | [in] | float64 | Specifies the starting frequency of the frequency band. This value is expressed in Hz. |
| channelBandwidth | [in] | float64 | Specifies the channel bandwidth You can choose a 5 MHz, 10 MHz, 20 MHz, or 40 MHz channel. This value is expressed in Hz. |
| channelNumber | [in] | int32 | Specifies the offset of the center frequency, in increments of 5 MHz, above the starting frequency of the channel. |
| secondaryFactor | [in] | int32 | Specifies whether the secondary channel is above or below the primary channel when you set the channelBandwidth parameter to 40 MHz. The WLAN Generation creates a 40 MHz channel by combining the primary channel and the secondary channel, each with a 20 MHz bandwidth.The value of -1 indicates that the secondary channel is below the primary channel whereas the value of +1 indicates that the secondary channel is above the primary channel. Valid values are -1 and +1. |
| carrierFrequency | [out] | float64 * | Returns the carrier frequency. This value is expressed in Hz. The function calculates the carrier frequency using the following equation: Carrier frequency (Hz) = channel starting frequency (Hz) + (channel number * 5 MHz)When you set the channelBandwidth parameter to 40 MHz, the channelNumber parameter is the primary channel number. The function calculates the carrier frequency using the following equation:carrier frequency (Hz) = channel starting frequency (Hz) + (channel number * 5 MHz)+ (Secondary factor * 20 MHz) |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to the function to determine if an error occurred. To obtain a text description of the status code, call the [niWLANG_GetErrorString](group____root__ni_w_l_a_n_generation__functions__generation__information_1ga1a41016e233cda383b13155fe884e0a1.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-c-api-ref path=group__root__ni_w_l_a_n_generation.html language=enus -->
## TOPIC 00102: niWLANGeneration.h

- bundle_id: `rfmxwlangen-c-api-ref`
- source_path: `group__root__ni_w_l_a_n_generation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-c-api-ref/raw/resource/enus/group__root__ni_w_l_a_n_generation.html
- document_id: `rfmxwlangen-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niWLANGeneration.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
