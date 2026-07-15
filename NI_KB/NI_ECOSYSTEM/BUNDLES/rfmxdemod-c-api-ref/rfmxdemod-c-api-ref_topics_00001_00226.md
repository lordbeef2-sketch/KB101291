# NI DOCUMENT BUNDLE: rfmxdemod-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxdemod-c-api-ref start=1 end=226 -->
<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes_1ga1b72dea3532a50f922736ac05d999be2.html language=enus -->
## TOPIC 00001: RFMXDEMOD_ATTR_RESULT_FETCH_TIMEOUT

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes_1ga1b72dea3532a50f922736ac05d999be2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes_1ga1b72dea3532a50f922736ac05d999be2.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxDemod Attribute. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxDemod Attribute waits until the measurement is complete. SyntaxRFMXDEMOD_ATTR_RESULT_FETCH_TIMEOUTNumer

### RFMXDEMOD_ATTR_RESULT_FETCH_TIMEOUT

Specifies the time to wait before results are available in the RFmxDemod Attribute. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxDemod Attribute waits until the measurement is complete.

#### Syntax

RFMXDEMOD_ATTR_RESULT_FETCH_TIMEOUT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2109440 | float64 | Read/Write | N/A |

#### Remarks

This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes_1gaa0359ef04bdd300be1125883c3cd6bd4.html language=enus -->
## TOPIC 00002: RFMXDEMOD_ATTR_REFERENCE_LEVEL_HEADROOM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes_1gaa0359ef04bdd300be1125883c3cd6bd4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes_1gaa0359ef04bdd300be1125883c3cd6bd4.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin RFmx adds to the RFMXDEMOD_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. SyntaxRFMXDEMOD_ATTR_REFERENCE_LEVEL_HEADROOMNumeric ValueData TypeAccessApplies To2109436float64Read/WriteN/AR

### RFMXDEMOD_ATTR_REFERENCE_LEVEL_HEADROOM

Specifies the margin RFmx adds to the [RFMXDEMOD_ATTR_REFERENCE_LEVEL](group____root__ni_r_fmx_demod__attributes_1gaf9205d59bdde596a8ae3c5821eca24b2.html) attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

#### Syntax

RFMXDEMOD_ATTR_REFERENCE_LEVEL_HEADROOM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2109436 | float64 | Read/Write | N/A |

#### Remarks

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

**Supported devices:**PXIe-5668, PXIe-5830/5831/5832/5840/5841/5842/5860.

**Default values**

| Name (value) | Description |
| --- | --- |
| PXIe-5668 | 6 dB |
| PXIe-5830/5831/5832/5841/5842/5860 | 1 dB |
| PXIe-5840 | 0 dB |

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod.html language=enus -->
## TOPIC 00003: Analog Demod

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAudio FilterAveragingCarrier CorrectionRBW FilterResultsGroup membersNameDescriptionRFMXDEMOD_ATTR_ADEMOD_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement. RFMXDEMOD_ATTR_ADEMOD_AM_CARRIER_SUPPRESSEDSpecifi

### Analog Demod

#### Groups

- Audio Filter
- Averaging
- Carrier Correction
- RBW Filter
- Results

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_ADEMOD_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the analog demodulation measurement. |
| RFMXDEMOD_ATTR_ADEMOD_AM_CARRIER_SUPPRESSED | Specifies whether the carrier of the AM (amplitude modulated) signal is absent. |
| RFMXDEMOD_ATTR_ADEMOD_AUDIO_MEASUREMENT_ENABLED | Specifies whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise. |
| RFMXDEMOD_ATTR_ADEMOD_FM_DEEMPHASIS | Specifies the time constant of de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. This value is expressed in seconds. |
| RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_ENABLED | Specifies whether to enable analog demodulation measurements. |
| RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_INTERVAL | Specifies the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. |
| RFMXDEMOD_ATTR_ADEMOD_MODULATION_TYPE | Specifies the analog modulation type of the signal that needs to be analyzed. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod_1ga266be22857b4ac63e33587256eb9f26d.html language=enus -->
## TOPIC 00004: RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_ENABLED

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod_1ga266be22857b4ac63e33587256eb9f26d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod_1ga266be22857b4ac63e33587256eb9f26d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable analog demodulation measurements. SyntaxRFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To2097209int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to t

### RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_ENABLED

Specifies whether to enable analog demodulation measurements.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097209 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

Analog Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod_1ga608d461918e3fb6e00e231d300c53dee.html language=enus -->
## TOPIC 00005: RFMXDEMOD_ATTR_ADEMOD_FM_DEEMPHASIS

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod_1ga608d461918e3fb6e00e231d300c53dee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod_1ga608d461918e3fb6e00e231d300c53dee.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time constant of de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. This value is expressed in seconds. SyntaxRFMXDEMOD_ATTR_ADEMOD_FM_DEEMPHASISNumeric ValueData TypeAccessApplies To2097164float64Read/WriteN/ARemarks The lowpass characteristic tra

### RFMXDEMOD_ATTR_ADEMOD_FM_DEEMPHASIS

Specifies the time constant of de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. This value is expressed in seconds.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_FM_DEEMPHASIS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097164 | float64 | Read/Write | N/A |

#### Remarks

The lowpass characteristic transfer function of the de-emphasis filter is as shown in the following equation:

*H*(*f*) = 1/(1+*j*(2*pi**f**τ)

where τ is the de-emphasis filter time constant. This value is expressed in seconds.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0 seconds. No filter is applied on the demodulated signal when de-emphasis is set to 0.

Parent topic:

Analog Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod_1ga7f4db53c936bd32569e6a9bc93d24ff4.html language=enus -->
## TOPIC 00006: RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_INTERVAL

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod_1ga7f4db53c936bd32569e6a9bc93d24ff4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod_1ga7f4db53c936bd32569e6a9bc93d24ff4.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds. SyntaxRFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_INTERVALNumeric ValueData TypeAccessApplies To2097165float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_INTERVAL

Specifies the signal acquisition time for the analog demodulation measurement. This value is expressed in seconds.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_MEASUREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097165 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 ms.

Parent topic:

Analog Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod_1ga983bb47d5ee3ce62ced9fc1684adb31d.html language=enus -->
## TOPIC 00007: RFMXDEMOD_ATTR_ADEMOD_MODULATION_TYPE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod_1ga983bb47d5ee3ce62ced9fc1684adb31d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod_1ga983bb47d5ee3ce62ced9fc1684adb31d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the analog modulation type of the signal that needs to be analyzed. SyntaxRFMXDEMOD_ATTR_ADEMOD_MODULATION_TYPENumeric ValueData TypeAccessApplies To2097166int32Read/WriteN/ARemarks The default value is AM.NameValueDescriptionRFMXDEMOD_VAL_ADEMOD_MODULATION_TYPE_AM0 (0x0)The signal to be a

### RFMXDEMOD_ATTR_ADEMOD_MODULATION_TYPE

Specifies the analog modulation type of the signal that needs to be analyzed.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_MODULATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097166 | int32 | Read/Write | N/A |

#### Remarks

The default value is **AM**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_ADEMOD_MODULATION_TYPE_AM | 0 (0x0) | The signal to be analyzed is amplitude modulated. |
| RFMXDEMOD_VAL_ADEMOD_MODULATION_TYPE_FM | 1 (0x1) | The signal to be analyzed is frequency modulated. |
| RFMXDEMOD_VAL_ADEMOD_MODULATION_TYPE_PM | 2 (0x2) | The signal to be analyzed is phase modulated. |

Parent topic:

Analog Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod_1gaa9072d1d52537b9bb6790ebd5770125d.html language=enus -->
## TOPIC 00008: RFMXDEMOD_ATTR_ADEMOD_AUDIO_MEASUREMENT_ENABLED

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod_1gaa9072d1d52537b9bb6790ebd5770125d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod_1gaa9072d1d52537b9bb6790ebd5770125d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise. SyntaxRFMXDEMOD_ATTR_ADEMOD_AUDIO_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To2097216int32Read/WriteN/ARemarks The default value is True.NameValueDescriptionRFMXDEMOD_VAL_ADEMOD_AUDIO_MEASU

### RFMXDEMOD_ATTR_ADEMOD_AUDIO_MEASUREMENT_ENABLED

Specifies whether to enable the audio signal measurements, such as SINAD, SNR, THD and THD+Noise.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_AUDIO_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097216 | int32 | Read/Write | N/A |

#### Remarks

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_ADEMOD_AUDIO_MEASUREMENT_ENABLED_FALSE | 0 (0x0) | Disables the audio measurements. |
| RFMXDEMOD_VAL_ADEMOD_AUDIO_MEASUREMENT_ENABLED_TRUE | 1 (0x1) | Enables the audio measurements. |

Parent topic:

Analog Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__audio__filter.html language=enus -->
## TOPIC 00009: Audio Filter

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__audio__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__audio__filter.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_LOWER_CUTOFF_FREQUENCYSpecifies the lower cutoff frequency of the custom audio filter. This attribute is applicable only when you set the RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE attribute to Custom. This value is expressed in H

### Audio Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_LOWER_CUTOFF_FREQUENCY | Specifies the lower cutoff frequency of the custom audio filter. This attribute is applicable only when you set the RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE attribute to Custom. This value is expressed in Hz. |
| RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE | Specifies the audio filter to be applied on the analog demodulated signal. |
| RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_UPPER_CUTOFF_FREQUENCY | Specifies the upper cutoff frequency of the custom audio filter. This attribute is applicable only when you set the RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE attribute to Custom. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Analog Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__audio__filter_1ga51aa1302708c346fa38cc09a9fa40f10.html language=enus -->
## TOPIC 00010: RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_UPPER_CUTOFF_FREQUENCY

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__audio__filter_1ga51aa1302708c346fa38cc09a9fa40f10.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__audio__filter_1ga51aa1302708c346fa38cc09a9fa40f10.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper cutoff frequency of the custom audio filter. This attribute is applicable only when you set the RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE attribute to Custom. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_UPPER_CUTOFF_FREQUENCYNumeric ValueData TypeAccessA

### RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_UPPER_CUTOFF_FREQUENCY

Specifies the upper cutoff frequency of the custom audio filter. This attribute is applicable only when you set the [RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_TYPE](group____root__ni_r_fmx_demod__attributes__analog__demod__audio__filter_1gab7b41d03ef902cad808d153b4b922689.html) attribute to **Custom**. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_AUDIO_FILTER_UPPER_CUTOFF_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097157 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10,000.

Parent topic:

Audio Filter

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__carrier__correction_1gaec36c11eb752d46a712f0ff87d194491.html language=enus -->
## TOPIC 00011: RFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_FREQUENCY_ENABLED

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__carrier__correction_1gaec36c11eb752d46a712f0ff87d194491.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__carrier__correction_1gaec36c11eb752d46a712f0ff87d194491.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals. SyntaxRFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_FREQUENCY_ENABLEDNumeric ValueData TypeAccessApplies To2097162int32Read/WriteN/ARemarks You do not need to use a

### RFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_FREQUENCY_ENABLED

Specifies whether to correct the frequency error in the carrier when demodulating frequency-modulated (FM) or phase-modulated (PM) signals.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_CARRIER_CORRECTION_FREQUENCY_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097162 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_ADEMOD_CARRIER_FREQUENCY_CORRECTION_ENABLED_FALSE | 0 (0x0) | Does not correct the carrier frequency error. |
| RFMXDEMOD_VAL_ADEMOD_CARRIER_FREQUENCY_CORRECTION_ENABLED_TRUE | 1 (0x1) | Corrects the carrier frequency error. |

Parent topic:

Carrier Correction

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter.html language=enus -->
## TOPIC 00012: RBW Filter

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHASpecifies the roll-off factor of the root-raised cosine (RRC) filter. RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the resolution bandwidth (RBW) filter to be applied to the acquired signal. This valu

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHA | Specifies the roll-off factor of the root-raised cosine (RRC) filter. |
| RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the resolution bandwidth (RBW) filter to be applied to the acquired signal. This value is expressed in Hz. |
| RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_TYPE | Specifies the shape of the digital RBW filter. |

#### Attachments

None

Parent topic:

Analog Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter_1ga6c2e4b6d5ea0aca90e21fb4fcdbf1af9.html language=enus -->
## TOPIC 00013: RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHA

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter_1ga6c2e4b6d5ea0aca90e21fb4fcdbf1af9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter_1ga6c2e4b6d5ea0aca90e21fb4fcdbf1af9.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the roll-off factor of the root-raised cosine (RRC) filter. SyntaxRFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHANumeric ValueData TypeAccessApplies To2097170float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Ref

### RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHA

Specifies the roll-off factor of the root-raised cosine (RRC) filter.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097170 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.1.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter_1gab959fddc0101c2a601229e234a8558e0.html language=enus -->
## TOPIC 00014: RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_TYPE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter_1gab959fddc0101c2a601229e234a8558e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__rbw__filter_1gab959fddc0101c2a601229e234a8558e0.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. SyntaxRFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To2097168int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String

### RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_TYPE

Specifies the shape of the digital RBW filter.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097168 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Flat**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_NONE | 0 (0x0) | RBW filter is not applied on the acquired signal. |
| RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | RBW filter has a Gaussian response. |
| RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_FLAT | 2 (0x2) | RBW filter has a Flat response. |
| RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_SYNCH_TUNED_4 | 3 (0x3) | RBW filter has a response of a 4-pole synchronously-tuned filter. |
| RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_SYNCH_TUNED_5 | 4 (0x4) | RBW filter has a response of a 5-pole synchronously-tuned filter. |
| RFMXDEMOD_VAL_ADEMOD_RBW_FILTER_TYPE_RRC | 5 (0x5) | RRC filter with roll-off specified by the RFMXDEMOD_ATTR_ADEMOD_RBW_FILTER_ALPHA attribute is used as the RBW filter. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga5d9cad06de8ee86dab60875d2265cf27.html language=enus -->
## TOPIC 00015: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD_WITH_NOISE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga5d9cad06de8ee86dab60875d2265cf27.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga5d9cad06de8ee86dab60875d2265cf27.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the averaged total harmonic distortion with noise of the demodulated signal, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD_WITH_NOISENumeric ValueData TypeAccessApplies To2097176float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this a

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD_WITH_NOISE

Returns the averaged total harmonic distortion with noise of the demodulated signal, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD_WITH_NOISE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097176 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga72097c1bf439c73ceefd353c2812e648.html language=enus -->
## TOPIC 00016: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga72097c1bf439c73ceefd353c2812e648.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga72097c1bf439c73ceefd353c2812e648.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the averaged total harmonic distortion of the demodulated signal, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THDNumeric ValueData TypeAccessApplies To2097177float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the defau

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD

Returns the averaged total harmonic distortion of the demodulated signal, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AVERAGE_THD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097177 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga734e91b1f10dda58a3f932cee11ff9e5.html language=enus -->
## TOPIC 00017: RFMXDEMOD_ATTR_ADEMOD_RESULTS_MEAN_MODULATION_FREQUENCY

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga734e91b1f10dda58a3f932cee11ff9e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results_1ga734e91b1f10dda58a3f932cee11ff9e5.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the demodulated signal frequency. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_MEAN_MODULATION_FREQUENCYNumeric ValueData TypeAccessApplies To2097174float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for t

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_MEAN_MODULATION_FREQUENCY

Returns the mean of the demodulated signal frequency. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_MEAN_MODULATION_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097174 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth.html language=enus -->
## TOPIC 00018: AM Modulation Depth

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_HALF_PEAK_TO_PEAKReturns the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage. RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_N

### AM Modulation Depth

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_HALF_PEAK_TO_PEAK | Returns the maximum (peak-to-peak)/2 amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_NEGATIVE_PEAK | Returns the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_POSITIVE_PEAK | Returns the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_RMS | Returns the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_STANDARD_DEVIATION | Returns the maximum modulation depth measured across multiple acquisitions, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_HALF_PEAK_TO_PEAK | Returns the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_NEGATIVE_PEAK | Returns the mean negative peak amplitude of the modulating signal, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_POSITIVE_PEAK | Returns the mean positive peak amplitude of the modulating signal, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_RMS | Returns the mean RMS amplitude of the modulating signal, as a percentage. |
| RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_STANDARD_DEVIATION | Returns the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga195d5a6fd7761d4cda89321a609df13f.html language=enus -->
## TOPIC 00019: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_HALF_PEAK_TO_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga195d5a6fd7761d4cda89321a609df13f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga195d5a6fd7761d4cda89321a609df13f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_HALF_PEAK_TO_PEAKNumeric ValueData TypeAccessApplies To2097180float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read t

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_HALF_PEAK_TO_PEAK

Returns the mean (peak-to-peak)/2 amplitude of the modulating signal, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_HALF_PEAK_TO_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097180 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga1b5dceba3d46bbc2cb11749a6c823ee2.html language=enus -->
## TOPIC 00020: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_STANDARD_DEVIATION

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga1b5dceba3d46bbc2cb11749a6c823ee2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga1b5dceba3d46bbc2cb11749a6c823ee2.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_STANDARD_DEVIATIONNumeric ValueData TypeAccessAppli

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_STANDARD_DEVIATION

Returns the mean amplitude variation around the unmodulated carrier amplitude, as a percentage. If the carrier is suppressed, the amplitude variation of the modulating signal is returned.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097179 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga39288cba88c31947e175d61c5ba9b585.html language=enus -->
## TOPIC 00021: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_STANDARD_DEVIATION

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga39288cba88c31947e175d61c5ba9b585.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga39288cba88c31947e175d61c5ba9b585.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum modulation depth measured across multiple acquisitions, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To2097184float64Read-OnlyN/ARemarks You do not need to use a selector string to configure

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_STANDARD_DEVIATION

Returns the maximum modulation depth measured across multiple acquisitions, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097184 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga41dbbe0752d04eea1aad04e16105adbe.html language=enus -->
## TOPIC 00022: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_NEGATIVE_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga41dbbe0752d04eea1aad04e16105adbe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga41dbbe0752d04eea1aad04e16105adbe.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean negative peak amplitude of the modulating signal, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_NEGATIVE_PEAKNumeric ValueData TypeAccessApplies To2097182float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this att

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_NEGATIVE_PEAK

Returns the mean negative peak amplitude of the modulating signal, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_NEGATIVE_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097182 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga4a5f012c873d2f31a0223fd1630ba46c.html language=enus -->
## TOPIC 00023: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_POSITIVE_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga4a5f012c873d2f31a0223fd1630ba46c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga4a5f012c873d2f31a0223fd1630ba46c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean positive peak amplitude of the modulating signal, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_POSITIVE_PEAKNumeric ValueData TypeAccessApplies To2097181float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this att

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_POSITIVE_PEAK

Returns the mean positive peak amplitude of the modulating signal, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_POSITIVE_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097181 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga5a5fc903493caf986a7c76cee1e8ba01.html language=enus -->
## TOPIC 00024: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_NEGATIVE_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga5a5fc903493caf986a7c76cee1e8ba01.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga5a5fc903493caf986a7c76cee1e8ba01.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_NEGATIVE_PEAKNumeric ValueData TypeAccessApplies To2097187float64Read-OnlyN/ARemarks You do not need to use a s

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_NEGATIVE_PEAK

Returns the maximum negative peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_NEGATIVE_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097187 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga8fb9c406c54266fe5eca4ef858ea8d6b.html language=enus -->
## TOPIC 00025: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_POSITIVE_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga8fb9c406c54266fe5eca4ef858ea8d6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1ga8fb9c406c54266fe5eca4ef858ea8d6b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_POSITIVE_PEAKNumeric ValueData TypeAccessApplies To2097186float64Read-OnlyN/ARemarks You do not need to use a s

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_POSITIVE_PEAK

Returns the maximum positive peak amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_POSITIVE_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097186 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1gaa68f622a22af404848ab7133d0d10c41.html language=enus -->
## TOPIC 00026: RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_RMS

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1gaa68f622a22af404848ab7133d0d10c41.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__am__modulation__depth_1gaa68f622a22af404848ab7133d0d10c41.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_RMSNumeric ValueData TypeAccessApplies To2097188float64Read-OnlyN/ARemarks You do not need to use a selector string to co

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_RMS

Returns the maximum RMS amplitude of the modulating signal measured across multiple acquisitions, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_RMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097188 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

AM Modulation Depth

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gaa62aa24c9757525cc177167cfa1c353a.html language=enus -->
## TOPIC 00027: RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_STANDARD_DEVIATION

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gaa62aa24c9757525cc177167cfa1c353a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gaa62aa24c9757525cc177167cfa1c353a.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean frequency deviation around the nominal frequency of the FM carrier. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To2097189float64Read-OnlyN/ARemarks You do not need to use a selector string

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_STANDARD_DEVIATION

Returns the mean frequency deviation around the nominal frequency of the FM carrier. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097189 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gaaaad22cc53bb08147c14d1e85028cea5.html language=enus -->
## TOPIC 00028: RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_HALF_PEAK_TO_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gaaaad22cc53bb08147c14d1e85028cea5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gaaaad22cc53bb08147c14d1e85028cea5.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_HALF_PEAK_TO_PEAKNumeric ValueData TypeAccessApplies To2097190float64Read-OnlyN/ARemarks You do not need to use a

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_HALF_PEAK_TO_PEAK

Returns the mean (peak-to-peak)/2 frequency variation around the nominal frequency of the FM carrier. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_HALF_PEAK_TO_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097190 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gabdf3b36c2c7fb05c2986aadbc98ce004.html language=enus -->
## TOPIC 00029: RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_NEGATIVE_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gabdf3b36c2c7fb05c2986aadbc98ce004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__fm__deviation_1gabdf3b36c2c7fb05c2986aadbc98ce004.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean negative peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_NEGATIVE_PEAKNumeric ValueData TypeAccessApplies To2097192float64Read-OnlyN/ARemarks You do not need to use a selector string to

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_NEGATIVE_PEAK

Returns the mean negative peak frequency deviation of the frequency-modulated signal. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_FM_DEVIATION_MEAN_NEGATIVE_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097192 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga30ab59ec2bcc6bfb1bbcffc1922abaa1.html language=enus -->
## TOPIC 00030: RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_STANDARD_DEVIATION

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga30ab59ec2bcc6bfb1bbcffc1922abaa1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga30ab59ec2bcc6bfb1bbcffc1922abaa1.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean phase deviation around the unmodulated carrier phase. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_STANDARD_DEVIATIONNumeric ValueData TypeAccessApplies To2097199float64Read-OnlyN/ARemarks You do not need to use a selector string to confi

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_STANDARD_DEVIATION

Returns the mean phase deviation around the unmodulated carrier phase. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_STANDARD_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097199 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

PM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga4ab1541076731ff758a969e19399a62f.html language=enus -->
## TOPIC 00031: RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_RMS

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga4ab1541076731ff758a969e19399a62f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga4ab1541076731ff758a969e19399a62f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum RMS phase deviation of the phase-modulated signal measured across multiple acquisitions. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_RMSNumeric ValueData TypeAccessApplies To2097208float64Read-OnlyN/ARemarks You do not need to use

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_RMS

Returns the maximum RMS phase deviation of the phase-modulated signal measured across multiple acquisitions. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_RMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097208 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

PM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga92e1c8c0e4891f89644c1b2b30446cf9.html language=enus -->
## TOPIC 00032: RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_NEGATIVE_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga92e1c8c0e4891f89644c1b2b30446cf9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga92e1c8c0e4891f89644c1b2b30446cf9.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean negative peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_NEGATIVE_PEAKNumeric ValueData TypeAccessApplies To2097202float64Read-OnlyN/ARemarks You do not need to use a selector string

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_NEGATIVE_PEAK

Returns the mean negative peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_NEGATIVE_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097202 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

PM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga9e2179919f5edf54d090652993ed5cc4.html language=enus -->
## TOPIC 00033: RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_RMS

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga9e2179919f5edf54d090652993ed5cc4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1ga9e2179919f5edf54d090652993ed5cc4.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean RMS phase deviation of the phase-modulated signal. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_RMSNumeric ValueData TypeAccessApplies To2097203float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_RMS

Returns the mean RMS phase deviation of the phase-modulated signal. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_RMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097203 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

PM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1gac8b463d1d5f319c6d1970c30f1e7298b.html language=enus -->
## TOPIC 00034: RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_POSITIVE_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1gac8b463d1d5f319c6d1970c30f1e7298b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__analog__demod__results__pm__deviation_1gac8b463d1d5f319c6d1970c30f1e7298b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean positive peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_POSITIVE_PEAKNumeric ValueData TypeAccessApplies To2097201float64Read-OnlyN/ARemarks You do not need to use a selector string

### RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_POSITIVE_PEAK

Returns the mean positive peak phase deviation around the unmodulated carrier phase. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_ADEMOD_RESULTS_PM_DEVIATION_MEAN_POSITIVE_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2097201 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

PM Deviation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod_1ga12bcb6541c78f95aa1dac51a99a0e9ca.html language=enus -->
## TOPIC 00035: RFMXDEMOD_ATTR_DDEMOD_EVM_NORMALIZATION_REFERENCE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod_1ga12bcb6541c78f95aa1dac51a99a0e9ca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod_1ga12bcb6541c78f95aa1dac51a99a0e9ca.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference used to normalize the error vector magnitude (EVM). SyntaxRFMXDEMOD_ATTR_DDEMOD_EVM_NORMALIZATION_REFERENCENumeric ValueData TypeAccessApplies To2101305int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signa

### RFMXDEMOD_ATTR_DDEMOD_EVM_NORMALIZATION_REFERENCE

Specifies the reference used to normalize the error vector magnitude (EVM).

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_EVM_NORMALIZATION_REFERENCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101305 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Peak**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_EVM_NORMALIZATION_REFERENCE_PEAK | 0 (0x0) | The EVM is normalized to the peak magnitude of the reference symbols. |
| RFMXDEMOD_VAL_DDEMOD_EVM_NORMALIZATION_REFERENCE_RMS | 1 (0x1) | The EVM is normalized to the RMS magnitude of the reference symbols. This value is applicable only to modulation types, such as quadrature-amplitude modulation (QAM). This value is expressed in which the symbols in the map do not have a constant amplitude. |

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod_1ga2e21e47d146267f04955d1a0e37fa7b5.html language=enus -->
## TOPIC 00036: RFMXDEMOD_ATTR_DDEMOD_SPECTRUM_INVERTED

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod_1ga2e21e47d146267f04955d1a0e37fa7b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod_1ga2e21e47d146267f04955d1a0e37fa7b5.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to swap the acquired I and Q samples for demodulation. SyntaxRFMXDEMOD_ATTR_DDEMOD_SPECTRUM_INVERTEDNumeric ValueData TypeAccessApplies To2101266int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. R

### RFMXDEMOD_ATTR_DDEMOD_SPECTRUM_INVERTED

Specifies whether to swap the acquired I and Q samples for demodulation.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_SPECTRUM_INVERTED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101266 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_SPECTRUM_INVERTED_FALSE | 0 (0x0) | The acquired I and Q samples are used for demodulation as is. |
| RFMXDEMOD_VAL_DDEMOD_SPECTRUM_INVERTED_TRUE | 1 (0x1) | The acquired I and Q samples are swapped before using the signal for demodulation. |

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod_1ga39382ce2de672a7882fc18317c471b85.html language=enus -->
## TOPIC 00037: RFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod_1ga39382ce2de672a7882fc18317c471b85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod_1ga39382ce2de672a7882fc18317c471b85.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal is either a bursty signal or a continuous signal. SyntaxRFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURENumeric ValueData TypeAccessApplies To2101313int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instan

### RFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURE

Specifies whether the signal is either a bursty signal or a continuous signal.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_SIGNAL_STRUCTURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101313 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Continuous**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_BURSTED | 0 (0x0) | The signal is a bursty signal. |
| RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_CONTINUOUS | 1 (0x1) | The signal is a continuous signal. |

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod_1ga5478ef2560c78e497efdd9c42df6bb7d.html language=enus -->
## TOPIC 00038: RFMXDEMOD_ATTR_DDEMOD_SYMBOL_MAP_TYPE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod_1ga5478ef2560c78e497efdd9c42df6bb7d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod_1ga5478ef2560c78e497efdd9c42df6bb7d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement uses the default symbol map or the map that you configure using the RFmxDemod_DDemodCfgSymbolMap function. SyntaxRFMXDEMOD_ATTR_DDEMOD_SYMBOL_MAP_TYPENumeric ValueData TypeAccessApplies To2101312int32Read/WriteN/ARemarks You do not need to use a selector string to c

### RFMXDEMOD_ATTR_DDEMOD_SYMBOL_MAP_TYPE

Specifies whether the measurement uses the default symbol map or the map that you configure using the [RFmxDemod_DDemodCfgSymbolMap](group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga43fd50406e3b667d30b6734629784ee9.html) function.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_SYMBOL_MAP_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101312 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_AUTO | 0 (0x0) | Uses a default symbol map. |
| RFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_CUSTOM | 1 (0x1) | Uses the map that you specify using the RFmxDemod_DDemodCfgSymbolMap function . |

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__apsk.html language=enus -->
## TOPIC 00039: APSK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__apsk.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__apsk.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_APSK_R2_TO_R1_RATIOSpecifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. RFMXDEMOD_ATTR_DDEMOD_APSK_R3_TO_R1_RATIOSpecifies the ratio

### APSK

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_APSK_R2_TO_R1_RATIO | Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. |
| RFMXDEMOD_ATTR_DDEMOD_APSK_R3_TO_R1_RATIO | Specifies the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__apsk_1ga421a4ec75e17270f0ee5f7706a1fea3c.html language=enus -->
## TOPIC 00040: RFMXDEMOD_ATTR_DDEMOD_APSK_R3_TO_R1_RATIO

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__apsk_1ga421a4ec75e17270f0ee5f7706a1fea3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__apsk_1ga421a4ec75e17270f0ee5f7706a1fea3c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK. SyntaxRFMXDEMOD_ATTR_DDEMOD_APSK_R3_TO_R1_RATIONumeric ValueData TypeAccessApplies To2101322float64Read/WriteN/ARemarks You do not need to use a selector str

### RFMXDEMOD_ATTR_DDEMOD_APSK_R3_TO_R1_RATIO

Specifies the ratio of the magnitude of symbols on a ring(R3) to the magnitude of symbols on the inner ring(R1). It is applicable for 32-APSK.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_APSK_R3_TO_R1_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101322 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 5.27. Valid values are from 3 to 12, inclusive.

Parent topic:

APSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__apsk_1ga6c492e1cee1fca5e97373ca652122e05.html language=enus -->
## TOPIC 00041: RFMXDEMOD_ATTR_DDEMOD_APSK_R2_TO_R1_RATIO

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__apsk_1ga6c492e1cee1fca5e97373ca652122e05.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__apsk_1ga6c492e1cee1fca5e97373ca652122e05.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK. SyntaxRFMXDEMOD_ATTR_DDEMOD_APSK_R2_TO_R1_RATIONumeric ValueData TypeAccessApplies To2101321float64Read/WriteN/ARemarks You do not need to u

### RFMXDEMOD_ATTR_DDEMOD_APSK_R2_TO_R1_RATIO

Specifies the ratio of the magnitude of symbols on a ring(R2) to the magnitude of symbols on the inner ring(R1). It is applicable for both 16-APSK and 32-APSK.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_APSK_R2_TO_R1_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101321 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 2.84. Valid values are from 2 to 8, inclusive.

Parent topic:

APSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__compensation.html language=enus -->
## TOPIC 00042: Compensation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__compensation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__compensation.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_CFO_ESTIMATION_MODESpecifies the carrier frequency offset estimation capability of the demodulator. If you select Narrow, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed.

### Compensation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_CFO_ESTIMATION_MODE | Specifies the carrier frequency offset estimation capability of the demodulator. If you select Narrow, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals. |
| RFMXDEMOD_ATTR_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED | Specifies whether to remove the I/Q offset before the EVM measurement. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__compensation_1ga816dccba5cb004387d6e3b2fa8e7a633.html language=enus -->
## TOPIC 00043: RFMXDEMOD_ATTR_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__compensation_1ga816dccba5cb004387d6e3b2fa8e7a633.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__compensation_1ga816dccba5cb004387d6e3b2fa8e7a633.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the EVM measurement. SyntaxRFMXDEMOD_ATTR_DDEMOD_IQ_OFFSET_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To2101316int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal insta

### RFMXDEMOD_ATTR_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED

Specifies whether to remove the I/Q offset before the EVM measurement.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101316 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED_FALSE | 0 (0x0) | The IQ offset is not removed before the EVM measurement. |
| RFMXDEMOD_VAL_DDEMOD_IQ_OFFSET_REMOVAL_ENABLED_TRUE | 1 (0x1) | The IQ offset is removed before the EVM measurement. |

Parent topic:

Compensation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__compensation_1ga88ced8335b4b6f06a8b23ec2ffa8d6be.html language=enus -->
## TOPIC 00044: RFMXDEMOD_ATTR_DDEMOD_CFO_ESTIMATION_MODE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__compensation_1ga88ced8335b4b6f06a8b23ec2ffa8d6be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__compensation_1ga88ced8335b4b6f06a8b23ec2ffa8d6be.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier frequency offset estimation capability of the demodulator. If you select Narrow, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals. SyntaxRFMXDEMOD_ATTR_DDEMOD_CFO

### RFMXDEMOD_ATTR_DDEMOD_CFO_ESTIMATION_MODE

Specifies the carrier frequency offset estimation capability of the demodulator. If you select **Narrow**, coarse carrier frequency offset estimation is disabled and only fine carrier frequency offset estimation is performed. This is useful when analysing low SNR signals.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_CFO_ESTIMATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101317 | int32 | Read/Write | N/A |

#### Remarks

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_CFO_ESTIMATION_MODE_NARROW | 0 (0x0) | The measurement disables coarse carrier frequency offset estimation. |
| RFMXDEMOD_VAL_DDEMOD_CFO_ESTIMATION_MODE_WIDE | 1 (0x1) | The measurement enables coarse and fine carrier frequency offset estimation. |

Parent topic:

Compensation

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__equalizer.html language=enus -->
## TOPIC 00045: Equalizer

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__equalizer.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__equalizer.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_EQUALIZER_CONVERGENCE_FACTORSpecifies the incremental step used by the equalizer to adapt to the channel during the training stage. RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_FILTER_LENGTHSpecifies the length of the equalization filter to be computed.

### Equalizer

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_CONVERGENCE_FACTOR | Specifies the incremental step used by the equalizer to adapt to the channel during the training stage. |
| RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_FILTER_LENGTH | Specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. |
| RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_MODE | Specifies whether the measurement needs to perform equalization. |
| RFMXDEMOD_ATTR_DDEMOD_EQUALIZER_TRAINING_COUNT | Specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. After the training stage, the measurement is performed over the specified number of averages. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__fsk.html language=enus -->
## TOPIC 00046: FSK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__fsk.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__fsk.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_FSK_DEVIATIONSpecifies the expected FSK frequency deviation At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation. This value is expressed in Hz.

### FSK

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_FSK_DEVIATION | Specifies the expected FSK frequency deviation At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation. This value is expressed in Hz. |
| RFMXDEMOD_ATTR_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED | Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__fsk_1ga487d83aedf3eb379fdd3b33cb9e4674f.html language=enus -->
## TOPIC 00047: RFMXDEMOD_ATTR_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__fsk_1ga487d83aedf3eb379fdd3b33cb9e4674f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__fsk_1ga487d83aedf3eb379fdd3b33cb9e4674f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error. SyntaxRFMXDEMOD_ATTR_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To2101304int32Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXDEMOD_ATTR_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED

Specifies whether the FSK deviation that you specify is used to compensate for gain errors and compute FSK error.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101304 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Does not compensate for gain errors. |
| RFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Compensates for gain errors. |

Parent topic:

FSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__fsk_1ga78a7763f24219f2857d0dc5f84d731b4.html language=enus -->
## TOPIC 00048: RFMXDEMOD_ATTR_DDEMOD_FSK_DEVIATION

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__fsk_1ga78a7763f24219f2857d0dc5f84d731b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__fsk_1ga78a7763f24219f2857d0dc5f84d731b4.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected FSK frequency deviation At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-fd, fd], where fd represents the frequency deviation. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_DDEMOD_FSK_DEVIATIONNumeric ValueData TypeAccessAppl

