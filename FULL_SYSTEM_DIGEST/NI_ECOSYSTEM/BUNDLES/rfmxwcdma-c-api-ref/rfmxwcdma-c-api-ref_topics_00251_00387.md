# NI DOCUMENT BUNDLE: rfmxwcdma-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwcdma-c-api-ref start=251 end=387 -->
<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1gaba3e44dbcd3284f628e362582ca3a385.html language=enus -->
## TOPIC 00251: RFmxWCDMA_CHPCfgRBWFilter

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1gaba3e44dbcd3284f628e362582ca3a385.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1gaba3e44dbcd3284f628e362582ca3a385.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxWCDMA_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxWCDMA_CHPCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxWCDMA_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat.If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter.NameValueDescriptionRFMXWCDMA_VAL_CHP_RBW_AUTO_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute.RFMXWCDMA_VAL_CHP_RBW_AUTO_TRUE1 (0x1)The measurement computes the RBW. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CHP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXWCDMA_VAL_CHP_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False.This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 50 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is applied.RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)An RBW filter with a Gaussian response is applied.RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FLAT2 (0x2)An RBW filter with a flat response is applied. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is applied. |  |
| RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1gad0cc606785d7171edde55e1b7e830393.html language=enus -->
## TOPIC 00252: RFmxWCDMA_CHPCfgSweepTime

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1gad0cc606785d7171edde55e1b7e830393.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__chp_1gad0cc606785d7171edde55e1b7e830393.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval. Syntaxint32 __stdcall RFmxWCDMA_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx s

### RFmxWCDMA_CHPCfgSweepTime

Configures the sweep time interval.

#### Syntax

int32 __stdcall RFmxWCDMA_CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.NameValueDescriptionRFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL attribute.RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement uses a sweep time value of one slot duration. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |  |
| RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time value of one slot duration. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__frequency.html language=enus -->
## TOPIC 00253: Frequency

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__frequency.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_CfgFrequencyConfigures the RF center frequency. RFmxWCDMA_CfgFrequencyUARFCNConfigures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal. Attac

### Frequency

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_CfgFrequency | Configures the RF center frequency. |
| RFmxWCDMA_CfgFrequencyUARFCN | Configures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__frequency_1gab26f7821d93d8073dc9960529425a38e.html language=enus -->
## TOPIC 00254: RFmxWCDMA_CfgFrequencyUARFCN

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__frequency_1gab26f7821d93d8073dc9960529425a38e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__frequency_1gab26f7821d93d8073dc9960529425a38e.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal. Syntaxint32 __stdcall RFmxWCDMA_CfgFrequencyUARFCN(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection

### RFmxWCDMA_CfgFrequencyUARFCN

Configures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgFrequencyUARFCN(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 band, int32 uarfcn)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| linkDirection | [in] | int32 | This parameter specifies the link direction.NameValueDescriptionRFMXWCDMA_VAL_LINK_DIRECTION_DOWNLINK0 (0x0)The link is from the base transceiver station to the user equipment.RFMXWCDMA_VAL_LINK_DIRECTION_UPLINK1 (0x1)The link is from the user equipment to the base transceiver station. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_LINK_DIRECTION_DOWNLINK | 0 (0x0) | The link is from the base transceiver station to the user equipment. |  |
| RFMXWCDMA_VAL_LINK_DIRECTION_UPLINK | 1 (0x1) | The link is from the user equipment to the base transceiver station. |  |
| band | [in] | int32 | This parameter specifies the UMTS operation band. The default value is 1.Name (Value)Description1 (1)The terminal operates in UMTS Band I.2 (2)The terminal operates in UMTS Band II.3 (3)The terminal operates in UMTS Band III.4 (4)The terminal operates in UMTS Band IV.5 (5)The terminal operates in UMTS Band V.6 (6)The terminal operates in UMTS Band function.7 (7)The terminal operates in UMTS Band VII.8 (8)The terminal operates in UMTS Band VIII.9 (9)The terminal operates in UMTS Band IX.10 (10)The terminal operates in UMTS Band X.11 (11)The terminal operates in UMTS Band XI.12 (12)The terminal operates in UMTS Band XII.13 (13)The terminal operates in UMTS Band XIII.14 (14)The terminal operates in UMTS Band XIV.19 (19)The terminal operates in UMTS Band XIX.20 (20)The terminal operates in UMTS Band XX.21 (21)The terminal operates in UMTS Band XXI.22 (22)The terminal operates in UMTS Band XXII.25 (25)The terminal operates in UMTS Band XXV.26 (26)The terminal operates in UMTS Band XXVI. |
| Name (Value) | Description |  |  |
| 1 (1) | The terminal operates in UMTS Band I. |  |  |
| 2 (2) | The terminal operates in UMTS Band II. |  |  |
| 3 (3) | The terminal operates in UMTS Band III. |  |  |
| 4 (4) | The terminal operates in UMTS Band IV. |  |  |
| 5 (5) | The terminal operates in UMTS Band V. |  |  |
| 6 (6) | The terminal operates in UMTS Band function. |  |  |
| 7 (7) | The terminal operates in UMTS Band VII. |  |  |
| 8 (8) | The terminal operates in UMTS Band VIII. |  |  |
| 9 (9) | The terminal operates in UMTS Band IX. |  |  |
| 10 (10) | The terminal operates in UMTS Band X. |  |  |
| 11 (11) | The terminal operates in UMTS Band XI. |  |  |
| 12 (12) | The terminal operates in UMTS Band XII. |  |  |
| 13 (13) | The terminal operates in UMTS Band XIII. |  |  |
| 14 (14) | The terminal operates in UMTS Band XIV. |  |  |
| 19 (19) | The terminal operates in UMTS Band XIX. |  |  |
| 20 (20) | The terminal operates in UMTS Band XX. |  |  |
| 21 (21) | The terminal operates in UMTS Band XXI. |  |  |
| 22 (22) | The terminal operates in UMTS Band XXII. |  |  |
| 25 (25) | The terminal operates in UMTS Band XXV. |  |  |
| 26 (26) | The terminal operates in UMTS Band XXVI. |  |  |
| uarfcn | [in] | int32 | This parameter specifies the UTRA absolute radio frequency channel number (UARFCN).UARFCN has to be updated according to the band for the uplink, as defined by the general UARFCNs in Table 4.2: UTRA Absolute Radio Frequency Channel Number in the 3GPP TS 34.121-1 specification, version 11.5.0. Otherwise, UARFCN is coerced to the top or bottom UARFCN of the selected band, depending on which is nearer. The center frequency then corresponds to this coerced UARFCN as defined by carrier frequencies in Table 4.1: UARFCN definition (general) of the 3GPP TS 34.121-1 specification, version 11.5.0. The default value is 9,750, which corresponds to the center of the UMTS Band I. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc.html language=enus -->
## TOPIC 00255: ModAcc

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_ModAccCfgReferenceWaveformConfigures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This function is used only when you set the RFM

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_ModAccCfgReferenceWaveform | Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This function is used only when you set the RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute to Marker. |
| RFmxWCDMA_ModAccCfgReferenceWaveformSplit | Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This function is used only when you set the RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute to Marker. |
| RFmxWCDMA_ModAccCfgSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc_1ga7ee5f6bcfdd608f71736451547ba8ae3.html language=enus -->
## TOPIC 00256: RFmxWCDMA_ModAccCfgReferenceWaveformSplit

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc_1ga7ee5f6bcfdd608f71736451547ba8ae3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc_1ga7ee5f6bcfdd608f71736451547ba8ae3.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This function is used only when you set the RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute to Marker. Syntaxint32 _

### RFmxWCDMA_ModAccCfgReferenceWaveformSplit

Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This function is used only when you set the [RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga2cf66134d1373e4d337a7540d5390ae7.html) attribute to **Marker**.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccCfgReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| x0 | [in] | float64 | This parameter specifies the start time. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the sample duration. This value is expressed in seconds. |
| referenceWaveformI | [in] | float32[] | This parameter specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| referenceWaveformQ | [in] | float32[] | This parameter specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc_1gaf5091fa5c539c21f6efcf8c485ec90a4.html language=enus -->
## TOPIC 00257: RFmxWCDMA_ModAccCfgReferenceWaveform

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc_1gaf5091fa5c539c21f6efcf8c485ec90a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__modacc_1gaf5091fa5c539c21f6efcf8c485ec90a4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This function is used only when you set the RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE attribute to Marker. Syntaxint32 _

### RFmxWCDMA_ModAccCfgReferenceWaveform

Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This function is used only when you set the [RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE](group____root__ni_r_fmx_w_c_d_m_a__attributes__modacc_1ga2cf66134d1373e4d337a7540d5390ae7.html) attribute to **Marker**.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccCfgReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 x0, float64 dx, NIComplexSingle referenceWaveform[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| x0 | [in] | float64 | This parameter specifies the start time. This value is expressed in seconds. |
| dx | [in] | float64 | This parameter specifies the sample duration. This value is expressed in seconds. |
| referenceWaveform | [in] | NIComplexSingle[] | This parameter specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__obw_1ga157190cf883915a8d14e02208697eb59.html language=enus -->
## TOPIC 00258: RFmxWCDMA_OBWCfgRBWFilter

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__obw_1ga157190cf883915a8d14e02208697eb59.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__obw_1ga157190cf883915a8d14e02208697eb59.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxWCDMA_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxWCDMA_OBWCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxWCDMA_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW. The default value is True.This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat.If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter.NameValueDescriptionRFMXWCDMA_VAL_OBW_RBW_AUTO_FALSE0 (0x0)The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute.RFMXWCDMA_VAL_OBW_RBW_AUTO_TRUE1 (0x1)The measurement uses an RBW value of 30 kHz. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_OBW_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |  |
| RFMXWCDMA_VAL_OBW_RBW_AUTO_TRUE | 1 (0x1) | The measurement uses an RBW value of 30 kHz. |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False.This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 30 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.NameValueDescriptionRFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED0 (0x0)No RBW filtering is applied.RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN1 (0x1)An RBW filter with a Gaussian response is applied.RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FLAT2 (0x2)An RBW filter with a flat response is applied. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is applied. |  |
| RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |  |
| RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__qevm_1ga1faefd2799717ca44e853a0e64773aaa.html language=enus -->
## TOPIC 00259: RFmxWCDMA_QEVMCfgAveraging

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__qevm_1ga1faefd2799717ca44e853a0e64773aaa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__qevm_1ga1faefd2799717ca44e853a0e64773aaa.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the QEVM measurement. Syntaxint32 __stdcall RFmxWCDMA_QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies

### RFmxWCDMA_QEVMCfgAveraging

Configures averaging for the QEVM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the QEVM measurement. The default value is False.NameValueDescriptionRFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_TRUE1 (0x1)The QEVM measurement uses the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute as the number of acquisitions over which the QEVM measurement is averaged. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The QEVM measurement uses the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute as the number of acquisitions over which the QEVM measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True.The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__qevm_1ga4541f8cb9a4efe1881fd4255e71cfccb.html language=enus -->
## TOPIC 00260: RFmxWCDMA_QEVMCfgMeasurementLength

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__qevm_1ga4541f8cb9a4efe1881fd4255e71cfccb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__qevm_1ga4541f8cb9a4efe1881fd4255e71cfccb.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement length of the QEVM measurement. Syntaxint32 __stdcall RFmxWCDMA_QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies t

### RFmxWCDMA_QEVMCfgMeasurementLength

Configures the measurement length of the QEVM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the QEVM measurement. The value is expressed in chips.The default value is 2560. NI recommends that you set this attribute to n * 512, where the value of n can range from 1 to 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem.html language=enus -->
## TOPIC 00261: SEM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_SEMCfgAveragingConfigures averaging for the SEM measurement. RFmxWCDMA_SEMCfgSweepTimeConfigures the sweep time interval. AttachmentsNone

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_SEMCfgAveraging | Configures averaging for the SEM measurement. |
| RFmxWCDMA_SEMCfgSweepTime | Configures the sweep time interval. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem_1ga6ef4ecafea285d6b50ce1d7416ca547f.html language=enus -->
## TOPIC 00262: RFmxWCDMA_SEMCfgAveraging

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem_1ga6ef4ecafea285d6b50ce1d7416ca547f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem_1ga6ef4ecafea285d6b50ce1d7416ca547f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. Syntaxint32 __stdcall RFmxWCDMA_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis p

### RFmxWCDMA_SEMCfgAveraging

Configures averaging for the SEM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging of the spectrum for the measurement. The default value is False.NameValueDescriptionRFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_FALSE0 (0x0)The measurement is performed on a single acquisition.RFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_TRUE1 (0x1)The SEM measurement uses the value of the RFMXWCDMA_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |  |
| RFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_TRUE | 1 (0x1) | The SEM measurement uses the value of the RFMXWCDMA_ATTR_SEM_AVERAGING_COUNT attribute as the number of acquisitions over which the SEM measurement is averaged. |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS.NameValueDescriptionRFMXWCDMA_VAL_SEM_AVERAGING_TYPE_RMS0 (0x0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_LOG1 (0x1)The power spectrum is averaged in a logarithmic scale.RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_SCALAR2 (0x2)The square root of the power spectrum is averaged.RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MAX3 (0x3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MIN4 (0x4)The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |  |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |  |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MAX | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |
| RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MIN | 4 (0x4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem_1ga7a136abd20193a26bc062f93d138de83.html language=enus -->
## TOPIC 00263: RFmxWCDMA_SEMCfgSweepTime

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem_1ga7a136abd20193a26bc062f93d138de83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__sem_1ga7a136abd20193a26bc062f93d138de83.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval. Syntaxint32 __stdcall RFmxWCDMA_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx s

### RFmxWCDMA_SEMCfgSweepTime

Configures the sweep time interval.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.NameValueDescriptionRFMXWCDMA_VAL_SEM_SWEEP_TIME_AUTO_FALSE0 (0x0)The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_SEM_SWEEP_TIME_INTERVAL attribute.RFMXWCDMA_VAL_SEM_SWEEP_TIME_AUTO_TRUE1 (0x1)The measurement uses a sweep time value of one slot duration. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_SEM_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXWCDMA_ATTR_SEM_SWEEP_TIME_INTERVAL attribute. |  |
| RFMXWCDMA_VAL_SEM_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement uses a sweep time value of one slot duration. |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotphase.html language=enus -->
## TOPIC 00264: SlotPhase

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotphase.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_SlotPhaseCfgSynchronizationModeAndIntervalConfigures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement. AttachmentsNone

### SlotPhase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_SlotPhaseCfgSynchronizationModeAndInterval | Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotphase_1ga50f0929db2b2ce2e0b29d70a68aa19d8.html language=enus -->
## TOPIC 00265: RFmxWCDMA_SlotPhaseCfgSynchronizationModeAndInterval

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotphase_1ga50f0929db2b2ce2e0b29d70a68aa19d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotphase_1ga50f0929db2b2ce2e0b29d70a68aa19d8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement. Syntaxint32 __stdcall RFmxWCDMA_SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffs

### RFmxWCDMA_SlotPhaseCfgSynchronizationModeAndInterval

Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot.NameValueDescriptionRFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME0 (0x0)The frame boundary is detected, and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the frame boundary.RFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT1 (0x1)The slot boundary is detected and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length attribute starting at SlotPhase Meas Offset slots from the slot boundary. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_LENGTH attribute starting at RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET slots from the frame boundary. |  |
| RFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length attribute starting at SlotPhase Meas Offset slots from the slot boundary. |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter.The default value is 0. The valid values are any value greater than or equal to 0. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the SlotPhase measurement. This value is expressed in slots.The default value is 15. The valid values are any value greater than or equal to 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotpower.html language=enus -->
## TOPIC 00266: SlotPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotpower.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_SlotPowerCfgSynchronizationModeAndIntervalConfigures the synchronization mode, measurement offset, and measurement length. AttachmentsNone

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_SlotPowerCfgSynchronizationModeAndInterval | Configures the synchronization mode, measurement offset, and measurement length. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotpower_1ga487e72c5a8b1c38669bc43d182ab4181.html language=enus -->
## TOPIC 00267: RFmxWCDMA_SlotPowerCfgSynchronizationModeAndInterval

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotpower_1ga487e72c5a8b1c38669bc43d182ab4181.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__slotpower_1ga487e72c5a8b1c38669bc43d182ab4181.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. Syntaxint32 __stdcall RFmxWCDMA_SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)Parameter

### RFmxWCDMA_SlotPowerCfgSynchronizationModeAndInterval

Configures the synchronization mode, measurement offset, and measurement length.

#### Syntax

int32 __stdcall RFmxWCDMA_SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame or slot boundary.The default value is Slot.NameValueDescriptionRFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME0 (0x0)The frame boundary is detected, and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary.RFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT1 (0x1)The slot boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPower Measurement Length attribute starting at SlotPower Measurement Offset slots from the slot boundary. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME | 0 (0x0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH attribute starting at RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET slots from the frame boundary. |  |
| RFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT | 1 (0x1) | The slot boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPower Measurement Length attribute starting at SlotPower Measurement Offset slots from the slot boundary. |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter.The default value is 0. The valid values are any value greater than or equal to 0. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the SlotPower measurement. This value is expressed in slots.The default value is 15. The valid values are any value greater than or equal to 1. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger.html language=enus -->
## TOPIC 00268: Trigger

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_CfgDigitalEdgeTriggerConfigures the device to wait for a digital edge trigger and then marks a reference point within the record. RFmxWCDMA_CfgIQPowerEdgeTriggerConfigures the device to wait for the complex power of the I/Q data to cross the specified

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_CfgDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| RFmxWCDMA_CfgIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. |
| RFmxWCDMA_CfgSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| RFmxWCDMA_DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga1c7c9d8dcb42705a051837c9b7b77808.html language=enus -->
## TOPIC 00269: RFmxWCDMA_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga1c7c9d8dcb42705a051837c9b7b77808.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga1c7c9d8dcb42705a051837c9b7b77808.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxWCDMA_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescriptioni

### RFmxWCDMA_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga5d2d50d0cb7a7de56bf7093cdeeb0e6c.html language=enus -->
## TOPIC 00270: RFmxWCDMA_DisableTrigger

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga5d2d50d0cb7a7de56bf7093cdeeb0e6c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga5d2d50d0cb7a7de56bf7093cdeeb0e6c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxWCDMA_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrume

### RFmxWCDMA_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxWCDMA_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga63489f4394082f962af2493cd919c9c6.html language=enus -->
## TOPIC 00271: RFmxWCDMA_CfgDigitalEdgeTrigger

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga63489f4394082f962af2493cd919c9c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1ga63489f4394082f962af2493cd919c9c6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxWCDMA_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enabl

### RFmxWCDMA_CfgDigitalEdgeTrigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital edge trigger. The default value of this parameter is hardware dependent.Name (Value)DescriptionPFI0 (PFI0)The trigger is received on PFI 0.PFI1 (PFI1)The trigger is received on PFI 1.PXI_Trig0 (PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1 (PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2 (PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3 (PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4 (PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5 (PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6 (PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7 (PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR (PXI_STAR)The trigger is received on the PXI star trigger line.PXIe_DStarB (PXIe_DStarB)The trigger is received on the PXIe DStar B trigger line.TimerEvent (TimerEvent)The trigger is received from the timer event. |
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
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |  |  |
| digitalEdge | [in] | int32 | This parameter specifies the trigger edge to detect. The default value is Rising Edge.NameValueDescriptionRFMXWCDMA_VAL_DIGITAL_EDGE_RISING_EDGE0 (0x0)The trigger asserts on the rising edge of the signal.RFMXWCDMA_VAL_DIGITAL_EDGE_FALLING_EDGE1 (0x1)The trigger asserts on the falling edge of the signal. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_DIGITAL_EDGE_RISING_EDGE | 0 (0x0) | The trigger asserts on the rising edge of the signal. |  |
| RFMXWCDMA_VAL_DIGITAL_EDGE_FALLING_EDGE | 1 (0x1) | The trigger asserts on the falling edge of the signal. |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1gaf3546037a81eb69779025cf1258f4ec4.html language=enus -->
## TOPIC 00272: RFmxWCDMA_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1gaf3546037a81eb69779025cf1258f4ec4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__configuration__trigger_1gaf3546037a81eb69779025cf1258f4ec4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record. Syntaxint32 __stdcall RFmxWCDMA_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iq

### RFmxWCDMA_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxWCDMA_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger)

#### Remarks

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. The default value of this parameter is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope.NameValueDescriptionRFMXWCDMA_VAL_IQ_POWER_EDGE_RISING_SLOPE0 (0x0)The trigger asserts when the signal power is rising.RFMXWCDMA_VAL_IQ_POWER_EDGE_FALLING_SLOPE1 (0x1)The trigger asserts when the signal power is falling. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_RISING_SLOPE | 0 (0x0) | The trigger asserts when the signal power is rising. |  |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_FALLING_SLOPE | 1 (0x1) | The trigger asserts when the signal power is falling. |  |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative; and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default value of this parameter is hardware dependent. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| minimumQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual.NameValueDescriptionRFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL0 (0x0)The minimum quiet time for triggering is the value of the RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute.RFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO1 (0x1)The measurement computes the minimum quiet time used for triggering. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL | 0 (0x0) | The minimum quiet time for triggering is the value of the RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION attribute. |  |
| RFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO | 1 (0x1) | The measurement computes the minimum quiet time used for triggering. |  |
| minimumQuietTime | [in] | float64 | This parameter specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. This value is expressed in seconds. The default value of this parameter is hardware dependent. |
| iqPowerEdgeLevelType | [in] | int32 | This parameter specifies the reference for the IQ Power Edge Level parameter.The IQ Power Edge Level Type parameter is used only when you set the RFMXWCDMA_ATTR_TRIGGER_TYPE attribute to IQ Power Edge.NameValueDescriptionRFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE0 (0x0)The IQ Power Edge Level attribute is relative to the value of the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute.RFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE1 (0x1)The IQ Power Edge Level attribute specifies the absolute power. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE | 0 (0x0) | The IQ Power Edge Level attribute is relative to the value of the RFMXWCDMA_ATTR_REFERENCE_LEVEL attribute. |  |
| RFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE | 1 (0x1) | The IQ Power Edge Level attribute specifies the absolute power. |  |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch.html language=enus -->
## TOPIC 00273: Fetch

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPCDACHPModAccOBWQEVMSEMSlotPhaseSlotPowerGroup membersNoneAttachmentsNone

### Fetch

#### Groups

- ACP
- CDA
- CHP
- ModAcc
- OBW
- QEVM
- SEM
- SlotPhase
- SlotPower

#### Group members

None

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp.html language=enus -->
## TOPIC 00274: ACP

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_ACPFetchAbsolutePowersTraceFetches the absolute powers trace for the ACP measurement. RFmxWCDMA_ACPFetchCarrierMeasurementFetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power. RFmxWCDMA_ACPF

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_ACPFetchAbsolutePowersTrace | Fetches the absolute powers trace for the ACP measurement. |
| RFmxWCDMA_ACPFetchCarrierMeasurement | Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power. |
| RFmxWCDMA_ACPFetchCarrierMeasurementArray | Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER attribute. |
| RFmxWCDMA_ACPFetchOffsetMeasurement | Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier. |
| RFmxWCDMA_ACPFetchOffsetMeasurementArray | Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. |
| RFmxWCDMA_ACPFetchRelativePowersTrace | Fetches the relative powers trace for the ACP measurement. |
| RFmxWCDMA_ACPFetchSpectrum | Fetches the spectrum used for the ACP measurement. |
| RFmxWCDMA_ACPFetchTotalCarrierPower | Fetches the total carrier power for the ACP measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga202c39e7b909df0b61695a908df4c9ce.html language=enus -->
## TOPIC 00275: RFmxWCDMA_ACPFetchCarrierMeasurementArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga202c39e7b909df0b61695a908df4c9ce.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga202c39e7b909df0b61695a908df4c9ce.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER attribute. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char se

### RFmxWCDMA_ACPFetchCarrierMeasurementArray

Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the [RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__results_1ga9e4694952f484cdb0511a76bc81c87cb.html) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64[] | This parameter returns an array of carrier power values. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the RFMXWCDMA_ATTR_CENTER_FREQUENCY and RFMXWCDMA_ATTR_CARRIER_FREQUENCY attributes. This value is expressed in dBm. |
| relativePower | [out] | float64[] | This parameter returns an array of carrier power values relative to the total active carrier power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga597af62c8a805930021fe9f0c4b790a5.html language=enus -->
## TOPIC 00276: RFmxWCDMA_ACPFetchSpectrum

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga597af62c8a805930021fe9f0c4b790a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga597af62c8a805930021fe9f0c4b790a5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the ACP measurement. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescription

### RFmxWCDMA_ACPFetchSpectrum

Fetches the spectrum used for the ACP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power at each frequency bin. The value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga6a6ba271dabf20e3b592ed55b5dc7256.html language=enus -->
## TOPIC 00277: RFmxWCDMA_ACPFetchRelativePowersTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga6a6ba271dabf20e3b592ed55b5dc7256.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga6a6ba271dabf20e3b592ed55b5dc7256.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for the ACP measurement. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actual

### RFmxWCDMA_ACPFetchRelativePowersTrace

Fetches the relative powers trace for the ACP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| relativePowersTrace | [out] | float32[] | This parameter returns the relative power with reference to the power reference carrier attribute. The value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga7adfc117b21696fe5663b4160b0a6dc9.html language=enus -->
## TOPIC 00278: RFmxWCDMA_ACPFetchOffsetMeasurement

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga7adfc117b21696fe5663b4160b0a6dc9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1ga7adfc117b21696fe5663b4160b0a6dc9.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 time

### RFmxWCDMA_ACPFetchOffsetMeasurement

Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerRelativePower, float64 *upperRelativePower, float64 *lowerAbsolutePower, float64 *upperAbsolutePower)

#### Remarks

Use "offset<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxWCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64 * | This parameter returns the offset channel power measured relative to the power of the carrier(s) that you specify in the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute.This value is expressed in dB. |
| upperRelativePower | [out] | float64 * | This parameter returns the upper offset channel power measured relative to the power of the carrier(s) that you specify in the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64 * | This parameter returns the lower offset channel power.The lower offset channel power is the integrated power of the RRC-filtered signal at the lower offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |
| upperAbsolutePower | [out] | float64 * | This parameter returns the upper offset channel power.The upper offset channel power is the integrated power of the RRC-filtered signal at the upper offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gaa77aa5de637d53e86b6ef743a476bc7e.html language=enus -->
## TOPIC 00279: RFmxWCDMA_ACPFetchOffsetMeasurementArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gaa77aa5de637d53e86b6ef743a476bc7e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gaa77aa5de637d53e86b6ef743a476bc7e.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchOffsetMeasurementAr

### RFmxWCDMA_ACPFetchOffsetMeasurementArray

Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the [RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER](group____root__ni_r_fmx_w_c_d_m_a__attributes__acp__offset__power__reference_1ga8c650634e5720b37039a2af0c4d66a8e.html) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64[] | This parameter returns an array of lower offset channel power values measured relative to the power of the carrier(s) that you specify in the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. This value is expressed in dB. |
| upperRelativePower | [out] | float64[] | This parameter returns an array of upper offset channel power values measured relative to the power of the carrier(s) that you specify in the RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER attribute. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64[] | This parameter returns an array of lower offset channel power values.The lower offset channel power is the integrated power of the RRC-filtered signal at the lower offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |
| upperAbsolutePower | [out] | float64[] | This parameter returns an array of upper offset channel power values.The upper offset channel power is the integrated power of the RRC-filtered signal at the upper offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gab05022a7428bc3763dcf393cd8a38563.html language=enus -->
## TOPIC 00280: RFmxWCDMA_ACPFetchCarrierMeasurement

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gab05022a7428bc3763dcf393cd8a38563.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gab05022a7428bc3763dcf393cd8a38563.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *relativePower)Re

### RFmxWCDMA_ACPFetchCarrierMeasurement

Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *relativePower)

#### Remarks

Use "carrier<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64 * | This parameter returns the carrier power. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the RFMXWCDMA_ATTR_CENTER_FREQUENCY and RFMXWCDMA_ATTR_CARRIER_FREQUENCY attributes. This value is expressed in dBm. |
| relativePower | [out] | float64 * | This parameter returns the carrier power relative to the total carrier power. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gaf3d61cc281d93ad02fac737a214809da.html language=enus -->
## TOPIC 00281: RFmxWCDMA_ACPFetchTotalCarrierPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gaf3d61cc281d93ad02fac737a214809da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gaf3d61cc281d93ad02fac737a214809da.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power for the ACP measurement. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis pa

### RFmxWCDMA_ACPFetchTotalCarrierPower

Fetches the total carrier power for the ACP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalCarrierPower | [out] | float64 * | This parameter returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER attribute. This value is expressed in dBm. For a single-carrier measurement, total carrier power is the same as carrier absolute power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gafd87d55c41be1967fb7a3f256dc29871.html language=enus -->
## TOPIC 00282: RFmxWCDMA_ACPFetchAbsolutePowersTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gafd87d55c41be1967fb7a3f256dc29871.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__acp_1gafd87d55c41be1967fb7a3f256dc29871.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for the ACP measurement. Syntaxint32 __stdcall RFmxWCDMA_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actual

### RFmxWCDMA_ACPFetchAbsolutePowersTrace

Fetches the absolute powers trace for the ACP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| absolutePowersTrace | [out] | float32[] | This parameter returns the averaged power at each frequency bin. The value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda.html language=enus -->
## TOPIC 00283: CDA

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_CDAFetchCodeDomainIAndQPowerFetches the I and Q mean active powers and I and Q peak inactive powers. RFmxWCDMA_CDAFetchCodeDomainIAndQPowerTraceFetches the code domain power trace for I and Q branches. The code domain power is obtained for all codes wi

### CDA

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_CDAFetchCodeDomainIAndQPower | Fetches the I and Q mean active powers and I and Q peak inactive powers. |
| RFmxWCDMA_CDAFetchCodeDomainIAndQPowerTrace | Fetches the code domain power trace for I and Q branches. The code domain power is obtained for all codes with a spreading factor of 256, for I and Q branches separately. |
| RFmxWCDMA_CDAFetchCodeDomainPower | Fetches the Total Power , Total Active Power , Mean and Peak Active Powers, and Mean and Peak Inactive Powers. |
| RFmxWCDMA_CDAFetchCodeDomainPowerTrace | Fetches the code domain power trace. The code domain power is obtained for all codes with spreading factor 256 for both I and Q branches in an interleaved manner. |
| RFmxWCDMA_CDAFetchSymbolEVM | Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel. |
| RFmxWCDMA_CDAFetchSymbolEVMTrace | Fetches the root mean square EVM trace of the measurement channel. |
| RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace | Fetches the magnitude error trace of the measurement channel. |
| RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace | Fetches the phase error trace of the measurement channel. |
| RFmxWCDMA_CDAFetchSymbolPowerTrace | Fetches the power versus time trace of the symbol corresponding to the measurement channel. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga0882cfbc9b17a47e31b2f8b6c718d515.html language=enus -->
## TOPIC 00284: RFmxWCDMA_CDAFetchSymbolEVMTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga0882cfbc9b17a47e31b2f8b6c718d515.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga0882cfbc9b17a47e31b2f8b6c718d515.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the root mean square EVM trace of the measurement channel. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptionins

### RFmxWCDMA_CDAFetchSymbolEVMTrace

Fetches the root mean square EVM trace of the measurement channel.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolEVM | [out] | float32[] | This parameter returns an array of RMS EVM values of the symbols of the measurement channel. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga269c6e3146fce2265be11513f6730fa3.html language=enus -->
## TOPIC 00285: RFmxWCDMA_CDAFetchSymbolEVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga269c6e3146fce2265be11513f6730fa3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga269c6e3146fce2265be11513f6730fa3.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout

### RFmxWCDMA_CDAFetchSymbolEVM

Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsSymbolEVM, float64 *peakSymbolEVM, float64 *rmsSymbolMagnitudeError, float64 *rmsSymbolPhaseError, float64 *meanSymbolPower, float64 *chipRateError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsSymbolEVM | [out] | float64 * | This parameter returns the RMS EVM for the measurement channel. This value is expressed as a percentage. |
| peakSymbolEVM | [out] | float64 * | This parameter returns the peak EVM for the measurement channel. This value is expressed as a percentage. |
| rmsSymbolMagnitudeError | [out] | float64 * | This parameter returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage. |
| rmsSymbolPhaseError | [out] | float64 * | This parameter returns the RMS phase error for the measurement channel. This value is expressed in degrees. |
| meanSymbolPower | [out] | float64 * | This parameter returns the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| chipRateError | [out] | float64 * | This parameter returns the chip rate error of the composite signal. This value is expressed in ppm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga59ddde65efb79c4427ecf731a6563a1f.html language=enus -->
## TOPIC 00286: RFmxWCDMA_CDAFetchCodeDomainIAndQPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga59ddde65efb79c4427ecf731a6563a1f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga59ddde65efb79c4427ecf731a6563a1f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I and Q mean active powers and I and Q peak inactive powers. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *imEanActivePower, float64 *qMeanActivePower, float64 *iPeakInactivePower, float64

### RFmxWCDMA_CDAFetchCodeDomainIAndQPower

Fetches the I and Q mean active powers and I and Q peak inactive powers.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *imEanActivePower, float64 *qMeanActivePower, float64 *iPeakInactivePower, float64 *qPeakInactivePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| imEanActivePower | [out] | float64 * | This parameter returns the average code power among the set of active in-phase channels in the code domain. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| qMeanActivePower | [out] | float64 * | This parameter returns the average code power among the set of active quadrature-phase channels in the code domain. If you set the CDA Pwr Unit attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr attribute. This value is expressed in dB or dBm. |
| iPeakInactivePower | [out] | float64 * | This parameter returns the largest code power among the set of inactive in-phase channels in the code domain. If you set the CDA Pwr Unit attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr attribute. This value is expressed in dB or dBm. |
| qPeakInactivePower | [out] | float64 * | This parameter returns the largest code power among the set of inactive quadrature-phase channels in the code domain. If you set the CDA Pwr Unit attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr attribute. This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga755a834d41f6bcadaf1e8a8f1bc3e7d6.html language=enus -->
## TOPIC 00287: RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga755a834d41f6bcadaf1e8a8f1bc3e7d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga755a834d41f6bcadaf1e8a8f1bc3e7d6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace of the measurement channel. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescripti

### RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace

Fetches the phase error trace of the measurement channel.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolPhaseError | [out] | float32[] | This parameter returns an array of phase errors of the symbols of the measurement channel. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga781d520723f64731e1cf01946c48c5e1.html language=enus -->
## TOPIC 00288: RFmxWCDMA_CDAFetchSymbolPowerTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga781d520723f64731e1cf01946c48c5e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga781d520723f64731e1cf01946c48c5e1.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power versus time trace of the symbol corresponding to the measurement channel. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32 *actualArraySize)ParametersN

### RFmxWCDMA_CDAFetchSymbolPowerTrace

Fetches the power versus time trace of the symbol corresponding to the measurement channel.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolPowers | [out] | float32[] | This parameter returns the array of symbol powers of the measurement channel. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga7f1b35260caf1c4c34f0fb58f6ecaae4.html language=enus -->
## TOPIC 00289: RFmxWCDMA_CDAFetchCodeDomainPowerTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga7f1b35260caf1c4c34f0fb58f6ecaae4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga7f1b35260caf1c4c34f0fb58f6ecaae4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the code domain power trace. The code domain power is obtained for all codes with spreading factor 256 for both I and Q branches in an interleaved manner. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchCodeDomainPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout,

### RFmxWCDMA_CDAFetchCodeDomainPowerTrace

Fetches the code domain power trace. The code domain power is obtained for all codes with spreading factor 256 for both I and Q branches in an interleaved manner.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 codeDomainPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| codeDomainPowers | [out] | float32[] | This parameter returns an array of code domain powers for I and Q branches in an interleaved manner. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga842a20e3c9823149a1301f788df2cfc4.html language=enus -->
## TOPIC 00290: RFmxWCDMA_CDAFetchCodeDomainPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga842a20e3c9823149a1301f788df2cfc4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1ga842a20e3c9823149a1301f788df2cfc4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the Total Power , Total Active Power , Mean and Peak Active Powers, and Mean and Peak Inactive Powers. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalPower, float64 *totalActivePower, float64 *

### RFmxWCDMA_CDAFetchCodeDomainPower

Fetches the Total Power , Total Active Power , Mean and Peak Active Powers, and Mean and Peak Inactive Powers.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalPower, float64 *totalActivePower, float64 *meanActivePower, float64 *peakActivePower, float64 *meanInactivePower, float64 *peakInactivePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalPower | [out] | float64 * | This parameter returns the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm. |
| totalActivePower | [out] | float64 * | This parameter returns the sum of all the active channel powers. If you set the RFMXWCDMA_ATTR_CDA_POWER_UNIT attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER attribute. This value is expressed in dB or dBm. |
| meanActivePower | [out] | float64 * | This parameter returns the average of all the active channel powers. If you set the CDA Pwr Unit attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr attribute. This value is expressed in dB or dBm. |
| peakActivePower | [out] | float64 * | This parameter returns the largest code power among the set of active channels in the code domain. If you set the CDA Pwr Unit attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr attribute. This value is expressed in dB or dBm. |
| meanInactivePower | [out] | float64 * | This parameter returns the average code power among the set of inactive channels in the code domain. If you set the CDA Pwr Unit attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr attribute. This value is expressed in dB or dBm. |
| peakInactivePower | [out] | float64 * | This parameter returns the largest code power among the set of inactive channels in the code domain. If you set the CDA Pwr Unit attribute to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr attribute. This value is expressed in dB or dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1gace5a3610509014865d32797e4ab65ecc.html language=enus -->
## TOPIC 00291: RFmxWCDMA_CDAFetchCodeDomainIAndQPowerTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1gace5a3610509014865d32797e4ab65ecc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1gace5a3610509014865d32797e4ab65ecc.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the code domain power trace for I and Q branches. The code domain power is obtained for all codes with a spreading factor of 256, for I and Q branches separately. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], floa

### RFmxWCDMA_CDAFetchCodeDomainIAndQPowerTrace

Fetches the code domain power trace for I and Q branches. The code domain power is obtained for all codes with a spreading factor of 256, for I and Q branches separately.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iCodeDomainPowers | [out] | float32[] | This parameter returns an array of code domain powers for the in-phase component. |
| qCodeDomainPowers | [out] | float32[] | This parameter returns an array of code domain powers for the quadrature-phase component. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1gaf3b27562bfb6a3335b54f9884609b801.html language=enus -->
## TOPIC 00292: RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1gaf3b27562bfb6a3335b54f9884609b801.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__cda_1gaf3b27562bfb6a3335b54f9884609b801.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error trace of the measurement channel. Syntaxint32 __stdcall RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionT

### RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace

Fetches the magnitude error trace of the measurement channel.

#### Syntax

int32 __stdcall RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolMagnitudeError | [out] | float32[] | This parameter returns an array of magnitude errors of the symbols of the measurement channel. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp.html language=enus -->
## TOPIC 00293: CHP

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_CHPFetchCarrierMeasurementFetches the absolute and relative powers of the carrier for the CHP measurement. The relative power is relative to the total carrier power. RFmxWCDMA_CHPFetchCarrierMeasurementArrayFetches an array of absolute powers and array

### CHP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_CHPFetchCarrierMeasurement | Fetches the absolute and relative powers of the carrier for the CHP measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_CHPFetchCarrierMeasurementArray | Fetches an array of absolute powers and array of relative powers of the carriers for the CHP measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_CHPFetchSpectrum | Fetches the spectrum used for the CHP measurement. |
| RFmxWCDMA_CHPFetchTotalCarrierPower | Fetches the total carrier power for the CHP measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1ga0ab595d241eb51ffb89be9d81a1e295d.html language=enus -->
## TOPIC 00294: RFmxWCDMA_CHPFetchCarrierMeasurement

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1ga0ab595d241eb51ffb89be9d81a1e295d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1ga0ab595d241eb51ffb89be9d81a1e295d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers of the carrier for the CHP measurement. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_CHPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, f

### RFmxWCDMA_CHPFetchCarrierMeasurement

Fetches the absolute and relative powers of the carrier for the CHP measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_CHPFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absolutePower, float64 *relativePower)

#### Remarks

Use "carrier<n>" as the selector string to configure this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64 * | This parameter returns the carrier power integrated over a bandwidth of 5 MHz. This value is expressed in dBm. |
| relativePower | [out] | float64 * | This parameter returns the carrier power relative to the RFMXWCDMA_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1ga393207e7694db14e57aec19e27ac2af7.html language=enus -->
## TOPIC 00295: RFmxWCDMA_CHPFetchCarrierMeasurementArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1ga393207e7694db14e57aec19e27ac2af7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1ga393207e7694db14e57aec19e27ac2af7.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of absolute powers and array of relative powers of the carriers for the CHP measurement. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_CHPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 time

### RFmxWCDMA_CHPFetchCarrierMeasurementArray

Fetches an array of absolute powers and array of relative powers of the carriers for the CHP measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_CHPFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absolutePower[], float64 relativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absolutePower | [out] | float64[] | This parameter returns an array of carrier powers integrated over a bandwidth of 5 MHz. This value is expressed in dBm. |
| relativePower | [out] | float64[] | This parameter returns an array of carrier powers relative to the RFMXWCDMA_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1gaad3920aae83bd226cd630d46c7cdb045.html language=enus -->
## TOPIC 00296: RFmxWCDMA_CHPFetchSpectrum

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1gaad3920aae83bd226cd630d46c7cdb045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1gaad3920aae83bd226cd630d46c7cdb045.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the CHP measurement. Syntaxint32 __stdcall RFmxWCDMA_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescription

### RFmxWCDMA_CHPFetchSpectrum

Fetches the spectrum used for the CHP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power at each frequency bin. The value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1gaedba24c9d50e5c4a9ff5242d4a39229d.html language=enus -->
## TOPIC 00297: RFmxWCDMA_CHPFetchTotalCarrierPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1gaedba24c9d50e5c4a9ff5242d4a39229d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__chp_1gaedba24c9d50e5c4a9ff5242d4a39229d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power for the CHP measurement. Syntaxint32 __stdcall RFmxWCDMA_CHPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis pa

### RFmxWCDMA_CHPFetchTotalCarrierPower

Fetches the total carrier power for the CHP measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_CHPFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalCarrierPower | [out] | float64 * | This parameter returns the total integrated power of all the active carriers. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc.html language=enus -->
## TOPIC 00298: ModAcc

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_ModAccFetchConstellationTraceFetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement. RFmxWCDMA_ModAccFetchConstellationTraceSplitFetches the complex chips of the composite corrected signal of a carrier for t

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_ModAccFetchConstellationTrace | Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchConstellationTraceSplit | Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchDetectedChannel | Returns the spreading factor, spreading code, modulation type, and branch of the detected channel of a carrier in the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchDetectedChannelArray | Fetches an array of spreading factors, an array of spreading codes, an array of modulation types, and an array of branches of the detected channels of the carriers, when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Auto Detect for the ModAcc measurement. When you set the Channel Configuration Mode attribute to User Defined or Test Model, it returns the corresponding results for the configured channels of all the carriers. |
| RFmxWCDMA_ModAccFetchEVM | Fetches the chip rate error, frequency error, RMS EVM, peak EVM, Rho, RMS magnitude error, and RMS phase error of the complex chips of the corrected composite signal for a carrier in the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchEVMArray | Fetches an array of chip rate errors, an array of frequency errors, an array of RMS EVMs, an array of peak EVMs, an array of Rhos, an array of RMS magnitude errors, and an array of RMS phase errors of the complex chips of the corrected signal corresponding to all the carriers in the ModAcc measurement. The array elements represent the result of each carrier in the measurement. |
| RFmxWCDMA_ModAccFetchEVMTrace | Fetches the EVM trace of a carrier for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchIQImpairments | Fetches the I/Q origin offset, I/Q gain imbalance and I/Q quadrature error for a carrier in the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchIQImpairmentsArray | Fetches the array of I/Q origin offsets, an array of I/Q gain imbalances, and an array of I/Q quadrature errors corresponding to all the carriers in the ModAcc measurement. The array elements represent result of each carrier in the measurement. |
| RFmxWCDMA_ModAccFetchMagnitudeErrorTrace | Fetches the magnitude error trace of a carrier for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchMulticarrierIQImpairments | Fetches the I/Q impairments for a multicarrier signal. |
| RFmxWCDMA_ModAccFetchNumberOfDetectedChannels | Fetches the number of detected channels in a carrier for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray | Fetches an array of number of detected channels of all the carriers in the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchPeakActiveCDE | Fetches the peak value among the code domain errors (CDEs) of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchPeakActiveCDEArray | Fetches arrays of peak CDE values among all the active channels of a carrier, and the corresponding code numbers, spreading factors, and branches of the carriers. Each element in these arrays corresponds to the peak value among the code domain errors of all the active channels in each carrier. |
| RFmxWCDMA_ModAccFetchPeakCDE | Fetches the peak value among the code domain errors (CDEs) obtained with a fixed spreading factor of 4, along with the code number and branch that correspond to this peak value for a carrier in the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchPeakCDEArray | Fetches an array of peak CDE values obtained with a fixed spreading factor of 4 for all the carriers and the corresponding code numbers and branches. Each element in these arrays corresponds to the peak value among the code domain errors in each carrier. |
| RFmxWCDMA_ModAccFetchPhaseErrorTrace | Fetches the phase error trace of a carrier for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchRCDE | Returns the peak relative code domain error (RCDE) value of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchRCDEArray | Fetches arrays of peak relative CDE values of the active channels, of the carriers and the corresponding code numbers, spreading factors, and branches. Each element in these arrays corresponds to the peak value among the relative code domain errors of all the active channels in each carrier. |
| RFmxWCDMA_ModAccFetchRCDETrace | Fetches the relative code domain errors (RCDE) trace of a carrier for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchReferenceWaveform | Fetches the reference waveform for the ModAcc measurement. |
| RFmxWCDMA_ModAccFetchReferenceWaveformSplit | Fetches the reference waveform for the ModAcc measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga0e517f7bfafe2cd190f029d22bbb670e.html language=enus -->
## TOPIC 00299: RFmxWCDMA_ModAccFetchRCDE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga0e517f7bfafe2cd190f029d22bbb670e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga0e517f7bfafe2cd190f029d22bbb670e.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak relative code domain error (RCDE) value of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchRCDE(niRFmxInstrHandle instrumentHandle, ch

### RFmxWCDMA_ModAccFetchRCDE

Returns the peak relative code domain error (RCDE) value of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchRCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakRCDE, int32 *peakRCDESpreadingFactor, int32 *peakRCDECode, int32 *peakRCDEBranch)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| peakRCDE | [out] | float64 * | This parameter returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB.The relative CDEs are computed by despreading the descrambled error vector corresponding to each active channel with the appropriate active channel codes. The RCDE is defined as the ratio of the mean power of this despread error vector to the mean power of the corresponding reference waveform. |
| peakRCDESpreadingFactor | [out] | int32 * | This parameter returns the spreading factor of the channel corresponding to the value of the Peak RCDE parameter for a carrier. |
| peakRCDECode | [out] | int32 * | This parameter returns the spreading code of the channel corresponding to the value of the Peak RCDE parameter for a carrier. |
| peakRCDEBranch | [out] | int32 * | This parameter returns the branch of the channel corresponding to the value of the Peak RCDE parameter for a carrier.NameValueDescriptionRFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I0 (0x0)The signal is modulated on the in-phase branch.RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_Q1 (0x1)The signal is modulated on the quadrature-phase branch.RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I_AND_Q2 (0x2)The signal is complex modulated. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga13d571ca3014d897f612e67e48b599ed.html language=enus -->
## TOPIC 00300: RFmxWCDMA_ModAccFetchDetectedChannel

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga13d571ca3014d897f612e67e48b599ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga13d571ca3014d897f612e67e48b599ed.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor, spreading code, modulation type, and branch of the detected channel of a carrier in the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedSpreadingFac

### RFmxWCDMA_ModAccFetchDetectedChannel

Returns the spreading factor, spreading code, modulation type, and branch of the detected channel of a carrier in the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedSpreadingFactor, int32 *detectedSpreadingCode, int32 *detectedModulationType, int32 *detectedBranch)

#### Remarks

Use "carrier<n>/channel<k>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, carrier number, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Example:"carrier0/channel0""signal::sig1/carrier0/channel0""signal::sig1/result::r1/carrier0/channel0""result::r1/carrier0/channel0"You can use the RFmxWCDMA_BuildChannelString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedSpreadingFactor | [out] | int32 * | This parameter returns the spreading factors of the detected channels when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Auto Detect. If you set the Channel Configuration Mode attribute to User Defined or Test Model, the measurement returns the spreading factor of the configured channel of a carrier. |
| detectedSpreadingCode | [out] | int32 * | This parameter returns the spreading code of the detected channels when you set the Channel Configuration Mode attribute to Auto Detect. If you set the Channel Configuration Mode attribute to User Defined or Test Model, the measurement returns the spreading code of the configured channel of a carrier. |
| detectedModulationType | [out] | int32 * | This parameter returns the modulation type of the detected channels when you set the Channel Configuration Mode attribute to Auto Detect. If you set the Channel configuration Mode attribute to User Defined or Test Model, the measurement returns the modulation type of the configured channel of a carrier.NameValueDescriptionRFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_BPSK_QPSK0 (0x0)The modulation type is BPSK.RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_4PAM_16QAM1 (0x1)The modulation type is 4-PAM.RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_64QAM2 (0x2)The modulation type is 64-QAM. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_BPSK_QPSK | 0 (0x0) | The modulation type is BPSK. |  |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_4PAM_16QAM | 1 (0x1) | The modulation type is 4-PAM. |  |
| RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_64QAM | 2 (0x2) | The modulation type is 64-QAM. |  |
| detectedBranch | [out] | int32 * | This parameter returns the branch of the detected channels when you set the Channel Configuration Mode attribute to Auto Detect. If you set the Channel Configuration Mode attribute to User Defined or Test Model, the measurement returns the branch of the configured channel of a carrier.NameValueDescriptionRFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I0 (0x0)The signal is modulated on the in-phase branch.RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_Q1 (0x1)The signal is modulated on the quadrature-phase branch.RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I_AND_Q2 (0x2)The signal is complex modulated. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga17d2a13d0dc99be7486ab6f31e499c6d.html language=enus -->
## TOPIC 00301: RFmxWCDMA_ModAccFetchMulticarrierIQImpairments

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga17d2a13d0dc99be7486ab6f31e499c6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga17d2a13d0dc99be7486ab6f31e499c6d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q impairments for a multicarrier signal. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchMulticarrierIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *multicarrierIQOriginOffset, float64 *multicarrierIQGainImbalance, float64 *multicarrierIQQu