### RFMXDEMOD_ATTR_DDEMOD_FSK_DEVIATION

Specifies the expected FSK frequency deviation At baseband frequencies, deviations for individual symbols are evenly spaced in the interval [-*fd*, *fd*], where *fd* represents the frequency deviation. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_FSK_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101256 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 15 kHz.

Parent topic:

FSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__measurement__filter.html language=enus -->
## TOPIC 00049: Measurement Filter

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__measurement__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__measurement__filter.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPESpecifies whether the measurement needs to compute the measurement filter based on the pulse-shaping filter type or uses the custom measurement filter coefficients. AttachmentsNone

### Measurement Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE | Specifies whether the measurement needs to compute the measurement filter based on the pulse-shaping filter type or uses the custom measurement filter coefficients. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__measurement__filter_1gaeb8d741ae79eced47bf005e2a99b0a74.html language=enus -->
## TOPIC 00050: RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__measurement__filter_1gaeb8d741ae79eced47bf005e2a99b0a74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__measurement__filter_1gaeb8d741ae79eced47bf005e2a99b0a74.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement needs to compute the measurement filter based on the pulse-shaping filter type or uses the custom measurement filter coefficients. SyntaxRFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPENumeric ValueData TypeAccessApplies To2101258int32Read/WriteN/ARemarks You do not ne

### RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE

Specifies whether the measurement needs to compute the measurement filter based on the pulse-shaping filter type or uses the custom measurement filter coefficients.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101258 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_AUTO | 0 (0x0) | The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE attribute. If the DDemod Pulse Shaping Filter Type attribute is set to Custom, the signal analyzer enables equalization. |
| RFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_CUSTOM | 1 (0x1) | The signal analyzer uses the coefficients specified by RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients function. |

Parent topic:

Measurement Filter

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__psk.html language=enus -->
## TOPIC 00051: PSK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__psk.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__psk.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_PSK_FORMATSpecifies the PSK format. AttachmentsNone

### PSK

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_PSK_FORMAT | Specifies the PSK format. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__psk_1ga23630588ed6762ee7383119ce1bc8e76.html language=enus -->
## TOPIC 00052: RFMXDEMOD_ATTR_DDEMOD_PSK_FORMAT

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__psk_1ga23630588ed6762ee7383119ce1bc8e76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__psk_1ga23630588ed6762ee7383119ce1bc8e76.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PSK format. SyntaxRFMXDEMOD_ATTR_DDEMOD_PSK_FORMATNumeric ValueData TypeAccessApplies To2101262int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for information abou

### RFMXDEMOD_ATTR_DDEMOD_PSK_FORMAT

Specifies the PSK format.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_PSK_FORMAT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101262 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Normal**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_NORMAL | 0 (0x0) | Sets the modulation type to PSK. |
| RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_OFFSET_QPSK | 1 (0x1) | Sets the modulation type to offset quadrature PSK (OQPSK). The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I. |
| RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_PI_BY_4_QPSK | 2 (0x2) | Sets the modulation type to pi/4 QPSK. In this modulation, each QPSK symbol is rotated by pi/4. |
| RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_PI_BY_8_8PSK | 3 (0x3) | Sets the modulation type to pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by pi/8. |
| RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_3PI_BY_8_8PSK | 4 (0x4) | Sets the modulation type to 3*pi/8-8 PSK. In this modulation, each 8 PSK symbol is rotated by 3*pi/8. |
| RFMXDEMOD_VAL_DDEMOD_PSK_FORMAT_SHAPED_OFFSET_QPSK | 5 (0x5) | Sets the modulation type to Shaped Offset QPSK.The ideal symbol timing of Q is offset by half of a symbol period from the ideal symbol timing of I and the waveform is shaped using frequency pulse filter. |

Parent topic:

PSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter.html language=enus -->
## TOPIC 00053: Pulse Shaping Filter

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETERSpecifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively. RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPESpecifies th

### Pulse Shaping Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETER | Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively. |
| RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE | Specifies the pulse-shaping filter used to transmit the signal. This attribute determines the measurement filter to be used for analysis when you set the RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE attribute to Auto. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter_1gad7e7fe3d2bda2cc4900b4d51d2486374.html language=enus -->
## TOPIC 00054: RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETER

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter_1gad7e7fe3d2bda2cc4900b4d51d2486374.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter_1gad7e7fe3d2bda2cc4900b4d51d2486374.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively. SyntaxRFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETERNumeric ValueData TypeAccessApplies To2101264float64Read/WriteN/ARemarks For Gaussian filte

### RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETER

Specifies the rolloff factor for raised cosine and root-raised cosine filter that is used as pulse-shaping filter and measurement filter respectively.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101264 | float64 | Read/Write | N/A |

#### Remarks

For Gaussian filter, this attribute specifies bandwidth * sample duration.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.5.

Parent topic:

Pulse Shaping Filter

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter_1gadb2418f06b41601e7c88310b613ed1b0.html language=enus -->
## TOPIC 00055: RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter_1gadb2418f06b41601e7c88310b613ed1b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__pulse__shaping__filter_1gadb2418f06b41601e7c88310b613ed1b0.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse-shaping filter used to transmit the signal. This attribute determines the measurement filter to be used for analysis when you set the RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE attribute to Auto. SyntaxRFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPENumeric ValueData TypeAccess

### RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE

Specifies the pulse-shaping filter used to transmit the signal. This attribute determines the measurement filter to be used for analysis when you set the [RFMXDEMOD_ATTR_DDEMOD_MEASUREMENT_FILTER_TYPE](group____root__ni_r_fmx_demod__attributes__digital__demod__measurement__filter_1gaeb8d741ae79eced47bf005e2a99b0a74.html) attribute to **Auto**.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101263 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Root Raised Cosine**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_RECTANGULAR | 0 (0x0) | The transmitted waveform is filtered using a rectangular filter. |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_RAISED_COSINE | 1 (0x1) | The transmitted waveform is filtered using a raised cosine filter. Specify the filter Alpha in the RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_PARAMETER attribute. |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_ROOT_RAISED_COSINE | 2 (0x2) | The transmitted waveform is filtered using a root raised cosine filter. Specify the filter Alpha in the DDemod Pulse Shaping Filter Parameter attribute. |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_GAUSSIAN | 3 (0x3) | The transmitted waveform is filtered using a Gaussian filter. Specify the filter bandwidth * sample duration in the DDemod Pulse Shaping Filter Parameter attribute. This filter is applicable only to FSK and MSK modulation types. |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_CUSTOM | 4 (0x4) | The transmitted waveform is filtered using the coefficients that you specify in the RFmxDemod_DDemodCfgPulseShapingFilterCustomCoefficients function. |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_HALF_SINE | 5 (0x5) | The transmitted waveform is filtered using a half sine filter. |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_LINEARIZED_GMSK_EDGE | 6 (0x6) | The transmitted waveform is filtered using an EDGE-specific linearized GMSK filter. |
| RFMXDEMOD_VAL_DDEMOD_PULSE_SHAPING_FILTER_TYPE_SOQPSK_TG | 7 (0x7) | The transmitted waveform is filtered using a SOQPSK - TG filter as defined in IRIG standard. |

Parent topic:

Pulse Shaping Filter

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results.html language=enus -->
## TOPIC 00056: Results

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCarrierEVMFSKIQ ImpairmentsMagnitude ErrorOffset EVMPhase ErrorGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOPReturns the mean amplitude droop per symbol. RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTORReturns the correlation of the measurement waveform and the ref

### Results

#### Groups

- Carrier
- EVM
- FSK
- IQ Impairments
- Magnitude Error
- Offset EVM
- Phase Error

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP | Returns the mean amplitude droop per symbol. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTOR | Returns the correlation of the measurement waveform and the reference waveform. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUND | Indicates whether the synchronization bits were found in the demodulated signal. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results_1ga61031676666a8939232ad00ed869a375.html language=enus -->
## TOPIC 00057: RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results_1ga61031676666a8939232ad00ed869a375.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results_1ga61031676666a8939232ad00ed869a375.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean amplitude droop per symbol. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOPNumeric ValueData TypeAccessApplies To2101311float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sele

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP

Returns the mean amplitude droop per symbol.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101311 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results_1gab797105119a8bfc318a3d4290be6ab0c.html language=enus -->
## TOPIC 00058: RFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUND

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results_1gab797105119a8bfc318a3d4290be6ab0c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results_1gab797105119a8bfc318a3d4290be6ab0c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the synchronization bits were found in the demodulated signal. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUNDNumeric ValueData TypeAccessApplies To2101301int32Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal ins

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUND

Indicates whether the synchronization bits were found in the demodulated signal.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_SYNC_FOUND

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101301 | int32 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results_1gaf4a07e579a4e244d18bd5347285d4c2c.html language=enus -->
## TOPIC 00059: RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTOR

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results_1gaf4a07e579a4e244d18bd5347285d4c2c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results_1gaf4a07e579a4e244d18bd5347285d4c2c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the correlation of the measurement waveform and the reference waveform. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTORNumeric ValueData TypeAccessApplies To2101310float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default sign

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTOR

Returns the correlation of the measurement waveform and the reference waveform.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_MEAN_RHO_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101310 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__carrier_1gab2e499054b115529b49256bf1d0e055d.html language=enus -->
## TOPIC 00060: RFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_PHASE_ERROR

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__carrier_1gab2e499054b115529b49256bf1d0e055d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__carrier_1gab2e499054b115529b49256bf1d0e055d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured phase offset from the transmitted carrier phase. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_PHASE_ERRORNumeric ValueData TypeAccessApplies To2101283float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_PHASE_ERROR

Returns the measured phase offset from the transmitted carrier phase. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_CARRIER_MEAN_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101283 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm.html language=enus -->
## TOPIC 00061: EVM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_PEAKReturns the maximum of the peak EVM measured per acquisition, as a percentage. RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_RMSReturns the maximum of the RMS EVM measured per acquisition, as a percentage. RFMXDEMOD_ATTR

### EVM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_PEAK | Returns the maximum of the peak EVM measured per acquisition, as a percentage. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_RMS | Returns the maximum of the RMS EVM measured per acquisition, as a percentage. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_MODULATION_ERROR_RATIO | Returns the modulation error ratio. This value is expressed in dB. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_PEAK | Returns the mean of the peak EVM measured per acquisition, as a percentage. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_RMS | Returns the mean of the RMS EVM measured per acquisition, as a percentage. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga0274c30a9ddc0bf43d4d23d4c1106226.html language=enus -->
## TOPIC 00062: RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_RMS

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga0274c30a9ddc0bf43d4d23d4c1106226.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga0274c30a9ddc0bf43d4d23d4c1106226.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the RMS EVM measured per acquisition, as a percentage. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_RMSNumeric ValueData TypeAccessApplies To2101285float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_RMS

Returns the maximum of the RMS EVM measured per acquisition, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_RMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101285 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga06716c067c835ba4dc62c2ab61e4e30d.html language=enus -->
## TOPIC 00063: RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga06716c067c835ba4dc62c2ab61e4e30d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga06716c067c835ba4dc62c2ab61e4e30d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the peak EVM measured per acquisition, as a percentage. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_PEAKNumeric ValueData TypeAccessApplies To2101286float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal ins

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_PEAK

Returns the mean of the peak EVM measured per acquisition, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101286 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga6d04300b27a77f85ea14186019516798.html language=enus -->
## TOPIC 00064: RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_PEAK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga6d04300b27a77f85ea14186019516798.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga6d04300b27a77f85ea14186019516798.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the peak EVM measured per acquisition, as a percentage. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_PEAKNumeric ValueData TypeAccessApplies To2101287float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default sign

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_PEAK

Returns the maximum of the peak EVM measured per acquisition, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MAXIMUM_PEAK

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101287 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga731160f8694e20f7f6ea3087c6c18e75.html language=enus -->
## TOPIC 00065: RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_MODULATION_ERROR_RATIO

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga731160f8694e20f7f6ea3087c6c18e75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1ga731160f8694e20f7f6ea3087c6c18e75.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation error ratio. This value is expressed in dB. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_MODULATION_ERROR_RATIONumeric ValueData TypeAccessApplies To2101288float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default s

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_MODULATION_ERROR_RATIO

Returns the modulation error ratio. This value is expressed in dB.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_MODULATION_ERROR_RATIO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101288 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1gae55b5bcfe860d3fb5a8561b431ab2554.html language=enus -->
## TOPIC 00066: RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_RMS

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1gae55b5bcfe860d3fb5a8561b431ab2554.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__evm_1gae55b5bcfe860d3fb5a8561b431ab2554.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the RMS EVM measured per acquisition, as a percentage. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_RMSNumeric ValueData TypeAccessApplies To2101284float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal insta

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_RMS

Returns the mean of the RMS EVM measured per acquisition, as a percentage.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_EVM_MEAN_RMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101284 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

EVM

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk.html language=enus -->
## TOPIC 00067: FSK

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERRORReturns the maximum of peak frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz. RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATIONReturns the reference FSK deviation us

### FSK

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERROR | Returns the maximum of peak frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATION | Returns the reference FSK deviation used to measure the FSK error. This value is expressed in Hz. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_RMS_FSK_ERROR | Returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1ga94385c66fe01c86e4539bf979e65e3be.html language=enus -->
## TOPIC 00068: RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATION

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1ga94385c66fe01c86e4539bf979e65e3be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1ga94385c66fe01c86e4539bf979e65e3be.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference FSK deviation used to measure the FSK error. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATIONNumeric ValueData TypeAccessApplies To2101293float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATION

Returns the reference FSK deviation used to measure the FSK error. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_DEVIATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101293 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1ga99c969cb79215efdd70c731bab4ec18a.html language=enus -->
## TOPIC 00069: RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_RMS_FSK_ERROR

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1ga99c969cb79215efdd70c731bab4ec18a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1ga99c969cb79215efdd70c731bab4ec18a.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_RMS_FSK_ERRORNumeric ValueData TypeAccessApplies To2101294float64Read-OnlyN/ARemarks You do not need to use a selector string to config

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_RMS_FSK_ERROR

Returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MEAN_RMS_FSK_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101294 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1gacb1ee2a4197088e18a3409e1ee844333.html language=enus -->
## TOPIC 00070: RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERROR

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1gacb1ee2a4197088e18a3409e1ee844333.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__fsk_1gacb1ee2a4197088e18a3409e1ee844333.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of peak frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERRORNumeric ValueData TypeAccessApplies To2101295float64Read-OnlyN/ARemarks You do not need to use a selector string to co

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERROR

Returns the maximum of peak frequency error of the FSK symbols measured per acquisition. This value is expressed in Hz.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101295 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

FSK

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__iq__impairments_1gaa2ed96f760857f2de6fc27dad9bca27b.html language=enus -->
## TOPIC 00071: RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEW

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__iq__impairments_1gaa2ed96f760857f2de6fc27dad9bca27b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__iq__impairments_1gaa2ed96f760857f2de6fc27dad9bca27b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEWNumeric ValueData TypeAccessAppl

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEW

Returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101297 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__iq__impairments_1gaee2f65e63d7398fcdf0679455da2471a.html language=enus -->
## TOPIC 00072: RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSET

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__iq__impairments_1gaee2f65e63d7398fcdf0679455da2471a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__iq__impairments_1gaee2f65e63d7398fcdf0679455da2471a.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the offset from the ideal location of the constellation origin. This value is expressed in dB. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSETNumeric ValueData TypeAccessApplies To2101298float64Read-OnlyN/ARemarks You do not need to use a selector string to configure

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSET

Returns the offset from the ideal location of the constellation origin. This value is expressed in dB.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101298 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

IQ Impairments

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__offset__evm_1gac07fb7d82def00aeb1659cd41283a629.html language=enus -->
## TOPIC 00073: RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMS

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__offset__evm_1gac07fb7d82def00aeb1659cd41283a629.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__offset__evm_1gac07fb7d82def00aeb1659cd41283a629.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMSNumeric ValueData TypeAccessApplies To2101308float64Read-OnlyN/ARemarks You do

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMS

Returns the maximum of the RMS EVM, as a percentage, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101308 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Offset EVM

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error.html language=enus -->
## TOPIC 00074: Phase Error

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUMReturns the maximum of the phase error measured per acquisition. This value is expressed in degrees. RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEANReturns the mean of the phase error measured per acquisition. This

### Phase Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM | Returns the maximum of the phase error measured per acquisition. This value is expressed in degrees. |
| RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEAN | Returns the mean of the phase error measured per acquisition. This value is expressed in degrees. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error_1ga3af76546a94a00b3bf1353cc7c70f525.html language=enus -->
## TOPIC 00075: RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error_1ga3af76546a94a00b3bf1353cc7c70f525.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error_1ga3af76546a94a00b3bf1353cc7c70f525.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the phase error measured per acquisition. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUMNumeric ValueData TypeAccessApplies To2101292float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attri

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM

Returns the maximum of the phase error measured per acquisition. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101292 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error_1ga3b1ebc608d9e6bd0b2adc8372e67adcf.html language=enus -->
## TOPIC 00076: RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEAN

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error_1ga3b1ebc608d9e6bd0b2adc8372e67adcf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__results__phase__error_1ga3b1ebc608d9e6bd0b2adc8372e67adcf.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the phase error measured per acquisition. This value is expressed in degrees. SyntaxRFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEANNumeric ValueData TypeAccessApplies To2101291float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute f

### RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEAN

Returns the mean of the phase error measured per acquisition. This value is expressed in degrees.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_RESULTS_PHASE_ERROR_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101291 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Phase Error

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__search.html language=enus -->
## TOPIC 00077: Search

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__search.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__search.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTHSpecifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO attribute to True. RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTOSpecifi

### Search

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH | Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO attribute to True. |
| RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO | Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__search_1ga4e9bea17c446ee3d73d78bfe5b3a525c.html language=enus -->
## TOPIC 00078: RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__search_1ga4e9bea17c446ee3d73d78bfe5b3a525c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__search_1ga4e9bea17c446ee3d73d78bfe5b3a525c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO attribute to True. SyntaxRFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTHNumeric ValueData TypeAccessApplies To2101320float64Read/WriteN/ARemarks You do

### RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH

Specifies the length of the waveform within which the synchronization bit pattern needs to be searched when you set the [RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO](group____root__ni_r_fmx_demod__attributes__digital__demod__search_1ga9dd7e5e22efed9b76492243d4ff78079.html) attribute to **True**.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101320 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.001 seconds.

Parent topic:

Search

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__search_1ga9dd7e5e22efed9b76492243d4ff78079.html language=enus -->
## TOPIC 00079: RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__search_1ga9dd7e5e22efed9b76492243d4ff78079.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__search_1ga9dd7e5e22efed9b76492243d4ff78079.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration. SyntaxRFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTONumeric ValueData TypeAccessApplies To2101319int32Read/WriteN/ARemarks You do not need

### RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO

Specifies whether the measurement should search for synchronization bit pattern in the waveform of length determined by the measurement or search for length duration.

#### Syntax

RFMXDEMOD_ATTR_DDEMOD_SEARCH_LENGTH_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2101319 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DDEMOD_SEARCH_LENGTH_AUTO_FALSE | 0 (0x0) | Synchronization bit pattern is searched in a waveform within the search Length duration. |
| RFMXDEMOD_VAL_DDEMOD_SEARCH_LENGTH_AUTO_TRUE | 1 (0x1) | Synchronization bit pattern is searched in a waveform of length determined by the measurement. |

Parent topic:

Search

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__digital__demod__synchronization.html language=enus -->
## TOPIC 00080: Synchronization

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__digital__demod__synchronization.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__digital__demod__synchronization.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_BITSSpecifies the synchronization bits used to create the reference sequence that must be located in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequenc

### Synchronization

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_BITS | Specifies the synchronization bits used to create the reference sequence that must be located in the demodulated signal. The synchronization bits are modulated based on the modulation type to create the reference sequence. |
| RFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_ENABLED | Specifies whether the demodulator needs to search and synchronize the signal to a known reference sequence. The reference sequence is the symbol representation of a defined set of bits known to be present in the transmitted signal. If the synchronization is found in the demodulated signal, the measurement is performed from this point onward. If the synchronization is not found, the entire signal is used for the measurement. |
| RFMXDEMOD_ATTR_DDEMOD_SYNCHRONIZATION_MEASUREMENT_OFFSET | Specifies the offset, which is the location from which the signal is considered for further measurements. The offset is specified in symbols of the reference sequence. This offset is not applicable when the synchronization bits are not found. |

#### Attachments

None

Parent topic:

Digital Demod

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__trigger.html language=enus -->
## TOPIC 00081: Trigger

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__trigger.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital EdgeIQ Power EdgeMinimum Quiet TimeGroup membersNameDescriptionRFMXDEMOD_ATTR_TRIGGER_DELAYSpecifies the trigger delay time. This value is expressed in seconds. RFMXDEMOD_ATTR_TRIGGER_TYPESpecifies the type of Reference Trigger to use for signal acquisition. AttachmentsNone

### Trigger

#### Groups

- Digital Edge
- IQ Power Edge
- Minimum Quiet Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_TRIGGER_DELAY | Specifies the trigger delay time. This value is expressed in seconds. |
| RFMXDEMOD_ATTR_TRIGGER_TYPE | Specifies the type of Reference Trigger to use for signal acquisition. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__trigger_1gadabf0af6d89bf407b62308e9708b45fd.html language=enus -->
## TOPIC 00082: RFMXDEMOD_ATTR_TRIGGER_DELAY

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__trigger_1gadabf0af6d89bf407b62308e9708b45fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__trigger_1gadabf0af6d89bf407b62308e9708b45fd.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger delay time. This value is expressed in seconds. SyntaxRFMXDEMOD_ATTR_TRIGGER_DELAYNumeric ValueData TypeAccessApplies To2105354float64Read/WriteN/ARemarks If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires p

### RFMXDEMOD_ATTR_TRIGGER_DELAY

Specifies the trigger delay time. This value is expressed in seconds.

#### Syntax

RFMXDEMOD_ATTR_TRIGGER_DELAY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2105354 | float64 | Read/Write | N/A |

#### Remarks

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0 seconds.

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__trigger__digital__edge.html language=enus -->
## TOPIC 00083: Digital Edge

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__trigger__digital__edge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__trigger__digital__edge.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGESpecifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. This attribute is applicable only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Digital Edge. RFMXDEMOD

### Digital Edge

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGE | Specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. This attribute is applicable only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Digital Edge. |
| RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE | Specifies the source terminal for the digital-edge trigger. This attribute is applicable only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Digital Edge. |

#### Attachments

None

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__trigger__digital__edge_1ga8420cb9689759947536841b68f9896e7.html language=enus -->
## TOPIC 00084: RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__trigger__digital__edge_1ga8420cb9689759947536841b68f9896e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__trigger__digital__edge_1ga8420cb9689759947536841b68f9896e7.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. This attribute is applicable only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGENumeric ValueData TypeAccessApplies To210

### RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

Specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. This attribute is applicable only when you set the [RFMXDEMOD_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_demod__attributes__trigger_1gaaa4cc806fa624cbbe322d958fedbb084.html) attribute to **Digital Edge**.

#### Syntax

RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2105350 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXDEMOD_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |
| RFMXDEMOD_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__trigger__digital__edge_1ga99fa0f0fb5843b441e26b1ed308b8829.html language=enus -->
## TOPIC 00085: RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__trigger__digital__edge_1ga99fa0f0fb5843b441e26b1ed308b8829.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__trigger__digital__edge_1ga99fa0f0fb5843b441e26b1ed308b8829.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital-edge trigger. This attribute is applicable only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Digital Edge. SyntaxRFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To2105349char[]Read/WriteN/ARemarks You do not nee

### RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

Specifies the source terminal for the digital-edge trigger. This attribute is applicable only when you set the [RFMXDEMOD_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_demod__attributes__trigger_1gaaa4cc806fa624cbbe322d958fedbb084.html) attribute to **Digital Edge**.

#### Syntax

RFMXDEMOD_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2105349 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Digital Edge

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__trigger__iq__power__edge_1ga5aa37ef0a28d3129d92f6b149e1a4d79.html language=enus -->
## TOPIC 00086: RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__trigger__iq__power__edge_1ga5aa37ef0a28d3129d92f6b149e1a4d79.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__trigger__iq__power__edge_1ga5aa37ef0a28d3129d92f6b149e1a4d79.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel from which the device monitors the trigger. This attribute is applicable only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to IQ Power Edge. SyntaxRFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To2105351char[]Read/WriteN/ARemarks You do

### RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

Specifies the channel from which the device monitors the trigger. This attribute is applicable only when you set the [RFMXDEMOD_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_demod__attributes__trigger_1gaaa4cc806fa624cbbe322d958fedbb084.html) attribute to **IQ Power Edge**.

#### Syntax

RFMXDEMOD_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2105351 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

IQ Power Edge

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__attributes__trigger__minimum__quiet__time_1ga2ff39ef2dae34a21724cce279fc832aa.html language=enus -->
## TOPIC 00087: RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__attributes__trigger__minimum__quiet__time_1ga2ff39ef2dae34a21724cce279fc832aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__attributes__trigger__minimum__quiet__time_1ga2ff39ef2dae34a21724cce279fc832aa.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. If you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to Falling Slope,

### RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. If you set the [RFMXDEMOD_ATTR_TRIGGER_TYPE](group____root__ni_r_fmx_demod__attributes__trigger_1gaaa4cc806fa624cbbe322d958fedbb084.html) attribute to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope attribute to **Falling Slope**, the signal is quiet above the trigger level. This value is expressed in seconds.

#### Syntax

RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 2105356 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Minimum Quiet Time

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions_1ga53bf97435d17e9c43fe392fdf243f3d3.html language=enus -->
## TOPIC 00088: RFmxDemod_Close

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions_1ga53bf97435d17e9c43fe392fdf243f3d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions_1ga53bf97435d17e9c43fe392fdf243f3d3.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the device. Syntaxint32 __stdcall RFmxDemod_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the RFmxInstr_Close function.Enabling the SFP (Soft Front Panel) debug has a performance impact. F

### RFmxDemod_Close

Closes the session to the device.

#### Syntax

int32 __stdcall RFmxDemod_Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_Close](/csh?context=rfmxinstr_rfmxinstrcref_function_close) function.