### RFmxWCDMA_ModAccFetchMulticarrierIQImpairments

Fetches the I/Q impairments for a multicarrier signal.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchMulticarrierIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *multicarrierIQOriginOffset, float64 *multicarrierIQGainImbalance, float64 *multicarrierIQQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| multicarrierIQOriginOffset | [out] | float64 * | This parameter returns the estimated I/Q origin offset of the multicarrier signal when the RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE attribute is set to LO per Band. This value is expressed in dB. This result is useful when the LO is at the center of the multicarrier signal. |
| multicarrierIQGainImbalance | [out] | float64 * | This parameter returns NaN. This parameter has been added for future use. |
| multicarrierIQQuadratureError | [out] | float64 * | This parameter returns NaN. This parameter has been added for future use. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga1fe07835e2d91d9c6a059c95c1ec71ec.html language=enus -->
## TOPIC 00302: RFmxWCDMA_ModAccFetchEVMArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga1fe07835e2d91d9c6a059c95c1ec71ec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga1fe07835e2d91d9c6a059c95c1ec71ec.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of chip rate errors, an array of frequency errors, an array of RMS EVMs, an array of peak EVMs, an array of Rhos, an array of RMS magnitude errors, and an array of RMS phase errors of the complex chips of the corrected signal corresponding to all the carriers in the ModAcc measureme

### RFmxWCDMA_ModAccFetchEVMArray

Fetches an array of chip rate errors, an array of frequency errors, an array of RMS EVMs, an array of peak EVMs, an array of Rhos, an array of RMS magnitude errors, and an array of RMS phase errors of the complex chips of the corrected signal corresponding to all the carriers in the ModAcc measurement. The array elements represent the result of each carrier in the measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchEVMArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 rmsEVM[], float64 peakEVM[], float64 rho[], float64 frequencyError[], float64 chipRateError[], float64 rmsMagnitudeError[], float64 rmsPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsEVM | [out] | float64[] | This parameter returns the array of RMS EVM values of the composite signal corresponding to the carriers. This value is expressed as a percentage. |
| peakEVM | [out] | float64[] | This parameter returns the array of peak EVM values of the composite signal corresponding to the carriers. This value is expressed as a percentage. |
| rho | [out] | float64[] | This parameter returns the array of correlation values of the received signal with the reference signal normalized by the signal power corresponding to the carriers. Valid values range from 0 to 1.0, inclusive. The maximum value of Rho is 1.0, which indicates that the received signal and reference signal are perfectly correlated. |
| frequencyError | [out] | float64[] | This parameter returns the array of frequency offset values of the composite signal corresponding to the carriers. This value is expressed in Hz. |
| chipRateError | [out] | float64[] | This parameter returns the array of chip rate errors of the composite signal corresponding to the carriers. This value is expressed in ppm. |
| rmsMagnitudeError | [out] | float64[] | This parameter returns the array of RMS magnitude errors of the composite signal corresponding to the carriers. This value is expressed in percentage. |
| rmsPhaseError | [out] | float64[] | This parameter returns the array of RMS phase error values of the composite signal corresponding to the carriers. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga3a67c8ccc700ac85ce4eed44a047c5c4.html language=enus -->
## TOPIC 00303: RFmxWCDMA_ModAccFetchPeakCDE

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga3a67c8ccc700ac85ce4eed44a047c5c4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga3a67c8ccc700ac85ce4eed44a047c5c4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak value among the code domain errors (CDEs) obtained with a fixed spreading factor of 4, along with the code number and branch that correspond to this peak value for a carrier in the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHan

### RFmxWCDMA_ModAccFetchPeakCDE

Fetches the peak value among the code domain errors (CDEs) obtained with a fixed spreading factor of 4, along with the code number and branch that correspond to this peak value for a carrier in the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakCDE, int32 *peakCDECode, int32 *peakCDEBranch)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| peakCDE | [out] | float64 * | This parameter returns the maximum CDE value for a carrier in the received signal.The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used.The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code.This value is expressed in dB. |
| peakCDECode | [out] | int32 * | This parameter returns the spreading code corresponding to the value of the Peak CDE parameter for a carrier in the received signal. |
| peakCDEBranch | [out] | int32 * | This parameter returns the branch of the channel corresponding to the value of the Peak CDE parameter for a carrier in the received signal.NameValueDescriptionRFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I0 (0x0)The signal is modulated on the in-phase branch.RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_Q1 (0x1)The signal is modulated on the quadrature-phase branch.RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I_AND_Q2 (0x2)The signal is complex modulated. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga3dd862a8cfaaad8953e928a304b599ef.html language=enus -->
## TOPIC 00304: RFmxWCDMA_ModAccFetchEVMTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga3dd862a8cfaaad8953e928a304b599ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga3dd862a8cfaaad8953e928a304b599ef.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM trace of a carrier for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)RemarksUse "carrier<n>" as t

### RFmxWCDMA_ModAccFetchEVMTrace

Fetches the EVM trace of a carrier for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| evm | [out] | float32[] | This parameter returns the EVM value. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga4136b4d20dda8c9a205e4eb67883e4e2.html language=enus -->
## TOPIC 00305: RFmxWCDMA_ModAccFetchIQImpairmentsArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga4136b4d20dda8c9a205e4eb67883e4e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga4136b4d20dda8c9a205e4eb67883e4e2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of I/Q origin offsets, an array of I/Q gain imbalances, and an array of I/Q quadrature errors corresponding to all the carriers in the ModAcc measurement. The array elements represent result of each carrier in the measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchIQImpairment

### RFmxWCDMA_ModAccFetchIQImpairmentsArray

Fetches the array of I/Q origin offsets, an array of I/Q gain imbalances, and an array of I/Q quadrature errors corresponding to all the carriers in the ModAcc measurement. The array elements represent result of each carrier in the measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchIQImpairmentsArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 iqOriginOffset[], float64 iqGainImbalance[], float64 iqQuadratureError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64[] | This parameter returns the array of I/Q origin offset values of the composite signal. This value is expressed in dB.The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |
| iqGainImbalance | [out] | float64[] | This parameter returns the array of I/Q gain imbalance values of the composite signal. This value is expressed in dB.The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. |
| iqQuadratureError | [out] | float64[] | This parameter returns the array of I/Q quadrature error values of the composite signal.This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga492201e397f4519fea8b61b68b27ba05.html language=enus -->
## TOPIC 00306: RFmxWCDMA_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga492201e397f4519fea8b61b68b27ba05.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga492201e397f4519fea8b61b68b27ba05.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace of a carrier for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)Remark

### RFmxWCDMA_ModAccFetchPhaseErrorTrace

Fetches the phase error trace of a carrier for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| phaseError | [out] | float32[] | This parameter returns an array of phase error values. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga49cf72f1290eaa8d5bce0c3a96d2543b.html language=enus -->
## TOPIC 00307: RFmxWCDMA_ModAccFetchPeakActiveCDEArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga49cf72f1290eaa8d5bce0c3a96d2543b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga49cf72f1290eaa8d5bce0c3a96d2543b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches arrays of peak CDE values among all the active channels of a carrier, and the corresponding code numbers, spreading factors, and branches of the carriers. Each element in these arrays corresponds to the peak value among the code domain errors of all the active channels in each carrier. Synta

### RFmxWCDMA_ModAccFetchPeakActiveCDEArray

Fetches arrays of peak CDE values among all the active channels of a carrier, and the corresponding code numbers, spreading factors, and branches of the carriers. Each element in these arrays corresponds to the peak value among the code domain errors of all the active channels in each carrier.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchPeakActiveCDEArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 peakActiveCDE[], int32 peakActiveCDESpreadingFactor[], int32 peakActiveCDECode[], int32 peakActiveCDEBranch[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| peakActiveCDE | [out] | float64[] | This parameter returns array of maximum values among the active code domain errors. This value is expressed in dB.The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform. |
| peakActiveCDESpreadingFactor | [out] | int32[] | This parameter returns the array of spreading factors of the channel corresponding to the value of the Peak Active CDE parameter. |
| peakActiveCDECode | [out] | int32[] | This parameter returns the array of spreading codes of the channel corresponding to the value of the Peak Active CDE parameter. |
| peakActiveCDEBranch | [out] | int32[] | This parameter returns the array of branch values of the channel corresponding to the value of the Peak Active CDE parameter.NameValueDescriptionRFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I0 (0x0)The signal is modulated on the in-phase branch.RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q1 (0x1)The signal is modulated on the quadrature-phase branch.RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q2 (0x2)The signal is complex modulated. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I | 0 (0x0) | The signal is modulated on the in-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q | 1 (0x1) | The signal is modulated on the quadrature-phase branch. |  |
| RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q | 2 (0x2) | The signal is complex modulated. |  |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga52de31c9339f20d736881ca9e72d3d55.html language=enus -->
## TOPIC 00308: RFmxWCDMA_ModAccFetchMagnitudeErrorTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga52de31c9339f20d736881ca9e72d3d55.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga52de31c9339f20d736881ca9e72d3d55.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error trace of a carrier for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArra

### RFmxWCDMA_ModAccFetchMagnitudeErrorTrace

Fetches the magnitude error trace of a carrier for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| magnitudeError | [out] | float32[] | This parameter returns the magnitude error values. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga6dc0447457d116930886c1f9ed83bd68.html language=enus -->
## TOPIC 00309: RFmxWCDMA_ModAccFetchIQImpairments

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga6dc0447457d116930886c1f9ed83bd68.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga6dc0447457d116930886c1f9ed83bd68.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q origin offset, I/Q gain imbalance and I/Q quadrature error for a carrier in the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance,

### RFmxWCDMA_ModAccFetchIQImpairments

Fetches the I/Q origin offset, I/Q gain imbalance and I/Q quadrature error for a carrier in the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64 * | This parameter returns the I/Q origin offset of the composite signal of a carrier. This value is expressed in dB.The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |
| iqGainImbalance | [out] | float64 * | This parameter returns the I/Q gain imbalance of the composite signal of a carrier. This value is expressed in dB.The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. |
| iqQuadratureError | [out] | float64 * | This parameter returns the I/Q quadrature error of the composite signal of a carrier.This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga74d2d2623f85f5b94f636829b1c1d5e4.html language=enus -->
## TOPIC 00310: RFmxWCDMA_ModAccFetchNumberOfDetectedChannels

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga74d2d2623f85f5b94f636829b1c1d5e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga74d2d2623f85f5b94f636829b1c1d5e4.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of detected channels in a carrier for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfDetectedChannels)RemarksUse "carrier<n>" as the selector str

### RFmxWCDMA_ModAccFetchNumberOfDetectedChannels

Fetches the number of detected channels in a carrier for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfDetectedChannels)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| numberOfDetectedChannels | [out] | int32 * | This parameter returns the number of detected channels when you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to Auto Detect. If you set the Channel Configuration Mode attribute to User Defined or Test Model, this parameter returns the number of configured channels. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga99d90f7605cb1df8ee7f8cbafc7b982a.html language=enus -->
## TOPIC 00311: RFmxWCDMA_ModAccFetchReferenceWaveform

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga99d90f7605cb1df8ee7f8cbafc7b982a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1ga99d90f7605cb1df8ee7f8cbafc7b982a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle referenceWaveform[], int32 arraySize, int32 *actualArraySize)P

### RFmxWCDMA_ModAccFetchReferenceWaveform