Note

Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| forceDestroy | [in] | int32 | Specifies whether to destroy the RFmx session.ValueDescriptionRFMXDEMOD_VAL_FALSE (0)Destroys the RFmx session. Call the RFmxDemod_Close function a number of times equal to the number of times you obtained a reference to the RFmx session.RFMXDEMOD_VAL_TRUE (1)Destroys the RFmx session. You do not have to call the RFmxDemod_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |
| Value | Description |  |  |
| RFMXDEMOD_VAL_FALSE (0) | Destroys the RFmx session. Call the RFmxDemod_Close function a number of times equal to the number of times you obtained a reference to the RFmx session. |  |  |
| RFMXDEMOD_VAL_TRUE (1) | Destroys the RFmx session. You do not have to call the RFmxDemod_Close function multiple times. Destroying the RFmx session invalidates all references to the session. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions_1ga55532607c09e80766bac2786fdb86e83.html language=enus -->
## TOPIC 00089: RFmxDemod_GetErrorString

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions_1ga55532607c09e80766bac2786fdb86e83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions_1ga55532607c09e80766bac2786fdb86e83.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an RFmxDemod function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxDemod_GetErrorString(niRFmxInstrHandle

### RFmxDemod_GetErrorString

Converts a status code returned by an RFmxDemod function into a user-readable string. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the **errorDescription** buffer.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| errorCode | [in] | int32 | Passes the statusOrRequiredSize parameter that is returned from any RFmxDemod function. |
| errorDescriptionBufferSize | [in] | int32 | Passes the number of bytes in the char array you specify in errorDescription.If the error description, including the terminating NULL byte, contains more bytes than you indicate in this parameter, the function copies errorDescriptionBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the size of the buffer that you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. |
| errorDescription | [out] | char[] | Returns the user-readable message string that corresponds to the status code you specify.If you pass 0 for errorDescriptionBufferSize, you can pass NULL for the errorDescription buffer parameter to get the size of error description message. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions_1ga8778fe6471a507c439032371a04b08d7.html language=enus -->
## TOPIC 00090: RFmxDemod_Initiate

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions_1ga8778fe6471a507c439032371a04b08d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions_1ga8778fe6471a507c439032371a04b08d7.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in

### RFmxDemod_Initiate

Initiates all enabled measurements. Call this function after configuring the signal and measurement. This function asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. To get the status of measurements, you can use the [RFmxDemod_WaitForMeasurementComplete](group____root__ni_r_fmx_demod__functions__utility_1gaa85442d440552943967ef2815fcc1a1b.html) function or the [RFmxDemod_CheckMeasurementStatus](group____root__ni_r_fmx_demod__functions__utility_1gac75e1700e587faa24c8472ddbe34ee3e.html) function.

#### Syntax

int32 __stdcall RFmxDemod_Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html language=enus -->
## TOPIC 00091: RFmxDemod_GetError

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the errorDescriptionBufferSize parameter. Syntaxint32 __stdcall RFmxDemod_GetError(niRFmxInstrH

### RFmxDemod_GetError

Retrieves and then clears the error information for the session or the current execution thread. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **errorDescriptionBufferSize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_GetError(niRFmxInstrHandle instrumentHandle, int32 *errorCode, int32 errorDescriptionBufferSize, char errorDescription[])

#### Remarks

If the error description, including the terminating NULL byte, is larger than the size you indicate in the **errorDescriptionBufferSize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

If you want to call this function just to get the required buffer size, you must pass 0 for **errorDescriptionBufferSize** and NULL for the errorDescription buffer.

Note

Use the [RFmxDemod_GetErrorString](group____root__ni_r_fmx_demod__functions_1ga55532607c09e80766bac2786fdb86e83.html) function if the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function does not return an error message.

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

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__advanced_1ga36292f6c32eb69d1007de740e89fbe89.html language=enus -->
## TOPIC 00092: RFmxDemod_CreateSignalConfiguration

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__advanced_1ga36292f6c32eb69d1007de740e89fbe89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__advanced_1ga36292f6c32eb69d1007de740e89fbe89.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. Syntaxint32 __stdcall RFmxDemod_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obt

### RFmxDemod_CreateSignalConfiguration

Creates a new instance of a signal.

#### Syntax

int32 __stdcall RFmxDemod_CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| signalName | [in] | char[] | This parameter specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix.Example:"signal::sig1""sig1" |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__advanced_1ga42c6cc87227b3cd8d29b4eef315f8397.html language=enus -->
## TOPIC 00093: RFmxDemod_AnalyzeIQ1Waveform

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__advanced_1ga42c6cc87227b3cd8d29b4eef315f8397.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__advanced_1ga42c6cc87227b3cd8d29b4eef315f8397.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only

### RFmxDemod_AnalyzeIQ1Waveform

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this function after you configure the signal and measurement attributes. You can fetch measurement results using the Fetch functions or result attributes in the attribute node. Use this function only if the [RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE](/csh?context=rfmxinstr_rfmxinstrcref_attribute_recommended_acquisition_type) attribute value is **IQ**.

#### Syntax

int32 __stdcall RFmxDemod_AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)

#### Remarks

Note

Query the Recommended Acquisition Type attribute from the RFmxInstr Attribute after calling the [RFmxDemod Commit](/csh?context=rfmxdemod_rfmxdemodcref_function_commit) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function or the RFmxInstr Initialize function with option string as "AnalysisOnly=1". |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| resultName | [in] | char[] | This parameter specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance.Example:"result::r1""r1" |
| x0 | [in] | float64 | This parameter specifies the start time of the input Y array. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
| iq | [in] | NIComplexSingle[] | This parameter specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| arraySize | [in] | int32 | Specifies the size of the array. |
| reset | [in] | int32 | This parameter resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
| reserved | [in] | int64 | Reserved for future use. Any value passed to this parameter will be ignored. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__advanced_1ga922c47f6e86ee9ccc5fd390a3efb23df.html language=enus -->
## TOPIC 00094: RFmxDemod_ClearAllNamedResults

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__advanced_1ga922c47f6e86ee9ccc5fd390a3efb23df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__advanced_1ga922c47f6e86ee9ccc5fd390a3efb23df.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxDemod_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxDemod_ClearAllNamedResults

Clears all results for the signal that you specify in the **Selector String** parameter.

#### Syntax

int32 __stdcall RFmxDemod_ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__advanced_1gaae2a4f1375602bfb418d5bccc0edd591.html language=enus -->
## TOPIC 00095: RFmxDemod_GetAllNamedResultNames

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__advanced_1gaae2a4f1375602bfb418d5bccc0edd591.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__advanced_1gaae2a4f1375602bfb418d5bccc0edd591.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all the named result names of the signal that you specify in the Selector String parameter. Syntaxint32 __stdcall RFmxDemod_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *

### RFmxDemod_GetAllNamedResultNames

Returns all the named result names of the signal that you specify in the Selector String parameter.

#### Syntax

int32 __stdcall RFmxDemod_GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32 *actualResultNamesSize, int32 *defaultResultExists)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| resultNames | [out] | char[] | This parameter returns an array of result names. |
| resultNamesBufferSize | [in] | int32 | Specifies the size of the resultNames array. Set the resultNamesBufferSize parameter to 0 to get the size of the resultNames array in the return value. |
| actualResultNamesSize | [out] | int32 * | Returns the actual size of the resultNames array, if you pass NULL to resultNames array parameter and set the resultNamesBufferSize parameter to 0. |
| defaultResultExists | [out] | int32 * | This parameter indicates whether the default result exists. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__build__string.html language=enus -->
## TOPIC 00096: Build String

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__build__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__build__string.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_BuildSignalStringCreates a selector string for use with Configuration or Fetch attributes and functions. AttachmentsNone

### Build String

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_BuildSignalString | Creates a selector string for use with Configuration or Fetch attributes and functions. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__build__string_1gad16d2ccc90afdc100fa909f88755372b.html language=enus -->
## TOPIC 00097: RFmxDemod_BuildSignalString

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__build__string_1gad16d2ccc90afdc100fa909f88755372b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__build__string_1gad16d2ccc90afdc100fa909f88755372b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string for use with Configuration or Fetch attributes and functions. Syntaxint32 __stdcall RFmxDemod_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])ParametersNameDirectionTypeDescriptionsignalName[in]char[]This parameter s

### RFmxDemod_BuildSignalString

Creates a selector string for use with Configuration or Fetch attributes and functions.

#### Syntax

int32 __stdcall RFmxDemod_BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| signalName | [in] | char[] | This parameter specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string).Example:"""signal::sig1""sig1" |
| resultName | [in] | char[] | This parameter specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string).Example:"""result::r1""r1" |
| selectorStringLength | [in] | int32 | Specifies the length of the selector string. Set this parameter to 0 to get the minimum buffer size required to build the selector string. |
| selectorString | [in] | char[] | This parameter returns the selector string created by this function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration_1ga233c37e537d831278f60c9382c797b15.html language=enus -->
## TOPIC 00098: RFmxDemod_CfgRFAttenuation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration_1ga233c37e537d831278f60c9382c797b15.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration_1ga233c37e537d831278f60c9382c797b15.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the nominal attenuation and the RFmx driver setting. Syntaxint32 __stdcall RFmxDemod_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)RemarksThis function is a wrapper over the RFmx Instruments API, and calls the

### RFmxDemod_CfgRFAttenuation

Configures the nominal attenuation and the RFmx driver setting.

#### Syntax

int32 __stdcall RFmxDemod_CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgRFAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_rf_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| rfAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver computes the RF attenuation.ValueDescriptionRFMXDEMOD_VAL_RF_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter.RFMXDEMOD_VAL_RF_ATTENUATION_AUTO_TRUE (1)Specifies that the RFmx driver computes the RF attenuation automatically. |
| Value | Description |  |  |
| RFMXDEMOD_VAL_RF_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured using the rfAttenuationValue parameter. |  |  |
| RFMXDEMOD_VAL_RF_ATTENUATION_AUTO_TRUE (1) | Specifies that the RFmx driver computes the RF attenuation automatically. |  |  |
| rfAttenuationValue | [in] | float64 | Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain when the rfAttenuationAuto parameter is set to RFMXDEMOD_VAL_RF_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration_1ga62c7b4820d841c6736f625838a461800.html language=enus -->
## TOPIC 00099: RFmxDemod_CfgMechanicalAttenuation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration_1ga62c7b4820d841c6736f625838a461800.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration_1ga62c7b4820d841c6736f625838a461800.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. Syntaxint32 __stdcall RFmxDemod_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)RemarksThis function is a wrap

### RFmxDemod_CfgMechanicalAttenuation

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

#### Syntax

int32 __stdcall RFmxDemod_CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgMechanicalAttenuation](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_mechanical_attenuation) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| mechanicalAttenuationAuto | [in] | int32 | Specifies whether the RFmx driver automatically chooses an attenuation setting based on the hardware settings.ValueDescriptionRFMXDEMOD_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0)Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter.RFMXDEMOD_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1)Specifies that the measurement computes the mechanical attenuation. |
| Value | Description |  |  |
| RFMXDEMOD_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE (0) | Specifies that the RFmx driver uses the value configured in the mechanicalAttenuationValue parameter. |  |  |
| RFMXDEMOD_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE (1) | Specifies that the measurement computes the mechanical attenuation. |  |  |
| mechanicalAttenuationValue | [in] | float64 | Specifies the level of mechanical attenuation, in dB, for the RF path when the mechanicalAttenuationAuto is set to RFMXDEMOD_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration_1ga674c7b9887eacbc3b028d2143321a095.html language=enus -->
## TOPIC 00100: RFmxDemod_CfgRF

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration_1ga674c7b9887eacbc3b028d2143321a095.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration_1ga674c7b9887eacbc3b028d2143321a095.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF attributes of the signal by specifying the selector string. Syntaxint32 __stdcall RFmxDemod_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)ParametersNameDirectionTypeDescriptioninstrument

### RFmxDemod_CfgRF

Configures the RF attributes of the signal by specifying the selector string.

#### Syntax

int32 __stdcall RFmxDemod_CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| centerFrequency | [in] | float64 | This parameter specifies the carrier frequency, in Hz, of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.The default of this attribute is hardware dependent. |
| referenceLevel | [in] | float64 | This parameter specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this attribute is hardware dependent. |
| externalAttenuation | [in] | float64 | This parameter specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration_1ga81f0bf7a0ac4beec0745ee4564727cf5.html language=enus -->
## TOPIC 00101: RFmxDemod_CfgFrequencyReference

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration_1ga81f0bf7a0ac4beec0745ee4564727cf5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration_1ga81f0bf7a0ac4beec0745ee4564727cf5.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. Syntaxint32 __stdcall RFmxDemod_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)RemarksThis function is a wrapper over the RFmx Instru

### RFmxDemod_CfgFrequencyReference

Configures the Reference Clock and the frequency reference source.

#### Syntax

int32 __stdcall RFmxDemod_CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_CfgFrequencyReference](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_frequency_reference) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| channelName | [in] | char[] | Set this parameter to "" (empty string) or NULL. |
| frequencyReferenceSource | [in] | char[] | Specifies the frequency reference source.ValueDescriptionRFMXDEMOD_VAL_ONBOARD_CLOCK_STR ("Onboard Clock")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock.RFMXDEMOD_VAL_REF_IN_STR ("RefIn")PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector.RFMXDEMOD_VAL_PXI_CLK_STR ("PXI_Clk")PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock.RFMXDEMOD_VAL_CLK_IN_STR ("ClkIn")PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |
| Value | Description |  |  |
| RFMXDEMOD_VAL_ONBOARD_CLOCK_STR ("Onboard Clock") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to its onboard clock. |  |  |
| RFMXDEMOD_VAL_REF_IN_STR ("RefIn") | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal.PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the frequencyReferenceFrequency parameter according to the frequency of your external clock signal.PXIe-5644R/5645R/5646R, PXIe-5840: The RFmx driver locks the device to the signal at the external REF IN connector. |  |  |
| RFMXDEMOD_VAL_PXI_CLK_STR ("PXI_Clk") | PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665, PXIe-5840: The RFmx driver locks the PXIe-5644R/5645R/5646R, PXIe-5663/5663E/5665 to the PXI backplane clock. |  |  |
| RFMXDEMOD_VAL_CLK_IN_STR ("ClkIn") | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652.PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the frequencyReferenceFrequency parameter to 100 MHz.PXIe-5644R/5645R/5646R, PXIe-5840: This configuration does not apply to the PXIe-5644R/5645R/5646R. |  |  |
| frequencyReferenceFrequency | [in] | float64 | Specifies the Reference Clock rate, in Hz, when the frequencyReferenceSource parameter is set to RFMXDEMOD_VAL_CLK_IN_STR or RFMXDEMOD_VAL_REF_IN_STR. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration_1gabd56c3fa71c6e41e3e619a115ea8c65c.html language=enus -->
## TOPIC 00102: RFmxDemod_CfgFrequency

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration_1gabd56c3fa71c6e41e3e619a115ea8c65c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration_1gabd56c3fa71c6e41e3e619a115ea8c65c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxDemod_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)ParametersNameDirectionTypeDescriptionins

### RFmxDemod_CfgFrequency

Configures the expected carrier frequency of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxDemod_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| centerFrequency | [in] | float64 | This parameter specifies the carrier frequency, in Hz, of the RF signal that needs to be acquired. The signal analyzer tunes to this frequency.The default of this attribute is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__amnu_1ga31bcec0c9fda036d5555adbd14ad0d5d.html language=enus -->
## TOPIC 00103: RFmxDemod_ADemodCfgFMDeEmphasis

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__amnu_1ga31bcec0c9fda036d5555adbd14ad0d5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__amnu_1ga31bcec0c9fda036d5555adbd14ad0d5d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the FM de-emphasis filter for analog demodulation measurements. Syntaxint32 __stdcall RFmxDemod_ADemodCfgFMDeEmphasis(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 deEmphasis)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter spe

### RFmxDemod_ADemodCfgFMDeEmphasis

Configures the FM de-emphasis filter for analog demodulation measurements.

#### Syntax

int32 __stdcall RFmxDemod_ADemodCfgFMDeEmphasis(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 deEmphasis)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| deEmphasis | [in] | float64 | This parameter specifies the time constant, in seconds, of the de-emphasis filter, which compensates for the pre-emphasis filter in the FM transmitter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Amnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__amnu_1ga45b53a60cfe6ef12286a1c6adb004bb6.html language=enus -->
## TOPIC 00104: RFmxDemod_ADemodCfgAMCarrierSuppressed

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__amnu_1ga45b53a60cfe6ef12286a1c6adb004bb6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__amnu_1ga45b53a60cfe6ef12286a1c6adb004bb6.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the presence of the amplitude modulated (AM) carrier. Syntaxint32 __stdcall RFmxDemod_ADemodCfgAMCarrierSuppressed(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 amCarrierSuppressedEnabled)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis pa

### RFmxDemod_ADemodCfgAMCarrierSuppressed

Configures the presence of the amplitude modulated (AM) carrier.

#### Syntax

int32 __stdcall RFmxDemod_ADemodCfgAMCarrierSuppressed(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 amCarrierSuppressedEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| amCarrierSuppressedEnabled | [in] | int32 | This parameter specifies whether the carrier of the AM signal is absent.The default value is False.NameValueDescriptionRFMXDEMOD_VAL_ADEMOD_AM_CARRIER_SUPPRESSED_FALSE0 (0x0)The carrier of the AM signal is present.RFMXDEMOD_VAL_ADEMOD_AM_CARRIER_SUPPRESSED_TRUE1 (0x1)The carrier of the AM signal is absent. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_ADEMOD_AM_CARRIER_SUPPRESSED_FALSE | 0 (0x0) | The carrier of the AM signal is present. |  |
| RFMXDEMOD_VAL_ADEMOD_AM_CARRIER_SUPPRESSED_TRUE | 1 (0x1) | The carrier of the AM signal is absent. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Amnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga285788a7650776a0e927b614bb7b9dc7.html language=enus -->
## TOPIC 00105: RFmxDemod_DDemodSetSymbolMap

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga285788a7650776a0e927b614bb7b9dc7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga285788a7650776a0e927b614bb7b9dc7.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the symbol map that is used for digital demodulation measurements. Syntaxint32 __stdcall RFmxDemod_DDemodSetSymbolMap(niRFmxInstrHandle insturmentHandle, char selectorString[], int32 symbolMapType, NIComplexSingle symbolMap[], int32 arraySize[])ParametersNameDirectionTypeDescriptioninsturmentHa

### RFmxDemod_DDemodSetSymbolMap

Sets the symbol map that is used for digital demodulation measurements.

#### Syntax

int32 __stdcall RFmxDemod_DDemodSetSymbolMap(niRFmxInstrHandle insturmentHandle, char selectorString[], int32 symbolMapType, NIComplexSingle symbolMap[], int32 arraySize[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| insturmentHandle | [in] | niRFmxInstrHandle | Specifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| symbolMapType | [in] | int32 | Specifies whether the measurement uses the default symbol map or the map that you configure using this function.ValueDescriptionRFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_AUTO (0)Uses a default symbol map.RFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_CUSTOM (1)Uses the map that you specify. |
| Value | Description |  |  |
| RFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_AUTO (0) | Uses a default symbol map. |  |  |
| RFMXDEMOD_VAL_DDEMOD_SYMBOL_MAP_TYPE_CUSTOM (1) | Uses the map that you specify. |  |  |
| symbolMap | [in] | NIComplexSingle[] | Specifies the symbol map used for demodulation. |
| arraySize | [in] | int32[] | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga5f604e5fc30966bdf90c39de34b3bd57.html language=enus -->
## TOPIC 00106: RFmxDemod_DDemodCfgAveraging

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga5f604e5fc30966bdf90c39de34b3bd57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga5f604e5fc30966bdf90c39de34b3bd57.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for digital demodulation measurements. Syntaxint32 __stdcall RFmxDemod_DDemodCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxDemod_DDemodCfgAveraging

Configures averaging for digital demodulation measurements.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| averagingEnabled | [in] | int32 | This parameter enables averaging for digital demodulation measurement.NameValueDescriptionRFMXDEMOD_VAL_DDEMOD_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXDEMOD_VAL_DDEMOD_AVERAGING_ENABLED_TRUE1 (0x1)The measurement uses the value of the RFMXDEMOD_ATTR_DDEMOD_AVERAGING_COUNT attribute for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_DDEMOD_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXDEMOD_VAL_DDEMOD_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement uses the value of the RFMXDEMOD_ATTR_DDEMOD_AVERAGING_COUNT attribute for the number of acquisitions over which the measurement is averaged. The traces are not averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7727441c45efeda8cad2cec9a331f519.html language=enus -->
## TOPIC 00107: RFmxDemod_DDemodCfgPulseShapingFilterCustomCoefficients

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7727441c45efeda8cad2cec9a331f519.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7727441c45efeda8cad2cec9a331f519.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse-shaping filter coefficients. Syntaxint32 __stdcall RFmxDemod_DDemodCfgPulseShapingFilterCustomCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 pulseShapingFilterCustomCoefficients[], int32 arraySize)ParametersNameDirectionTy

### RFmxDemod_DDemodCfgPulseShapingFilterCustomCoefficients

Configures the pulse-shaping filter coefficients.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgPulseShapingFilterCustomCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 pulseShapingFilterCustomCoefficients[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| x0 | [in] | float64 | This parameter specifies the filter coefficients used as the pulse shaping filter on the transmitter. |
| dx | [in] | float64 | This parameter specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| pulseShapingFilterCustomCoefficients | [in] | float32[] | This parameter specifies the filter coefficients used as the pulse shaping filter on the transmitter. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7d0a8e4d87cb3cd3e39caeaacbfd4041.html language=enus -->
## TOPIC 00108: RFmxDemod_DDemodCfgMeasurementFilter

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7d0a8e4d87cb3cd3e39caeaacbfd4041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7d0a8e4d87cb3cd3e39caeaacbfd4041.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement filter. Syntaxint32 __stdcall RFmxDemod_DDemodCfgMeasurementFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementFilterType, float64 x0, float64 dx, float32 measurementFilterCustomCoefficients[], int32 arraySize)ParametersNameDirectionTypeDesc

### RFmxDemod_DDemodCfgMeasurementFilter

Configures the measurement filter.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgMeasurementFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementFilterType, float64 x0, float64 dx, float32 measurementFilterCustomCoefficients[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| measurementFilterType | [in] | int32 | This parameter specifies whether the measurement needs to compute the measurement filter based on the pulse shaping filter type or uses the custom measurement filter coefficients.The default value is Auto.NameValueDescriptionRFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_AUTO0 (0x0)The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE attribute. If the DDemod Pulse Shaping Filter Type attribute is set to Custom, the signal analyzer enables equalization.RFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_CUSTOM1 (0x1)The signal analyzer uses the coefficients specified by RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients function. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_AUTO | 0 (0x0) | The signal analyzer computes the measurement filter coefficients based on the pulse-shaping filter information that you specify in the RFMXDEMOD_ATTR_DDEMOD_PULSE_SHAPING_FILTER_TYPE attribute. If the DDemod Pulse Shaping Filter Type attribute is set to Custom, the signal analyzer enables equalization. |  |
| RFMXDEMOD_VAL_DDEMOD_MEASUREMENT_FILTER_TYPE_CUSTOM | 1 (0x1) | The signal analyzer uses the coefficients specified by RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients function. |  |
| x0 | [in] | float64 | This parameter always pass 0 to this parameter. Any other values are ignored. |
| dx | [in] | float64 | This parameter specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| measurementFilterCustomCoefficients | [in] | float32[] | This parameter specifies the filter coefficients to be used by demodulator. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7e9462305238c1109d2402cf3c1bc769.html language=enus -->
## TOPIC 00109: RFmxDemod_DDemodCfgFSKDeviation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7e9462305238c1109d2402cf3c1bc769.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga7e9462305238c1109d2402cf3c1bc769.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected FSK deviation. Syntaxint32 __stdcall RFmxDemod_DDemodCfgFSKDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 fskDeviation, int32 fskRefCompEnabled)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies th

### RFmxDemod_DDemodCfgFSKDeviation

Configures the expected FSK deviation.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgFSKDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 fskDeviation, int32 fskRefCompEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| fskDeviation | [in] | float64 | This parameter specifies the expected FSK frequency deviation, in Hz. |
| fskRefCompEnabled | [in] | int32 | This parameter specifies whether the FSK deviation that you specify is used to compensate for gain errors and to compute the FSK error.Default value is False.NameValueDescriptionRFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_FALSE0 (0x0)Does not compensate for gain errors.RFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_TRUE1 (0x1)Compensates for gain errors. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Does not compensate for gain errors. |  |
| RFMXDEMOD_VAL_DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Compensates for gain errors. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gab3b4125d2ab1e2656c296393443ebfeb.html language=enus -->
## TOPIC 00110: RFmxDemod_DDemodCfgEqualizerSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gab3b4125d2ab1e2656c296393443ebfeb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gab3b4125d2ab1e2656c296393443ebfeb.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the equalizer. Syntaxint32 __stdcall RFmxDemod_DDemodCfgEqualizerSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 equalizerMode, int32 equalizerFilterLength, float64 x0, float64 dx, float32 equalizerInitialCoefficientsI[], float32 equalizerInitialCoefficientsQ[], int

### RFmxDemod_DDemodCfgEqualizerSplit

Configures the equalizer.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgEqualizerSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 equalizerMode, int32 equalizerFilterLength, float64 x0, float64 dx, float32 equalizerInitialCoefficientsI[], float32 equalizerInitialCoefficientsQ[], int32 equalizerTrainingCount, float64 equalizerConvergenceFactor, int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| equalizerMode | [in] | int32 | This parameter specifies whether the measurement needs to perform equalization.The default value is Off.NameValueDescriptionRFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_OFF0 (0x0)Equalization is not performed.RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_TRAIN1 (0x1)The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used.RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_HOLD2 (0x2)The filter that you specify using the RFmxDemod_DDemodCfgEqualizerInitialCoefficients function is used as the channel filter, and it is applied before demodulating the acquired signal. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_OFF | 0 (0x0) | Equalization is not performed. |  |
| RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_TRAIN | 1 (0x1) | The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. |  |
| RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_HOLD | 2 (0x2) | The filter that you specify using the RFmxDemod_DDemodCfgEqualizerInitialCoefficients function is used as the channel filter, and it is applied before demodulating the acquired signal. |  |
| equalizerFilterLength | [in] | int32 | This parameter specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. This parameter is ignored when the equalizer initial coefficients are specified. |
| x0 | [in] | float64 | This parameter always pass 0 to this parameter. Any other values are ignored. |
| dx | [in] | float64 | This parameter specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerInitialCoefficientsI | [in] | float32[] | This parameter Specifies the real part of initial coefficients to be used by the equalizer. |
| equalizerInitialCoefficientsQ | [in] | float32[] | This parameter Specifies the imaginary part of initial coefficients to be used by the equalizer. |
| equalizerTrainingCount | [in] | int32 | This parameter specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. |
| equalizerConvergenceFactor | [in] | float64 | This parameter specifies the incremental step used to adapt the equalizer to the channel during the training stage.The default value is 0.0001. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gabd6eda18ae1b0d948fb6fe6932e0408d.html language=enus -->
## TOPIC 00111: RFmxDemod_DDemodCfgSymbolRate

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gabd6eda18ae1b0d948fb6fe6932e0408d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gabd6eda18ae1b0d948fb6fe6932e0408d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the symbol rate for digital demodulation measurements. Syntaxint32 __stdcall RFmxDemod_DDemodCfgSymbolRate(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 symbolRate)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxDemod_DDemodCfgSymbolRate

Configures the symbol rate for digital demodulation measurements.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgSymbolRate(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 symbolRate)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| symbolRate | [in] | float64 | This parameter specifies the symbol rate in Hz.The default value is 100 kHz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gaca88dcf1ff25b6849508abb353d14b36.html language=enus -->
## TOPIC 00112: RFmxDemod_DDemodCfgNumberOfSymbols

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gaca88dcf1ff25b6849508abb353d14b36.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gaca88dcf1ff25b6849508abb353d14b36.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of symbols to be measured. Syntaxint32 __stdcall RFmxDemod_DDemodCfgNumberOfSymbols(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfSymbols)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx sess

### RFmxDemod_DDemodCfgNumberOfSymbols

Configures the number of symbols to be measured.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgNumberOfSymbols(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfSymbols)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| numberOfSymbols | [in] | int32 | This parameter specifies the number of symbols to be analyzed. The measurement acquires additional symbols to account for filter delays. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gacd8d3f4dad47107b4b8a7027777b4487.html language=enus -->
## TOPIC 00113: RFmxDemod_DDemodCfgEqualizer

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gacd8d3f4dad47107b4b8a7027777b4487.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gacd8d3f4dad47107b4b8a7027777b4487.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the equalizer. Syntaxint32 __stdcall RFmxDemod_DDemodCfgEqualizer(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 equalizerMode, int32 equalizerFilterLength, float64 x0, float64 dx, NIComplexSingle equalizerInitialCoefficients[], int32 equalizerTrainingCount, float64 equa

### RFmxDemod_DDemodCfgEqualizer

Configures the equalizer.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgEqualizer(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 equalizerMode, int32 equalizerFilterLength, float64 x0, float64 dx, NIComplexSingle equalizerInitialCoefficients[], int32 equalizerTrainingCount, float64 equalizerConvergenceFactor, int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| equalizerMode | [in] | int32 | This parameter specifies whether the measurement needs to perform equalization.The default value is Off.NameValueDescriptionRFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_OFF0 (0x0)Equalization is not performed.RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_TRAIN1 (0x1)The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used.RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_HOLD2 (0x2)The filter that you specify using the RFmxDemod_DDemodCfgEqualizerInitialCoefficients function is used as the channel filter, and it is applied before demodulating the acquired signal. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_OFF | 0 (0x0) | Equalization is not performed. |  |
| RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_TRAIN | 1 (0x1) | The adaptive feedforward equalizer is turned ON to compensate for the effect of the channel. You can set the initial coefficients to be used by the equalizer. If you do not specify the initial coefficients, an impulse is used. |  |
| RFMXDEMOD_VAL_DDEMOD_EQUALIZER_MODE_HOLD | 2 (0x2) | The filter that you specify using the RFmxDemod_DDemodCfgEqualizerInitialCoefficients function is used as the channel filter, and it is applied before demodulating the acquired signal. |  |
| equalizerFilterLength | [in] | int32 | This parameter specifies the length of the equalization filter to be computed. The length is specified in terms of symbols. This parameter is ignored when the equalizer initial coefficients are specified. |
| x0 | [in] | float64 | This parameter always pass 0 to this parameter. Any other values are ignored. |
| dx | [in] | float64 | This parameter specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerInitialCoefficients | [in] | NIComplexSingle[] | This parameter specifies the initial coefficients to be used by the equalizer. |
| equalizerTrainingCount | [in] | int32 | This parameter specifies the number of iterations during which the equalizer adapts its coefficients in the training stage. |
| equalizerConvergenceFactor | [in] | float64 | This parameter specifies the incremental step used to adapt the equalizer to the channel during the training stage.The default value is 0.0001. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gace909d6fa4c384d3268615191fca94b6.html language=enus -->
## TOPIC 00114: RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gace909d6fa4c384d3268615191fca94b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gace909d6fa4c384d3268615191fca94b6.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement filter custom coefficients. Syntaxint32 __stdcall RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 measurementFilterCustomCoefficients[], int32 arraySize)ParametersNameDirectio

### RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients

Configures the measurement filter custom coefficients.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgMeasurementFilterCustomCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 measurementFilterCustomCoefficients[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| x0 | [in] | float64 | This parameter specifies the filter coefficients to be used by demodulator. |
| dx | [in] | float64 | This parameter specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| measurementFilterCustomCoefficients | [in] | float32[] | This parameter specifies the filter coefficients to be used by demodulator. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gad369dd5cba1fca0aee633a927ede70d8.html language=enus -->
## TOPIC 00115: RFmxDemod_DDemodCfgSignalStructure

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gad369dd5cba1fca0aee633a927ede70d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gad369dd5cba1fca0aee633a927ede70d8.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the structure of the incoming signal to be either a continuous signal or a bursty signal. Syntaxint32 __stdcall RFmxDemod_DDemodCfgSignalStructure(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 signalStructure)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niR

### RFmxDemod_DDemodCfgSignalStructure

Configures the structure of the incoming signal to be either a continuous signal or a bursty signal.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgSignalStructure(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 signalStructure)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| signalStructure | [in] | int32 | This parameter specifies whether the signal is either a bursty signal or a continuous signal.The default value is Continuous.NameValueDescriptionRFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_BURSTED0 (0x0)The signal is a bursty signal.RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_CONTINUOUS1 (0x1)The signal is a continuous signal. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_BURSTED | 0 (0x0) | The signal is a bursty signal. |  |
| RFMXDEMOD_VAL_DDEMOD_SIGNAL_STRUCTURE_CONTINUOUS | 1 (0x1) | The signal is a continuous signal. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gada032c540791f3f7d873551b946362f1.html language=enus -->
## TOPIC 00116: RFmxDemod_DDemodCfgEqualizerInitialCoefficients

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gada032c540791f3f7d873551b946362f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__dmnu_1gada032c540791f3f7d873551b946362f1.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the equalizer coefficients. Syntaxint32 __stdcall RFmxDemod_DDemodCfgEqualizerInitialCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle equalizerInitialCoefficients[], int32 arraySize)ParametersNameDirectionTypeDescriptioninstru

### RFmxDemod_DDemodCfgEqualizerInitialCoefficients

Configures the equalizer coefficients.

#### Syntax

int32 __stdcall RFmxDemod_DDemodCfgEqualizerInitialCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle equalizerInitialCoefficients[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| x0 | [in] | float64 | This parameter always pass 0 to this parameter. Any other values are ignored. |
| dx | [in] | float64 | This parameter specifies the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerInitialCoefficients | [in] | NIComplexSingle[] | This parameter specifies the initial coefficients to be used by the equalizer. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Dmnu

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__trigger.html language=enus -->
## TOPIC 00117: Trigger

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__trigger.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_CfgDigitalEdgeTriggerConfigures the digital edge trigger. RFmxDemod_CfgIQPowerEdgeTriggerConfigures the I/Q power edge trigger. RFmxDemod_CfgSoftwareEdgeTriggerConfigures the software-edge trigger. RFmxDemod_DisableTriggerDisables the trigger. Attachme

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_CfgDigitalEdgeTrigger | Configures the digital edge trigger. |
| RFmxDemod_CfgIQPowerEdgeTrigger | Configures the I/Q power edge trigger. |
| RFmxDemod_CfgSoftwareEdgeTrigger | Configures the software-edge trigger. |
| RFmxDemod_DisableTrigger | Disables the trigger. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__trigger_1ga1404d6cf93204a0ca975821098e8c930.html language=enus -->
## TOPIC 00118: RFmxDemod_CfgDigitalEdgeTrigger

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__trigger_1ga1404d6cf93204a0ca975821098e8c930.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__trigger_1ga1404d6cf93204a0ca975821098e8c930.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the digital edge trigger. Syntaxint32 __stdcall RFmxDemod_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFm

### RFmxDemod_CfgDigitalEdgeTrigger

Configures the digital edge trigger.

#### Syntax

int32 __stdcall RFmxDemod_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital-edge trigger. This parameter is used only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Digital Edge.The default value is PFI0.Name (Value)DescriptionPFI0 (PFI0)The trigger is received on PFI 0.PFI1 (PFI1)The trigger is received on PFI 1.PXI_Trig0 (PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1 (PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2 (PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3 (PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4 (PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5 (PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6 (PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7 (PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR (PXI_STAR)The trigger is received on the PXI star trigger line.PXIe_DStarB (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line.TimerEvent (TimerEvent)The trigger is received from the Timer Event. |
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
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |  |  |
| TimerEvent (TimerEvent) | The trigger is received from the Timer Event. |  |  |
| digitalEdge | [in] | int32 | This parameter specifies whether the signal analyzer detects a rising or falling edge on the digital-edge trigger signal. The parameter is used only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to Digital Edge.The default value is Rising Edge.NameValueDescriptionRFMXDEMOD_VAL_DIGITAL_EDGE_RISING_EDGE0 (0x0)The trigger asserts on the rising edge of the signal.RFMXDEMOD_VAL_DIGITAL_EDGE_FALLING_EDGE1 (0x1)The trigger asserts on the falling edge of the signal. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |  |
| RFMXDEMOD_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__trigger_1ga4b77925ef6f965c4b8a2e82a55b645a4.html language=enus -->
## TOPIC 00119: RFmxDemod_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__trigger_1ga4b77925ef6f965c4b8a2e82a55b645a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__trigger_1ga4b77925ef6f965c4b8a2e82a55b645a4.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the software-edge trigger. Syntaxint32 __stdcall RFmxDemod_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RF

### RFmxDemod_CfgSoftwareEdgeTrigger

Configures the software-edge trigger.

#### Syntax

int32 __stdcall RFmxDemod_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__trigger_1gaa55db2ac218b53775f8dcddeaad3bd15.html language=enus -->
## TOPIC 00120: RFmxDemod_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__trigger_1gaa55db2ac218b53775f8dcddeaad3bd15.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__trigger_1gaa55db2ac218b53775f8dcddeaad3bd15.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the I/Q power edge trigger. Syntaxint32 __stdcall RFmxDemod_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], float64 iqPowerEdgeLevel, int32 iqPowerEdgeSlope, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQ

### RFmxDemod_CfgIQPowerEdgeTrigger

Configures the I/Q power edge trigger.

#### Syntax

int32 __stdcall RFmxDemod_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], float64 iqPowerEdgeLevel, int32 iqPowerEdgeSlope, float64 triggerDelay, int32 triggerMinQuietTimeMode, float64 triggerMinQuietTimeDuration, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger.The default value is 0. |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative, and this value is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this attribute is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This parameter is used only when you set the RFMXDEMOD_ATTR_TRIGGER_TYPE attribute to IQ Power Edge.The default value is Rising Slope.NameValueDescriptionRFMXDEMOD_VAL_IQ_POWER_EDGE_RISING_SLOPE0 (0x0)The trigger asserts when the signal power is rising.RFMXDEMOD_VAL_IQ_POWER_EDGE_FALLING_SLOPE1 (0x1)The trigger asserts when the signal power is falling. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |  |
| RFMXDEMOD_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time, in seconds. |
| triggerMinQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering.The default value is Manual.NameValueDescriptionRFMXDEMOD_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL0 (0x0)The minimum quiet time for triggering is the value of the RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute.RFMXDEMOD_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO1 (0x1)The measurement computes the minimum quiet time used for triggering. |
| Name | Value | Description |  |
| RFMXDEMOD_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXDEMOD_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |  |
| RFMXDEMOD_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |  |
| triggerMinQuietTimeDuration | [in] | float64 | This parameter specifies the time duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q power-edge trigger. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__configuration__trigger_1gaa87360297c21edd59dc78f9f3e4a6668.html language=enus -->
## TOPIC 00121: RFmxDemod_DisableTrigger

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__configuration__trigger_1gaa87360297c21edd59dc78f9f3e4a6668.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__configuration__trigger_1gaa87360297c21edd59dc78f9f3e4a6668.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the trigger. Syntaxint32 __stdcall RFmxDemod_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxIn

### RFmxDemod_DisableTrigger

Disables the trigger.

#### Syntax

int32 __stdcall RFmxDemod_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch.html language=enus -->
## TOPIC 00122: Fetch

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsADGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- A
- D

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a.html language=enus -->
## TOPIC 00123: A

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_ADemodFetchAMMaximumModulationDepthFetches the AM maximum modulation depth. RFmxDemod_ADemodFetchAMMeanModulationDepthFetches AM mean modulation depth for analog demodulation measurements. RFmxDemod_ADemodFetchCarrierMeasurementFetches the carrier meas

### A

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_ADemodFetchAMMaximumModulationDepth | Fetches the AM maximum modulation depth. |
| RFmxDemod_ADemodFetchAMMeanModulationDepth | Fetches AM mean modulation depth for analog demodulation measurements. |
| RFmxDemod_ADemodFetchCarrierMeasurement | Fetches the carrier measurement. |
| RFmxDemod_ADemodFetchDemodSignalTrace | Fetches the demodulated signal trace. |
| RFmxDemod_ADemodFetchDemodSpectrumTrace | Fetches the demodulated signal spectrum trace. |
| RFmxDemod_ADemodFetchDistortions | Fetches distortions for analog demodulation measurements. |
| RFmxDemod_ADemodFetchFMMaximumDeviation | Fetches the FM maximum deviation measurements. |
| RFmxDemod_ADemodFetchFMMeanDeviation | Fetches the FM mean deviation measurements. |
| RFmxDemod_ADemodFetchMeanModulationFrequency | Fetches the mean modulation frequency. |
| RFmxDemod_ADemodFetchPMMaximumDeviation | Fetches the PM maximum deviation measurements. |
| RFmxDemod_ADemodFetchPMMeanDeviation | Fetches the PM mean deviation measurements. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1ga2232601fb3e97d54094cf63149675870.html language=enus -->
## TOPIC 00124: RFmxDemod_ADemodFetchAMMeanModulationDepth

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1ga2232601fb3e97d54094cf63149675870.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1ga2232601fb3e97d54094cf63149675870.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches AM mean modulation depth for analog demodulation measurements. Syntaxint32 __stdcall RFmxDemod_ADemodFetchAMMeanModulationDepth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanModulationDepth, float64 *meanHalfPeakToPeak, float64 *meanRMS, float64 *me

### RFmxDemod_ADemodFetchAMMeanModulationDepth

Fetches AM mean modulation depth for analog demodulation measurements.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchAMMeanModulationDepth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanModulationDepth, float64 *meanHalfPeakToPeak, float64 *meanRMS, float64 *meanPositivePeak, float64 *meanNegativePeak)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanModulationDepth | [out] | float64 * | This parameter returns the mean amplitude variation, as a percentage, around the unmodulated carrier amplitude. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |
| meanHalfPeakToPeak | [out] | float64 * | This parameter returns the mean (peak-to-peak)/2 amplitude, as a percentage, of the modulating signal. |
| meanRMS | [out] | float64 * | This parameter returns the mean RMS amplitude of the modulating signal. |
| meanPositivePeak | [out] | float64 * | This parameter returns the mean positive peak amplitude, as a percentage, of the modulating signal. |
| meanNegativePeak | [out] | float64 * | This parameter returns the mean negative peak amplitude, as a percentage, of the modulating signal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1ga4c1bdfe59b17c4689253768c4579ea7f.html language=enus -->
## TOPIC 00125: RFmxDemod_ADemodFetchFMMaximumDeviation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1ga4c1bdfe59b17c4689253768c4579ea7f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1ga4c1bdfe59b17c4689253768c4579ea7f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the FM maximum deviation measurements. Syntaxint32 __stdcall RFmxDemod_ADemodFetchFMMaximumDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumDeviation, float64 *maximumHalfPeakToPeak, float64 *maximumRMS, float64 *maximumPositivePeak, float

### RFmxDemod_ADemodFetchFMMaximumDeviation

Fetches the FM maximum deviation measurements.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchFMMaximumDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumDeviation, float64 *maximumHalfPeakToPeak, float64 *maximumRMS, float64 *maximumPositivePeak, float64 *maximumNegativePeak)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| maximumDeviation | [out] | float64 * | This parameter returns the maximum frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |
| maximumHalfPeakToPeak | [out] | float64 * | This parameter returns the maximum (peak-to-peak)/2 frequency variation, in Hz, around the nominal frequency of the FM carrier measured across multiple acquisitions. |
| maximumRMS | [out] | float64 * | This parameter returns the maximum RMS frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |
| maximumPositivePeak | [out] | float64 * | This parameter returns the maximum positive peak frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |
| maximumNegativePeak | [out] | float64 * | This parameter returns the maximum negative peak frequency deviation, in Hz, of the frequency-modulated signal measured across multiple acquisitions. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1ga8b7eab327706d0d0c109403f96b5054f.html language=enus -->
## TOPIC 00126: RFmxDemod_ADemodFetchDemodSpectrumTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1ga8b7eab327706d0d0c109403f96b5054f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1ga8b7eab327706d0d0c109403f96b5054f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the demodulated signal spectrum trace. Syntaxint32 __stdcall RFmxDemod_ADemodFetchDemodSpectrumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 demodulatedSpectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDire

### RFmxDemod_ADemodFetchDemodSpectrumTrace

Fetches the demodulated signal spectrum trace.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchDemodSpectrumTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 demodulatedSpectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start bin frequency, in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing, in Hz. |
| demodulatedSpectrum | [out] | float32[] | This parameter returns the demodulated signal spectrum. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gaced1e9efc96fa5deec745767595795b4.html language=enus -->
## TOPIC 00127: RFmxDemod_ADemodFetchPMMeanDeviation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gaced1e9efc96fa5deec745767595795b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gaced1e9efc96fa5deec745767595795b4.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PM mean deviation measurements. Syntaxint32 __stdcall RFmxDemod_ADemodFetchPMMeanDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanHalfPeakToPeak, float64 *meanRMS, float64 *meanPositivePeak, float64 *meanNegativePe

### RFmxDemod_ADemodFetchPMMeanDeviation

Fetches the PM mean deviation measurements.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchPMMeanDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanHalfPeakToPeak, float64 *meanRMS, float64 *meanPositivePeak, float64 *meanNegativePeak)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanDeviation | [out] | float64 * | This parameter returns the mean deviation around the unmodulated carrier phase. |
| meanHalfPeakToPeak | [out] | float64 * | This parameter returns the mean (peak-to-peak)/2 phase deviation, in degrees, around the unmodulated carrier phase. |
| meanRMS | [out] | float64 * | This parameter returns the mean RMS phase deviation, in degrees, of the phase-modulated signal. |
| meanPositivePeak | [out] | float64 * | This parameter returns the mean positive peak phase deviation, in degrees, around the unmodulated carrier phase. |
| meanNegativePeak | [out] | float64 * | This parameter returns the mean negative peak phase deviation, in degrees, around the unmodulated carrier phase. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gad0bdcdfa68dc818e4e72f19de61c3b07.html language=enus -->
## TOPIC 00128: RFmxDemod_ADemodFetchDistortions

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gad0bdcdfa68dc818e4e72f19de61c3b07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gad0bdcdfa68dc818e4e72f19de61c3b07.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches distortions for analog demodulation measurements. Syntaxint32 __stdcall RFmxDemod_ADemodFetchDistortions(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageSinad, float64 *averageSnr, float64 *averageThd, float64 *averageThdWithNoise)ParametersNameDir

### RFmxDemod_ADemodFetchDistortions

Fetches distortions for analog demodulation measurements.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchDistortions(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *averageSinad, float64 *averageSnr, float64 *averageThd, float64 *averageThdWithNoise)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| averageSinad | [out] | float64 * | This parameter returns the averaged signal-to-noise and distortion ratio, in dB, of the demodulated signal. |
| averageSnr | [out] | float64 * | This parameter returns the averaged signal-to-noise ratio, in dB, of the demodulated signal. |
| averageThd | [out] | float64 * | This parameter returns the averaged total harmonic distortion, as a percentage, of demodulated signal. |
| averageThdWithNoise | [out] | float64 * | This parameter returns the averaged total harmonic distortion with noise, as a percentage, of the demodulated signal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gad840eb6749e085b5c7dcbdaf10022406.html language=enus -->
## TOPIC 00129: RFmxDemod_ADemodFetchCarrierMeasurement

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gad840eb6749e085b5c7dcbdaf10022406.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gad840eb6749e085b5c7dcbdaf10022406.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the carrier measurement. Syntaxint32 __stdcall RFmxDemod_ADemodFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanCarrierFrequencyError, float64 *meanCarrierPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxIns

### RFmxDemod_ADemodFetchCarrierMeasurement

Fetches the carrier measurement.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanCarrierFrequencyError, float64 *meanCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanCarrierFrequencyError | [out] | float64 * | This parameter returns the mean of the measured carrier frequency error, in Hz. |
| meanCarrierPower | [out] | float64 * | This parameter returns the mean of the measured carrier power, in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gadb78324819d3a1547856ce42b6537375.html language=enus -->
## TOPIC 00130: RFmxDemod_ADemodFetchAMMaximumModulationDepth

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gadb78324819d3a1547856ce42b6537375.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gadb78324819d3a1547856ce42b6537375.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the AM maximum modulation depth. Syntaxint32 __stdcall RFmxDemod_ADemodFetchAMMaximumModulationDepth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumModulationDepth, float64 *maximumHalfPeakToPeak, float64 *maximumRMS, float64 *maximumPositivePeak,

### RFmxDemod_ADemodFetchAMMaximumModulationDepth

Fetches the AM maximum modulation depth.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchAMMaximumModulationDepth(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumModulationDepth, float64 *maximumHalfPeakToPeak, float64 *maximumRMS, float64 *maximumPositivePeak, float64 *maximumNegativePeak)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| maximumModulationDepth | [out] | float64 * | This parameter returns the maximum modulation depth, as a percentage, measured across multiple acquisitions. |
| maximumHalfPeakToPeak | [out] | float64 * | This parameter returns the maximum (peak-to-peak)/2 amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |
| maximumRMS | [out] | float64 * | This parameter returns the maximum RMS amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |
| maximumPositivePeak | [out] | float64 * | This parameter returns the maximum positive peak amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |
| maximumNegativePeak | [out] | float64 * | This parameter returns the maximum negative peak amplitude, as a percentage, of the modulating signal measured across multiple acquisitions. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gae69a47185ebdec9936d13f54f9b1a5c7.html language=enus -->
## TOPIC 00131: RFmxDemod_ADemodFetchMeanModulationFrequency

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gae69a47185ebdec9936d13f54f9b1a5c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gae69a47185ebdec9936d13f54f9b1a5c7.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean modulation frequency. Syntaxint32 __stdcall RFmxDemod_ADemodFetchMeanModulationFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanModulationFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxDemod_ADemodFetchMeanModulationFrequency

Fetches the mean modulation frequency.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchMeanModulationFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanModulationFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanModulationFrequency | [out] | float64 * | This parameter returns the mean of the demodulated signal frequency. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gaf1a0ea77271bd3ded1e2e0dbe908f856.html language=enus -->
## TOPIC 00132: RFmxDemod_ADemodFetchDemodSignalTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gaf1a0ea77271bd3ded1e2e0dbe908f856.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gaf1a0ea77271bd3ded1e2e0dbe908f856.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the demodulated signal trace. Syntaxint32 __stdcall RFmxDemod_ADemodFetchDemodSignalTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 demodulatedSignal[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDesc

### RFmxDemod_ADemodFetchDemodSignalTrace

Fetches the demodulated signal trace.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchDemodSignalTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 demodulatedSignal[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start time, in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration, in seconds. |
| demodulatedSignal | [out] | float32[] | This parameter returns the demodulated signal. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gaf2a3ab4c98641b11eb80d29df8723a20.html language=enus -->
## TOPIC 00133: RFmxDemod_ADemodFetchPMMaximumDeviation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gaf2a3ab4c98641b11eb80d29df8723a20.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gaf2a3ab4c98641b11eb80d29df8723a20.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PM maximum deviation measurements. Syntaxint32 __stdcall RFmxDemod_ADemodFetchPMMaximumDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumDeviation, float64 *maximumHalfPeakToPeak, float64 *maximumRMS, float64 *maximumPositivePeak, float

### RFmxDemod_ADemodFetchPMMaximumDeviation

Fetches the PM maximum deviation measurements.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchPMMaximumDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumDeviation, float64 *maximumHalfPeakToPeak, float64 *maximumRMS, float64 *maximumPositivePeak, float64 *maximumNegativePeak)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| maximumDeviation | [out] | float64 * | This parameter returns the maximum phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. |
| maximumHalfPeakToPeak | [out] | float64 * | This parameter returns the maximum (peak to peak)/2 phase deviation, in degrees, around the unmodulated carrier phase measured over multiple acquisitions. |
| maximumRMS | [out] | float64 * | This parameter returns the maximum RMS phase deviation, in degrees, of the PM signal measured over multiple acquisitions. |
| maximumPositivePeak | [out] | float64 * | This parameter returns the maximum positive peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |
| maximumNegativePeak | [out] | float64 * | This parameter returns the maximum negative peak phase deviation, in degrees, around the unmodulated carrier phase, measured across multiple acquisitions. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__a_1gafc0ac320d0af68d744ca2a7fb7186e2a.html language=enus -->
## TOPIC 00134: RFmxDemod_ADemodFetchFMMeanDeviation

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__a_1gafc0ac320d0af68d744ca2a7fb7186e2a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__a_1gafc0ac320d0af68d744ca2a7fb7186e2a.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the FM mean deviation measurements. Syntaxint32 __stdcall RFmxDemod_ADemodFetchFMMeanDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanHalfPeakToPeak, float64 *meanRMS, float64 *meanPositivePeak, float64 *meanNegativePe

### RFmxDemod_ADemodFetchFMMeanDeviation

Fetches the FM mean deviation measurements.

#### Syntax

int32 __stdcall RFmxDemod_ADemodFetchFMMeanDeviation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanHalfPeakToPeak, float64 *meanRMS, float64 *meanPositivePeak, float64 *meanNegativePeak)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanDeviation | [out] | float64 * | This parameter returns the mean deviation, in Hz, of the frequency-modulated signal. |
| meanHalfPeakToPeak | [out] | float64 * | This parameter returns the mean (peak-to-peak)/2 frequency variation, in Hz, around the nominal frequency of the FM carrier. |
| meanRMS | [out] | float64 * | This parameter returns the mean RMS frequency deviation, in Hz, of the frequency-modulated signal. |
| meanPositivePeak | [out] | float64 * | This parameter returns the mean positive peak frequency deviation, in Hz, of the frequency-modulated signal. |
| meanNegativePeak | [out] | float64 * | This parameter returns the mean negative peak frequency deviation of the frequency-modulated signal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

A

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d.html language=enus -->
## TOPIC 00135: D

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_DDemodFetchCarrierMeasurementFetches the carrier measurement. RFmxDemod_DDemodFetchConstellationTraceFetches the constellation trace. RFmxDemod_DDemodFetchConstellationTraceSplitFetches the constellation trace. RFmxDemod_DDemodFetchDemodulatedBitsFetch

### D

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_DDemodFetchCarrierMeasurement | Fetches the carrier measurement. |
| RFmxDemod_DDemodFetchConstellationTrace | Fetches the constellation trace. |
| RFmxDemod_DDemodFetchConstellationTraceSplit | Fetches the constellation trace. |
| RFmxDemod_DDemodFetchDemodulatedBits | Fetches the demodulated bit stream. |
| RFmxDemod_DDemodFetchEVM | Fetches the EVM measurements. |
| RFmxDemod_DDemodFetchEVMTrace | Fetches the EVM trace. |
| RFmxDemod_DDemodFetchEqualizerCoefficients | Fetches the updated equalizer coefficients. |
| RFmxDemod_DDemodFetchEqualizerCoefficientsSplit | Fetches the updated equalizer coefficients. |
| RFmxDemod_DDemodFetchFSKDeviationTrace | Fetches the frequency-shift keying (FSK) deviation trace. |
| RFmxDemod_DDemodFetchFSKResults | Fetches frequency-shift keying (FSK) results. |
| RFmxDemod_DDemodFetchIQImpairments | Fetches I/Q impairments. |
| RFmxDemod_DDemodFetchMagnitudeError | Fetches the magnitude error measurements. |
| RFmxDemod_DDemodFetchMagnitudeErrorTrace | Fetches the magnitude error trace. |
| RFmxDemod_DDemodFetchMeanAmplitudeDroop | Fetches the mean amplitude droop per symbol. |
| RFmxDemod_DDemodFetchMeanIQOriginOffset | Fetches the offset, in dB, from the ideal location of the constellation origin. |
| RFmxDemod_DDemodFetchMeanQuadratureSkew | Fetches the mean quadrature skew. |
| RFmxDemod_DDemodFetchMeanRhoFactor | Fetches the correlation of the measurement waveform and the reference waveform. |
| RFmxDemod_DDemodFetchMeasurementWaveform | Fetches the measurement waveform. |
| RFmxDemod_DDemodFetchMeasurementWaveformSplit | Fetches the measurement waveform. |
| RFmxDemod_DDemodFetchOffsetConstellationTrace | Fetches the offset constellation trace. |
| RFmxDemod_DDemodFetchOffsetConstellationTraceSplit | Fetches the offset constellation trace. |
| RFmxDemod_DDemodFetchOffsetEVM | Fetches the offset error vector magnitude (EVM). |
| RFmxDemod_DDemodFetchOffsetEVMTrace | Fetches the offset error vector magnitude (EVM) trace measured on OQPSK signal. |
| RFmxDemod_DDemodFetchPhaseError | Fetches the phase error measurements. |
| RFmxDemod_DDemodFetchPhaseErrorTrace | Fetches the phase error trace. |
| RFmxDemod_DDemodFetchReferenceWaveform | Fetches the reference waveform. |
| RFmxDemod_DDemodFetchReferenceWaveformSplit | Fetches the reference waveform. |
| RFmxDemod_DDemodFetchSyncFound | Indicates whether synchronization bits were found in the demodulated symbol. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga04d27e37e5ddff2ff4aecdd6713245d7.html language=enus -->
## TOPIC 00136: RFmxDemod_DDemodFetchConstellationTraceSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga04d27e37e5ddff2ff4aecdd6713245d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga04d27e37e5ddff2ff4aecdd6713245d7.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationTraceI[], float32 constellationTraceQ[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectio

### RFmxDemod_DDemodFetchConstellationTraceSplit

Fetches the constellation trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationTraceI[], float32 constellationTraceQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| constellationTraceI | [out] | float32[] | This parameter Returns the real part of constellation trace. |
| constellationTraceQ | [out] | float32[] | This parameter Returns the imaginary part of constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga0b697e67600e1fa8a51a7a9825cb71c7.html language=enus -->
## TOPIC 00137: RFmxDemod_DDemodFetchDemodulatedBits

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga0b697e67600e1fa8a51a7a9825cb71c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga0b697e67600e1fa8a51a7a9825cb71c7.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the demodulated bit stream. Syntaxint32 __stdcall RFmxDemod_DDemodFetchDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 demodulatedBits[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxI

### RFmxDemod_DDemodFetchDemodulatedBits

Fetches the demodulated bit stream.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchDemodulatedBits(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int8 demodulatedBits[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| demodulatedBits | [out] | int8[] | This parameter returns the demodulated bit stream. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga0f48d779344ed85142e1dbb4b231a6aa.html language=enus -->
## TOPIC 00138: RFmxDemod_DDemodFetchMeanIQOriginOffset

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga0f48d779344ed85142e1dbb4b231a6aa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga0f48d779344ed85142e1dbb4b231a6aa.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset, in dB, from the ideal location of the constellation origin. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMeanIQOriginOffset(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 *meanIQOriginOffset)ParametersNameDirectionTypeDescriptioninstrumentHandle

### RFmxDemod_DDemodFetchMeanIQOriginOffset

Fetches the offset, in dB, from the ideal location of the constellation origin.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMeanIQOriginOffset(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 *meanIQOriginOffset)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanIQOriginOffset | [out] | float32 * | This parameter returns the offset, in dB, from the ideal location of the constellation origin. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga22315e899f7743e80e092d8b347ef54c.html language=enus -->
## TOPIC 00139: RFmxDemod_DDemodFetchIQImpairments

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga22315e899f7743e80e092d8b347ef54c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga22315e899f7743e80e092d8b347ef54c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q impairments. Syntaxint32 __stdcall RFmxDemod_DDemodFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanIQGainImbalance, float64 *meanQuadratureSkew, float64 *meanIQOriginOffset)ParametersNameDirectionTypeDescriptioninstrumentHandle[

### RFmxDemod_DDemodFetchIQImpairments

Fetches I/Q impairments.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanIQGainImbalance, float64 *meanQuadratureSkew, float64 *meanIQOriginOffset)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanIQGainImbalance | [out] | float64 * | This parameter returns the measured ratio of I gain to Q gain, in dB. |
| meanQuadratureSkew | [out] | float64 * | This parameter returns a measure of I and Q components in the signal that are not perfectly orthogonal. |
| meanIQOriginOffset | [out] | float64 * | This parameter returns the offset, in dB, from the ideal location of the constellation origin. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga26bbe3d85d828e2736c31825d2b1a436.html language=enus -->
## TOPIC 00140: RFmxDemod_DDemodFetchOffsetConstellationTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga26bbe3d85d828e2736c31825d2b1a436.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga26bbe3d85d828e2736c31825d2b1a436.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset constellation trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchOffsetConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle offsetConstellationTrace[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescr

### RFmxDemod_DDemodFetchOffsetConstellationTrace

Fetches the offset constellation trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchOffsetConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle offsetConstellationTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| offsetConstellationTrace | [out] | NIComplexSingle[] | This parameter returns the offset constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga2b4fdba1ea86d077c5c85189eb085c9b.html language=enus -->
## TOPIC 00141: RFmxDemod_DDemodFetchMeasurementWaveform

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga2b4fdba1ea86d077c5c85189eb085c9b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga2b4fdba1ea86d077c5c85189eb085c9b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement waveform. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMeasurementWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle measurementWaveform[], int32 arraySize, int32 *actualArraySize, int32 *samplesPerSymb

### RFmxDemod_DDemodFetchMeasurementWaveform

Fetches the measurement waveform.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMeasurementWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle measurementWaveform[], int32 arraySize, int32 *actualArraySize, int32 *samplesPerSymbol, float64 *symbolRate)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start sample index. |
| dx | [out] | float64 * | This parameter returns the spacing between samples normalized to samples per symbol. |
| measurementWaveform | [out] | NIComplexSingle[] | This parameter returns the measured samples. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |
| samplesPerSymbol | [out] | int32 * | This parameter returns the samples per symbol. |
| symbolRate | [out] | float64 * | This parameter returns the symbol rate in Hz.The default value is 100 kHz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga32d073f971c42f974477867ae7cf51ba.html language=enus -->
## TOPIC 00142: RFmxDemod_DDemodFetchReferenceWaveformSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga32d073f971c42f974477867ae7cf51ba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga32d073f971c42f974477867ae7cf51ba.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform. Syntaxint32 __stdcall RFmxDemod_DDemodFetchReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize, int32 *actualArraySize)

### RFmxDemod_DDemodFetchReferenceWaveformSplit

Fetches the reference waveform.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start sample index. |
| dx | [out] | float64 * | This parameter returns the spacing between samples normalized to samples per symbol. |
| referenceWaveformI | [out] | float32[] | This parameter Returns the real part of reference samples. |
| referenceWaveformQ | [out] | float32[] | This parameter Returns the imaginary part of reference samples. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga33e76fe33bee4fa8d34e374482bb7eb4.html language=enus -->
## TOPIC 00143: RFmxDemod_DDemodFetchMeanRhoFactor

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga33e76fe33bee4fa8d34e374482bb7eb4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga33e76fe33bee4fa8d34e374482bb7eb4.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the correlation of the measurement waveform and the reference waveform. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMeanRhoFactor(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRhoFactor)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmx

### RFmxDemod_DDemodFetchMeanRhoFactor

Fetches the correlation of the measurement waveform and the reference waveform.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMeanRhoFactor(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRhoFactor)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanRhoFactor | [out] | float64 * | This parameter returns the correlation of the measurement waveform and the reference waveform. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga3d2bb5cdfabd9bff85910d083dbb3d77.html language=enus -->
## TOPIC 00144: RFmxDemod_DDemodFetchPhaseError

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga3d2bb5cdfabd9bff85910d083dbb3d77.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga3d2bb5cdfabd9bff85910d083dbb3d77.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error measurements. Syntaxint32 __stdcall RFmxDemod_DDemodFetchPhaseError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanPhaseError, float64 *maximumPhaseError)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxDemod_DDemodFetchPhaseError

Fetches the phase error measurements.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchPhaseError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanPhaseError, float64 *maximumPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanPhaseError | [out] | float64 * | This parameter returns the mean of the phase error. |
| maximumPhaseError | [out] | float64 * | This parameter returns the maximum of the phase error. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga3e11c7b2e1e26ec9f243c22e09b07c0c.html language=enus -->
## TOPIC 00145: RFmxDemod_DDemodFetchMagnitudeError

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga3e11c7b2e1e26ec9f243c22e09b07c0c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga3e11c7b2e1e26ec9f243c22e09b07c0c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error measurements. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMagnitudeError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanMagnitudeError, float64 *maximumMagnitudeError)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmx

### RFmxDemod_DDemodFetchMagnitudeError

Fetches the magnitude error measurements.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMagnitudeError(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanMagnitudeError, float64 *maximumMagnitudeError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanMagnitudeError | [out] | float64 * | This parameter returns the mean of the magnitude error measured per acquisition. |
| maximumMagnitudeError | [out] | float64 * | This parameter returns the maximum of the magnitude error measured per acquisition. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga41fffee72c441e46b775ec671e4dcccb.html language=enus -->
## TOPIC 00146: RFmxDemod_DDemodFetchEVM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga41fffee72c441e46b775ec671e4dcccb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga41fffee72c441e46b775ec671e4dcccb.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM measurements. Syntaxint32 __stdcall RFmxDemod_DDemodFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSEVM, float64 *maximumRMSEVM, float64 *meanModulationErrorRatio, float64 *maximumPeakEVM, float64 *meanPeakEVM)ParametersNameDirecti

### RFmxDemod_DDemodFetchEVM

Fetches the EVM measurements.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSEVM, float64 *maximumRMSEVM, float64 *meanModulationErrorRatio, float64 *maximumPeakEVM, float64 *meanPeakEVM)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanRMSEVM | [out] | float64 * | This parameter returns the mean of the RMS EVM, as a percentage, measured per acquisition. |
| maximumRMSEVM | [out] | float64 * | This parameter returns the maximum of the RMS EVM, as a percentage, measured per acquisition. |
| meanModulationErrorRatio | [out] | float64 * | This parameter returns the modulation error ratio, in dB. |
| maximumPeakEVM | [out] | float64 * | This parameter returns the maximum of the peak EVM measured per acquisition. |
| meanPeakEVM | [out] | float64 * | This parameter returns the mean of the peak EVM measured per acquisition. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga50d52d9927ed2ecbb3ae40d58071f35f.html language=enus -->
## TOPIC 00147: RFmxDemod_DDemodFetchFSKResults

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga50d52d9927ed2ecbb3ae40d58071f35f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga50d52d9927ed2ecbb3ae40d58071f35f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches frequency-shift keying (FSK) results. Syntaxint32 __stdcall RFmxDemod_DDemodFetchFSKResults(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanFskDeviation, float64 *meanRMSFskError, float64 *maximumPeakFskError)ParametersNameDirectionTypeDescriptioninst

### RFmxDemod_DDemodFetchFSKResults

Fetches frequency-shift keying (FSK) results.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchFSKResults(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanFskDeviation, float64 *meanRMSFskError, float64 *maximumPeakFskError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanFskDeviation | [out] | float64 * | This parameter returns the measured FSK deviation, in Hz. |
| meanRMSFskError | [out] | float64 * | This parameter returns the mean of the RMS frequency error, in Hz, of the FSK symbols measured per acquisition. |
| maximumPeakFskError | [out] | float64 * | This parameter returns the maximum of peak frequency error of the FSK symbols measured per acquisition. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga57e60453bb5b8c83741a23f8f906180f.html language=enus -->
## TOPIC 00148: RFmxDemod_DDemodFetchSyncFound

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga57e60453bb5b8c83741a23f8f906180f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga57e60453bb5b8c83741a23f8f906180f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether synchronization bits were found in the demodulated symbol. Syntaxint32 __stdcall RFmxDemod_DDemodFetchSyncFound(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *syncFound)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleTh

### RFmxDemod_DDemodFetchSyncFound

Indicates whether synchronization bits were found in the demodulated symbol.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchSyncFound(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *syncFound)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| syncFound | [out] | int32 * | This parameter returns TRUE if the synchronization bits was found in the demodulated signal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga589f82b483f4ed80b2c797c5e4cf5af7.html language=enus -->
## TOPIC 00149: RFmxDemod_DDemodFetchReferenceWaveform

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga589f82b483f4ed80b2c797c5e4cf5af7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga589f82b483f4ed80b2c797c5e4cf5af7.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform. Syntaxint32 __stdcall RFmxDemod_DDemodFetchReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle referenceWaveform[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeD

### RFmxDemod_DDemodFetchReferenceWaveform

Fetches the reference waveform.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle referenceWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start sample index. |
| dx | [out] | float64 * | This parameter returns the spacing between samples normalized to samples per symbol. |
| referenceWaveform | [out] | NIComplexSingle[] | This parameter returns the reference samples. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga5df3a46408db3b57fd74911fe7fd49b2.html language=enus -->
## TOPIC 00150: RFmxDemod_DDemodFetchOffsetEVMTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga5df3a46408db3b57fd74911fe7fd49b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga5df3a46408db3b57fd74911fe7fd49b2.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset error vector magnitude (EVM) trace measured on OQPSK signal. Syntaxint32 __stdcall RFmxDemod_DDemodFetchOffsetEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 offsetEVM[], int32 arraySize, int32 *actualArraySize

### RFmxDemod_DDemodFetchOffsetEVMTrace

Fetches the offset error vector magnitude (EVM) trace measured on OQPSK signal.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchOffsetEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 offsetEVM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start symbol index. |
| dx | [out] | float64 * | This parameter returns the spacing between symbols normalized to symbol rate. |
| offsetEVM | [out] | float32[] | This parameter returns the offset EVM trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga5ee5775f2fb8d684225485beb1d65a3b.html language=enus -->
## TOPIC 00151: RFmxDemod_DDemodFetchCarrierMeasurement

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga5ee5775f2fb8d684225485beb1d65a3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga5ee5775f2fb8d684225485beb1d65a3b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the carrier measurement. Syntaxint32 __stdcall RFmxDemod_DDemodFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanFrequencyOffset, float64 *meanFrequencyDrift, float64 *meanPhaseError)ParametersNameDirectionTypeDescriptioninstrume

### RFmxDemod_DDemodFetchCarrierMeasurement

Fetches the carrier measurement.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanFrequencyOffset, float64 *meanFrequencyDrift, float64 *meanPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanFrequencyOffset | [out] | float64 * | This parameter returns the mean of the measured carrier frequency offset, in Hz. |
| meanFrequencyDrift | [out] | float64 * | This parameter returns the mean of the measured carrier frequency drift, in Hz. |
| meanPhaseError | [out] | float64 * | This parameter returns the mean of the measured phase offset, in degrees, from the transmitted carrier phase. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga623027b51baa0be712903142c2b5f084.html language=enus -->
## TOPIC 00152: RFmxDemod_DDemodFetchConstellationTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga623027b51baa0be712903142c2b5f084.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga623027b51baa0be712903142c2b5f084.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellationTrace[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHan

### RFmxDemod_DDemodFetchConstellationTrace

Fetches the constellation trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellationTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| constellationTrace | [out] | NIComplexSingle[] | This parameter returns the constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga66008617dac0f7787d520c0afdf97f6e.html language=enus -->
## TOPIC 00153: RFmxDemod_DDemodFetchOffsetConstellationTraceSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga66008617dac0f7787d520c0afdf97f6e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga66008617dac0f7787d520c0afdf97f6e.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset constellation trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchOffsetConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 offsetConstellationTraceI[], float32 offsetConstellationTraceQ[], int32 arraySize, int32 *actualArraySi

### RFmxDemod_DDemodFetchOffsetConstellationTraceSplit

Fetches the offset constellation trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchOffsetConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 offsetConstellationTraceI[], float32 offsetConstellationTraceQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| offsetConstellationTraceI | [out] | float32[] | This parameter Returns the real part of offset constellation trace. |
| offsetConstellationTraceQ | [out] | float32[] | This parameter Returns the imaginary part of offset constellation trace. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga6c71bc4b682d32492e765cd6ef77f1d1.html language=enus -->
## TOPIC 00154: RFmxDemod_DDemodFetchMeanQuadratureSkew

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga6c71bc4b682d32492e765cd6ef77f1d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga6c71bc4b682d32492e765cd6ef77f1d1.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean quadrature skew. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMeanQuadratureSkew(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 *meanQuadratureSkew)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies

### RFmxDemod_DDemodFetchMeanQuadratureSkew

Fetches the mean quadrature skew.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMeanQuadratureSkew(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 *meanQuadratureSkew)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanQuadratureSkew | [out] | float32 * | This parameter returns a measure of I and Q components in the signal that are not perfectly orthogonal. Quadrature error can be either positive or negative, with the sign indicating the orientation of the error. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga6d1a82c615f87c97411523b148ed3bf0.html language=enus -->
## TOPIC 00155: RFmxDemod_DDemodFetchPhaseErrorTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga6d1a82c615f87c97411523b148ed3bf0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga6d1a82c615f87c97411523b148ed3bf0.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrume

### RFmxDemod_DDemodFetchPhaseErrorTrace

Fetches the phase error trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start symbol index. |
| dx | [out] | float64 * | This parameter returns the spacing between symbols normalized to symbol rate. |
| phaseError | [out] | float32[] | This parameter returns the phase error. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga756b8cc0ac0181257ce529bf1377235e.html language=enus -->
## TOPIC 00156: RFmxDemod_DDemodFetchEqualizerCoefficientsSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga756b8cc0ac0181257ce529bf1377235e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga756b8cc0ac0181257ce529bf1377235e.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the updated equalizer coefficients. Syntaxint32 __stdcall RFmxDemod_DDemodFetchEqualizerCoefficientsSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 equalizerCoefficientsI[], float32 equalizerCoefficientsQ[], int32 arraySize,

### RFmxDemod_DDemodFetchEqualizerCoefficientsSplit

Fetches the updated equalizer coefficients.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchEqualizerCoefficientsSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 equalizerCoefficientsI[], float32 equalizerCoefficientsQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter this parameter always returns 0. |
| dx | [out] | float64 * | This parameter returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerCoefficientsI | [out] | float32[] | This parameter Returns the real part of updated equalizer coefficients. |
| equalizerCoefficientsQ | [out] | float32[] | This parameter Returns the imaginary part of updated equalizer coefficients. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga98ce486ddc2387a9694203095b1e93a1.html language=enus -->
## TOPIC 00157: RFmxDemod_DDemodFetchMagnitudeErrorTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga98ce486ddc2387a9694203095b1e93a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga98ce486ddc2387a9694203095b1e93a1.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescrip

### RFmxDemod_DDemodFetchMagnitudeErrorTrace

Fetches the magnitude error trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start symbol index. |
| dx | [out] | float64 * | This parameter returns the spacing between symbols normalized to symbol rate. |
| magnitudeError | [out] | float32[] | This parameter returns the magnitude error. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1ga9fd0d956b26664f68b3fa5f755416eed.html language=enus -->
## TOPIC 00158: RFmxDemod_DDemodFetchOffsetEVM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1ga9fd0d956b26664f68b3fa5f755416eed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1ga9fd0d956b26664f68b3fa5f755416eed.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the offset error vector magnitude (EVM). Syntaxint32 __stdcall RFmxDemod_DDemodFetchOffsetEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSOffsetEVM, float64 *maximumRMSOffsetEVM, float64 *maximumPeakOffsetEVM, float64 *meanPeakOffsetEVM)Paramet

### RFmxDemod_DDemodFetchOffsetEVM

Fetches the offset error vector magnitude (EVM).

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchOffsetEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSOffsetEVM, float64 *maximumRMSOffsetEVM, float64 *maximumPeakOffsetEVM, float64 *meanPeakOffsetEVM)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanRMSOffsetEVM | [out] | float64 * | This parameter returns the mean of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
| maximumRMSOffsetEVM | [out] | float64 * | This parameter returns the mean of the RMS EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
| maximumPeakOffsetEVM | [out] | float64 * | This parameter returns the maximum of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |
| meanPeakOffsetEVM | [out] | float64 * | This parameter returns the mean of the peak EVM, measured per acquisition, after removing the offset between the I and Q channels of OQPSK demodulated signal. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1gaa49e7d9d54eb924fbe8a276592c5937b.html language=enus -->
## TOPIC 00159: RFmxDemod_DDemodFetchEqualizerCoefficients

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1gaa49e7d9d54eb924fbe8a276592c5937b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1gaa49e7d9d54eb924fbe8a276592c5937b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the updated equalizer coefficients. Syntaxint32 __stdcall RFmxDemod_DDemodFetchEqualizerCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle equalizerCoefficients[], int32 arraySize, int32 *actualArraySize)Paramete

### RFmxDemod_DDemodFetchEqualizerCoefficients

Fetches the updated equalizer coefficients.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchEqualizerCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle equalizerCoefficients[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter this parameter always returns 0. |
| dx | [out] | float64 * | This parameter returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerCoefficients | [out] | NIComplexSingle[] | This parameter returns the updated equalizer coefficients. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1gac05dbbd0667f727ee3d325c440df979d.html language=enus -->
## TOPIC 00160: RFmxDemod_DDemodFetchFSKDeviationTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1gac05dbbd0667f727ee3d325c440df979d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1gac05dbbd0667f727ee3d325c440df979d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency-shift keying (FSK) deviation trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchFSKDeviationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 fskError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirec

### RFmxDemod_DDemodFetchFSKDeviationTrace

Fetches the frequency-shift keying (FSK) deviation trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchFSKDeviationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 fskError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start symbol index. |
| dx | [out] | float64 * | This parameter returns the spacing between symbols normalized to symbol rate. |
| fskError | [out] | float32[] | This parameter returns the mean of the RMS frequency error of the FSK symbols measured per acquisition. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1gac49b8304fe6a7e9a832a8613b6922e1f.html language=enus -->
## TOPIC 00161: RFmxDemod_DDemodFetchMeanAmplitudeDroop

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1gac49b8304fe6a7e9a832a8613b6922e1f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1gac49b8304fe6a7e9a832a8613b6922e1f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean amplitude droop per symbol. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMeanAmplitudeDroop(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanAmplitudeDroop)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter

### RFmxDemod_DDemodFetchMeanAmplitudeDroop

Fetches the mean amplitude droop per symbol.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMeanAmplitudeDroop(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanAmplitudeDroop)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanAmplitudeDroop | [out] | float64 * | This parameter returns the mean amplitude droop per symbol. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1gac54ec0ddaf5910c683bf18afefb388da.html language=enus -->
## TOPIC 00162: RFmxDemod_DDemodFetchMeasurementWaveformSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1gac54ec0ddaf5910c683bf18afefb388da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1gac54ec0ddaf5910c683bf18afefb388da.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement waveform. Syntaxint32 __stdcall RFmxDemod_DDemodFetchMeasurementWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 measurementWaveformI[], float32 measurementWaveformQ[], int32 arraySize, int32 *actualAr

### RFmxDemod_DDemodFetchMeasurementWaveformSplit

Fetches the measurement waveform.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchMeasurementWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 measurementWaveformI[], float32 measurementWaveformQ[], int32 arraySize, int32 *actualArraySize, int32 *samplesPerSymbol, float64 *symbolRate)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start sample index. |
| dx | [out] | float64 * | This parameter returns the spacing between samples normalized to samples per symbol. |
| measurementWaveformI | [out] | float32[] | This parameter Returns the real part of measured samples. |
| measurementWaveformQ | [out] | float32[] | This parameter Returns the imaginary part of measured samples. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |
| samplesPerSymbol | [out] | int32 * | This parameter returns the samples per symbol. |
| symbolRate | [out] | float64 * | This parameter returns the symbol rate in Hz.The default value is 100 kHz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__fetch__d_1gaf3d54720da3f65c13a1bad84b7898255.html language=enus -->
## TOPIC 00163: RFmxDemod_DDemodFetchEVMTrace

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__fetch__d_1gaf3d54720da3f65c13a1bad84b7898255.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__fetch__d_1gaf3d54720da3f65c13a1bad84b7898255.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM trace. Syntaxint32 __stdcall RFmxDemod_DDemodFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInst

### RFmxDemod_DDemodFetchEVMTrace

Fetches the EVM trace.

#### Syntax

int32 __stdcall RFmxDemod_DDemodFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| x0 | [out] | float64 * | This parameter returns the start symbol index. |
| dx | [out] | float64 * | This parameter returns the spacing between symbols normalized to symbol rate. |
| evm | [out] | float32[] | This parameter returns the EVM measured per symbol. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

D

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__read.html language=enus -->
## TOPIC 00164: Read

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__read.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__read.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_ADemodReadAMConfigures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results. RFmxDemod_ADemodReadFMConfigures hardware for acquisition, performs measurement on acquired data, and returns the FM measure

### Read

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_ADemodReadAM | Configures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results. |
| RFmxDemod_ADemodReadFM | Configures hardware for acquisition, performs measurement on acquired data, and returns the FM measurement results. |
| RFmxDemod_ADemodReadPM | Configures hardware for acquisition, performs measurement on acquired data, and returns the PM measurement results. |
| RFmxDemod_DDemodRead | Configures hardware for acquisition, performs measurement on acquired data for modulation type configured using the RFmxDemod_DDemodCfgModulationType function, and returns the frequency offset, EVM, and MER results. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__read_1ga10d0b6c60bb151753a64a277569c8381.html language=enus -->
## TOPIC 00165: RFmxDemod_DDemodRead

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__read_1ga10d0b6c60bb151753a64a277569c8381.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__read_1ga10d0b6c60bb151753a64a277569c8381.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data for modulation type configured using the RFmxDemod_DDemodCfgModulationType function, and returns the frequency offset, EVM, and MER results. Syntaxint32 __stdcall RFmxDemod_DDemodRead(niRFmxInstrHandle instrumentHandle, char

### RFmxDemod_DDemodRead

Configures hardware for acquisition, performs measurement on acquired data for modulation type configured using the [RFmxDemod_DDemodCfgModulationType](group____root__ni_r_fmx_demod__functions__configuration__dmnu_1ga47d7b5a09bedd3871143d8933378758f.html) function, and returns the frequency offset, EVM, and MER results.

#### Syntax

int32 __stdcall RFmxDemod_DDemodRead(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanFrequencyOffset, float64 *meanRMSEVM, float64 *maximumPeakEVM, float64 *meanModulationErrorRatio)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanFrequencyOffset | [out] | float64 * | This parameter returns the mean of the measured carrier frequency offset, in Hz. |
| meanRMSEVM | [out] | float64 * | This parameter returns the mean of the RMS EVM measured per acquisition. |
| maximumPeakEVM | [out] | float64 * | This parameter returns the maximum of the peak EVM measured per acquisition. |
| meanModulationErrorRatio | [out] | float64 * | This parameter returns the modulation error ratio, in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__read_1ga4ddaa4b9925d7f5d02df259c8e080600.html language=enus -->
## TOPIC 00166: RFmxDemod_ADemodReadAM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__read_1ga4ddaa4b9925d7f5d02df259c8e080600.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__read_1ga4ddaa4b9925d7f5d02df259c8e080600.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results. Syntaxint32 __stdcall RFmxDemod_ADemodReadAM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanModulationDepth, float64 *meanCarrierPower)Paramet

### RFmxDemod_ADemodReadAM

Configures hardware for acquisition, performs measurement on acquired data, and returns the AM measurement results.

#### Syntax

int32 __stdcall RFmxDemod_ADemodReadAM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanModulationDepth, float64 *meanCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanModulationDepth | [out] | float64 * | This parameter returns the mean amplitude variation, as a percentage, around the unmodulated carrier amplitude. If the carrier is suppressed, the amplitude variation of the modulating signal is returned. |
| meanCarrierPower | [out] | float64 * | This parameter returns the mean of the measured carrier power, in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__read_1ga8c66ef73aed3c43b4b8955d70126dc9c.html language=enus -->
## TOPIC 00167: RFmxDemod_ADemodReadPM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__read_1ga8c66ef73aed3c43b4b8955d70126dc9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__read_1ga8c66ef73aed3c43b4b8955d70126dc9c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the PM measurement results. Syntaxint32 __stdcall RFmxDemod_ADemodReadPM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanCarrierFrequencyError)Para

### RFmxDemod_ADemodReadPM

Configures hardware for acquisition, performs measurement on acquired data, and returns the PM measurement results.

#### Syntax

int32 __stdcall RFmxDemod_ADemodReadPM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanCarrierFrequencyError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanDeviation | [out] | float64 * | This parameter returns the mean phase deviation, in degrees, of a phase modulated signal. |
| meanCarrierFrequencyError | [out] | float64 * | This parameter returns the mean of the measured carrier frequency error, in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__read_1gabb80c594e9221a0deb61b3af4ec4f7d3.html language=enus -->
## TOPIC 00168: RFmxDemod_ADemodReadFM

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__read_1gabb80c594e9221a0deb61b3af4ec4f7d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__read_1gabb80c594e9221a0deb61b3af4ec4f7d3.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures hardware for acquisition, performs measurement on acquired data, and returns the FM measurement results. Syntaxint32 __stdcall RFmxDemod_ADemodReadFM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanCarrierFrequencyError)Para

### RFmxDemod_ADemodReadFM

Configures hardware for acquisition, performs measurement on acquired data, and returns the FM measurement results.

#### Syntax

int32 __stdcall RFmxDemod_ADemodReadFM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanDeviation, float64 *meanCarrierFrequencyError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |
| meanDeviation | [out] | float64 * | This parameter returns the mean frequency deviation, in Hz, around the nominal frequency of the FM carrier. |
| meanCarrierFrequencyError | [out] | float64 * | This parameter returns the mean of the measured carrier frequency error, in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Read

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__select__measurement.html language=enus -->
## TOPIC 00169: Select Measurement

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__select__measurement.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__select__measurement_1ga28a89201291239cbb9f66b23401c4a22.html language=enus -->
## TOPIC 00170: RFmxDemod_SelectMeasurements

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__select__measurement_1ga28a89201291239cbb9f66b23401c4a22.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__select__measurement_1ga28a89201291239cbb9f66b23401c4a22.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxDemod_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescrip

### RFmxDemod_SelectMeasurements

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxDemod_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| measurements | [in] | uInt32 | This parameter specifies an array of measurements to perform. You can specify the following measurements.Name (Value)DescriptionADemod (0)Enables analog demodulation measurements.DDemod (1)Enables digital demodulation measurements. |
| Name (Value) | Description |  |  |
| ADemod (0) | Enables analog demodulation measurements. |  |  |
| DDemod (1) | Enables digital demodulation measurements. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all the traces for the selected measurements. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00171: Set and Get Attributes

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes.html
- document_id: `rfmxdemod-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00172: Get Attributes

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxDemod_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffe

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxDemod_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxDemod_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxDemod_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxDemod_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxDemod_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxDemod_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxDemod_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxDemod_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxDemod_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxDemod_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga0c73b119eb6be7a292d0df16751aec71.html language=enus -->
## TOPIC 00173: RFmxDemod_GetAttributeU8

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga0c73b119eb6be7a292d0df16751aec71.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga0c73b119eb6be7a292d0df16751aec71.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxDemod_GetAttributeU8

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga0e9ae77e613619a1fe6ca76a1ed77a35.html language=enus -->
## TOPIC 00174: RFmxDemod_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga0e9ae77e613619a1fe6ca76a1ed77a35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga0e9ae77e613619a1fe6ca76a1ed77a35.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxDemod_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga100e46f9005e473e11ba5a18dd439469.html language=enus -->
## TOPIC 00175: RFmxDemod_GetAttributeI64Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga100e46f9005e473e11ba5a18dd439469.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga100e46f9005e473e11ba5a18dd439469.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxDemod_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga24c1b639362728006cc69d5860f8771a.html language=enus -->
## TOPIC 00176: RFmxDemod_GetAttributeU32

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga24c1b639362728006cc69d5860f8771a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga24c1b639362728006cc69d5860f8771a.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxDemod_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga3c1ea740e4e165eedff5baa9e8630f02.html language=enus -->
## TOPIC 00177: RFmxDemod_GetAttributeF32Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga3c1ea740e4e165eedff5baa9e8630f02.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga3c1ea740e4e165eedff5baa9e8630f02.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxDemod_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga3dfac16a309e9d6c607b2c8932242a27.html language=enus -->
## TOPIC 00178: RFmxDemod_GetAttributeI16

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga3dfac16a309e9d6c607b2c8932242a27.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga3dfac16a309e9d6c607b2c8932242a27.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxDemod_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga42d2cd1b5982eb0682d495186e0599c8.html language=enus -->
## TOPIC 00179: RFmxDemod_GetAttributeU8Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga42d2cd1b5982eb0682d495186e0599c8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga42d2cd1b5982eb0682d495186e0599c8.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxDemod_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga59c75a22faa77d2bdd578d21b5e5aacc.html language=enus -->
## TOPIC 00180: RFmxDemod_GetAttributeI64

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga59c75a22faa77d2bdd578d21b5e5aacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga59c75a22faa77d2bdd578d21b5e5aacc.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxDemod_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga6570d0ead02b7be21848dd29f46c8cd6.html language=enus -->
## TOPIC 00181: RFmxDemod_GetAttributeF64Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga6570d0ead02b7be21848dd29f46c8cd6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga6570d0ead02b7be21848dd29f46c8cd6.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxDemod_GetAttributeF64Array

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga6da58fdfa6f76eb9836efbce0e080b28.html language=enus -->
## TOPIC 00182: RFmxDemod_GetAttributeI8

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga6da58fdfa6f76eb9836efbce0e080b28.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga6da58fdfa6f76eb9836efbce0e080b28.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxDemod_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga8bb524a989e1e69b571dbbb954b69339.html language=enus -->
## TOPIC 00183: RFmxDemod_GetAttributeF64

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga8bb524a989e1e69b571dbbb954b69339.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga8bb524a989e1e69b571dbbb954b69339.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxDemod_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga973125b90f9ff7287e1f070f2f18b087.html language=enus -->
## TOPIC 00184: RFmxDemod_GetAttributeU32Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga973125b90f9ff7287e1f070f2f18b087.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga973125b90f9ff7287e1f070f2f18b087.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxDemod_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga97a7906db8a89e4f03c6a9f871af976c.html language=enus -->
## TOPIC 00185: RFmxDemod_GetAttributeI32

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga97a7906db8a89e4f03c6a9f871af976c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1ga97a7906db8a89e4f03c6a9f871af976c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxDemod_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaa84b693dea4ddc009419a9aa0cd99579.html language=enus -->
## TOPIC 00186: RFmxDemod_GetAttributeF32

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaa84b693dea4ddc009419a9aa0cd99579.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaa84b693dea4ddc009419a9aa0cd99579.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxDemod_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaba628ef1eb2a0294627924ecb74480b1.html language=enus -->
## TOPIC 00187: RFmxDemod_GetAttributeI8Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaba628ef1eb2a0294627924ecb74480b1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaba628ef1eb2a0294627924ecb74480b1.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxDemod_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacbaa0ad64979a78adcae7145a1b7f07f.html language=enus -->
## TOPIC 00188: RFmxDemod_GetAttributeString

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacbaa0ad64979a78adcae7145a1b7f07f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacbaa0ad64979a78adcae7145a1b7f07f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxDemod_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacd0821dca98a5acd620c25b75d944874.html language=enus -->
## TOPIC 00189: RFmxDemod_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacd0821dca98a5acd620c25b75d944874.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacd0821dca98a5acd620c25b75d944874.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxDemod_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacd62d1e18396a6cb320716615cc2d054.html language=enus -->
## TOPIC 00190: RFmxDemod_GetAttributeU64Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacd62d1e18396a6cb320716615cc2d054.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gacd62d1e18396a6cb320716615cc2d054.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxDemod_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gad55fc4f63f348f21e8e02565a080cf39.html language=enus -->
## TOPIC 00191: RFmxDemod_GetAttributeU16

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gad55fc4f63f348f21e8e02565a080cf39.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gad55fc4f63f348f21e8e02565a080cf39.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxDemod_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxDemod_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaf00d5dc9194c75128c4a35f187e46e03.html language=enus -->
## TOPIC 00192: RFmxDemod_GetAttributeI32Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaf00d5dc9194c75128c4a35f187e46e03.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__get__attributes_1gaf00d5dc9194c75128c4a35f187e46e03.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxDemod_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxDemod_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00193: Set Attributes

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxDemod_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxDemod_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxDemod_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxDemod_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxDemod_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxDemod_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxDemod_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxDemod_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxDemod_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxDemod_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxDemod_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxDemod_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga1d9cb923ab9236d0e9927d4d593b64d9.html language=enus -->
## TOPIC 00194: RFmxDemod_SetAttributeU8

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga1d9cb923ab9236d0e9927d4d593b64d9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga1d9cb923ab9236d0e9927d4d593b64d9.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFm

### RFmxDemod_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga2510fccb5786e2b22d3c818e0f35f7ef.html language=enus -->
## TOPIC 00195: RFmxDemod_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga2510fccb5786e2b22d3c818e0f35f7ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga2510fccb5786e2b22d3c818e0f35f7ef.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxDemod_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga2f77bef2e832aed4038c8359cf2f9b79.html language=enus -->
## TOPIC 00196: RFmxDemod_SetAttributeU32Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga2f77bef2e832aed4038c8359cf2f9b79.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga2f77bef2e832aed4038c8359cf2f9b79.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxDemod_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga3565bc79f76485992aa4b218befcee89.html language=enus -->
## TOPIC 00197: RFmxDemod_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga3565bc79f76485992aa4b218befcee89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga3565bc79f76485992aa4b218befcee89.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxDemod_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga3a06318426d02252041efe8e6d9bdbdf.html language=enus -->
## TOPIC 00198: RFmxDemod_SetAttributeF32

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga3a06318426d02252041efe8e6d9bdbdf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga3a06318426d02252041efe8e6d9bdbdf.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentif

### RFmxDemod_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga49a70f6a679d32fb9053d6ea6823f44f.html language=enus -->
## TOPIC 00199: RFmxDemod_SetAttributeI8

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga49a70f6a679d32fb9053d6ea6823f44f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga49a70f6a679d32fb9053d6ea6823f44f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxDemod_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga5f6af47ef214ca243131ae34a68e763f.html language=enus -->
## TOPIC 00200: RFmxDemod_SetAttributeI32

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga5f6af47ef214ca243131ae34a68e763f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga5f6af47ef214ca243131ae34a68e763f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxDemod_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga66066710ec338c6493bd0e00b52dd843.html language=enus -->
## TOPIC 00201: RFmxDemod_SetAttributeU32

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga66066710ec338c6493bd0e00b52dd843.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga66066710ec338c6493bd0e00b52dd843.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxDemod_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga6897c946c72a409598227729d9cd8c9c.html language=enus -->
## TOPIC 00202: RFmxDemod_SetAttributeF64Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga6897c946c72a409598227729d9cd8c9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga6897c946c72a409598227729d9cd8c9c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, ch

### RFmxDemod_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga73d602c3061b43d0c0a204400e224d76.html language=enus -->
## TOPIC 00203: RFmxDemod_SetAttributeF32Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga73d602c3061b43d0c0a204400e224d76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga73d602c3061b43d0c0a204400e224d76.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, ch

### RFmxDemod_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga764de252243c5606628fef78d9954cff.html language=enus -->
## TOPIC 00204: RFmxDemod_SetAttributeString

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga764de252243c5606628fef78d9954cff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga764de252243c5606628fef78d9954cff.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can

### RFmxDemod_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga89508d6b20467875fb032aa984b29686.html language=enus -->
## TOPIC 00205: RFmxDemod_SetAttributeU64Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga89508d6b20467875fb032aa984b29686.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga89508d6b20467875fb032aa984b29686.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxDemod_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga979e5ccd66f1019e1b03d6efb49113eb.html language=enus -->
## TOPIC 00206: RFmxDemod_SetAttributeU16

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga979e5ccd66f1019e1b03d6efb49113eb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga979e5ccd66f1019e1b03d6efb49113eb.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxDemod_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga9fe8485817ab8ae5e5a6ac623c11587e.html language=enus -->
## TOPIC 00207: RFmxDemod_SetAttributeI32Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga9fe8485817ab8ae5e5a6ac623c11587e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1ga9fe8485817ab8ae5e5a6ac623c11587e.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxDemod_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaa7696150c5d00472d57deeb958bf4525.html language=enus -->
## TOPIC 00208: RFmxDemod_SetAttributeI64Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaa7696150c5d00472d57deeb958bf4525.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaa7696150c5d00472d57deeb958bf4525.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxDemod_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaab324fec326673fac95fb107691695a3.html language=enus -->
## TOPIC 00209: RFmxDemod_SetAttributeI64

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaab324fec326673fac95fb107691695a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaab324fec326673fac95fb107691695a3.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxDemod_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaaed425b8713edbd52777762f0aa864c2.html language=enus -->
## TOPIC 00210: RFmxDemod_SetAttributeU8Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaaed425b8713edbd52777762f0aa864c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gaaed425b8713edbd52777762f0aa864c2.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char select

### RFmxDemod_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gab581d569fd0eea483ba1cf18e7ab302c.html language=enus -->
## TOPIC 00211: RFmxDemod_SetAttributeF64

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gab581d569fd0eea483ba1cf18e7ab302c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gab581d569fd0eea483ba1cf18e7ab302c.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentif

### RFmxDemod_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gab77b2560ec2d3ea638e5fa755db40d73.html language=enus -->
## TOPIC 00212: RFmxDemod_SetAttributeI8Array

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gab77b2560ec2d3ea638e5fa755db40d73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gab77b2560ec2d3ea638e5fa755db40d73.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxDemod_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[]

### RFmxDemod_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gae5ca2eb5de6149dda421109b5d58a8c1.html language=enus -->
## TOPIC 00213: RFmxDemod_SetAttributeI16

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gae5ca2eb5de6149dda421109b5d58a8c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__set__and__get__attributes__set__attributes_1gae5ca2eb5de6149dda421109b5d58a8c1.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxDemod_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxDemod_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxDemod_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility.html language=enus -->
## TOPIC 00214: Utility

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxDemod_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxDemod_CommitCommits settings to the h

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxDemod_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxDemod_Commit | Commits settings to the hardware. Calling this function is optional. RFmxDemod commits settings to the hardware when you call the RFmxDemod_Initiate function or any of the measurement Read functions. |
| RFmxDemod_DDemodGetEqualizerInitialCoefficients | Gets the initial equalizer coefficients used by the digital demodulation measurement. |
| RFmxDemod_DDemodGetEqualizerInitialCoefficientsSplit | Gets the initial equalizer coefficients used by the digital demodulation measurement. |
| RFmxDemod_DDemodGetSymbolMap | Gets the symbol map that is used for digital demodulation measurements. Call this function after calling RFmxDemod_Commit function. |
| RFmxDemod_DDemodGetSymbolMapSplit | Gets the symbol map that is used for digital demodulation measurements. Call this function after calling RFmxDemod_Commit function. |
| RFmxDemod_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxDemod_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxDemod_ResetToDefault | Resets a signal to the default values. |
| RFmxDemod_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxDemod_WaitForMeasurementComplete | Waits for the specified number for seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1ga2ae56bc61598a8c1294a7a414d199c04.html language=enus -->
## TOPIC 00215: RFmxDemod_DDemodGetEqualizerInitialCoefficients

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1ga2ae56bc61598a8c1294a7a414d199c04.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1ga2ae56bc61598a8c1294a7a414d199c04.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the initial equalizer coefficients used by the digital demodulation measurement. Syntaxint32 __stdcall RFmxDemod_DDemodGetEqualizerInitialCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, NIComplexSingle equalizerInitialCoefficients[], int32 array

### RFmxDemod_DDemodGetEqualizerInitialCoefficients

Gets the initial equalizer coefficients used by the digital demodulation measurement.

#### Syntax

int32 __stdcall RFmxDemod_DDemodGetEqualizerInitialCoefficients(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, NIComplexSingle equalizerInitialCoefficients[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| x0 | [out] | float64 * | This parameter this parameter always returns 0. |
| dx | [out] | float64 * | This parameter returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerInitialCoefficients | [out] | NIComplexSingle[] | This parameter returns the filter coefficients used as the equalizer initial coefficients. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1ga2d8fee610a069e4a3c541eb20c9c8acd.html language=enus -->
## TOPIC 00216: RFmxDemod_DDemodGetEqualizerInitialCoefficientsSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1ga2d8fee610a069e4a3c541eb20c9c8acd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1ga2d8fee610a069e4a3c541eb20c9c8acd.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the initial equalizer coefficients used by the digital demodulation measurement. Syntaxint32 __stdcall RFmxDemod_DDemodGetEqualizerInitialCoefficientsSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, float32 equalizerInitialCoefficientsI[], float32 equal

### RFmxDemod_DDemodGetEqualizerInitialCoefficientsSplit

Gets the initial equalizer coefficients used by the digital demodulation measurement.

#### Syntax

int32 __stdcall RFmxDemod_DDemodGetEqualizerInitialCoefficientsSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 *x0, float64 *dx, float32 equalizerInitialCoefficientsI[], float32 equalizerInitialCoefficientsQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| x0 | [out] | float64 * | This parameter this parameter always returns 0. |
| dx | [out] | float64 * | This parameter returns the spacing between the coefficients as a fraction of the symbol spacing. For example, if four coefficients correspond to one symbol, the spacing is 1/4. |
| equalizerInitialCoefficientsI | [out] | float32[] | This parameter Returns the real part of filter coefficients used as the equalizer initial coefficients. |
| equalizerInitialCoefficientsQ | [out] | float32[] | This parameter Returns the imaginary part of filter coefficients used as the equalizer initial coefficients. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1ga360bf9712f506f879b38a3de6d90b82b.html language=enus -->
## TOPIC 00217: RFmxDemod_Commit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1ga360bf9712f506f879b38a3de6d90b82b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1ga360bf9712f506f879b38a3de6d90b82b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this function is optional. RFmxDemod commits settings to the hardware when you call the RFmxDemod_Initiate function or any of the measurement Read functions. Syntaxint32 __stdcall RFmxDemod_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])Par

### RFmxDemod_Commit

Commits settings to the hardware. Calling this function is optional. RFmxDemod commits settings to the hardware when you call the [RFmxDemod_Initiate](group____root__ni_r_fmx_demod__functions_1ga8778fe6471a507c439032371a04b08d7.html) function or any of the measurement Read functions.

#### Syntax

int32 __stdcall RFmxDemod_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1ga58b3f434aca0f64aa591bfbb09b36e1f.html language=enus -->
## TOPIC 00218: RFmxDemod_InitializeFromNIRFSASession

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1ga58b3f434aca0f64aa591bfbb09b36e1f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1ga58b3f434aca0f64aa591bfbb09b36e1f.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device

### RFmxDemod_InitializeFromNIRFSASession

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxDemod_InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle *handleOut)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| nirfsaSession | [in] | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| handleOut | [out] | niRFmxInstrHandle * | Returns an RFmx instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1ga627d4419b205017ceedb643200630009.html language=enus -->
## TOPIC 00219: RFmxDemod_DDemodGetSymbolMapSplit

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1ga627d4419b205017ceedb643200630009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1ga627d4419b205017ceedb643200630009.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbol map that is used for digital demodulation measurements. Call this function after calling RFmxDemod_Commit function. Syntaxint32 __stdcall RFmxDemod_DDemodGetSymbolMapSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float32 symbolMapI[], float32 symbolMapQ[], int32 arr

### RFmxDemod_DDemodGetSymbolMapSplit

Gets the symbol map that is used for digital demodulation measurements. Call this function after calling [RFmxDemod_Commit](group____root__ni_r_fmx_demod__functions__utility_1ga360bf9712f506f879b38a3de6d90b82b.html) function.

#### Syntax

int32 __stdcall RFmxDemod_DDemodGetSymbolMapSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float32 symbolMapI[], float32 symbolMapQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| symbolMapI | [out] | float32[] | This parameter Returns the real part of symbol map used for demodulation. |
| symbolMapQ | [out] | float32[] | This parameter Returns the imaginary part of symbol map used for demodulation. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1gaa85442d440552943967ef2815fcc1a1b.html language=enus -->
## TOPIC 00220: RFmxDemod_WaitForMeasurementComplete

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1gaa85442d440552943967ef2815fcc1a1b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1gaa85442d440552943967ef2815fcc1a1b.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. Syntaxint32 __stdcall RFmxDemod_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxDemod_WaitForMeasurementComplete

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

int32 __stdcall RFmxDemod_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. This value is expressed in seconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1gab8d6ba09229ffebc6338f86400057e27.html language=enus -->
## TOPIC 00221: RFmxDemod_WaitForAcquisitionComplete

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1gab8d6ba09229ffebc6338f86400057e27.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1gab8d6ba09229ffebc6338f86400057e27.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxDemod_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instrum

### RFmxDemod_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxDemod_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1gac75e1700e587faa24c8472ddbe34ee3e.html language=enus -->
## TOPIC 00222: RFmxDemod_CheckMeasurementStatus

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1gac75e1700e587faa24c8472ddbe34ee3e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1gac75e1700e587faa24c8472ddbe34ee3e.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxDemod_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxDemod_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxDemod_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *isDone)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| isDone | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1gadf2424b92dee99288e4c7622939b35f6.html language=enus -->
## TOPIC 00223: RFmxDemod_ResetToDefault

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1gadf2424b92dee99288e4c7622939b35f6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1gadf2424b92dee99288e4c7622939b35f6.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. Syntaxint32 __stdcall RFmxDemod_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. Instrument Handle In is obtaine

### RFmxDemod_ResetToDefault

Resets a signal to the default values.

#### Syntax

int32 __stdcall RFmxDemod_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1gaecb4f24b7f97209db4b07fbd214e40ea.html language=enus -->
## TOPIC 00224: RFmxDemod_DDemodGetSymbolMap

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1gaecb4f24b7f97209db4b07fbd214e40ea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1gaecb4f24b7f97209db4b07fbd214e40ea.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbol map that is used for digital demodulation measurements. Call this function after calling RFmxDemod_Commit function. Syntaxint32 __stdcall RFmxDemod_DDemodGetSymbolMap(niRFmxInstrHandle instrumentHandle, char selectorString[], NIComplexSingle symbolMap[], int32 arraySize, int32 *actua

### RFmxDemod_DDemodGetSymbolMap

Gets the symbol map that is used for digital demodulation measurements. Call this function after calling [RFmxDemod_Commit](group____root__ni_r_fmx_demod__functions__utility_1ga360bf9712f506f879b38a3de6d90b82b.html) function.

#### Syntax

int32 __stdcall RFmxDemod_DDemodGetSymbolMap(niRFmxInstrHandle instrumentHandle, char selectorString[], NIComplexSingle symbolMap[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter comprises of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:"""signal::sig1"You can use the RFmxDemod_BuildSignalString function to build the Selector String. |
| symbolMap | [out] | NIComplexSingle[] | This parameter returns the symbol map used for demodulation. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group____root__ni_r_fmx_demod__functions__utility_1gaf7cf2b3c06240b244bf7e898c57e353d.html language=enus -->
## TOPIC 00225: RFmxDemod_ResetAttribute

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group____root__ni_r_fmx_demod__functions__utility_1gaf7cf2b3c06240b244bf7e898c57e353d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_demod__functions__utility_1gaf7cf2b3c06240b244bf7e898c57e353d.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an attribute that you specify in the attributeID parameter to default values. Syntaxint32 __stdcall RFmxDemod_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the R

### RFmxDemod_ResetAttribute

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Syntax

int32 __stdcall RFmxDemod_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxDemod_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being reset. Refer to the Selector String (C or LabWindows/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxDemod_GetError](group____root__ni_r_fmx_demod__functions_1gadf0e1a20b680023cc199bba14171f29a.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxdemod-c-api-ref path=group__root__ni_r_fmx_demod.html language=enus -->
## TOPIC 00226: niRFmxDemod.h

- bundle_id: `rfmxdemod-c-api-ref`
- source_path: `group__root__ni_r_fmx_demod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxdemod-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_demod.html
- document_id: `rfmxdemod-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxDemod.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