Fetches the reference waveform for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchReferenceWaveform(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, NIComplexSingle referenceWaveform[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration. This value is expressed in seconds. |
| referenceWaveform | [out] | NIComplexSingle[] | This parameter returns an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gaac92c0adb863eae349f1deafc084ece8.html language=enus -->
## TOPIC 00312: RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gaac92c0adb863eae349f1deafc084ece8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gaac92c0adb863eae349f1deafc084ece8.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of number of detected channels of all the carriers in the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 numberofDetectedChannels[], int32 arraySize, int32

### RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray

Fetches an array of number of detected channels of all the carriers in the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 numberofDetectedChannels[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| numberofDetectedChannels | [out] | int32[] | This parameter returns the array of the number of detected channels when you set the Channel Configuration Mode attribute to Auto Detect. If you set the RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined or Test Model, this parameter returns the array of the number of configured channels. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gab0eb665b9a7644ffc33c123a0a47f15b.html language=enus -->
## TOPIC 00313: RFmxWCDMA_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gab0eb665b9a7644ffc33c123a0a47f15b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gab0eb665b9a7644ffc33c123a0a47f15b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int3

### RFmxWCDMA_ModAccFetchConstellationTraceSplit

Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellationI | [out] | float32[] | This parameter returns an array of complex chips of the corrected signal of a carrier on which the ModAcc measurements are done. You can use these chips to obtain the constellation diagram. |
| constellationQ | [out] | float32[] | This parameter returns an array of complex chips of the corrected signal of a carrier on which the ModAcc measurements are done. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gac4fc69527188ccae016b952757472337.html language=enus -->
## TOPIC 00314: RFmxWCDMA_ModAccFetchConstellationTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gac4fc69527188ccae016b952757472337.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gac4fc69527188ccae016b952757472337.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actu

### RFmxWCDMA_ModAccFetchConstellationTrace

Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellation | [out] | NIComplexSingle[] | This parameter returns an array of complex chips of the corrected signal of a carrier on which the ModAcc measurements are done. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gad23d7ac6cbc51a7033547bc0eaecd0b0.html language=enus -->
## TOPIC 00315: RFmxWCDMA_ModAccFetchPeakCDEArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gad23d7ac6cbc51a7033547bc0eaecd0b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gad23d7ac6cbc51a7033547bc0eaecd0b0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of peak CDE values obtained with a fixed spreading factor of 4 for all the carriers and the corresponding code numbers and branches. Each element in these arrays corresponds to the peak value among the code domain errors in each carrier. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchPe

### RFmxWCDMA_ModAccFetchPeakCDEArray

Fetches an array of peak CDE values obtained with a fixed spreading factor of 4 for all the carriers and the corresponding code numbers and branches. Each element in these arrays corresponds to the peak value among the code domain errors in each carrier.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchPeakCDEArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 peakCDE[], int32 peakCDECode[], int32 peakCDEBranch[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| peakCDE | [out] | float64[] | This parameter returns the array of maximum CDE values. This value is expressed in dB.The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used.The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code. |
| peakCDECode | [out] | int32[] | This parameter returns the array of spreading codes corresponding to the value of the Peak CDE parameter. |
| peakCDEBranch | [out] | int32[] | This parameter returns the array of branches of the channel corresponding to the value of the Peak CDE parameter. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gaef05309b7078a2695465792981a85821.html language=enus -->
## TOPIC 00316: RFmxWCDMA_ModAccFetchReferenceWaveformSplit

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gaef05309b7078a2695465792981a85821.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__modacc_1gaef05309b7078a2695465792981a85821.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference waveform for the ModAcc measurement. Syntaxint32 __stdcall RFmxWCDMA_ModAccFetchReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySi

### RFmxWCDMA_ModAccFetchReferenceWaveformSplit

Fetches the reference waveform for the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_ModAccFetchReferenceWaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 referenceWaveformI[], float32 referenceWaveformQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the sample duration. This value is expressed in seconds. |
| referenceWaveformI | [out] | float32[] | This parameter returns an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| referenceWaveformQ | [out] | float32[] | This parameter returns an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__obw.html language=enus -->
## TOPIC 00317: OBW

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__obw.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_OBWFetchMeasurementFetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power. RFmxWCDMA_OBWFetchSpectrumFetches the spectrum used for the OBW measurement. AttachmentsNone

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_OBWFetchMeasurement | Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_OBWFetchSpectrum | Fetches the spectrum used for the OBW measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__obw_1ga5d87bc0b58f9ef55d6888683794f29d2.html language=enus -->
## TOPIC 00318: RFmxWCDMA_OBWFetchMeasurement

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__obw_1ga5d87bc0b58f9ef55d6888683794f29d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__obw_1ga5d87bc0b58f9ef55d6888683794f29d2.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, floa

### RFmxWCDMA_OBWFetchMeasurement

Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| occupiedBandwidth | [out] | float64 * | This parameter returns the bandwidth containing 99% of the total integrated power of the acquired signal, around the center of the carriers. |
| absolutePower | [out] | float64 * | This parameter returns the carrier power integrated over a bandwidth of 5 MHz. This value is expressed in dBm. |
| startFrequency | [out] | float64 * | This parameter returns the start frequency of the Occupied Bandwidth parameter. |
| stopFrequency | [out] | float64 * | This parameter returns the stop frequency of the Occupied Bandwidth parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm.html language=enus -->
## TOPIC 00319: QEVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_QEVMFetchConstellationTraceFetches the complex chips of the composite corrected signal for the QEVM measurement. RFmxWCDMA_QEVMFetchConstellationTraceSplitFetches the complex chips of the composite corrected signal for the QEVM measurement. RFmxWCDMA_Q

### QEVM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_QEVMFetchConstellationTrace | Fetches the complex chips of the composite corrected signal for the QEVM measurement. |
| RFmxWCDMA_QEVMFetchConstellationTraceSplit | Fetches the complex chips of the composite corrected signal for the QEVM measurement. |
| RFmxWCDMA_QEVMFetchEVM | Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement. |
| RFmxWCDMA_QEVMFetchEVMTrace | Fetches the EVM trace for the QEVM measurement. |
| RFmxWCDMA_QEVMFetchIQImpairments | Fetches the mean and maximum I/Q origin offsets, I/Q gain imbalances, and I/Q quadrature errors for the QEVM measurement. |
| RFmxWCDMA_QEVMFetchMagnitudeErrorTrace | Fetches the magnitude error trace for the QEVM measurement. |
| RFmxWCDMA_QEVMFetchPhaseErrorTrace | Fetches the phase error trace for the QEVM measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga12dca64738a8a7fe403965455420ab51.html language=enus -->
## TOPIC 00320: RFmxWCDMA_QEVMFetchPhaseErrorTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga12dca64738a8a7fe403965455420ab51.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga12dca64738a8a7fe403965455420ab51.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace for the QEVM measurement. Syntaxint32 __stdcall RFmxWCDMA_QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirection

### RFmxWCDMA_QEVMFetchPhaseErrorTrace

Fetches the phase error trace for the QEVM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| phaseError | [out] | float32[] | This parameter returns an array of phase error values. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga2e3c721c571ef4a9d6be1613056668d9.html language=enus -->
## TOPIC 00321: RFmxWCDMA_QEVMFetchMagnitudeErrorTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga2e3c721c571ef4a9d6be1613056668d9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga2e3c721c571ef4a9d6be1613056668d9.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error trace for the QEVM measurement. Syntaxint32 __stdcall RFmxWCDMA_QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)ParametersN

### RFmxWCDMA_QEVMFetchMagnitudeErrorTrace

Fetches the magnitude error trace for the QEVM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| magnitudeError | [out] | float32[] | This parameter returns the magnitude error values. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7aa6a63bac7573d3f3bcdb3d87f1739a.html language=enus -->
## TOPIC 00322: RFmxWCDMA_QEVMFetchConstellationTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7aa6a63bac7573d3f3bcdb3d87f1739a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7aa6a63bac7573d3f3bcdb3d87f1739a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the complex chips of the composite corrected signal for the QEVM measurement. Syntaxint32 __stdcall RFmxWCDMA_QEVMFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)Param

### RFmxWCDMA_QEVMFetchConstellationTrace

Fetches the complex chips of the composite corrected signal for the QEVM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_QEVMFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellation | [out] | NIComplexSingle[] | This parameter returns an array of complex chips of the QPSK corrected signal for the last acquisition. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7eb928234537200426b525dcdd48558c.html language=enus -->
## TOPIC 00323: RFmxWCDMA_QEVMFetchEVMTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7eb928234537200426b525dcdd48558c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7eb928234537200426b525dcdd48558c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM trace for the QEVM measurement. Syntaxint32 __stdcall RFmxWCDMA_QEVMFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioninstrum

### RFmxWCDMA_QEVMFetchEVMTrace

Fetches the EVM trace for the QEVM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_QEVMFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| evm | [out] | float32[] | This parameter returns the EVM value. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7fe02ef84fbdaf4aa53aa227a1a55d83.html language=enus -->
## TOPIC 00324: RFmxWCDMA_QEVMFetchEVM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7fe02ef84fbdaf4aa53aa227a1a55d83.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__qevm_1ga7fe02ef84fbdaf4aa53aa227a1a55d83.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement. Syntaxint32 __stdcall RFmxWCDMA_QEVMFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorStri

### RFmxWCDMA_QEVMFetchEVM

Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_QEVMFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanRMSEVM, float64 *maximumPeakEVM, float64 *meanFrequencyError, float64 *meanMagnitudeError, float64 *meanPhaseError, float64 *meanChipRateError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanRMSEVM | [out] | float64 * | This parameter returns the mean of the RMS EVM values for a QPSK signal. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute. This value is expressed as a percentage.The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval. |
| maximumPeakEVM | [out] | float64 * | This parameter returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute.The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval. |
| meanFrequencyError | [out] | float64 * | This parameter returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz. This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute.The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal. |
| meanMagnitudeError | [out] | float64 * | This parameter returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute.The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. |
| meanPhaseError | [out] | float64 * | This parameter returns the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute.The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval. |
| meanChipRateError | [out] | float64 * | This parameter returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT attribute.The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem.html language=enus -->
## TOPIC 00325: SEM

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_SEMFetchCarrierMeasurementFetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power. RFmxWCDMA_SEMFetchCarrierMeasurementArrayFetches an arr

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_SEMFetchCarrierMeasurement | Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_SEMFetchCarrierMeasurementArray | Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power. |
| RFmxWCDMA_SEMFetchLowerOffsetMargin | Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_SEMFetchLowerOffsetMarginArray | Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_SEMFetchLowerOffsetPower | Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power. |
| RFmxWCDMA_SEMFetchLowerOffsetPowerArray | Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_SEMFetchMeasurementStatus | Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the 3GPP TS 34.121-1 specification, version 11.5.0, release 11. |
| RFmxWCDMA_SEMFetchSpectrum | Fetches the spectrum used for the SEM measurement. |
| RFmxWCDMA_SEMFetchTotalCarrierPower | Fetches the total carrier power for the SEM measurement. |
| RFmxWCDMA_SEMFetchUpperOffsetMargin | Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_SEMFetchUpperOffsetMarginArray | Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_SEMFetchUpperOffsetPower | Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power. |
| RFmxWCDMA_SEMFetchUpperOffsetPowerArray | Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. All relative powers are relative to the total carrier power. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga0441808599edb43d7f8dd1a9e183195a.html language=enus -->
## TOPIC 00326: RFmxWCDMA_SEMFetchUpperOffsetMargin

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga0441808599edb43d7f8dd1a9e183195a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga0441808599edb43d7f8dd1a9e183195a.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetMargin(niRFmx

### RFmxWCDMA_SEMFetchUpperOffsetMargin

Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxWCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter Indicates the measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute. |
| margin | [out] | float64 * | This parameter returns the margin of the upper offset segment.In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit in the upper offset segment is also measured. The higher value is the margin.In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is the margin.This value is expressed in dB. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurred in the upper, or positive, segment. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the upper, or positive, offset segmentThis value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr attribute.This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga2d6cf0313ff3caa37dc45f5e5a28f739.html language=enus -->
## TOPIC 00327: RFmxWCDMA_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga2d6cf0313ff3caa37dc45f5e5a28f739.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga2d6cf0313ff3caa37dc45f5e5a28f739.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. Syntaxint32 __s

### RFmxWCDMA_SEMFetchLowerOffsetPowerArray

Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns an array of the powers measured in the lower, or negative, offset segments. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns an array of powers measured in the lower, or negative, offset segments relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |
| absolutePeakPower | [out] | float64[] | This parameter returns an array of peak power values measured in the lower, or negative, offset segments. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns an array of frequencies corresponding to the lower offset segment peak power values. This value is expressed in Hz. |
| relativePeakPower | [out] | float64[] | This parameter returns an array of peak power values measured in the lower, or negative, offset segments relative to the SEM Results Total Carrier Pwr attribute. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga2feab491c3cab7802a06a6b2422f16e6.html language=enus -->
## TOPIC 00328: RFmxWCDMA_SEMFetchLowerOffsetPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga2feab491c3cab7802a06a6b2422f16e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga2feab491c3cab7802a06a6b2422f16e6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetPo

### RFmxWCDMA_SEMFetchLowerOffsetPower

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFrequency, float64 *relativePeakPower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxWCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the power measured in the lower, or negative, offset segment. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the power measured in the lower, or negative, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute.This value is expressed in dB. |
| absolutePeakPower | [out] | float64 * | This parameter returns the peak power measured in the lower, or negative, offset segment. This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency corresponding to the lower offset segment peak power. This value is expressed in Hz. |
| relativePeakPower | [out] | float64 * | This parameter returns the peak power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr attribute. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga34f9b78e514093b4d16cf48a2cde2a87.html language=enus -->
## TOPIC 00329: RFmxWCDMA_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga34f9b78e514093b4d16cf48a2cde2a87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga34f9b78e514093b4d16cf48a2cde2a87.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relati

### RFmxWCDMA_SEMFetchUpperOffsetMarginArray

Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns an array of measurement status values based on the values of the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN attribute corresponding to each upper offset segment. |
| margin | [out] | float64[] | This parameter returns an array of margins of the upper offset segments.In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit, in the upper offset segment, is also measured. The higher value is the margin.In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is the margin.This value is expressed in dB. |
| marginFrequency | [out] | float64[] | This parameter returns an array of frequencies corresponding to the SEM Results Upper Offset Margin attribute. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin attribute. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin attribute, relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga388f52cc6f78bdcfb5082ddd770964d3.html language=enus -->
## TOPIC 00330: RFmxWCDMA_SEMFetchTotalCarrierPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga388f52cc6f78bdcfb5082ddd770964d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga388f52cc6f78bdcfb5082ddd770964d3.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power for the SEM measurement. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis pa

### RFmxWCDMA_SEMFetchTotalCarrierPower

Fetches the total carrier power for the SEM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchTotalCarrierPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalCarrierPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalCarrierPower | [out] | float64 * | This parameter returns the sum of all active carrier powers, where each carrier power corresponds to the value of the RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER attribute. This value is expressed in dBm. For a single-carrier measurement, total carrier power is the same as carrier absolute power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga5a1fc92a59b11d952660126f7b72967f.html language=enus -->
## TOPIC 00331: RFmxWCDMA_SEMFetchUpperOffsetPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga5a1fc92a59b11d952660126f7b72967f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga5a1fc92a59b11d952660126f7b72967f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetPowe

### RFmxWCDMA_SEMFetchUpperOffsetPower

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFrequency, float64 *relativePeakPower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxWCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the power measured in the upper, or positive, offset segment. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the power measured in the upper, or positive, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |
| absolutePeakPower | [out] | float64 * | This parameter returns an array of peak power values measured in the lower, or negative, offset segments This value is expressed in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency corresponding to the upper offset segment peak power. This value is expressed in Hz. |
| relativePeakPower | [out] | float64 * | This parameter returns the peak power measured in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr attribute. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga8e9d976e121005424e880ead2ca70882.html language=enus -->
## TOPIC 00332: RFmxWCDMA_SEMFetchCarrierMeasurementArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga8e9d976e121005424e880ead2ca70882.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga8e9d976e121005424e880ead2ca70882.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char

### RFmxWCDMA_SEMFetchCarrierMeasurementArray

Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchCarrierMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns an array of carrier power values. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the RFMXWCDMA_ATTR_CENTER_FREQUENCY and RFMXWCDMA_ATTR_CARRIER_FREQUENCY attributes. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns an array of carrier power values relative to the total carrier power of all enabled carriers. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga973d6f6b09f64bb8e47df5039ab05e55.html language=enus -->
## TOPIC 00333: RFmxWCDMA_SEMFetchSpectrum

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga973d6f6b09f64bb8e47df5039ab05e55.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1ga973d6f6b09f64bb8e47df5039ab05e55.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the SEM measurement. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32 *actual

### RFmxWCDMA_SEMFetchSpectrum

Fetches the spectrum used for the SEM measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns an array of averaged powers measured at each frequency bin. The value is expressed in dBm. |
| relativeMask | [out] | float32[] | This parameter returns an array of averaged powers measured at each frequency bin. The value is expressed in dBm. |
| absoluteMask | [out] | float32[] | This parameter returns an array of averaged powers measured at each frequency bin. The value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gac6adb465dafd6fc1ac524d46f1887ae6.html language=enus -->
## TOPIC 00334: RFmxWCDMA_SEMFetchLowerOffsetMargin

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gac6adb465dafd6fc1ac524d46f1887ae6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gac6adb465dafd6fc1ac524d46f1887ae6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetMargin(niRFmx

### RFmxWCDMA_SEMFetchLowerOffsetMargin

Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxWCDMA_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter indicates the measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN attribute. |
| margin | [out] | float64 * | This parameter returns the margin of the lower offset segment. This value is expressed in dB.In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit in the lower offset segment is also measured. The higher value is the margin.In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is the margin. |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurred in the lower, or negative, offset segment. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the lower, or negative, offset segment.This value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the lower, or negative, offset segment relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute.This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gad6676a557a8fa21ae1f2ea3dab5b9660.html language=enus -->
## TOPIC 00335: RFmxWCDMA_SEMFetchMeasurementStatus

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gad6676a557a8fa21ae1f2ea3dab5b9660.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gad6676a557a8fa21ae1f2ea3dab5b9660.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the 3GPP TS 34.121-1 specification, version 11.5.0, release 11. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchMeasurementStatu

### RFmxWCDMA_SEMFetchMeasurementStatus

Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the *3GPP TS 34.121-1* specification, version 11.5.0, release 11.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter indicates the overall SEM measurement status based on the RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS and the RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS attributes.NameValueDescriptionRFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_FAIL0 (0x0)The measurement status of at least one offset segment has failed.RFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_PASS1 (0x1)The measurement status of all offset segments have passed. |
| Name | Value | Description |  |
| RFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_FAIL | 0 (0x0) | The measurement status of at least one offset segment has failed. |  |
| RFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_PASS | 1 (0x1) | The measurement status of all offset segments have passed. |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gadc1f18ccc2b053923e2ba260a5e55167.html language=enus -->
## TOPIC 00336: RFmxWCDMA_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gadc1f18ccc2b053923e2ba260a5e55167.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gadc1f18ccc2b053923e2ba260a5e55167.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total ca

### RFmxWCDMA_SEMFetchLowerOffsetMarginArray

Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter indicates an array of measurement status values based on the values of the SEM Results Lower Offset Margin attribute corresponding to each lower offset segment. |
| margin | [out] | float64[] | This parameter returns an array of margins of the lower offset segments. This value is expressed in dB.In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit, in the lower offset segment is also measured. The higher value is the margin.In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is the margin. |
| marginFrequency | [out] | float64[] | This parameter returns an array of frequencies at which the margins occurred in the lower, or negative, offset segments This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns an array of powers at which the margins occurred in the lower, or negative, offset segment.This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns an array of powers at which the margins occurred in the lower, or negative, offset segments relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gae456774f85032f3c0472e00d79a19cac.html language=enus -->
## TOPIC 00337: RFmxWCDMA_SEMFetchCarrierMeasurement

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gae456774f85032f3c0472e00d79a19cac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gae456774f85032f3c0472e00d79a19cac.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power. Syntaxint32 __stdcall RFmxWCDMA_SEMFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 tim

### RFmxWCDMA_SEMFetchCarrierMeasurement

Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchCarrierMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower)

#### Remarks

Use "carrier<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0".Example:"carrier0""signal::sig1/carrier0""result::r1/carrier0""signal::sig1/result::r1/carrier0"You can use the RFmxWCDMA_BuildCarrierString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the carrier power. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the RFMXWCDMA_ATTR_CENTER_FREQUENCY and RFMXWCDMA_ATTR_CARRIER_FREQUENCY attributes. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the carrier power relative to the total carrier power attribute. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gafbd1dc96c1ff34926ff03d4cee829095.html language=enus -->
## TOPIC 00338: RFmxWCDMA_SEMFetchUpperOffsetPowerArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gafbd1dc96c1ff34926ff03d4cee829095.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__sem_1gafbd1dc96c1ff34926ff03d4cee829095.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. A

### RFmxWCDMA_SEMFetchUpperOffsetPowerArray

Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. All relative powers are relative to the total carrier power.

#### Syntax

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns an array of the powers measured in the upper, or positive, offset segments. This value is expressed in dBm. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns an array of powers measured in the upper, or positive, offset segments relative to the RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER attribute. This value is expressed in dB. |
| absolutePeakPower | [out] | float64[] | This parameter returns an array of peak power values measured in the upper, or positive, offset segments. This value is expressed in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns an array of frequencies at which the peak power is observed in the upper, or positive, offset segments. This value is expressed in Hz. |
| relativePeakPower | [out] | float64[] | This parameter returns an array of peak power values measured in the upper, or positive, offset segments relative to the SEM Results Total Carrier Pwr attribute.This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase.html language=enus -->
## TOPIC 00339: SlotPhase

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_SlotPhaseFetchChipPhaseErrorLinearFitTraceFetches the chip phase error linear fit trace for the SlotPhase measurement. RFmxWCDMA_SlotPhaseFetchChipPhaseErrorTraceFetches the chip phase error trace for the SlotPhase measurement. RFmxWCDMA_SlotPhaseFetch

### SlotPhase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_SlotPhaseFetchChipPhaseErrorLinearFitTrace | Fetches the chip phase error linear fit trace for the SlotPhase measurement. |
| RFmxWCDMA_SlotPhaseFetchChipPhaseErrorTrace | Fetches the chip phase error trace for the SlotPhase measurement. |
| RFmxWCDMA_SlotPhaseFetchMeasurement | Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results. |
| RFmxWCDMA_SlotPhaseFetchPhaseDiscontinuities | Fetches the phase discontinuity values for the slot phase measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1ga87bd3507fc381762420f143da614eaed.html language=enus -->
## TOPIC 00340: RFmxWCDMA_SlotPhaseFetchPhaseDiscontinuities

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1ga87bd3507fc381762420f143da614eaed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1ga87bd3507fc381762420f143da614eaed.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase discontinuity values for the slot phase measurement. Syntaxint32 __stdcall RFmxWCDMA_SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32 *actualArraySize)ParametersNa

### RFmxWCDMA_SlotPhaseFetchPhaseDiscontinuities

Fetches the phase discontinuity values for the slot phase measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| slotPhaseDiscontinuity | [out] | float64[] | This parameter returns the difference between the first extrapolated linear chip phase of the current slot and the last extrapolated linear chip phase of the preceding slot. The extrapolation is for the exclusion period of 25us on either side of the slot boundary. If you set the RFMXWCDMA_ATTR_SLOTPHASE_TRANSIENT_REMOVAL_ENABLED attribute to False, this parameter returns the difference between the first and last linear chip phase, at each slot boundary. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1ga94135b86edb859261e6bb2a353e5b6a3.html language=enus -->
## TOPIC 00341: RFmxWCDMA_SlotPhaseFetchChipPhaseErrorTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1ga94135b86edb859261e6bb2a353e5b6a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1ga94135b86edb859261e6bb2a353e5b6a3.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace for the SlotPhase measurement. Syntaxint32 __stdcall RFmxWCDMA_SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chipPhaseError[], int32 arraySize, int32 *actualArraySize)

### RFmxWCDMA_SlotPhaseFetchChipPhaseErrorTrace

Fetches the chip phase error trace for the SlotPhase measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chipPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| chipPhaseError | [out] | float32[] | This parameter returns an array of phase error values. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1gab7b9c7f4cefd22405d2289ef80c087ef.html language=enus -->
## TOPIC 00342: RFmxWCDMA_SlotPhaseFetchMeasurement

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1gab7b9c7f4cefd22405d2289ef80c087ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1gab7b9c7f4cefd22405d2289ef80c087ef.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results. Syntaxint32 __stdcall RFmxWCDMA_SlotPhaseFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeou

### RFmxWCDMA_SlotPhaseFetchMeasurement

Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results.

#### Syntax

int32 __stdcall RFmxWCDMA_SlotPhaseFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumPhaseDiscontinuity, int32 *discontinuityCountGreaterThanLimit1, int32 *discontinuityCountGreaterThanLimit2, int32 *discontinuityMinimumDistance)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumPhaseDiscontinuity | [out] | float64 * | This parameter returns the maximum of all the measured phase discontinuity values at the slot boundaries.This value is expressed in degrees. |
| discontinuityCountGreaterThanLimit1 | [out] | int32 * | This parameter returns the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. |
| discontinuityCountGreaterThanLimit2 | [out] | int32 * | This parameter returns the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. |
| discontinuityMinimumDistance | [out] | int32 * | This parameter returns the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots.If there are no phase discontinuity values greater than Limit 1, or if there is only one phase discontinuity value greater than Limit 1, this result is not valid. In such a case, -1 is reported as the result. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1gaefb3835245f0cda2786bd1499890b38d.html language=enus -->
## TOPIC 00343: RFmxWCDMA_SlotPhaseFetchChipPhaseErrorLinearFitTrace

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1gaefb3835245f0cda2786bd1499890b38d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotphase_1gaefb3835245f0cda2786bd1499890b38d.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error linear fit trace for the SlotPhase measurement. Syntaxint32 __stdcall RFmxWCDMA_SlotPhaseFetchChipPhaseErrorLinearFitTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chipPhaseErrorLinearFit[], int32 array

### RFmxWCDMA_SlotPhaseFetchChipPhaseErrorLinearFitTrace

Fetches the chip phase error linear fit trace for the SlotPhase measurement.

#### Syntax

int32 __stdcall RFmxWCDMA_SlotPhaseFetchChipPhaseErrorLinearFitTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chipPhaseErrorLinearFit[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| chipPhaseErrorLinearFit | [out] | float32[] | This parameter returns the linear-fit chip phase error values. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotpower.html language=enus -->
## TOPIC 00344: SlotPower

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotpower.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_SlotPowerFetchPowersFetches the Slot Power and Slot Power delta for all the slots in the measurement length. AttachmentsNone

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_SlotPowerFetchPowers | Fetches the Slot Power and Slot Power delta for all the slots in the measurement length. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotpower_1ga14c7fce9f0a1e7121c8c03a7cc003111.html language=enus -->
## TOPIC 00345: RFmxWCDMA_SlotPowerFetchPowers

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotpower_1ga14c7fce9f0a1e7121c8c03a7cc003111.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__fetch__slotpower_1ga14c7fce9f0a1e7121c8c03a7cc003111.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the Slot Power and Slot Power delta for all the slots in the measurement length. Syntaxint32 __stdcall RFmxWCDMA_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32 *actualArray

### RFmxWCDMA_SlotPowerFetchPowers

Fetches the Slot Power and Slot Power delta for all the slots in the measurement length.

#### Syntax

int32 __stdcall RFmxWCDMA_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the time for which the function waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| slotPower | [out] | float64[] | This parameter returns an array of slot powers. This value is expressed in dBm. |
| slotPowerDelta | [out] | float64[] | This parameter returns an array of differences in powers between the adjacent slots. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__select__measurement.html language=enus -->
## TOPIC 00346: Select Measurement

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__select__measurement.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__select__measurement_1ga3142f34fcc97690ef5840ce1dd419718.html language=enus -->
## TOPIC 00347: RFmxWCDMA_SelectMeasurements

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__select__measurement_1ga3142f34fcc97690ef5840ce1dd419718.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__select__measurement_1ga3142f34fcc97690ef5840ce1dd419718.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxWCDMA_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescrip

### RFmxWCDMA_SelectMeasurements

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxWCDMA_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Example:"signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurements to perform. You can specify one or more of the following measurements. The default is an empty array.Name (Value)DescriptionModAcc (0)Enables the ModAcc measurement.ACP (1)Enables the ACP measurement.CHP (2)Enables the CHP measurement.OBW (3)Enables the OBW measurement.SEM (4)Enables the SEM measurement.QEVM (5)Enables the QEVM measurement.SlotPhase (6)Enables the SlotPhase measurement.CDA (7)Enables the CDA measurement.SlotPower (8)Enables the SlotPower measurement. |
| Name (Value) | Description |  |  |
| ModAcc (0) | Enables the ModAcc measurement. |  |  |
| ACP (1) | Enables the ACP measurement. |  |  |
| CHP (2) | Enables the CHP measurement. |  |  |
| OBW (3) | Enables the OBW measurement. |  |  |
| SEM (4) | Enables the SEM measurement. |  |  |
| QEVM (5) | Enables the QEVM measurement. |  |  |
| SlotPhase (6) | Enables the SlotPhase measurement. |  |  |
| CDA (7) | Enables the CDA measurement. |  |  |
| SlotPower (8) | Enables the SlotPower measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurements. The default value is FALSE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00348: Set and Get Attributes

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes.html
- document_id: `rfmxwcdma-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00349: Get Attributes

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxWCDMA_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffe

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxWCDMA_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxWCDMA_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxWCDMA_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxWCDMA_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxWCDMA_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxWCDMA_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxWCDMA_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxWCDMA_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxWCDMA_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxWCDMA_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga034288a97876b7208f9123527175a986.html language=enus -->
## TOPIC 00350: RFmxWCDMA_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga034288a97876b7208f9123527175a986.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga034288a97876b7208f9123527175a986.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxWCDMA_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga059cc9d63372f631dec1195a267d8714.html language=enus -->
## TOPIC 00351: RFmxWCDMA_GetAttributeI16

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga059cc9d63372f631dec1195a267d8714.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga059cc9d63372f631dec1195a267d8714.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxWCDMA_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga09450b23de761be3906c156474488269.html language=enus -->
## TOPIC 00352: RFmxWCDMA_GetAttributeF64Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga09450b23de761be3906c156474488269.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga09450b23de761be3906c156474488269.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxWCDMA_GetAttributeF64Array

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga2283213a7784cee4c605b52d2691cf9b.html language=enus -->
## TOPIC 00353: RFmxWCDMA_GetAttributeF32Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga2283213a7784cee4c605b52d2691cf9b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga2283213a7784cee4c605b52d2691cf9b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxWCDMA_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga250ee6557c7e46f308b75d9bddd54442.html language=enus -->
## TOPIC 00354: RFmxWCDMA_GetAttributeI8

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga250ee6557c7e46f308b75d9bddd54442.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga250ee6557c7e46f308b75d9bddd54442.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxWCDMA_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga3ad11be68f99353023ca77dac5ae8760.html language=enus -->
## TOPIC 00355: RFmxWCDMA_GetAttributeU8Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga3ad11be68f99353023ca77dac5ae8760.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga3ad11be68f99353023ca77dac5ae8760.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxWCDMA_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga3cd0736ee09d9c61368bcb5e79355421.html language=enus -->
## TOPIC 00356: RFmxWCDMA_GetAttributeI32Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga3cd0736ee09d9c61368bcb5e79355421.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga3cd0736ee09d9c61368bcb5e79355421.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxWCDMA_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga55bb1b2f462a71e14afaaaa1884a7452.html language=enus -->
## TOPIC 00357: RFmxWCDMA_GetAttributeU32

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga55bb1b2f462a71e14afaaaa1884a7452.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga55bb1b2f462a71e14afaaaa1884a7452.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxWCDMA_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga5c07e36b7b197b806625b7ee2d383e44.html language=enus -->
## TOPIC 00358: RFmxWCDMA_GetAttributeU8

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga5c07e36b7b197b806625b7ee2d383e44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga5c07e36b7b197b806625b7ee2d383e44.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxWCDMA_GetAttributeU8

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga64a5f910a390a48dba86c028c87959ee.html language=enus -->
## TOPIC 00359: RFmxWCDMA_GetAttributeI64

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga64a5f910a390a48dba86c028c87959ee.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga64a5f910a390a48dba86c028c87959ee.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxWCDMA_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6552db68ce6d3e35a1155dcb7714d52b.html language=enus -->
## TOPIC 00360: RFmxWCDMA_GetAttributeI8Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6552db68ce6d3e35a1155dcb7714d52b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6552db68ce6d3e35a1155dcb7714d52b.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxWCDMA_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6f5931d538d2bafa9753f660420e660c.html language=enus -->
## TOPIC 00361: RFmxWCDMA_GetAttributeF64

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6f5931d538d2bafa9753f660420e660c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga6f5931d538d2bafa9753f660420e660c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxWCDMA_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga8feb0b33fd55eaa65aa26f2156af18b0.html language=enus -->
## TOPIC 00362: RFmxWCDMA_GetAttributeString

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga8feb0b33fd55eaa65aa26f2156af18b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga8feb0b33fd55eaa65aa26f2156af18b0.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxWCDMA_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga9203a4a28178e944e83ac366887f9fcf.html language=enus -->
## TOPIC 00363: RFmxWCDMA_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga9203a4a28178e944e83ac366887f9fcf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga9203a4a28178e944e83ac366887f9fcf.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxWCDMA_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga936ed6ee739214912173866e92abf8e1.html language=enus -->
## TOPIC 00364: RFmxWCDMA_GetAttributeI32

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga936ed6ee739214912173866e92abf8e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga936ed6ee739214912173866e92abf8e1.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx s

### RFmxWCDMA_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga9e22a8b72c57c5b9f9de0c8b214c64cd.html language=enus -->
## TOPIC 00365: RFmxWCDMA_GetAttributeU16

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga9e22a8b72c57c5b9f9de0c8b214c64cd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1ga9e22a8b72c57c5b9f9de0c8b214c64cd.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies

### RFmxWCDMA_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaae20c75302618b2726c4e58ac32b770c.html language=enus -->
## TOPIC 00366: RFmxWCDMA_GetAttributeI64Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaae20c75302618b2726c4e58ac32b770c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaae20c75302618b2726c4e58ac32b770c.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxWCDMA_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaf317ab7659575f3771252a869f7d9e02.html language=enus -->
## TOPIC 00367: RFmxWCDMA_GetAttributeU64Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaf317ab7659575f3771252a869f7d9e02.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gaf317ab7659575f3771252a869f7d9e02.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxWCDMA_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gafee369d5ade505e03270bcdf35325886.html language=enus -->
## TOPIC 00368: RFmxWCDMA_GetAttributeF32

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gafee369d5ade505e03270bcdf35325886.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__get__attributes_1gafee369d5ade505e03270bcdf35325886.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxWCDMA_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIde

### RFmxWCDMA_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga184a184821b1a8ef2a011c1dcad37a7f.html language=enus -->
## TOPIC 00369: RFmxWCDMA_SetAttributeI64Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga184a184821b1a8ef2a011c1dcad37a7f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga184a184821b1a8ef2a011c1dcad37a7f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorStrin

### RFmxWCDMA_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga212f627ae457f420103a867bf9bd6759.html language=enus -->
## TOPIC 00370: RFmxWCDMA_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga212f627ae457f420103a867bf9bd6759.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga212f627ae457f420103a867bf9bd6759.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxWCDMA_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga3082db947e6fd9dc3826d8aaf6ab7762.html language=enus -->
## TOPIC 00371: RFmxWCDMA_SetAttributeF32Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga3082db947e6fd9dc3826d8aaf6ab7762.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga3082db947e6fd9dc3826d8aaf6ab7762.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, ch

### RFmxWCDMA_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga40bf192880a326fc14cfca3cae7f84db.html language=enus -->
## TOPIC 00372: RFmxWCDMA_SetAttributeF32

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga40bf192880a326fc14cfca3cae7f84db.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga40bf192880a326fc14cfca3cae7f84db.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentif

### RFmxWCDMA_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga5e750417c8a2a709e5c83ca53809bff5.html language=enus -->
## TOPIC 00373: RFmxWCDMA_SetAttributeI8Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga5e750417c8a2a709e5c83ca53809bff5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga5e750417c8a2a709e5c83ca53809bff5.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[]

### RFmxWCDMA_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga6a1f33bf3ed5ccc6f1bc4cf922076b23.html language=enus -->
## TOPIC 00374: RFmxWCDMA_SetAttributeString

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga6a1f33bf3ed5ccc6f1bc4cf922076b23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga6a1f33bf3ed5ccc6f1bc4cf922076b23.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can

### RFmxWCDMA_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga76911c3699715493524e17bf7a420abe.html language=enus -->
## TOPIC 00375: RFmxWCDMA_SetAttributeU16

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga76911c3699715493524e17bf7a420abe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga76911c3699715493524e17bf7a420abe.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxWCDMA_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga790c2d42ed56e061ccd50557931902d3.html language=enus -->
## TOPIC 00376: RFmxWCDMA_SetAttributeU32

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga790c2d42ed56e061ccd50557931902d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga790c2d42ed56e061ccd50557931902d3.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxWCDMA_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga876820e5e3c98f223d01565dbe33424f.html language=enus -->
## TOPIC 00377: RFmxWCDMA_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga876820e5e3c98f223d01565dbe33424f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga876820e5e3c98f223d01565dbe33424f.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selector

### RFmxWCDMA_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga8b201d31340425b2db97f337a2052d00.html language=enus -->
## TOPIC 00378: RFmxWCDMA_SetAttributeU8

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga8b201d31340425b2db97f337a2052d00.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga8b201d31340425b2db97f337a2052d00.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFm

### RFmxWCDMA_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga9347ea1b225fb8433e7052543095a8ef.html language=enus -->
## TOPIC 00379: RFmxWCDMA_SetAttributeF64Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga9347ea1b225fb8433e7052543095a8ef.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1ga9347ea1b225fb8433e7052543095a8ef.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, ch

### RFmxWCDMA_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gadb24970a351de192e641cf5348c176b6.html language=enus -->
## TOPIC 00380: RFmxWCDMA_SetAttributeU64Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gadb24970a351de192e641cf5348c176b6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gadb24970a351de192e641cf5348c176b6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxWCDMA_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gae36f8aa96bd7cc9a705406f99ea64693.html language=enus -->
## TOPIC 00381: RFmxWCDMA_SetAttributeU32Array

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gae36f8aa96bd7cc9a705406f99ea64693.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gae36f8aa96bd7cc9a705406f99ea64693.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char sel

### RFmxWCDMA_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gae6fc7383bc4e776fdba481006c259acf.html language=enus -->
## TOPIC 00382: RFmxWCDMA_SetAttributeI64

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gae6fc7383bc4e776fdba481006c259acf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gae6fc7383bc4e776fdba481006c259acf.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sessi

### RFmxWCDMA_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gafbcc3ba777ce64b7822d3778707ef123.html language=enus -->
## TOPIC 00383: RFmxWCDMA_SetAttributeI8

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gafbcc3ba777ce64b7822d3778707ef123.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__set__and__get__attributes__set__attributes_1gafbcc3ba777ce64b7822d3778707ef123.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxWCDMA_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxWCDMA_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxWCDMA_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__utility.html language=enus -->
## TOPIC 00384: Utility

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__utility.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxWCDMA_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxWCDMA_CommitCommits settings to the h

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxWCDMA_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxWCDMA_Commit | Commits settings to the hardware. Calling this function is optional. RFmxWCDMA commits settings to the hardware when you call the RFmxWCDMA_Initiate function. |
| RFmxWCDMA_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxWCDMA_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxWCDMA_ResetToDefault | Resets a signal to the default values. |
| RFmxWCDMA_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxWCDMA_WaitForMeasurementComplete | Waits for the specified number of seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga6c7f46a88aa573fca679405abe6c0be6.html language=enus -->
## TOPIC 00385: RFmxWCDMA_ResetAttribute

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga6c7f46a88aa573fca679405abe6c0be6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga6c7f46a88aa573fca679405abe6c0be6.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an attribute that you specify in the attributeID parameter to default values. Syntaxint32 __stdcall RFmxWCDMA_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the R

### RFmxWCDMA_ResetAttribute

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Syntax

int32 __stdcall RFmxWCDMA_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being reset. Refer to the Selector String (C or LabWindows/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga818e842a3ad83d8e592de9b7f007b254.html language=enus -->
## TOPIC 00386: RFmxWCDMA_WaitForAcquisitionComplete

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga818e842a3ad83d8e592de9b7f007b254.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga818e842a3ad83d8e592de9b7f007b254.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxWCDMA_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instrum

### RFmxWCDMA_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxWCDMA_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxWCDMA_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwcdma-c-api-ref path=group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga8668dd75d5b6b2f554b79069010c82fa.html language=enus -->
## TOPIC 00387: RFmxWCDMA_CheckMeasurementStatus

- bundle_id: `rfmxwcdma-c-api-ref`
- source_path: `group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga8668dd75d5b6b2f554b79069010c82fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_w_c_d_m_a__functions__utility_1ga8668dd75d5b6b2f554b79069010c82fa.html
- document_id: `rfmxwcdma-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxWCDMA_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxWCDMA_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxWCDMA_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *done)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Example:"signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxWCDMA_BuildSignalString function to build the selector string. |
| done | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxWCDMA_GetError](group____root__ni_r_fmx_w_c_d_m_a__functions_1gae254427b2bb10313f22e504c2b5eec7d.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility
